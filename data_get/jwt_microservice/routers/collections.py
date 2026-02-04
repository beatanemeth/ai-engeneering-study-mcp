# routes/collections.py
import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Collections"],
)

# Configuration
JWT_SUBJECT = os.environ.get("JWT_SUBJECT_COLLECTIONS")
WIX_ENDPOINT = os.environ.get("WIX_COLLECTIONS_ENDPOINT")
COLLECTION_ARTICLES = "articles"
COLLECTION_ARTICLES_CATEGORY = "articles-category"
LOCAL_PATH_ARTICLES = "wix_articles_data.json"
LOCAL_PATH_ARTICLES_CATEGORY = "wix_articles-category_data.json"


@router.get("/collections/{collection}")
async def download_collections_(collection: str):
    """
    Determines which collection to fetch based on the URL path.
    """
    if collection == COLLECTION_ARTICLES:
        local_path = LOCAL_PATH_ARTICLES
    elif collection == COLLECTION_ARTICLES_CATEGORY:
        local_path = LOCAL_PATH_ARTICLES_CATEGORY
    else:
        return {"error": "Invalid collection type"}

    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=f"{WIX_ENDPOINT}?coll={collection}",
        local_path=local_path,
        data_type=collection.capitalize(),
    )
