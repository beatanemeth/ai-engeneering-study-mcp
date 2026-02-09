import asyncio
import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os

# Get the absolute path to the server script
current_dir = os.path.dirname(os.path.abspath(__file__))
server_script = os.path.join(current_dir, "mcp_server", "server.py")

# 1. Setup Server Parameters
# This tells the client how to launch your MCP server
server_params = StdioServerParameters(
    command="python3",  # Or path to your .venv/bin/python
    args=[server_script],
    env=os.environ.copy(),  # Crucial: passes current environment to the server
)


async def run_insight_hub_client():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Get tools and format for Ollama
            tools_response = await session.list_tools()
            available_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema,
                    },
                }
                for tool in tools_response.tools
            ]

            user_prompt = "How many participants did we have in 2024 total, and which was the biggest event?"
            # user_prompt = "Can you list all the unique categories and tags used in the blog posts ever?"
            # user_prompt = (
            #     "Give me the breakdown of online vs. venue events for the year 2021."
            # )
            # user_prompt = "What was our total attendance across all events, and what was the single most popular event we've ever held?"
            # user_prompt = "I want to compare our output from 2025. How many blog posts did we write compared to the number of events we held, and which month was the busiest for the number of blog posts published that year?"
            # user_prompt = "I want to compare our output from 2025. How many blog posts did we write compared to the number of events we held? Which month did we published the most blog posts that year?"

            # Also tested with RAG prompt:
            # user_prompt = "Were there any events in November 2023, and were there any posts published?"
            # user_prompt = "List the posts written in 2022!"
            # user_prompt = (
            #     "When was the most recent ‘Összehangolva a Simonton módszerrel’ event?"
            # )

            print(f"\n[User]: {user_prompt}")

            # 2. First Call to Ollama
            messages = [{"role": "user", "content": user_prompt}]
            response = ollama.chat(
                model="qwen2.5:7b",
                messages=messages,
                tools=available_tools,
            )

            # Add Ollama's response (containing tool_calls) to history
            messages.append(response["message"])

            # 3. Process Tool Calls
            if response["message"].get("tool_calls"):
                for tool_call in response["message"]["tool_calls"]:
                    tool_name = tool_call["function"]["name"]
                    tool_args = tool_call["function"]["arguments"]

                    print(f"--- Calling Tool: {tool_name} with {tool_args} ---")

                    # Execute tool on MCP Server
                    result = await session.call_tool(tool_name, tool_args)

                    # FIX: Extract only the text from the result content
                    # result.content is a list of TextContent objects
                    tool_result_text = ""
                    for content in result.content:
                        if hasattr(content, "text"):
                            tool_result_text += content.text
                        elif isinstance(content, dict) and "text" in content:
                            tool_result_text += content["text"]

                    # Add the tool result to message history
                    messages.append(
                        {
                            "role": "tool",
                            "content": tool_result_text,
                            "name": tool_name,
                        }
                    )

                # 4. Final Call to Ollama with the data
                final_response = ollama.chat(model="qwen2.5:7b", messages=messages)
                print(f"\n[AI]: {final_response['message']['content']}")
            else:
                print(f"\n[AI]: {response['message']['content']}")


if __name__ == "__main__":
    try:
        asyncio.run(run_insight_hub_client())
    except Exception as e:
        # This will now catch detailed errors if the server fails
        import traceback

        traceback.print_exc()
