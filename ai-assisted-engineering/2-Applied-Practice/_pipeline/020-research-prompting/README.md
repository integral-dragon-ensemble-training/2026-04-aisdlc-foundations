# 020 Research Prompting

This stage documents how the course intent moved into research and structured course generation.

## Source Files

- `ai-assisted-engineering/__research/v-gpt-2/applied-practice/01-research/01-gemini-deep-research-prompt.md`
- `ai-assisted-engineering/__research/v-gpt-2/applied-practice/01-research/02-gemini-follow-up-prompt.md`

## Transformation

The first prompt asks Gemini Deep Research to explore a rigorous applied class for AI-assisted software development. The core constraints were:

- Claude Code CLI is central to the workflow.
- Azure and enterprise engineering context matter.
- .NET is primary; Python is secondary.
- The real problem is brownfield quality, technical debt, validation, security, and governance.
- The course should move beyond tool demos into practical software delivery improvement.

The follow-up prompt asks for classroom-ready assets from the research:

- final course outline
- slide outline
- exercise pack
- Claude Code CLI lab guide
- scorecard handout
- capstone brief

## Rerun Instructions

If rerunning the research stage:

1. Start with `01-gemini-deep-research-prompt.md`.
2. Preserve the enterprise brownfield constraints.
3. Store the resulting research report under a new dated or versioned folder in `ai-assisted-engineering/__research/`.
4. Run the follow-up prompt against that research report.
5. Store the generated asset bundle separately from the current live course.

Do not overwrite the existing `v-gpt-2` folders during a rerun. Treat each rerun as a candidate branch until it is selected.

## Acceptance Criteria

A research rerun is usable if it preserves:

- brownfield codebase improvement as the practical center
- AI agents as accelerators for inspection, refactoring, test generation, and workflow improvement
- security and governance as operating constraints
- validation and observability as proof mechanisms
- enough classroom structure to generate decks, exercises, and handouts

