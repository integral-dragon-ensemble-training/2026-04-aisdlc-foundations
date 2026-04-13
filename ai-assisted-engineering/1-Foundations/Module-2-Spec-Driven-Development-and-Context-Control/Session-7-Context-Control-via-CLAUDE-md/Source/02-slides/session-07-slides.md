# Session 07
## Context Control via CLAUDE.md
### Put stable rules in the harness, not in the prompt

---

# The same reminder repeated ten times is a missing system rule

- Teams often keep retyping the same instructions: use this style, avoid this path, run these tests.
- That is not discipline. That is a configuration gap.
- Persistent rules reduce variance without depending on memory.

---

# `CLAUDE.md` is shared working context

- It carries durable instructions the agent should apply repeatedly.
- It is part of the environment, not part of a one-off task description.
- Think of it as project memory with rules, not a giant prompt scrapbook.

---

# What belongs in `CLAUDE.md`

- coding and formatting conventions
- architecture boundaries and no-go zones
- testing and verification expectations
- review and narration requirements
- repo-specific workflow rules

---

# What does not belong there

- temporary task goals
- one-time business decisions
- long speculative background dumps
- instructions that change every hour
- duplicated documentation nobody will maintain

---

# Scope matters

- User scope: your default personal preferences across projects
- Project scope: rules shared with the team and checked in
- Local scope: per-machine or experimental overrides
- Managed scope: organization-enforced policy that cannot be bypassed casually

---

# The teaching model: durable rules at the right layer

- Put team conventions in project scope.
- Put personal experiments in local scope.
- Put enterprise policy in managed settings.
- Do not hide shared project rules in your private setup.

---

# A good `CLAUDE.md` rule is short and enforceable

- Weak: "write clean code"
- Better: "prefer existing service abstractions; do not introduce new top-level folders without approval"
- Better: "run targeted tests for changed modules and report what was or was not run"

---

# Bad `CLAUDE.md` files usually fail one of two ways

- too vague to change behavior
- too bloated to stay relevant

The goal is durable, high-signal constraints.

---

# Live demo: behavior changes when the rules move into the repo

1. Start without a project rule.
2. Ask Claude to format or structure a change.
3. Add a precise `CLAUDE.md` rule.
4. Re-run the same task and compare the output.

---

# Example rule categories for regulated teams

- no schema changes without explicit approval
- preserve existing audit logging
- keep diffs small and narrate file-level impact
- do not introduce new dependencies without justification

---

# `CLAUDE.md` complements specs and plans

- The spec defines this task.
- The plan defines this execution path.
- `CLAUDE.md` defines recurring project rules.
- Hooks and permissions enforce deterministic controls around them.

---

# Common failure modes

- stuffing every thought into `CLAUDE.md`
- encoding personal taste as team policy
- hiding project rules in local files
- forgetting to update the file when standards change

---

# Key takeaway

- Stable instructions should become environment rules.
- `CLAUDE.md` is how teams make good behavior durable.

---

# Bridge to Session 08

- Session 07 defined persistent internal rules.
- Session 08 extends the environment outward by connecting Claude to external tools and systems through MCP.
