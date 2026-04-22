ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 08-exercise-pack.md

# Exercise Pack

## Day 1 Exercise — Repo Health Scorecard

**Learning goal**
Teach students to evaluate a codebase for changeability rather than aesthetics.

**Estimated duration**
15 minutes

**Setup**
- any representative brownfield repo
- Claude Code CLI available
- scorecard handout from `10-scorecards-and-rubrics.md`

**Student instructions**
1. Start Claude Code CLI in the repo.
2. Ask it to inspect the repository and summarize the engineering health.
3. Use the scorecard to assign 0–3 ratings across the 12 dimensions.
4. Identify the top three technical-debt blockers.
5. Decide which one you would fix first and why.

**Claude Code CLI prompt example**
```text
Inspect this repository and help me score it for engineering changeability.
For each of the following dimensions, summarize evidence from the repo and suggest a 0–3 score:
architecture clarity, onboarding/setup, build reproducibility, local run path, tests, testability, data/migrations, observability, release/version visibility, secrets/configuration, static quality gates, safe change process.
Do not modify files.
At the end, identify the top three blockers to safer change.
```

**Expected output**
- a completed scorecard
- a ranked blocker list
- one short explanation of the first improvement to attempt

**Debrief points**
- Did Claude distinguish evidence from inference?
- Which dimensions were easy to score?
- Which dimensions required human context outside the repo?

---

## Day 2 Exercise — README vs Reality

**Learning goal**
Train students to use Claude for documentation and environment-gap analysis.

**Estimated duration**
15 minutes

**Student instructions**
1. Ask Claude to compare README and actual setup/build/run paths.
2. Identify every setup assumption that is undocumented.
3. Draft a corrected README outline.
4. Review the outline manually and note missing business context.

**Claude Code CLI prompt example**
```text
Compare the README and onboarding docs in this repo to the actual project structure and scripts.
Identify inaccuracies, omissions, and ambiguous steps for a new engineer on a clean machine.
Then draft a corrected README outline with:
- prerequisites
- setup
- build
- run
- test
- troubleshooting
Do not update files until I approve the outline.
```

**Expected output**
- mismatch list
- improved README outline
- top setup blockers

**Debrief points**
- Documentation debt is often one of the cheapest high-value fixes.
- Claude can draft structure well, but exact commands and hidden environment dependencies need verification.

---

## Day 2 Exercise — Architecture Map

**Learning goal**
Use Claude to create a first-pass architecture summary from code, not slides.

**Estimated duration**
15 minutes

**Prompt — .NET version**
```text
Analyze this .NET solution and produce a first-pass architecture map.
Identify:
- projects and their likely responsibilities
- primary API entry points
- infrastructure dependencies
- test projects
- key runtime flows
- the places where the architecture is unclear or under-documented
Do not modify code.
```

**Prompt — Python version**
```text
Analyze this Python service and produce a first-pass architecture map.
Identify:
- entry points
- modules and responsibilities
- external services
- config and secrets patterns
- tests
- likely runtime flow
- the places where documentation is missing or misleading
Do not modify code.
```

**Expected output**
- architecture bullets
- probable dependency diagram content
- unanswered questions

---

## Day 3 Exercise — Testability Gap Analysis

**Learning goal**
Distinguish between “tests exist” and “the design is testable.”

**Estimated duration**
15 minutes

**Student instructions**
1. Pick one module or service.
2. Ask Claude why it is or is not easy to test.
3. Ask for the smallest viable changes that improve testability.
4. Reject any broad rewrite suggestion.

**Claude Code CLI prompt example**
```text
Review this module for testability.
Tell me:
- what makes it hard or easy to test
- where dependencies are too tightly coupled
- what the smallest viable seam-creating changes would be
- what tests would provide the highest confidence first
Do not make changes yet.
```

**Expected output**
- testability issues
- seam suggestions
- prioritized tests

**Debrief points**
- The first job is often making code testable, not generating a huge test suite.

---

## Day 3 Exercise — Migration and Test Data Review

**Learning goal**
Make students look at data discipline as part of changeability.

**Estimated duration**
10–15 minutes

**Claude Code CLI prompt example**
```text
Inspect this repository for database migration and test-data discipline.
Identify:
- where schema changes are defined
- whether migrations are versioned and traceable
- how local/dev/test data appears to be managed
- risks around drift, resets, or non-repeatable test runs
Then propose the smallest useful improvements.
```

**Expected output**
- migration maturity summary
- reset/reseed risk summary
- small improvement plan

---

## Day 4 Exercise — Observability Gap Hunt

**Learning goal**
Teach students to inspect whether the system is diagnosable.

**Estimated duration**
15 minutes

**Claude Code CLI prompt example**
```text
Inspect this service for observability quality.
Identify:
- where logs are emitted
- whether structured logging is likely
- whether trace or request correlation is present
- whether health checks exist
- whether version/build metadata is visible
Then propose one small and one medium observability improvement.
Do not modify code yet.
```

**Expected output**
- observability gap summary
- small improvement candidate
- validation approach

**Debrief points**
- Logging alone is not observability.
- “Can we follow a request?” is often a better question than “Do we have logs?”

---

## Day 4 Exercise — Version and Deploy Verification

**Learning goal**
Teach students to think about release confidence as part of engineering quality.

**Estimated duration**
10–15 minutes

**Claude Code CLI prompt example**
```text
Assess this project for version and deployment verification.
Can an engineer tell:
- what build version is running
- whether a specific deploy took effect
- whether the service is healthy
- whether there is enough information to verify QA or staging quickly
Suggest the smallest useful changes to improve that.
```

**Expected output**
- deploy-verification gap list
- proposed status/version endpoint or metadata strategy
- reviewer checklist

---

## Day 5 Exercise — Safe Incremental Improvement Plan

**Learning goal**
Turn diagnosis into a practical debt-paydown roadmap.

**Estimated duration**
20 minutes

**Student instructions**
1. Choose the top technical-debt item from prior exercises.
2. Ask Claude for an incremental improvement plan, not a rewrite.
3. Review the plan for effort, blast radius, and validation.
4. Convert it into a two-week plan.

**Claude Code CLI prompt example**
```text
Given these repo health findings, propose an incremental two-week debt-paydown plan.
Constraints:
- prefer small reviewable changes
- avoid broad refactors
- prioritize high-confidence improvements
- include validation steps
- call out where human review is mandatory
Return the plan as:
1. sequence of changes
2. why each change matters
3. dependencies and risks
4. expected confidence gains
```

**Expected output**
- 2-week plan
- first change candidate
- explicit validation and review gates

---

## Capstone Exercise — Brownfield Changeability Assessment

**Learning goal**
Synthesize the whole week.

**Estimated duration**
30–45 minutes, possibly homework or final class segment

**Deliverables**
- completed scorecard
- top 3–5 blockers
- one-page architecture summary
- first improvement plan
- statement of how Claude Code CLI was used
- statement of what still required human judgment

**Success criteria**
- realistic
- incremental
- validated
- aware of trade-offs
- grounded in repo evidence
