"""
OpenAI API Example
Demonstrates how to use OpenAI's API for various LLM tasks.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("⚠️  WARNING: OPENAI_API_KEY not set in .env file")
        print("   This example requires a valid OpenAI API key")
        print("   Get one at: https://platform.openai.com/api-keys")
        return False
    return True

def simple_chat_completion():
    """Basic chat completion example"""
    print("\n" + "=" * 60)
    print("1. SIMPLE CHAT COMPLETION")
    print("=" * 60)
    
    if not check_api_key():
        return
    
    client = OpenAI()
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains AI concepts clearly."},
                {"role": "user", "content": "Explain what a Large Language Model is in 2 sentences."}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        answer = response.choices[0].message.content
        print(f"\n🤖 Assistant: {answer}")
        print(f"\n📊 Tokens used: {response.usage.total_tokens}")
        print(f"   - Prompt: {response.usage.prompt_tokens}")
        print(f"   - Completion: {response.usage.completion_tokens}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def streaming_example():
    """Streaming response example"""
    print("\n" + "=" * 60)
    print("2. STREAMING RESPONSE")
    print("=" * 60)
    
    if not check_api_key():
        return
    
    client = OpenAI()
    
    try:
        print("\n🤖 Assistant: ", end="", flush=True)
        
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Write a haiku about artificial intelligence."}
            ],
            stream=True,
            temperature=0.8
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

def function_calling_example():
    """Function calling (tool use) example"""
    print("\n" + "=" * 60)
    print("3. FUNCTION CALLING")
    print("=" * 60)
    
    if not check_api_key():
        return
    
    client = OpenAI()
    
    # Define a function
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA"
                        },
                        "unit": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit"
                        }
                    },
                    "required": ["location"]
                }
            }
        }
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "What's the weather like in San Francisco?"}
            ],
            tools=tools,
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        
        if message.tool_calls:
            tool_call = message.tool_calls[0]
            print(f"\n🔧 Function called: {tool_call.function.name}")
            print(f"📝 Arguments: {tool_call.function.arguments}")
            print("\nℹ️  In a real application, you would:")
            print("   1. Execute the function with these arguments")
            print("   2. Send the result back to the model")
            print("   3. Get a natural language response")
        else:
            print(f"\n🤖 Direct response: {message.content}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def multi_turn_conversation():
    """Multi-turn conversation example"""
    print("\n" + "=" * 60)
    print("4. MULTI-TURN CONVERSATION")
    print("=" * 60)
    
    if not check_api_key():
        return
    
    client = OpenAI()
    
    # Conversation history
    messages = [
        {"role": "system", "content": "You are a helpful AI tutor teaching machine learning."}
    ]
    
    conversation = [
        "What is supervised learning?",
        "Can you give me an example?",
        "How is it different from unsupervised learning?"
    ]
    
    try:
        for user_msg in conversation:
            print(f"\n👤 User: {user_msg}")
            
            # Add user message
            messages.append({"role": "user", "content": user_msg})
            
            # Get response
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            
            assistant_msg = response.choices[0].message.content
            print(f"🤖 Assistant: {assistant_msg}")
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": assistant_msg})
            
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("OPENAI API EXAMPLES")
    print("=" * 60)
    
    # Check if API key is configured
    if not check_api_key():
        print("\n⚠️  Skipping examples - API key not configured")
        return
    
    # Run examples
    simple_chat_completion()
    streaming_example()
    function_calling_example()
    multi_turn_conversation()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)
    print("\n💡 Tips:")
    print("   - Use gpt-3.5-turbo for faster, cheaper responses")
    print("   - Use gpt-4 for complex reasoning tasks")
    print("   - Always handle errors and rate limits")
    print("   - Monitor your token usage and costs")
    print("\n")

if __name__ == "__main__":
    main()
