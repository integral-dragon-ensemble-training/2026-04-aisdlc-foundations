# Coding Harness Demo Scenarios

This folder contains four demonstration scenarios designed to teach the core principles of how **coding harnesses work** and how **AI models have been modified to interact with code**.

## What is a Coding Harness?

A coding harness is a system that:
1. Allows an AI model to **read** source code files
2. Allows an AI model to **modify** source code files
3. Provides **structured feedback** to the model about the results
4. Enables **iterative problem-solving** through multiple tool invocations

This architecture fundamentally changes what AI models can do—they go from being passive text generators to **active agents** that can directly interact with and modify software systems.

## The Four Scenarios

### 📋 [Scenario 1: Bug Fixing](./scenario-1-bug-fixing.md)
**Focus**: Error detection and simple fixes

Demonstrates how models can:
- Identify bugs by reading source code
- Understand error conditions
- Implement fixes using the edit tool
- Validate their own changes

**Key Principle**: Models can **reason about correctness** and apply domain knowledge to fix problems.

---

### 🔧 [Scenario 2: Code Refactoring](./scenario-2-refactoring.md)
**Focus**: Architecture improvement and best practices

Demonstrates how models can:
- Recognize anti-patterns and design flaws
- Understand software engineering principles (DRY, SRP)
- Redesign code structure for maintainability
- Coordinate multi-file changes

**Key Principle**: Models understand **code quality** and can improve architecture, not just fix bugs.

---

### ✨ [Scenario 3: Feature Addition](./scenario-3-feature-addition.md)
**Focus**: Planning and coordinated implementation

Demonstrates how models can:
- Explore existing code to understand architecture
- Plan new features before implementing
- Extend APIs in backward-compatible ways
- Coordinate changes across multiple files
- Maintain consistency with existing code

**Key Principle**: Models can **plan and execute** non-trivial features, not just make isolated changes.

---

### 📚 [Scenario 4: Code Analysis & Documentation](./scenario-4-code-analysis.md)
**Focus**: Understanding, analysis, and artifact generation

Demonstrates how models can:
- Explore and navigate codebases
- Comprehend complex systems
- Generate documentation
- Identify improvements and issues
- Create learning materials

**Key Principle**: Harnesses aren't just for modification—they enable **analysis, documentation, and teaching**.

---

## How to Use These Scenarios in Your Course

### For Instructors

Each scenario file contains:
- **Overview**: What the scenario demonstrates
- **Principles Demonstrated**: Core concepts
- **The Task**: A concrete challenge to give to the harness
- **How the Harness Works Here**: Step-by-step walkthrough
- **Expected Output**: What a good response should include
- **Course Learning Objectives**: Educational goals
- **Challenge Extensions**: More advanced tasks

### Live Demo Approach

1. **Start Simple**: Begin with Scenario 1 (Bug Fixing)
   - Shows the basic mechanic: read → understand → fix
   - Demonstrates the tool invocation pattern
   - Clear success criteria

2. **Show Complexity**: Move to Scenario 2 (Refactoring)
   - Shows that harnesses can improve code, not just fix it
   - Demonstrates multi-step reasoning
   - Introduces software engineering principles

3. **Show Scale**: Progress to Scenario 3 (Feature Addition)
   - Shows that models can plan before implementing
   - Demonstrates coordinated multi-file changes
   - Shows understanding of architecture

4. **Show Depth**: Finish with Scenario 4 (Code Analysis)
   - Shows broader capabilities beyond modification
   - Demonstrates reading and analysis without writing
   - Shows real-world productivity applications

### Sample Instructions for Students

For each scenario, you can tell students:

**Scenario 1**: "Ask the harness to fix the bugs in the calculator. See if it can identify both issues and implement appropriate fixes."

**Scenario 2**: "Ask the harness to refactor the data_processor module. Notice how it breaks functions into smaller pieces and uses more Pythonic patterns."

**Scenario 3**: "Ask the harness to add statistical functions. Watch how it explores the existing code before implementing."

**Scenario 4**: "Ask the harness to analyze the codebase and create documentation. See what insights it generates."

---

## Key Teaching Points

### How Models Work With Code

1. **Context Window**: Models receive the entire file content in a single message
2. **Tool Format**: Models learn to output `tool: TOOL_NAME({...})` for invocations
3. **Feedback Loop**: Tool results are fed back as new messages for continued reasoning
4. **Multi-Step Reasoning**: Complex tasks require multiple tool calls in sequence

### Differences from Traditional Programming

| Traditional | Harness-Based |
|---|---|
| Programmer writes all code | Model generates, fixes, improves code |
| Isolated changes | Coordinated changes across files |
| Implementation → Testing | Implementation + automatic testing/validation |
| One solution | Multiple options/approaches explored |

### Limitations to Discuss

- Models can still make mistakes (always verify)
- No automatic testing (though scenarios can add this)
- Models work within tool constraints
- Effective prompting is crucial for good results

---

## For Different Model Architectures

### Claude-Specific Considerations

These scenarios work well with Claude because:
- Strong code understanding (trained on lots of high-quality code)
- Good planning and reasoning (can think through problems)
- Tool use is natural (learned to output tool invocations)
- Explains reasoning (can describe what it's doing and why)

### Adapting for Other Models

If using GPT, Gemini, etc.:
- Adjust model names in the harness
- Tool format may differ slightly
- May need more explicit prompting
- Reasoning patterns will differ

---

## Extensions for Advanced Students

### Advanced Challenges

- **Create a test suite**: "Generate comprehensive unit tests"
- **Performance optimization**: "Profile and optimize the slowest function"
- **Security analysis**: "Audit the code for security issues"
- **Add type hints**: "Add Python type hints throughout"
- **Create a CLI**: "Build a command-line interface"

### Research Directions

- How does model choice affect code quality?
- What prompting strategies work best?
- How to measure "good" refactoring?
- Can harnesses work for complex systems?
- How to ensure generated code is correct?

---

## File Structure

```
demo-scenarios/
├── README.md (this file)
├── scenario-1-bug-fixing.md
├── scenario-2-refactoring.md
├── scenario-3-feature-addition.md
└── scenario-4-code-analysis.md

demo-source/
├── calculator.py (intentionally has bugs)
├── data_processor.py (intentionally needs refactoring)
└── main.py (ties everything together)
```

The source code is **intentionally imperfect** to make for good teaching demonstrations.

---

## Getting Started

1. **Run the harness**: `./run.sh` from the parent directory
2. **Start with Scenario 1**: Follow the "Task" section
3. **Copy and paste** the task description into the harness
4. **Observe** how the model interacts with the code
5. **Try variations** using the "Challenge Extensions"

Happy teaching! 🚀
