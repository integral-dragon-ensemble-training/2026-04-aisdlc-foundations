# AI Accelerated Software Development

## Applied Practice

Guided artifact delivery using AI-assisted workflows in sandbox and approved enterprise repositories.

## Program Snapshot

- Phase: `2 of 3`
- Duration: `4 weeks`
- Expected cadence: `8-10 hours per week`
- Format: guided applied work, artifact submission, cohort review, and coach-supported execution
- Core workstreams: `4`

## Program Overview

Applied Practice is the bridge between Foundations and real-project coaching. Participants stop working only at the concept level and begin producing reviewable engineering artifacts inside controlled environments. The goal is not abstract exposure to AI tools. The goal is repeatable delivery under enterprise constraints.

This section assumes the learner already understands:

- agentic engineering posture
- bounded context and context rot
- plan mode and execution discipline
- least-privilege tool usage
- review and narration expectations

Applied Practice takes those foundations and turns them into concrete outputs:

- architecture documentation
- test suites and coverage deltas
- security and compliance artifacts
- observability instrumentation and runbooks

## Delivery Characteristics

### Enterprise-safe

- no unapproved external SaaS workflows
- no casual code upload patterns
- approved models and bounded execution only
- work happens inside sandbox or approved repos

### Real deliverables

- every week produces artifacts that can be reviewed
- outputs are judged on engineering quality, not prompt cleverness
- participants build a usable portfolio of process and code artifacts

### Production-oriented

- exercises mirror the conditions of enterprise software teams
- work emphasizes maintainability, reviewability, and operational readiness
- labs are replaced with applied work that resembles real team delivery

### Coach-supported

- coaching happens off-network or through approved review channels
- coaches guide method and quality without directly handling sensitive code
- participants remain responsible for execution inside their own environment

## Prerequisites

Completion of `AI Accelerated Software Development - Foundations` is required.

Foundations is the safety and operating-model gate for this section. Participants should already be able to:

- work in the Claude Code CLI confidently
- scope context intentionally
- produce reviewed plans before mutation
- treat AI output as untrusted until verified
- narrate changes with clear risk and testing notes

## Weekly Structure

Each week follows a consistent pattern:

- `2 hours` lecture or guidance content for the week’s applied focus
- `5-6 hours` applied work producing artifacts in sandbox or approved repos
- `1-2 hours` review, submission, cohort discussion, and feedback

## The Applied Workstreams

### Applied 01. Codebase Analysis and Documentation

Analyze a larger codebase safely and produce documentation that reduces onboarding friction and clarifies delivery risk. This workstream teaches participants how to inspect a repo read-only first, identify system boundaries, and create a risk-ranked backlog of safe improvements.

#### You'll learn

- safe repo inspection techniques with read-only first-pass discipline
- dependency and boundary mapping
- hotspot identification using churn, complexity, and low-test areas
- documentation that is actionable for new engineers rather than generic summary text

#### Deliverables

- architecture README covering purpose, runtime model, risks, and key boundaries
- `ADR v1` documenting one significant decision with trade-offs
- dependency and boundary map notes
- risk-ranked backlog with the top safe PR candidates
- one selected safe change with plan and acceptance criteria

#### Suggested timing

- Week: `3`
- Time: `4 hours`
- Mode: `read-only analysis first`

### Applied 02. Testing and Coverage Acceleration

Use AI where it improves confidence, not where it creates unmaintainable test debt. This workstream focuses on baseline measurement, high-ROI target selection, deterministic test generation, and readable test design that survives future maintenance.

#### You'll learn

- baseline coverage measurement and interpretation
- high-ROI target selection based on risk and change frequency
- human review loops for AI-generated tests
- coverage delta reporting that communicates value clearly

#### Deliverables

- coverage baseline before changes
- test plan defining what to test and why
- new tests with edge cases and readable naming
- coverage delta report after changes
- refactoring notes where testability required code improvements

#### Suggested timing

- Week: `4`
- Time: `4 hours`
- Focus: `unit tests preferred, deterministic patterns only`

### Applied 03. Security and Compliance

Turn the security posture from a policy idea into engineering behavior. This workstream focuses on prompt hygiene, redaction discipline, permissions reasoning, injection defense, and documentation that would stand up to security review or regulated delivery scrutiny.

#### You'll learn

- prompt redaction and safe-data handling patterns
- prompt injection attack and defense in practical workflows
- permission-boundary reasoning for agentic execution
- minimum viable compliance documentation for AI-assisted work
- how to convert abstract policy into reviewable execution controls

