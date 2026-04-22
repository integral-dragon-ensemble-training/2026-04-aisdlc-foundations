# 050 Validation Gate For AI Diff

## Objective

Apply a final validation gate to the AI-assisted branch.

## Claude Prompt

```text
Apply the AI change validation gate to this branch.

Classify the branch as:
- approve
- revise
- reject

Base the decision on:
- test evidence
- observability evidence
- security evidence
- scope control
- reviewability
- what remains unproven

Do not merge. Write the validation gate decision to my coursework folder.
```

## Output

- validation gate decision
- evidence summary
- unresolved risks

