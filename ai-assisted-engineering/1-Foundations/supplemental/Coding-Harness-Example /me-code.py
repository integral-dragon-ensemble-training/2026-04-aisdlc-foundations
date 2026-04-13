"""
Interactive Coding Harness using Claude (Anthropic)

This harness implements an interactive agent loop where Claude can read, list,
and edit files in response to user requests. The agent communicates tool
invocations using a simple text format, which the harness then executes.

Flow:
1. User provides a task description
2. Claude suggests tool invocations using 'tool: TOOL_NAME({JSON_ARGS})' format
3. Harness executes the tool and returns the result to Claude
4. Claude continues until the task is complete

API calls are logged to the 'api-logs' directory for inspection and debugging.
"""

import inspect
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

from anthropic import Anthropic

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def initialize_api_client():
    """
    Initialize the Anthropic API client with proper environment setup.

    Checks for the ANTHROPIC_API_KEY in this order:
    1. Shell environment variable (set via 'export ANTHROPIC_API_KEY=...')
    2. .env file in the current directory (loaded via python-dotenv)
    3. .env file in the project root

    Returns:
        Anthropic client instance

    Raises:
        ValueError: If API key is not found or is empty
    """
    # Try to load .env file if python-dotenv is available
    if load_dotenv:
        # Load from .env in current directory first
        load_dotenv(dotenv_path=".env", verbose=False)
        # Also check project root
        load_dotenv(dotenv_path=Path.cwd() / ".env", verbose=False)

    # Get API key from environment
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()

    if not api_key:
        error_msg = (
            "\n"
            "❌ ANTHROPIC_API_KEY not found!\n\n"
            "Please set it in one of these ways:\n"
            "  1. Shell environment: export ANTHROPIC_API_KEY='sk-ant-...'\n"
            "  2. .env file in project root: ANTHROPIC_API_KEY=sk-ant-...\n"
            "  3. .env file in current directory: ANTHROPIC_API_KEY=sk-ant-...\n\n"
            "Get your API key from: https://console.anthropic.com/\n"
        )
        print(error_msg, file=sys.stderr)
        sys.exit(1)

    # Validate that the key looks reasonable (basic sanity check)
    if len(api_key) < 10:
        print(
            "⚠️  Warning: ANTHROPIC_API_KEY seems unusually short. "
            "Make sure it's set correctly.",
            file=sys.stderr
        )

    try:
        return Anthropic(api_key=api_key)
    except Exception as e:
        print(
            f"❌ Failed to initialize Anthropic client: {e}",
            file=sys.stderr
        )
        sys.exit(1)


# Initialize the API client
client = initialize_api_client()

# Setup API logging directory
API_LOG_DIR = Path.cwd() / "api-logs"
API_LOG_DIR.mkdir(exist_ok=True)

# Terminal color codes for better visual distinction between user and assistant
USER_COLOR = "\u001b[94m"       # Blue
ASSISTANT_COLOR = "\u001b[93m"  # Yellow
API_LOG_COLOR = "\u001b[36m"    # Cyan
API_INPUT_COLOR = "\u001b[35m"  # Magenta
API_OUTPUT_COLOR = "\u001b[32m" # Green
RESET_COLOR = "\u001b[0m"

# System prompt that instructs Claude how to use the available tools
SYSTEM_PROMPT = """
You are a coding assistant designed to help solve coding tasks using file operations.

You have access to the following tools:

{tool_list_repr}

IMPORTANT: When you want to use a tool, reply with EXACTLY one line in this format:
    tool: TOOL_NAME({{JSON_ARGS}})

Use compact single-line JSON with double quotes. Do not include any other text on the tool invocation line.

After you receive the tool result, continue working on the task until it's complete.
If no tool is needed, respond naturally in English.
"""


import subprocess

def resolve_abs_path(path_str: str) -> Path:
    """
    Convert a relative or absolute path to an absolute Path object.

    Examples:
        "file.py" -> "/Users/home/user/project/file.py" (relative to cwd)
        "~/documents/file.py" -> "/Users/home/user/documents/file.py"
        "/absolute/path/file.py" -> "/absolute/path/file.py"
    """
    path = Path(path_str).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    return path


