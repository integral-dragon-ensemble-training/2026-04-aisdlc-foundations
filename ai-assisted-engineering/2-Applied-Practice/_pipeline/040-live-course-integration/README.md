# 040 Live Course Integration

This stage documents how the selected source bundle became the live `2-Applied-Practice` course.

## Primary Commit

- `b93fb3a` - `Add Applied Practice Week 3 course, session artifacts, and supplemental materials`

This commit added:

- Gemini research material
- GPT/GT-side generated bundles
- live Applied Practice course folders
- session artifacts
- supplemental materials

## Transformation

The selected source bundle was converted into a live course tree:

```text
ai-assisted-engineering/2-Applied-Practice/
  _overview-internal/
  _template/
  overview/
  Workshop-1-What-Good-Looks-Like/
  Workshop-2-Technical-Debt-as-Friction/
  Workshop-3-Using-AI-to-Inspect-and-Improve/
  Workshop-4-Validation-Tests-Observability-Security/
  Workshop-5-Making-It-Repeatable/
```

The integration did not simply copy all files. It turned source material into deliverable-oriented folders:

- `slides/` for markdown slide source and rendered decks
- `exercises/` for participant practice
- `resources/` for reference material and diagrams
- `instructor/` for teaching notes and facilitation assets

## Integration Pattern

Use this pattern if regenerating a live course from a selected bundle:

1. Preserve the selected bundle unchanged under `__research`.
2. Copy or adapt durable framework material into `_overview-internal`.
3. Generate participant-facing overview material separately.
4. Create one folder per workshop.
5. Keep workshop-local `slides`, `exercises`, `resources`, and `instructor` folders together.
6. Use `_template` for repeated slide, handout, and artifact patterns.
7. Render artifacts after source markdown is stable.

## Quality Bar

A generated live course should be rejected if it:

- loses the brownfield quality thesis
- becomes mostly Claude Code feature training
- separates security and governance from real workflow design
- lacks hands-on exercises
- lacks participant-facing clarity
- cannot be extended into multi-day workshops without large restructuring

