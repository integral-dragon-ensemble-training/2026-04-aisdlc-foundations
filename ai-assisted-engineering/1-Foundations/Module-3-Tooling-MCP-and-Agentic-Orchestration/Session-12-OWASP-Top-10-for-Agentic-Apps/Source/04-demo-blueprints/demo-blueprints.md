# Demo Blueprints

## Session 12

## OWASP Top 10 for Agentic Apps

### Demo 01

## Tabletop threat model

### Goal

Show how to reason about an agentic incident without relying on a live code demo.

### Suggested flow

1. Present a short incident trace.
2. Ask Claude to identify the attack path and control failure.
3. Map the trace to an agentic risk class.
4. Review what should have blocked the chain earlier.

### Teaching points

- the problem is action safety, not only output quality
- the earliest failing control matters most
- modeling the attack chain is the skill, not memorizing a label

### Demo 02

## Layer-by-layer defense map

### Goal

Show where each kind of control belongs.

### Suggested flow

1. Present four scenarios: malicious ticket, read-only data source, context poisoning, and tool abuse.
2. Ask Claude to assign the control layer for each.
3. Challenge any answer that places all safety at the prompt layer.

### Teaching points

- prompt hygiene is only one layer
- permissions, sandboxing, and server controls matter
- identity and auditability are core security requirements

### Demo 03

## Zero-demo, high-discussion session

### Goal

Emphasize that threat modeling can be the entire teaching artifact when the goal is architectural clarity.

### Suggested flow

1. Walk the cohort through a realistic attack chain.
2. Pause at each step to ask what failed.
3. End by naming the earliest control that should have stopped the breach.

### Teaching points

- some sessions should be tabletop only
- security thinking should be explicit and shared
- the next module turns this into practical policy and governance
