# Claude Support

This folder holds shared Claude Code support material for Applied Practice.

It is intentionally not workshop-specific. Workshop folders can point here instead of carrying duplicate support instructions.

## Folder Map

```text
Claude-Support/
  README.md
  ADO-Deployment/
    README.md
    deployment-instructions-for-claude.md
    export-map.md
  Skills/
    README.md
    Claude-Teaching-Assistant/
    Architecture-Clarity-And-Diagrams/
  Branching-And-Group-Review/
    README.md
  Claude-Sandboxing/
    README.md
```

## Current Support Areas

- `Skills/Claude-Teaching-Assistant/` contains the reusable participant assistant skill for guided workshop work.
- `Skills/Architecture-Clarity-And-Diagrams/` documents the architecture diagram skill dependency.
- `Branching-And-Group-Review/` defines the participant branch and team review model.
- `Claude-Sandboxing/` is a placeholder for sandboxing and execution-environment guidance.
- `ADO-Deployment/` tells the Ensemble-side Claude how to deploy approved material to ADO.

## Operating Model

The current Applied Practice model is:

```text
course-work/participant-work/<FirstName LastName>
  + participant branch in target repo
  + no merge during individual work
  + group review before adoption
```

Participants use Claude Code to inspect and improve real project repositories, but the output is staged:

- coursework artifacts go into `course-work/participant-work/<FirstName LastName>/`
- candidate code or docs changes go onto the participant branch
- team decisions happen later in group review
- production branches are not updated automatically

## ADO Repositories

Expected ADO destinations:

```text
aisdlc-resources/
course-work/
```

`aisdlc-resources` gets course-facing resources.

`course-work` gets participant work under:

```text
course-work/participant-work/<FirstName LastName>/
```

The architecture diagram skill is expected to already exist in ADO at:

```text
aisdlc-resources/skills/AISDLC-tech-diagrams/
```

## Naming

Use `Claude Support`, not `cloud support`.

Use non-underscore folders for participant-facing support material. Keep underscore prefixes for private/internal instructor or pipeline material.
