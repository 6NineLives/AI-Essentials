# 🚀 MCP in 5 Minutes

## 🧠 Concept

**Model Context Protocol (MCP)** is an open standard that enables AI applications to securely connect to data sources and tools. Think of it as USB for AI - one protocol to connect everything.

**Created by**: Anthropic (makers of Claude)  
**Status**: Open source, growing adoption

## 💡 Why It Matters

Before MCP, every AI app needed custom integrations:

**Problem**:
- 🔴 Each app writes custom code for every integration
- 🔴 No reusability across applications
- 🔴 Security and access control per-app
- 🔴 Maintenance nightmare

**With MCP**:
- ✅ Write once, use everywhere
- ✅ Standard protocol = composability
- ✅ Centralized security model
- ✅ Growing ecosystem of servers

**Business Impact**: Reduce integration time from weeks to hours. Connect Claude, custom apps, or IDEs to your data instantly.

## ⚙️ How It Works (Simplified)

### Architecture

```
┌─────────────────┐
│  Host App       │  (Claude Desktop, IDE, Custom App)
│  (has MCP Client)│
└────────┬────────┘
         │ JSON-RPC
    ┌────┴─────┬──────┬──────┐
    │          │      │      │
┌───▼───┐  ┌──▼──┐ ┌─▼──┐ ┌─▼──┐
│Server1│  │Srv2 │ │Srv3│ │... │
│ Files │  │ DB  │ │API │ │    │
└───┬───┘  └──┬──┘ └─┬──┘ └────┘
    │         │      │
┌───▼───┐  ┌──▼──┐ ┌─▼──┐
│Local  │  │ SQL │ │HTTP│
│Files  │  │ DB  │ │APIs│
└───────┘  └─────┘ └────┘
```

### Core Capabilities

**1. Resources** - Read data
```
MCP Server exposes:
- file:///project/README.md
- db://customers/table
- api://weather/current
```

**2. Tools** - Execute functions
```
LLM can call:
- read_file(path)
- query_database(sql)
- send_email(to, subject, body)
```

**3. Prompts** - Reusable templates
```
Predefined prompts:
- "Review this code: {file_path}"
- "Summarize document: {doc_uri}"
```

## 🔍 Quick Example

### Simple MCP Server (Python)

```python
from mcp.server import Server

server = Server("my-server")

# Expose a resource
@server.resource("file://data")
async def get_data():
    return {
        "uri": "file://data.json",
        "mimeType": "application/json",
        "text": '{"users": 150, "active": 120}'
    }

# Expose a tool
@server.tool("calculate_total")
async def calc(items: list[float]):
    return {"total": sum(items)}

server.run()
```

### Using from Client

```python
from mcp.client import ClientSession

async with ClientSession() as session:
    # Connect
    await session.connect("python my-server.py")
    
    # List resources
    resources = await session.list_resources()
    # → ["file://data"]
    
    # Call tool
    result = await session.call_tool("calculate_total", {
        "items": [10.5, 20.0, 15.75]
    })
    # → {"total": 46.25}
```

### Claude Desktop Integration

```json
// ~/.config/claude/config.json
{
  "mcpServers": {
    "filesystem": {
      "command": "python",
      "args": ["/path/to/mcp_filesystem_server.py"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your_token"
      }
    }
  }
}
```

Now Claude can read your files and access GitHub!

## 💻 Common Use Cases

### Development Tools
```
MCP Server: Development
├── read_file(path)
├── write_file(path, content)
├── run_tests()
├── git_status()
└── deploy()
```

### Database Access
```
MCP Server: PostgreSQL
├── query(sql)
├── get_schema()
├── list_tables()
└── export_data(table)
```

### API Integration
```
MCP Server: Slack
├── list_channels()
├── send_message(channel, text)
├── get_thread(thread_id)
└── search_messages(query)
```

### File Operations
```
MCP Server: Filesystem
├── read(path)
├── write(path, content)
├── list_directory(path)
├── search(pattern)
└── get_info(path)
```

## 🔑 Key Components

### Server Definition
```typescript
{
  name: "my-server",
  version: "1.0.0",
  capabilities: {
    resources: true,  // Can provide data
    tools: true,      // Can execute functions
    prompts: true     // Has prompt templates
  }
}
```

### Resource Schema
```json
{
  "uri": "file:///project/README.md",
  "name": "Project README",
  "mimeType": "text/markdown",
  "description": "Main project documentation"
}
```

### Tool Schema
```json
{
  "name": "send_email",
  "description": "Send an email",
  "inputSchema": {
    "type": "object",
    "properties": {
      "to": {"type": "string"},
      "subject": {"type": "string"},
      "body": {"type": "string"}
    },
    "required": ["to", "subject", "body"]
  }
}
```

## 🎯 Best Practices

### Server Design
```python
# ✅ Good: Clear, focused server
class FileServer:
    resources: ["file://..."]
    tools: ["read", "write", "search"]

# ❌ Bad: Kitchen sink server
class EverythingServer:
    resources: ["file://", "db://", "api://", ...]
    tools: [50+ functions]
```

### Security
```python
# ✅ Validate and sanitize
def read_file(path: str):
    # Check path is within allowed directory
    if not is_safe_path(path):
        raise SecurityError("Invalid path")
    return read_safe(path)

# ❌ Direct file access
def read_file(path: str):
    return open(path).read()  # Dangerous!
```

### Error Handling
```python
# ✅ Graceful errors
try:
    result = await server.call_tool("query", {"sql": sql})
except ToolError as e:
    return {"error": str(e), "code": "TOOL_ERROR"}

# ❌ Unhandled exceptions
result = await server.call_tool("query", {"sql": sql})  # May crash
```

## 📊 MCP Ecosystem

### Official Servers
- **Filesystem** - Local file access
- **GitHub** - Repository operations
- **Slack** - Team communication
- **PostgreSQL** - Database queries
- **Google Drive** - Cloud storage

### Growing Fast
- 50+ servers available
- Active community
- Language support: Python, TypeScript, Go
- Integration in major tools

## 🚧 Current Status

**✅ Ready**:
- Protocol specification stable
- Claude Desktop integration
- Multiple server implementations
- Growing community

**🚧 Evolving**:
- IDE integrations (VSCode, etc.)
- More official servers
- Advanced features
- Enterprise tooling

## 🌟 Real-World Impact

### Developer Experience
```
Before: 2 weeks to integrate Slack
With MCP: 10 minutes to configure server
```

### Claude Desktop Users
- Connect to 10+ data sources instantly
- Use private files in conversations
- Execute tools from chat
- Secure, sandboxed access

## 📖 Learn More

### Quick Start
1. Install: `pip install mcp` or `npm install @modelcontextprotocol/sdk`
2. Run example: `python 04_MCP/mcp_server_example.py`
3. Connect to Claude Desktop

### Resources
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Server Examples](https://github.com/modelcontextprotocol/servers)
- [Python SDK Docs](https://modelcontextprotocol.io/docs/python)

### Next Topics
- **Build custom servers** for your data
- **Combine with Agents** for autonomous actions
- **Integrate with RAG** for enhanced context

---

**⏱️ Time to First Server**: ~15 minutes

**💰 Cost**: Free (open source)

**📈 Adoption**: Rapidly growing, backed by Anthropic
