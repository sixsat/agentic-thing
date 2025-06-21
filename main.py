import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import call_function, available_functions


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
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    response = client.models.generate_content(
        # https://ai.google.dev/gemini-api/docs/models
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if isVerbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if not response.function_calls:
        print(response.text)
        return

    function_responses = []
    for func in response.function_calls:
        result = call_function(func, isVerbose)
        if not result.parts or not result.parts[0].function_response:
            raise Exception("empty function call result")
        if isVerbose:
            print(f"-> {result.parts[0].function_response.response}")
        function_responses.append(result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")


if __name__ == "__main__":
    main()
