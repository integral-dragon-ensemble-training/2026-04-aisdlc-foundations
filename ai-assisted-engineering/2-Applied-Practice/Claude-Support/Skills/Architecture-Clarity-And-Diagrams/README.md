# Architecture Clarity And Diagrams

This documents the architecture diagram skill used by Applied Practice.

The canonical Ensemble-side skill is expected at:

```text
aisdlc-resources/skills/AISDLC-tech-diagrams/
```

The local Dex equivalent is `justin-tech-diagrams`.

## Purpose

This skill should help participants use Claude Code to make architecture visible enough to discuss and improve.

Expected behavior:

- identify major components
- identify entry points
- identify boundaries and responsibilities
- trace dependency direction
- name integration points
- separate evidence from inference
- name uncertainty explicitly
- produce a current-state architecture summary
- recommend a lightweight diagram
- avoid inventing architecture that is not supported by repo evidence

## Workshop 1 Use

Workshop 1 uses this skill during the architecture clarity deep dive.

The goal is not a polished diagram. The goal is a shared map that lets engineers reason about where change belongs and where risk may hide.

## Ensemble Setup

When deploying the course support material into Ensemble:

- verify `aisdlc-resources/skills/AISDLC-tech-diagrams/` exists
- verify the skill has a `SKILL.md` or equivalent instruction entrypoint
- install or register that skill in the Ensemble Claude Code environment before the Workshop 1 demo
- verify diagram rendering dependencies if the skill exports images

Do not duplicate the full skill content into this support folder unless the instructor explicitly asks for a copy. Treat the ADO skill location as canonical.

## Verification Prompt

Ask Ensemble Claude:

```text
Verify that the architecture diagram skill exists at aisdlc-resources/skills/AISDLC-tech-diagrams/.
Confirm the skill entrypoint file, summarize what it does, and tell me whether it is installed or only present on disk.
Do not modify it unless I ask.
```
