# 070 Rerun Playbook

This playbook defines how to regenerate the Applied Practice course in a way that is logically consistent with the current course.

## Rerun Scope

Before rerunning, choose one scope:

- `source-refresh`: rerun research and regenerate candidate bundles
- `bundle-refresh`: reuse existing research, generate a new course bundle
- `live-refresh`: reuse `applied-practice 2`, regenerate live workshop materials
- `expansion`: expand current workshops into longer hands-on workshops

Do not mix scopes in one pass unless explicitly planned.

## Steps

1. Create a versioned rerun folder under `ai-assisted-engineering/__research/`.
2. Preserve the original prompts and source documents.
3. If refreshing research, run the Gemini deep research prompt first.
4. Run the follow-up classroom-asset prompt against the research output.
5. Generate one or more candidate bundles.
6. Select the candidate using the decision rule in `030-expansion-bundle-selection`.
7. Copy durable design and framework material into `_overview-internal`.
8. Generate or update workshop-local `slides`, `exercises`, `resources`, and `instructor` material.
9. Distill participant-facing material into `overview`.
10. Run terminology checks and render/update artifacts.
11. Record commit hashes and rerun notes back into `_pipeline`.

## Stable Invariants

These should remain stable across reruns:

- Applied Practice is about making real codebases easier for humans and AI agents to improve.
- The course starts with "what good looks like" before jumping into tools.
- Technical debt is treated as delivery and AI-agent friction.
- AI is used to inspect, improve, and validate, not to bypass engineering judgment.
- Validation includes tests, observability, security, and governance.
- The final state is a repeatable operating practice, not a collection of one-off prompts.

## Expected Variation

These may vary without breaking consistency:

- slide titles
- examples
- diagrams
- exercise prompts
- exact repository examples
- amount of facilitator detail
- phrasing around tools and governance

## Verification Checklist

Run from the repository root:

```bash
git status --short
```

```bash
find ai-assisted-engineering/2-Applied-Practice -maxdepth 3 -type f | sort
```

```bash
rg -n "Session|session|student|Student|one-hour|1 hour" ai-assisted-engineering/2-Applied-Practice
```

```bash
rg -n "Claude Code|technical debt|observability|security|governance|validation|repeatable" ai-assisted-engineering/2-Applied-Practice
```

Positive proof means more than no errors. A rerun should show:

- which research source was used
- which candidate bundle was selected
- which live workshop files changed
- which participant-facing files changed
- which rendered artifacts were refreshed
- what remains unverified

## Stop Conditions

Pause and ask for review if:

- the rerun changes the course thesis
- the selected bundle no longer maps cleanly to live workshops
- the output becomes mostly tool-specific training
- security and governance are treated as optional add-ons
- workshop expansion requires changing the folder strategy

