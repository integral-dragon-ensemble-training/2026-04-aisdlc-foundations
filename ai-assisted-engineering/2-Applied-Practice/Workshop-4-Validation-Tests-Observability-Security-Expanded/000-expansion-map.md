# 000 Expansion Map

Workshop 4 consumes candidate changes from Workshop 3 and turns them into validation decisions.

## Expanded Flow

```text
candidate branch
  -> validation matrix
  -> testing confidence review
  -> observability review
  -> security review
  -> approve / revise / reject
  -> rescore and group decision
```

## Core Idea

Validation is not one thing. A change may need tests, logs, traces, dependency checks, secret checks, deployment visibility, or human review.

## Outputs

- validation matrix
- testing confidence findings
- observability gap findings
- security and supply-chain review
- AI change review checklist
- approve/revise/reject recommendation

## Guardrails

- Do not confuse test count with confidence.
- Do not accept "looks fine" as validation.
- Do not let security become optional polish.
- Do not merge without evidence.
- Separate what passed from what remains unproven.

