ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/04-exercises/03-rubrics-and-scorecards.md

# Rubrics and Scorecards

## 1. Repository Health Scorecard

Score each category from 1 to 5.

| Category | 1 | 3 | 5 |
|---|---|---|---|
| Documentation & discoverability | misleading or absent | partially useful | accurate, actionable, current enough to trust |
| Architecture clarity | highly opaque | partial mental model possible | responsibilities and boundaries are understandable |
| Reproducible setup | snowflake setup | workable with friction | clean-machine setup is realistic and documented |
| Testability & quality confidence | weak signal | some confidence | clear strategy and meaningful confidence |
| Data/schema discipline | ad hoc and fragile | partial migration discipline | reviewable, versioned, reliable |
| Build/release discipline | manual mystery steps | mixed consistency | clear, repeatable, versioned |
| Observability & operability | poor runtime visibility | partial signals | useful logs, metrics, traces, and verification paths |
| Security & supply chain | little visible hygiene | some checks | baseline scanning and secret handling are deliberate |
| Workflow & collaboration | chaotic or hero-driven | some conventions | reviewable, consistent, small-change friendly |

### Interpretation

- 37–45: relatively healthy project
- 28–36: workable but carrying notable friction
- 18–27: debt is materially slowing change
- below 18: the team is likely paying high interest constantly

---

## 2. Technical Debt Assessment Rubric

For each debt item, score:

| Dimension | Low | Medium | High |
|---|---|---|---|
| Frequency of pain | occasional | recurring | constant |
| Change slowdown | minor | noticeable | severe |
| Risk added | low | moderate | high |
| Cognitive load | limited | annoying | exhausting |
| Blast radius | local | team-wide | multi-team / system-wide |
| Ease of staged improvement | hard | possible | good quick-win candidate |

### Priority hint

Highest priority items usually combine:
- high frequency,
- high slowdown,
- and a feasible staged improvement path.

---

## 3. AI-Assisted Refactoring Review Checklist

Use this before merging or endorsing an AI-generated change.

### Scope
- Is the change small enough to reason about?
- Does it solve the stated problem instead of expanding into adjacent cleanup?

### Understanding
- Did the AI identify assumptions and uncertainty?
- Can a human reviewer explain what changed and why?

### Validation
- What tests prove the change is safe?
- What runtime or deploy-time checks exist?
- Were any security-sensitive areas touched?

### Operations
- Does this affect logs, metrics, traces, or deployment visibility?
- Is the deployed version still easy to verify?

### Quality
- Did the change reduce or increase complexity?
- Did it create hidden coupling or shallow abstractions?

### Decision
- Approve,
- narrow scope and revise,
- or reject pending better evidence.

---

## 4. “What Good Looks Like” Checklist

Use this as a quick class handout or as a repo-review starting point.

- README is accurate
- local setup is documented
- architecture is understandable
- module boundaries are reasonably clear
- the project can be built in a clean environment
- tests provide real confidence
- schema changes are versioned
- test data has a strategy
- releases and versions are visible
- deployments can be verified
- logs are structured enough to help
- traces and metrics exist where complexity justifies them
- secrets are not casually embedded
- dependency and code scanning are visible
- code review workflow supports small, repeatable improvements

---

## 5. Student Prompt Template for Codebase Analysis

Use this prompt with Claude, Gemini, ChatGPT, or similar.

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
