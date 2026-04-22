ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/03-slides/01-day-1-what-good-looks-like.md

# Day 1 Slide Deck — What Good Looks Like

## Slide 1 — Why This Course Starts With “What Good Looks Like”

**Core message:** Students need a quality target before they can discuss debt or use AI responsibly.

**Bullets**
- If you cannot define healthy project qualities, AI will optimize the wrong thing.
- More code is not automatically progress.
- A good project is easier to understand, change, test, debug, and operate.

**Suggested visual**
- Simple contrast diagram: 'More code faster' vs 'Better changeability and confidence'

**Speaker notes**
Drive home that this course is about quality criteria and engineering leverage.

---

## Slide 2 — A Healthy Software Project Has More Than Clean Code

**Core message:** Project health spans docs, architecture, setup, testing, release, observability, security, and workflow.

**Bullets**
- Clean code is only one slice.
- Docs, environment setup, release process, and operational visibility are part of software quality.
- Teams suffer when these are weak even if the code style looks decent.

**Suggested visual**
- Wheel or radar chart with nine health categories

**Speaker notes**
This is the moment to broaden their mental model beyond code aesthetics.

---

## Slide 3 — Documentation and Discoverability

**Core message:** A repo should tell the next engineer how to understand, run, and change it.

**Bullets**
- Trustworthy README and setup docs
- Contribution guidance and glossary where needed
- Architecture notes and runbooks
- Reduced dependence on tribal knowledge

**Suggested visual**
- Screenshot idea: strong README or checklist of expected doc sections

**Speaker notes**
Emphasize that inaccurate documentation is not neutral; it actively creates debt.

---

## Slide 4 — Architecture Clarity and Reproducible Setup

**Core message:** If boundaries are unclear and setup is fragile, change becomes slow and risky.

**Bullets**
- Clear responsibilities and dependency direction
- Useful architecture diagrams
- Versioned toolchain assumptions
- Bootstrap scripts or devcontainer-based setup

**Suggested visual**
- Two-column visual: architecture map + reproducible setup pipeline

**Speaker notes**
This is where you can introduce C4 and devcontainers as examples of lightweight structure.

---

## Slide 5 — Testability, Quality Confidence, and Meaningful Local or Isolated Testability

**Core message:** Students should think in terms of confidence, not vanity metrics.

**Bullets**
- Coverage is not the same as confidence
- Fast, meaningful tests beat broad but brittle test suites
- Not every system can run fully local, but every system should have meaningful local or isolated validation paths
- Fixtures and test data quality matter

**Suggested visual**
- Triangle or layered test visualization with a confidence meter

**Speaker notes**
Call out the difference between 'all green' and 'I actually trust this change.'

---

## Slide 6 — Observability, Release Visibility, and Operability

**Core message:** A healthy system can explain what it is doing in production and what version is live.

**Bullets**
- Structured logs with enough context
- Metrics that reflect behavior, not just uptime
- Tracing across boundaries when the system is distributed
- Ability to verify deployments and versions quickly

**Suggested visual**
- Flow of request → logs, metrics, traces → deployment verification

**Speaker notes**
Observability is part of maintainability. If you cannot see the system, you cannot change it safely.

---

## Slide 7 — Day 1 Exercise: Score a Repository Against “What Good Looks Like”

**Core message:** The first exercise should make the framework concrete.

**Bullets**
- Use the repository health scorecard
- Assess docs, boundaries, setup, tests, release discipline, observability, security, and workflow
- Pick the three biggest weaknesses
- Discuss which weaknesses most increase change cost

**Suggested visual**
- Simple scorecard table with 1–5 scores by category

**Speaker notes**
End the session with a practical, inspectable artifact rather than abstract agreement.
