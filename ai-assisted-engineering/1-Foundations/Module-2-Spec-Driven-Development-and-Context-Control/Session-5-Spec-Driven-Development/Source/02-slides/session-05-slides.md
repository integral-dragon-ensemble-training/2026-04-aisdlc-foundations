# Session 05
## Spec-Driven Development
### The spec is the source of truth, not the prompt

---

# Most AI misses are specification misses

- The model usually fails where intent is missing, not where syntax is hard.
- Review pain starts upstream: vague tickets create vague plans, vague diffs, and vague tests.
- This cohort already uses AI often; the next maturity jump is better requirement shaping.

---

# Vibe coding optimizes for motion; SDD optimizes for convergence

- Vibe coding: prompt, inspect, retry, patch, hope.
- Spec-Driven Development: define target behavior, constraints, and checks before code exists.
- The win is not formality for its own sake. The win is fewer loops and more predictable output.

---

# A useful engineering spec is compact and executable

- Goal: what outcome must exist when the work is done.
- Constraints: what the agent must not violate.
- Interfaces: APIs, files, schemas, commands, or contracts touched.
- Acceptance criteria: binary checks that let a reviewer say pass or fail.
- Non-goals: what is explicitly out of scope.

---

# Good acceptance criteria are observable

- Weak: "make auth more robust"
- Better: "expired bearer token returns 401 with the existing error envelope"
- Better: "no database schema changes"
- Better: "existing integration tests continue to pass"

---

# Write what must be true before guessing how it should be built

- Lead with behavior, boundaries, and risk.
- Add implementation constraints only when they are real requirements.
- Example: "must use existing audit logger" is a valid constraint.
- Example: "should probably use a service class" is design advice, not acceptance criteria.

---

# Minimum viable spec template

- Problem statement
- Current boundary or affected area
- Inputs and outputs
- Constraints and invariants
- Edge cases and failure modes
- Acceptance checks
- Non-goals

---

# Repo reconnaissance comes before finalizing the spec

- Read the current code before freezing the request.
- Ask Claude Code to map the auth flow, touched files, and existing conventions.
- Then write the spec against the system that exists, not the system you imagine.

---

# Specs make decomposition cleaner

- A clear spec can usually be sliced into reviewable work packets.
- Typical slices:
- boundary mapping and risk notes
- implementation change
- tests and narration

---

# A short SDD loop beats a giant requirements ceremony

- Ticket or idea
- Read the boundary
- Draft the spec
- Critique the spec
- Freeze the acceptance checks
- Hand the spec to planning

---

# Live demo: turn a weak ticket into an executable spec

```bash
claude
```

Prompt flow:

1. "Critique this ticket for ambiguity and hidden assumptions."
2. "Rewrite it as a compact markdown spec with binary acceptance criteria."
3. "List open questions that still block safe planning."

---

# What to listen for in the demo

- Did Claude surface missing business rules or quietly invent them?
- Are the acceptance checks observable by a reviewer?
- Did the rewrite reduce ambiguity without becoming a giant PRD?
- Could this spec now feed Plan Mode safely?

---

# Common failure modes

- Treating a user story as if it were already a spec
- Writing criteria that sound good but cannot be tested
- Smuggling implementation guesses into the acceptance section
- Forgetting non-goals and letting the agent widen scope

---

# Key takeaway

- A prompt can start work.
- A spec can govern work.
- In enterprise delivery, governing work is the job.

---

# Bridge to Session 06

- A good spec is necessary.
- It is not sufficient.
- Next: how Plan Mode turns a spec into a reviewable execution proposal before the repo is touched.
