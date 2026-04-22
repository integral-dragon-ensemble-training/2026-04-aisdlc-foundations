# Expanded “What Good Looks Like” Framework

This file turns the abstract qualities of a good software project into teachable categories.

## A healthy software project is not just “clean code”

A project is healthy when a competent engineer can:

- understand what the system is for,
- find the relevant code and docs quickly,
- set up the environment without heroics,
- build and test meaningful changes,
- understand system boundaries and dependencies,
- make changes with confidence,
- observe what the system is doing,
- understand what is deployed and where,
- and improve the project without introducing chaos.

## Category 1 — Documentation and Discoverability

### What it includes

- an accurate README,
- local setup instructions that actually work,
- contribution guidance,
- architecture notes,
- domain concepts and glossary,
- runbooks for common tasks,
- deployment or release notes,
- change history where useful.

### What good looks like

- The docs are current enough to trust.
- A new engineer can find the path from clone to running system.
- The most common tasks are documented.
- The docs reduce dependency on tribal knowledge.

### Debt signals

- README lies.
- setup steps are missing or outdated,
- docs explain the happy path but not reality,
- operational knowledge lives only in chat or in people’s heads,
- architecture diagrams exist but do not match the code.

### Why it matters

Missing or inaccurate docs slow down every change because engineers must re-discover the system repeatedly.

### How AI can help

- summarize repo structure,
- draft or refresh READMEs,
- identify undocumented scripts and commands,
- compare docs to actual workflows,
- generate glossary or onboarding material.

### Where AI can go wrong

- inventing architecture,
- generating overly generic documentation,
- obscuring uncertainty instead of flagging it,
- making documentation sound polished while remaining inaccurate.

## Category 2 — Architecture Clarity and Boundaries

### What it includes

- clear system context,
- understandable module boundaries,
- known responsibilities,
- documented integration points,
- dependency direction that makes sense,
- diagrams that help engineers navigate the system.

### What good looks like

- The team can explain major components and why they exist.
- Responsibilities are reasonably separated.
- Cross-cutting concerns are visible.
- Engineers can tell where to make a change and where not to.

### Debt signals

- “Everything touches everything.”
- hard-to-follow control flow,
- implicit coupling,
- duplicated business logic across layers,
- no diagrams or wildly misleading diagrams,
- modules with unclear ownership or purpose.

### Why it matters

Architecture confusion increases the cost and risk of every change. Teams make slower, more defensive edits because they do not trust the impact surface.

### How AI can help

- generate first-pass component maps,
- trace dependencies and usage,
- summarize module responsibilities,
- identify duplication or suspicious coupling,
- propose candidate seams for refactoring.

### Where AI can go wrong

- overstating confidence in inferred architecture,
- recommending large refactors without enough context,
- collapsing domain nuance into simplistic abstractions.

## Category 3 — Reproducible Developer Setup

### What it includes

- clean setup instructions,
- versioned toolchain assumptions,
- bootstrap scripts,
- dev containers or equivalent reproducible environment,
- minimal hidden machine-specific steps,
- fast path from clone to development.

### What good looks like

- A new machine can reach a working state with bounded effort.
- Required versions and dependencies are explicit.
- Environment drift is limited.
- “Works on my machine” is the exception, not the norm.

### Debt signals

- snowflake laptops,
- hidden global dependencies,
- setup requires oral tradition,
- unclear environment variables,
- no devcontainer, lockfiles, or documented toolchain,
- onboarding measured in days of debugging.

### Why it matters

If the development environment is unreliable, AI tools cannot help much. They will generate commands, patches, or tests against a moving target.

### How AI can help

- extract implicit setup assumptions,
- draft setup scripts,
- create environment checklists,
- propose devcontainer or Docker-based development approaches,
- identify missing version constraints.

### Where AI can go wrong

- generating setup instructions that sound standard but do not match the repo,
- choosing tools that are inappropriate for the stack,
- ignoring platform-specific issues.

## Category 4 — Testability and Quality Confidence

### What it includes

- a balanced test strategy,
- meaningful unit/integration/end-to-end coverage,
- isolated tests where useful,
- realistic data and fixtures,
- confidence signals that correlate with real risk,
- fast enough feedback loops.

### What good looks like

- Tests help the team move faster, not slower.
- Failing tests are actionable.
- Test data is manageable and trustworthy.
- Quality measures reflect risk better than vanity.
- Engineers know what they can safely change.

### Debt signals

- high coverage, low confidence,
- brittle end-to-end tests,
- no clear testing strategy,
- missing mocks or over-mocking,
- test data chaos,
- long-running pipelines that nobody trusts.

### Why it matters

Confidence is what allows refactoring. Without it, teams avoid improvements because they fear hidden regressions.

### How AI can help

- suggest test cases from code paths,
- identify untested behaviors,
- generate initial test scaffolds,
- propose fixture cleanup,
- explain failing tests,
- map code changes to likely regression risk.

### Where AI can go wrong

- generating shallow tests that verify implementation detail,
- inflating coverage without improving confidence,
- producing flaky tests,
- missing the difference between business behavior and code mechanics.

## Category 5 — Buildability, Deployability, and Release Discipline

### What it includes

- local buildability,
- CI pipelines,
- consistent packaging,
- environment-specific configuration discipline,
- semantic versioning or explicit release conventions,
- visibility into what is deployed and where.

### What good looks like

- The team can build the software reliably.
- A change has a clear path from branch to environment.
- Versions mean something.
- Deployed artifacts are identifiable.
- Verification is possible after deployment.

### Debt signals

- manual mystery steps,
- builds that only one person understands,
- unclear artifact provenance,
- version numbers that communicate nothing,
- environments running unknown code,
- release notes as an afterthought.

