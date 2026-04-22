ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 01-course-architecture.md

# Course Architecture

## Course thesis

The course teaches a disciplined way to use Claude Code CLI to improve software changeability.

The core message is not:
- “AI writes code faster.”

The core message is:
- “AI-assisted engineering helps teams expose and remove the technical debt that makes change slow, risky, and expensive.”

## Why this is a better teaching frame

Most enterprise teams do not need more speculative feature generation.
They need:
- faster repo understanding
- more reliable setup
- stronger tests
- better operational visibility
- safer release practices
- a way to improve brownfield systems without destabilizing them

Claude Code CLI is strong when it is used as:
- a repo analyst
- a documentation drafter
- a test and refactor assistant
- a codebase reconnaissance tool
- a gap finder
- a change planner
- a verification helper

It is weak when it is used as:
- a substitute for architecture judgment
- a reason to skip validation
- a broad uncontrolled refactoring engine
- a generator of large unreviewed changes

## Recommended five-pillar taxonomy

### 1. Architecture clarity

**Question:** Can engineers understand the system well enough to change it safely?

Includes:
- useful documentation
- current diagrams
- service boundaries
- dependency visibility
- decisions captured in ADRs or equivalent notes
- identifiable entry points and data flows

### 2. Reproducibility

**Question:** Can engineers reliably build and run the software from a fresh environment?

Includes:
- local setup
- dependency bootstrap
- deterministic scripts
- build commands
- local environment variables and secrets handling
- consistent local/dev/test workflows

### 3. Testability

**Question:** Can engineers verify changes quickly and with confidence?

Includes:
- unit tests
- integration tests
- e2e tests where warranted
- seam creation for dependency isolation
- test data discipline
- migration discipline
- coverage and risk-based quality signals

### 4. Observability

**Question:** Can engineers see what the system is doing and diagnose behavior?

Includes:
- logs
- metrics
- traces
- health checks
- version visibility
- deploy verification
- correlation across components

### 5. Safe change

**Question:** Can the team ship improvements in small, reviewable, rollback-friendly steps?

Includes:
- linting and static analysis
- security scanning
- secret handling
- semantic versioning or other release identification
- CI quality gates
- reviewer checklists
- deployment verification
- incremental rollout and rollback patterns

## Why this sequence works

The sequence moves from understanding to execution:

1. If the architecture is unclear, the wrong things get changed.
2. If the environment is not reproducible, improvement work is hard to verify.
3. If tests are weak, every change feels risky.
4. If observability is weak, production behavior is opaque.
5. If release practices are weak, teams keep paying the same debt again and again.

## Role of Claude Code CLI across the sequence

| Pillar | Best Claude Code CLI uses |
|---|---|
| Architecture clarity | architecture mapping, repo summaries, dependency tracing, README repair, ADR drafts |
| Reproducibility | setup audits, script drafting, build/run validation planning, env var inventories |
| Testability | test gap identification, test scaffolding, fixture suggestions, refactor seam discovery |
| Observability | logging gap analysis, trace correlation suggestions, version endpoint proposals |
| Safe change | security review prompts, lint cleanup, small change planning, PR descriptions, rollout checklists |

## Instructor stance

Teach students to treat Claude Code CLI as:
- fast
- useful
- sometimes insightful
- never self-justifying

The workflow should always be:
1. inspect
2. hypothesize
3. change small
4. verify
5. review
6. document
