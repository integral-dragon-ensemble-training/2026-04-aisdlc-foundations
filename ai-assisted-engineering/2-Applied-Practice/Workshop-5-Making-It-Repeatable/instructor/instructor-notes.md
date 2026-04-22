# Instructor Notes — Workshop 5: Making It Repeatable

## What this workshop is for

This is the close of Applied Practice. Participants have a scorecard, a debt inventory, AI-assisted findings, and a validation review. The job today is to turn all of that into a plan small enough to actually run and a workflow disciplined enough to keep running after the course ends.

The two failure modes to prevent:
1. **Rewrite fantasy** — "we should just rebuild this."
2. **Backlog dump** — "here are 40 things we should do."

Everything in this workshop pushes participants toward *staged, validated, small* improvements with owners and a follow-up date.

---

## Opening move

Ask the group: *"What would make this work after the class ends?"*

Let the group surface "cadence," "ownership," "a backlog," "management buy-in," "a PR template," etc. Collect those and write them visibly. The 30-day plan exercise should feel like a direct response to what they just said.

---

## Key teaching points

- Improvement work needs cadence, ownership, and a backlog — not a one-off sprint.
- Teams should standardize small, reviewable changes before they try to standardize anything ambitious.
- AI usage needs policy and workflow norms, not just access.
- The improvement sequence (visible → unblock → confidence → observability → standardize) is the operational form of the course thesis.
- Measurement choices should tie to changeability and confidence, not to vanity.

---

## Misconceptions most worth correcting today

### "We just need a cleanup sprint."
A sprint without cadence creates a temporary dip in debt followed by normal re-accumulation. The point is to change the workflow, not to run a one-time event.

### "Our situation requires a rewrite."
Sometimes true, but less often than participants think. Push them to name the real blocker — usually understanding, confidence, or visibility — before committing to rewrite.

### "We need management buy-in first."
Some of the work listed in the 30-day plan does not require any new budget — PR template, pre-commit hook, README fixes, a Conventional Commits adoption, a scorecard cadence. Protect the "do the visible parts first" framing.

### "AI will pick the plan for us."
AI can draft and sequence. Humans still own the plan, because only humans know the team's real calendar, political surface area, and fear level.

### "Governance is bureaucracy."
Lightweight governance — a PR template, a scorecard cadence, a small-diff preference — is not bureaucracy. It is a workflow norm. Keep it boring and useful.

---

## Pacing

| Segment |
| --- |
| Opening move + "what makes this last" brainstorm |
| Slides 1–3 (rewrite fantasy, improvement sequence) |
| Slides 4–5 (standardize, measure) |
| Lightweight exercise — *Rewrite or Stage It?* (group vote + debate on the tight cases) |
| Exercise 8 — 30-day plan (small groups produce the plan; instructor rotates) |
| Share two plans; close with "The point is not more code. The point is easier change." |

If you need to compress, cut the *Rewrite or Stage It?* exercise to five situations. The 30-day plan must not be rushed — that is the capstone.

---

## What to watch for in the 30-day plan

Strong groups produce plans that:
- have exactly seven actions plus one check-in,
- start with visibility or a quick win, not a refactor,
- include at least one non-code item (docs, telemetry, workflow),
- name a human owner for each action,
- state *what evidence* shows each item is done,
- sequence low-risk items before anything that touches production behavior,
- end with a measurable, dated check-in.

Weak groups produce plans that:
- list 15+ things ("we'll triage later"),
- are all structural work ("nothing to show for week one"),
- are all quick wins ("no compounding"),
- have no owner or vague owner ("the team"),
- have no measurement or check-in,
- propose a rewrite disguised as "rebuild X service."

Intervene early if you see the weak pattern forming.

---

## Where AI fits today

- **Good uses:** drafting the plan, suggesting sequencing, proposing owners from commit history, generating a PR template, generating a Conventional Commits guide, drafting a scorecard cadence proposal.
- **Bad uses:** letting AI decide what the team can actually do, accepting AI's sequencing without challenge, asking AI to rewrite a service as part of "staged improvement."

Phrases worth repeating:
- "Use AI to inspect, explain, propose, and standardize."
- "Use humans to decide, validate, and own the change."
- "Treat AI output as draft material with a burden of proof."

---

## Closing language

End on one of these (the canonical close is the first):

- "The point is not more code. The point is easier change."
- "Good engineering fundamentals make AI more useful."
- "Small validated improvements beat heroic cleanups."

---

## Exit prompt

*"What is one change your team could normalize next month that would permanently reduce friction?"*

Have participants write a single sentence before they leave. You can collect these as a signal of whether the material landed.
