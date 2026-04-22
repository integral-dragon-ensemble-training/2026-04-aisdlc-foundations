# Workshop 4 — AI-Assisted Refactoring Review Checklist

Use this checklist before merging or endorsing an AI-generated change. It is designed to be applied to a single PR, diff, or change proposal. Each section asks for evidence, not vibes.

---

## Scope

- Is the change small enough to reason about in one sitting?
- Does it solve the stated problem, instead of expanding into adjacent cleanup?
- Is the blast radius named? (files, services, data, consumers)

## Understanding

- Did the AI identify its assumptions and the uncertainty in its reasoning?
- Can a human reviewer explain what changed and why, without re-reading the diff?
- Are the edges of the change well-defined: what it *will not* touch?

## Validation

- What tests prove the change is safe?
- Which assertions would fail if the change were wrong?
- What runtime or deploy-time checks exist to confirm it in operation?
- Were any security-sensitive areas touched (authn, authz, secrets, input handling, dependencies)?

## Operations

- Does this affect logs, metrics, traces, or deployment visibility?
- Is the deployed version still easy to verify after merge?
- Is there a rollback path if the change misbehaves?

## Quality

- Did the change reduce or increase complexity?
- Did it create hidden coupling or shallow abstractions?
- Is the naming honest? Do tests verify behavior, not implementation trivia?

## Decision

Pick one, with a one-sentence rationale:

- **Approve** — evidence is present, scope is controlled, risk is understood.
- **Narrow scope and revise** — the idea is good but the diff is too broad or under-tested.
- **Reject pending better evidence** — assumptions are unverified or validation is missing.

---

## How to use this rubric in a live review

1. Read the diff or proposal end to end before you open this checklist.
2. Work top to bottom. Note where the evidence lives, or note that it is missing.
3. State your decision in writing. If you narrow or reject, name the specific evidence that would change your answer.
4. Apply the same checklist to human-authored changes too. The standard is evidence, not authorship.

---

## What a strong review output looks like

- Specific about risk. Names the failure mode, not "could break things."
- Aware of missing validation. Does not approve because the summary sounds intelligent.
- Willing to cut scope. Treats "this is half a good PR" as a useful outcome, not a failure.
- Honest about its own uncertainty. If the reviewer cannot tell whether a seam is safe, the reviewer says so.
