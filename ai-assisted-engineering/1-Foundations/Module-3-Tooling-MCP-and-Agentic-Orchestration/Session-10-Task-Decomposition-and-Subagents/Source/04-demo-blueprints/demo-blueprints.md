# Demo Blueprints

## Session 10

## Task Decomposition and Subagents

### Demo 01

## One giant prompt versus three bounded tasks

### Goal

Show that the main problem is not lack of model capability. It is lack of task structure.

### Suggested flow

1. Present a large request as one monolithic prompt.
2. Ask Claude to critique why the request is poorly decomposed.
3. Rewrite it into 3 bounded delegated tasks.
4. Compare the result quality and reviewability.

### Teaching points

- decomposition improves determinism
- smaller scopes create clearer outputs
- the human must design the work boundary

### Demo 02

## Focused reviewer subagent

### Goal

Show how a subagent can isolate a narrow analysis task and return only what matters.

### Suggested flow

1. Define a read-only code-review subagent or use an existing reviewer subagent.
2. Ask it to inspect one file or one module only.
3. Require a concise summary:
   - issues found
   - risk level
   - suggested next action

### Teaching points

- role focus matters
- output compression preserves main context
- narrow tasks are easier to trust

### Demo 03

## Tool restriction as part of task design

### Goal

Show that decomposition is not only about splitting work. It is also about controlling capability.

### Suggested flow

1. Define two versions of the same subagent:
   - read-only reviewer
   - full-access implementer
2. Ask which one should handle each subtask in the workflow.
3. Discuss why the default should usually be the narrower one first.

### Teaching points

- capability should follow task scope
- review and implementation are not the same role
- Session 10 prepares students for parallel orchestration in Session 11
