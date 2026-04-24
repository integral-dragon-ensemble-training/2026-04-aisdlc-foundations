# Historic Engineering-Insight Analysis — Project Plan

**Goal.** Produce the engineering insight dashboard *for real*, once, against the last three months of actual ADO + git + incident data for a chosen scope. Every number on the dashboard must link back to the query, commit, or work-item that produced it.

**Audience.** The output is for engineering and executive leadership. The process itself is also a proof of what the Applied Practice methodology can do before we sell running it on a cadence.

**Not in scope (yet).** Running this weekly. Multi-service rollup. Real-time telemetry. All of those are follow-ups that only make sense after the one-off works.

---

## Honest confidence statement

Before committing, read this:

| Piece | Confidence | Notes |
|---|---|---|
| **95%-confidence signals dashboard** on 2-month consistency view | **Very high** (~95%) | Every tile is a row count or aggregate from `az devops` / `git`. No inference. This is what we commit to deliver. |
| Producing the *ambitious* dashboard (narrative + cost framing) | **High** (~85%) | Data exists; narrative requires human judgment round-trip |
| Precision of dollar/hour numbers | **Medium** (~55%) | Publish ranges, not point estimates, on the first pass |
| Cross-linking git → ADO → incidents | **Medium** (~60%) | Depends on existing link discipline (`AB#NNN` refs, consistent labels) |
| Making this a weekly cadence | **Medium** (~60%) | Out of scope for this project but tractable afterward |

**Two dashboards, two confidence levels.** Use the 95% version as your floor — what you can absolutely deliver with read access to the repo and ADO. Use the ambitious version as your ceiling — the story you can tell once the signals dashboard has established credibility. The signals dashboard answers "is this real?" The ambitious dashboard answers "so what?"

If any of the medium items are below 40% for your environment, solve that first before committing to the ambitious dashboard. The signals dashboard works regardless.

---

## Objectives (what "done" looks like)

1. **A dashboard snapshot** dated for the 3-month window, identical in shape to [`engineering-insight-dashboard.html`](./engineering-insight-dashboard.html), populated with real numbers.
2. **A reasoning page** identical in shape to [`engineering-insight-dashboard-reasoning.html`](./engineering-insight-dashboard-reasoning.html), with every claim linked to the specific query, commit, or PR it came from.
3. **A raw evidence bundle** — the JSON outputs of every query, saved and committed so results are reproducible.
4. **A short written memo** (~1 page) — what the analysis found, what's signal, what's noise, what to act on first.

---

## Scope for the first run

**Pick one service.** Do not attempt the whole engineering org. A single service that is moderately active (dozens of PRs/month, active work items) is enough to produce a compelling dashboard. Recommendation: the codebase that generated the most rework in the last quarter, because the insights will be sharp.

**Window.** **Two consecutive months, analyzed separately, then compared.** Not "last 60 days as one bucket." The consistency between months is the headline finding — if the same files, the same cycle-time patterns, and the same PR behavior appear in both months, the signal is structural, not a bad week.

This framing does two things for the executive conversation:
1. **It pre-empts the "is this a one-off" objection.** You show the same finding in two independent windows.
2. **It sets the precision bar at "95% confidence direct measurement"** — see [`engineering-signals-dashboard.html`](./engineering-signals-dashboard.html) for the output format this targets. All numbers are row counts or aggregates from ADO / git queries. No derived cost numbers. No narrative inference in the dashboard itself — those go in the accompanying memo.

The more ambitious dashboard ([`engineering-insight-dashboard.html`](./engineering-insight-dashboard.html)) remains the target for the second run, once the signals dashboard has built credibility.

**Data sources (in priority order):**

1. **ADO Work Items** — estimate vs actuals, cycle time, tags, states
2. **ADO Repos** — PRs, branches, reviewers, comments, diffs
3. **ADO Pipelines** — build/test/release success rates, rollback counts
4. **Git** — commit history, file churn, co-change patterns
5. **Dependency / security scans** — existing Snyk, Dependabot, or ADO Advanced Security output
6. **Incident log or on-call notes** — if they exist in a queryable form. If not, skip.

---

## Phase plan

### Phase 0 — Access and plumbing (1–2 days)

**What happens.** Confirm you can read the data. This is where most projects in this space stall.

- Obtain a read-only ADO PAT with scopes: `Work Items (Read)`, `Code (Read)`, `Build (Read)`, `Release (Read)`.
- Confirm `az devops` CLI works against your org.
- Pick the target service and confirm its area path and repo ID.
- Clone the repo locally.
- Validate one of every query class: one `az boards query`, one `az repos pr list`, one `az pipelines runs list`, one `git log`.

**Exit criteria.** You can run every command on the reasoning page against real data and get something back (not necessarily meaningful yet).

**Risks.** ADO access is siloed; someone needs to provision. If Advanced Security is a separate license, dependency-scan data may not be reachable — fall back to local `npm audit` / `pip-audit` / `mvn dependency-check` runs.

### Phase 1 — Evidence extraction (2–3 days)

**What happens.** Run every query on the reasoning page. Save the raw JSON outputs. Don't try to be clever yet.

- One script per insight. Each script writes its output to `snapshots/<date>/<insight-slug>.json`.
- Include command metadata: timestamp, query string, row count, any warnings.
- Commit the snapshots folder — it's the audit trail.

**Exit criteria.** Every claim on the dashboard has a backing JSON file on disk.

