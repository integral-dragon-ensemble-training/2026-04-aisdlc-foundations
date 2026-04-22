# Project Health Reference

A working reference for the nine categories of project health used throughout the week. Use it during the exercises, and keep it afterward as a checklist you can apply to your own codebases.

## A healthy project is more than clean code

A project is healthy when a competent engineer can:

- understand what the system is for,
- find the relevant code and docs quickly,
- set up the environment without heroics,
- build and test meaningful changes,
- understand system boundaries and dependencies,
- make changes with confidence,
- observe what the system is doing in production,
- see what's deployed and where,
- and improve the project without introducing chaos.

Every category below maps to one of those capabilities.

---

## 1. Documentation and discoverability

**What it includes.** An accurate README, working setup instructions, contribution guidance, architecture notes, domain glossary, runbooks, release notes, change history.

**What good looks like.**

- The docs are current enough to trust.
- A new engineer can follow the path from clone to running system.
- The most common tasks are documented.
- The docs reduce dependence on tribal knowledge.

**Debt signals.** The README lies. Setup steps are missing or outdated. Docs describe the happy path but not reality. Operational knowledge lives only in chat or in people's heads. Architecture diagrams exist but don't match the code.

**Where AI helps.** Summarizing repo structure, drafting or refreshing READMEs, identifying undocumented scripts, comparing docs to actual workflows, generating glossaries and onboarding material.

**Where AI goes wrong.** Inventing architecture, producing generic-sounding documentation, obscuring uncertainty, making inaccurate docs sound polished.

---

## 2. Architecture clarity and boundaries

**What it includes.** Clear system context, understandable module boundaries, known responsibilities, documented integration points, sensible dependency direction, diagrams that help engineers navigate.

**What good looks like.**

- The team can explain major components and why they exist.
- Responsibilities are reasonably separated.
- Cross-cutting concerns are visible.
- Engineers can tell where to make a change — and where not to.

**Debt signals.** "Everything touches everything." Hard-to-follow control flow. Implicit coupling. Duplicated business logic across layers. No diagrams, or wildly misleading diagrams. Modules with unclear ownership or purpose.

**Where AI helps.** Generating first-pass component maps, tracing dependencies, summarizing module responsibilities, identifying duplication or suspicious coupling, proposing candidate seams for refactoring.

**Where AI goes wrong.** Overstating confidence in inferred architecture, recommending large refactors without enough context, collapsing domain nuance into simplistic abstractions.

---

## 3. Reproducible developer setup

**What it includes.** Clean setup instructions, versioned toolchain assumptions, bootstrap scripts, dev containers or equivalent, minimal hidden machine-specific steps, a fast path from clone to development.

**What good looks like.**

- A new machine reaches a working state with bounded effort.
- Required versions and dependencies are explicit.
- Environment drift is limited.
- "Works on my machine" is the exception, not the norm.

**Debt signals.** Snowflake laptops. Hidden global dependencies. Setup requires oral tradition. Unclear environment variables. No devcontainer, lockfiles, or documented toolchain. Onboarding measured in days of debugging.

**Where AI helps.** Extracting implicit setup assumptions, drafting setup scripts, creating environment checklists, proposing devcontainer or Docker-based development approaches, identifying missing version constraints.

**Where AI goes wrong.** Generating setup instructions that sound standard but don't match the repo, choosing tools inappropriate for the stack, ignoring platform-specific issues.

---

## 4. Testability and quality confidence

**What it includes.** A balanced test strategy, meaningful unit/integration/end-to-end coverage, isolated tests where useful, realistic data and fixtures, confidence signals that correlate with real risk, feedback loops fast enough to use.

**What good looks like.**

- Tests help the team move faster, not slower.
- Failing tests are actionable.
- Test data is manageable and trustworthy.
- Quality measures reflect risk better than vanity.
- Engineers know what they can safely change.

**Debt signals.** High coverage, low confidence. Brittle end-to-end tests. No clear testing strategy. Missing mocks or over-mocking. Test data chaos. Long-running pipelines nobody trusts.

**Where AI helps.** Suggesting test cases from code paths, identifying untested behaviors, generating initial test scaffolds, proposing fixture cleanup, explaining failing tests, mapping code changes to likely regression risk.

**Where AI goes wrong.** Generating shallow tests that verify implementation detail, inflating coverage without improving confidence, producing flaky tests, missing the difference between business behavior and code mechanics.

---

## 5. Buildability, deployability, and release discipline

**What it includes.** Local buildability, CI pipelines, consistent packaging, environment-specific configuration discipline, semantic versioning or explicit release conventions, visibility into what's deployed and where.

**What good looks like.**

