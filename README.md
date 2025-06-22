# Agentic AI Proof of Concept

## Overview

This project is a proof-of-concept demonstrating an agentic AI system. It includes a simple calculator application and a set of tools that an AI agent can use to interact with the file system and execute code. The main purpose is to showcase how an AI can perform tasks by planning and executing a series of actions (function calls).

## How to Run

The primary entry point for the agentic AI system is `main.py`.

1.  **Set up the environment:**
    *   Ensure you have Python 3 installed.
    *   Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   You will need a Gemini API key. You can set it as an environment variable:
        ```bash
        export GEMINI_API_KEY="YOUR_API_KEY"
        ```
        (Replace `"YOUR_API_KEY"` with your actual API key)
        Alternatively, you can create a `.env` file in the root of the project and add your API key there:
        ```
        GEMINI_API_KEY="YOUR_API_KEY"
        ```
        Ensure this `.env` file is added to your `.gitignore` if you plan to commit your project to a public repository.

2.  **Run the agent:**
    Execute the `main.py` script with a prompt for the AI:
    ```bash
    python3 main.py "Your prompt for the AI here"
    ```
    For example:
    ```bash
    python3 main.py "Read the contents of calculator/main.py"
    ```
    You can also run with the `--verbose` flag to see more details about the AI's actions:
    ```bash
    python3 main.py "Your prompt for the AI here" --verbose
    ```

The `calculator/` directory contains a standalone command-line calculator:
```bash
python3 calculator/main.py "3 + 5 * 2"
```

## Tool Functions (for AI)

The AI agent has access to the following tools, defined in the `functions/` directory and orchestrated by `call_function.py`:

*   **`get_files_info(directory: str = None) -> str`**
    *   **Description:** Lists files and directories within a specified path relative to the agent's working directory. If no directory is provided, it lists the contents of the current working directory.
    *   **Output:** A string containing the names, sizes, and whether each item is a directory.

*   **`get_file_content(file_path: str) -> str`**
    *   **Description:** Reads and returns the content of a specified file. The content is truncated if it exceeds a maximum character limit (currently 10,000 characters).
    *   **Output:** The content of the file as a string, or an error message if the file cannot be accessed or read.

*   **`run_python_file(file_path: str, args: list[str] = None) -> str`**
    *   **Description:** Executes a Python file (`.py`) within the agent's working directory. Optional arguments can be passed to the script.
    *   **Output:** A string containing the STDOUT and STDERR from the executed script, or an error message.

*   **`write_file(file_path: str, content: str) -> str`**
    *   **Description:** Writes the given content to a specified file within the agent's working directory. If the file exists, it will be overwritten. If the file or its parent directories do not exist, they will be created.
    *   **Output:** A success message including the number of characters written, or an error message.

These tools are made available to the Gemini model via function calling, allowing the AI to interact with the local environment in a controlled manner. The `call_function.py` script handles the invocation of these tools based on the AI's requests.

## Benefits of Agentic AI

Agentic AI systems, like the one demonstrated in this proof-of-concept, offer several advantages:

*   **Autonomy:** Agents can independently plan and execute sequences of actions to achieve a given goal, reducing the need for step-by-step human guidance.
*   **Task Decomposition:** Complex tasks can be broken down into smaller, manageable steps that the agent can execute using its available tools.
*   **Tool Use:** By providing agents with specific tools (like file system operations or code execution), they can interact with and manipulate their environment in meaningful ways. This extends their capabilities beyond simple text generation.
*   **Adaptability:** Agents can potentially adapt their plans based on the outcomes of their actions or changes in the environment.
*   **Efficiency:** For certain tasks, an agent can automate processes that would be tedious or time-consuming for humans.
*   **Interactive Problem Solving:** Agents can engage in a dialogue (through prompts and responses, including function calls and results) to collaboratively solve problems.

This project serves as a basic illustration of these principles. More advanced agentic systems can incorporate more sophisticated planning, learning, and reasoning capabilities.
