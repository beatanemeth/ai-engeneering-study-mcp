# Study MCP

This repository explores how **Model Context Protocol (MCP)** can be used to overcome a common limitation of RAG-based systems when working with **structured, real-world data** such as events, articles, and usage metrics.

## Table of Contents

1. [Background & Motivation](#background--motivation)
2. [How MCP Improves InsightHubAI](#how-mcp-improves-insighthubai)
3. [Data Preparation](#data-preparation)
4. [MCP Tools Development](#mcp-tools-development)
5. [MCP Server Setup](#mcp-server-setup)
6. [Technical Details](#technical-details)
7. [Summary](#summary)

## Background & Motivation

- 📖 **Related Medium article**
  [The AI Engineering Challenge: A Three-Step Journey into RAG, LangChain, and Real-World Data](https://medium.com/@beataspace/the-ai-engineering-challenge-a-three-step-journey-into-rag-langchain-and-real-world-data-90badbd139f0)
- 🧑‍💻 **Related GitHub repository**
  [LangChain RAG Project: Unified Custom Data Chat](https://github.com/beatanemeth/ai-engineering-custom-wix-data-chat)

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

The following datasets were downloaded as JSON files:

- Events
- Articles
- Blog posts

The original datasets are stored locally in the `/data` folder, which is **not committed to GitHub**.

To preserve structure without exposing real data:

- a `/data_dummy` folder is included
- it contains representative files with **dummy values** matching the original schemas

**Note**: For simplicity, this is a one-time download rather than a continuous ingestion pipeline.

### Clean Data

After downloading, the data was cleaned and normalized to ensure:

- Consistent date formats
- Structured categories and tags
- Reliable numeric fields
  (attendance, views, likes, waitlist counts)

Data preparation was performed using **Jupyter Notebook and Pandas**.

📂 See: `/data_prepare`
This folder documents the full data preparation process, including cleaning, normalization, and schema validation.

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

## Technical Details

This project is built using a local-first approach, prioritizing open-source tools and data privacy.

### 📦 Prerequisites

- **Python 3.10 or higher**
- **LLM Runtime**: [Ollama](https://ollama.com/) (running `qwen2.5:7b`)

### 🖥️ Operating System Used

- Linux Mint 21.2 (development environment used)

### 🤖 MCP Stack Overview

- Protocol Framework: **FastMCP** (Python-based)
- Intelligence Layer: **Ollama** running the Qwen 2.5 (7B) model.
- Data Processing: **Pandas & Jupyter**.

### 🐍 Python Virtual Environment

It is best practice to use a virtual environment to isolate project dependencies.

#### 1. Initialize the Environment

Create the virtual environment in the project root:

```Bash
python3 -m venv .venv
```

#### 2. Activate the Environment

```Bash
# macOS/Linux:
source .venv/bin/activate

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

Your command prompt will now show the environment name, like `(.venv) user@host:~/project$`, indicating that it is active.

#### 3. Install Project Dependencies

This installs all dependencies required to explore the full project end-to-end.

```Bash
# Update pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

⚠️ **IMPORTANT:**
Whether you have installed the **entire repository** or only want to use a **part of it**, you **must consult the dedicated README** for each service to understand how to **set it up** and **run it** correctly:

- **MCP Server**: `/mcp_server/README.md`
- **JWT Microservice**: `/data_get/jwt_microservice/README.md`
- **Jupyter Notebooks**: `/data_prepare/README.md`

#### 4. Shutting Down

When you are finished working, simply run:

```Bash
deactivate
```

Your command prompt will return to its default state, and the environment name (`.venv`) will disappear.

### 🧹 Jupyter Cleanup & Git Hygiene

> This project uses `nbstripout` to keep notebook outputs out of version control and a `pre-commit` hook to ensure consistent formatting for all files.

- [kynan/nbstripout](https://github.com/kynan/nbstripout)
- [pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

Configuration details can be found in `.pre-commit-config.yaml`.

To check all files and automatically clean notebook outputs before committing, run:

```Bash
pre-commit run --all-files
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
