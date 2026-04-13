# Session 06
## Plan Mode vs. Act Mode
### Make the agent show its work before it edits the repo

---

# Mode separation is an engineering control, not a UI preference

- Planning and execution create different kinds of risk.
- The same agent that can help quickly can also widen scope quickly.
- Separating analysis from action gives the human a real approval gate.

---

# What Plan Mode is for

- Read-only codebase analysis
- clarifying questions and missing-requirement discovery
- multi-file change proposals before execution
- safer exploration of unfamiliar or sensitive areas

---

# Anthropic's current docs are explicit here

- Plan Mode lets Claude analyze with read-only operations.
- Anthropic positions it for exploring codebases, planning complex changes, and safe review.
- You can start directly with:

```bash
claude --permission-mode plan
```

---

# Use Plan Mode when the task is high-risk or high-ambiguity

- multi-step implementation
- refactors that touch many files
- migrations, auth, billing, CI, or compliance-sensitive flows
- work where the repo boundary is still unclear

---

# What a good plan should contain

- likely files or components touched
- invariants that must remain true
- migration or compatibility concerns
- testing strategy
- open questions and unresolved assumptions

---

# Review the plan like an engineer, not a spectator

- What did the plan assume without evidence?
- What failure modes did it ignore?
- Which files should not be touched?
- What test evidence would prove this change is safe?

---

# Teaching nuance: Claude Code now has more than two permission modes

- `default`
- `acceptEdits`
- `plan`
- `auto`
- `dontAsk`
- `bypassPermissions`

But for this course, the key mental model is still simple:

- analyze first
- execute only after review

---

# Plan Mode and permissions solve different problems

- Plan Mode controls when action can begin.
- Permission rules control what actions are allowed.
- Hooks and managed settings add another policy layer.
- In enterprise practice, you want all of them.

---

# The safest execution rhythm is small and explicit

- spec
- plan
- challenge the plan
- approve
- execute a bounded slice
- test
- narrate

---

# Live demo: propose, critique, refine, approve

```bash
claude --permission-mode plan
```

Prompt flow:

1. "Analyze the auth module and propose the safest refactor path."
2. "List touched files, hidden risks, and required tests."
3. "Revise the plan to avoid schema changes and keep the diff small."

---

# Common failure modes

- approving a plan that never named the touched files
- letting the agent execute against an ambiguous request
- treating Plan Mode as ceremony instead of real review
- using broad permissions to compensate for weak planning

---

# What success looks like

- smaller diffs
- fewer surprise edits
- earlier reviewer engagement
- clearer test expectations
- safer AI use in regulated codebases

---

# Key takeaway

- Planning is not delay.
- Planning is where you move uncertainty out of the repo and into a reviewable artifact.

---

# Bridge to Session 07

- Session 05 made intent explicit.
- Session 06 made execution reviewable.
- Next: how persistent project rules in `CLAUDE.md` keep those constraints alive across sessions.
