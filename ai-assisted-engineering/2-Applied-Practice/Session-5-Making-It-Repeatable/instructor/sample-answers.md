# Sample Answers — Session 5: Making It Repeatable

Use these notes to calibrate review of student work. The goal is to show instructors what "good" looks like, not to give students a template to imitate.

---

## Strong Day 5 plans usually include

*(From sample-answer-guidance.md)*

- A few quick wins.
- One or two structural improvements.
- One process or workflow change.
- A measurable follow-up point.
- Sequencing that starts with visibility and confidence.

A strong plan also tends to include:
- At least one non-code item (docs, telemetry, workflow).
- Named owners who actually exist on the team.
- A clear "done" criterion for each action.
- An explicit 30-day check-in with a measurement, not just a meeting.

---

## Strong answer — Exercise 8 (30-Day Improvement Plan)

### Context (given by the student group)

"Our repo is a mid-sized internal Python service. Scorecard weaknesses: README drift, no reproducible setup, one flaky integration test, no deployment verification, migrations sometimes break staging."

### The plan

**Quick wins — Week 1**
1. **Rewrite the README's "Getting started" section** so a new hire can run the service in under 30 minutes. *Owner: M. (senior engineer already onboarding the new hire).* *Done when: new hire runs the service from the README unaided.*
2. **Add a pre-commit hook config** with lint + format on touched files only. *Owner: J. (tooling lead).* *Done when: hook runs on every dev machine and in CI.*
3. **Purge the 11 dead links in `docs/`** and move the runbook from Confluence into the repo. *Owner: R.* *Done when: `docs/` has zero dead links and one linked runbook.*

**Structural improvements — Weeks 2–3**
4. **Add a devcontainer** to remove "works on my machine" setup drift. *Owner: J.* *Done when: a fresh clone plus "Reopen in Container" runs the full test suite.*
5. **Add a contract test for the riskiest external API** (billing provider). *Owner: M.* *Done when: test runs in CI and has caught at least one intentional regression in a spike branch.*

**Workflow change — Week 2**
6. **Adopt a PR template** requiring (a) scope, (b) validation evidence, (c) risk. Small-diff preference codified. *Owner: team lead.* *Done when: every merged PR in weeks 2–4 uses the template and diffs average under 300 lines.*

**Validation improvement — Week 3**
7. **Add a post-deploy smoke test** that hits the `/health` and one real read endpoint, and fails the deploy if either fails. *Owner: ops partner.* *Done when: the last three deploys end with a green smoke test or an automatic rollback.*

**30-day check-in — End of Week 4**
- **Rescore the repo health scorecard** and compare against the baseline captured in Session 1.
- Track one primary metric: **build reliability on main** — target from ~70% green to ≥85% green without retries.

### Sequencing rationale

"We start with visibility (README, links, hook) because nothing else compounds without it. Then setup (devcontainer) and one real confidence investment (contract test), because onboarding and risk coverage block everything else. Workflow and validation go next because they become permanent norms rather than one-off work. The check-in is measurable and dated — we picked build reliability because it affects every engineer every day."

### Why this plan is strong

- Seven actions plus one check-in — not a backlog dump.
- Starts with visibility and a quick win (README), which gives the team something to show by Friday.
- At least one non-code item (PR template, docs, smoke test).
- Each item has a named owner and a stated "done when."
- Sequencing is defensible, not alphabetical.
- Structural improvements compound — devcontainer unblocks the next set of engineers; contract test gives confidence to refactor the billing path.
- Validation is a concrete signal (smoke test + rollback), not "more logs."
- The check-in uses a real baseline from Session 1 and a specific metric.

---

## Adequate answer (still passes)

- Seven items with owners, but sequencing is weak (structural items in week one).
- Quick wins are real but mostly cosmetic (README, link purge, logo fix).
- Workflow change is vague ("we will write better PRs").
- Validation improvement is "add more logs."
- Check-in is a meeting, not a metric.

**Instructor response:** praise the prioritization; push on the sequencing and on what "done" means.

---

## Weak answer (needs intervention)

- 12+ items on the plan. No sequencing.
- Quick wins are all "small refactors" that touch production behavior.
- Structural improvement is "rewrite the auth service."
- Workflow change is "use AI for all PR reviews."
- Validation improvement is "increase coverage to 90%."
- No owners. No check-in.

**Instructor response:**
- Reject the rewrite. Ask what the real blocker is.
- Cut the plan to seven items.
- Force a named owner and a "done when" for each item.
- Replace the coverage target with a risk-relevant test.
- Replace "use AI for PR reviews" with a concrete workflow norm (PR template, small-diff rule).

---

## Strong answer — lightweight exercise (*Rewrite or Stage It?*)

For each situation, a strong answer:
- Names the real blocker (understanding, confidence, visibility) before choosing an action.
- Treats rewrite as the rare option and justifies it with evidence, not aesthetics.
- Distinguishes "the code is ugly" from "the code resists change."

### Expected answers (defensible, not the only valid ones)

1. **Payments retry logic, works fine, no one understands it.**
   → **Documentation first.** Then testing. Rewrite is tempting but dangerous; the system works. Blocker is understanding, not code.

2. **Six-hour reporting job, fails weekly, opaque errors.**
   → **Observability first.** You cannot fix what you cannot see. Rewriting without telemetry just produces a faster opaque failure.

3. **Small clean microservice on a soon-EOL framework.**
   → **Staged refactor** (or legitimate rewrite). Small and clean means the risk is bounded. This is one of the rare rewrite-defensible cases.

4. **4,000-line utilities file, no tests, no owner.**
   → **Testing first**, then staged refactor. Do not rewrite without a safety net.

5. **API endpoint documented in an 18-month-old Slack thread.**
   → **Documentation first.** Possibly contract test second. The endpoint works; the knowledge is missing.

6. **Shared migration process, broke 3 of last 5 deploys.**
   → **Staged refactor** *and* **observability**. Fix the migration pattern and add deploy-time checks. This is workflow debt, not code debt.

7. **Auth module, good tests, slightly unidiomatic, author gone.**
   → **Leave it alone.** Good tests. Works. Rewriting is a vanity project. At most, document the style choices for future maintainers.

8. **Deprecated frontend framework, users like it, 6-month rebuild.**
   → **Staged refactor / strangler pattern.** A 6-month freeze is not affordable. Replace page by page behind the existing shell.

### Weak patterns to correct

- Choosing "rewrite" for anything ugly.
- Choosing "testing first" reflexively without asking whether confidence is the actual blocker.
- Refusing "rewrite" categorically even in case 3 (the rare defensible case).
- Skipping the real-blocker question and going straight to an action.

---

## Common weak patterns across the week

*(From sample-answer-guidance.md — reinforce on Day 5 as the final synthesis.)*

- Treating architecture as optional.
- Using "AI should fix this" as a substitute for prioritization.
- Confusing lots of text with good documentation.
- Equating coverage with confidence.
- Proposing big rewrites instead of staged improvements.
- Ignoring operations and deployment visibility.
