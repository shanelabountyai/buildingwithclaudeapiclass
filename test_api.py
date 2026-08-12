#!/usr/bin/env python3
"""Test Anthropic API connection using curl (workaround for DNS issues)."""
import os
import sys
import json
import subprocess
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root
project_root = Path(__file__).parent
load_dotenv(dotenv_path=project_root / ".env")

print(f"Python: {sys.executable}")
print(f"Project: {project_root}")

api_key = os.getenv("ANTHROPIC_API_KEY")
print(f"API key loaded: {bool(api_key)}")

if not api_key or api_key == "your_api_key_here":
    print("ERROR: ANTHROPIC_API_KEY is missing or placeholder")
    print("Add your real key to .env and try again")
    sys.exit(1)

print("\nMaking API request via curl...")

# Build curl command
payload = {
    "model": "claude-3-5-haiku-20241022",
    "max_tokens": 200,
    "messages": [{"role": "user", "content": "What is quantum computing in one sentence?"}]
}

cmd = [
    "curl", "-s",
    "-H", f"x-api-key: {api_key}",
    "-H", "anthropic-version: 2023-06-01",
    "-H", "content-type: application/json",
    "-d", json.dumps(payload),
    "https://api.anthropic.com/v1/messages"
]

result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode != 0:
    print(f"Error: {result.stderr}")
    sys.exit(1)

response = json.loads(result.stdout)
if "error" in response:
    print(f"API Error: {response['error']}")
    sys.exit(1)

print("\nResponse:")
print(response["content"][0]["text"])
