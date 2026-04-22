ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 06-slides-day-4.md

# Day 4 Slides — Observability and Release Visibility

## Slide 1 — Day 4 opening

**Title:** Can we see the system, and can we verify what is deployed?

---

## Slide 2 — Observability is operational confidence

**Key points**
- logs are necessary but not sufficient
- metrics help detect patterns
- traces help follow work across boundaries
- health and version information reduce ambiguity after deploys

---

## Slide 3 — Common observability failure smells

**Key points**
- logs without structure
- no correlation IDs or trace continuity
- no health checks
- no version/build exposure
- impossible to answer “what changed?”
- dashboards that show activity but not diagnosis

---

## Slide 4 — Azure/.NET observability context

**Key points**
- OpenTelemetry is a useful common model
- Application Insights and Azure Monitor are natural enterprise endpoints
- .NET Aspire and related tooling can simplify some observability baselines
- serverless and distributed systems still need correlation and verification discipline

**Speaker notes**
- Stay principle-first, not product-pitchy.

---

## Slide 5 — Claude Code CLI demo: observability gap hunt

**Demo prompt**
```text
Inspect this service for observability quality.
Identify logging gaps, missing correlation or tracing clues, health-check presence, and version/build visibility.
Then propose one small and one medium observability improvement.
```

---

## Slide 6 — Release visibility matters

**Key points**
- engineers need to know what is deployed
- QA verification should not feel like archaeology
- version endpoints, build metadata, and health surfaces reduce uncertainty

---

## Slide 7 — Common release verification smells

**Key points**
- no status endpoint
- no build/version metadata
- no post-deploy verification checklist
- no obvious way to confirm that a deploy actually changed runtime behavior

---

## Slide 8 — Claude Code CLI demo: deploy verification

**Demo prompt**
```text
Assess this project for version and deployment verification.
Can an engineer tell what build is running, whether a specific deploy took effect, and whether the service is healthy?
Suggest the smallest useful improvements.
```

---

## Slide 9 — Human review checkpoints

**Key points**
- data sensitivity in logs
- telemetry cost and noise
- realistic correlation boundaries
- platform constraints and hosting model
- whether observability changes fit operational ownership

---

## Slide 10 — Exercise instructions

**Exercise**
- inspect one service
- identify observability and version-visibility gaps
- propose the smallest safe improvement
- define how you would verify success

---

## Slide 11 — Debrief theme

**Key point**
A system is not truly changeable if it becomes opaque after deployment.

---

## Slide 12 — Bridge to day 5

Tomorrow we convert these ideas into a safe, repeatable operating model for AI-assisted engineering.
