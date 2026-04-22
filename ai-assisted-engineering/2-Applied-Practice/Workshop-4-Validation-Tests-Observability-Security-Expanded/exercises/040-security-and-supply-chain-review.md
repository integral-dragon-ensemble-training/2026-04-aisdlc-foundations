# 040 Security And Supply Chain Review

## Objective

Check whether the candidate branch introduces security, secret, dependency, or supply-chain risk.

## Claude Prompt

```text
Review the candidate branch for security and supply-chain risk.

Inspect:
- secrets or credentials
- dependency changes
- package or lockfile changes
- generated code that handles input, auth, data, or external calls
- unsafe defaults
- missing validation or error handling
- available scanning workflows

Do not run external scanners unless approved.
Summarize risks, evidence, and recommended next action.
```

## Output

- security review
- dependency/supply-chain notes
- approve/revise/reject signal

