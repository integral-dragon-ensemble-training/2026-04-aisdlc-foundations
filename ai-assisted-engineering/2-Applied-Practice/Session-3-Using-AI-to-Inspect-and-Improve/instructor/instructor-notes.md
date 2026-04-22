# Session 3 — Instructor Notes

## The main move of this session

Shift the room from "AI is impressive" to "AI is useful when aimed carefully." The session works when students leave with a sharper sense of **which AI tasks they will trust, which they will review, and which they will refuse** — and with a prompt shape they can actually reuse.

## Misconceptions most worth correcting today

### Misconception 1 — AI matters mainly because it writes code quickly

**Correction.** AI often creates more value when used for codebase understanding, documentation, test scaffolding, refactoring prep, and workflow cleanup. The capability map on Slide 2 (inspect / explain / propose / scaffold / standardize) is the spine of the day. Return to it whenever a student frames AI primarily as a typing accelerator.

### Misconception 6 — AI-generated changes should speed up review

**Correction.** AI can speed drafting, but review must remain rigorous. Fluent output is not evidence. This misconception is the one most likely to produce real damage in a production codebase, and it is the point of Slides 6 (Failure Modes) and 7 (Human Review Rules).

### Supporting misconceptions worth flagging

- AI-generated tests are not automatically good tests.
- Generated architecture diagrams are drafts, not sources of truth.
- A long, confident AI response is not a well-reasoned AI response.

## Places students may be skeptical

- "AI-generated tests are usually low quality." — Agree, partly. That is why Exercise 5 explicitly asks them to **filter** the generated tests, not accept them.
- "This sounds like basic prompt discipline, not AI engineering." — Yes. The point of prompt discipline is that it is the cheapest, highest-leverage thing most teams are not doing.
- "Our architecture is too weird for AI to map." — Possibly true. Exercise 4 is partly designed to produce that exact finding, expressed as a list of knowns and unknowns.

## Pacing (60 minutes)

- **0–5 min.** Opening move: show the weak prompt on Slide 3 live, then the tightened one. Let the room feel the difference before you explain it.
- **5–15 min.** Slides 2 (capability map) and 3 (prompt shape). Keep conceptual framing concise.
- **15–25 min.** Slides 4 (docs/architecture) and 5 (tests/small refactors). Move quickly — these are setup for the exercises.
- **25–30 min.** Slides 6 (failure modes) and 7 (review rules). This is where engineering discipline lands. Do not shortcut.
- **30–55 min.** Choose **one** core exercise to run live in the room (Documentation Gap Hunt is the lowest-barrier; Architecture Map is the highest-value). Assign the other two as follow-up on students' own repos. The lightweight exercises can be sprinkled as energy drops.
- **55–60 min.** Exit prompt and debrief.

## What to emphasize repeatedly

- Use AI to **make the hidden visible** — docs gaps, unclear module roles, untested behaviors.
- **Trust evidence, not fluency.** Every claim the AI makes about "the repo does X" needs a file path.
- **Small, scoped, reviewable.** If a student's AI output cannot be reviewed line by line, the scope is wrong.
- Fluent output is the **most dangerous** output, because it is the hardest to push back on.

## When to cut material

- If time is short, cut Slide 5 down to one bullet ("small, scoped, reviewable").
- The lightweight exercises are all optional — pick at most one.

## Exit prompt

> "What AI-generated outputs would you trust after review, and which would you never trust without deeper verification?"

Capture answers on the board. The shape of the list — not the specific items — is the artifact you want the class to leave with.

## Good closing language

- "Use AI to make the hidden visible."
- "Trust evidence, not fluency."
- "The point is not more code. The point is easier change."
