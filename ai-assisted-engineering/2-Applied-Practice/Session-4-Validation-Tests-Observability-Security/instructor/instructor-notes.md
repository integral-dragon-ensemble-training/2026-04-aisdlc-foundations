# Session 4 — Instructor Notes

## What this session is for

Day 4 is the guardrail day. It exists because a plausible AI-generated diff is not a safe diff, and because most teams over-trust fluency and under-trust evidence. The core claim of the session:

> AI-generated change + validation = trustworthy improvement.

If students leave with one line, it is that one.

## Misconceptions worth correcting in the room

### Coverage equals confidence

Coverage is one signal. Confidence comes from meaningful tests, stable fixtures, trustworthy pipelines, and runtime visibility. A 92% coverage number with mocked-to-oblivion assertions is theater.

### Observability is an operations topic

Observability is part of *maintainability*. Teams need runtime visibility to refactor safely and to verify that improvements are actually in use. If your system cannot explain itself in operation, it is hard to change safely.

### Security is a later-stage problem

Security and supply-chain checks are baseline engineering, not optional polish. AI can reduce this debt, and it can silently introduce it (insecure patterns from public repos, unsafe defaults, new dependencies).

### AI output should speed up review

AI can speed drafting. Review still needs to be rigorous. Fluent output is not evidence. The Score the Diff exercise exists to surface this directly.

## Places students are likely to push back

- "We have good coverage, we are fine." Counter with: name a real incident in the last year where the failure mode was covered by a passing test.
- "Observability is an SRE thing, not a dev thing." Counter with: who pays the cost when a refactor regresses silently in prod?
- "Security scanning is noisy and slows us down." Counter with: which specific finding would you defer, and what is your policy for that?

## Pacing

- Keep conceptual framing concise. The slides are a scaffold, not the substance.
- Get to the **Refactoring Review exercise** with at least 20 minutes left. It is where the day lands.
- Use the **lightweight Score the Diff** exercise if you have five extra minutes at the end. It works well as a closer because it puts the checklist into muscle memory.

## What to emphasize repeatedly

- Strong fundamentals increase AI leverage; weak fundamentals make AI noisier and riskier.
- Small validated improvements beat big speculative refactors.
- Operational visibility is part of software quality, not a separate concern.
- The standard for review is evidence, not authorship.

## Good closing language for Day 4

- "Trust evidence, not fluency."
- "Coverage is a count. Confidence is a capability."
- "A plausible diff is not a safe diff."
- "Use AI to make the hidden visible."
