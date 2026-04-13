# Demo Blueprints

## Session 06

## Plan Mode vs. Act Mode

### Demo 01

## Start in Plan Mode on purpose

### Goal

Show students that planning is not passive; it is an active read-only investigation step.

### Suggested flow

```bash
claude --permission-mode plan
```

Prompt:

`Analyze the authentication flow, identify the likely files involved, and propose a low-risk change plan.`

### Teaching points

- the agent can still do meaningful work without editing
- planning is useful for unfamiliar codebases
- the first artifact is a plan, not a diff

### Demo 02

## Challenge the first plan

### Goal

Show that plan review should change the plan.

### Suggested flow

Ask follow-ups such as:

- `Assume database schema changes are not allowed. Revise the plan.`
- `Keep the first PR under 150 lines changed. Revise the plan.`
- `What tests are required before this is safe?`

### Teaching points

- approval is not automatic
- constraints should tighten the plan
- review starts before execution

### Demo 03

## From approved plan to bounded execution

### Goal

Show the handoff from planning to safe action without encouraging uncontrolled autonomy.

### Suggested flow

1. Accept the refined plan.
2. Instruct Claude to execute only the first bounded slice.
3. Require a short narration of:
   - files changed
   - risk introduced
   - tests run or still needed

### Teaching points

- do not approve the whole future, approve the next slice
- execution should stay small and reviewable
- narration closes the loop
