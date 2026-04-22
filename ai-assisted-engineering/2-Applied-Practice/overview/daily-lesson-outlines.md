# Daily Lesson Outlines

This file provides the more detailed lesson shape for each day.

## Day 1 — What Good Looks Like

### Opening move
Ask: “If I gave a new engineer this repo at 9:00 a.m., what would they need in order to make a safe change by the end of the day?”

### Key teaching points
- Good software is understandable, reproducible, testable, observable, and operable.
- Documentation and architecture are not side topics; they are part of maintainability.
- Observability belongs in “what good looks like,” not just in operations.

### Activity
Use the repository health scorecard on a public repo or an internal training repo.

### Exit prompt
“What are the top three missing qualities that most slow down changes in your team’s codebase?”

---

## Day 2 — Technical Debt as Friction

### Opening move
Ask: “What do engineers complain about repeatedly that is not itself the business feature they are trying to change?”

### Key teaching points
- Debt is anything that makes future changes slower, riskier, or harder to reason about.
- Code debt is only one slice.
- Friction compounds through repeated use.

### Activity
Have groups classify real examples into debt categories and estimate the “interest” paid.

### Exit prompt
“Which kind of debt in your environment creates the highest repeated tax?”

---

## Day 3 — Using AI to Inspect and Improve

### Opening move
Show a weak prompt and a strong prompt for analyzing a repo.

### Key teaching points
- AI is strongest when given clear scope, artifacts, criteria, and desired output format.
- AI should produce inspectable outputs: lists, maps, candidate refactors, checklists, test ideas.
- Small, validated improvements beat giant speculative rewrites.

### Activity
Use AI to generate:
- a docs gap list,
- a candidate refactor plan,
- test ideas for one component,
- and a repo health report.

### Exit prompt
“What AI-generated outputs would you trust after review, and which would you never trust without deeper verification?”

---

## Day 4 — Validation: Tests, Observability, Security

### Opening move
Ask: “How do you know an improvement is real?”

### Key teaching points
- Coverage is not confidence.
- Observability is part of change safety.
- Security and supply chain checks are not optional polish.
- AI changes should pass through explicit validation gates.

### Activity
Evaluate a sample change request using the AI-assisted refactoring review checklist.

### Exit prompt
“Which validation signals in your current team are genuinely trustworthy, and which are mostly theater?”

---

## Day 5 — Making It Repeatable

### Opening move
Ask: “What would make this work after the class ends?”

### Key teaching points
- Improvement work needs cadence, ownership, and a backlog.
- Teams should standardize small reviewable changes.
- AI usage needs policy and workflow norms, not just access.

### Activity
Build a 30-day improvement plan:
- 3 quick wins,
- 2 structural improvements,
- 1 workflow change,
- 1 measurement change.

### Exit prompt
“What is one change your team could normalize next month that would permanently reduce friction?”
