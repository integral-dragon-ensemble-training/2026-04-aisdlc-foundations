# 050 Participant Polish

This stage documents the split between internal source reference and participant-facing course materials.

## Primary Commit

- `cce2be0` - `Rename overview/ to _overview-internal/; add participant-facing overview/`

## Transformation

The first generated overview was useful as an internal source and planning reference, but it was not the right surface for participants.

The polish pass created two layers:

- `_overview-internal/` keeps the original source/reference material close to the course.
- `overview/` provides the participant-facing explanation, overview deck, preparation guide, and reference material.

## Why This Matters

This split should be preserved in reruns.

Internal source material can be dense, generative, and structured for course design. Participant-facing material should be clearer, shorter, and oriented around what the cohort will do.

## Rerun Rule

Do not overwrite participant-facing material directly from generated research output.

Instead:

1. Generate or update internal source material.
2. Distill it into participant-facing language.
3. Check that the participant layer explains why the work matters, what will happen, and how to prepare.
4. Keep instructor-only rationale out of participant handouts unless it helps execution.

## Acceptance Criteria

The participant layer should answer:

- What is this section about?
- Why does it matter for AI-assisted engineering?
- What will participants do hands-on?
- What should they bring or prepare?
- How does this connect to real project work?

