# Session 3 — Discussion Prompts

These are the day's prompts. Use them to open the session, transition between slides, or anchor the debrief after the exercises.

## Primary prompts (Day 3)

- **What AI tasks are genuinely high leverage in your environment?**
  Push students past "code completion." Listen for the tasks that fit the capability map: repo summarization, test scaffolding, docs drafts, refactor prep.

- **Which engineering tasks still demand the most human judgment?**
  Useful after Slides 6 and 7. Expect answers about architecture decisions, security-sensitive changes, and anything touching production behavior without good tests.

- **What makes an AI analysis output useful instead of generic?**
  This is the prompt-shape lesson in one sentence. Expect answers about scope, structure, and explicit uncertainty.

## Supporting prompts

- **Describe a time AI gave you a confident-sounding wrong answer about a codebase.**
  Great opener. Normalizes distrust of fluency. Pair it with a quick round-robin.

- **What would an AI have to produce for you to trust it with a PR?**
  Forces students to articulate their own review bar. Most will realize they have not stated one explicitly.

- **Which of today's capability-map jobs (inspect / explain / propose / scaffold / standardize) is the lowest-risk to try on your repo this week?**
  Good transition out of the lecture into the exercises.

- **If the AI told you "this module handles user authentication," what would you do before believing it?**
  A direct handle on "trust evidence, not fluency."

## Exit prompt

> "What AI-generated outputs would you trust after review, and which would you never trust without deeper verification?"

Ask every student to put one answer in each bucket. Capture the class pattern on the board. Don't adjudicate disagreements — the disagreements are the artifact.

## Prompt-for-the-prompts

If the room is quiet, pick a single repository visible in the session (public or student-provided) and run one question against it live:

> "Summarize what this repo seems to do based only on its structure and README. Flag everything you are inferring rather than confirming."

Let the class critique the answer. Most of the day's lessons surface in five minutes of that critique.
