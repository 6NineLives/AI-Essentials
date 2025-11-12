# Few-Shot Learning Examples

## What is Few-Shot Learning?

Few-shot learning is providing the LLM with a few examples of the desired input-output pattern before asking it to complete a new task. This helps the model understand the format, style, and requirements.

## Zero-Shot vs Few-Shot

### Zero-Shot (No Examples)
```
Prompt: "Classify the sentiment of this review: 'This product is terrible!'"
```
→ Model uses only training knowledge

### Few-Shot (With Examples)
```
Prompt: """
Classify sentiment as positive, negative, or neutral.

Review: "This product exceeded my expectations!"
Sentiment: positive

Review: "It's okay, nothing special"
Sentiment: neutral

Review: "Complete waste of money"
Sentiment: negative

Review: "Best purchase I've made this year"
Sentiment:
"""
```
→ Model learns from examples

## Pattern Recognition Examples

### Example 1: Data Extraction

```python
prompt = """
Extract structured information from text.

Text: "John Smith, age 30, works at Google as a Software Engineer"
Output: {
  "name": "John Smith",
  "age": 30,
  "company": "Google",
  "role": "Software Engineer"
}

Text: "Sarah Chen, 28 years old, Data Scientist at Microsoft"
Output: {
  "name": "Sarah Chen",
  "age": 28,
  "company": "Microsoft",
  "role": "Data Scientist"
}

Text: "Mike Johnson, 35, Technical Lead at Amazon"
Output:
"""
```

**Expected Output**:
```json
{
  "name": "Mike Johnson",
  "age": 35,
  "company": "Amazon",
  "role": "Technical Lead"
}
```

### Example 2: Code Translation

```python
prompt = """
Convert Python code to JavaScript.

Python:
def greet(name):
    return f"Hello, {name}!"

JavaScript:
function greet(name) {
    return `Hello, ${name}!`;
}

Python:
def add_numbers(a, b):
    return a + b

JavaScript:
function addNumbers(a, b) {
    return a + b;
}

Python:
def filter_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

JavaScript:
"""
```

**Expected Output**:
```javascript
function filterEvens(numbers) {
    return numbers.filter(n => n % 2 === 0);
}
```

### Example 3: Text Summarization

```python
prompt = """
Summarize text in one sentence, focusing on the main action.

Text: "The company announced quarterly earnings today. Revenue increased by 15% year-over-year. The CEO attributed success to strong product sales and market expansion. Investors reacted positively with stock rising 3%."
Summary: Company reports 15% revenue growth, stock rises 3%.

Text: "Scientists discovered a new species of butterfly in the Amazon rainforest. The butterfly has unique wing patterns and feeds on specific plants. Researchers plan to study its ecosystem role and conservation needs."
Summary: New butterfly species with unique features found in Amazon rainforest.

Text: "The city council approved a new budget including funding for schools, infrastructure repairs, and public safety. The budget passed with a 7-2 vote after weeks of debate and public hearings."
Summary:
"""
```

**Expected Output**:
```
City council approves new budget for schools, infrastructure, and safety with 7-2 vote.
```

### Example 4: Classification

```python
prompt = """
Classify programming questions by difficulty: beginner, intermediate, or advanced.

Question: "How do I print 'Hello World' in Python?"
Difficulty: beginner

Question: "What's the difference between a list and a tuple?"
Difficulty: beginner

Question: "How can I implement a binary search tree?"
Difficulty: intermediate

Question: "How do I optimize database queries using indexing strategies?"
Difficulty: intermediate

Question: "Explain how to implement a distributed consensus algorithm"
Difficulty: advanced

Question: "How do I create a REST API with authentication?"
Difficulty:
"""
```

**Expected Output**:
```
intermediate
```

### Example 5: Format Conversion

```python
prompt = """
Convert casual language to professional tone.

Casual: "Hey, can u send me that doc ASAP?"
Professional: "Could you please send me that document at your earliest convenience?"

Casual: "The project is kinda behind schedule lol"
Professional: "The project is slightly behind schedule."

Casual: "IMO we should just scrap the whole thing"
Professional: "In my opinion, we should consider discontinuing this initiative."

Casual: "That's a really dumb idea tbh"
Professional:
"""
```

**Expected Output**:
```
"I respectfully disagree with that approach."
```

## Best Practices for Few-Shot Prompting

### 1. Use Diverse Examples
```python
# ✅ Good: Diverse cases
examples = [
    "Short text → result",
    "A longer, more complex text with multiple clauses → result",
    "Edge case with special characters!? → result"
]

# ❌ Bad: Repetitive examples
examples = [
    "Text one → result",
    "Text two → result",
    "Text three → result"
]
```

### 2. Show Edge Cases
```python
# Include examples that handle:
- Empty input
- Special characters
- Very long input
- Ambiguous cases
```

### 3. Be Consistent
```python
# ✅ Consistent format
"""
Input: X
Output: Y

Input: X
Output: Y
"""

# ❌ Inconsistent format
"""
Input: X
Result: Y

X → Y
```

### 4. Order Matters
```python
# ✅ Simple to complex
"""
Example 1: Basic case
Example 2: More complex
Example 3: Edge case
"""

# Start with clear, simple examples
# Build to more complex scenarios
```

## Advanced Few-Shot Patterns

### Chain-of-Thought with Examples

```python
prompt = """
Solve math problems step by step.

Problem: If a shirt costs $20 and is on sale for 25% off, what's the final price?
Solution:
1. Calculate discount: $20 × 0.25 = $5
2. Subtract from original: $20 - $5 = $15
Answer: $15

Problem: A book costs $30 and has a 15% discount, plus 8% tax. What's the total?
Solution:
1. Calculate discount: $30 × 0.15 = $4.50
2. Price after discount: $30 - $4.50 = $25.50
3. Calculate tax: $25.50 × 0.08 = $2.04
4. Add tax: $25.50 + $2.04 = $27.54
Answer: $27.54

Problem: A laptop costs $800, has a 20% discount, and 10% tax. What's the final price?
Solution:
"""
```

### Dynamic Few-Shot (RAG)

```python
# Retrieve relevant examples from vector database
def get_examples(task, k=3):
    examples = vector_db.similarity_search(task, k=k)
    return examples

# Build prompt with retrieved examples
task = "Extract email addresses from text"
relevant_examples = get_examples(task)

prompt = f"""
{format_examples(relevant_examples)}

Now apply to: {new_text}
"""
```

## When to Use Few-Shot

### ✅ Use Few-Shot When:
- Task requires specific format
- Need consistent output structure
- Model needs to understand pattern
- You have good examples available
- Zero-shot results are inconsistent

### ❌ Skip Few-Shot When:
- Task is simple and common
- Model already knows the pattern
- Token limit is tight
- Examples would be too long

## Measuring Few-Shot Effectiveness

```python
# Test with different numbers of examples
test_cases = [...] # 100 test cases

# 0-shot
results_0 = [llm(test) for test in test_cases]

# 3-shot
results_3 = [llm(examples[:3] + test) for test in test_cases]

# 5-shot
results_5 = [llm(examples[:5] + test) for test in test_cases]

# Compare accuracy
print(f"0-shot: {accuracy(results_0)}%")
print(f"3-shot: {accuracy(results_3)}%")
print(f"5-shot: {accuracy(results_5)}%")

# Often 3-5 examples is optimal
```

## Summary

Few-shot learning is a powerful technique that:
- ✅ Improves output consistency
- ✅ Reduces need for fine-tuning
- ✅ Works with general-purpose models
- ✅ Easy to update with new examples

**Rule of Thumb**: Start with 3-5 examples, adjust based on results.
