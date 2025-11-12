"""
OpenAI Agent Example
Demonstrates building an AI agent using OpenAI's function calling.
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import math

# Load environment variables
load_dotenv()

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("⚠️  WARNING: OPENAI_API_KEY not set in .env file")
        return False
    return True

# Tool implementations
def calculator(operation: str, a: float, b: float) -> dict:
    """Perform mathematical operations"""
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero",
        "power": a ** b,
        "sqrt": math.sqrt(a) if operation == "sqrt" else None
    }
    
    result = operations.get(operation, "Unknown operation")
    return {
        "operation": operation,
        "result": result,
        "calculation": f"{operation}({a}, {b}) = {result}"
    }

def get_weather(location: str, unit: str = "celsius") -> dict:
    """Simulated weather tool (in real app, would call weather API)"""
    # Simulated weather data
    weather_data = {
        "new york": {"temp": 22, "condition": "Sunny", "humidity": 65},
        "london": {"temp": 15, "condition": "Cloudy", "humidity": 80},
        "tokyo": {"temp": 25, "condition": "Clear", "humidity": 70},
        "paris": {"temp": 18, "condition": "Rainy", "humidity": 85},
    }
    
    location_lower = location.lower()
    data = weather_data.get(location_lower, {
        "temp": 20,
        "condition": "Unknown",
        "humidity": 60
    })
    
    if unit == "fahrenheit":
        data["temp"] = data["temp"] * 9/5 + 32
        data["unit"] = "°F"
    else:
        data["unit"] = "°C"
    
    return {
        "location": location,
        **data,
        "timestamp": datetime.now().isoformat()
    }

def search_knowledge_base(query: str) -> dict:
    """Simulated knowledge base search"""
    knowledge = {
        "python": "Python is a high-level programming language known for readability and versatility.",
        "ai": "Artificial Intelligence enables machines to learn and make decisions.",
        "agent": "AI agents are autonomous systems that can perceive, reason, and act.",
        "llm": "Large Language Models are neural networks trained on vast text data.",
    }
    
    # Simple keyword matching
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return {"found": True, "query": query, "answer": value}
    
    return {"found": False, "query": query, "answer": "No information found."}

# Define tools for the agent
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform mathematical calculations like add, subtract, multiply, divide, power",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide", "power", "sqrt"],
                        "description": "The mathematical operation to perform"
                    },
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    }
                },
                "required": ["operation", "a"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_knowledge_base",
            "description": "Search the knowledge base for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# Tool execution mapping
TOOL_FUNCTIONS = {
    "calculator": calculator,
    "get_weather": get_weather,
    "search_knowledge_base": search_knowledge_base
}

def execute_tool_call(tool_call):
    """Execute a tool call and return the result"""
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
    
    print(f"   🔧 Calling: {function_name}({json.dumps(function_args, indent=6)})")
    
    if function_name in TOOL_FUNCTIONS:
        result = TOOL_FUNCTIONS[function_name](**function_args)
        print(f"   ✅ Result: {json.dumps(result, indent=6)}")
        return json.dumps(result)
    else:
        return json.dumps({"error": f"Unknown function: {function_name}"})

def run_agent(user_query: str, max_iterations: int = 5):
    """Run the agent loop"""
    print(f"\n{'='*60}")
    print(f"🤖 AGENT TASK: {user_query}")
    print(f"{'='*60}\n")
    
    if not check_api_key():
        print("⚠️  Skipping - API key not configured")
        return
    
    client = OpenAI()
    
    messages = [
        {
            "role": "system",
            "content": """You are a helpful AI agent with access to tools.
            Use tools when needed to answer questions accurately.
            Always explain your reasoning."""
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
    
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        print(f"Iteration {iteration}:")
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )
            
            message = response.choices[0].message
            messages.append(message)
            
            if message.tool_calls:
                print(f"   💭 Thought: Need to use tools")
                
                for tool_call in message.tool_calls:
                    result = execute_tool_call(tool_call)
                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_call.function.name,
                        "content": result
                    })
            else:
                # Agent has final answer
                print(f"\n   🎯 Final Answer:\n   {message.content}\n")
                break
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            break
    
    if iteration >= max_iterations:
        print(f"\n   ⚠️  Reached maximum iterations ({max_iterations})")

def main():
    """Run agent examples"""
    print("\n" + "="*60)
    print("OPENAI AGENT EXAMPLE")
    print("="*60)
    
    if not check_api_key():
        return
    
    # Example 1: Simple calculation
    run_agent("What is 15 multiplied by 23?")
    
    # Example 2: Weather query
    run_agent("What's the weather like in Tokyo?")
    
    # Example 3: Multi-step reasoning
    run_agent("What's the weather in New York and London? Tell me the average temperature.")
    
    # Example 4: Knowledge base search
    run_agent("What is an AI agent?")
    
    # Example 5: Complex multi-tool query
    run_agent("If it's 22°C in New York, convert that to Fahrenheit and then calculate 10% of that number.")
    
    print("\n" + "="*60)
    print("✅ Agent examples completed!")
    print("="*60)
    print("\n💡 Key Features Demonstrated:")
    print("   1. Tool selection and execution")
    print("   2. Multi-step reasoning")
    print("   3. Context maintenance")
    print("   4. Error handling")
    print("\n")

if __name__ == "__main__":
    main()
