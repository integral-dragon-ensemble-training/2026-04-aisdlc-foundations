# 080 Expansion Next Pass

This stage prepares the next planned transformation: expanding the current Applied Practice workshops from compact units into three-to-five-day hands-on workshops.

## Current Baseline

Current live workshops:

```text
ai-assisted-engineering/2-Applied-Practice/
  Workshop-1-What-Good-Looks-Like/
  Workshop-2-Technical-Debt-as-Friction/
  Workshop-3-Using-AI-to-Inspect-and-Improve/
  Workshop-4-Validation-Tests-Observability-Security/
  Workshop-5-Making-It-Repeatable/
```

Current expanded reference implementation:

```text
ai-assisted-engineering/2-Applied-Practice/
  Workshop-1-What-Good-Looks-Like-Expanded/
  Workshop-2-Technical-Debt-as-Friction-Expanded/
  Workshop-3-Using-AI-to-Inspect-and-Improve-Expanded/
  Workshop-4-Validation-Tests-Observability-Security-Expanded/
  Workshop-5-Making-It-Repeatable-Expanded/
```

Current source references:

- `ai-assisted-engineering/__research/gemini/ge,-v-2-AI-Assisted Enterprise Software Quality Course.pdf`
- `ai-assisted-engineering/__research/v-gpt-2/applied-practice 2/`
- `ai-assisted-engineering/2-Applied-Practice/_overview-internal/`
- `ai-assisted-engineering/2-Applied-Practice/overview/`

## Expansion Principle

Treat each existing workshop as the seed of a larger applied arc.

The expansion should add hands-on depth without discarding the current sequence:

1. Define good engineering outcomes.
2. Diagnose friction and technical debt.
3. Use AI agents to inspect and improve.
4. Prove changes with validation, observability, security, and governance.
5. Make the workflow repeatable.

## Proposed Write Boundary

If expanding in place, use a local expansion folder inside each workshop before replacing existing materials:

```text
Workshop-N-Name/
  _expansion/
    000-expansion-map.md
    010-day-1/
    020-day-2/
    030-day-3/
    040-day-4/
    050-day-5/
```

This keeps the current course stable while allowing Dex or sub-agents to expand workshops independently.

## Expansion Inputs Per Workshop

For each workshop, use:

- current workshop slides as the participant-facing baseline
- current exercises as the minimum viable hands-on path
- `_overview-internal` as the concept source
- `applied-practice 2` as the selected generation source
- Gemini PDF as the broader research rationale

## Quality Risks

Main risks during expansion:

- adding time without adding real practice
- overfitting to Claude Code features instead of engineering outcomes
- duplicating concepts across workshops
- losing the progressive course storyline
- burying security and governance in lecture instead of workflow
- creating parallel expansions with inconsistent structure

## Recommended Expansion Pass

1. Create an expansion map for all workshops before generating slides.
2. Define day-level objectives for each workshop.
3. Identify shared exercises and prevent duplicate work.
4. Use the `Workshop-*-Expanded/` folders as the current candidate expanded implementation.
5. Review the expanded structure before replacing or deprecating the original compact workshops.
6. Generate slides only after the expanded workshop maps are stable.
7. Render PDFs only after markdown content has been reviewed.

## Sub-Agent Suitability

Parallel expansion is safe only after each workshop has a clear write boundary.

Safe parallel units:

- one worker per workshop under `Workshop-N/_expansion/`
- one worker for shared overview alignment
- one worker for validation terminology and cross-workshop consistency

Unsafe parallel units:

- multiple workers editing the same slide deck
- independent rewrites of shared overview files
- simultaneous source and render changes in the same folder
