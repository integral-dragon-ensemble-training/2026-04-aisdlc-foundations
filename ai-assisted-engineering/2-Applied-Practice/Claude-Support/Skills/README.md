# Claude Skills

Shared Claude Code skills and skill-like instruction packages for Applied Practice.

## Current Skills

```text
Skills/
  Claude-Teaching-Assistant/
  Architecture-Clarity-And-Diagrams/
```

## Claude Teaching Assistant

`Claude-Teaching-Assistant/` guides participants through the Workshop 1 loop:

- collect setup details
- create coursework workspace
- create participant target-repo branch
- run scorecard workflow
- maintain learning log
- prepare group review packet

## Architecture Clarity And Diagrams

`Architecture-Clarity-And-Diagrams/` documents the architecture diagram skill dependency.

The canonical Ensemble-side skill is expected at:

```text
aisdlc-resources/skills/AISDLC-tech-diagrams/
```

The local Dex equivalent is `justin-tech-diagrams`.

## Skill Packaging Rule

Each skill folder should include:

- `SKILL.md` for the core instruction
- `README.md` for human orientation
- optional templates, examples, or prompt blocks