# ============================================================================
# PYTHON BACKEND - File operations using Python's built-in functions
# ============================================================================

def read_file_python(filename: str) -> Dict[str, Any]:
    """
    Read and return the full content of a file (Python backend).

    Args:
        filename: Path to the file to read (relative or absolute)

    Returns:
        Dictionary with 'file_path' (absolute path) and 'content' (file contents)
    """
    full_path = resolve_abs_path(filename)
    with open(str(full_path), "r") as f:
        content = f.read()
    return {
        "file_path": str(full_path),
        "content": content
    }


def list_files_python(path: str) -> Dict[str, Any]:
    """
    List all files and directories in a given directory (Python backend).

    Args:
        path: Directory path to list (relative or absolute)

    Returns:
        Dictionary with 'path' (absolute path) and 'files' (list of items with name/type)
    """
    full_path = resolve_abs_path(path)
    all_files = []
    for item in full_path.iterdir():
        all_files.append({
            "filename": item.name,
            "type": "file" if item.is_file() else "dir"
        })
    return {
        "path": str(full_path),
        "files": all_files
    }


def edit_file_python(path: str, old_str: str, new_str: str) -> Dict[str, Any]:
    """
    Replace or create file content (Python backend).

    If old_str is empty, creates or overwrites the file with new_str.
    Otherwise, replaces the first occurrence of old_str with new_str.

    Args:
        path: Path to the file to edit (relative or absolute)
        old_str: String to replace (empty string to create new file)
        new_str: Replacement string or new file content

    Returns:
        Dictionary indicating success or describing what happened
    """
    full_path = resolve_abs_path(path)

    # Create or overwrite file if old_str is empty
    if old_str == "":
        full_path.write_text(new_str, encoding="utf-8")
        return {
            "path": str(full_path),
            "action": "created_file"
        }

    # Replace first occurrence of old_str
    original = full_path.read_text(encoding="utf-8")
    if original.find(old_str) == -1:
        return {
            "path": str(full_path),
            "action": "old_str not found",
            "details": f"Could not find '{old_str}' in file"
        }

    edited = original.replace(old_str, new_str, 1)
    full_path.write_text(edited, encoding="utf-8")
    return {
        "path": str(full_path),
        "action": "edited"
    }


# ============================================================================
# BASH BACKEND - File operations using shell commands
# ============================================================================

def read_file_bash(filename: str) -> Dict[str, Any]:
    """
    Read and return the full content of a file (Bash backend).

    Uses: cat <file>

    Args:
        filename: Path to the file to read (relative or absolute)

    Returns:
        Dictionary with 'file_path' (absolute path) and 'content' (file contents)
    """
    full_path = resolve_abs_path(filename)
    try:
        result = subprocess.run(
            ["cat", str(full_path)],
            capture_output=True,
            text=True,
            check=True
        )
        return {
            "file_path": str(full_path),
            "content": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "file_path": str(full_path),
            "error": e.stderr or "File not found"
        }


def list_files_bash(path: str) -> Dict[str, Any]:
    """
    List all files and directories in a given directory (Bash backend).

    Uses: ls -1 <directory>

    Args:
        path: Directory path to list (relative or absolute)

    Returns:
        Dictionary with 'path' (absolute path) and 'files' (list of items with name/type)
    """
    full_path = resolve_abs_path(path)
    try:
        result = subprocess.run(
            ["ls", "-1", str(full_path)],
            capture_output=True,
            text=True,
            check=True
        )
        all_files = []
        for filename in result.stdout.strip().split("\n"):
            if filename:
                file_path = full_path / filename
                is_file = file_path.is_file()
                all_files.append({
                    "filename": filename,
                    "type": "file" if is_file else "dir"
                })
        return {
            "path": str(full_path),
            "files": all_files
        }
    except subprocess.CalledProcessError as e:
        return {
            "path": str(full_path),
            "error": e.stderr or "Directory not found"
        }


