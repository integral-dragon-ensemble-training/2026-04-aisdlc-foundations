# Demo Blueprints

## Session 07

## Context Control via CLAUDE.md

### Demo 01

## Repeated prompt vs persistent rule

### Goal

Show that recurring instructions are better encoded once in the project than retyped for every task.

### Suggested flow

1. Start in a repo with no project rule for output narration.
2. Ask Claude to make a small change and summarize what it did.
3. Add a `CLAUDE.md` rule that requires file-level narration and explicit test reporting.
4. Repeat a similar task and compare the response shape.

### Teaching points

- repeated prompting is a weak control mechanism
- project rules make behavior more stable
- durable rules reduce operator effort

### Demo 02

## Scope separation

### Goal

Show students that not every instruction belongs in the same layer.

### Suggested flow

1. Present four example rules.
2. Ask Claude to classify them as user, project, local, or task-specific.
3. Challenge one classification and explain why a different scope would create risk.

### Teaching points

- shared rules should be versioned with the project
- local experiments should stay local
- scope mistakes create hidden inconsistency

### Demo 03

## Tighten a noisy `CLAUDE.md`

### Goal

Show how to reduce a bloated rule file into a smaller, higher-signal set of controls.

### Suggested flow

1. Start with an intentionally overloaded `CLAUDE.md`.
2. Ask Claude:
   `Reduce this file to the smallest set of durable, enforceable project rules.`
3. Review what was removed and why.

### Teaching points

- brevity improves durability
- vague rules create little leverage
- a good rule file should survive repeated use
