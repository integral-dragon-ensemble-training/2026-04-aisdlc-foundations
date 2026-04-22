# 030 Expansion Bundle Selection

This stage documents how the generated material was narrowed to the source bundle that best explains the current course.

## Candidate Bundles

Earlier or alternate bundle:

- `ai-assisted-engineering/__research/v-gpt-2/applied-practice/`

Selected bundle:

- `ai-assisted-engineering/__research/v-gpt-2/applied-practice 2/`

Compressed artifacts:

- `ai-assisted-engineering/__research/v-gpt-2/applied-practice-v0.1.zip`
- `ai-assisted-engineering/__research/v-gpt-2/applied-practice-course-bundle-v0.1.zip`

## Selection Rationale

`applied-practice 2` is the selected source bundle because it directly maps to the live `_overview-internal` files.

Examples:

- `applied-practice 2/02-course-design/01-five-day-course-map.md` maps to `_overview-internal/five-day-course-map.md`.
- `applied-practice 2/01-course-foundation/02-what-good-looks-like-framework.md` maps to `_overview-internal/what-good-looks-like-framework.md`.
- `applied-practice 2/03-slides/` maps to the live workshop slide outlines, although the live slides are condensed and polished.

The main observed difference is removal of generated breadcrumb lines such as `ChatGPT Folder > ...`.

## Decision Rule

When comparing future candidate bundles, prefer the candidate that best supports:

- concrete workshop delivery
- brownfield repository improvement
- practical Claude Code workflows
- progressive quality model from "what good looks like" to repeatable operating practice
- exercises that can be run against current project codebases
- enough source structure to generate slides, handouts, instructor notes, and artifacts

## Output Of This Stage

The selected course-generation source is:

```text
ai-assisted-engineering/__research/v-gpt-2/applied-practice 2/
```

The alternate bundle remains a supporting reference, especially for research prompts and additional framing:

```text
ai-assisted-engineering/__research/v-gpt-2/applied-practice/
```