def edit_file_bash(path: str, old_str: str, new_str: str) -> Dict[str, Any]:
    """
    Replace or create file content (Bash backend).

    Uses: sed -i (in-place editing) or echo (file creation)

    If old_str is empty, creates or overwrites the file with new_str.
    Otherwise, replaces the first occurrence of old_str with new_str.

    Args:
        path: Path to the file to edit (relative or absolute)
        old_str: String to replace (empty string to create new file)
        new_str: Replacement string or new file content

    Returns:
        Dictionary indicating success or describing what happened
    """
    full_path = resolve_abs_path(path)

    try:
        # Create or overwrite file if old_str is empty
        if old_str == "":
            result = subprocess.run(
                f"echo {repr(new_str)} > {repr(str(full_path))}",
                shell=True,
                capture_output=True,
                text=True
            )
            return {
                "path": str(full_path),
                "action": "created_file",
                "backend": "bash (echo)"
            }

        # Replace first occurrence of old_str using sed
        # Escape special characters for sed
        escaped_old = old_str.replace("/", "\\/").replace("&", "\\&")
        escaped_new = new_str.replace("/", "\\/").replace("&", "\\&")

        result = subprocess.run(
            f"sed -i '' 's/{escaped_old}/{escaped_new}/' {repr(str(full_path))}",
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return {
                "path": str(full_path),
                "action": "edited",
                "backend": "bash (sed)"
            }
        else:
            return {
                "path": str(full_path),
                "action": "old_str not found",
                "error": result.stderr
            }
    except Exception as e:
        return {
            "path": str(full_path),
            "error": str(e)
        }


# ============================================================================
# TOOL REGISTRY SELECTION
# ============================================================================

def get_backend() -> str:
    """
    Determine which backend to use based on environment variable.
    Default: python
    """
    return os.environ.get("HARNESS_BACKEND", "python").lower()


# Select tools based on backend
BACKEND = get_backend()
if BACKEND == "bash":
    read_file_tool = read_file_bash
    list_files_tool = list_files_bash
    edit_file_tool = edit_file_bash
else:
    read_file_tool = read_file_python
    list_files_tool = list_files_python
    edit_file_tool = edit_file_python


# Registry of available tools
TOOL_REGISTRY = {
    "read_file": read_file_tool,
    "list_files": list_files_tool,
    "edit_file": edit_file_tool
}


def get_tool_str_representation(tool_name: str) -> str:
    """
    Generate a human-readable description of a tool's interface.
    Includes the docstring, signature, and parameter details.
    """
    tool = TOOL_REGISTRY[tool_name]
    return f"""
    Name: {tool_name}
    Description: {tool.__doc__}
    Signature: {inspect.signature(tool)}
    """


def print_tool_registry():
    """
    Display all available tools in a formatted list for the user.
    """
    print(f"\n{API_LOG_COLOR}Available Tools:{RESET_COLOR}")
    for tool_name in TOOL_REGISTRY:
        tool = TOOL_REGISTRY[tool_name]
        # Get first line of docstring
        doc_first_line = (tool.__doc__ or "").split('\n')[0].strip()
        print(f"  • {tool_name}: {doc_first_line}")
    print()


def get_full_system_prompt() -> str:
    """
    Build the complete system prompt by listing all available tools.
    Claude uses this to understand what it can do.
    """
    tool_descriptions = ""
    for tool_name in TOOL_REGISTRY:
        tool_descriptions += "TOOL\n" + "=" * 20 + get_tool_str_representation(tool_name)
        tool_descriptions += f"\n{'='*20}\n"

    return SYSTEM_PROMPT.format(tool_list_repr=tool_descriptions)


def extract_tool_invocations(text: str) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Parse Claude's response to extract tool invocations.

    Looks for lines in the format: 'tool: TOOL_NAME({...})'
    Returns a list of (tool_name, args_dict) tuples.

    Args:
        text: The response text from Claude

    Returns:
        List of (tool_name, args) tuples to execute
    """
    invocations = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("tool:"):
            continue

        try:
            # Remove "tool:" prefix and parse the rest
            after = line[len("tool:"):].strip()
            name, rest = after.split("(", 1)
            name = name.strip()

            if not rest.endswith(")"):
                continue

            # Extract JSON arguments
            json_str = rest[:-1].strip()
            args = json.loads(json_str)
            invocations.append((name, args))
        except (ValueError, json.JSONDecodeError):
            # Silently skip malformed invocations
            continue

    return invocations


def execute_tool(tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute a single tool with the given arguments.
    Logs the command being executed.

    Args:
        tool_name: Name of the tool to execute
        args: Dictionary of arguments for the tool

    Returns:
        The tool's return value (usually a dict with status info)
    """
    if tool_name not in TOOL_REGISTRY:
        return {
            "error": f"Unknown tool: {tool_name}",
            "available_tools": list(TOOL_REGISTRY.keys())
        }

    tool_func = TOOL_REGISTRY[tool_name]

    # Build command string for display
    args_json = json.dumps(args, separators=(',', ': '))
    command_str = f"tool: {tool_name}({args_json})"
    print(f"{API_INPUT_COLOR}→ {command_str}{RESET_COLOR}")

    try:
        # Call the tool with its expected arguments
        if tool_name == "read_file":
            result = tool_func(args.get("filename", "."))
        elif tool_name == "list_files":
            result = tool_func(args.get("path", "."))
        elif tool_name == "edit_file":
            result = tool_func(
                args.get("path", "."),
                args.get("old_str", ""),
                args.get("new_str", "")
            )
        else:
            return {"error": f"Tool {tool_name} not implemented"}

        return result
    except Exception as e:
        return {
            "error": f"Tool execution failed: {str(e)}",
            "tool_name": tool_name,
            "args": args
        }


def write_api_logs(conversation: List[Dict[str, str]], response_text: str):
    """
    Write complete API request and response to numbered JSON files.

    Creates:
    - 001-request.json / 001-response.json
    - 002-request.json / 002-response.json
    - etc.

    Each file contains the COMPLETE untruncated data for inspection.
    """
    # Find the next call number
    existing_files = list(API_LOG_DIR.glob("*-request.json"))
    call_number = len(existing_files) + 1
    call_num_str = f"{call_number:03d}"  # Format as 001, 002, etc.

    timestamp = datetime.now().isoformat()

    # Write full request
    request_file = API_LOG_DIR / f"{call_num_str}-request.json"
    request_data = {
        "call_number": call_number,
        "timestamp": timestamp,
        "system_prompt": get_full_system_prompt(),
        "messages": conversation,
        "model": "claude-opus-4-6",
        "max_tokens": 4096
    }
    request_file.write_text(json.dumps(request_data, indent=2))

    # Write full response
    response_file = API_LOG_DIR / f"{call_num_str}-response.json"
    response_data = {
        "call_number": call_number,
        "timestamp": timestamp,
        "response": response_text,
        "response_length": len(response_text),
        "has_tool_invocations": "tool:" in response_text
    }
    response_file.write_text(json.dumps(response_data, indent=2))

    # Print console notification
    print(f"{API_LOG_COLOR}✓ Call #{call_number} logged → {call_num_str}-request.json, {call_num_str}-response.json{RESET_COLOR}")


def log_api_call(conversation: List[Dict[str, str]]):
    """
    Display that request is being made.
    Full request details logged to numbered JSON file.
    """
    print(f"\n{API_LOG_COLOR}📤 API REQUEST (logging...){RESET_COLOR}")


def log_api_response(response_text: str):
    """
    Display that response was received.
    Full response details logged to numbered JSON file.
    """
    print(f"{API_LOG_COLOR}📥 API RESPONSE (logged){RESET_COLOR}\n")


def execute_llm_call(conversation: List[Dict[str, str]]) -> str:
    """
    Send a conversation to Claude and get back the response.

    Logs both the request and response to files and console.

    Args:
        conversation: List of message dicts with 'role' and 'content'

    Returns:
        Claude's response text

    Raises:
        Exception: If the API call fails
    """
    # Display console notification
    log_api_call(conversation)

    try:
        # Make the API call
        response = client.messages.create(
            model="claude-opus-4-6",  # Latest Claude model (change to claude-sonnet-4-6 for faster/cheaper)
            max_tokens=4096,
            system=get_full_system_prompt(),
            messages=conversation
        )

        response_text = response.content[0].text

        # Write full logs to files
        write_api_logs(conversation, response_text)

        # Display console notification
        log_api_response(response_text)

        return response_text

    except Exception as e:
        error_msg = f"\n❌ API Error: {str(e)}\n"
        print(error_msg, file=sys.stderr)
        raise


def run_coding_agent_loop():
    """
    Main interactive loop that orchestrates the agent.

    Flow:
    1. Initialize conversation with system prompt
    2. Get user input
    3. Send to Claude
    4. While Claude requests tools:
       a. Parse tool invocations from Claude's response
       b. Execute each tool
       c. Send tool results back to Claude
    5. Display Claude's final response
    6. Repeat
    """
    print("\n" + "=" * 70)
    print("Claude Coding Harness")
    print("=" * 70)
    print(f"\n🔧 Backend: {BACKEND.upper()}", end="")
    if BACKEND == "python":
        print(" (Python file operations)")
    elif BACKEND == "bash":
        print(" (Shell/Bash commands)")
    else:
        print()

    print_tool_registry()

    print("📊 API Logging".center(70))
    print("Each API call is logged with complete request/response in:")
    print("  api-logs/001-request.json  & api-logs/001-response.json")
    print("  api-logs/002-request.json  & api-logs/002-response.json")
    print("  api-logs/003-request.json  & api-logs/003-response.json")
    print("  ... (numbered sequentially)")
    print("=" * 70)
    print("\n💡 Switch backend: HARNESS_BACKEND=bash ./run.sh")
    print("   Or run with Python (default): ./run.sh\n")

    # Initialize conversation with system prompt
    conversation = []

    while True:
        try:
            user_input = input(f"{USER_COLOR}You:{RESET_COLOR} ").strip()
            if not user_input:
                continue
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

        # Add user message to conversation
        conversation.append({
            "role": "user",
            "content": user_input
        })

        # Agentic loop: keep getting Claude's responses until it stops requesting tools
        while True:
            try:
                # Get Claude's response
                assistant_response = execute_llm_call(conversation)

                # Check if Claude is requesting any tool executions
                tool_invocations = extract_tool_invocations(assistant_response)

                if not tool_invocations:
                    # No tools requested - display the final response and store in conversation
                    print(f"{ASSISTANT_COLOR}Claude:{RESET_COLOR} {assistant_response}\n")
                    conversation.append({
                        "role": "assistant",
                        "content": assistant_response
                    })
                    break

                # Store Claude's response with tool invocations in conversation
                conversation.append({
                    "role": "assistant",
                    "content": assistant_response
                })

                # Execute each tool and collect results
                print(f"{ASSISTANT_COLOR}Claude is executing tools:{RESET_COLOR}\n")
                for tool_name, args in tool_invocations:
                    print(f"  🔧 {tool_name}({json.dumps(args)[:60]}...)")
                    result = execute_tool(tool_name, args)

                    # Add tool result to conversation for Claude to process
                    tool_result_msg = f"tool_result({json.dumps(result)})"
                    conversation.append({
                        "role": "user",
                        "content": tool_result_msg
                    })

                print()  # Add spacing between iterations

            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break
            except Exception as e:
                print(f"{ASSISTANT_COLOR}Error:{RESET_COLOR} {str(e)}", file=sys.stderr)
                print("Continuing...\n")
                break


if __name__ == "__main__":
    run_coding_agent_loop()
