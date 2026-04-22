# Claude Sandboxing

Sandboxing guidance is TBD.

This folder exists because Claude Code execution safety will matter as the course moves from analysis into more autonomous agentic workflows.

## Current Position

Until sandboxing guidance is finalized:

- do not run destructive commands
- do not install global tools without approval
- do not contact external services without approval
- do not execute unknown scripts without inspecting them
- do not copy secrets into coursework artifacts
- do not let Claude operate unattended in sensitive repositories

## Questions To Resolve

- Where should Claude Code run for participant project work?
- Are local desktops acceptable for analysis-only work?
- When is an isolated server or container required?
- What network access is allowed?
- What credentials should be unavailable to Claude?
- How should generated commands be reviewed before execution?
- What logs should be kept for auditability?

## Future Output

Expected future artifacts:

- sandboxing decision matrix
- approved execution environments
- command review checklist
- secrets handling checklist
- safe autonomy levels
- instructor demo environment setup

