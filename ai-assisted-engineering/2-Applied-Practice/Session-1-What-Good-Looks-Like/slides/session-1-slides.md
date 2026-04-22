# Session 1 — What Good Looks Like

Module 02 · Session 01
Define project health in practical terms.

---

# Why start with "what good looks like"

- If you cannot define healthy project qualities, AI will optimize the wrong thing.
- More code is not automatically progress.
- A good project is easier to understand, change, test, debug, and operate.
- Students need a quality target before they can talk about debt or use AI responsibly.

---

# A healthy project is more than clean code

- Clean code is only one slice of project health.
- Docs, environment setup, release process, and operational visibility are part of software quality.
- Teams suffer when these are weak even if the code style looks decent.
- Today we broaden the mental model from "clean code" to **project health**.

---

# Nine categories of project health

1. Documentation & discoverability
2. Architecture clarity & boundaries
3. Reproducible developer setup
4. Testability & quality confidence
5. Build, deploy & release discipline
6. Data, schema & environment discipline
7. Observability & operational insight
8. Security, secrets & supply chain
9. Workflow & collaboration discipline

---

# The top 12 "what good looks like" checks

1. The README is trustworthy.
2. Architecture is understandable at a glance.
3. Local setup is reproducible.
4. The project can be built in a clean environment.
5. Tests provide real confidence.
6. Schema changes are versioned and reviewable.
7. Test data is intentional, not accidental.
8. Versions and releases are visible.
9. Deployments can be verified.
10. Logs, metrics, and traces help explain behavior.
11. Secrets and dependency risk are managed deliberately.
12. Team workflow supports small, repeatable improvements.

---

# Important nuances

- "Run the full system locally" is not always realistic. Teach **meaningful local or isolated testability** instead of insisting on perfect local parity.
- "High test coverage" is not the same as confidence. Teach **risk-relevant testing**.
- "No passwords in code" is too vague. Teach **secrets management and secure defaults**.
- "Observability" is not just logs. Teach **logs + traces + metrics + deployment visibility + debugging usefulness**.

---

# Exercise: Repository Health Scorecard

- Review a real repo: README, structure, workflows, visible docs.
- Score each of the nine categories from 1 to 5.
- Write one sentence explaining each low score.
- Identify the three weaknesses most likely to slow future change.
- Use AI to summarize the repo and surface missing docs — but do not let AI assign scores.

---

# The point is not more code. The point is easier change.

Good engineering fundamentals do not compete with AI. They make AI more powerful.
