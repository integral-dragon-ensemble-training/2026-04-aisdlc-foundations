# 050 Testing Confidence And Lockdown Tests

## Objective

Use Claude Code to evaluate whether existing tests provide meaningful confidence and to suggest characterization or lockdown tests for risky behavior.

## Key Teaching Point

Coverage is not confidence. A repo can have many tests and still be hard to change safely.

## Participant Instructions

1. Ask Claude Code to inventory tests and CI signals.
2. Ask it to map tests to user-visible or business-relevant behaviors.
3. Ask it to identify brittle, shallow, or missing test areas.
4. Ask it to propose lockdown tests for high-risk current behavior.
5. Choose one small test to add or improve.

## Definition: Lockdown Test

A lockdown test is a characterization or regression test that captures current known behavior before refactoring.

It is useful when:

- the code is brownfield
- behavior is important but poorly documented
- refactoring is risky
- the team needs a safety net before changing internals

## Suggested Claude Code Prompt

```text
Inspect this repository for testing confidence.

Rules:
- Do not edit files yet.
- Inventory the test frameworks, test locations, CI test commands, and visible coverage or quality signals.
- Distinguish coverage from confidence.
- Identify which important behaviors appear protected and which do not.
- Suggest candidate lockdown tests for risky current behavior.
- For each proposed test, explain what behavior it protects and why it matters.

Show the findings and recommend one small test improvement before writing code.
```

## Optional Apply Prompt

Use only after reviewing the proposal:

```text
Apply the smallest recommended lockdown test.

Constraints:
- Keep the change minimal.
- Do not refactor production code unless the test cannot be written without a tiny seam.
- If a seam is needed, explain it first.
- Run the narrowest relevant test command.
- Report what passed, failed, and remains unproven.
```

## Expected Output

- Test inventory.
- Confidence gap list.
- Candidate lockdown tests.
- One small applied test improvement if approved.
- Test command result.

## Scoring Connection

Use the result to revisit `Testability and quality confidence`.

A score should improve only if the repo gained a meaningful confidence signal, not just a new test file.

