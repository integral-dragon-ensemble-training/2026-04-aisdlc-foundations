# Session 2 — Instructor Notes

## Session purpose

Move students from "debt equals messy code" to "debt is the repeated tax the system charges on every change." By the end of the hour they should be able to classify a debt item precisely, estimate its interest, and prioritize it by impact on flow.

## Opening move

Ask: *"What do engineers complain about repeatedly that is not itself the business feature they are trying to change?"*

Let students answer for two or three minutes before introducing the taxonomy. The complaints are the raw material for the exercise; do not let the lecture replace their examples.

## Key teaching points

- Debt is anything that makes future changes slower, riskier, or harder to reason about.
- Code debt is only one slice. Environment, data, release, observability, and workflow debt are usually larger.
- Friction compounds through repeated use — interest is what matters, not the principal.
- Precise labeling (the nine-category taxonomy) moves the conversation from venting to diagnosis.
- Not all debt deserves the same attention. High-frequency pain beats theoretically elegant cleanup.

## Misconceptions most worth correcting

### Misconception 1 — Technical debt means messy code

*Correction:* Technical debt also lives in documentation, environment setup, test data, release process, observability, and security hygiene. Push back explicitly when students reduce it to code formatting.

### Misconception 2 — AI matters mainly because it writes code quickly

*Correction:* On Day 2, AI's value is inspection and classification — turning a repo tour into a categorized debt inventory, clustering findings, and drafting a first-pass backlog. AI is not deciding tradeoffs.

### Misconception 3 — Coverage equals confidence

*Correction:* Quality-confidence debt is not "no tests." It is the inability to know whether a change is safe. A green CI with shallow assertions is still debt.

### Misconception 4 — Observability is an operations topic

*Correction:* Observability is part of maintainability and change safety. Teams need runtime visibility to refactor and ship safely. It belongs in the debt taxonomy.

## Where students are often skeptical

- *"This sounds like basic software engineering, not AI."* — Agree. The point is that AI becomes more valuable when basic engineering quality exists.
- *"We do not have time to fix all this."* — You do not need to fix all of it. You need a better order of operations. That is what the prioritization exercise teaches.
- *"Management only rewards new features."* — Feature speed without change confidence is a short-term illusion. The friction map is a tool to make the hidden tax visible to leadership.

## Pacing (60 minutes)

- 0–10 min — opening question, define debt operationally, introduce principal vs. interest.
- 10–20 min — walk the nine-category taxonomy with concrete examples. Use student complaints from the opening.
- 20–30 min — "How teams pay interest" + priority 2x2 framing. Reinforce that high-frequency pain beats elegance.
- 30–50 min — Friction Map exercise in groups. If time allows, insert "Smell or Debt?" as a 10-minute warm-up.
- 50–57 min — debrief: share one group's top three; compare rankings.
- 57–60 min — exit prompt and Day 3 setup.

## What to emphasize repeatedly

- Debt is operational, not aesthetic.
- Principal vs. interest — the interest is where the real cost lives.
- Classification is prioritization's prerequisite.
- Small validated improvements beat giant speculative rewrites.
- Operational visibility is part of software quality.

## Exit prompt

*"Which kind of debt in your environment creates the highest repeated tax?"*

Ask students to write one sentence before leaving. These answers are the input for Day 3 — they tell you where AI-assisted inspection should point first.

## Good closing language

- "Use AI to make the hidden visible."
- "Use AI to reduce recurring friction."
- "Technical debt is the repeated tax paid when the system resists change."
- "The point is not more code. The point is easier change."

## What a "ready for Day 3" student looks like

- Can name at least one non-code debt item in their own environment.
- Can identify who pays the interest and how often.
- Has at least one ranked item they would be comfortable discussing with their team.
- Understands that AI is for inspection, not prioritization.
