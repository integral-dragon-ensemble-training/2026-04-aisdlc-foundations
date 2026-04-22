# 040 Flow Impact Prioritization

## Objective

Prioritize debt by impact on delivery flow, not by annoyance.

## Claude Prompt

```text
Prioritize the classified debt items.

Score each item on:
- interest: repeated cost
- frequency: how often the cost is paid
- blast radius: how many people or changes are affected
- fix size: small, medium, large
- risk: low, medium, high
- AI suitability: good candidate, needs human design, not suitable

Recommend the top five items for group discussion and the top one small candidate improvement for an individual branch.

Do not apply changes yet.
```

## Output

- prioritized debt list
- top five group review items
- one small candidate improvement

