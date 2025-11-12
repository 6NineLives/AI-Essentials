"""
CrewAI Agent Example
Demonstrates multi-agent collaboration using CrewAI framework.
"""

import os
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

def simulate_crewai_example():
    """
    Simulated CrewAI example (actual implementation requires: pip install crewai)
    This demonstrates the concept and structure.
    """
    
    print("\n" + "="*60)
    print("CREWAI MULTI-AGENT EXAMPLE (SIMULATED)")
    print("="*60)
    
    print("\n📋 Scenario: Create a technical blog post about AI agents")
    
    # Simulated agent definitions
    print("\n1. Defining Agents:")
    print("   🔍 Researcher Agent:")
    print("      Role: Research Specialist")
    print("      Goal: Find accurate information about AI agents")
    print("      Tools: Web search, knowledge base")
    
    print("\n   ✍️  Writer Agent:")
    print("      Role: Content Writer")
    print("      Goal: Write engaging technical content")
    print("      Tools: Grammar checker, style guide")
    
    print("\n   👁️  Editor Agent:")
    print("      Role: Quality Editor")
    print("      Goal: Ensure accuracy and readability")
    print("      Tools: Fact checker, readability analyzer")
    
    # Simulated task execution
    print("\n2. Task Execution:")
    
    print("\n   Task 1: Research (Researcher Agent)")
    print("   Status: 🔄 Researching...")
    research_output = """
   Key Findings:
   - AI agents use LLMs to reason and act
   - They can use tools to interact with external systems
   - Popular frameworks: LangChain, CrewAI, AutoGPT
   - Use cases: Customer support, data analysis, automation
   """
    print(research_output)
    
    print("\n   Task 2: Write Draft (Writer Agent)")
    print("   Status: 🔄 Writing...")
    draft_output = """
   Draft Article:
   
   # Understanding AI Agents
   
   AI agents represent a significant leap forward in artificial
   intelligence. Unlike traditional chatbots, agents can reason
   about problems and take actions to solve them.
   
   ## Key Capabilities
   - Autonomous decision making
   - Tool usage (APIs, databases, search)
   - Multi-step planning
   - Learning from feedback
   
   ## Real-World Applications
   AI agents are being used in customer support, data analysis,
   and development workflows to automate complex tasks.
   """
    print(draft_output)
    
    print("\n   Task 3: Edit & Review (Editor Agent)")
    print("   Status: 🔄 Editing...")
    edit_output = """
   Review Comments:
   ✅ Technical accuracy verified
   ✅ Readability score: 85/100
   ⚠️  Suggested improvements:
      - Add specific examples
      - Include statistics
      - Expand on framework comparison
   """
    print(edit_output)
    
    print("\n3. Collaboration Summary:")
    print("   • Researcher provided comprehensive background")
    print("   • Writer created well-structured content")
    print("   • Editor ensured quality and accuracy")
    
    # Show how agents would be defined with actual CrewAI
    print("\n4. Actual CrewAI Code Structure:")
    print("""
   from crewai import Agent, Task, Crew
   
   # Define agents
   researcher = Agent(
       role='Research Specialist',
       goal='Find accurate AI information',
       backstory='Expert researcher with focus on AI',
       tools=[search_tool],
       verbose=True
   )
   
   writer = Agent(
       role='Content Writer',
       goal='Write engaging content',
       backstory='Technical writer with 10 years experience',
       tools=[grammar_tool],
       verbose=True
   )
   
   # Define tasks
   research_task = Task(
       description='Research AI agents comprehensively',
       agent=researcher,
       expected_output='Research report with key findings'
   )
   
   write_task = Task(
       description='Write blog post based on research',
       agent=writer,
       expected_output='Complete blog article'
   )
   
   # Create crew
   crew = Crew(
       agents=[researcher, writer],
       tasks=[research_task, write_task],
       verbose=True
   )
   
   # Execute
   result = crew.kickoff()
   """)

def show_agent_patterns():
    """Show different agent collaboration patterns"""
    
    print("\n" + "="*60)
    print("MULTI-AGENT COLLABORATION PATTERNS")
    print("="*60)
    
    print("\n1. Sequential Pattern:")
    print("   Agent 1 → Agent 2 → Agent 3")
    print("   Example: Research → Write → Edit")
    
    print("\n2. Hierarchical Pattern:")
    print("   Manager Agent")
    print("      ├─ Worker Agent 1")
    print("      ├─ Worker Agent 2")
    print("      └─ Worker Agent 3")
    print("   Example: Project manager coordinating specialists")
    
    print("\n3. Consensus Pattern:")
    print("   Multiple agents vote on decisions")
    print("   Example: Code review by multiple experts")
    
    print("\n4. Debate Pattern:")
    print("   Agents argue different perspectives")
    print("   Example: Pros/cons analysis")

def main():
    """Run CrewAI examples"""
    
    print("\n" + "="*60)
    print("CREWAI MULTI-AGENT SYSTEM DEMO")
    print("="*60)
    
    print("\nℹ️  CrewAI enables multiple AI agents to work together")
    print("   Each agent has a role, goal, and specialized tools")
    
    if not check_api_key():
        print("\n⚠️  Note: API key needed for actual CrewAI execution")
    
    # Show simulation
    simulate_crewai_example()
    
    # Show patterns
    show_agent_patterns()
    
    print("\n" + "="*60)
    print("✅ CrewAI concepts demonstrated!")
    print("="*60)
    
    print("\n💡 Key Takeaways:")
    print("   1. Multi-agent systems divide complex tasks")
    print("   2. Each agent specializes in specific roles")
    print("   3. Agents collaborate to achieve goals")
    print("   4. Results are often better than single-agent")
    
    print("\n📦 To use CrewAI in production:")
    print("   pip install crewai crewai-tools")
    print("   Then run actual multi-agent workflows!")
    
    print("\n🔗 Resources:")
    print("   - CrewAI Docs: https://docs.crewai.com/")
    print("   - GitHub: https://github.com/joaomdmoura/crewAI")
    print("\n")

if __name__ == "__main__":
    main()
