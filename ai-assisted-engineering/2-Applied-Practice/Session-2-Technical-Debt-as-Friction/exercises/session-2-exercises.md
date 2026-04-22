# Session 2 — Exercises

This session's work centers on turning vague complaints into a categorized, prioritized technical debt inventory. One core group exercise is supported by two short lightweight activities.

---

## Core Exercise — Friction Map and Debt Inventory

**Objective**

Turn vague complaints into a categorized technical debt inventory.

**Estimated time**

15 minutes.

**Format**

Small groups.

**Inputs required**

- Repo health notes from Session 1 (or a public / training repo you have access to).
- The debt taxonomy: knowledge, design, environment, quality-confidence, release, data & schema, observability, security, workflow.

**Instructions**

1. List 8–10 sources of friction in the repo or workflow. Be specific. "Setup is hard" is not enough — say what breaks.
2. Classify each item into one of the nine debt categories.
3. Estimate the "interest" paid each week or each change. Who pays it? How often? How much time?
4. Rank the items by practical impact on change cost, risk, and frequency.
5. Pick three items for staged improvement and write one-sentence rationales.

**Expected output**

- A friction map (list + category + interest estimate).
- A ranked debt list.
- A short rationale for the top three.

**How AI should be used**

- Cluster raw findings into debt categories.
- Suggest categories you may have missed.
- Draft a prioritized backlog as a first pass.
- Do **not** let AI assign final priority without human review.

**What a good answer looks like**

- Specific and operational, not generic.
- Focused on cost of change, not aesthetic complaints.
- Distinguishes symptoms from root causes.
- At least one non-code debt item in the top priorities (environment, docs, release, observability, workflow).
- Avoids treating every annoyance as equally important.

**Common weak patterns**

- Mixing symptoms and root causes.
- Treating debt as only code debt.
- Failing to identify high-frequency pain.
- Flattening priority so everything looks urgent.

---

## Lightweight Activity — Smell or Debt?

**Estimated time**

10 minutes.

**Instructions**

Give students the list below and ask them to sort each item into one of four buckets:

- code smell,
- broader technical debt,
- both,
- or neither.

**Examples to sort**

- Misleading README.
- No traceability in logs.
- Flaky end-to-end test.
- Giant service class doing five things.
- Unversioned database change applied directly in production.
- Hardcoded API key in a helper script.
- Commented-out dead code in a frequently-edited file.
- Inconsistent naming across modules.
- Setup instructions that only work on one operating system.

**Debrief**

- Smells tend to be local, code-level, and cheap to fix in isolation.
- Debt items are usually broader: they touch environment, data, release, or operations.
- "Both" is common — a smell can be a visible symptom of deeper debt.
- "Neither" is allowed — not every annoyance qualifies as serious debt.

---

## Lightweight Activity — The Highest-Interest Debt

**Estimated time**

10 minutes.

**Instructions**

Each participant writes down one debt item from their own environment and answers four questions:

1. What **category** of debt is it? (Use the nine-category taxonomy.)
2. Who **pays the interest**? (Individuals, a team, multiple teams, new hires?)
3. **How often** is it paid? (Every release, every PR, every incident, every onboarding?)
4. **Why does it matter**? (What change does it block? What risk does it add?)

**Debrief**

Read two or three aloud. Look for:

- repeated pain vs. one-off annoyance,
- who actually pays (often not the person who complains),
- and whether the cost is visible to leadership.

The goal is to make the invisible tax visible.
