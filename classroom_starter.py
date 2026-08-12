"""
Classroom Starter Template for Anthropic API
==============================================

This file demonstrates how to:
1. Load your API key from .env
2. Create an Anthropic client
3. Send a message to Claude
4. Handle responses and errors

Setup Instructions:
1. Make sure your .env file has your real API key:
   ANTHROPIC_API_KEY=your-key-here

2. Run this file from the terminal:
   python classroom_starter.py

3. Modify the prompt and experiment!
"""

import subprocess
from pathlib import Path
import os

# ============================================================================
# STEP 1: Load your API key from the .env file
# ============================================================================

# Find the .env file in the project root
env_file = Path(__file__).parent / ".env"

if not env_file.exists():
    print("ERROR: .env file not found!")
    print(f"Expected at: {env_file}")
    exit(1)

# Read the API key from .env
api_key = None
with open(env_file) as f:
    for line in f:
        if line.startswith("ANTHROPIC_API_KEY="):
            api_key = line.split("=", 1)[1].strip()
            break

if not api_key or api_key == "your_api_key_here":
    print("ERROR: ANTHROPIC_API_KEY is missing or still a placeholder!")
    print(f"Edit your .env file and add your real key")
    exit(1)

print(f"✓ API key loaded ({len(api_key)} characters)")

# ============================================================================
# STEP 2: Create and execute Claude request
# ============================================================================

# You can modify this prompt to experiment!
prompt = "What is quantum computing in one sentence?"

print(f"\nSending prompt: {prompt}")
print("-" * 60)

# Run the API call in Python (using subprocess to avoid environment issues)
python_code = f"""
import os
os.environ["ANTHROPIC_API_KEY"] = "{api_key}"

from anthropic import Anthropic

client = Anthropic()
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=200,
    messages=[{{"role": "user", "content": "{prompt}"}}]
)

print(response.content[0].text)
print("---METADATA---")
print(f"Model: {{response.model}}")
print(f"Input tokens: {{response.usage.input_tokens}}")
print(f"Output tokens: {{response.usage.output_tokens}}")
"""

result = subprocess.run(
    [str(Path(__file__).parent / ".venv/bin/python"), "-c", python_code],
    capture_output=True,
    text=True,
    cwd=Path(__file__).parent,
    env={k: v for k, v in os.environ.items() if not k.upper().endswith(("_PROXY", "PROXY"))}
)

if result.returncode != 0:
    print(f"ERROR: {result.stderr}")
    exit(1)

# Parse and display the output
output_lines = result.stdout.strip().split("\n")
if "---METADATA---" in result.stdout:
    # Split response and metadata
    response_end = result.stdout.index("---METADATA---")
    response_text = result.stdout[:response_end].strip()
    metadata = result.stdout[response_end + len("---METADATA---"):].strip()
    
    print(response_text)
    print("-" * 60)
    print(f"\n✓ Request successful!")
    print(metadata)
else:
    print(result.stdout)
    print("-" * 60)
    print(f"\n✓ Request successful!")


# ============================================================================
# CLASSROOM CHALLENGES
# ============================================================================
# Try modifying this file to:
#
# 1. Change the prompt to ask a different question
# 2. Use a different model (change "claude-haiku-4-5-20251001" to something else)
# 3. Add a loop to ask multiple questions in a row
# 4. Create a conversation where Claude remembers previous messages
# 5. Extract just the token count and print it differently
#
# ============================================================================

