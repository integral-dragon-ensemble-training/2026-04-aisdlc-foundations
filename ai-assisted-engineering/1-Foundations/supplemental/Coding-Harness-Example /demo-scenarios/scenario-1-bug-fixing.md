# Scenario 1: Bug Fixing (Simple Error Handling)

## Overview
This scenario demonstrates how a coding harness enables a model to **identify and fix bugs** by reading source code, understanding the problem, and implementing a fix.

## Principles Demonstrated
- **Context Awareness**: The model reads the actual source code to understand the bug
- **Tool Usage**: The model uses `read_file` and `edit_file` tools to interact with code
- **Iterative Problem Solving**: The model can test, verify, and iterate on fixes
- **Error Understanding**: Models can parse error messages and map them to code locations

## The Task

"Fix the bugs in the calculator module. Specifically:
1. The `divide` function crashes when dividing by zero
2. The `factorial` function doesn't handle negative numbers properly"

## How the Harness Works Here

1. **Model reads** `demo-source/calculator.py` using the `read_file` tool
2. **Model identifies** the bugs in the division and factorial functions
3. **Model suggests fixes**:
   - Add zero-check in `divide()` with appropriate error handling
   - Add validation in `factorial()` for negative inputs
4. **Harness executes** the `edit_file` tool with the replacement code
5. **Model verifies** by reading the file again and confirming changes

## Expected Output

The model should:
- Recognize that `divide(a, b)` will crash with `ZeroDivisionError`
- Propose adding an if-statement check: `if b == 0: raise ValueError("Cannot divide by zero")`
- Add input validation to factorial: `if n < 0: raise ValueError("Factorial not defined for negative numbers")`
- Explain why these fixes prevent runtime errors

## Course Learning Objectives

- Understand how models can **reason about code they haven't written**
- See how **tool-use enables code modification** without human interaction
- Recognize that models can **understand domain knowledge** (math, error handling patterns)

## Challenge Extension

Ask the model to:
- "Add unit tests for these functions"
- "Add logging to the divide function to track errors"
- "Refactor the factorial function to use recursion instead of loops"
