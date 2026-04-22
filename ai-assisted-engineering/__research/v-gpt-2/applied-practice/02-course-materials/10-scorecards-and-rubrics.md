ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 10-scorecards-and-rubrics.md

# Scorecards and Rubrics

## A. What Good Looks Like — Repo Health Scorecard

Score each dimension from 0 to 3.

### 1. Architecture clarity
- **0** — no clear structure; unclear boundaries; engineers infer the system by trial and error
- **1** — some structure exists, but diagrams/docs are stale or partial
- **2** — boundaries and major flows are mostly understandable
- **3** — architecture, runtime flow, and ownership are clear and current

### 2. Onboarding and setup
- **0** — a new engineer cannot get running without tribal help
- **1** — partial docs exist but are unreliable
- **2** — most setup works with modest manual intervention
- **3** — setup is repeatable from a clean machine

### 3. Build reproducibility
- **0** — build process is fragile or environment-specific
- **1** — build works inconsistently
- **2** — build is mostly reliable with a known path
- **3** — build is deterministic and documented

### 4. Local run path
- **0** — no meaningful local run path
- **1** — partial local run path with hidden assumptions
- **2** — meaningful subset runs locally
- **3** — core workflows are locally runnable and documented

### 5. Test coverage and confidence
- **0** — little or no meaningful automated testing
- **1** — tests exist but provide weak confidence
- **2** — tests cover important behavior
- **3** — tests give fast and useful feedback across levels

### 6. Testability of design
- **0** — modules are tightly coupled and hard to isolate
- **1** — limited seams exist for testing
- **2** — most critical code can be exercised predictably
- **3** — seams, boundaries, and dependencies support focused testing

### 7. Data and migration discipline
- **0** — schema changes are ad hoc; test data is unmanaged
- **1** — some migration process exists but is inconsistent
- **2** — migrations and test data workflows are mostly controlled
- **3** — migrations, reset paths, and test data are disciplined and repeatable

### 8. Observability
- **0** — behavior is opaque after deployment
- **1** — logs exist but are inconsistent or low-value
- **2** — logs and some metrics/traces support troubleshooting
- **3** — logs, metrics, traces, health, and correlation are useful and consistent

### 9. Release and version visibility
- **0** — hard to tell what version is running
- **1** — some build/version info exists but is incomplete
- **2** — version and deploy state are usually visible
- **3** — version, health, and deployment verification are easy to confirm

### 10. Secrets and configuration hygiene
- **0** — hard-coded secrets or unsafe defaults exist
- **1** — secrets are partially managed but risky patterns remain
- **2** — configuration is mostly controlled and secrets are externalized
- **3** — secrets posture is strong and aligned with platform standards

### 11. Static quality gates
- **0** — linting and analysis are absent
- **1** — checks exist but are inconsistently enforced
- **2** — checks catch common issues reliably
- **3** — quality gates are part of normal change flow

### 12. Safe change process
- **0** — changes are large, risky, and poorly reviewed
- **1** — some review discipline exists
- **2** — changes are usually small and reviewable
- **3** — change flow is incremental, verified, and rollback-aware

## How to use the scorecard

- Score quickly first.
- Do not pretend the scores are exact.
- Use the scorecard to focus discussion.
- Look for the few dimensions that most reduce changeability.

## B. Debt Prioritization Matrix

Score each candidate debt item from 1 to 5.

| Factor | Question |
|---|---|
| Delivery speed | How much does this slow normal engineering work? |
| Reliability | How much does this contribute to incidents or hidden failures? |
| Onboarding | How much does this hurt new engineer productivity? |
| Security | How much risk does it create? |
| Observability | How much does it prevent diagnosis and verification? |
| Frequency | How often does the team trip over it? |
| Effort | How hard is it to improve? |
| Blast radius | How risky is the change itself? |
| AI suitability | Is this a good candidate for Claude Code CLI-assisted analysis or implementation? |

### Prioritization rule of thumb

Fix first:
- high pain
- high frequency
- low or moderate effort
- low or moderate blast radius
- strong AI suitability
- clear validation path

Defer:
- architecture fantasy projects
- broad rewrites
- changes with unclear ownership
- changes that cannot be validated

## C. Capstone rubric

Students should produce:
1. a scorecard for a repo or subsystem
2. the top 3–5 technical debt blockers
3. one recommended improvement per blocker
4. a “start here” improvement plan for the first two weeks
5. an explanation of how Claude Code CLI would help and where human review is mandatory

Grade on:
- clarity of diagnosis
- prioritization quality
- change safety
- realism of sequencing
- validation strategy
- quality of Claude usage

## D. Top 10 non-negotiables

1. Engineers can understand the system well enough to change it safely.
2. A new engineer can build and run the project without heroic effort.
3. Tests provide meaningful feedback on important behavior.
4. Schema and data changes are disciplined.
5. Logs and traces support diagnosis.
6. Teams can tell what version is deployed.
7. Secrets are not managed carelessly.
8. Changes are reviewed in small, understandable units.
9. CI or equivalent quality gates catch obvious regressions.
10. Documentation matches reality closely enough to be trusted.
