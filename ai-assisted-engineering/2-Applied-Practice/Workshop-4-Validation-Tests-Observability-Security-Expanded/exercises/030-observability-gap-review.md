# 030 Observability Gap Review

## Objective

Check whether the change can be understood in operation.

## Claude Prompt

```text
Review the candidate branch for observability impact.

Inspect:
- logging around changed behavior
- error handling
- correlation or request context
- metrics or traces if relevant
- deployment verification signals
- runbooks or operational notes

Identify observability gaps and recommend one small improvement if needed.
Do not add noisy telemetry.
```

## Output

- observability findings
- operational uncertainty
- optional logging/runbook improvement

