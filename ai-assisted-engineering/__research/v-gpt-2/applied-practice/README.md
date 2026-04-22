ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > README.md

# Applied Practice Bundle

This bundle is a markdown-first planning kit for a five-day, one-hour-per-day class on AI-SDLC.

## Core organizing theme

**AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.**

## How to use this bundle

1. Start with `00-overview-approach-slides.md`.
2. Use `01-research/01-gemini-deep-research-prompt.md` to generate a broader external research report in Gemini Deep Research.
3. Use `02-course-materials/01-course-architecture.md` and `02-course-materials/02-instructor-overview-and-timing.md` to decide what will fit the available class time.
4. Build your actual teaching deck from:
   - `00-overview-approach-slides.md`
   - `02-course-materials/03-slides-day-1.md`
   - `02-course-materials/04-slides-day-2.md`
   - `02-course-materials/05-slides-day-3.md`
   - `02-course-materials/06-slides-day-4.md`
   - `02-course-materials/07-slides-day-5.md`
5. Pull labs and demonstrations from:
   - `02-course-materials/08-exercise-pack.md`
   - `02-course-materials/09-claude-code-cli-playbook.md`
   - `02-course-materials/10-scorecards-and-rubrics.md`
6. Use `02-course-materials/11-recommended-repos-and-readings.md` as the reading list and source bank.

## Folder structure

- `01-research/`
  - Gemini Deep Research inputs and refinement prompts.
- `02-course-materials/`
  - Course structure, slide markdown, exercise pack, Claude Code CLI workflows, scorecards, and reading/repo recommendations.

## Design choices

- Claude Code CLI is treated as the primary hands-on tool.
- Azure is the default enterprise context.
- .NET examples are primary.
- Python examples are secondary and increasing in importance.
- The course is brownfield-first, not greenfield-first.
- The class focuses on safer change, not just faster code generation.

## Suggested build order for your final deck

1. Opening story and course thesis
2. Definition of “what good looks like”
3. Five-pillar framework
4. Daily lessons
5. Claude Code CLI workflows
6. Labs and capstone
7. Reading list / repo list