**Risks.** Rate limits; long-running queries. Mitigate with `--top` caps and batched pagination. Some work-item fields are org-specific — expect to tune 2–3 WIQL queries.

### Phase 2 — Analysis and derivation (2–3 days)

**What happens.** Turn raw data into insights. This is where Claude earns its keep.

- For each insight, Claude reads the JSON + the relevant code, and produces a derived finding with evidence citations.
- Score the nine health categories using the evidence (not vibes).
- Identify the top 3 friction hotspots by combining git co-change data with ADO variance.
- Compute the AI-pipeline funnel (if the team has been labeling AI-assisted PRs; if not, skip this tile or note the gap honestly).
- Generate the "watching next" items from trend signals.
- **Report ranges, not points.** `40–50 engineer-hours/month`, not `42`. Tighten later.

**Exit criteria.** A JSON summary file per dashboard section, with every number sourced to a specific JSON line in Phase 1 output.

**Risks.** Over-claiming. This is the biggest single risk. Build in a "human review" step before any number leaves the repo. Document where Claude inferred vs. where the data is direct.

### Phase 3 — Render and review (1 day)

**What happens.** Plug the Phase 2 numbers into a templated version of the dashboard HTML + reasoning page. Send to 2–3 trusted engineers for a review pass before any executive sees it.

- Flag every claim the reviewers push back on for revision.
- Adjust language from "is" to "appears to be" wherever confidence is medium.
- Ship.

**Exit criteria.** Dashboard + reasoning HTML + memo, reviewed and revised, ready to present.

### Phase 4 (optional, later) — Cadence pipeline

**Only after the one-off works.** Wrap Phases 1–3 in a weekly job (ADO Pipeline or GitHub Action). Store snapshots by date. Build a "delta" view that compares weeks.

- Weekly cost: ~1 hour of human review per run, plus compute.
- Value: trend visibility. Tells you whether engineering health is improving.
- Prerequisite: the one-off has been shipped and trusted. Don't skip ahead.

---

## Effort estimate

**First run, single service, one engineer + Claude Code:**

| Phase | Days |
|---|---|
| 0 — Access and plumbing | 1–2 |
| 1 — Evidence extraction | 2–3 |
| 2 — Analysis and derivation | 2–3 |
| 3 — Render and review | 1 |
| **Total** | **6–9 working days** |

Double if you're building the cadence pipeline (Phase 4) in the same pass. Halve if the team already has well-linked ADO + git + tickets (rare).

---

## Deliverables

1. `historic-dashboard-YYYY-MM-DD.html` — populated dashboard for the 3-month window
2. `historic-dashboard-reasoning-YYYY-MM-DD.html` — same page, every claim linked to live query result
3. `snapshots/YYYY-MM-DD/` — raw JSON evidence bundle, one file per query
4. `memo.md` — executive summary, ~1 page: what we found, confidence on each finding, suggested first action
5. `README.md` — how to re-run the analysis, what PAT scopes are needed, what queries to tune for a different service

---

## Success criteria for the executive conversation

- Every number on the dashboard links to a query that reviewers can click through.
- The memo identifies 1–3 high-interest items worth acting on, with estimated payback.
- At least one reviewer outside the project confirms the findings match their lived experience of the codebase.
- The conversation ends with "what's the next one?" — not "how do we know this is real?"

If you get "how do we know this is real" in the room, the reasoning page should close that in under two minutes.

---

## Risks and what to do about them

| Risk | Likelihood | Mitigation |
|---|---|---|
| ADO access can't be provisioned in time | Medium | Start Phase 0 a week before the pitch date; prefer read-only PATs |
| Work-item linkage to commits is weak | Medium–High | Audit first; if <50% of PRs link to work items, drop ADO-cycle-time claims or use PR counts instead |
| Executives treat illustrative ranges as commitments | High | Lead every number with a range. Caveat in the hero tile. Use "appears to be" language |
| Analysis takes longer than estimated | Medium | Cap scope: one service, 3 months. Resist adding more |
| Numbers are underwhelming | Low | Pick a service that you already know has friction; boring services produce boring dashboards |
| Findings embarrass a team | Medium | Share findings with the team before any executive. Frame as "here's what we can fix," not "here's who failed" |

---

## What the proof-of-concept pitch sounds like

> "The dashboards we showed are mockups. Here's the project plan to produce a real one against the last two months of data — analyzed as two separate windows, compared head-to-head. The headline would not be any single finding. It would be how many of the top findings recur across both months. If the same three files top the churn leaderboard two months running, we have a credible, defensible, source-linked engineering picture of the service."
>
> "Six to nine working days, one engineer, one service. The 95%-confidence signals dashboard is what we commit to. The more ambitious insight dashboard would follow if the first run lands."

That's the ask that makes you look credible, not the ask to deploy this dashboard everywhere next quarter.

### Why two months, specifically

- **One month** reads like a snapshot. Skeptics will say the sample is too small or this particular month was weird.
- **Three months** as one bucket hides the consistency signal — you get a single aggregate number with no way to separate "this is real" from "this week was bad."
- **Two months analyzed separately** lets you show that the top 3 file-churn leaders, the top co-change pairs, the median cycle time, and the PR behavior patterns all **recurred**. The dashboard's headline becomes "8 of 10 top findings appeared in both months" — which is a statement about stability, not about any single finding.

An executive can challenge a number. They can't as easily challenge a stable pattern that showed up twice.
