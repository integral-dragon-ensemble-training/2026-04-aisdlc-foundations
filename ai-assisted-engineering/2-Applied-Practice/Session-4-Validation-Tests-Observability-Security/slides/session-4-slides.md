# Session 4 — Validation: Tests, Observability, Security

Module 02 · Session 04
Confidence beats speed. Validation is what turns cleanup into engineering.

---

# Improvements only count if they are validated

- A plausible diff is not a safe diff.
- Validation is what turns cleanup into engineering.
- Tests, observability, and security each contribute a slice of confidence.
- Today is the guardrail day: the day we say no to fluent-but-unchecked AI output.

AI-generated change + validation = trustworthy improvement

---

# Coverage is a count. Confidence is a capability.

- Coverage percentages can hide weak signal.
- Prefer tests tied to important behaviors and real failure modes.
- Fast feedback matters. Flaky tests erode trust even when they raise the number.
- Fixture quality and realistic data decide whether a green build means anything.

"92% coverage with no meaningful assertions is theater, not confidence."

---

# Observability is part of maintainability

A system that cannot explain itself in operation is hard to change safely.

- **Logs** — structured enough to diagnose, with correlation IDs and request context.
- **Metrics** — reflect real behavior and failure conditions, not vanity uptime.
- **Traces** — matter most when control flow crosses service boundaries.
- **Deployment visibility** — what version is live, and is it behaving correctly.

---

# Baseline security and supply-chain hygiene

- Secrets management — not casually embedded, not oral tradition.
- Dependency review — visible, routine, tied to the PR.
- Code scanning — automated baseline, not a one-time audit.
- Vulnerability visibility — the team knows what is outstanding.
- Safer defaults — in code and in configuration.

Security is baseline engineering, not optional polish.

---

# A validation checklist for AI-assisted changes

- What behavior changed?
- What tests prove it?
- What logs or metrics help verify it in runtime?
- What security or dependency risk changed?
- What assumptions did the AI make, and are they documented?

This checklist is meant to be re-used verbatim as a PR template.

---

# Validation gates by change type

Different changes need different evidence.

- **Docs** — accuracy review against the actual repo.
- **Refactor** — regression tests and behavior checks.
- **Observability** — log, metric, and trace verification in a real environment.
- **Dependency** — dependency review and scanning signals.
- **Migration** — rollback plan and compatibility thinking.

---

# Exercise: Review an AI-generated change like an engineer

- Read the proposed plan or diff.
- Identify assumptions and unknowns.
- Check what validation evidence actually exists.
- Decide: approve, narrow, or reject.

Debrief: "What made this output look good at first, and what made it unreliable on inspection?"

---

# Coverage is a count. Confidence is a capability.

Trust evidence, not fluency. Small validated improvements beat big speculative refactors.
