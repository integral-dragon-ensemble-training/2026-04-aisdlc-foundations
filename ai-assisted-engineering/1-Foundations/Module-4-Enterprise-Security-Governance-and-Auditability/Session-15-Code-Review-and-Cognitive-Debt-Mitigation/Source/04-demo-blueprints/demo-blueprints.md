# Demo Blueprints

## Session 15

## Code Review and Cognitive Debt Mitigation

### Demo 01

## Review the AI diff, not the AI story

### Goal

Show that the same diff can look safe until the reviewer examines behavior and structure.

### Suggested flow

1. Present a short AI-generated PR or synthetic diff.
2. Ask Claude to summarize what changed.
3. Switch to a human review lens and ask what the change actually does.
4. Identify one load-bearing logic flaw or boundary problem.

### Teaching points

- polished text is not proof
- structure matters more than explanation quality
- the reviewer must validate the mental model

### Demo 02

## Tests passed, review still failed

### Goal

Show that passing tests are useful but incomplete evidence.

### Suggested flow

1. Present a change with passing tests.
2. Ask which assumptions the test suite did not prove.
3. Ask which business behavior or boundary still needs verification.
4. Write a review comment that explains the missing structural check.

### Teaching points

- tests are one signal, not the signal
- review should cover invariants and architecture
- “green” does not mean “understood”

### Demo 03

## Code reviewer subagent as a first pass, human as final owner

### Goal

Show how the built-in code-reviewer pattern can help without replacing human judgment.

### Suggested flow

1. Invoke a review-oriented subagent or code reviewer workflow.
2. Ask it to identify issues in a recent diff.
3. Compare its findings to a human architectural review.
4. Note what the subagent saw and what the human still had to decide.

### Teaching points

- subagents can accelerate review
- the human still owns understanding and approval
- the final call is about risk, not just issue count
