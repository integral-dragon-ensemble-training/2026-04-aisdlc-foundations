# Session 4 — Discussion Prompts

Use these prompts during or between activities. Each is intended to surface either a misconception worth correcting or a concrete experience from the room.

---

## Opening move

> "How do you know an improvement is real?"

Keep this open for 2–3 minutes. Good answers name a specific validation signal — a test that failed before and passes after, a metric that moved, a log line that appeared — rather than "we reviewed it."

---

## Mid-session prompts

### Theater vs. confidence

> "Which of your current validation signals are real, and which are mostly theater?"

Push for specifics. "Our CI is green" is a dashboard observation, not an answer. Good answers name which signals a senior engineer would actually trust if a production incident happened tomorrow.

### Observability and change safety

> "Where would observability reduce fear of change the most in your system?"

Good answers tie observability back to *refactoring safety*, not just incident response. The hidden claim: you can refactor more aggressively in a system you can see.

### AI-generated change and review standards

> "What kinds of AI-generated changes would you refuse to merge without deeper review?"

Good answers draw lines by category (schema, auth, dependencies, anything that touches a boundary), not by author. The standard is evidence, not authorship.

---

## Debrief prompt for Exercise 7

> "What made this output look good at first, and what made it unreliable on inspection?"

This is the most important prompt of the day. It forces students to articulate the difference between fluency and evidence. Expect answers about confident tone, plausible structure, and missing edge cases.

---

## Exit prompt

> "What is one validation gate you could add to your team's workflow next week that would materially reduce risk?"

Constrain to *one*, and to *next week*, so the answer has to be realistic. Good answers are concrete (a dependency-review action, a PR template question, a named runtime check), not aspirational ("we should do better testing").
