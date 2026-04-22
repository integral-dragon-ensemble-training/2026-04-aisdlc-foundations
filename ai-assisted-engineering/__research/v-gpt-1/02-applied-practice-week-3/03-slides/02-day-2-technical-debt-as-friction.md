ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/03-slides/02-day-2-technical-debt-as-friction.md

# Day 2 Slide Deck — Technical Debt as Friction

## Slide 1 — Technical Debt Is Friction, Not Just Ugly Code

**Core message:** Teach debt as the repeated tax paid every time the system resists change.

**Bullets**
- Debt is any deficiency that increases the cost, risk, or time of future changes
- The 'interest' is the repeated extra effort teams keep paying
- Debt can live in code, docs, environment, data, release process, or operations

**Suggested visual**
- Metaphor visual: debt principal vs interest, but with engineering examples

**Speaker notes**
Avoid reducing the concept to style complaints or generic cleanup.

---

## Slide 2 — The Nine Debt Categories in This Course

**Core message:** Students should classify debt precisely so they can prioritize it.

**Bullets**
- Knowledge debt
- Design debt
- Environment debt
- Quality-confidence debt
- Release debt
- Data and schema debt
- Observability debt
- Security debt
- Workflow debt

**Suggested visual**
- Grid or matrix showing the nine categories

**Speaker notes**
Precise labeling helps move the conversation from venting to diagnosis.

---

## Slide 3 — How Teams Pay Interest

**Core message:** Show that friction compounds through repetition.

**Bullets**
- Slow onboarding due to unreliable setup
- Fearful changes because tests are weak
- Slack archaeology because docs are stale
- Production debugging because logs and traces are poor
- Release uncertainty because versions and deployments are unclear

**Suggested visual**
- Table: debt source → repeated interest paid

**Speaker notes**
This slide should feel painfully familiar to working engineers.

---

## Slide 4 — Prioritize Debt by Change Cost, Risk, and Frequency

**Core message:** Not all debt deserves the same attention.

**Bullets**
- High-frequency pain beats theoretically elegant cleanup
- Fix debt that blocks common changes first
- Favor improvements that unlock confidence and speed for the team
- Look for debt that affects multiple categories at once

**Suggested visual**
- 2x2 chart: impact on flow vs cost to fix

**Speaker notes**
Push students away from beautification projects and toward leverage.

---

## Slide 5 — Debt Examples: Local Setup, Test Data, and Observability

**Core message:** Concrete examples make the taxonomy real.

**Bullets**
- Environment debt: setup only works on one machine
- Data debt: no stable seed data or migration discipline
- Observability debt: no way to follow a request through the system
- These are often more expensive than a messy function

**Suggested visual**
- Three short case cards with a symptom, debt type, and likely consequence

**Speaker notes**
Use this slide to challenge the assumption that debt equals bad code formatting.

---

## Slide 6 — Where AI Helps on Day 2

**Core message:** AI is useful for classification, summarization, and prioritization.

**Bullets**
- Turn a repo tour into a debt inventory
- Group findings by category
- Draft a cleanup backlog
- Estimate which improvements are quick wins versus structural work

**Suggested visual**
- Pipeline visual: repo inputs → AI summary → debt categories → ranked backlog

**Speaker notes**
Explain that AI is not deciding the tradeoffs. It is accelerating inspection.

---

## Slide 7 — Day 2 Exercise: Friction Map and Debt Backlog

**Core message:** Students should leave with a ranked list, not just a complaint list.

**Bullets**
- List 10 sources of friction in a repo or workflow
- Classify each one
- Estimate the repeated cost
- Select three items for staged improvement

**Suggested visual**
- Backlog board with category, interest, risk, and priority columns

**Speaker notes**
The output should be something a team could actually discuss after class.
