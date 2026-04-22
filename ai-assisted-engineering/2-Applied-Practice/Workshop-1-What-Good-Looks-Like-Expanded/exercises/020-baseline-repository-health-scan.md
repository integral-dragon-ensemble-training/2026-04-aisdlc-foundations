# 020 Baseline Repository Health Scan

## Objective

Use Claude Code to collect evidence for a baseline Repository Health Scorecard.

## Key Teaching Point

Claude Code can draft the scorecard, but participants must review the evidence and own the scoring.

## Participant Instructions

1. Ask Claude Code to run a read-only repository scan.
2. Require evidence for every category.
3. Require an uncertainty note where evidence is missing.
4. Review the draft scores.
5. Adjust any score that is based on weak evidence.
6. Identify the top three weak areas most likely to slow future change.

## Suggested Claude Code Prompt

```text
Use the Repository Health Scorecard skill we just created.

Run a read-only baseline scan of this repository.

Rules:
- Do not edit files.
- Use only visible repository evidence.
- For each category, list the files, scripts, workflows, tests, or docs you inspected.
- Give a proposed score from 1 to 5.
- Explain the score in one or two sentences.
- Add an "uncertainty" note if the repository does not expose enough evidence.
- End with the top three weak areas most likely to slow future change.

Write the result to docs/ai-sdlc/repo-health/baseline-scorecard.md only after showing me the proposed content.
```

## Expected Output

- Baseline scorecard.
- Evidence list.
- Uncertainty notes.
- Top three weak areas.

## Debrief Questions

- Which scores were supported by clear evidence?
- Which scores were guesses dressed up as confidence?
- Which weak area would create the most friction for a new engineer?
- Which weak area would most reduce AI agent effectiveness?

