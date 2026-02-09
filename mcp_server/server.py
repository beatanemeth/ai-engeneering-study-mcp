from fastmcp import FastMCP
import pandas as pd
import json
from pathlib import Path
from typing import Optional, Union

mcp = FastMCP("InsightHub-Server")
BASE_DIR = Path(__file__).resolve().parent


# --- GLOBAL HELPER: Load and Prepare Data ---
def load_prepared_data(
    filename: str, original_date_col: str, nested_col: Optional[str] = None
):
    path = BASE_DIR.parent / "data_prepared" / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Handle nested columns (guests/metrics) if they exist
    if nested_col and nested_col in df.columns:
        nested_df = pd.json_normalize(df[nested_col])
        nested_df.columns = [f"{nested_col}_{c}" for c in nested_df.columns]
        df = pd.concat([df.drop(columns=[nested_col]), nested_df], axis=1)

    # Standardize the date column name to 'date' for ALL DataFrames internally
    df["date"] = pd.to_datetime(df[original_date_col], errors="coerce")
    return df


# --- INITIALIZE DATA ---
events_df = load_prepared_data("events.json", "date", "eventGuests")
articles_df = load_prepared_data("articles.json", "publishedDate")
blog_posts_df = load_prepared_data("blog_posts.json", "publishedDate", "metrics")

# --- GLOBAL CONFIG & MAPS ---
MONTH_MAP = {
    "január": 1,
    "jan": 1,
    "február": 2,
    "feb": 2,
    "március": 3,
    "már": 3,
    "április": 4,
    "ápr": 4,
    "május": 5,
    "máj": 5,
    "június": 6,
    "jún": 6,
    "július": 7,
    "júl": 7,
    "augusztus": 8,
    "aug": 8,
    "szeptember": 9,
    "szept": 9,
    "október": 10,
    "okt": 10,
    "november": 11,
    "nov": 11,
    "december": 12,
    "dec": 12,
}


def resolve_month(month_val: Optional[Union[int, str]]):
    if month_val is None:
        return None, "Full Year"
    if isinstance(month_val, str):
        num = MONTH_MAP.get(month_val.lower().replace(".", ""), None)
        return num, month_val
    return month_val, str(month_val)


# ---------- AGGREGATOR TOOLS ----------
@mcp.tool()
def get_events_count(
    year_val: int, month_val: Optional[Union[int, str]] = None
) -> dict:
    """Returns the count of events for a specific year and optional month."""
    month_num, month_name = resolve_month(month_val)
    if month_val and not month_num:
        return {"error": f"Invalid month name: {month_val}"}

    mask = events_df["date"].dt.year == year_val
    if month_num:
        mask = mask & (events_df["date"].dt.month == month_num)

    return {
        "year": year_val,
        "month": month_name,
        "events_count": int(len(events_df[mask])),
    }


@mcp.tool()
def get_articles_count(
    year_val: int, month_val: Optional[Union[int, str]] = None
) -> dict:
    """Returns the count of articles for a specific year and optional month."""
    month_num, month_name = resolve_month(month_val)
    if month_val and not month_num:
        return {"error": f"Invalid month name: {month_val}"}

    mask = articles_df["date"].dt.year == year_val
    if month_num:
        mask = mask & (articles_df["date"].dt.month == month_num)

    return {
        "year": year_val,
        "month": month_name,
        "articles_count": int(len(articles_df[mask])),
    }


@mcp.tool()
def get_blog_posts_count(
    year_val: int, month_val: Optional[Union[int, str]] = None
) -> dict:
    """Returns the count of blog posts for a specific year and optional month."""
    month_num, month_name = resolve_month(month_val)
    if month_val and not month_num:
        return {"error": f"Invalid month name: {month_val}"}

    mask = blog_posts_df["date"].dt.year == year_val
    if month_num:
        mask = mask & (blog_posts_df["date"].dt.month == month_num)

    return {
        "year": year_val,
        "month": month_name,
        "blog_posts_count": int(len(blog_posts_df[mask])),
    }


