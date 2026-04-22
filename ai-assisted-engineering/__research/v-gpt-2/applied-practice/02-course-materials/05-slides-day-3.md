ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 05-slides-day-3.md

# Day 3 Slides — Testability and Data Discipline

## Slide 1 — Day 3 opening

**Title:** Can we make a change and know whether it worked?

---

## Slide 2 — Testing is confidence infrastructure

**Key points**
- tests are not just coverage numbers
- they reduce fear and shorten review loops
- weak testability is often a design problem before it is a test-writing problem

**Speaker notes**
- Make the distinction between “more tests” and “better feedback.”

---

## Slide 3 — Testability smells

**Key points**
- hidden dependencies
- hard-coded time, network, or data access
- giant methods
- no seam for isolation
- flaky integration setup
- tests that assert implementation trivia instead of behavior

---

## Slide 4 — Claude Code CLI demo: testability gap analysis

**Demo prompt**
```text
Review this module for testability.
Tell me what makes it hard to test, what the smallest seam-creating changes would be, and what tests would provide the highest confidence first.
Do not modify code yet.
```

---

## Slide 5 — The staged testing model

**Key points**
- unit tests for focused behavior
- integration tests for real wiring
- e2e tests for critical workflows only
- the goal is confidence per dollar and per minute, not maximal test count

---

## Slide 6 — Data and migration discipline

**Key points**
- schema changes must be traceable
- local and test data must be repeatable enough to support learning and verification
- migration discipline affects developer speed and production safety

---

## Slide 7 — Common data discipline smells

**Key points**
- manual database drift
- no reset path
- shared mutable test data
- schema changes with unclear ownership
- local test setup that depends on unstated data conditions

---

## Slide 8 — Claude Code CLI demo: migration and test-data review

**Demo prompt**
```text
Inspect this repository for migration and test-data discipline.
Identify schema change patterns, reset/reseed strategies, and risks to repeatable testing.
Then suggest the smallest useful improvements.
```

---

## Slide 9 — .NET and Python examples

**Key points**
- .NET: xUnit/NUnit/MSTest, test project structure, dependency injection seams, EF Core migrations
- Python: pytest fixtures, dependency overrides, test app factories, migration tooling by framework
- both: prefer repeatable, narrow feedback loops

---

## Slide 10 — Human review checkpoints

**Key points**
- whether generated tests protect real business behavior
- whether proposed seams distort the design
- whether migration changes are safe in shared environments
- whether the validation path is realistic

---

## Slide 11 — Exercise instructions

**Exercise**
- choose a module
- diagnose testability
- propose smallest seam-creating change
- identify one high-value test and one risky test
- assess data/migration discipline

---

## Slide 12 — Bridge to day 4

Tomorrow: even if changes pass locally, can we see what the system is doing once it runs?
