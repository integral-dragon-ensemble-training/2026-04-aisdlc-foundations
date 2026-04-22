# Session 5 — Making It Repeatable

Module 02 · Applied Practice · Session 05 (Week 3, Day 5 · 60 minutes)

**Theme:** Staged modernization over rewrite fantasies. Turn one-off cleanup into a repeatable engineering practice.

This is the **final session of Week 3 (Applied Practice)** and the bridge into **Phase 3 (Applied)**, where students take the method to their own repositories.

---

## Session thesis

- Most teams cannot rewrite safely or quickly — small, compounding improvements beat grand clean-slate plans.
- Improvement work needs cadence, ownership, and a backlog, not a one-off sprint.
- AI usage needs policy and workflow norms, not just access.
- The improvement sequence is **visible → unblock → confidence → observability → standardize**.
- The point is not more code. The point is easier change.

---

## Asset index

### Slides
- [`slides/session-5-slides.md`](slides/session-5-slides.md) — markdown source (9 slides).
- [`slides/session-5-slides.html`](slides/session-5-slides.html) — rendered Integral Dragon navy+cyan deck.
- [`slides/session-5-slides.pdf`](slides/session-5-slides.pdf) — print-rendered PDF (1280×720, one slide per page).

### Exercises
- [`exercises/session-5-exercises.md`](exercises/session-5-exercises.md) — Exercise 8 (30-Day Improvement Plan) and the lightweight *Rewrite or Stage It?* in-class exercise.
- [`exercises/session-5-exercises.docx`](exercises/session-5-exercises.docx) — pandoc render.

### Resources
- [`resources/session-5-resources.md`](resources/session-5-resources.md) — Day 5 curated readings (Semantic Versioning, Conventional Commits, semantic-release, release-please) plus supporting references and example repositories.
- [`resources/session-5-resources.docx`](resources/session-5-resources.docx) — pandoc render.

### Instructor
- [`instructor/instructor-notes.md`](instructor/instructor-notes.md) — pacing, misconceptions, what to watch for in the 30-day plan.
- [`instructor/discussion-prompts.md`](instructor/discussion-prompts.md) — Day 5 prompts plus prompts specific to the plan, workflow standardization, measurement, and AI discipline.
- [`instructor/sample-answers.md`](instructor/sample-answers.md) — strong/adequate/weak calibration, including the "Strong Day 5 plans" section and a worked example.
- [`instructor/student-handout.md`](instructor/student-handout.md) — the shared weekly student handout.

---

## Slide deck structure (9 slides)

1. **Title** — Making It Repeatable.
2. **Do not turn this into a rewrite fantasy** — stair-step diagram.
3. **A practical improvement sequence** — five-step timeline.
4. **What to standardize in team workflow** — arrow-bullet norms.
5. **What to measure** — six-card metrics grid plus recurring-friction note.
6. **30-day team plan** — four-card structure (3 quick wins, 2 structural, 1 workflow, 1 validation) plus check-in.
7. **The mature use of AI in engineering** — AI discipline norms.
8. **Final takeaways** — five takeaway cards plus a forward-looking Phase-3 card.
9. **Close** — "The point is not more code. The point is easier change."

---

## Exercise map

- **Core:** Exercise 8 — 30-Day Improvement Plan (20 min, group).
- **Lightweight:** *Rewrite or Stage It?* (10–15 min, individual + group debate).

Both exercises explicitly consume inputs from Sessions 1–4 (scorecard, debt inventory, AI-assisted findings, validation review).

---

## Connects to

- **Phase 2 · Applied Practice** — this session closes Week 3. Every prior session feeds into the 30-day plan.
- **Phase 3 · Applied** — students take the method to their own repositories. The 30-day plan built in this session is the artifact they carry forward.

---

## Render commands

```bash
# PDF
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-pdf.sh \
    Session-5-Making-It-Repeatable/slides/session-5-slides.html \
    Session-5-Making-It-Repeatable/slides/session-5-slides.pdf

# DOCX (exercises)
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-docx.sh \
    Session-5-Making-It-Repeatable/exercises/session-5-exercises.md \
    Session-5-Making-It-Repeatable/exercises/session-5-exercises.docx

# DOCX (resources)
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-docx.sh \
    Session-5-Making-It-Repeatable/resources/session-5-resources.md \
    Session-5-Making-It-Repeatable/resources/session-5-resources.docx
```
