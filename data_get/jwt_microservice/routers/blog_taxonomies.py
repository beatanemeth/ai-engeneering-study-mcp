# routes/taxonomies.py
import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Taxonomies"],
)

# Configuration
JWT_SUBJECT = os.environ.get("JWT_SUBJECT_BLOG_TAXONOMIES")
WIX_ENDPOINT = os.environ.get("WIX_BLOG_TAXONOMIES_ENDPOINT")
TAXONOMY_TYPE_CATEGORIES = "categories"
TAXONOMY_TYPE_TAGS = "tags"
LOCAL_PATH_CATEGORIES = "wix_blog_categories_data.json"
LOCAL_PATH_TAGS = "wix_blog_tags_data.json"


@router.get("/blog/{taxonomy_type}")
async def download_blog_taxonomies_(taxonomy_type: str):
    """
    Determines which collection to fetch based on the URL path.
    """

    print(f"DEBUG: Endpoint being used: {WIX_ENDPOINT}")
    print(f"DEBUG: JWT Subject: {JWT_SUBJECT}")

    if taxonomy_type == TAXONOMY_TYPE_CATEGORIES:
        local_path = LOCAL_PATH_CATEGORIES
    elif taxonomy_type == TAXONOMY_TYPE_TAGS:
        local_path = LOCAL_PATH_TAGS
    else:
        return {"error": "Invalid taxonomy type"}

    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=f"{WIX_ENDPOINT}?tax={taxonomy_type}",
        local_path=local_path,
        data_type=taxonomy_type.capitalize(),
    )
