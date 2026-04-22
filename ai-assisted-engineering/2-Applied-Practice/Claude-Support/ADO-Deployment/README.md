# ADO Deployment

Instructions for the Claude Code instance running inside Ensemble to deploy course-facing material from this GitHub repository into the Azure DevOps repositories.

## Target ADO Repositories

```text
aisdlc-resources/
course-work/
```

## Primary Handoff

After pulling this GitHub repository inside Ensemble, give the Ensemble-side Claude:

```text
Claude-Support/ADO-Deployment/post-pull-handoff-for-ensemble-claude.md
```

## Target Layout

`aisdlc-resources` is the main course resource repository.

Deploy participant-facing course support material there:

```text
aisdlc-resources/
  2-Applied-Practice/
    Claude-Support/
    Workshop-1-What-Good-Looks-Like-Expanded/
  skills/
    AISDLC-tech-diagrams/
```

`course-work` is the participant work repository.

Participant work should live under:

```text
course-work/
  participant-work/
    <FirstName LastName>/
      workshop-1-what-good-looks-like/
```

The participant display folder should use the participant's first and last name. Branch names should still use lowercase kebab-case:

```text
workshop-1-what-good-looks-like/<first-last-kebab>
```

## Existing Skill Dependency

The architecture diagram skill should already be present in ADO:

```text
aisdlc-resources/skills/AISDLC-tech-diagrams/
```

Deployment should verify it exists and is installable. Do not overwrite it from this source repo unless explicitly instructed.

## Internal-Only Material

Do not deploy internal-only material to ADO.

Keep these local to the instructor laptop or the private GitHub source repo unless explicitly approved:

- `_pipeline/`
- `_overview-internal/`
- `_template/`
- `_instructor-cheat-sheet/`
- `__research/`
- generated temp files
- `.DS_Store`
- Office lock files like `~$*.docx`
- any file containing secrets, credentials, private notes, or unreviewed research source material

## Deployment Principle

Deploy only what participants or the Ensemble-side Claude assistant need.

If a file is mainly for instructor planning, provenance, source reconstruction, private prompting, or internal delivery operations, do not copy it to ADO.
