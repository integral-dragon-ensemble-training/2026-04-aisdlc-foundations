# 020 Codebase Understanding Run

## Objective

Use Claude Code to inspect the target area and produce evidence-backed understanding.

## Claude Prompt

```text
Run the approved inspection plan.

Rules:
- inspect only the agreed scope unless you ask first
- cite concrete paths and symbols
- separate evidence from inference
- identify tests, docs, and workflows related to this area
- name uncertainty
- do not edit files

Write a proposed codebase understanding summary before saving it.
```

## Output

- codebase understanding summary
- evidence list
- uncertainty list

