# Instructor Cheat Sheet

This folder is for live demonstration support.

Use it when participants need to see the workflow before doing it themselves.

## Files

- `claude-code-demo-script.md` - live demo sequence from scorecard skill to rescore.
- `participant-assistant-workflow.md` - instructor explanation of the participant-facing Claude TA workflow.
- `prompt-blocks.md` - individual copy/paste prompts for Claude Code.

## Demo Goal

Show the full loop once:

```text
scorecard skill
  -> baseline scan
  -> architecture/setup/test confidence deep dive
  -> one small improvement
  -> rescore
```

## Instructor Stance

Keep repeating:

```text
Claude Code collects evidence and proposes improvements.
Engineers make the judgment call.
```

## Safety Boundary

Start every live demo by saying:

```text
This is read-only until I explicitly approve a change.
We are not committing, deploying, or running destructive commands.
```

## Participant Assistant Model

Participants can use the materials in `../claude-teaching-assistant/` to have Claude Code guide them when the instructor is not present.

The default model is:

```text
target repo: inspect only
homework folder: write class artifacts
learning log: visible working journal
patches: optional, branch-based, instructor-approved
```

Use `participant-assistant-workflow.md` for the instructor explanation and review criteria.
