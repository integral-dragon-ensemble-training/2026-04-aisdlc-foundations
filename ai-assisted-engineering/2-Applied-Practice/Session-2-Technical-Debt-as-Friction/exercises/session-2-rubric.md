# Session 2 — Technical Debt Assessment Rubric

Use this rubric to evaluate individual debt items surfaced during the Friction Map exercise. Score each dimension Low / Medium / High, then use the priority hint at the bottom to select the items worth attention first.

## Per-item scoring

| Dimension | Low | Medium | High |
|---|---|---|---|
| **Frequency of pain** | Occasional — a few times a quarter. | Recurring — weekly or every release. | Constant — every PR, every change. |
| **Change slowdown** | Minor — minutes added. | Noticeable — hours added per change. | Severe — days of delay, or the change is abandoned. |
| **Risk added** | Low — localized, easily reverted. | Moderate — touches a shared component or unclear area. | High — affects security, data integrity, or customer-visible behavior. |
| **Cognitive load** | Limited — one engineer handles it without friction. | Annoying — requires context-switching or asking around. | Exhausting — drains reviewers, blocks focus, leaks into off-hours. |
| **Blast radius** | Local — one file, one job, one person. | Team-wide — multiple engineers or one service. | Multi-team / system-wide — crosses ownership or affects production broadly. |
| **Ease of staged improvement** | Hard — no clear incremental path. | Possible — can be broken into meaningful steps. | Good quick-win candidate — can be addressed in one or two small changes. |

## Priority hint

The highest-priority items usually combine:

- **High frequency** of pain,
- **high change slowdown**, and
- a **feasible staged improvement path**.

Items scoring high on frequency, slowdown, and feasibility should go at the top of the backlog regardless of how small they seem. These are where AI-assisted cleanup produces the most leverage.

## De-prioritize with care

An item that scores high on cognitive load but low on frequency is often a morale hit more than a delivery blocker — still worth tracking, but not the first to fix.

An item that scores high on everything **except** ease of staged improvement is a strategic bet. It belongs in the plan but needs sequencing, not a sprint.

## What to record per item

For each ranked debt item, capture:

- The item name and a one-sentence description.
- Its category from the nine-category taxonomy.
- The six dimension scores above.
- Who pays the interest, how often.
- A one-sentence proposed next step (quick win, structural, or observe-first).
