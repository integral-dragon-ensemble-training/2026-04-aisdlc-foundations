# Engineering Insight Dashboard — Evidence Sources

Every claim on [`engineering-insight-dashboard.html`](./engineering-insight-dashboard.html) is intended to resolve to an **ADO query, a git command, or a scheduled scan** — not to Claude's opinion. This file maps each dashboard claim to the data source and the query that would back it in production.

Use this file when an executive (or auditor) asks "how do you know?"

## Elevator version

> Every claim on the dashboard resolves to either an ADO query, a git command, or a scheduled scan. None of it is Claude's opinion.

---

## Hero insight — "42 engineer-hours / month"

- **ADO.** Pull last 90 days of work items on the Claims Adjudication area path. Compare `Original Estimate` vs `Completed Work`. Roll up variance by epic.
- **Git.** `git log --since=3.months --numstat` on files appearing in the over-estimate tickets. Surface files that repeatedly co-change.
- **Incident DB.** Tickets tagged `rework` / `estimation-overrun` / `scope-creep` in the same window.

---

## Project-health scorecard (nine categories)

| Category | Where the score comes from |
|---|---|
| Documentation | README last-modified vs `git log` on setup scripts; broken-link scan; new-hire surveys from onboarding tickets |
| Architecture clarity | Claude-generated dependency graph; count of modules with >3 inbound/outbound edges; wiki diagram timestamps vs code |
| Reproducible setup | Fresh-clone in container, time to first `make test` pass; ADO tickets tagged `environment` in last 90d |
| Testability | CI logs: flaky-test rate, test-to-code ratio, % test names that reference behavior not implementation |
| Release discipline | ADO Pipelines: deploy frequency, rollback count, PR-merge-to-prod latency |
| Data / schema | `db/migrations/` completeness; seed-data presence; % migrations with rollback scripts |
| Observability | Middleware scan for correlation-ID injection; log-structure grep; dashboard inventory from Grafana / App Insights |
| Security | Dependency-scan (Snyk / Dependabot) history; secrets-scan clean runs; findings-to-remediation time |
| Workflow | ADO: PR size distribution, review turnaround, comment density, squash-commit discipline |

---

## Friction hotspots

### Claims submission API · entangled validation logic

- **Git.** `git log --follow` on `SubmissionService`, `PayerMapper`, controller; Claude flags co-change frequency.
- **ADO.** Sum of estimate variance on PRs touching ≥ 2 of those files.
- **Architecture.** Claude's dependency graph shows cross-module pull.

### Eligibility data pipeline · undocumented Oracle seed requirements

- **ADO.** Onboarding tickets with `blocked` status in last 6 months.
- **Git / Bitbucket.** Personal forks with seed-data commits that never landed in main.
- **Fresh-clone test.** Local setup passes but returns empty responses for ~30 % of eligibility codes.

### Denial-letter templates · release required for every legal copy change

- **Git.** `grep -r 'DenialLetter\|\.denial-template' src/` → templates are compiled artifacts.
- **ADO.** Tickets labeled `legal-copy-change`; average cycle time per ticket.
- **CI.** Pipeline step that bundles templates into the binary.

---

## AI-assisted change pipeline (127 → 34 → 22 → 14 → 9)

- **Claude-side log.** Every inspection question and evidence packet is persisted in the participant course-work repo (Workshop-1-Expanded design).
- **Git.** Branches under `workshop-*/<first-last>` count candidate changes; merges to `main` count the final tier.
- **ADO.** PR labels `ai-assisted`, `validated`, `group-reviewed` provide the filter; cycle time per label shows where changes got stuck.

---

## Confidence signals

- **Test-suite actionability 62 %.** Sample last 200 CI failures; Claude classifies whether each failing-test name matched the regression found in the fix PR.
- **Observability coverage 3 of 11.** Service catalog + middleware scan for correlation-ID presence on each hot-path endpoint.
- **Review-rigor parity 100 %.** ADO query: mean reviewers + mean comments on PRs labeled `ai-assisted` vs unlabeled.
- **Lockdown-test coverage 8 of 9.** Pre-refactor check: characterization tests must be present on any PR labeled `refactor` before merge.

---

## 30-day before / after delta

- Same scorecard method, run 30 days apart. Snapshots stored as JSON in the course-work repo — delta is a `diff`, not a narrative.
- **ADO.** Cycle-time query on the affected work-stream before vs after.

---

## Watching next

- **Payer integration drift.** Claude diffs `PayerAdapter` across all consumer services; reports forked signatures.
- **Denial-template extraction candidate.** Rolls up hotspot data × 12 for annualized cost signal.
- **Trace coverage on oldest services.** Same observability scan, filtered by service age from `git log --reverse`.

---

## Companion file

[`engineering-insight-dashboard-reasoning.html`](./engineering-insight-dashboard-reasoning.html) — interactive page that lets you click through each claim to see the specific ADO CLI, `git`, and shell commands that would run in production.
