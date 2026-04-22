ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 03-slides-day-1.md

# Day 1 Slides — What Good Looks Like

## Slide 1 — Day 1 opening

**Title:** What good looks like in a software project

**Key points**
- Today is about engineering changeability, not feature count.
- We need a shared way to recognize healthy versus fragile systems.
- Claude Code CLI will help us inspect, summarize, and prioritize.

**Speaker notes**
- Students need a common vocabulary before they can improve anything.
- Explain that “good” means “easier to understand, verify, and change safely.”

---

## Slide 2 — The real target is changeability

**Key points**
- Software quality is not one thing.
- Many quality attributes matter because they affect the cost and risk of change.
- A system is better when engineers can understand it, run it, test it, observe it, and ship changes with confidence.

**Speaker notes**
- This is a framing correction.
- Teams often debate style while ignoring friction.

---

## Slide 3 — Why technical debt matters more in the age of AI

**Key points**
- AI can amplify both quality and mess.
- Weak architecture, setup, tests, or observability reduce the value of AI assistance.
- AI is most useful when it helps expose and reduce the debt that blocks safe change.

**Speaker notes**
- Claude can move faster than the human system around it.
- If the surrounding system is weak, fast change becomes unsafe change.

---

## Slide 4 — The five pillars

**Key points**
- Architecture clarity
- Reproducibility
- Testability
- Observability
- Safe change

**Speaker notes**
- Introduce the pillars now; the rest of the week drills into them.

---

## Slide 5 — What poor looks like

**Key points**
- no one trusts the README
- build steps only work on one person’s laptop
- tests are slow, flaky, or missing
- nobody can trace a request end to end
- no one can tell what version is in QA
- changes feel scary and large

**Speaker notes**
- This slide should feel uncomfortably familiar.

---

## Slide 6 — Repo health scorecard

**Key points**
- Use a lightweight 0–3 score across 12 dimensions.
- Focus on evidence, not opinion.
- Scoring creates a shared diagnosis, not a perfect measurement system.

**Speaker notes**
- Show the scorecard categories.
- Explain that precision is less important than consistency and actionability.

---

## Slide 7 — Claude Code CLI demo: first-pass repo diagnosis

**Demo prompt**
```text
Inspect this repository and help me score it for engineering changeability.
For each dimension, summarize evidence from the repo and suggest a 0–3 score.
Do not modify code.
At the end, identify the top three blockers to safer change.
```

**Speaker notes**
- Do not let Claude change anything yet.
- Make the point that analysis comes before action.

---

## Slide 8 — What Claude is good at on day 1

**Key points**
- summarizing structure
- identifying obvious gaps
- comparing docs to code
- surfacing likely missing practices
- helping draft a health score

**Speaker notes**
- It is especially good at generating a first pass that humans can refine.

---

## Slide 9 — What still requires human judgment

**Key points**
- actual business criticality
- hidden team pain not visible in code
- compliance and operational constraints
- the true cost and blast radius of changing something
- whether a proposed score reflects real lived experience

**Speaker notes**
- Students should not confuse “plausible analysis” with “complete understanding.”

---

## Slide 10 — Day 1 exercise instructions

**Exercise**
- inspect a repo
- complete the scorecard
- pick the first debt item to fix
- justify the choice using impact, effort, and blast radius

**Speaker notes**
- This is the pattern for the whole course: inspect, prioritize, improve.

---

## Slide 11 — Debrief questions

**Questions**
- Which score dimensions were easiest to assess from the repo alone?
- Which required outside context?
- What did Claude infer that it could not fully prove?

---

## Slide 12 — Bridge to day 2

**Key points**
- tomorrow we move from scoring to two concrete improvement areas:
  - architecture clarity
  - reproducible setup

**Speaker notes**
- Set expectation that tomorrow gets more concrete and operational.
