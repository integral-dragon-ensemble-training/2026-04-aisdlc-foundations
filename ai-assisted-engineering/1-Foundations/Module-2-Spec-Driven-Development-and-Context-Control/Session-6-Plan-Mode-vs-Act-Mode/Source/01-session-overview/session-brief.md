# Session Brief

## Session 06

## Plan Mode vs. Act Mode

### Purpose

Teach students to separate read-only analysis from write-enabled execution so the agent must first produce a reviewable plan, surface open questions, and expose risk before any changes are applied.

### Why this session matters

The survey says this cohort wants smaller diffs, better review quality, and safer use of AI in regulated environments. Plan Mode is the operational control that makes those outcomes realistic. It slows the first move down so the rest of the workflow speeds up safely.

### Learning outcomes

By the end of this session, students should be able to:

- explain what Plan Mode is for and when to use it
- start Claude Code in Plan Mode and use it for repo analysis
- critique a proposed plan before approving execution
- distinguish planning, approval, and execution as separate control points
- connect permission modes to enterprise review discipline

### Core ideas

#### 1. Read-only analysis is a safety feature

Plan Mode keeps the agent in analysis mode. It can inspect the repo, ask clarifying questions, and propose work without modifying files or executing commands.

#### 2. The plan is an engineering artifact

A plan should name likely touched files, hidden risks, migration concerns, test implications, and open questions. If it cannot do that, the task is not ready for execution.

#### 3. Approval is not a rubber stamp

The value is not simply having a plan. The value is challenging the plan before execution begins. Students should learn to reject shallow plans and force refinement.

#### 4. Permission modes are broader than a simple binary

Current Claude Code exposes multiple permission modes, but the teaching model still benefits from a clean separation: first analyze, then execute with explicit approval and scoped permissions.

#### 5. Small approved steps outperform one giant leap

Even after approval, execution should stay sliced. The best operational rhythm is spec, plan, challenge, approve, act in small diffs, test, narrate.

### Engineering implications

- multi-file changes should default to planning first
- the reviewer can begin before code exists
- permission settings and planning are complementary controls
- challenge-and-revise is part of the workflow, not a sign of failure
- execution quality improves when the plan names risk and invariants explicitly

### 23-minute flow

- `00:00-04:00`: Why mode separation matters
- `04:00-09:00`: What Plan Mode does and does not do
- `09:00-14:00`: What to review in a plan
- `14:00-18:00`: Live Claude Code planning workflow
- `18:00-21:00`: Permission modes and safe execution
- `21:00-23:00`: Debrief and bridge to Session 07

### Key takeaway

Do not let the first draft of the agent's thinking become the first write to the repo. Make the agent show its work, challenge it, then approve execution deliberately.
