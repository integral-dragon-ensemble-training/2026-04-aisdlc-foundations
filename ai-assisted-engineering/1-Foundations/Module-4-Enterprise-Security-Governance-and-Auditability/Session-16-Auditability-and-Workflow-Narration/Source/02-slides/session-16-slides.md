# Session 16
## Auditability and Workflow Narration
### Make the path from request to result reconstructable

---

# A working result is not the same as an auditable result

- correct code can still be undocumented
- a successful demo can still be non-reproducible
- an approved change can still be impossible to defend later

The workflow must leave evidence.

---

# Narration is part of the engineering record

- what was asked
- what was observed
- what was changed
- why that path was chosen
- what evidence supports the choice

If the engineer cannot explain it, the record is incomplete.

---

# Logs, traces, and narration serve different jobs

- logs: discrete events and outcomes
- traces: the sequence and relationship of actions
- narration: the human justification and review context

You need all three when the decision path matters.

---

# What should be preserved

- session logs
- session transcripts or export artifacts
- PR descriptions
- review comments
- trace IDs or event references

If the team cannot retrieve these later, they were not captured well enough.

---

# Claude Code already exposes useful record signals

- prompt correlation
- tool events
- session state
- checkpointing
- usage and audit controls

Use the available signals instead of relying on memory.

---

# The PR should tell a story

- why this change exists
- why this approach was chosen
- what alternatives were rejected
- what evidence was checked
- what remains uncertain

That is narration, not padding.

---

# Live demo: export trace evidence and attach it

1. Export or capture the relevant Claude Code session record.
2. Summarize the reasoning in a PR narration.
3. Attach the trace evidence or link it in the PR description.
4. Show how the record supports later review.

---

# Compliance and incident response depend on this

- auditors need a defensible trail
- security teams need reconstruction ability
- incident responders need sequence and ownership
- leadership needs evidence, not assurances

---

# Common failure modes

- leaving the rationale in the chat buffer only
- writing a PR summary that explains nothing
- capturing logs but not making them retrievable
- assuming the code speaks for itself

---

# Key takeaway

- If the team cannot reconstruct the path, it cannot defend the path.
- Auditability turns AI-assisted work into enterprise-grade work.

---

# Bridge to Module 05

- Module 04 hardened the execution and recordkeeping layers.
- Module 05 turns those controls into applied workflow readiness for lab work.