@mcp.tool()
def get_total_events_count() -> dict:
    """Returns the total number of events in the database across all time."""
    return {"total_events": int(len(events_df))}


@mcp.tool()
def get_events_by_location(year_val: Optional[int] = None) -> dict:
    """Returns the count of ONLINE vs VENUE events."""
    df_filtered = events_df
    if year_val:
        df_filtered = events_df[events_df["date"].dt.year == year_val]

    online_count = int((df_filtered["location"] == "ONLINE").sum())
    venue_count = int((df_filtered["location"] == "VENUE").sum())

    return {
        "year": year_val if year_val else "All Time",
        "online_count": online_count,
        "venue_count": venue_count,
        "total": online_count + venue_count,
    }


# ---------- ANALYST TOOLS ----------
@mcp.tool()
def get_attendance_stats(
    year_val: Optional[int] = None, category: Optional[str] = None
) -> dict:
    """Calculates total attendance and identifies the most popular (star) event."""
    df_filtered = events_df.copy()

    if year_val:
        df_filtered = df_filtered[df_filtered["date"].dt.year == year_val]
    if category:
        df_filtered = df_filtered[df_filtered["categories"] == category]

    if df_filtered.empty:
        return {"message": "No data found for the given filters."}

    total_participants = int(df_filtered["eventGuests_going"].sum())
    star_event_idx = df_filtered["eventGuests_total"].idxmax()
    star_event = df_filtered.loc[star_event_idx]

    return {
        "filter_year": year_val if year_val else "All Time",
        "filter_category": category if category else "All Categories",
        "total_attendance": total_participants,
        "star_event": {
            "title": star_event["title"],
            "attendance": int(star_event["eventGuests_total"]),
            "date": str(star_event["date"].date()),
            "location": star_event["location"],
        },
    }


@mcp.tool()
def get_blog_stats(
    year_val: Optional[int] = None,
    category: Optional[str] = None,
    tag: Optional[str] = None,
) -> dict:
    """
    Retrieves analytical data for blog posts, including frequency and timing.

    Use this tool to answer:
    - How many blog posts were published (total_posts).
    - Which month or time of year was the most active/busiest (monthly_distribution).
    - What are the titles of recent or relevant posts (sample_titles).

    The monthly_distribution return value maps month numbers (1-12) to the count of posts.
    """
    df_filtered = blog_posts_df.copy()

    if year_val:
        df_filtered = df_filtered[df_filtered["date"].dt.year == year_val]
    if category:
        df_filtered = df_filtered[
            df_filtered["categories"].apply(
                lambda x: category in x if isinstance(x, list) else category == x
            )
        ]
    if tag:
        df_filtered = df_filtered[
            df_filtered["tags"].apply(
                lambda x: tag in x if isinstance(x, list) else tag == x
            )
        ]

    if df_filtered.empty:
        return {"message": "No blog posts found for these filters."}

    monthly_counts = df_filtered["date"].dt.month.value_counts().sort_index().to_dict()

    return {
        "total_posts": len(df_filtered),
        "filter_year": year_val if year_val else "All Time",
        "monthly_distribution": monthly_counts,
        "sample_titles": df_filtered["title"].head(5).tolist(),
    }


# ---------- THEMATIC FINDER TOOLS ----------
@mcp.tool()
def list_blog_metadata() -> dict:
    """Returns unique tags and categories from blog posts."""
    all_cats = set()
    blog_posts_df["categories"].apply(
        lambda x: all_cats.update(x) if isinstance(x, list) else all_cats.add(x)
    )

    all_tags = set()
    blog_posts_df["tags"].apply(
        lambda x: all_tags.update(x) if isinstance(x, list) else all_tags.add(x)
    )

    return {
        "unique_categories": sorted(list(all_cats)),
        "unique_tags": sorted(list(all_tags)),
        "total_tag_count": len(all_tags),
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
