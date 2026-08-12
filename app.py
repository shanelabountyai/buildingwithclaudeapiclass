from src.claude_client import generate_response


if __name__ == "__main__":
    prompt = "Say hello in one sentence."
    print(generate_response(prompt))
