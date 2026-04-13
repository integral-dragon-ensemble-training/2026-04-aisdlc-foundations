# Packaging Instructions

Use these instructions when turning the session source material into final presentation artifacts.

## Goal

Convert the authored source in `Source/` into polished delivery artifacts in `Artifacts/` using the presentation style template that will be provided separately.

Do not mention AI, source generation, or internal workflow in the final packaged outputs.

Do not package `Supplemental/` by default. Treat it as optional presenter support material unless explicitly requested.

## Input

Use all materials in:

- `Source/01-session-overview/`
- `Source/02-slides/`
- `Source/03-practice-and-feedback/`
- `Source/04-demo-blueprints/`
- `Source/05-reading-and-resources/`

## Output expectations

Create the following in `Artifacts/`:

### 1. Slide deck

- Format: PDF
- Source: `Source/02-slides/session-10-slides.md`
- Audience: live classroom delivery
- Purpose: presentation-ready deck for Session 10

Suggested filename:

- `Session-10-Task-Decomposition-and-Subagents-Slides.pdf`

### 2. Facilitator brief

- Format: Word document (`.docx`)
- Primary sources:
  - `Source/01-session-overview/session-brief.md`
  - `Source/04-demo-blueprints/demo-blueprints.md`
- Audience: instructor/facilitator
- Purpose: speaking notes, pacing, decomposition guidance, live-demo sequence, and teaching intent

Suggested filename:

- `Session-10-Task-Decomposition-and-Subagents-Facilitator-Brief.docx`

### 3. Participant handout

- Format: Word document (`.docx`)
- Primary sources:
  - `Source/03-practice-and-feedback/practice-and-feedback.md`
  - relevant excerpts from `Source/05-reading-and-resources/reading-and-resources.md`
- Audience: learners
- Purpose: exercises, discussion prompts, between-session follow-through, and survey/reflection prompts

Suggested filename:

- `Session-10-Task-Decomposition-and-Subagents-Participant-Handout.docx`

### 4. Reading list

- Format: Word document (`.docx`)
- Source: `Source/05-reading-and-resources/reading-and-resources.md`
- Audience: learners and facilitator
- Purpose: clean session-specific reading/resource sheet

Suggested filename:

- `Session-10-Task-Decomposition-and-Subagents-Reading-List.docx`

## Packaging guidance

### What should become slides

Only the content from `Source/02-slides/` should become the slide deck.

Do not dump the practice material or demo notes into the presentation unless they clearly belong as one short exercise prompt or one short demo cue.

### What should become Word documents

The following are document-shaped and should stay documents:

- session brief
- practice and feedback
- demo blueprints
- reading/resources

### Explicit source-to-artifact mapping

Use this mapping directly:

- `Source/01-session-overview/session-brief.md`
  - package into the facilitator brief
- `Source/04-demo-blueprints/demo-blueprints.md`
  - package into the facilitator brief
- `Source/03-practice-and-feedback/practice-and-feedback.md`
  - package into the participant handout
- `Source/05-reading-and-resources/reading-and-resources.md`
  - package into the participant handout and optionally also into a separate reading-list document

Do not place the full demo blueprint content in the participant handout unless there is a clear learner-facing reason.
Do not place the full practice-and-feedback content in the facilitator brief unless it is being quoted for delivery cues.

### Recommended consolidation

If time is limited, combine:

- `session-brief.md` + `demo-blueprints.md` into one facilitator brief
- `practice-and-feedback.md` + selected reading/resources into one participant handout

If time is not limited, keep the reading list separate as its own `.docx`.

## Tone and formatting rules

- Match the provided style template for typography, spacing, and branding.
- Keep the voice enterprise-grade, pragmatic, and instructor-ready.
- Preserve the distinction between instructor-facing and participant-facing documents.
- Avoid exposing internal file names, markdown structure, or generation traces.
- Use clean headings and page breaks where helpful.

## Content priorities

Preserve these ideas exactly:

- large prompts should be decomposed into bounded tasks
- subagents are useful because they isolate context and capability
- subagent inputs and outputs should be explicit and reviewable
- decomposition quality is a core engineering skill, not a model trick

## Minimum viable package

If only three artifacts are produced, prioritize:

1. slide deck PDF
2. facilitator brief DOCX
3. participant handout DOCX

## Default packaging decision

If there is any ambiguity, use this default:

- `demo-blueprints` goes with the facilitator material
- `practice-and-feedback` goes with the participant material
- `reading-and-resources` can either stay standalone or be appended to the participant handout
