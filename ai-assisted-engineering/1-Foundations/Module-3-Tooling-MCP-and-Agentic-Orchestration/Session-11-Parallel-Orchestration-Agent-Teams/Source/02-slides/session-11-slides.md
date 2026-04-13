# Session 11
## Parallel Orchestration: Agent Teams
### Parallel workers help only when the coordination model is sound

---

# Session 10 solved isolation; Session 11 solves coordination

- Subagents isolate focused delegated work.
- Agent teams coordinate multiple independent workers.
- The question is not "can we spawn more agents?"
- The question is "does this work benefit from peers working in parallel?"

---

# Agent teams are for genuinely parallel work

- cross-layer feature exploration
- competing debugging hypotheses
- multi-lens review
- research and design work with distinct ownership tracks

They are not the default answer for routine sequential tasks.

---

# Agent teams and subagents are different architectures

- Subagents:
  - hierarchical
  - report back to the caller
  - lower token cost
  - best when only the result matters
- Agent teams:
  - independent teammates
  - direct peer-to-peer messaging
  - shared task list
  - best when teammates need to collaborate

---

# Core team components

- lead session
- teammates
- shared task list
- mailbox and direct messaging

This is an orchestration system, not just a spawn command.

---

# The lead still owns the operation

- decide whether a team should exist
- define roles
- steer the work
- review plans if required
- shut down teammates
- clean up the team

More workers increase orchestration responsibility.

---

# Good team design starts with role clarity

- UI researcher
- API architect
- QA reviewer

Distinct roles reduce overlap and file conflicts.

---

# Shared task lists create leverage and risk

- pending
- in progress
- completed
- dependency-aware claiming

Good task structure prevents idle waiting and duplicated work.

---

# Teammates can talk directly

- useful for sharing findings
- useful for challenging assumptions
- risky if left unmonitored or underspecified

Direct communication is the biggest architectural shift from subagents.

---

# Parallelism has real costs

- more tokens
- more coordination overhead
- more permission surface
- more chance of collisions

If the task is sequential, one session is cheaper and safer.

---

# Live demo: create a 3-agent team

Example structure:

- one teammate on UX
- one teammate on technical design
- one teammate on QA or devil's-advocate review

The point is role separation, not raw agent count.

---

# Best-practice operating rules

- start with research and review
- keep teams small
- size tasks to be self-contained
- avoid same-file edits
- monitor and steer instead of walking away

---

# Common failure modes

- creating a team for sequential work
- vague teammate roles
- too many teammates
- letting the lead implement instead of coordinating
- forgetting shutdown and cleanup

---

# Key takeaway

- Agent teams are worth it when parallel exploration and peer coordination add real value.
- Otherwise, subagents or a single session are better tools.

---

# Bridge to Session 12

- Session 11 expands the execution surface.
- Session 12 examines the threat model that comes with that expansion.
