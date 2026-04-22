# 010 Create The Scorecard Skill

## Objective

Create a reusable Claude Code scoring instruction that turns the Workshop 1 rubric into a repeatable repo health scan.

## Why This Exercise Exists

Without a rubric, AI will optimize for whatever the prompt makes salient. The scorecard gives Claude Code a stable quality target.

## Participant Instructions

1. Open the target repository in Claude Code.
2. Tell Claude Code this is a training exercise and the first pass is read-only.
3. Create a repo-local scorecard skill or instruction file.
4. Ask Claude Code to confirm the scoring categories and evidence rules before scanning.
5. Do not allow code edits yet.

## Suggested Claude Code Prompt

```text
We are doing an AI-SDLC training exercise.

Create a repo-local Repository Health Scorecard skill or instruction file using the rubric I provide.

Requirements:
- Do not modify application code.
- If this repo already has a Claude Code skill convention, use it.
- If it does not, create docs/ai-sdlc/repository-health-scorecard-skill.md.
- The skill must score the repo across nine categories from 1 to 5.
- The skill must require concrete evidence for each score.
- The skill must explicitly name uncertainty instead of guessing.
- The skill must say that humans make the final scoring decision.

After creating the file, summarize what you created and stop.
```

Then provide the scorecard content from:

```text
Workshop-1-What-Good-Looks-Like-Expanded/resources/repository-health-scorecard-skill.md
```

## Expected Output

- A repo-local scorecard skill or instruction file.
- A short Claude Code summary of where it was stored.
- No code changes.

## Instructor Notes

If Claude Code wants to immediately scan or edit the repo, stop it and reset the boundary:

```text
Stop. Do not scan or modify yet. First confirm the scorecard categories, output format, and evidence rules.
```

