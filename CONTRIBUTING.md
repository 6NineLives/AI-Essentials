# Contributing to AI-Essentials

Thank you for your interest in contributing to AI-Essentials! This guide will help you get started.

## 🎯 Ways to Contribute

### 1. Report Bugs or Issues
Found a bug? [Open an issue](https://github.com/6NineLives/AI-Essentials/issues/new) with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python/Node version)

### 2. Suggest New Content
Have ideas for new topics or examples? We'd love to hear them!
- Check existing issues first
- Open a new issue with the "enhancement" label
- Describe what you'd like to see and why it would be valuable

### 3. Improve Documentation
Help make our docs clearer:
- Fix typos or grammar
- Add missing explanations
- Improve code comments
- Expand "AI in 5 Minutes" summaries

### 4. Add Examples
Contribute new runnable examples:
- Keep examples minimal and focused
- Include clear comments
- Test thoroughly before submitting
- Follow the existing code style

### 5. Expand Resources
Add valuable learning resources:
- Update resources.md files
- Add tutorials, articles, or videos
- Ensure links are high-quality and relevant

## 📝 Contribution Guidelines

### Before You Start
1. **Search existing issues** - Someone might already be working on it
2. **Open an issue first** - For major changes, discuss your idea
3. **Keep it focused** - One improvement per pull request
4. **Test your changes** - Ensure everything works

### Code Standards

#### Python Code
- Use Python 3.10+
- Follow PEP 8 style guidelines
- Include docstrings for functions
- Add type hints where helpful
- Test code runs without errors

Example:
```python
def process_data(input_data: list) -> dict:
    """
    Process input data and return results.
    
    Args:
        input_data: List of data items to process
        
    Returns:
        Dictionary containing processed results
    """
    # Your code here
    pass
```

#### JavaScript/Node.js Code
- Use ES6+ syntax
- Use clear variable names
- Include JSDoc comments
- Test in Node.js 18+

Example:
```javascript
/**
 * Process data and return results
 * @param {Array} inputData - Data to process
 * @returns {Object} Processed results
 */
function processData(inputData) {
    // Your code here
}
```

### Documentation Standards

#### README Files
- Start with a clear overview
- Include visual diagrams where helpful
- Provide runnable code examples
- List use cases
- Link to related topics

#### Code Comments
```python
# ✅ Good: Explains WHY
# Use cosine similarity for better accuracy with normalized vectors
similarity = cosine_distance(vec1, vec2)

# ❌ Bad: Explains WHAT (code already shows this)
# Calculate similarity
similarity = cosine_distance(vec1, vec2)
```

### Example Structure

When adding a new example file:

```python
"""
Brief description of what this example demonstrates.
"""

import required_modules

def main():
    """Run the example"""
    print("=" * 60)
    print("EXAMPLE NAME")
    print("=" * 60)
    
    # 1. Setup
    print("\n1. Setting up...")
    # setup code
    
    # 2. Main demonstration
    print("\n2. Running example...")
    # example code
    
    # 3. Results
    print("\n" + "=" * 60)
    print("✅ Example completed!")
    print("=" * 60)
    print("\n💡 Key takeaways...")

if __name__ == "__main__":
    main()
```

## 🔄 Pull Request Process

### 1. Fork and Clone
```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/AI-Essentials.git
cd AI-Essentials
git remote add upstream https://github.com/6NineLives/AI-Essentials.git
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Your Changes
- Write clear, focused code
- Test everything works
- Update documentation if needed
- Follow the style guidelines

### 4. Test Your Changes
```bash
# Test Python examples
python your_example.py

# Test Node.js examples
node your_example.js

# Run any existing tests
pytest  # if tests exist
```

### 5. Commit Your Changes
Write clear commit messages:
```bash
# ✅ Good commit messages
git commit -m "Add ChromaDB filtering example"
git commit -m "Fix typo in RAG documentation"
git commit -m "Improve error handling in agent example"

# ❌ Bad commit messages
git commit -m "Update"
git commit -m "Fix stuff"
git commit -m "WIP"
```

### 6. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then:
1. Go to GitHub and create a Pull Request
2. Fill out the PR template
3. Link any related issues
4. Wait for review

### PR Guidelines
- **Title**: Clear, descriptive title
- **Description**: Explain what and why
- **Scope**: Keep PRs focused and small
- **Tests**: Verify everything works
- **Documentation**: Update docs if needed

## 🎨 Content Guidelines

### Writing Style
- **Clear and Concise** - Avoid jargon when possible
- **Beginner-Friendly** - Explain concepts simply
- **Practical** - Focus on real-world applications
- **Visual** - Use diagrams where helpful

### Code Examples
- **Minimal** - Only include necessary code
- **Runnable** - Must work out-of-the-box
- **Commented** - Explain non-obvious parts
- **Standalone** - Don't depend on external files

### Learning Resources
When adding to resources.md:
- **Verified** - Test links work
- **Quality** - Only high-quality content
- **Diverse** - Include various formats (videos, articles, docs)
- **Organized** - Group by topic

## 🚫 What NOT to Contribute

Please avoid:
- ❌ Untested code that doesn't run
- ❌ Code with security vulnerabilities
- ❌ Plagiarized content without attribution
- ❌ Promotional or commercial content
- ❌ Large dependencies without good reason
- ❌ Breaking changes without discussion

## 🤔 Questions?

- **General Questions**: [Open a Discussion](https://github.com/6NineLives/AI-Essentials/discussions)
- **Bug Reports**: [Open an Issue](https://github.com/6NineLives/AI-Essentials/issues)
- **Security Issues**: See [SECURITY.md](./SECURITY.md)

## 📜 Code of Conduct

Please note that this project follows a [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## 🎉 Recognition

Contributors will be:
- Listed in our contributors section
- Credited in release notes
- Part of a growing AI community

Thank you for helping make AI-Essentials better for everyone!

---

**Happy Contributing! 🚀**