# 020 Testing Confidence And Lockdown Tests

## Objective

Evaluate whether the candidate branch has enough test confidence.

## Claude Prompt

```text
Review the candidate branch for testing confidence.

Inspect:
- tests changed or added
- tests that should cover the changed behavior
- CI test commands
- missing behavior coverage
- brittle or shallow tests
- candidate lockdown tests

Recommend the smallest useful test improvement.
Do not edit files until I approve.
```

## Output

- test confidence findings
- candidate lockdown tests
- optional small test improvement

