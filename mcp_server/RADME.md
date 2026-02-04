# MCP Server

> In case, that you only would like to use this service, follow the steps bellow for the installation.

The intention was to use local, free tools.

## MCP Components

To understand how this project works, it helps to define the core roles in the MCP ecosystem:

- **MCP Host**: The main application where the LLM lives (e.g., Claude Desktop, an IDE, or in this case, our `client.py` script). The Host orchestrates the interaction between the user, the AI, and the data.
- **MCP Client**: A protocol-level component within the Host that maintains a 1:1 connection with a specific server.
- **MCP Server**: A lightweight program that exposes specific capabilities (tools, resources, or prompts) through the standardized Model Context Protocol.
- **Tools**: Executable functions provided by the server. For example, a tool might query a local JSON file or calculate an average attendance count.

## Project Structure

- `mcp_server/server.py`: Contains the tool definitions (the "Server").
- `client.py`: Located in the project root. It acts as both the MCP Host and the MCP Client, bridging our local Ollama LLM with the tools in the server.

**Why no third-party Host?**
While many tutorials use tools like `MCPHost` or `Claude Desktop` to interact with servers, this project implements the host logic directly in `client.py`. This provides a deeper understanding of the "handshake" between the LLM and the tools and demonstrates how to build a custom integrated AI system.

---

---

## Getting Started 🚀

### 1. Setup Python Virtual Environment

Ensure you have initialized your virtual environment as described in the **root `README.md`**.

### 2. Install Dependencies

This project uses **FastMCP**, a high-level framework for building MCP servers.

```bash
pip install fastmcp ollama mcp
```

Then, you can check that the server will run using the following command:

```bash
fastmcp run server.py
```

What this does: This command initializes the server and makes it available to other tools at `127.0.0.1:8000`.

⚠️ **Important**: Ollama is a system-level service. The installation should be done in a **global terminal**, not inside the project's `.venv`.

Exit with` Ctrl + D` or `/bye`.

---

## Ollama Setup (Local LLM) ⚙️

To process requests locally without third-party API costs, you need to install and run Ollama.

**Note**: Ollama is a system-level service. The Ollama setup should be done in a globally opened terminal, not in the projects `.venv`.

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

Follow these steps in order using two separate terminal windows:

### 1. Start the Ollama Service (Global Terminal)

Ensure the "brain" is awake and ready:

```bash
ollama run qwen2.5:7b
```

### 2. Run the Client

Step 2: Run the Client (Project Terminal)
In a separate window with your `.venv` active, run the bridge script:

```bash
python3 client.py
```

## Shutting Down 🛑

### 1. Stop Ollama

In the Ollama terminal, type `/bye` or press `Ctrl + D`˛

### 2. Stop the Client

The client is designed to exit automatically once the question is answered.

### 3. Deactivate Environment

```Bash
deactivate
```
