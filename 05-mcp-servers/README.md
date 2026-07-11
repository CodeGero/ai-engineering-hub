# 05 — MCP: Give Your Agent Real Tools (The Standard Way)

**Model Context Protocol (MCP)** is the fastest-adopted standard for connecting
AI agents to tools and data. Before MCP, every agent framework had its *own*
tool format — you rewrote the same "search my database" tool for LangChain,
then again for Cursor, then again for Claude Desktop. MCP ends that: **write a
tool once, any MCP-compatible client can use it.**

- MCP servers: 88k★ on GitHub. It's the new default.
- Supported by Claude Desktop, Cursor, VS Code, and most agent frameworks.

## The mental model
```
Agent (Claude/Cursor/your code)
        │  MCP (JSON-RPC over stdio or HTTP)
        ▼
MCP Server  ──▶ your tools: search_docs(), query_db(), deploy()
```
The agent discovers your tools automatically. No glue code per client.

## Build a minimal MCP server (Python)
Install the SDK:
```bash
pip install mcp
```

`server.py` — exposes one tool, `add(a, b)`:
```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool
import anyio

app = Server("demo")

@app.list_tools()
async def list_tools():
    return [Tool(
        name="add",
        description="Add two numbers.",
        inputSchema={"type":"object",
            "properties":{"a":{"type":"number"},"b":{"type":"number"}},
            "required":["a","b"]})]

@app.call_tool()
async def call_tool(name, args):
    if name == "add":
        return [TextContent(type="text", text=str(args["a"]+args["b"]))]
    raise ValueError(f"unknown tool {name}")

async def main():
    async with stdio_server() as (r, w):
        await app.run(r, w, app.create_initialization_options())

if __name__ == "__main__":
    anyio.run(main)
```

Run it (stdio mode — the client launches it):
```bash
python server.py
```
To connect it to Claude Desktop, add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "demo": {"command": "python", "args": ["/path/to/server.py"]}
  }
}
```
Restart Claude Desktop. It now has an `add` tool — no code changes to the client.

## Why this matters for you
- **Write once, use everywhere.** Your internal API becomes an agent tool in one file.
- **Security boundary.** The server runs your code; the agent only sees the tool schema.
- **Composable.** Chain a Postgres MCP server + a filesystem MCP server + a Slack MCP server and let the agent orchestrate.

## Exercise
Replace `add` with `query_weather(city)` that calls a free weather API. Now any
MCP client can ask "what's the weather in Bahrain?" and the agent uses your tool.

→ Next: [06 RAG with LlamaIndex](06-rag-llamaindex/README.md)
