# Workshop 4 — Validation: Tests, Observability, Security

Module 02 · Workshop 04 of the AI-Accelerated Software Development Applied Practice. The guardrail workshop: where participants practice rejecting or tightening fluent-but-unchecked AI output.

## Workshop thesis

> AI-generated change + validation = trustworthy improvement.

Coverage is a count. Confidence is a capability. Tests, observability, and security each contribute a slice of real confidence, and AI-assisted changes should pass through explicit validation gates before merge.

## Learning outcomes

By the end of this workshop participants can:

- Distinguish coverage (a count) from confidence (a capability).
- Name the four components of operational visibility: logs, metrics, traces, deployment visibility.
- Apply a validation checklist to an AI-generated change and decide approve / narrow / reject.
- Map change types (docs, refactor, observability, dependency, migration) to the evidence each requires.

## Artifacts in this folder

### Slides

- `slides/workshop-4-slides.md` — markdown source (one slide per `---`).
- `slides/workshop-4-slides.html` — rendered HTML deck, 9 slides (title + 7 content + close).
- `slides/workshop-4-slides.pdf` — PDF render of the HTML deck.

### Exercises

- `exercises/workshop-4-exercises.md` — Exercise 6 (Observability Gap Review), Exercise 7 (AI-Assisted Refactoring Review), and three lightweight activities (Confidence or Theater?, Where Would You Put the Log?, Score the Diff).
- `exercises/workshop-4-exercises.docx` — pandoc render.
- `exercises/workshop-4-rubric.md` — AI-Assisted Refactoring Review Checklist.
- `exercises/workshop-4-rubric.docx` — pandoc render.

### Resources

- `resources/workshop-4-resources.md` — curated readings for Workshop 4: Practical Test Pyramid, OpenTelemetry primer, GitHub Actions CI, Code Scanning, Dependabot, Dependency Review, OWASP Top 10, SLSA, plus example repos.
- `resources/workshop-4-resources.docx` — pandoc render.

### Instructor

- `instructor/instructor-notes.md` — misconceptions worth correcting, pacing, emphasis.
- `instructor/discussion-prompts.md` — the workshop's prompts.
- `instructor/sample-answers.md` — sample answer guidance for Exercises 6 and 7 and the lightweight activities.
- `instructor/participant-handout.md` — the participant handout.

## Delivery notes

- The slide deck is built on the shared Integral Dragon template (navy + cyan). No orange, no purple.
- The core exercise of the workshop is Exercise 7. Leave at least 20 minutes for it.
- If time is tight, drop a lightweight activity; do not compress the refactoring review.
