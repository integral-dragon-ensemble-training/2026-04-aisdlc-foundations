# Workshop 3 — Sample Answer Guidance

Use these notes while reviewing participant work on the Workshop 3 exercises. The strong Workshop 3 pattern is simple: **structured, uncertain, evidence-grounded.**

## Strong Workshop 3 outputs usually include

- **Structured findings.** Per-category, per-component, or per-test-case — not one prose blob.
- **Explicit uncertainty.** Confidence levels, assumption flags, or an "unanswered questions" section.
- **Ranked recommendations.** At most three or five items, ordered by impact, not by length.
- **Small-scope improvement ideas.** "Refresh this README section" beats "rewrite the docs."
- **Avoidance of sweeping refactor claims.** If the participant's output recommends a big rewrite, they have missed the lesson.
- **Visible edits to AI output.** A participant who accepts the AI draft unchanged is not demonstrating the skill of the workshop.

## Exercise 3 — Documentation Gap Hunt

**Strong answers**

- List the gaps by category (setup, architecture, operations, ownership) rather than as a flat dump.
- Distinguish "not documented" from "documented but not discoverable."
- The drafted README sections are specific enough to paste into a PR — names of commands, config keys, file paths are all present.
- The "questions still unanswered" section is non-empty and is focused on things the repo does not answer, not things the participant did not read.

**Weak patterns to flag**

- Generic README filler ("add a Getting Started section").
- Missing platform or runtime assumptions (OS, language version, required services).
- Accepting the AI's summary of what the repo does without verifying.
- A gap list without replacement drafts — the point is to produce the fix, not name the hole.

## Exercise 4 — Architecture Map from the Repo

**Strong answers**

- Focused on responsibilities and boundaries, not package names.
- At least one area flagged as low confidence or speculation.
- A narrative, not just a diagram — a reviewer can read what it claims.
- Names one specific thing the AI's first pass got wrong, with the correction.
- Useful as an onboarding document — a new engineer could read it productively.

**Weak patterns to flag**

- Diagramming the filesystem tree and calling it architecture.
- Accepting hallucinated flows (especially cross-service or cross-boundary flows) without verification.
- Over-confident single-sentence claims about components.
- No narrative — just boxes and arrows.

## Exercise 5 — AI-Assisted Test Improvement

**Strong answers**

- Tests target observable behavior — inputs, outputs, side effects, error paths.
- Include edge cases or failure paths, not just happy path.
- Each selected test has a sentence explaining why it increases confidence.
- Names which AI-proposed tests were discarded and **why** (over-mocking, implementation-detail assertions, redundant cases).
- Respects scope — tests one component well rather than dozens shallowly.

**Weak patterns to flag**

- "The AI generated 20 tests and I kept them all."
- Over-mocking that tests the mock, not the code.
- Brittle tests that would break on a harmless refactor.
- Shallow assertions that merely exercise lines.
- No prioritization — all tests treated as equally important.

## Lightweight exercises

- **Prompt Tightening.** Strong rewrites explicitly address all five levers (scope, criteria, output structure, uncertainty, validation). A strong answer is also **shorter than you'd expect** — tightness is not verbosity.
- **Is This a Good AI Task?** Strong groups separate tasks by **whether the human can verify the output**, not by how "AI-like" the task sounds. Security-sensitive changes and large architecture decisions land in "poor fit." Summarization and candidate generation land in "strong fit."
- **One Better Question.** Strong follow-ups demand evidence, narrow scope, or surface uncertainty. Weak follow-ups just ask for more of the same.

## Common weak patterns across Workshop 3

- Treating the AI response as a verdict instead of a draft.
- Confusing length and fluency with depth and correctness.
- Over-generalizing from one AI run ("AI is great at this" or "AI is terrible at this") rather than reasoning about the specific task shape.
- Using "AI should fix this" as a substitute for prioritization.
- Avoiding review rigor on the (usually false) assumption that AI code is already close enough.

## How to grade leniently but honestly

Most participants will produce something imperfect on Workshop 3 — that is fine. The grading question is:

- Did they **shape the prompt** deliberately?
- Did they **filter the AI output** rather than accepting it?
- Did they leave with an **artifact they could reuse** on a real repo next week?

If those three are present, the workshop worked.
