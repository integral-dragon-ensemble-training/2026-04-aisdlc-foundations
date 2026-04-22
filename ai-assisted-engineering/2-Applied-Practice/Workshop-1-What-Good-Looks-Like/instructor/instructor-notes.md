# Workshop 1 — Instructor Notes

Workshop 1 is the conceptual anchor for the whole course. If participants leave with a concrete rubric they trust, the rest of the course has traction. If they leave thinking "this is just basic software engineering, not AI" you lose half the audience for Workshops 2–5.

## Misconceptions most relevant to Workshop 1

### "AI matters mainly because it writes code quickly"

Correction: AI often creates more value when used for codebase understanding, documentation, test scaffolding, refactoring prep, and workflow cleanup. Workshop 1 is where you plant this seed — the scorecard exercise is a direct demonstration that AI-assisted analysis is higher-leverage than AI-assisted generation.

### "Technical debt means messy code"

Correction: Technical debt also lives in documentation, environment setup, test data, release process, observability, and security hygiene. The nine-category framework is the antidote to this misconception.

### "Local full-system execution is always the standard"

Correction: For distributed systems, the better standard is **meaningful local or isolated testability** plus reproducible development workflows. Call this out explicitly when you introduce the testability category — it preempts a common objection.

### "Observability is an operations topic"

Correction: Observability is part of maintainability and change safety. Teams need runtime visibility to refactor and ship safely. Repeat this phrasing: *"observability is part of maintainability."*

## Places where participants may push back in Workshop 1

- "This sounds like basic software engineering, not AI." → *"Yes. The point is that AI becomes more valuable when basic engineering quality exists."*
- "Our architecture is too distributed to run locally." → *"This course explicitly makes room for isolated testability instead of unrealistic full-local parity."*
- "Management only rewards new features." → *"Feature speed without change confidence is a short-term illusion."*

## What to emphasize repeatedly

- Strong fundamentals increase AI leverage.
- Poor fundamentals make AI noisier and riskier.
- End with a concrete artifact, not abstract agreement — the scorecard is that artifact.
- Use at least one real repo; do not keep the conversation purely abstract.

## Discussion prompts for Workshop 1

- If a new engineer joined today, what would block them first?
- What signals tell you a repo is healthy before you read much code?
- Which quality category does your team under-invest in the most?

## Sample-answer guidance for Workshop 1

Strong scorecard outputs usually include:

- distinction between documentation quality and architecture clarity,
- concrete evidence from the repo,
- awareness that setup, observability, and release discipline are first-class categories,
- honest uncertainty where the repo does not expose enough information.

## Good closing language

- "Use AI to make the hidden visible."
- "Trust evidence, not fluency."
- "The point is not more code. The point is easier change."

## Exit prompt

*"What are the top three missing qualities that most slow down changes in your team's codebase?"*

Capture responses — they seed Workshop 2's friction mapping exercise.
