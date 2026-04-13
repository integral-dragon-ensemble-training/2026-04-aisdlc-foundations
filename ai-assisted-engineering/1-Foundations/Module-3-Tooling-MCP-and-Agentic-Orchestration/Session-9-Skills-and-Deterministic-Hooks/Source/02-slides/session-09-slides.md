# Session 09
## Skills and Deterministic Hooks
### Good advice is useful; automatic enforcement is safer

---

# The model should not be your compliance memory

- "Remember to run tests" is not an engineering control.
- "Remember not to commit secrets" is not an engineering control.
- If a check is mandatory, the system should enforce it.

---

# Skills and hooks solve different categories of work

- Skills: reusable guidance, domain knowledge, workflow acceleration
- Hooks: deterministic behavior at defined lifecycle events
- The mistake is treating them as substitutes

---

# What a skill is good for

- reusable review patterns
- architecture-specific implementation guidance
- domain conventions
- multi-step workflows that still benefit from judgment

---

# What a hook is good for

- block unsafe commands
- auto-format after edits
- run validations after file changes
- protect specific files or paths
- trigger notifications or audit events

---

# Flexible guidance is not the same as mandatory enforcement

- A skill can improve consistency.
- A hook can guarantee the check ran.
- Enterprise teams need to know exactly where that boundary sits.

---

# Hooks run at lifecycle boundaries

- session start
- prompt submission
- pre-tool use
- post-tool use
- stop
- subagent start and stop

Those are control points, not just convenience triggers.

---

# Shared settings turn hooks into team controls

- user scope for personal automation
- project scope for team-shared guardrails
- local scope for experimentation
- managed scope for organization policy

---

# Example policy split

- Skill:
  - "review this API change against our service conventions"
- Hook:
  - "block edits to protected config files"
  - "run formatter after write"
  - "deny destructive shell commands"

---

# Live demo: add one useful hook

1. Start with an unsafe or forgetful workflow.
2. Add a project hook.
3. Trigger the event.
4. Show that the behavior is automatic.

---

# A strong hook policy reduces review burden

- fewer manual reminders
- fewer preventable mistakes
- clearer evidence that checks happened
- better confidence in AI-assisted changes

---

# Common failure modes

- encoding mandatory policy only in `CLAUDE.md`
- overusing hooks for tasks that still require judgment
- hiding team hooks in user-local settings
- installing automation nobody can explain or maintain

---

# Key takeaway

- Skills are reusable guidance.
- Hooks are deterministic enforcement.
- Keep the distinction sharp.

---

# Bridge to Session 10

- Once enforcement is in place, the next scaling problem is complexity.
- Session 10 focuses on breaking large work into isolated delegated tasks with subagents.
