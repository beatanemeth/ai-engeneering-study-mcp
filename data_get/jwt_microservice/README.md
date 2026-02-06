# FastAPI/JWT Microservice

This microservice contains a simple **FastAPI** application that

- generates **JSON Web Tokens** (JWTs),
- fetches protected data from Wix APIs, and
- stores the downloaded **JSON** files to the `/data `directory (_relative to the project root_) for downstream processing.

> If you only want to run this microservice independently, follow the steps below.

## Getting Started 🚀

### 1. Set Up Python Virtual Environment

Ensure you have initialized your virtual environment as described in the **root `README.md`**.

### 2. Configuration (`.env`)

1. In the root directory of this project, rename the `.env.example` to `.env`.
2. Populate the file with your environmental keys:

```bash
WIX_AUTH_SECRET=your_wix_auth_secret_here

# JWT Subjects
JWT_SUBJECT_EVENTS=REPLACE-ME-EVENTS-JWT-SUB
JWT_SUBJECT_POSTS=REPLACE-ME-POSTS-JWT-SUB
...

# Wix Endpoints
WIX_EVENTS_ENDPOINT=https://www.yourdomain.com/_functions/yourEventsEndpoint
...
```

⚠️ **Security Tip**: Never commit your `.env` file to version control.

### 3. Install Dependencies

With the virtual environment active, install all necessary packages in a single command.

```Bash
# Navigate to the Directory
cd data_get/jwt_microservice/

# Update pip
python -m pip install --upgrade pip

# Install the Packages
pip install -r requirements.txt
```

ℹ️ The `requirements.txt` file contains _all dependencies required_ to run the service: `fastapi`, `uvicorn`, `requests`, `pyjwt`, `python-dotenv`.

## Run the Application ▶️

This process requires two terminal windows:

- one to host the server and
- one to trigger the data fetch.

### Terminal_1: Run the Service

```Bash
# Navigate to the Microservice Directory
cd data_get/jwt_microservice/

# Launch the Uvicorn server
uvicorn main:app --reload
```

_The server will automatically load your secrets from the `.env` file._ **_Keep this terminal open._**

---

### Terminal_2: Call the Endpoint:

Open a second terminal to call the endpoints. This triggers

- the microservice to generate a JWT,
- fetch data from Wix, and
- save it locally.

You must activate the environment here as well to access the project utilities, though `curl` is system-level. The service runs on `http://127.0.0.1:8000` by default.

```Bash
# Activate the Environment
source .venv/bin/activate

# Execute the `curl` Command to Call an Endpoint
curl http://127.0.0.1:8000/events
```

If successful, the downloaded file (e.g., `wix_events_data.json`) will be saved to your project's `/data `directory (relative to your project root).

Available endpoints:

```Bash
# Download events
curl http://127.0.0.1:8000/events

# Download blog posts
curl http://127.0.0.1:8000/blog/posts

# Download blog categories
curl http://127.0.0.1:8000/blog/categories

# Download blog tags
curl http://127.0.0.1:8000/blog/tags

# Download collection with articles
curl http://127.0.0.1:8000/collection/articles

# Download collection with articles' categories
curl http://127.0.0.1:8000/collection/articles-category

# Download members
curl http://127.0.0.1:8000/members
```

## Shutting Down 🛑

### Terminal_1: Stop the Server

Stop the server by pressing `Ctrl + C` (Control + C) on your keyboard. This shuts down the Uvicorn server.

### Terminal_1 & Terminal_2: Exit the Environment

When you are finished, exit the isolated environment in both terminals:

```Bash
deactivate
```

Your command prompt will return to its default state, and the environment name (`.venv`) will disappear.
