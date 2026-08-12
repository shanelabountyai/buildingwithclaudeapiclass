import os
from pathlib import Path

import httpx
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")


def generate_response(prompt: str) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise RuntimeError(
            "ANTHROPIC_API_KEY is missing or still set to the placeholder value. "
            "Update your .env file before running the app."
        )

    http_client = httpx.Client(trust_env=False)
    client = Anthropic(api_key=api_key, http_client=http_client)
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text
