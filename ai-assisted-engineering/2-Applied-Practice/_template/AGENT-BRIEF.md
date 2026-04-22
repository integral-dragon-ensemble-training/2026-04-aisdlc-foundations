# Agent Brief — Applied Practice Workshop Build

This document is the shared brief for all parallel agents building Applied Practice workshops.

## Product context

**Applied Practice (Week 3)** is Phase 2 of Integral Dragon's AI-SDLC course pipeline.
Parent org: **Integral Dragon**. Delivered for: **Ensemble Health Partners**.

**Course thesis (one line):**
> AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.

**Five-part method taught across the program:**
1. Define what good looks like.
2. Identify the debt that blocks it.
3. Use AI to analyze and improve it.
4. Validate improvements with tests, observability, and security.
5. Turn that into a repeatable engineering practice.

**Five workshops:**
- Workshop 1 — What Good Looks Like
- Workshop 2 — Technical Debt as Friction
- Workshop 3 — Using AI to Inspect and Improve
- Workshop 4 — Validation: Tests, Observability, Security
- Workshop 5 — Making It Repeatable

## Per-workshop deliverables

Each workshop folder must contain this structure:

```
Workshop-N-<Title>/
├── README.md
├── slides/
│   ├── workshop-N-slides.md          — markdown source (one slide per H1/---)
│   ├── workshop-N-slides.html        — rendered HTML deck (copy of template with content filled in)
│   └── workshop-N-slides.pdf         — rendered via _template/render-pdf.sh
├── exercises/
│   ├── workshop-N-exercises.md       — core exercise(s) + any lightweight in-class exercises applicable
│   ├── workshop-N-exercises.docx     — pandoc render of the .md
│   ├── workshop-N-rubric.md          — rubric/scorecard relevant to this workshop (if any)
│   └── workshop-N-rubric.docx        — pandoc render (if rubric exists)
├── resources/
│   ├── workshop-N-resources.md       — curated readings + repo cheat sheet entries for this workshop
│   └── workshop-N-resources.docx     — pandoc render
└── instructor/
    ├── instructor-notes.md          — relevant misconceptions, pacing, emphasis
    ├── discussion-prompts.md        — the workshop's discussion prompts
    ├── sample-answers.md            — sample answer guidance for this workshop's exercise
    └── participant-handout.md       — participant-facing handout (shared across all workshops; duplicate the overall handout or customize)
```

## Style constraints (MUST follow)

### Slide HTML deck

**Base the HTML on this template (copy + adapt):**
`/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/slide-template.html`

**CRITICAL visual rules:**
- Deep navy background (`#0b1429`), cyan accent (`#3ab5cc`), white text
- Wordmark `INTEGRAL DRAGON` in monospace uppercase at top (left on title slide, right on content slides)
- Title slide: large display headline, short cyan accent line, subtitle, program tag, decorative concentric-circles SVG art on right
- Content slides: top eyebrow `• WORKSHOP 0N | SECTION LABEL` in cyan monospace; headline; thin accent-tinted rule; content
- Cards: light-background (`#f6f9fc`) with 4px cyan left border, rounded 10px, subtle shadow
- Arrow bullets: cyan `→` glyph + text, generous spacing
- Footer: `Workshop 0N | Integral Dragon` (left) + page number (right), 10px uppercase monospace, muted gray
- Page size: 1280×720, each `<section class="slide">` is one page

**DO NOT:**
- Invent new colors (no orange, no purple, only the template palette)
- Use rounded container hero backdrops that reveal template placeholder shapes ("Workshop Title" fallback)
- Use the McKinsey firm name anywhere (just use Integral Dragon)

### Slide count per deck
- Target **7–9 slides** per workshop deck (title + 5–7 content + close)

### Slide content
Use the source slide markdown at `__research/v-gpt-1/02-applied-practice-week-3/03-slides/<dayfile>.md` as the primary content. Each "Slide N" section there maps to one `<section class="slide">` in the HTML. Apply the visual patterns from the template (cards, arrows, stat rows, timeline, quote) as appropriate for each slide's content.

## Rendering commands (run at end of your build)

```bash
# Render PDF
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-pdf.sh \
    <workshop>/slides/workshop-N-slides.html \
    <workshop>/slides/workshop-N-slides.pdf

# Render DOCX (for each markdown deliverable that needs docx form)
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-docx.sh \
    <workshop>/exercises/workshop-N-exercises.md \
    <workshop>/exercises/workshop-N-exercises.docx
```

## Source research paths

All source research lives under:
`/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/__research/v-gpt-1/02-applied-practice-week-3/`

Key files:
- `01-course-foundation/01-course-thesis-and-storyline.md`
- `01-course-foundation/02-what-good-looks-like-framework.md` (primarily Workshop 1, supports Workshop 3)
- `01-course-foundation/03-technical-debt-taxonomy.md` (primarily Workshop 2)
- `02-course-design/01-five-day-course-map.md`
- `02-course-design/02-daily-lesson-outlines.md`
- `03-slides/01-day-1-what-good-looks-like.md` … `05-day-5-making-it-repeatable.md`
- `04-exercises/01-core-exercises.md` (Exercise 1-8, pick the relevant ones for your workshop)
- `04-exercises/02-lightweight-in-class-exercises.md`
- `04-exercises/03-rubrics-and-scorecards.md`
- `05-resources/02-curated-readings-and-repos.md` (organized by workshop already)
- `05-resources/03-example-repositories-cheat-sheet.md`
- `05-resources/04-course-phrasing-and-terminology.md`
- `06-instructor-assets/01-instructor-notes.md`
- `06-instructor-assets/02-discussion-prompts.md` (organized by workshop already)
- `06-instructor-assets/03-student-handout.md`
- `06-instructor-assets/04-sample-answer-guidance.md`

## Workshop-to-exercise mapping

Per user instruction, split exercises per-workshop based on which workshop they apply to:

- **Workshop 1:** Exercise 1 (Repository Health Scorecard); Scorecard #1 + #4 from rubrics; lightweight: "Missing Artifact Drill"
- **Workshop 2:** Exercise 2 (Friction Map and Debt Inventory); Rubric #2; lightweight: "Smell or Debt?", "The Highest-Interest Debt"
- **Workshop 3:** Exercise 3 (Documentation Gap Hunt), Exercise 4 (Architecture Map), Exercise 5 (AI-Assisted Test Improvement); Participant Prompt Template (#5); lightweight: "Prompt Tightening", "Is This a Good AI Task?", "One Better Question"
- **Workshop 4:** Exercise 6 (Observability Gap Review), Exercise 7 (AI-Assisted Refactoring Review); Rubric #3 (AI-Assisted Refactoring Review Checklist); lightweight: "Confidence or Theater?", "Where Would You Put the Log?", "Score the Diff"
- **Workshop 5:** Exercise 8 (30-Day Improvement Plan); lightweight: "Rewrite or Stage It?"

## Writing voice

- Plain, declarative, engineer-respectful.
- Uses the framing lines from `05-resources/04-course-phrasing-and-terminology.md`.
- Never prescribes more process than the source supports.
- When summarizing source, keep claims tight and evidence-grounded.

## When you finish

Write a short `README.md` in the workshop folder that lists all artifacts produced and their paths.
