"""
System Prompt Tuning Example
Demonstrates how different system prompts affect LLM behavior.
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
        return False
    return True

def test_system_prompt(client, system_prompt, user_message, label):
    """Test a specific system prompt"""
    print(f"\n{'='*60}")
    print(f"{label}")
    print(f"{'='*60}")
    print(f"\nSystem Prompt:\n{system_prompt}")
    print(f"\nUser Message: '{user_message}'")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content
        print(f"\n🤖 Response:\n{answer}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

def main():
    """Run system prompt tuning examples"""
    
    print("\n" + "="*60)
    print("SYSTEM PROMPT TUNING EXAMPLES")
    print("="*60)
    
    if not check_api_key():
        print("\n⚠️  Skipping examples - API key not configured")
        return
    
    client = OpenAI()
    user_message = "Explain what machine learning is."
    
    # Example 1: No specific guidance
    test_system_prompt(
        client,
        system_prompt="You are a helpful assistant.",
        user_message=user_message,
        label="Example 1: GENERIC ASSISTANT"
    )
    
    # Example 2: Expert role
    test_system_prompt(
        client,
        system_prompt="""You are a machine learning professor with 20 years 
of experience. Explain concepts clearly with academic rigor.""",
        user_message=user_message,
        label="Example 2: EXPERT PROFESSOR"
    )
    
    # Example 3: Beginner-friendly
    test_system_prompt(
        client,
        system_prompt="""You are a patient teacher explaining to complete 
beginners. Use simple words, everyday analogies, and avoid jargon.""",
        user_message=user_message,
        label="Example 3: BEGINNER-FRIENDLY TEACHER"
    )
    
    # Example 4: Technical writer
    test_system_prompt(
        client,
        system_prompt="""You are a technical documentation writer. Provide 
concise, structured explanations with bullet points and examples.""",
        user_message=user_message,
        label="Example 4: TECHNICAL WRITER"
    )
    
    # Example 5: Specific format
    test_system_prompt(
        client,
        system_prompt="""You are a tutor. Format all responses as:
1. One-sentence definition
2. Key concepts (3 bullet points)
3. Real-world example
4. Further reading suggestion""",
        user_message=user_message,
        label="Example 5: STRUCTURED FORMAT"
    )
    
    # Example 6: Persona with constraints
    test_system_prompt(
        client,
        system_prompt="""You are an AI researcher. Explain concepts in 
exactly 3 sentences: 
1. What it is
2. Why it matters
3. How it works
Use technical terms but keep it accessible.""",
        user_message=user_message,
        label="Example 6: CONSTRAINED EXPERT"
    )
    
    print("\n" + "="*60)
    print("✅ System prompt tuning examples completed!")
    print("="*60)
    
    print("\n💡 Key Takeaways:")
    print("   1. System prompts dramatically affect output style")
    print("   2. Define role, tone, and format clearly")
    print("   3. Add constraints for consistency")
    print("   4. Iterate to find what works best")
    
    print("\n🎯 Best Practices:")
    print("   • Be specific about the role/persona")
    print("   • Set clear formatting expectations")
    print("   • Define what to include/exclude")
    print("   • Specify tone and style")
    print("   • Test with multiple examples")
    
    print("\n📝 Template Structure:")
    print("""
   system_prompt = '''
   Role: You are a [role/persona]
   
   Expertise: [domain knowledge]
   
   Style: [tone, formality]
   
   Format:
   - [structure details]
   - [must include]
   - [must avoid]
   
   Constraints:
   - [length, language]
   - [specific requirements]
   '''
   """)
    print()

if __name__ == "__main__":
    main()
