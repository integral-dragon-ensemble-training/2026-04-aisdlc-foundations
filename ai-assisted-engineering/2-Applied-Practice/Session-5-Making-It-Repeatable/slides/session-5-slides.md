# Session 5 — Making It Repeatable

Module 02 · Session 05
Staged modernization over rewrite fantasies.

---

# Do not turn this into a rewrite fantasy

- Most teams cannot rewrite safely or quickly.
- Small, compounding improvements beat grand clean-slate plans.
- Start where friction is high and validation is possible.
- The goal is staged modernization, not a clean-sheet redesign.

---

# A practical improvement sequence

1. Make the system visible.
2. Fix setup and documentation blockers.
3. Increase confidence with tests and data discipline.
4. Improve observability and release visibility.
5. Standardize workflow and review norms.

This is the operational shape of the course thesis.

---

# What to standardize in team workflow

- Repo health scorecard reviews on a regular cadence.
- PR templates for AI-assisted work (scope, evidence, validation).
- Small-diff preference; narrow scope before merge.
- Baseline checks in CI (tests, lint, security, dependency review).
- Periodic debt review and prioritization sessions.

Governance can be lightweight and still useful.

---

# What to measure

- Onboarding friction — time to first local run.
- Time to first safe change — first merged PR for a new engineer.
- Build reliability — CI green rate without retries.
- Test stability — flake rate on main.
- Deployment verification speed — time from deploy to "known healthy".
- Incident diagnosis speed — time from alert to probable cause.
- Recurring friction categories — themes in the last 30 days of pain.

Tie every metric to a practical use. Avoid vanity.

---

# 30-day team plan

- Three quick wins — visible, low-risk, fast.
- Two structural improvements — setup, tests, or architecture clarity.
- One workflow change — PR template, review norm, or CI gate.
- One validation improvement — telemetry, contract test, or release check.
- One 30-day check-in — revisit scorecard, debt list, or a chosen metric.

Force prioritization. Teams do not need 30 actions; they need the right seven.

---

# The mature use of AI in engineering

- Use AI to inspect, explain, propose, and standardize.
- Require human review and evidence before merge.
- Treat AI output as draft material with a burden of proof.
- Prefer repeatable prompts and checklists over improvisation.

AI belongs inside disciplined engineering, not as a chaotic side channel.

---

# Final takeaways

- Good engineering fundamentals make AI more useful.
- Technical debt is friction that compounds with every change.
- AI is strongest in understanding and improvement work.
- Validation turns plausible output into trustworthy change.
- Small repeatable improvements beat heroic cleanups.

---

# The point is not more code. The point is easier change.

Staged modernization, validated improvements, and repeatable practice — that is what makes AI-assisted engineering lasting instead of loud.
