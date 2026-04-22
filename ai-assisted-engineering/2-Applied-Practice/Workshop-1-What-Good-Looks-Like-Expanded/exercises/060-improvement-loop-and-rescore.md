# 060 Improvement Loop And Rescore

## Objective

Complete the Workshop 1 loop by applying one small improvement and rerunning the scorecard.

## Key Teaching Point

The output is not a one-time assessment. The output is a repeatable improvement loop.

## Participant Instructions

1. Pick one weak scorecard category.
2. Ask Claude Code for three small improvement options.
3. Choose the safest, highest-leverage option.
4. Apply the improvement.
5. Run the narrowest relevant validation.
6. Rerun the scorecard for the changed category and overall summary.
7. Capture the before/after delta.

## Suggested Claude Code Prompt

```text
Use the baseline scorecard and our findings so far.

Pick improvement options for the weakest category we selected.

Rules:
- Propose three options.
- Each option must be small enough to review.
- For each option, list expected benefit, files likely touched, validation method, and risk.
- Recommend one option, but do not apply it yet.
```

## Apply Prompt

```text
Apply the selected improvement.

Constraints:
- Keep the diff small.
- Preserve existing behavior unless we explicitly agree to change it.
- Run the narrowest relevant validation.
- Show positive proof of what changed and what was verified.
- Do not commit unless I ask.
```

## Rescore Prompt

```text
Rerun the Repository Health Scorecard for the changed category and update the overall summary.

Compare:
- baseline score
- new proposed score
- concrete evidence that changed
- what remains uncertain
- next recommended action

Write the result to docs/ai-sdlc/repo-health/rescore-delta.md after showing me the proposed content.
```

## Expected Output

- One small improvement.
- Validation result.
- Rescore delta.
- Next action list.

## Debrief Questions

- Did the score change because the repo improved, or because we understood it better?
- Was the improvement small enough to review?
- What would be the next most logical improvement?
- Which parts of the workflow should become team habit?

