# 🚀 Prompt Engineering in 5 Minutes

## 🧠 Concept

**Prompt Engineering** is the practice of designing effective instructions for AI models to get better, more accurate, and more useful outputs. It's like learning to communicate clearly with an intelligent but literal assistant.

**Bad Prompt**: "Tell me about AI"  
**Good Prompt**: "You're an expert teacher. Explain neural networks to a software developer using code analogies in under 200 words."

## 💡 Why It Matters

The same AI model produces dramatically different results based on how you ask:

**Impact of Good Prompts**:
- 🔴 Accuracy: 40% → 90%
- 🔴 Relevance: Generic → Exactly what you need
- 🔴 Efficiency: 10 iterations → 1-2 iterations
- 🔴 Cost: $1 of wasted tokens → $0.10

**Business Value**: Teams report 3-5x productivity gains simply by improving their prompting skills. No model changes needed.

## ⚙️ How It Works (Simplified)

### The Prompt Quality Ladder

```
Level 0: "Write code"
   ↓ (too vague)
Result: Random code snippet

Level 1: "Write Python code"
   ↓ (better, but still vague)
Result: Some Python code

Level 2: "Write a Python function to sort a list"
   ↓ (specific task)
Result: Working function

Level 3: "Write a Python function that:
         - Takes a list of integers
         - Returns sorted ascending
         - Handles empty lists
         - Includes docstring and type hints"
   ↓ (detailed requirements)
Result: Production-quality code
```

### Core Components

```
Good Prompt = Role + Context + Task + Format + Constraints
```

## 🔍 Quick Examples

### Example 1: Basic Improvement

**❌ Vague**:
```
"Help me with my code"
```

**✅ Specific**:
```
"You're a Python expert. Debug this function that should
calculate averages but returns incorrect values:

def calc_avg(numbers):
    return sum(numbers) / len(numbers)

The input [1, 2, 3] should return 2.0 but returns an error.
Explain the issue and provide the fix."
```

### Example 2: Role-Based

**❌ Generic**:
```
"Explain machine learning"
```

**✅ With Role**:
```
"You are a university professor teaching a CS101 class.
Explain machine learning to students with no prior
experience using a cooking recipe analogy.
Keep it to 3 paragraphs."
```

### Example 3: Format Control

**❌ Unstructured**:
```
"Analyze this data"
```

**✅ Structured**:
```
"Analyze this sales data and provide:

1. Summary Statistics (mean, median, outliers)
2. Key Insights (3-5 bullet points)
3. Recommendations (specific actions)

Format output as JSON with these exact fields."
```

## 💻 Essential Techniques

### 1. Few-Shot Learning
Teach by example:

```python
"""
Classify sentiment:

Review: "This product is amazing!" → positive
Review: "Terrible quality" → negative  
Review: "It's okay" → neutral

Review: "Best purchase ever!" → 
"""
```

### 2. Chain-of-Thought
Ask for step-by-step reasoning:

```python
"""
Solve step by step:

Problem: If a shirt costs $50 with 20% off, what's the price?

Steps:
1. Calculate discount: $50 × 0.20 = $10
2. Subtract: $50 - $10 = $40
Answer: $40

Problem: A $100 item with 30% off and 10% tax?
Steps:
"""
```

### 3. System Prompts
Set persistent behavior:

```python
system = """
You are a helpful coding assistant that:
- Writes clean, documented code
- Explains complex concepts simply
- Suggests best practices
- Includes error handling
"""
```

### 4. Output Constraints
Control the format:

```python
"""
Answer in exactly:
- 3 bullet points
- Each under 20 words
- Technical but accessible
"""
```

## 🎯 Prompt Patterns

### Pattern 1: Task-Context-Format (TCF)
```
Task: Summarize this article
Context: For technical audience, focus on implementation
Format: 5 bullet points with code examples
```

### Pattern 2: Role-Task-Constraint (RTC)
```
Role: Senior software architect
Task: Review this code for security issues
Constraint: List issues by severity, suggest fixes
```

