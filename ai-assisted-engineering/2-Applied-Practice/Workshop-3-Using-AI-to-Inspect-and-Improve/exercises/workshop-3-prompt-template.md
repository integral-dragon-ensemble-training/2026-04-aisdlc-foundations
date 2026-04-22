# Workshop 3 — Codebase Analysis Prompt Template

This is the participant-facing prompt template for structured repository analysis. It is the reusable asset that supports the three core exercises in Workshop 3 (Documentation Gap Hunt, Architecture Map, and AI-Assisted Test Improvement) and anchors the prompt-shape lesson of the workshop.

Paste this into Claude, Gemini, ChatGPT, or any capable coding assistant that has access to your repository. Adjust the language/stack line if relevant.

## Why this template works

It gives the AI five things a weak prompt does not:

- **scope** — the evaluation framework is named explicitly,
- **criteria** — nine project-health categories with graded expectations,
- **output structure** — per-category fields plus ranked findings and recommendations,
- **uncertainty requirements** — confidence levels, assumption flagging, facts-vs-inferences,
- **validation expectations** — what should be checked with tests, observability, or security before any major cleanup begins.

## The prompt

```text
Analyze this codebase as if you were a senior software architect assessing project health.

Evaluate the repository against these categories:
1. Documentation and discoverability
2. Architecture clarity and boundaries
3. Reproducible developer setup
4. Testability and quality confidence
5. Data/schema discipline
6. Build/release discipline
7. Observability and operability
8. Security and supply-chain hygiene
9. Workflow and collaboration discipline

For each category:
- summarize what you can confirm from the repo,
- list weaknesses or missing evidence,
- identify likely technical debt,
- explain how that debt slows future changes,
- rate the category from 1 to 5,
- state your confidence level and any uncertainty.

Then:
- rank the top 5 project-health problems,
- recommend 3 quick wins and 2 structural improvements,
- suggest what should be validated with tests, observability, or security checks before major cleanup.

Important:
- do not hallucinate missing architecture,
- clearly distinguish confirmed facts from inferences,
- prefer concrete repo evidence over generic advice,
- keep the output structured and concise.
```

## How to use the output

Treat the AI's response as a **first-pass draft**, not a verdict. For each claim the AI makes:

- check it against the repo before citing it,
- note any category where the AI's confidence seems higher than the evidence justifies,
- keep the rankings but verify the recommendations are appropriately scoped (a "quick win" should actually be quick in your environment).

The prompt is most useful when run against a specific, bounded repository — not against a monorepo of unrelated services in one sitting. Narrow scope, better output.

## When to tighten further

If the AI's output is still too generic, add any of these refinements:

- **Stack specificity.** `This is a Python/FastAPI service backed by Postgres, deployed via GitHub Actions to AWS ECS.`
- **Context anchor.** `The team's primary concern is slow change velocity. Bias findings toward things that increase cost-to-change.`
- **Evidence discipline.** `For every claim, cite at least one file path or config reference. If you cannot cite evidence, mark the claim as an inference.`
- **Output schema.** `Return your analysis as a JSON object with the schema I will now describe …`

## Related assets

- **Rubric #1 — Repository Health Scorecard** (Workshop 1) provides the graded interpretation for the 1–5 ratings this prompt produces.
- **Rubric #3 — AI-Assisted Refactoring Review Checklist** (Workshop 4) is the review gate for any change action taken on the back of this analysis.
