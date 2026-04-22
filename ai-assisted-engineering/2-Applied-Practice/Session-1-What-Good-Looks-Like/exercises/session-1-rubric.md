# Session 1 — Rubric and Checklist

Two instruments for Day 1:

1. **Repository Health Scorecard** — a scored rubric for the core exercise.
2. **"What Good Looks Like" Checklist** — a compact handout you can apply to any repo in minutes.

---

## 1. Repository Health Scorecard

Score each category from 1 to 5. Use the anchor descriptions to calibrate.

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

- **37–45** — relatively healthy project.
- **28–36** — workable but carrying notable friction.
- **18–27** — debt is materially slowing change.
- **below 18** — the team is likely paying high interest constantly.

### Scoring discipline

- One sentence of evidence per low score.
- Prefer concrete repo artifacts (file names, workflow names, doc links) over vibes.
- Flag categories where the repo does not expose enough information — uncertainty is a valid answer.

---

## 2. "What Good Looks Like" Checklist

Use this as a quick class handout or as a repo-review starting point.

- [ ] README is accurate.
- [ ] Local setup is documented.
- [ ] Architecture is understandable.
- [ ] Module boundaries are reasonably clear.
- [ ] The project can be built in a clean environment.
- [ ] Tests provide real confidence.
- [ ] Schema changes are versioned.
- [ ] Test data has a strategy.
- [ ] Releases and versions are visible.
- [ ] Deployments can be verified.
- [ ] Logs are structured enough to help.
- [ ] Traces and metrics exist where complexity justifies them.
- [ ] Secrets are not casually embedded.
- [ ] Dependency and code scanning are visible.
- [ ] Code review workflow supports small, repeatable improvements.

### How to use it

- Run through it in under five minutes on a new repo.
- Check items only when you have evidence, not a hunch.
- An unchecked item is not automatically a problem — note whether the gap matters for the work this team actually does.
