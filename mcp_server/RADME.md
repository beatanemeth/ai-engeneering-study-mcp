# MCP Server

This service exposes a set of analytical **MCP tools** that answer a predefined question currently hard-coded in `client.py`.
There is no continuous user interaction — the client runs once, calls the tools, and exits.

The project uses **FastMCP**, a high-level framework for building Model Context Protocol (MCP) servers.

> If you only want to run this service independently, follow the steps below.

The overall intention is to use **local, free tools** only, without relying on third-party APIs.

---

## MCP Components

To understand how this project works, it helps to define the core roles in the MCP ecosystem:

- **MCP Host**
  The main application where the LLM lives (e.g., Claude Desktop, an IDE, or in this case, the `client.py` script).
  The Host orchestrates the interaction between the user, the AI, and the data.

- **MCP Client**
  A protocol-level component within the Host that maintains a 1:1 connection with a specific server.

- **MCP Server**
  A lightweight program that exposes specific capabilities (tools, resources, or prompts) through the standardized Model Context Protocol.

- **Tools**
  Executable functions provided by the server. For example, a tool might query a local JSON file or calculate an average attendance count.

---

## Project Structure

- `mcp_server/server.py`
  Contains the MCP tool definitions (the **Server**).

- `client.py` (project root)
  Acts as both the **MCP Host** and the **MCP Client**, bridging the local Ollama LLM with the tools exposed by the server.

#### Why no third-party Host?

While many tutorials rely on tools like `MCPHost` or Claude Desktop, this project implements the host logic directly in `client.py`.
This makes the MCP handshake explicit and demonstrates how to build a fully custom, integrated AI system.

---

---

## Getting Started 🚀

### 1. Setup Python Virtual Environment

Ensure you have initialized your virtual environment as described in the **root `README.md`**.

### 2. Install Dependencies

With the virtual environment active, install all necessary packages in a single command.

```Bash
# Navigate to the Directory
cd mcp_server/

# Update pip
python -m pip install --upgrade pip

# Install the Packages
pip install -r requirements.txt
```

ℹ️ The `requirements.txt` file contains _all dependencies required_ to run the service: `fastmcp`, `ollama`, `mcp`, `pandas`.

Then, you can check that the server will run using the following command:

```bash
fastmcp run server.py
```

What this does: This command initializes the server and makes it available to other tools at `127.0.0.1:8000`.

Exit with` Ctrl + D` or `/bye`.

---

## Ollama Setup (Local LLM) ⚙️

To process requests locally without third-party API costs, you need to install and run Ollama.

⚠️ **Important**: Ollama is a system-level service. The Ollama setup should be done in a globally opened terminal, not in the projects `.venv`.

### 1. Download & Install:

Visit [ollama.com/download](https://ollama.com/download) or run the following command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Pull the Model:

We use the `qwen2.5:7b` model for its balance of speed and reasoning.

```bash
ollama pull qwen2.5:7b
```

### 3. Verify the Model:

You can test that the model is responding correctly by running:

```bash
ollama run qwen2.5:7b
```

Exit with` Ctrl + D` or `/bye`.

---

## Running the MCP Application ▶️

This process requires two terminal windows:

- one to start the Ollama service and
- one to run the Client.

### Terminal_1: Start the Ollama Service (Global Terminal)

```bash
ollama run qwen2.5:7b
```

### Terminal_2: Run the Client (Project Terminal)

With the virtual environment active:

```bash
python3 client.py
```

## Shutting Down 🛑

### Terminal_1:Stop Ollama

In the Ollama terminal, type `/bye` or press `Ctrl + D`˛

### Terminal_1 & Terminal_2: Exit the Environment

```Bash
deactivate
```

Your command prompt will return to its default state, and the environment name (`.venv`) will disappear.

**Note**: The client exits automatically once the question is answered.
