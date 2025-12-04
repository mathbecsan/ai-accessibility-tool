# Contributing to LearnEasy

Thank you for your interest in contributing to LearnEasy! We appreciate your efforts to improve this AI accessibility tool. This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Contributions](#making-contributions)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

---

## 🤝 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please:

- Be respectful and constructive in all interactions
- Welcome diverse perspectives and experiences
- Focus on what is best for the community
- Show empathy towards other community members

Unacceptable behavior includes harassment, discrimination, and disrespectful comments.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account
- Familiarity with Git and GitHub workflows

### Initial Setup

1. **Fork the Repository**

   - Click the "Fork" button on the repository page
   - This creates a copy under your GitHub account

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-accessibility-tool.git
   cd ai-accessibility-tool
   ```

3. **Add Upstream Remote**

   ```bash
   git remote add upstream https://github.com/Chaiya8/ai-accessibility-tool.git
   ```

4. **Verify Remotes**
   ```bash
   git remote -v
   # origin = your fork
   # upstream = original repository
   ```

---

## 🛠️ Development Setup

### Step 1: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Create Feature Branch

```bash
git checkout -b feature/YourFeatureName
```

Use descriptive branch names:

- `feature/add-multilingual-support`
- `bugfix/fix-tts-crash`
- `docs/improve-readme`

---

## ✨ Making Contributions

### Types of Contributions

We welcome several types of contributions:

1. **Bug Fixes** – Fix existing issues
2. **New Features** – Add new functionality
3. **Documentation** – Improve README, docs, and comments
4. **Performance** – Optimize code for better performance
5. **Tests** – Add or improve test coverage
6. **Translations** – Help translate content

### Before You Start

1. **Check Existing Issues** – Avoid duplicate work
2. **Discuss Major Changes** – Open an issue first for large features
3. **Read the Code** – Familiarize yourself with the codebase

---

## 📝 Commit Guidelines

### Commit Message Format

Use clear, descriptive commit messages:

```
[TYPE] Brief description (50 characters or less)

Detailed explanation of the change, if necessary.
Include:
- What was changed
- Why it was changed
- Any relevant issue numbers

Examples:
[FEATURE] Add multi-language support for TTS
[BUGFIX] Fix crash when processing empty text
[DOCS] Improve API documentation examples
[REFACTOR] Simplify run_instruction function
[TEST] Add unit tests for text simplification
```

### Commit Types

- `FEATURE` – New functionality
- `BUGFIX` – Bug fix
- `DOCS` – Documentation changes
- `REFACTOR` – Code refactoring without functional changes
- `TEST` – Adding or updating tests
- `STYLE` – Code style/formatting changes
- `PERF` – Performance improvements

### Best Practices

- Make small, logical commits
- Commit frequently
- Write meaningful messages
- Reference issues in commits: `Fixes #123`

---

## 🔄 Pull Request Process

### Creating a Pull Request

1. **Sync with Upstream**

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

3. **Open Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template completely

### PR Title Format

```
[TYPE] Brief description

Examples:
[FEATURE] Add support for PDF input files
[BUGFIX] Fix incorrect text simplification for numbers
[DOCS] Add API usage examples
```

### PR Description Template

```markdown
## Description

Brief explanation of the changes

## Related Issues

Fixes #123
Related to #456

## Changes

- Change 1
- Change 2
- Change 3

## Type of Change

- [ ] New feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Breaking change

## Testing

Describe how you tested the changes

## Screenshots (if applicable)

Include relevant screenshots

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No new warnings generated
```

### Review Process

- At least one maintainer review required
- All CI checks must pass
- Address feedback promptly
- Request re-review after changes

---

## 🎨 Coding Standards

### Python Style Guide

We follow PEP 8 with these conventions:

```python
# Use 4 spaces for indentation
# Line length: max 100 characters
# Use meaningful variable names

def run_instruction(text: str, mode: str, level: str = "6th grade") -> str:
    """
    Brief one-line description.

    Longer description if needed, explaining the function's purpose,
    parameters, and return value.

    Args:
        text (str): The input text to process
        mode (str): Transformation mode (simplify, summarize, etc.)
        level (str): Reading level for simplification

    Returns:
        str: Transformed text

    Raises:
        ValueError: If mode is not supported
    """
    pass
```

### Code Organization

```python
# 1. Imports (standard library, then third-party, then local)
import os
from io import BytesIO

from transformers import T5Tokenizer
import streamlit as st

from backend.simplify import run_instruction

# 2. Constants
DEFAULT_MODEL = "google/flan-t5-small"
SUPPORTED_LANGUAGES = ["en", "es", "fr"]

# 3. Functions (organized by purpose)
def helper_function():
    pass

def main_function():
    pass

# 4. Main execution
if __name__ == "__main__":
    main_function()
```

### Naming Conventions

- **Variables & Functions:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Private members:** `_leading_underscore`

### Comments & Documentation

- Write clear, concise comments
- Avoid obvious comments
- Update comments when code changes
- Use docstrings for functions and classes

---

## ✅ Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_simplify.py

# Run with coverage
pytest --cov=backend tests/
```

### Writing Tests

```python
import pytest
from backend.simplify import run_instruction

def test_simplify_basic_text():
    """Test basic text simplification"""
    text = "The photosynthetic process converts light energy into chemical energy."
    result = run_instruction(text, mode="simplify", level="3rd grade")
    assert len(result) < len(text)
    assert result is not None

def test_invalid_mode():
    """Test error handling for invalid mode"""
    with pytest.raises(ValueError):
        run_instruction("test text", mode="invalid_mode")
```

### Test Coverage

- Aim for >80% test coverage
- Test edge cases and error conditions
- Include both unit and integration tests

---

## 🐛 Reporting Bugs

### Bug Report Template

**Title:** Brief description of the bug

```markdown
## Description

Clear description of the bug

## Steps to Reproduce

1. Step 1
2. Step 2
3. Step 3

## Expected Behavior

What should happen

## Actual Behavior

What actually happens

## Environment

- OS: [e.g., macOS 12.0]
- Python: [e.g., 3.9.0]
- Browser: [if applicable]

## Screenshots

[If applicable]

## Additional Context

Any other relevant information
```

### Good Bug Reports Include

- Clear, descriptive title
- Step-by-step reproduction
- Expected vs actual behavior
- System information
- Screenshots/error logs (if applicable)

---

## 💡 Suggesting Enhancements

### Enhancement Request Template

**Title:** Brief description of enhancement

```markdown
## Description

Explain the enhancement and why it would be useful

## Use Case

Real-world scenario where this would help

## Proposed Solution

How you envision this feature working

## Alternatives Considered

Other possible approaches

## Additional Context

Relevant information or examples
```

---

## 📚 Documentation Contributions

### Improving Documentation

1. **README Updates**

   - Clarify unclear sections
   - Add examples
   - Fix typos or outdated info

2. **Code Comments**

   - Explain complex logic
   - Add docstrings to functions
   - Document edge cases

3. **New Guides**
   - Create tutorials
   - Add troubleshooting guides
   - Document best practices

---

## ❓ Questions?

- Check existing GitHub Issues
- Review discussions in GitHub Discussions
- Open a new issue if needed

---

## 🎉 Recognition

Contributors will be recognized in:

- README.md contributors section
- GitHub contributors page
- Release notes

---

**Thank you for contributing to LearnEasy! Your efforts make a difference in making education more accessible.**
