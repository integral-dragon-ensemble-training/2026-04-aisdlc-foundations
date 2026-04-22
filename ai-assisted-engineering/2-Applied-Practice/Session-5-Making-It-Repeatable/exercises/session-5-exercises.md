# Session 5 — Exercises

These exercises convert everything from Sessions 1–4 into an executable near-term plan and a disciplined, repeatable workflow.

---

## Exercise 8 — 30-Day Improvement Plan

**Objective**

Turn all prior analysis (scorecard, debt inventory, AI-assisted findings, validation review) into a staged plan the team could actually run in the next 30 days.

**Estimated time**

20 minutes

**Format**

Group (3–5 students per team).

**Inputs required**

- Session 1 repository health scorecard,
- Session 2 friction map and debt inventory,
- Session 3 notes (docs gaps, architecture map, test ideas),
- Session 4 validation review (observability gaps, refactor review),
- AI assistant (optional).

**Instructions**

1. Choose **three quick wins** — visible, low-risk, finishable in under a week.
2. Choose **two structural improvements** — foundations that compound (reproducible setup, a real test for the riskiest path, schema-migration discipline, an architecture map).
3. Choose **one workflow or governance change** — PR template, small-diff norm, AI-assisted review checklist, Conventional Commits, cadence for scorecard reviews.
4. Choose **one validation improvement** — new telemetry, post-deploy smoke test, contract test, dependency review gate.
5. Choose **one measure to revisit in 30 days** — rescore the repo, re-rank the debt list, or track a single metric (onboarding time, build reliability, flake rate, time to diagnosis).
6. Put them in an order that **minimizes risk and maximizes leverage**. Start with visibility and confidence; standardize last.
7. For each item, write a single sentence on **who owns it** and **what evidence shows it is done**.

**Expected output**

- A 30-day plan with seven actions plus one check-in,
- Sequencing rationale (one paragraph),
- Owner suggestions where appropriate,
- One measurable follow-up.

**How AI should be used**

- AI can draft the plan and sequencing.
- AI can suggest owners based on the repo history.
- Humans must test whether the plan fits team reality, available time, and deployment risk.
- Do **not** accept AI sequencing without challenging it against the team's real calendar.

**What a good answer looks like**

- Constrained — seven items, not seventy.
- Prioritized — order is defensible, not alphabetical.
- Realistic — the team can actually do this alongside normal work.
- Focused on leverage rather than completeness.
- Starts with visibility and confidence; ends with standardization.
- At least one non-code item (docs, workflow, telemetry).

**Common weak patterns**

- Too many items — the plan becomes a backlog dump.
- All structural work and no quick wins — nothing visible to show in week one.
- All quick wins and no structural work — the team never compounds.
- No validation or measurement component.
- "AI will do it" treated as ownership.
- Big-bang rewrite disguised as "structural improvements."

---

## Lightweight in-class exercise — Rewrite or Stage It?

**Format**

10–15 minutes. Individual thinking, then group vote, then 2-minute debate on the tightest cases.

**Instructions**

For each engineering situation below, choose **one**:

- **Rewrite** — replace the module/service from scratch,
- **Staged refactor** — improve incrementally without changing the external shape,
- **Documentation first** — understanding is the real blocker,
- **Testing first** — confidence is the real blocker,
- **Observability first** — visibility is the real blocker.

Then justify the choice in one sentence. The right answer is often *not* rewrite.

### Situations

1. A payments service where nobody on the team understands the retry logic. It has been working fine for two years.
2. A legacy reporting job that takes six hours, fails once a week, and leaves no useful error output.
3. A microservice with a small, clean codebase that runs on a framework version that hits end-of-life in nine months.
4. A 4,000-line "utilities" file that everything imports from, with no tests and no clear ownership.
5. A customer-facing API endpoint whose behavior is documented only in a Slack thread from 18 months ago.
6. A shared database migration process that has broken three of the last five deploys.
7. An auth module that works, has good tests, and was written by a contractor who left. The code is slightly unidiomatic.
8. A frontend built on a deprecated framework. Users like it. Rebuilding it would take six months.

**Discussion moves**

- Which situations did the class split on? Why?
- Which situations are almost always "stage it," and which occasionally justify a rewrite?
- What evidence would change the answer for each borderline case?
- Where would AI be genuinely useful — and where would it push the team toward the wrong choice?

**What a good answer looks like**

- Treats rewrite as the rare option.
- Names the *real* blocker (understanding, confidence, visibility) before choosing an action.
- Distinguishes "the code is ugly" from "the code resists change."
- Asks what evidence would make a rewrite defensible, instead of refusing the idea categorically.
