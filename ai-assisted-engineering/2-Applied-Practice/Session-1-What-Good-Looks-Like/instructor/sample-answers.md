# Session 1 — Sample Answer Guidance

Reference notes to use while reviewing student work on the Repository Health Scorecard.

## Strong Day 1 scorecard outputs usually include

- A distinction between documentation quality and architecture clarity — students do not collapse them into "the docs are bad."
- Concrete evidence from the repo — file names, workflow files, missing sections, broken setup steps.
- Awareness that setup, observability, and release discipline are first-class categories — not afterthoughts.
- Honest uncertainty where the repo does not expose enough information — e.g., "I cannot tell whether schema migrations are versioned because no DB is visible in the repo tree."

## Common weak patterns across the week

These patterns start appearing on Day 1 and recur through Day 5. Flag them early so students can self-correct later:

- Treating architecture as optional.
- Using "AI should fix this" as a substitute for prioritization.
- Confusing lots of text with good documentation.
- Equating coverage with confidence.
- Proposing big rewrites instead of staged improvements.
- Ignoring operations and deployment visibility.

## Feedback style

- Praise evidence-grounded scores even if the score is "wrong."
- Push back on category scores that have no supporting sentence.
- Ask "what would change your score?" rather than correcting the number directly.
- Encourage students to name the *downstream effect* of each weakness ("this slows reviews," "this means deploys require the one person who knows the script"), not just the weakness itself.
