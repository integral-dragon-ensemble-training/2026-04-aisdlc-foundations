# Scenario 3: Feature Addition (Planning & Implementation)

## Overview
This scenario demonstrates how a coding harness can **implement new features** by understanding existing code, planning the implementation, and executing coordinated changes across multiple files.

## Principles Demonstrated
- **Code Exploration**: Model reads and understands existing architecture before extending
- **Planning Capability**: Model creates a mental model of the system before making changes
- **Consistency Awareness**: Model ensures new code follows existing patterns and conventions
- **Multi-File Coordination**: Model manages changes that span multiple files
- **API Design**: Model understands how to extend an API in backward-compatible ways

## The Task

"Add new statistical functions to the data processor:
1. Add a `median()` function to the calculator module
2. Add a `standard_deviation()` function
3. Update `process_numbers()` in data_processor to include these new statistics
4. Update `main.py` to demonstrate these new functions"

## How the Harness Works Here

1. **Model reads** all relevant files:
   - `calculator.py` to understand the structure
   - `data_processor.py` to see how it uses calculator functions
   - `main.py` to see the usage pattern
2. **Model plans** the implementation:
   - Determine what algorithm to use for median
   - Understand how to calculate standard deviation
   - Design where the code should live (in calculator vs data_processor)
3. **Model implements** in order:
   - Add `median()` to calculator.py
   - Add `standard_deviation()` to calculator.py
   - Update `process_numbers()` in data_processor.py
   - Update `main.py` to test the new functions
4. **Model verifies** by examining the updated files

## Expected Output

The model should:
- Implement median using the sorted approach or quickselect
- Implement standard deviation using the mathematical formula
- Maintain code style consistency with existing functions
- Add docstrings following the existing pattern
- Update main.py with example usage

## Course Learning Objectives

- See how models **understand system architecture** before extending it
- Understand that harnesses support **planned, multi-step implementations**
- Recognize that models can **reason about appropriate placement** of new code
- Learn how harnesses enable **cohesive feature development**

## Challenge Extension

Ask the model to:
- "Add quartile calculations (Q1, Q2, Q3)"
- "Create visualizations of the statistics (if matplotlib available)"
- "Add a command-line interface to the main.py script"
- "Create comprehensive documentation for all new functions"
- "Implement these using NumPy for better performance"
