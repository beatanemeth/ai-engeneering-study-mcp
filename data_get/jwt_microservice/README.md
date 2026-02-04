# FastAPI/JWT Microservice

> In case, that you only would like to use this service, follow the steps bellow for the installation.

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
pip install fastapi uvicorn requests pyjwt python-dotenv
```

## Run the Application ▶️

This process requires two terminal windows: one to host the server and one to trigger the data fetch.

### Terminal_1: Run the Service

1. #### Navigate to the Microservice Directory

```Bash
cd data_get/jwt_microservice/
```

2. #### Launch the Uvicorn server

```Bash
uvicorn main:app --reload
```

_The server will automatically load your secrets from the `.env` file._ **_Keep this terminal open._**

---

### Terminal_2: Call the Endpoint:

Open a second terminal to call the endpoints. This triggers the microservice to generate a JWT, fetch data from Wix, and save it locally.

1. #### Activate the Environment
   You must activate the environment here as well to access the project utilities, though curl is system-level.

```Bash
source .venv/bin/activate
```

2. #### Execute the Request
   Execute the `curl` command to call an endpoint. The service runs on `http://127.0.0.1:8000` by default.

```Bash
curl http://127.0.0.1:8000/events

# OR

curl http://127.0.0.1:8000/blog/posts

# OR

curl http://127.0.0.1:8000/blog/categories

# OR

curl http://127.0.0.1:8000/blog/tags

# OR

curl http://127.0.0.1:8000/collection/articles

# OR

curl http://127.0.0.1:8000/collection/articles-category

# OR

curl http://127.0.0.1:8000/members
```

If successful, the downloaded file (e.g., `wix_events_data.json`) will be saved to your project's `/data `directory (relative to your project root).

## Shutting Down 🛑

### Terminal_1: Stop the Server

Stop the server by pressing `Ctrl + C` (Control + C) on your keyboard. This shuts down the Uvicorn server.

### Terminals_1&2: Exit the Environment

When you are finished, exit the isolated environment in both terminals:

```Bash
deactivate
```

Your command prompt will return to its default state, and the environment name (`.venv`) will disappear.
