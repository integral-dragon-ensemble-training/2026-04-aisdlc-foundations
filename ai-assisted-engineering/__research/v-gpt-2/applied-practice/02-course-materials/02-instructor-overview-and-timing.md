ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 02-instructor-overview-and-timing.md

# Instructor Overview and Timing

## Daily format template

Use this cadence to keep the hour tight:

- 0:00–0:08 — framing / review / why today matters
- 0:08–0:20 — concept teaching
- 0:20–0:35 — instructor demo with Claude Code CLI
- 0:35–0:50 — student exercise
- 0:50–0:58 — debrief
- 0:58–1:00 — preview next day

## Recommended daily plan

### Day 1 — What good looks like
- lesson 1: changeability as the real quality target
- lesson 2: repo health scorecard and debt prioritization

### Day 2 — Architecture clarity and reproducibility
- lesson 3: architecture reconnaissance
- lesson 4: build/run reproducibility

### Day 3 — Testability and data discipline
- lesson 5: tests as confidence infrastructure
- lesson 6: migration and test-data discipline

### Day 4 — Observability and release visibility
- lesson 7: logs, metrics, traces, and correlation
- lesson 8: version visibility and deploy verification

### Day 5 — Safe change and operating model
- lesson 9: guardrails for secure, reviewable change
- lesson 10: capstone and repeatable AI-assisted engineering practice

## If time is tight, cut in this order

1. deep tool detail before students understand the problem
2. advanced e2e testing discussion
3. deeper preview or automation features of Claude Code CLI
4. extended debate about perfect architecture
5. large platform-specific digressions

Do not cut:
- the core organizing theme
- the scorecard
- the debt prioritization lens
- the observation that AI must be validated
- the capstone framing

## Azure/.NET/Python bias guidance

### Use .NET first when teaching:
- solution structure
- services and APIs
- test projects
- OpenTelemetry instrumentation
- Application Insights integration
- version exposure
- build and publish paths

### Use Python when teaching:
- automation scripts
- lightweight service examples
- test patterns with pytest
- utility tooling
- data or agent-support workflows

### Use Azure context for:
- deployment verification
- configuration handling
- managed identity and secrets posture
- Application Insights / Azure Monitor
- Azure Functions
- Azure Developer CLI or repeatable provisioning/deploy flow

## Suggested training repo shape

If you create or curate a training repo, include:
- one .NET service
- one optional Python utility or sidecar
- intentionally stale README sections
- missing or partial tests
- at least one configuration smell
- at least one observability gap
- at least one release/version visibility gap
- a small amount of technical debt that is safe for students to inspect and discuss
