# Demo Blueprints

## Session 16

## Auditability and Workflow Narration

### Demo 01

## Export the session evidence

### Goal

Show that the AI-assisted workflow can be preserved as an artifact, not just remembered.

### Suggested flow

1. Open a completed Claude Code session.
2. Export or capture the relevant log or transcript.
3. Point out the useful evidence: prompts, tool use, decisions, and checkpoints.
4. Show where that record would live for later review.

### Teaching points

- the record should outlive the session
- retrieval matters as much as capture
- the evidence should be interpretable by a third party

### Demo 02

## Write a PR narration

### Goal

Show how to turn a code change into a defensible human narrative.

### Suggested flow

1. Present a change that could be summarized too vaguely.
2. Ask Claude to draft a PR narration with rationale, alternatives, and evidence.
3. Tighten the narration until it is useful to an auditor or reviewer.

### Teaching points

- narration is not a changelog
- the explanation should justify the path taken
- uncertainty and rejected options should be visible

### Demo 03

## Attach trace evidence to the PR

### Goal

Show that the narrative becomes stronger when supported by retrievable evidence.

### Suggested flow

1. Add session-log or trace references to the PR description.
2. Explain what a reviewer can reconstruct from those references.
3. Discuss what would still be missing for full audit readiness.

### Teaching points

- evidence beats memory
- the best records are recoverable and specific
- the final workflow should be reviewable by someone not in the room
