from dotenv import load_dotenv
from fastapi import FastAPI

# Load the .env file from the project root
# You must ensure that the load_dotenv call happens before the application imports any module
# that relies on those environment variables (i.e., your router files).
load_dotenv(dotenv_path="../../.env")

# Import Routers *AFTER* the environment is loaded
from routers import events, collections, blog_posts, blog_taxonomies, members, event

# Initialize App
app = FastAPI(
    title="Wix Data Fetcher",
    description="A service to fetch data from Wix HTTP functions and store it locally.",
)

# Include Routers
app.include_router(events.router)
app.include_router(collections.router)
app.include_router(blog_posts.router)
app.include_router(blog_taxonomies.router)
app.include_router(members.router)
app.include_router(event.router)
