ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/04-exercises/01-core-exercises.md

# Core Exercises

These exercises are designed to fit the five-session course.

## Exercise 1 — Repository Health Scorecard

**Objective**

Evaluate a repository against the “what good looks like” framework.

**Estimated time**

15–20 minutes

**Format**

Pairs or small groups

**Inputs required**

- a public GitHub repository or internal training repo,
- the repository health scorecard from `04-exercises/03-rubrics-and-scorecards.md`

**Instructions**

1. Review the README, repo structure, workflow files, and visible docs.
2. Score each project-health category from 1 to 5.
3. Write one sentence explaining each low score.
4. Identify the three weaknesses most likely to slow future change.

**Expected output**

- a scored rubric,
- a top-three problem list,
- a one-paragraph conclusion.

**How AI should be used**

Ask AI to:
- summarize the repo structure,
- identify missing docs,
- list visible testing and CI signals,
- but do not let AI assign scores without human review.

**What a good answer looks like**

- grounded in actual repo evidence,
- distinguishes weak setup from weak architecture,
- names the likely downstream effect of each weakness.

**Common weak patterns**

- scoring based on vibe,
- over-weighting code style,
- mistaking a long README for good documentation,
- assuming presence of tests equals confidence.

---

## Exercise 2 — Friction Map and Debt Inventory

**Objective**

Turn vague complaints into a categorized technical debt inventory.

**Estimated time**

15 minutes

**Format**

Small groups

**Inputs required**

- repo health notes,
- debt taxonomy from `01-course-foundation/03-technical-debt-taxonomy.md`

**Instructions**

1. List 8–10 sources of friction in the repo or workflow.
2. Classify each into a debt category.
3. Estimate the “interest” paid each week or each change.
4. Rank the items by practical impact.

**Expected output**

- a friction map,
- a ranked debt list,
- a short rationale for the top three.

**How AI should be used**

Use AI to:
- cluster findings,
- suggest missing categories,
- and draft a prioritized backlog.

**What a good answer looks like**

- specific and operational,
- focused on cost of change,
- avoids treating every annoyance as equally important.

**Common weak patterns**

- mixing symptoms and root causes,
- treating debt as only code debt,
- failing to identify high-frequency pain.

---

## Exercise 3 — Documentation Gap Hunt

**Objective**

Identify where the repo relies on tribal knowledge.

**Estimated time**

10–15 minutes

**Format**

Individual or pairs

**Inputs required**

- repo README and docs,
- AI assistant

**Instructions**

1. Ask the AI to outline what the repo seems to do.
2. Compare that with the repo’s actual documentation.
3. List the top missing or misleading documentation items.
4. Draft improved README sections.

**Expected output**

- gap list,
- draft replacement sections,
- one “questions still unanswered” section.

**How AI should be used**

Use AI for first-pass documentation rewrite and for spotting undocumented commands, configs, or architectural assumptions.

**What a good answer looks like**

- points to real missing knowledge,
- distinguishes “not documented” from “not discoverable,”
- includes uncertainty.

**Common weak patterns**

- generic README filler,
- missing platform or runtime assumptions,
- no attention to local setup.

---

## Exercise 4 — Architecture Map From the Repo

**Objective**

Produce a lightweight architecture understanding artifact.

**Estimated time**

20 minutes

**Format**

Pairs or groups

**Inputs required**

- repo tree,
- main application entry points,
- AI assistant

**Instructions**

1. Identify the main services, modules, or top-level application pieces.
2. Ask AI to draft a component map and list responsibilities.
3. Mark places where confidence is low.
4. Convert the result into a simple context/container/component narrative.

**Expected output**

- a one-page architecture summary,
- list of knowns and unknowns,
- likely high-coupling hotspots.

**How AI should be used**

AI should propose the first-pass map, but humans should edit it for accuracy and uncertainty.

**What a good answer looks like**

- honest about ambiguity,
- focused on responsibilities and boundaries,
- useful for future onboarding.

**Common weak patterns**

- diagramming package names without meaning,
- hallucinating flows,
- pretending uncertainty does not exist.

---

## Exercise 5 — AI-Assisted Test Improvement

**Objective**

Use AI to improve confidence in one specific area.

**Estimated time**

20 minutes

**Format**

Pairs

**Inputs required**

- one component, endpoint, or service,
- current tests if any,
- AI assistant

**Instructions**

1. Select one behavior that seems risky or under-tested.
2. Ask AI to propose test cases.
3. Review which proposed tests reflect true behavior versus implementation trivia.
4. Draft the final test plan or scaffold.

**Expected output**

- a prioritized test list,
- optional scaffold code,
- notes on what still requires human design judgment.

**How AI should be used**

AI can generate candidate cases and scaffolds, but students should filter aggressively.

**What a good answer looks like**

- tests observable behavior,
- includes edge cases or failure paths,
- explains why the test increases confidence.

**Common weak patterns**

- over-mocking,
- brittle tests,
- shallow assertions that merely exercise lines.

---

## Exercise 6 — Observability Gap Review

**Objective**

Evaluate whether the system is diagnosable in runtime.

**Estimated time**

15 minutes

**Format**

Group

**Inputs required**

- code sample, service flow, or public demo repo,
- observability checklist

**Instructions**

1. Identify the main request path or business action.
2. Ask what logs, traces, metrics, and deployment markers should exist.
3. Review what is actually present.
4. Recommend the top three observability improvements.

**Expected output**

- gap analysis,
- ranked telemetry improvements,
- verification plan after deployment.

**How AI should be used**

AI can propose missing telemetry and draft logging standards or runbook snippets.

**What a good answer looks like**

- tied to an actual workflow,
- distinguishes noise from useful signal,
- includes how the telemetry would be used.

**Common weak patterns**

- “add more logs” as the whole answer,
- dashboards without use cases,
- no attention to correlation or traceability.

---

## Exercise 7 — AI-Assisted Refactoring Review

**Objective**

Judge whether an AI-proposed change is safe, scoped, and worthwhile.

**Estimated time**

15 minutes

**Format**

Individual or pairs

**Inputs required**

- AI-generated change proposal or diff,
- review checklist

**Instructions**

1. Read the proposed change.
2. Identify assumptions and unknowns.
3. Check what validation evidence exists.
4. Decide: approve, narrow, or reject.

**Expected output**

- a review decision,
- a list of missing evidence,
- a rewritten, tighter scope if needed.

**How AI should be used**

Use AI to summarize the change and enumerate risks, but students make the final decision.

**What a good answer looks like**

- specific about risk,
- aware of missing validation,
- willing to cut scope.

**Common weak patterns**

- approving because the output sounds intelligent,
- rejecting without identifying what evidence would make it acceptable,
- ignoring deployment or runtime consequences.

---

## Exercise 8 — 30-Day Improvement Plan

**Objective**

Turn all prior analysis into a staged plan.

**Estimated time**

20 minutes

**Format**

Group

**Inputs required**

- scorecard,
- debt inventory,
- notes from exercises,
- AI assistant optional

**Instructions**

1. Choose three quick wins.
2. Choose two structural improvements.
3. Choose one workflow or governance improvement.
4. Choose one measure to revisit in 30 days.
5. Put them in an order that minimizes risk and maximizes leverage.

**Expected output**

- a 30-day plan,
- sequencing rationale,
- owner suggestions if appropriate.

**How AI should be used**

AI can draft the plan and sequencing, but humans should test whether the plan fits team reality.

**What a good answer looks like**

- constrained,
- prioritized,
- realistic,
- focused on leverage rather than completeness.

**Common weak patterns**

- too many items,
- all structural work and no quick wins,
- no validation or measurement component.
