# Demo Blueprints

## Session 09

## Skills and Deterministic Hooks

### Demo 01

## The same rule as advice versus enforcement

### Goal

Show the difference between asking Claude to remember a rule and configuring the tool to enforce it.

### Suggested flow

1. Ask Claude to avoid a protected file or to remember a validation step.
2. Show that this still depends on model behavior.
3. Add a hook that blocks the risky action automatically.
4. Re-run the workflow and inspect the difference.

### Teaching points

- advice is not enforcement
- deterministic control reduces trust burden
- quality policy should be mechanized where possible

### Demo 02

## Skill or hook classification

### Goal

Show students how to decide which category of control they are really asking for.

### Suggested flow

1. Present five recurring workflow requirements.
2. Ask Claude:
   `Classify each as skill, hook, or both, and explain why.`
3. Challenge one answer where the boundary is blurry.

### Teaching points

- reusable guidance and deterministic control are complementary
- classification improves architecture decisions
- the wrong mechanism creates fragility

### Demo 03

## Hook a deterministic quality gate into the workflow

### Goal

Show a concrete project-level hook that provides immediate engineering value.

### Suggested flow

1. Add a hook for one of:
   - formatting after edits
   - blocking destructive shell commands
   - scanning for secret-like strings before commit
2. Trigger the relevant lifecycle event.
3. Inspect the resulting behavior and discuss where it belongs relative to CI.

### Teaching points

- project-scope hooks can become shared team guardrails
- earlier failure is cheaper failure
- Session 09 is about moving controls into the workflow itself
