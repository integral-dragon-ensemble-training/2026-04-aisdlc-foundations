# Technical Debt Reference

A working reference for the nine categories of technical debt used throughout the week. Use it during the exercises, and keep it afterward to classify the friction you see in your own codebases.

## A working definition

> Technical debt is any deficiency in the software system or its delivery environment that increases the cost, risk, or time required to make future changes.

Debt is broader than messy code. It lives in documentation, architecture, environment, testing, release, data, observability, security, and workflow.

## The nine categories

### 1. Knowledge debt

Missing or misleading understanding.

Examples: outdated docs, no architecture map, unclear ownership, hidden operational steps, inconsistent naming.

### 2. Design debt

Structure that makes change unnecessarily hard.

Examples: tangled dependencies, mixed responsibilities, duplicated logic, poor modularity, weak boundaries.

### 3. Environment debt

Drift or fragility in the developer and test environment.

Examples: snowflake machines, missing setup automation, dependency version chaos, local startup fragility.

### 4. Quality-confidence debt

Inability to know whether a change is safe.

Examples: missing tests, flaky tests, poor fixtures, meaningless coverage metrics, no regression confidence.

### 5. Release debt

Weaknesses in the build, versioning, packaging, and deployment path.

Examples: manual release steps, unknown deployed version, weak artifact traceability, inconsistent build outputs.

### 6. Data and schema debt

Deficiencies in how data structure and state are managed.

Examples: untracked schema changes, fragile migrations, impossible test-data setup, stateful environment surprises.

### 7. Observability debt

Inability to understand runtime behavior efficiently.

Examples: noisy logs, missing correlation, no traces, vanity dashboards, unclear deployment verification.

### 8. Security and supply-chain debt

Weaknesses that increase exposure or reduce trust in the software and its build chain.

Examples: hardcoded secrets, unreviewed dependencies, no code scanning, no dependency review, unclear provenance.

### 9. Workflow debt

Process choices that make healthy change harder than it should be.

Examples: huge PRs, weak review norms, no issue/change traceability, cleanup work never scheduled, AI changes not reviewed with the same rigor as human changes.

---

## How to think about "interest"

The financial metaphor is useful if you apply it carefully:

- The **debt** is the underlying deficiency.
- The **interest** is the repeated extra cost of every future change.

A few examples:

- Onboarding takes two extra days because setup is unreliable. That extra time is interest — paid on every new hire.
- A bug fix requires reading five unrelated modules because boundaries are unclear. That cognitive cost is interest — paid on every fix.
- Each deployment needs Slack archaeology and manual checks. That verification cost is interest — paid on every release.

The debt itself might cost a few days to fix. The interest is what you're already paying, over and over, until you do.

## When friction counts as serious debt

A problem is worth treating as technical debt when it does at least one of the following:

- slows routine change,
- increases the risk of regression,
- increases cognitive load,
- makes debugging materially harder,
- increases dependence on a few heroic individuals,
- or hides whether the system is actually healthy.

## Where AI has the highest leverage on debt

AI is strongest when the debt is:

- pattern-heavy,
- text-heavy,
- repetitive,
- cross-cutting,
- or diagnostic.

Practical examples:

- summarizing old scripts,
- finding duplicated logic,
- proposing logging improvements,
- drafting missing docs,
- generating first-pass tests,
- identifying undocumented configuration,
- turning recurring issues into cleanup epics.

## Where human judgment stays central

Humans still own:

- prioritization,
- tradeoffs,
- architectural direction,
- production risk judgment,
- security-sensitive changes,
- and the final decision on whether a generated change is actually safe or worthwhile.
