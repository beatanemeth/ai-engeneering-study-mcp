# routes/events.py
import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Events"],
)

# Configuration
JWT_SUBJECT = os.environ.get("JWT_SUBJECT_EVENTS")
WIX_ENDPOINT = os.environ.get("WIX_EVENTS_ENDPOINT")
LOCAL_PATH = "wix_events_data.json"
DATA_TYPE = "Events"


@router.get("/events")
async def download_events():
    """
    Calls the generalized data fetch utility for Events data.
    """
    print(f"DEBUG: Endpoint being used: {WIX_ENDPOINT}")
    print(f"DEBUG: JWT Subject: {JWT_SUBJECT}")

    result = await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=WIX_ENDPOINT,
        local_path=LOCAL_PATH,
        data_type=DATA_TYPE,
    )

    # Access the 'count' key inside the result dictionary
    if isinstance(result, dict) and "count" in result:
        print(f"DEBUG: Successfully processed {result['count']} items.")
    else:
        print(f"DEBUG: Request failed or returned unexpected format.")

    return result
