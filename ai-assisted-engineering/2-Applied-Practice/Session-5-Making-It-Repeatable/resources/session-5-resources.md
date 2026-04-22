# Session 5 — Resources

Curated readings and references for Day 5: *Making It Repeatable*. The focus is on release discipline, commit hygiene, and workflow automation that support a repeatable improvement practice.

---

## Core readings

### Semantic Versioning
Link: <https://semver.org/>

Why use it:
- Baseline reference for what release numbers *mean*.
- Lets a team signal compatibility intentionally instead of by accident.
- Useful vocabulary for the 30-day plan ("this is a MINOR; this is a MAJOR").

### Conventional Commits
Link: <https://www.conventionalcommits.org/en/v1.0.0/>

Why use it:
- Connects commit hygiene to release automation and changelog clarity.
- Small, reviewable commits become machine-readable — AI and tooling can both use them.
- Low-friction workflow norm to adopt as the "one workflow change" in the 30-day plan.

### semantic-release
Link: <https://github.com/semantic-release/semantic-release>

Why use it:
- Concrete example of automated release discipline.
- Shows how Conventional Commits + CI produce predictable versions, changelogs, and tags.
- Good model for "releases should not be heroic."

### release-please
Link: <https://github.com/googleapis/release-please>

Why use it:
- Practical, review-oriented release automation from Google Cloud.
- PR-based release flow keeps humans in the loop without manual bookkeeping.
- Useful contrast to semantic-release: same goal, different safety posture.

---

## Supporting references (from earlier in the week)

These come up naturally when standardizing the workflow.

- **GitHub Actions · Continuous Integration** — <https://docs.github.com/en/actions/get-started/continuous-integration> · baseline CI reference for the "baseline checks" norm.
- **Dependency Review Action** — <https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-the-dependency-review-action> · PR-time supply-chain gate.
- **pre-commit/pre-commit-hooks** — <https://github.com/pre-commit/pre-commit-hooks> · visible example of cheap, repeatable quality checks.
- **actions/starter-workflows** — <https://github.com/actions/starter-workflows> · reference points for good CI starting templates.

---

## Example repositories worth showing

### open-telemetry/opentelemetry-demo
Link: <https://github.com/open-telemetry/opentelemetry-demo>

Why use it:
- Strong teaching repo for the "observability and release visibility" step of the improvement sequence.
- Distributed system example with traces, metrics, and dashboards.

### fastapi/full-stack-fastapi-template
Link: <https://github.com/fastapi/full-stack-fastapi-template>

Why use it:
- Production-minded template with Dockerized setup, GitHub Actions, and migration structure.
- Good target for a "what 'done' could look like" conversation.

### devcontainers/templates
Link: <https://github.com/devcontainers/templates>

Why use it:
- Reproducible setup patterns — supports the "fix setup blockers" step in the sequence.

---

## Framing lines worth keeping visible

- "The point is not more code. The point is easier change."
- "Good engineering fundamentals make AI more useful."
- "AI amplifies clarity, but it also amplifies confusion."
- "Technical debt is the repeated tax paid when the system resists change."
- "If you cannot validate the change, AI only helped you move faster in the dark."
