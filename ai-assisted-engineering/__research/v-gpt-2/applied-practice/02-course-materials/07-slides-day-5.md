ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 07-slides-day-5.md

# Day 5 Slides — Safe Change and the Operating Model

## Slide 1 — Day 5 opening

**Title:** How do we turn one-off improvement work into a repeatable practice?

---

## Slide 2 — Safe change is the goal

**Key points**
- small changes
- clear review boundaries
- strong validation
- rollback awareness
- secure defaults
- reduced approval fatigue and reduced heroics

---

## Slide 3 — Guardrails that matter

**Key points**
- linting
- static analysis
- security scanning
- secret hygiene
- reviewer checklists
- deploy verification
- incremental rollout discipline

---

## Slide 4 — Claude Code CLI is powerful but must be governed

**Key points**
- use it to inspect, draft, and accelerate
- do not hand it uncontrolled architectural change
- require evidence, summaries, and validation notes
- prefer small diff sets and reviewable plans

---

## Slide 5 — Claude Code CLI demo: safe incremental plan

**Demo prompt**
```text
Given these repo health findings, propose an incremental two-week debt-paydown plan.
Prefer small reviewable changes, avoid broad refactors, include validation steps, and call out where human review is mandatory.
```

---

## Slide 6 — Common anti-patterns in AI-assisted engineering

**Key points**
- “fix the repo”
- giant generated diffs
- generated tests no one understands
- hidden coupling from confident but shallow edits
- skipping manual verification because the model sounds certain
- letting the tool define the architecture

---

## Slide 7 — The operating model

**Key points**
1. inspect the repo
2. score quality dimensions
3. identify high-friction blockers
4. choose one small improvement
5. use Claude to analyze and draft
6. verify narrowly
7. review carefully
8. document the result
9. repeat

---

## Slide 8 — Capstone instructions

**Deliverables**
- repo scorecard
- top blockers
- first improvement recommendation
- validation plan
- explanation of Claude’s role
- explanation of what required human judgment

---

## Slide 9 — What success looks like after the course

**Key points**
- students stop asking only “can AI write this?”
- students start asking “where is our delivery friction?”
- students use Claude to expose and reduce that friction
- teams get safer, not just faster

---

## Slide 10 — Closing synthesis

**Message**
AI-assisted engineering pays off most when it helps teams see, reduce, and systematically pay down the technical debt that makes software hard to change.

**Speaker notes**
- End on the same line you started with.
- Tie the week back to practical leadership and delivery outcomes.
