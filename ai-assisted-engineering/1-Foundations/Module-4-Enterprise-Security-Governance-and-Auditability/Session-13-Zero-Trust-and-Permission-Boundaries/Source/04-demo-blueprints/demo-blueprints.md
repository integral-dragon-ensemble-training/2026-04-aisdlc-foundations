# Demo Blueprints

## Session 13

## Zero Trust and Permission Boundaries

### Demo 01

## Blocked execution

### Goal

Show that the control boundary should stop disallowed actions before they reach the system.

### Suggested flow

1. Run a task that requests a write or shell action outside policy.
2. Show the system denying the action.
3. Explain why the denial is the correct outcome.
4. Re-run with a narrower, approved scope.

### Teaching points

- deny-by-default is the baseline
- approval and permission are not the same
- unsafe convenience should not be normalized

### Demo 02

## Read-only versus write-capable roles

### Goal

Show how the same agentic workflow should split into separate privilege levels.

### Suggested flow

1. Present a read-only review role.
2. Present a write-capable change role.
3. Compare their tool access and approval requirements.
4. Ask which role should be the default starting point.

### Teaching points

- most work can start read-only
- write access should be justified
- RBAC should cover AI identities just like human ones

### Demo 03

## Anti-pattern review

### Goal

Show why `--dangerously-skip-permissions` is the wrong answer to friction.

### Suggested flow

1. Present a scenario where someone wants to skip approval for speed.
2. Ask Claude to explain the risk tradeoff.
3. Reframe the task with a narrower permission set instead.

### Teaching points

- speed without controls is not a valid optimization
- the right fix is smaller scope, not bypass
- Session 13 is about control correctness, not process theater
