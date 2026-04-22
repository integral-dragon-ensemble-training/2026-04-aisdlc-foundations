ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 04-slides-day-2.md

# Day 2 Slides — Architecture Clarity and Reproducibility

## Slide 1 — Day 2 opening

**Title:** Can a new engineer understand, build, and run this system?

**Speaker notes**
- This is one of the strongest litmus tests for engineering quality.

---

## Slide 2 — Architecture clarity is an engineering capability

**Key points**
- people need more than source files
- they need boundaries, flow, dependencies, and decisions
- diagrams are useful only if they reflect reality
- ADRs and README sections are small but high-leverage artifacts

**Speaker notes**
- Architecture clarity is not architecture theater.

---

## Slide 3 — Common architecture clarity failure smells

**Key points**
- unclear entry points
- hidden service dependencies
- confusing project naming
- stale diagrams
- no explanation of runtime flow
- no record of key decisions

---

## Slide 4 — Claude Code CLI demo: architecture reconnaissance

**Demo prompt**
```text
Analyze this .NET solution and produce a first-pass architecture map.
Identify projects, likely responsibilities, runtime dependencies, test projects, and unclear areas.
Do not modify code.
```

**Speaker notes**
- Show students how to ask for a map, not a rewrite.
- Ask Claude to state what evidence it used.

---

## Slide 5 — Reproducibility as a debt-reduction multiplier

**Key points**
- if local setup is fragile, every improvement costs more
- reproducibility shortens onboarding
- reproducibility reduces hidden tribal knowledge
- reproducibility makes Claude-assisted changes more verifiable

---

## Slide 6 — Common reproducibility failure smells

**Key points**
- README lies
- undocumented environment variables
- local setup depends on one expert
- missing seed data
- inconsistent scripts across dev machines
- build/test/run paths diverge by environment

---

## Slide 7 — Azure/.NET/Python examples

**Key points**
- .NET: solution build paths, test projects, appsettings, secrets, versioning, service defaults
- Python: virtualenv/poetry/pip gaps, entry points, env files, pytest setup
- Azure context: local-to-cloud assumptions, managed identity, config, azd or repeatable provisioning

**Speaker notes**
- Ground abstract ideas in familiar technology.

---

## Slide 8 — Claude Code CLI demo: README vs reality

**Demo prompt**
```text
Compare the README and setup docs to the actual repository structure and scripts.
Identify inaccuracies, omissions, and ambiguous steps for a new engineer.
Draft a corrected README outline.
Do not update files until I approve the outline.
```

---

## Slide 9 — What to change first

**Key points**
- fix the smallest high-friction setup blocker
- document the real build/run path
- expose hidden assumptions
- create a reliable “minimum viable local run” path before chasing a perfect full-local stack

**Speaker notes**
- This is an anti-perfection slide.

---

## Slide 10 — Human review checkpoints

**Key points**
- exact prerequisites
- secrets and identity requirements
- infra dependencies that cannot be reproduced locally
- whether docs overpromise what can be run locally

---

## Slide 11 — Exercise instructions

**Exercise**
- create a first-pass architecture map
- identify README/setup drift
- propose the smallest setup improvement
- explain how you would verify it

---

## Slide 12 — Bridge to day 3

Tomorrow we shift from “can we run it?” to “can we trust changes to it?”
