ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/06-instructor-assets/01-instructor-notes.md

# Instructor Notes

## The misconceptions most worth correcting

### Misconception 1 — AI matters mainly because it writes code quickly
Correction:
AI often creates more value when used for codebase understanding, documentation, test scaffolding, refactoring prep, and workflow cleanup.

### Misconception 2 — Technical debt means messy code
Correction:
Technical debt also lives in documentation, environment setup, test data, release process, observability, and security hygiene.

### Misconception 3 — Local full-system execution is always the standard
Correction:
For distributed systems, the better standard is meaningful local or isolated testability plus reproducible development workflows.

### Misconception 4 — Coverage equals confidence
Correction:
Coverage is one signal. Confidence comes from meaningful tests, stable fixtures, trustworthy pipelines, and runtime visibility.

### Misconception 5 — Observability is an operations topic
Correction:
Observability is part of maintainability and change safety. Teams need runtime visibility to refactor and ship safely.

### Misconception 6 — AI-generated changes should speed up review
Correction:
AI can speed drafting, but review needs to remain rigorous. Fluent output is not evidence.

## Places where students may be skeptical

- “This sounds like basic software engineering, not AI.”
- “We do not have time to fix all this.”
- “Our architecture is too distributed to run locally.”
- “Management only rewards new features.”
- “AI-generated tests are usually low quality.”

## Useful responses

- “Yes, the point is that AI becomes more valuable when basic engineering quality exists.”
- “You do not need to fix all of it. You need a better order of operations.”
- “This course explicitly makes room for isolated testability instead of unrealistic full-local parity.”
- “Feature speed without change confidence is a short-term illusion.”
- “Correct—AI-generated tests need review. That is part of the lesson.”

## What to emphasize repeatedly

- strong fundamentals increase AI leverage,
- poor fundamentals make AI noisier and riskier,
- small validated improvements beat big speculative refactors,
- operational visibility is part of software quality,
- repeatable practice matters more than a one-time cleanup sprint.

## Recommended pacing

- Keep conceptual framing concise.
- Move into repo inspection early.
- Use at least one concrete artifact every day: scorecard, backlog, prompt, checklist, or plan.
- End each session with one practical thing students could do in a real codebase next week.

## Good closing language

- “Use AI to make the hidden visible.”
- “Use AI to reduce recurring friction.”
- “Trust evidence, not fluency.”
- “The point is not more code. The point is easier change.”
