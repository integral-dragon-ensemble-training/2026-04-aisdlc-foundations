# Scenario 2: Code Refactoring (Architecture & Best Practices)

## Overview
This scenario demonstrates how a coding harness can **improve code architecture** by refactoring a poorly-structured module to follow better design principles. This shows how models understand **software engineering concepts**, not just syntax.

## Principles Demonstrated
- **Code Quality Understanding**: Models can recognize anti-patterns and violations of best practices
- **Architecture Awareness**: Models understand design principles (SRP, DRY, separation of concerns)
- **Composite Tool Usage**: The model must coordinate multiple `read_file` and `edit_file` operations
- **Holistic Problem Solving**: The model must understand how changes to one function affect others
- **Python-Specific Knowledge**: Understanding of Pythonic patterns and standard library

## The Task

"Refactor the `data_processor.py` module to be cleaner and more maintainable:
1. The `process_numbers` function does too much - break it into smaller functions
2. The `validate_and_process` function mixes validation, error handling, and processing
3. Replace manual loops with Python built-in functions where appropriate"

## How the Harness Works Here

1. **Model reads** `demo-source/data_processor.py`
2. **Model analyzes** the code structure and identifies:
   - Repeated patterns in max/min finding and even/odd counting
   - Mixed concerns in validation and processing
   - Inefficient manual loops (could use `sum()`, `min()`, `max()`)
3. **Model proposes refactoring**:
   - Extract `calculate_sum()`, `find_max()`, `find_min()`, `count_evens()`, etc.
   - Create helper functions: `validate_input()`, `convert_to_numbers()`
   - Use built-in functions: `sum(numbers)` instead of manual loop
4. **Harness executes** multiple `edit_file` calls to update the module
5. **Model verifies** the refactored code maintains same behavior

## Expected Output

The model should:
- Create focused helper functions that each have a single responsibility
- Use Pythonic idioms: `sum()`, `max()`, `min()`, list comprehensions
- Separate validation logic from processing logic
- Maintain the same interface for `process_numbers()` and `validate_and_process()`
- Add/improve docstrings explaining the purpose of each function

## Course Learning Objectives

- See how models understand **software engineering principles** (DRY, SRP)
- Understand that tool-use enables **multi-file, coordinated changes**
- Recognize that models can **reason about code quality**, not just correctness
- Learn how harnesses support **architectural decisions** and improvements

## Challenge Extension

Ask the model to:
- "Add type hints to all functions"
- "Create a unit test file that validates all the refactored functions"
- "Create a usage example showing how to use the refactored module"
- "Add error handling with proper exception types and messages"