### Pattern 3: Example-Then-Task (ETT)
```
Example 1: Input → Output
Example 2: Input → Output
Example 3: Input → Output
Now: New Input → ?
```

## 🔑 Key Principles

### ✅ Do This
```python
# Be specific
"Write a Python function that validates email addresses
using regex, returns boolean, includes unit tests"

# Provide context
"This is for a user registration form in a Flask app"

# Specify format
"Return code with docstrings and type hints"

# Set constraints
"Keep function under 15 lines, Python 3.10+"
```

### ❌ Avoid This
```python
# Too vague
"Write code"

# Contradictory
"Be brief but explain everything in detail"

# No context
"Fix this" (without showing what "this" is)

# Unclear format
"Give me some data" (structured how?)
```

## 📊 Measuring Success

### Good Prompt Checklist
- [ ] Clear role/persona defined
- [ ] Specific task described
- [ ] Context provided
- [ ] Output format specified
- [ ] Constraints/limits set
- [ ] Examples included (if needed)

### Quality Metrics
- **First-Try Success**: 70%+ with good prompts
- **Token Efficiency**: 30-50% reduction
- **User Satisfaction**: 80%+ vs 40% with bad prompts

## 🎨 Prompt Templates

### Code Review
```python
"""
You are an expert {language} developer.
Review this code for:
1. Bugs and errors
2. Performance issues
3. Security vulnerabilities
4. Best practices

Code:
```{language}
{code}
```

Provide specific feedback with line numbers.
"""
```

### Data Analysis
```python
"""
Analyze this data:
{data}

Provide:
1. Summary statistics
2. Key insights (3-5 bullet points)
3. Visualizations (describe)
4. Recommendations

Output as JSON.
"""
```

### Creative Writing
```python
"""
Write a {genre} story:
- Setting: {setting}
- Characters: {characters}
- Length: {length} words
- Tone: {tone}
- Include: {must_include}

Start with a hook. End with a twist.
"""
```

## 🚧 Common Mistakes

### Mistake 1: Assuming Knowledge
```python
# ❌ Bad
"Fix the bug"

# ✅ Good
"This Python Flask app has a bug in user authentication.
When users log in, they get redirected incorrectly.
Here's the code and error message..."
```

### Mistake 2: No Format Specification
```python
# ❌ Bad
"Extract information from this text"

# ✅ Good
"Extract information and return as JSON:
{
  'name': string,
  'age': integer,
  'skills': array
}"
```

### Mistake 3: Conflicting Instructions
```python
# ❌ Bad
"Explain in one sentence but be very detailed"

# ✅ Good
"Explain in one clear sentence, then provide
detailed explanation in a separate paragraph"
```

## 📈 Results

### Typical Improvements
- **Accuracy**: 40% → 85%+ with good prompts
- **Consistency**: 50% → 95%+ same task, same output
- **Efficiency**: 5-10 tries → 1-2 tries
- **Cost**: 70% reduction in wasted tokens

### Real-World Impact
- **GitHub Copilot**: Better comments = better code suggestions
- **ChatGPT Users**: Specific prompts = 10x better answers
- **Enterprise AI**: Good prompts = $100K+ in productivity gains

## 📖 Learn More

### Quick Start
1. Start with the TCF pattern (Task-Context-Format)
2. Add examples for complex tasks
3. Iterate based on results
4. Build a prompt library

### Resources
- [OpenAI Prompt Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [Learn Prompting](https://learnprompting.org/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Practice
- Run: `python 07_Prompt_Engineering/examples/system_prompt_tuning.py`
- Read: `07_Prompt_Engineering/examples/few_shot_examples.md`
- Experiment with your own tasks

### Next Topics
- **Advanced**: Chain-of-thought, self-consistency
- **Integration**: Use with RAG, Agents
- **Automation**: Prompt optimization tools

---

**⏱️ Time to Learn Basics**: ~30 minutes

**💰 Impact**: 3-5x productivity improvement

**📈 Skill Curve**: Easy to start, always improving
