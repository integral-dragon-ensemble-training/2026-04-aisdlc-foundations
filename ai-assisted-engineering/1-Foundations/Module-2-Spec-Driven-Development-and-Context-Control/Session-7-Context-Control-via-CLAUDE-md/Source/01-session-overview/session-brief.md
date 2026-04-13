# Session Brief

## Session 07

## Context Control via CLAUDE.md

### Purpose

Teach students how to encode persistent project rules in `CLAUDE.md` so the agent follows stable architectural, formatting, safety, and workflow expectations without requiring repetitive prompting.

### Why this session matters

Specs and plans help on a single task. Enterprise teams still need a durable way to carry standards across every task. `CLAUDE.md` is where recurring constraints become part of the working environment instead of tribal knowledge.

### Learning outcomes

By the end of this session, students should be able to:

- explain what kinds of instructions belong in `CLAUDE.md`
- distinguish user, project, local, and managed configuration scopes
- write compact project rules that are stable, testable, and worth versioning
- avoid overloading `CLAUDE.md` with task-specific noise
- use persistent rules to reduce variance across teammates and sessions

### Core ideas

#### 1. Persistent rules beat repeated prompts

If the same instruction is repeated every session, it probably belongs in the harness. Stable constraints should live in a durable file, not in a human memory loop.

#### 2. `CLAUDE.md` is for policy and conventions, not everything

Good `CLAUDE.md` content includes coding conventions, review expectations, path rules, architecture boundaries, testing expectations, and other durable instructions. Temporary task goals still belong in the task itself.

#### 3. Scope is part of the control model

Some rules belong to the user globally. Some belong to the project. Some are local experiments. Some must be managed centrally and never overridden. Students need to understand which layer solves which problem.

#### 4. Brevity matters

A bloated `CLAUDE.md` becomes background fog. High-value rules are concise, enforceable, and worth carrying forward across many tasks.

#### 5. Persistent context reduces drift

When project rules are versioned and shared, outputs become more consistent across engineers, sessions, and agents. That lowers review friction and makes AI-assisted work feel less random.

### Engineering implications

- recurring instructions should move from chat history into versioned project rules
- review expectations can be encoded before work begins
- project-level rules improve cross-team consistency
- local overrides should not silently replace shared standards
- `CLAUDE.md` works best when paired with specs, plans, hooks, and permissions

### 23-minute flow

- `00:00-04:00`: Why persistent context matters
- `04:00-09:00`: What belongs in `CLAUDE.md`
- `09:00-14:00`: Scope hierarchy and override behavior
- `14:00-18:00`: Live rule-authoring and behavior shift demo
- `18:00-21:00`: Common failure modes
- `21:00-23:00`: Debrief and bridge to Session 08

### Key takeaway

If a rule is stable enough to matter on every task, it should live in the environment. `CLAUDE.md` turns repeated verbal reminders into durable project controls.