#### Deliverables

- prompt policy or working policy addendum for the chosen workflow
- redaction checklist tied to actual delivery scenarios
- prompt-review workflow showing who checks what before submission
- injection drill findings with concrete mitigations
- permissions and data-handling notes for the repo or workflow
- short compliance rationale explaining why the workflow is acceptable or what blocks it

#### Suggested timing

- Week: `5`
- Time: `4 hours`
- Focus: `security review discipline and compliance-ready evidence`

### Applied 04. Observability

Make the system operable after the code lands. This workstream focuses on structured logging, correlation propagation, operational troubleshooting, and the artifacts needed for engineers to understand behavior in production-like conditions.

#### You'll learn

- structured logging with defined fields and stable schemas
- correlation or trace ID propagation across requests and components
- minimum viable operational instrumentation
- runbook authoring for local run, failure triage, and log interpretation
- how observability reduces ambiguity during AI-assisted delivery and later debugging

#### Deliverables

- structured logging implementation or logging retrofit
- correlation ID propagation across the relevant request path
- log field reference or schema note
- operational runbook covering startup, normal flow, and failure diagnosis
- troubleshooting examples tied to actual log output
- observability gap note listing what still is not instrumented well enough

#### Suggested timing

- Week: `6`
- Time: `4 hours`
- Focus: `operational readiness and reconstructable system behavior`

## Week-by-Week Journey

### Week 3

`Applied 01: Codebase Analysis and Documentation`

- inspect a production-style repository safely
- produce architecture notes and an ADR
- create a safe-change backlog with explicit reasoning

### Week 4

`Applied 02: Testing and Coverage Acceleration`

- measure the baseline
- choose the highest-value test targets
- generate and review maintainable tests

### Week 5

`Applied 03: Security and Compliance`

- practice prompt redaction and workflow review
- run an injection-defense drill
- produce evidence that the workflow can be defended to security stakeholders

### Week 6

`Applied 04: Observability`

- add structured logging and correlation propagation
- produce an operational runbook
- make the delivered artifact easier to diagnose, support, and hand off

## What Participants Build

### Code artifacts

- targeted test suites
- structured logging improvements
- safe, bounded implementation changes where applicable
- low-risk PR candidates selected from real repo analysis

### Documentation

- architecture READMEs
- Architecture Decision Records
- runbooks
- dependency and boundary notes

### Process artifacts

- PR narrations
- plan-mode outputs with acceptance criteria
- coverage delta reports
- risk-ranked backlogs

### Security and compliance artifacts

- prompt policy notes
- redaction checklists
- injection drill findings
- permissions and data-handling notes
- workflow acceptability rationale

### Observability artifacts

- logging field definitions
- correlation propagation notes
- troubleshooting guides
- instrumentation gap assessments

## Assessment and Rubrics

Every deliverable should be evaluated against explicit quality standards.

### PR rubric

- clear statement of what changed
- clear explanation of why it changed
- risk assessment included
- testing approach documented
- follow-up items identified

### Tests rubric

- readable and well named
- deterministic and non-flaky
- edge cases included where appropriate
- maintainable structure
- meaningful confidence improvement shown

### Documentation rubric

- actionable for another engineer
- accurate to the current system state
- risks clearly identified
- run and build steps verified where relevant
- trade-offs explained rather than hidden

### Security rubric

- constraints and sensitive-data boundaries are explicit
- no unsafe prompt content is normalized
- mitigation steps are concrete and reviewable
- approvals and ownership are visible
- evidence is sufficient for later audit or security review

### Observability rubric

- logs are structured and purposeful
- correlation or trace identifiers are usable end-to-end
- runbook steps are practical
- troubleshooting guidance maps to actual signals
- remaining blind spots are acknowledged explicitly

## Exit State

By the end of Applied Practice, participants should be able to:

- inspect an enterprise codebase safely and extract usable understanding
- improve confidence through targeted testing rather than indiscriminate generation
- demonstrate secure and compliant AI-assisted workflow behavior
- make system behavior more observable and easier to support
- submit artifacts that are reviewable by engineering, security, and delivery stakeholders

## What Comes Next

After Applied Practice, the next phase should move into coached work on actual project delivery. The emphasis shifts from bounded training exercises to real repository outcomes, team-specific rollout decisions, and measurable operational impact.

Suggested framing for the next phase:

- `Embedded Project Coaching`, or
- `Applied Delivery on Real Repositories`

That avoids collapsing this section into generic labs while still distinguishing it from the fully coached real-project phase.