- The team can build the software reliably.
- A change has a clear path from branch to environment.
- Versions mean something.
- Deployed artifacts are identifiable.
- Verification is possible after deployment.

**Debt signals.** Manual mystery steps. Builds only one person understands. Unclear artifact provenance. Version numbers that communicate nothing. Environments running unknown code. Release notes as an afterthought.

**Where AI helps.** Summarizing CI workflows, identifying fragile pipeline steps, suggesting release checklists, drafting changelogs and release notes, standardizing versioning conventions, proposing post-deploy verification steps.

**Where AI goes wrong.** Over-automating before basics are understood, recommending process complexity without payoff, generating release artifacts that misrepresent actual changes.

---

## 6. Data, schema, and environment discipline

**What it includes.** A database migration strategy, versioned schema changes, seed data or fixtures, test data snapshotting where appropriate, safe rollback thinking, environment parity where practical.

**What good looks like.**

- Schema changes are reviewable and repeatable.
- Data setup is not magical.
- Engineers can stand up useful test conditions.
- Database change history is visible.

**Debt signals.** Hand-applied database changes. Mystery data dependencies. Broken local data bootstrapping. Irreversible changes without discipline. QA environments that drift too far from known state.

**Where AI helps.** Identifying schema/version mismatches, explaining migration scripts, proposing seed data organization, generating migration review checklists, documenting environment assumptions.

**Where AI goes wrong.** Unsafe migration suggestions, misunderstanding data semantics, proposing synthetic data that destroys test relevance.

---

## 7. Observability and operational insight

**What it includes.** Logs with enough structure to be useful, traceability across service boundaries, metrics that reflect behavior and health, release and deployment visibility, enough context to debug production behavior, operational runbooks and verification paths.

**What good looks like.**

- The team can answer: what happened, where, when, and why.
- Logs support diagnosis, not guesswork.
- Traces connect the request path.
- Metrics reveal behavior trends and failure patterns.
- Teams can verify which version is live and whether it's behaving correctly.

**Debt signals.** Logs without correlation IDs or request context. No tracing across services. Vanity-only dashboards. Production debugging by intuition. No quick way to verify deployment health. Incidents that become archaeology projects.

**Where AI helps.** Proposing logging gaps, interpreting logs or traces, drafting operational runbooks, identifying missing telemetry around critical workflows, summarizing incidents and recurring patterns.

**Where AI goes wrong.** Producing dashboards with weak signal, normalizing noisy telemetry instead of reducing it, hallucinating root causes from incomplete logs.

---

## 8. Security, secrets, and supply chain hygiene

**What it includes.** Secret management, dependency scanning, code scanning, secure defaults, reviewable credential usage, artifact and dependency integrity thinking.

**What good looks like.**

- Secrets are not living in repos and docs casually.
- Vulnerable dependencies are visible.
- Basic scanning is automated.
- The team knows which controls are baseline versus advanced.

**Debt signals.** Hardcoded secrets. Unmanaged service credentials. Dependencies updated blindly or not at all. No vulnerability review path. "Security later" as normal workflow.

**Where AI helps.** Identifying risky secret usage patterns, summarizing dependency and code scanning findings, drafting remediation plans, proposing safer defaults, standardizing security review checklists.

**Where AI goes wrong.** Suggesting insecure code, normalizing insecure patterns from public repos, treating security scanning as optional polish.

---

## 9. Workflow and collaboration discipline

**What it includes.** Pull request quality, code review discipline, commit hygiene, issue-to-change traceability, team conventions, visible ownership and maintenance paths.

**What good looks like.**

- Changes are understandable and reviewable.
- Small improvements can land consistently.
- Team conventions reduce friction.
- AI usage is reviewed like any other engineering output.

**Debt signals.** Huge unreviewable PRs. Unclear change history. No conventions for code review. Cleanup work constantly deferred. AI-produced diffs treated as inherently correct.

**Where AI helps.** Drafting clearer PR summaries, standardizing review templates, classifying debt items, suggesting issue decomposition, generating checklists and migration plans.

**Where AI goes wrong.** Producing too much change at once, making poor code review habits look productive, hiding weak reasoning behind fluent summaries.

---

## The twelve-point scoreboard

A compact version of the above. Use it to score any repository in five minutes.

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

---

## Nuances worth keeping in mind

- "Run the full system locally" isn't always realistic. Aim for **meaningful local or isolated testability** rather than perfect local parity.
- "High test coverage" is not the same as confidence. Aim for **risk-relevant testing**.
- "No passwords in the repo" is too vague. Aim for **managed secrets and secure defaults**.
- "Observability" is not just logs. Aim for **logs + traces + metrics + deployment visibility + debugging usefulness**.
