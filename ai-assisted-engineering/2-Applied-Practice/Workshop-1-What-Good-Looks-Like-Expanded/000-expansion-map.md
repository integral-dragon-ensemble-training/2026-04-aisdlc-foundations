# 000 Expansion Map

This map turns the original one-session Workshop 1 into a hands-on workshop sequence.

## Original Workshop 1

Original emphasis:

- define project health
- introduce nine categories
- introduce the top 12 checks
- run a Repository Health Scorecard exercise
- warn participants not to let AI assign scores without review

## Expanded Workshop 1

Expanded emphasis:

- convert the scorecard into a reusable Claude Code skill or equivalent repo-local instruction
- use Claude Code to collect evidence from a real repo
- make scoring evidence-based
- apply specific improvement patterns to weak categories
- rerun the scorecard and compare before/after deltas

## Narrative Spine

The workshop should feel like this:

```text
We are not asking AI to tell us whether a repo is good.
We are teaching AI what evidence to look for.
Then we use that evidence to make better engineering decisions.
Then we use AI to make one targeted improvement.
Then we measure again.
```

## Core Exercises

| Exercise | Purpose | Output |
| --- | --- | --- |
| `010-create-scorecard-skill` | Give Claude Code a reusable scoring frame. | Repo-local scorecard skill or instruction file. |
| `020-baseline-repository-health-scan` | Inspect a repo using the scorecard. | Baseline scorecard with evidence and uncertainty. |
| `030-architecture-clarity-and-diagrams` | Make architecture visible enough to discuss. | Current-state architecture notes and diagram. |
| `040-reproducible-setup-check` | Test whether setup is repeatable. | Reproducibility findings and setup fix candidates. |
| `050-testing-confidence-and-lockdown-tests` | Use AI to identify confidence gaps and create characterization tests. | Test strategy notes and candidate lockdown tests. |
| `060-improvement-loop-and-rescore` | Apply one small improvement and rerun the scorecard. | Before/after delta and next action list. |

## Day-Level Option

### Day 1 - Scorecard And Baseline

- Introduce "AI needs a quality target."
- Create the scorecard skill.
- Run a read-only repo scan.
- Produce the first baseline scorecard.
- Pick the top three weak areas.

### Day 2 - Architecture And Setup

- Use Claude Code to summarize architecture evidence.
- Use the architecture/diagramming skill to produce a current-state diagram.
- Inspect setup docs, scripts, tool versions, lockfiles, and environment assumptions.
- Identify the smallest docs or automation improvement that would reduce onboarding friction.

### Day 3 - Testing Confidence And Improvement Loop

- Ask Claude Code to map current test signals to actual confidence.
- Identify missing behavior tests and candidate lockdown tests.
- Apply one small safe improvement.
- Rerun the scorecard.
- Capture what changed, what did not, and what remains uncertain.

### Optional Day 4 - Team Repo Application

- Participants repeat the workflow on their own team repos.
- Instructor circulates and helps with scope control.
- Each team picks one category to improve.

### Optional Day 5 - Report-Out And Operating Practice

- Teams present baseline score, one improvement, and rescore delta.
- Compare which categories are recurring across projects.
- Convert recurring gaps into backlog items or working agreements.

## Guardrails

- Claude Code can collect evidence; humans own scoring decisions.
- Improvements should be small enough to review.
- Avoid broad rewrites.
- Do not let diagram generation become the deliverable; the deliverable is shared understanding.
- Lockdown tests should protect current known behavior before refactoring.
- If a repo contains sensitive code or secrets, run in an approved environment only.

