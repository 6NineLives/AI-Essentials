"""
MCP Server Example
A minimal Model Context Protocol server in Python demonstrating core concepts.
"""

import asyncio
import json
from datetime import datetime

# Note: This is a simplified example showing MCP concepts
# For production use, install: pip install mcp

class SimpleMCPServer:
    """
    Simplified MCP server demonstration
    
    In production, use the official MCP SDK:
    from mcp.server import Server
    """
    
    def __init__(self, name="demo-mcp-server"):
        self.name = name
        self.version = "1.0.0"
        self.resources = []
        self.tools = []
        
    def register_resource(self, uri, name, mime_type, content):
        """Register a resource that can be accessed"""
        resource = {
            "uri": uri,
            "name": name,
            "mimeType": mime_type,
            "description": f"Resource: {name}",
            "content": content
        }
        self.resources.append(resource)
        
    def register_tool(self, name, description, handler):
        """Register a tool that can be called"""
        tool = {
            "name": name,
            "description": description,
            "handler": handler,
            "inputSchema": {
                "type": "object",
                "properties": {}
            }
        }
        self.tools.append(tool)
        
    async def list_resources(self):
        """List all available resources"""
        return {
            "resources": [
                {
                    "uri": r["uri"],
                    "name": r["name"],
                    "mimeType": r["mimeType"],
                    "description": r["description"]
                }
                for r in self.resources
            ]
        }
    
    async def read_resource(self, uri):
        """Read a specific resource"""
        for resource in self.resources:
            if resource["uri"] == uri:
                return {
                    "contents": [{
                        "uri": resource["uri"],
                        "mimeType": resource["mimeType"],
                        "text": resource["content"]
                    }]
                }
        return {"error": "Resource not found"}
    
    async def list_tools(self):
        """List all available tools"""
        return {
            "tools": [
                {
                    "name": t["name"],
                    "description": t["description"],
                    "inputSchema": t["inputSchema"]
                }
                for t in self.tools
            ]
        }
    
    async def call_tool(self, tool_name, arguments):
        """Call a tool with arguments"""
        for tool in self.tools:
            if tool["name"] == tool_name:
                try:
                    result = await tool["handler"](**arguments)
                    return {
                        "content": [{
                            "type": "text",
                            "text": str(result)
                        }]
                    }
                except Exception as e:
                    return {"error": str(e)}
        return {"error": "Tool not found"}

# Tool implementations
async def calculator_tool(operation, a, b):
    """Simple calculator tool"""
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    if operation in operations:
        result = operations[operation](float(a), float(b))
        return f"{operation}({a}, {b}) = {result}"
    return f"Unknown operation: {operation}"

async def get_time_tool():
    """Get current time"""
    return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

async def echo_tool(message):
    """Echo back a message"""
    return f"Echo: {message}"

async def main():
    """Demonstrate MCP server functionality"""
    print("=" * 60)
    print("MCP SERVER EXAMPLE")
    print("=" * 60)
    
    # Initialize server
    print("\n1. Initializing MCP server...")
    server = SimpleMCPServer("demo-mcp-server")
    print(f"   Server name: {server.name}")
    print(f"   Version: {server.version}")
    
    # Register resources
    print("\n2. Registering resources...")
    server.register_resource(
        uri="resource://documentation",
        name="API Documentation",
        mime_type="text/markdown",
        content="# API Documentation\n\nThis is sample documentation."
    )
    server.register_resource(
        uri="resource://config",
        name="Configuration",
        mime_type="application/json",
        content='{"env": "production", "debug": false}'
    )
    print(f"   Registered {len(server.resources)} resources")
    
    # Register tools
    print("\n3. Registering tools...")
    server.register_tool(
        name="calculator",
        description="Perform basic arithmetic operations",
        handler=calculator_tool
    )
    server.register_tool(
        name="get_time",
        description="Get the current time",
        handler=get_time_tool
    )
    server.register_tool(
        name="echo",
        description="Echo back a message",
        handler=echo_tool
    )
    print(f"   Registered {len(server.tools)} tools")
    
    # Demonstrate listing resources
    print("\n4. Listing available resources...")
    resources = await server.list_resources()
    for resource in resources["resources"]:
        print(f"   • {resource['name']}: {resource['uri']}")
    
    # Demonstrate reading a resource
    print("\n5. Reading a resource...")
    config = await server.read_resource("resource://config")
    print(f"   Resource content:")
    print(f"   {config['contents'][0]['text']}")
    
    # Demonstrate listing tools
    print("\n6. Listing available tools...")
    tools = await server.list_tools()
    for tool in tools["tools"]:
        print(f"   • {tool['name']}: {tool['description']}")
    
    # Demonstrate calling tools
    print("\n7. Calling tools...")
    
    # Calculator
    result = await server.call_tool("calculator", {
        "operation": "add",
        "a": 15,
        "b": 27
    })
    print(f"   Calculator: {result['content'][0]['text']}")
    
    # Get time
    result = await server.call_tool("get_time", {})
    print(f"   Get Time: {result['content'][0]['text']}")
    
    # Echo
    result = await server.call_tool("echo", {
        "message": "Hello, MCP!"
    })
    print(f"   Echo: {result['content'][0]['text']}")
    
    print("\n" + "=" * 60)
    print("✅ MCP Server demonstration completed!")
    print("=" * 60)
    print("\n💡 Key Concepts:")
    print("   1. Resources - Data sources accessible to clients")
    print("   2. Tools - Functions clients can invoke")
    print("   3. Protocol - Standardized communication")
    print("\n📚 Next Steps:")
    print("   - Install official MCP SDK: pip install mcp")
    print("   - Create custom servers for your data")
    print("   - Integrate with Claude Desktop or custom clients")
    print("\n")

if __name__ == "__main__":
    asyncio.run(main())
