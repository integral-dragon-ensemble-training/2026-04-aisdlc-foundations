# Technical Debt Taxonomy for the Course

## Definition to use in class

Technical debt is any deficiency in the software system or its delivery environment that increases the cost, risk, or time required to make future changes.

## The most useful taxonomy for this course

### 1. Knowledge debt

Missing or misleading understanding.

Examples:
- outdated docs,
- no architecture map,
- unclear ownership,
- hidden operational steps,
- inconsistent naming.

### 2. Design debt

Structure that makes change unnecessarily hard.

Examples:
- tangled dependencies,
- mixed responsibilities,
- duplicated logic,
- poor modularity,
- weak boundaries.

### 3. Environment debt

Drift or fragility in the developer and test environment.

Examples:
- snowflake machines,
- missing setup automation,
- dependency version chaos,
- local startup fragility.

### 4. Quality-confidence debt

Inability to know whether a change is safe.

Examples:
- missing tests,
- flaky tests,
- poor fixtures,
- meaningless coverage metrics,
- no regression confidence.

### 5. Release debt

Weaknesses in the build, versioning, packaging, and deployment path.

Examples:
- manual release steps,
- unknown deployed version,
- weak artifact traceability,
- inconsistent build outputs.

### 6. Data and schema debt

Deficiencies in how data structure and state are managed.

Examples:
- untracked schema changes,
- fragile migrations,
- impossible test-data setup,
- stateful environment surprises.

### 7. Observability debt

Inability to understand runtime behavior efficiently.

Examples:
- noisy logs,
- missing correlation,
- no traces,
- vanity dashboards,
- unclear deployment verification.

### 8. Security and supply-chain debt

Weaknesses that increase exposure or reduce trust in the software and build chain.

Examples:
- hardcoded secrets,
- unreviewed dependencies,
- no code scanning,
- no dependency review,
- unclear provenance.

### 9. Workflow debt

Process choices that make healthy change harder than it should be.

Examples:
- huge PRs,
- weak review norms,
- no issue/change traceability,
- cleanup work never scheduled,
- AI changes not reviewed with the same rigor as human changes.

## How to explain “interest”

Use the financial metaphor carefully:

- The debt is the underlying deficiency.
- The interest is the repeated extra cost of future changes.

Example:
- If onboarding takes 2 extra days because the setup is unreliable, that extra time is interest.
- If every bug fix requires reading five unrelated modules because boundaries are unclear, that is interest.
- If deployments require Slack archaeology and manual checks, that is interest.

## A useful classroom rule

A problem counts as serious technical debt when it does at least one of these:

- slows routine change,
- increases risk of regression,
- increases cognitive load,
- makes debugging materially harder,
- increases dependence on heroic individuals,
- or hides whether the system is actually healthy.

## Where AI has the highest leverage

AI is strongest when the debt is:

- pattern-heavy,
- text-heavy,
- repetitive,
- cross-cutting,
- or diagnostic.

Examples:
- summarizing old scripts,
- finding duplicated logic,
- proposing logging improvements,
- drafting missing docs,
- generating first-pass tests,
- identifying undocumented configuration,
- turning issue patterns into cleanup epics.

## Where human judgment stays central

Humans still need to own:

- prioritization,
- tradeoffs,
- architectural direction,
- production risk judgment,
- security-sensitive changes,
- and the final decision on whether a generated change is actually safe or worthwhile.
