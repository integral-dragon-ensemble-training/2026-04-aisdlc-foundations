# Session Brief

## Session 05

## Spec-Driven Development

### Purpose

Teach students to replace vague prompting with explicit, reviewable specifications that constrain what the agent is allowed to build and how the result will be judged.

### Why this session matters

The Ensemble cohort is already using AI frequently. Their actual bottleneck is not basic access. It is reviewability, trust, governance, and getting consistent outputs on real work. Spec-Driven Development is the discipline that turns "please build this" into "here is what must be true when we are done."

### Learning outcomes

By the end of this session, students should be able to:

- explain why many AI failures are really specification failures
- distinguish a vague request from an executable engineering specification
- write acceptance criteria that are binary, observable, and reviewable
- separate required outcomes from premature implementation guesses
- turn a ticket or idea into a bounded spec that is ready for planning

### Core ideas

#### 1. The spec carries intent

The model can generate syntax, scaffolding, and candidate implementations. It cannot infer unstated business rules, non-goals, operational constraints, or compliance boundaries reliably enough for enterprise work.

#### 2. A good spec reduces variance

Structured requirements narrow the solution space. That lowers rework, reduces prompt thrash, and makes downstream planning more stable.

#### 3. Acceptance criteria are the control surface

If the team cannot tell whether the output passed or failed, the spec is not ready. "Feels right" is not a criterion. "Returns 401 for expired token and does not mutate existing sessions" is.

#### 4. Specs are not giant documents

Students do not need heavyweight template theater. They need a compact, versionable structure that covers goal, constraints, interfaces, edge cases, acceptance checks, and non-goals.

#### 5. Specs should be grounded in the actual repo

Good specs are informed by the current system. Read the codebase, map the boundary, then write the spec. Otherwise the team produces elegant nonsense.

### Engineering implications

- tickets should be upgraded before code generation starts
- ambiguity should be surfaced as questions, not silently guessed away
- acceptance criteria drive test plans and review comments
- decomposition quality improves when the spec is explicit
- small PRs become easier when the scope is decided before implementation

### 23-minute flow

- `00:00-04:00`: Why specification discipline matters now
- `04:00-09:00`: Weak prompt vs executable spec
- `09:00-14:00`: Minimum viable spec structure
- `14:00-18:00`: Acceptance criteria and non-goals
- `18:00-21:00`: Live Claude Code critique and rewrite
- `21:00-23:00`: Debrief and bridge to Session 06

### Key takeaway

The agent is not the source of truth. The spec is. If the team wants reliable AI-assisted delivery, intent must be made explicit before planning and execution begin.
