# Session Brief

## Session 16

## Auditability and Workflow Narration

### Purpose

Teach students how to make AI-assisted work reconstructable by combining immutable records, explicit narration, and reviewable trace evidence.

### Why this session matters

A correct result that nobody can explain is still an enterprise problem. If an auditor, security reviewer, or incident responder asks why the system chose a path, the team must be able to answer with evidence, not just confidence. Auditability turns the workflow itself into a defensible artifact.

### Learning outcomes

By the end of this session, students should be able to:

- explain why narration is part of the engineering record
- identify the minimum evidence needed to reconstruct an AI-assisted change
- distinguish logs, traces, PR notes, and human justification
- export or preserve a Claude Code session record for later review
- attach trace evidence to a PR description without turning it into noise

### Core ideas

#### 1. A working outcome is not enough

Teams often stop once the code works. Enterprise work also needs to answer how the code was produced, what was reviewed, what was changed, and what evidence supports the decision.

#### 2. Narration is a control, not a luxury

If the engineer cannot explain the architectural choices, the process is under-documented. Narration forces the human to own the reasoning, not just the result.

#### 3. Logs and traces are complementary

Logs show what happened. Traces show how one action relates to another. Narration explains why the path was taken. A strong record uses all three.

#### 4. Review artifacts should survive later scrutiny

PR descriptions, session logs, and trace evidence should make the path from request to change reconstructable by someone who was not in the session.

#### 5. Auditability is a delivery requirement

This is not just compliance theater. Auditability protects the team during incidents, reviews, regulated delivery, and postmortems.

### Engineering implications

- session logs should be preserved where the team can retrieve them
- PRs should capture rationale, not only a summary of changes
- logs and trace evidence should be attached when the decision path matters
- the team should be able to answer who approved, who changed, and why
- Session 16 closes the foundations arc by making the workflow itself reviewable

### 23-minute flow

- `00:00-04:00`: Why traceability matters even when the code works
- `04:00-09:00`: Logs, traces, narration, and PR evidence
- `09:00-14:00`: What should be captured for reconstruction
- `14:00-18:00`: Live session-log export and PR narration demo
- `18:00-21:00`: Compliance and incident-response value
- `21:00-23:00`: Debrief and bridge to Module 05

### Key takeaway

If the team cannot reconstruct the decision path, the workflow is not auditable enough for enterprise use.
