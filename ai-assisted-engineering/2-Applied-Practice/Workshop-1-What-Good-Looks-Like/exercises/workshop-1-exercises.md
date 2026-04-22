# Workshop 1 — Exercises

This handout contains the core exercise for Workshop 1 plus one lightweight in-class activity. Both use the "what good looks like" framework as their anchor.

---

## Exercise 1 — Repository Health Scorecard

### Objective

Evaluate a repository against the "what good looks like" framework.

### Estimated time

15–20 minutes.

### Format

Pairs or small groups.

### Inputs required

- A public GitHub repository or internal training repo.
- The Repository Health Scorecard (see `workshop-1-rubric.md`).

### Instructions

1. Review the README, repo structure, workflow files, and visible docs.
2. Score each project-health category from 1 to 5.
3. Write one sentence explaining each low score.
4. Identify the three weaknesses most likely to slow future change.

### Expected output

- A scored rubric.
- A top-three problem list.
- A one-paragraph conclusion.

### How AI should be used

Ask AI to:

- summarize the repo structure,
- identify missing docs,
- list visible testing and CI signals.

Do not let AI assign scores without human review.

### What a good answer looks like

- Grounded in actual repo evidence.
- Distinguishes weak setup from weak architecture.
- Names the likely downstream effect of each weakness.

### Common weak patterns

- Scoring based on vibe.
- Over-weighting code style.
- Mistaking a long README for good documentation.
- Assuming presence of tests equals confidence.

---

## Lightweight — Missing Artifact Drill

### Objective

Practice naming the single most useful artifact for an ambiguous situation.

### Estimated time

10–15 minutes.

### Format

Individual or quick round-robin.

### Instructions

For each situation the instructor presents, answer one question:

> **What artifact would most reduce confusion here?**

Choose from:

- README section,
- architecture diagram,
- migration guide,
- runbook,
- test fixture strategy,
- PR template.

Be ready to explain, in one sentence, why that artifact is the highest-leverage thing to add first.

### Expected output

- A chosen artifact per scenario.
- A short rationale: who benefits, how often, and what confusion it removes.

### How AI should be used

Optional. You can ask AI to list candidate artifacts for a scenario, but the final choice and rationale should be yours.

### What a good answer looks like

- Tied to a specific reader or decision the artifact unblocks.
- Picks the artifact that reduces repeated confusion, not one-time confusion.
- Willing to say "no artifact — this is a conversation problem" when appropriate.

### Common weak patterns

- Defaulting to "more docs" without naming which docs.
- Picking the most elaborate artifact instead of the most leveraged one.
- Ignoring whether anyone will maintain the artifact once written.
