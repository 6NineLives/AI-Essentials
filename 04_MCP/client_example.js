/**
 * MCP Client Example
 * Demonstrates connecting to and interacting with an MCP server from JavaScript.
 */

// Note: This is a simplified example showing MCP concepts
// For production use: npm install @modelcontextprotocol/sdk

class SimpleMCPClient {
  constructor(serverName = 'demo-client') {
    this.serverName = serverName;
    this.connected = false;
  }

  async connect(serverCommand) {
    console.log(`🔌 Connecting to MCP server: ${serverCommand}`);
    this.connected = true;
    console.log('   ✅ Connected');
  }

  async listResources() {
    if (!this.connected) {
      throw new Error('Not connected to server');
    }
    
    // Simulated response
    return {
      resources: [
        {
          uri: 'resource://documentation',
          name: 'API Documentation',
          mimeType: 'text/markdown',
          description: 'Resource: API Documentation'
        },
        {
          uri: 'resource://config',
          name: 'Configuration',
          mimeType: 'application/json',
          description: 'Resource: Configuration'
        }
      ]
    };
  }

  async readResource(uri) {
    if (!this.connected) {
      throw new Error('Not connected to server');
    }

    console.log(`📖 Reading resource: ${uri}`);
    
    // Simulated responses
    const resources = {
      'resource://documentation': {
        uri: uri,
        mimeType: 'text/markdown',
        text: '# API Documentation\n\nThis is sample documentation.'
      },
      'resource://config': {
        uri: uri,
        mimeType: 'application/json',
        text: '{"env": "production", "debug": false}'
      }
    };

    return {
      contents: [resources[uri] || { error: 'Resource not found' }]
    };
  }

  async listTools() {
    if (!this.connected) {
      throw new Error('Not connected to server');
    }

    return {
      tools: [
        {
          name: 'calculator',
          description: 'Perform basic arithmetic operations',
          inputSchema: {
            type: 'object',
            properties: {
              operation: { type: 'string' },
              a: { type: 'number' },
              b: { type: 'number' }
            }
          }
        },
        {
          name: 'get_time',
          description: 'Get the current time',
          inputSchema: { type: 'object', properties: {} }
        },
        {
          name: 'echo',
          description: 'Echo back a message',
          inputSchema: {
            type: 'object',
            properties: {
              message: { type: 'string' }
            }
          }
        }
      ]
    };
  }

  async callTool(toolName, args) {
    if (!this.connected) {
      throw new Error('Not connected to server');
    }

    console.log(`🔧 Calling tool: ${toolName}`);
    console.log(`   Arguments:`, args);

    // Simulated tool responses
    if (toolName === 'calculator') {
      const { operation, a, b } = args;
      let result;
      switch (operation) {
        case 'add': result = a + b; break;
        case 'subtract': result = a - b; break;
        case 'multiply': result = a * b; break;
        case 'divide': result = b !== 0 ? a / b : 'Error: Division by zero'; break;
        default: result = `Unknown operation: ${operation}`;
      }
      return {
        content: [{
          type: 'text',
          text: `${operation}(${a}, ${b}) = ${result}`
        }]
      };
    }

    if (toolName === 'get_time') {
      const now = new Date().toLocaleString();
      return {
        content: [{
          type: 'text',
          text: `Current time: ${now}`
        }]
      };
    }

    if (toolName === 'echo') {
      return {
        content: [{
          type: 'text',
          text: `Echo: ${args.message}`
        }]
      };
    }

    throw new Error(`Unknown tool: ${toolName}`);
  }

  async disconnect() {
    console.log('👋 Disconnecting from server');
    this.connected = false;
  }
}

async function main() {
  console.log('='.repeat(60));
  console.log('MCP CLIENT EXAMPLE');
  console.log('='.repeat(60));

  try {
    // Initialize client
    console.log('\n1. Initializing MCP client...');
    const client = new SimpleMCPClient('demo-client');
    console.log(`   Client name: ${client.serverName}`);

    // Connect to server
    console.log('\n2. Connecting to server...');
    await client.connect('python mcp_server_example.py');

    // List resources
    console.log('\n3. Listing available resources...');
    const resources = await client.listResources();
    console.log(`   Found ${resources.resources.length} resources:`);
    resources.resources.forEach(resource => {
      console.log(`   • ${resource.name}: ${resource.uri}`);
    });

    // Read a resource
    console.log('\n4. Reading a resource...');
    const config = await client.readResource('resource://config');
    console.log('   Content:');
    console.log(`   ${config.contents[0].text}`);

    // List tools
    console.log('\n5. Listing available tools...');
    const tools = await client.listTools();
    console.log(`   Found ${tools.tools.length} tools:`);
    tools.tools.forEach(tool => {
      console.log(`   • ${tool.name}: ${tool.description}`);
    });

    // Call tools
    console.log('\n6. Calling tools...');
    
    // Calculator
    let result = await client.callTool('calculator', {
      operation: 'multiply',
      a: 12,
      b: 8
    });
    console.log(`   Result: ${result.content[0].text}`);

    // Get time
    result = await client.callTool('get_time', {});
    console.log(`   Result: ${result.content[0].text}`);

    // Echo
    result = await client.callTool('echo', {
      message: 'Hello from JavaScript!'
    });
    console.log(`   Result: ${result.content[0].text}`);

    // Disconnect
    console.log('\n7. Cleaning up...');
    await client.disconnect();

    console.log('\n' + '='.repeat(60));
    console.log('✅ MCP Client demonstration completed!');
    console.log('='.repeat(60));
    console.log('\n💡 Key Takeaways:');
    console.log('   1. MCP enables standardized client-server communication');
    console.log('   2. Clients can discover and use server capabilities');
    console.log('   3. Resources and tools are accessed via protocol');
    console.log('\n📚 Next Steps:');
    console.log('   - Install official SDK: npm install @modelcontextprotocol/sdk');
    console.log('   - Connect to real MCP servers');
    console.log('   - Build custom integrations');
    console.log('');

  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

// Run if executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}

export { SimpleMCPClient };