### Why it matters

If release discipline is weak, cleanup work does not stick. Teams cannot tell whether improvements are actually in use.

### How AI can help

- summarize CI workflows,
- identify fragile pipeline steps,
- suggest release checklists,
- draft changelogs and release notes,
- standardize versioning conventions,
- propose post-deploy verification steps.

### Where AI can go wrong

- over-automating before basics are understood,
- recommending process complexity without payoff,
- generating release artifacts that misrepresent actual changes.

## Category 6 — Data, Schema, and Environment Discipline

### What it includes

- database migration strategy,
- versioned schema changes,
- seed data or fixtures,
- test data snapshotting where appropriate,
- safe rollback thinking,
- environment parity where practical.

### What good looks like

- Schema changes are reviewable and repeatable.
- Data setup is not magical.
- Engineers can stand up useful test conditions.
- Database change history is visible.

### Debt signals

- hand-applied database changes,
- mystery data dependencies,
- broken local data bootstrapping,
- irreversible changes with no discipline,
- QA environments that drift too far from known state.

### Why it matters

Data problems are a major hidden source of technical debt because they break reproducibility and make testing untrustworthy.

### How AI can help

- identify schema/version mismatches,
- explain migration scripts,
- propose seed data organization,
- generate migration review checklists,
- document environment assumptions.

### Where AI can go wrong

- unsafe migration suggestions,
- misunderstanding data semantics,
- proposing synthetic data that destroys test relevance.

## Category 7 — Observability and Operational Insight

### What it includes

- logs with enough structure to be useful,
- traceability across service boundaries,
- metrics that reflect behavior and health,
- release and deployment visibility,
- enough context to debug production behavior,
- operational runbooks and verification paths.

### What good looks like

- The team can answer: what happened, where, when, and why.
- Logs support diagnosis, not guesswork.
- Traces connect the request path.
- Metrics reveal behavior trends and failure patterns.
- Teams can verify what version is live and whether it is behaving correctly.

### Debt signals

- logs without correlation IDs or request context,
- no tracing across services,
- dashboards that are vanity-only,
- production debugging by intuition,
- no quick way to verify deployment health,
- incidents that become archaeology projects.

### Why it matters

Observability is part of maintainability. A system that cannot be understood in operation is hard to change safely.

### How AI can help

- propose logging gaps,
- interpret logs or traces,
- draft operational runbooks,
- identify missing telemetry around critical workflows,
- summarize incidents and recurring patterns.

### Where AI can go wrong

- producing dashboards with weak signal,
- normalizing noisy telemetry instead of reducing it,
- hallucinating root causes from incomplete logs.

## Category 8 — Security, Secrets, and Supply Chain Hygiene

### What it includes

- secret management,
- dependency scanning,
- code scanning,
- basic secure defaults,
- reviewable credential usage,
- artifact and dependency integrity thinking.

### What good looks like

- Secrets are not living in repos and docs casually.
- Vulnerable dependencies are visible.
- Basic scanning is automated.
- The team knows which controls are baseline versus advanced.

### Debt signals

- hardcoded secrets,
- unmanaged service credentials,
- dependencies updated blindly or not at all,
- no vulnerability review path,
- “security later” as normal workflow.

### Why it matters

Security debt compounds quietly and often surfaces at the worst time. AI can help reduce it, but it can also introduce it.

### How AI can help

- identify risky secret usage patterns,
- summarize dependency and code scanning findings,
- draft remediation plans,
- propose safer defaults,
- standardize security review checklists.

### Where AI can go wrong

- suggesting insecure code,
- normalizing insecure patterns it has seen in public repos,
- treating security scanning as optional polish.

## Category 9 — Workflow and Collaboration Discipline

### What it includes

- pull request quality,
- code review discipline,
- commit hygiene,
- issue-to-change traceability,
- team conventions,
- visible ownership and maintenance paths.

### What good looks like

- Changes are understandable and reviewable.
- Small improvements can land consistently.
- Team conventions reduce friction.
- AI usage is reviewed like any other engineering output.

### Debt signals

- huge unreviewable PRs,
- unclear change history,
- no conventions for code review,
- cleanup work constantly deferred,
- AI-produced diffs treated as inherently correct.

### Why it matters

Without workflow discipline, technical debt cleanup becomes a one-time event instead of an ongoing capability.

### How AI can help

- draft clearer PR summaries,
- standardize review templates,
- classify debt items,
- suggest issue decomposition,
- generate checklists and migration plans.

### Where AI can go wrong

- producing too much change at once,
- making poor code review habits look productive,
- hiding weak reasoning behind fluent summaries.

## The top 12 “what good looks like” checks

Use these in class as a compact scoreboard:

1. The README is trustworthy.
2. Architecture is understandable at a glance.
3. Local setup is reproducible.
4. The project can be built in a clean environment.
5. Tests provide real confidence.
6. Schema changes are versioned and reviewable.
7. Test data is intentional, not accidental.
8. Versions and releases are visible.
9. Deployments can be verified.
10. Logs, metrics, and traces help explain behavior.
11. Secrets and dependency risk are managed deliberately.
12. Team workflow supports small, repeatable improvements.

## Important nuance to teach

- “Run the full system locally” is not always realistic. Teach **meaningful local or isolated testability** instead of insisting on perfect local parity in all cases.
- “High test coverage” is not the same as confidence. Teach **risk-relevant testing**.
- “No passwords” is too vague. Teach **secrets management and secure default handling**.
- “Observability” is not just logs. Teach **logs + traces + metrics + deployment visibility + debugging usefulness**.
