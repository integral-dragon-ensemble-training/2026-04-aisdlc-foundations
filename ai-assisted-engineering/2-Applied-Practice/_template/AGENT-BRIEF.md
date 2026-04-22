# Agent Brief — Applied Practice Session Build

This document is the shared brief for all parallel agents building Applied Practice sessions.

## Product context

**Applied Practice (Week 3)** is Phase 2 of Integral Dragon's AI-SDLC course pipeline.
Parent org: **Integral Dragon**. Delivered for: **Ensemble Health Partners**.

**Course thesis (one line):**
> AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.

**Five-part method taught across the week:**
1. Define what good looks like.
2. Identify the debt that blocks it.
3. Use AI to analyze and improve it.
4. Validate improvements with tests, observability, and security.
5. Turn that into a repeatable engineering practice.

**Five sessions, one per day, 60 minutes each:**
- Session 1 — What Good Looks Like
- Session 2 — Technical Debt as Friction
- Session 3 — Using AI to Inspect and Improve
- Session 4 — Validation: Tests, Observability, Security
- Session 5 — Making It Repeatable

## Per-session deliverables

Each session folder must contain this structure:

```
Session-N-<Title>/
├── README.md
├── slides/
│   ├── session-N-slides.md          — markdown source (one slide per H1/---)
│   ├── session-N-slides.html        — rendered HTML deck (copy of template with content filled in)
│   └── session-N-slides.pdf         — rendered via _template/render-pdf.sh
├── exercises/
│   ├── session-N-exercises.md       — core exercise(s) + any lightweight in-class exercises applicable
│   ├── session-N-exercises.docx     — pandoc render of the .md
│   ├── session-N-rubric.md          — rubric/scorecard relevant to this session (if any)
│   └── session-N-rubric.docx        — pandoc render (if rubric exists)
├── resources/
│   ├── session-N-resources.md       — curated readings + repo cheat sheet entries for this day
│   └── session-N-resources.docx     — pandoc render
└── instructor/
    ├── instructor-notes.md          — relevant misconceptions, pacing, emphasis
    ├── discussion-prompts.md        — the day's discussion prompts
    ├── sample-answers.md            — sample answer guidance for this day's exercise
    └── student-handout.md           — student-facing handout (shared across all sessions; duplicate the overall handout or customize)
```

## Style constraints (MUST follow)

### Slide HTML deck

**Base the HTML on this template (copy + adapt):**
`/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/slide-template.html`

**CRITICAL visual rules:**
- Deep navy background (`#0b1429`), cyan accent (`#3ab5cc`), white text
- Wordmark `INTEGRAL DRAGON` in monospace uppercase at top (left on title slide, right on content slides)
- Title slide: large display headline, short cyan accent line, subtitle, program tag, decorative concentric-circles SVG art on right
- Content slides: top eyebrow `• SESSION 0N | SECTION LABEL` in cyan monospace; headline; thin accent-tinted rule; content
- Cards: light-background (`#f6f9fc`) with 4px cyan left border, rounded 10px, subtle shadow
- Arrow bullets: cyan `→` glyph + text, generous spacing
- Footer: `Session 0N | Integral Dragon` (left) + page number (right), 10px uppercase monospace, muted gray
- Page size: 1280×720, each `<section class="slide">` is one page

**DO NOT:**
- Invent new colors (no orange, no purple, only the template palette)
- Use rounded container hero backdrops that reveal template placeholder shapes ("Session Title" fallback)
- Use the McKinsey firm name anywhere (just use Integral Dragon)

### Slide count per deck
- Target **7–9 slides** per session deck (title + 5–7 content + close)

### Slide content
Use the source slide markdown at `__research/v-gpt-1/02-applied-practice-week-3/03-slides/<dayfile>.md` as the primary content. Each "Slide N" section there maps to one `<section class="slide">` in the HTML. Apply the visual patterns from the template (cards, arrows, stat rows, timeline, quote) as appropriate for each slide's content.

## Rendering commands (run at end of your build)

```bash
# Render PDF
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-pdf.sh \
    <session>/slides/session-N-slides.html \
    <session>/slides/session-N-slides.pdf

# Render DOCX (for each markdown deliverable that needs docx form)
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-docx.sh \
    <session>/exercises/session-N-exercises.md \
    <session>/exercises/session-N-exercises.docx
```

## Source research paths

All source research lives under:
`/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/__research/v-gpt-1/02-applied-practice-week-3/`

Key files:
- `01-course-foundation/01-course-thesis-and-storyline.md`
- `01-course-foundation/02-what-good-looks-like-framework.md` (primarily Session 1, supports Session 3)
- `01-course-foundation/03-technical-debt-taxonomy.md` (primarily Session 2)
- `02-course-design/01-five-day-course-map.md`
- `02-course-design/02-daily-lesson-outlines.md`
- `03-slides/01-day-1-what-good-looks-like.md` … `05-day-5-making-it-repeatable.md`
- `04-exercises/01-core-exercises.md` (Exercise 1-8, pick the relevant ones for your day)
- `04-exercises/02-lightweight-in-class-exercises.md`
- `04-exercises/03-rubrics-and-scorecards.md`
- `05-resources/02-curated-readings-and-repos.md` (organized by day already)
- `05-resources/03-example-repositories-cheat-sheet.md`
- `05-resources/04-course-phrasing-and-terminology.md`
- `06-instructor-assets/01-instructor-notes.md`
- `06-instructor-assets/02-discussion-prompts.md` (organized by day already)
- `06-instructor-assets/03-student-handout.md`
- `06-instructor-assets/04-sample-answer-guidance.md`

## Day-to-exercise mapping

Per user instruction, split exercises per-session based on which session they apply to:

- **Session 1:** Exercise 1 (Repository Health Scorecard); Scorecard #1 + #4 from rubrics; lightweight: "Missing Artifact Drill"
- **Session 2:** Exercise 2 (Friction Map and Debt Inventory); Rubric #2; lightweight: "Smell or Debt?", "The Highest-Interest Debt"
- **Session 3:** Exercise 3 (Documentation Gap Hunt), Exercise 4 (Architecture Map), Exercise 5 (AI-Assisted Test Improvement); Student Prompt Template (#5); lightweight: "Prompt Tightening", "Is This a Good AI Task?", "One Better Question"
- **Session 4:** Exercise 6 (Observability Gap Review), Exercise 7 (AI-Assisted Refactoring Review); Rubric #3 (AI-Assisted Refactoring Review Checklist); lightweight: "Confidence or Theater?", "Where Would You Put the Log?", "Score the Diff"
- **Session 5:** Exercise 8 (30-Day Improvement Plan); lightweight: "Rewrite or Stage It?"

## Writing voice

- Plain, declarative, engineer-respectful.
- Uses the framing lines from `05-resources/04-course-phrasing-and-terminology.md`.
- Never prescribes more process than the source supports.
- When summarizing source, keep claims tight and evidence-grounded.

## When you finish

Write a short `README.md` in the session folder that lists all artifacts produced and their paths.
