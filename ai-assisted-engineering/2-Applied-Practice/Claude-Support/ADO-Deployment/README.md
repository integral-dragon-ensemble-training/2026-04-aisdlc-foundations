# ADO Deployment

Instructions for the Claude Code instance running inside Ensemble to deploy course-facing material from this GitHub repository into the Azure DevOps repositories.

## Target ADO Repositories

```text
ai-sdlc-resources/
course-work/
```

## Target Layout

`ai-sdlc-resources` is the main course resource repository.

Deploy participant-facing course support material there:

```text
ai-sdlc-resources/
  2-Applied-Practice/
    Claude-Support/
    Workshop-1-What-Good-Looks-Like-Expanded/
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

