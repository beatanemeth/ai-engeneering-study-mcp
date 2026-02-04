# routes/members.py
import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Members"],
)

# Configuration
JWT_SUBJECT = os.environ.get("JWT_SUBJECT_MEMBERS")
WIX_ENDPOINT = os.environ.get("WIX_MEMBERS_ENDPOINT")
LOCAL_PATH = "wix_members_data.json"
DATA_TYPE = "Members"


@router.get("/members")
async def download_members():
    """
    Calls the generalized data fetch utility for Members data.
    """
    print(f"DEBUG: Endpoint being used: {WIX_ENDPOINT}")
    print(f"DEBUG: JWT Subject: {JWT_SUBJECT}")

    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=WIX_ENDPOINT,
        local_path=LOCAL_PATH,
        data_type=DATA_TYPE,
    )
