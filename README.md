# Study MCP

This repository explores how **Model Context Protocol (MCP)** can be used to overcome a common limitation of RAG-based systems when working with **structured, real-world data**.

## Background & Motivation

📖 **Related Medium article**
[The AI Engineering Challenge: A Three-Step Journey into RAG, LangChain, and Real-World Data](https://medium.com/@beataspace/the-ai-engineering-challenge-a-three-step-journey-into-rag-langchain-and-real-world-data-90badbd139f0)

In the article above, it was identified that **InsightHubAI** struggled with _data mining_–style questions.
This highlights a classic **“RAG vs. Structured Data”** problem:

- Semantic search (RAG) is excellent at answering questions like
  _“What is the policy on X?”_
- But it performs poorly for questions like
  _“How many times did X happen?”_

The reason is simple: RAG retrieves **text chunks**, not **data rows**.
Counting, aggregating, ranking, and filtering require structured access to data — not semantic similarity.

---

## How MCP Improves InsightHubAI

MCP allows structured data to be treated as a **queryable system**, rather than a passive pile of text.

Instead of the AI:

- guessing answers based on retrieved snippets, or
- attempting to infer numbers from prose,

it can:

- invoke **explicit tools**
- apply **deterministic logic**
- and return **exact, verifiable results**

In short, MCP turns your data into a **functional database interface for the LLM**.

---

## Data Preparation

### Download Data

The following datasets were downloaded as a JSON files:

- Events
- Articles
- Blog posts

The original datasets are stored locally in the `/data` folder, which is **not committed to GitHub**.

To preserve structure without exposing real data:

- a `/data_dummy` folder is included
- it contains representative files with **dummy values** matching the original schemas

---

### Clean Data

After downloading, the data was cleaned and normalized to ensure:

- Consistent date formats
- Structured categories and tags
- Reliable numeric fields
  (attendance, views, likes, waitlist counts)

Data preparation was performed using **Jupyter Notebook and Pandas**.

📂 See: `/data_prepare`
This folder documents the full data preparation process.

The cleaned datasets were saved locally in `/data_prepared`, which is excluded from GitHub.
Instead, a `/data_prepared_dummy` folder is included with cleaned dummy data reflecting the final structure.

---

## MCP Tools Development

The design and development of MCP tools is documented step by step.

📂 See: `/mcp_tools_development`
In particular, review the `README.md` in that directory for:

- question formulation
- tool taxonomy design
- reasoning behind Aggregator, Analyst, and Thematic Finder tools

This section focuses on **how to think about MCP tools**, not just how to implement them.

---

## MCP Server Setup

📂 See: `/mcp_server`

- `server.py` — MCP server implementation
- `client.py` — simple client located in the project root for testing and interaction

This setup demonstrates how the developed MCP tools can be exposed and invoked programmatically.

---

---

## Technical Details 🛠️

This project is built using a local-first approach, prioritizing open-source tools and data privacy.

### 📦 Prerequisites

- **Python 3.x**
- **Python**: Version 3.10 or higher
- **LLM Runtime**: [Ollama](https://ollama.com/) (running `qwen2.5:7b`)

### 🖥️ Operating System Used

- Linux Mint 21.2

### 🤖 MCP Stack Overview

- Protocol Framework: **FastMCP** (Python-based)
- Intelligence Layer: **Ollama** running the Qwen 2.5 (7B) model.
- Data Processing: **Pandas & Jupyter**.

### 🐍 Python Virtual Environment

It is best practice to use a virtual environment to isolate project dependencies.

1. Initialize the Environment

Create the virtual environment in the project root:

```Bash
python3 -m venv .venv
```

2. Activate the environment

```Bash
# macOS/Linux:
source .venv/bin/activate

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

Your command prompt will now show the environment name, like `(.venv) user@host:~/project$`, indicating that it is active.

#### Install Project Dependencies

Update `pip` and install the required libraries for the **entire repository**:

```Bash
# Update pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Run the MCP Service ▶️

For details see:

- **MCP Server**: `/mcp_server/README.md`

⚠️ **IMPORTANT:** If you want to run **_other services_**, please refer to the dedicated instructions in these subdirectories:

- **JWT Microservice**: `/data_get/jwt_microservice/README.md` — Configures data fetching from Wix.
- **Jupyter Notebooks**: `/data_prepare/README.md` — Setup for data cleaning.

#### Shutting Down

When you are finished working, simply run:

```Bash
deactivate
```

---

---

## Summary

This repository documents a practical exploration of:

- why RAG alone is insufficient for structured analytics
- how MCP enables deterministic reasoning over real-world data
- and how to design MCP tools that align with clear analytical intent

It is intended as both:

- a learning project, and
- a reference for designing MCP-based AI systems that go beyond semantic search.
