ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 00-overview-approach-slides.md

# Overview Slide Deck — AI-SDLC Applied Practice

## Slide 1 — Title

**AI-SDLC Applied Practice**
Using Claude Code CLI to reduce technical debt and make software easier to change

**Speaker notes**
- Frame the course as engineering quality work, not AI spectacle.
- Emphasize brownfield systems, delivery friction, and operational confidence.
- State that Claude Code CLI is the main hands-on mechanism for the class.

---

## Slide 2 — Core organizing theme

**AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.**

**Speaker notes**
- This is the anchor statement for the whole week.
- The course is not primarily about generating net-new features.
- It is about increasing changeability: understanding, building, testing, observing, and shipping software safely.

---

## Slide 3 — Why this framing matters

- Many teams use AI mostly for feature scaffolding.
- That can add code faster than the team can safely absorb it.
- Brownfield systems are usually slowed by hidden friction:
  - unclear architecture
  - weak setup reproducibility
  - fragile tests
  - poor observability
  - unsafe or inconsistent release practices
- Claude Code CLI is especially valuable when used to expose and reduce those bottlenecks.

**Speaker notes**
- Faster code generation without stronger engineering foundations often creates more debt.
- The winning move is not just “more code faster,” but “more trustworthy change.”

---

## Slide 4 — What “good” looks like

A healthy software project tends to have:
- understandable architecture
- useful, current documentation
- reproducible local setup
- reliable build and run paths
- meaningful tests
- disciplined data and migrations
- logs, metrics, traces, and version visibility
- secrets handled safely
- CI and code review guardrails
- a predictable path from laptop to QA or production

**Speaker notes**
- These are engineering capabilities, not ideology.
- We will treat them as dimensions of changeability.

---

## Slide 5 — The five-pillar model

1. **Architecture clarity** — people can understand the system
2. **Reproducibility** — people can build and run the system
3. **Testability** — people can verify changes confidently
4. **Observability** — people can see behavior and diagnose issues
5. **Safe change** — people can ship and roll back with control

**Speaker notes**
- These pillars are cumulative.
- A team with observability but no reproducible setup still struggles.
- A team with tests but no release visibility still has confidence gaps.

---

## Slide 6 — Where Claude Code CLI fits

Claude Code CLI helps with:
- repo reconnaissance
- architecture summarization
- documentation repair
- script generation and cleanup
- test generation and gap finding
- tracing dependency chains
- identifying secrets and risky patterns
- proposing minimal change sets
- drafting rollout plans and PR descriptions

**Speaker notes**
- Claude is not the source of truth.
- It is a strong accelerator for analysis, drafting, and incremental implementation.
- The engineer remains responsible for judgment, validation, and trade-offs.

---

## Slide 7 — Why Azure, .NET, and Python matter here

- Many enterprise teams run heavily on Azure.
- .NET often sits in the core path for APIs, services, data, and line-of-business systems.
- Python is increasingly common for automation, integration, data work, and agentic workflows.
- The course should stay principle-first but use examples that feel native to the students’ environment.

**Speaker notes**
- .NET examples should dominate when showing service structure, tests, logging, telemetry, and deployment.
- Python examples should appear where scripting, APIs, utility services, or automation are useful.

---

## Slide 8 — The weekly narrative

- **Day 1:** Define what good looks like and how to score a repo
- **Day 2:** Make the architecture understandable and the setup reproducible
- **Day 3:** Strengthen testability, data discipline, and quality feedback
- **Day 4:** Add observability and release/version visibility
- **Day 5:** Turn all of this into a safe, repeatable operating model

**Speaker notes**
- Each day turns a vague complaint into an engineering capability.
- Students should leave with a sequence for real brownfield improvement.

---

## Slide 9 — Learning mode for the week

Students will repeatedly do four things:
1. inspect a real or representative codebase
2. use Claude Code CLI to analyze and propose improvements
3. review the output critically
4. convert findings into small, safe, prioritized work

**Speaker notes**
- This is deliberate practice, not passive theory.
- Repetition across different quality dimensions is a feature, not a flaw.

---

## Slide 10 — Capstone outcome

By the end of the week, students should be able to:
- assess a codebase against a changeability scorecard
- identify the highest-leverage technical debt blockers
- use Claude Code CLI to propose targeted improvements
- judge which changes are safe to automate and which require deeper human review
- present a realistic debt-paydown roadmap

**Speaker notes**
- The goal is not perfect architecture.
- The goal is better judgment, stronger review habits, and more trustworthy incremental change.
