# Session 2 — Technical Debt as Friction

Module 02 · Session 02
Treat debt as the repeated tax the system charges on every change.

---

# Technical debt is friction, not just ugly code

- Debt is any deficiency that increases the cost, risk, or time of future changes.
- Code style is one slice. Environment, data, release, observability, and workflow are larger slices.
- The **principal** is the underlying deficiency. The **interest** is the repeated extra effort the team keeps paying.
- If a problem slows routine change, raises regression risk, or hides whether the system is healthy — it counts.

---

# The nine debt categories in this course

- **Knowledge debt** — missing or misleading understanding.
- **Design debt** — structure that makes change unnecessarily hard.
- **Environment debt** — drift or fragility in developer and test environments.
- **Quality-confidence debt** — inability to know whether a change is safe.
- **Release debt** — weaknesses in build, versioning, and deployment.
- **Data & schema debt** — untracked migrations, fragile seed data.
- **Observability debt** — inability to understand runtime behavior.
- **Security debt** — hardcoded secrets, unreviewed dependencies, weak provenance.
- **Workflow debt** — huge PRs, weak review norms, cleanup never scheduled.

---

# Principal vs. interest

- Principal: a snowflake setup script that only runs on one machine.
- Interest: two extra days of onboarding for every new engineer, every time.
- Principal: unclear module boundaries.
- Interest: reading five unrelated files to make one safe change, every bug fix.
- Principal: no deployment verification path.
- Interest: Slack archaeology after every release, by several humans.

The principal rarely shows up on the backlog. The interest is paid quietly, forever.

---

# How teams pay interest

- Slow onboarding because setup is unreliable.
- Fearful changes because tests are weak or flaky.
- Slack archaeology because docs are stale.
- Production debugging because logs and traces are poor.
- Release uncertainty because versions and deployments are unclear.
- Heroic individuals carrying knowledge that was never written down.

This should feel painfully familiar. That familiarity is the diagnosis.

---

# Prioritize by impact on flow and cost to fix

- **Quick wins** — high flow impact, low cost to fix. Do these first.
- **Strategic bets** — high flow impact, high cost. Stage them, don't rewrite.
- **Nice-to-have** — low flow impact, low cost. Batch opportunistically.
- **Avoid** — low flow impact, high cost. This is beautification; skip it.

High-frequency pain beats theoretically elegant cleanup. Favor debt that blocks common changes or affects multiple categories at once.

---

# Where AI helps on Day 2

- Turn a repo tour into a **categorized debt inventory**.
- Cluster vague complaints into knowledge, environment, release, or observability debt.
- Draft a first-pass cleanup backlog with quick wins vs. structural work.
- Estimate where interest is highest so humans can prioritize with evidence.

AI is not deciding the tradeoffs. It is accelerating inspection so humans can prioritize.

---

# Exercise: Friction map and debt inventory

- List 8–10 sources of friction in your repo or workflow.
- Classify each into one of the nine debt categories.
- Estimate the interest paid per week or per change.
- Rank by practical impact. Pick the top three for staged improvement.
- Plus two lightweights: **Smell or Debt?** and **The Highest-Interest Debt**.

Leave with a ranked list — not a complaint list.

---

# Technical debt is the repeated tax paid when the system resists change.

Name the debt. Separate principal from interest. Fix the friction that actually blocks flow.
