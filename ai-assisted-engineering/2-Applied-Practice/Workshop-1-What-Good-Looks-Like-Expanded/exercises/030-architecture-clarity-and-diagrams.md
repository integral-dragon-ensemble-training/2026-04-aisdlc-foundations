# 030 Architecture Clarity And Diagrams

## Objective

Use Claude Code and the available architecture or diagramming skill to make the current architecture visible enough to discuss.

## Key Teaching Point

The diagram is not the goal. Shared understanding is the goal.

## Participant Instructions

1. Ask Claude Code to identify major components, entry points, dependencies, and boundaries.
2. Ask it to name uncertainty explicitly.
3. Use the architecture/diagramming skill if available.
4. Generate a current-state architecture note and diagram.
5. Compare the diagram to the scorecard architecture score.
6. Identify one improvement that would make architecture easier to understand.

## Suggested Claude Code Prompt

```text
Use the architecture analysis or diagramming skill if one is available.

Analyze the current repository for architecture clarity.

Rules:
- Do not edit application code.
- Identify major components, entry points, boundaries, dependency directions, and integration points.
- Separate evidence from inference.
- Name anything you cannot determine from the repo.
- Produce a current-state architecture summary.
- Propose one lightweight diagram that would help a new engineer.
- If you create a diagram, store it under docs/architecture/current-state.*

Before writing files, show me the proposed architecture summary and diagram plan.
```

## Expected Output

- Current-state architecture summary.
- Diagram plan or generated diagram.
- List of architecture uncertainties.
- One candidate improvement, such as a boundary note, module ownership table, or README architecture section.

## Scoring Connection

Use the result to revisit the `Architecture clarity and boundaries` score.

A score should improve only if the repo now contains a maintained artifact that makes the architecture easier to understand.

