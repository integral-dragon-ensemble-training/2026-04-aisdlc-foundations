# 000 Expansion Map

Workshop 3 consumes the Workshop 2 friction map and teaches participants how to aim Claude Code carefully.

## Expanded Flow

```text
friction priority
  -> inspection question
  -> evidence-gathering prompt
  -> codebase understanding pass
  -> improvement options
  -> small candidate change
  -> review and validation
```

## Core Idea

AI should not be asked to "improve the repo." It should be asked to answer a bounded engineering question, cite evidence, and propose small options.

## Outputs

- AI inspection plan
- evidence-backed findings
- tightened prompts
- change plan
- branch summary
- review packet

## Guardrails

- Do not accept fluent answers without evidence.
- Do not let Claude expand scope without permission.
- Do not combine unrelated fixes.
- Prefer small diffs and narrow validation.
- Preserve human review as the decision point.

