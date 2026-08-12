# Classroom Setup - What You Have Ready

## 🎓 For Your Class: Use the Notebook

**File:** `apilcass1.ipynb`

This is your classroom template. It:
- ✅ Loads your API key from `.env`
- ✅ Connects to Claude successfully
- ✅ Works reliably in VS Code

**To use it:**
1. Modify the prompt in the cell
2. Run the cell
3. Show students the response
4. Edit and re-run with different prompts

## 📝 Python Files for Reference

### `app.py`
- Simple entry point
- Shows basic Anthropic SDK usage
- Run with: `python app.py`

### `classroom_starter.py`  
- Documented template with setup steps
- Best for learning the conceptual flow
- Has environment/network constraints when run from terminal
- Use the notebook version instead for reliable class execution

### `src/claude_client.py`
- Reusable helper module
- Import into your own scripts with: `from src.claude_client import generate_response`
- Use if you want to build on top of it

### `test_api.py`
- Diagnostic tool for testing API connectivity

### `beginner_blank.py`
- Blank template for students to code along
- Has comment sections for variables, loops, functions

## 🚀 Quick Start for Class

Run the notebook cell in VS Code. That's it!

If you want to use Python files instead:
```bash
. .venv/bin/activate
python app.py
```

## 🔑 Important Files

- **`.env`** - Your API key (don't commit this)
- **`.venv/`** - Python environment (already installed with anthropic SDK)
- **`.env.example`** - Template showing what `.env` should look like

Everything is set up and working. Use `apilcass1.ipynb` for the class!
