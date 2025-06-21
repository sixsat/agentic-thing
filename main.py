import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    isVerbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print('Usage: python main.py "your prompt here" [--verbose]')
        sys.exit(1)

    user_prompt = " ".join(args)
    if isVerbose:
        print(f"User prompt: {user_prompt}\n")

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages, isVerbose)


def generate_content(client, messages, isVerbose):
    response = client.models.generate_content(
        # https://ai.google.dev/gemini-api/docs/models
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(response.text)
    if isVerbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
