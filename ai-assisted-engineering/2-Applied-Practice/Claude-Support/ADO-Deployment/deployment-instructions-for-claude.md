# Deployment Instructions For Ensemble Claude

You are running inside Ensemble and have access to the Azure DevOps repositories.

Your job is to copy approved course-facing material from the GitHub-sourced course repository into the ADO repositories without deploying instructor-private or internal-only content.

## Inputs To Confirm First

Ask the instructor for:

1. Local path to the pulled GitHub course repository.
2. Local path to the `aisdlc-resources` ADO repository.
3. Local path to the `course-work` ADO repository.
4. Whether `course-work-exercises` exists as a required folder in `course-work`.
5. Whether you should commit only, or commit and push.

Do not copy anything until these paths are confirmed.

## First Verification

Before copying course support material, verify the architecture skill:

```text
aisdlc-resources/skills/AISDLC-tech-diagrams/
```

Report whether:

- the folder exists
- it has a `SKILL.md` or equivalent entrypoint
- Claude Code can use it as an installed skill or only as a checked-in resource
- any rendering dependencies are missing

## Source Path

The expected source inside the GitHub course repository is:

```text
ai-assisted-engineering/2-Applied-Practice/
```

## Destination 1: aisdlc-resources

Copy participant-facing Applied Practice support into:

```text
aisdlc-resources/2-Applied-Practice/
```

Also verify the existing architecture skill:

```text
aisdlc-resources/skills/AISDLC-tech-diagrams/
```

Do not overwrite that skill from this source repository unless explicitly instructed.

Approved folders to copy:

```text
Claude-Support/
Workshop-1-What-Good-Looks-Like-Expanded/
Workshop-2-Technical-Debt-as-Friction-Expanded/
Workshop-3-Using-AI-to-Inspect-and-Improve-Expanded/
Workshop-4-Validation-Tests-Observability-Security-Expanded/
Workshop-5-Making-It-Repeatable-Expanded/
overview/
```

When copying `Workshop-1-What-Good-Looks-Like-Expanded/`, exclude:

```text
_instructor-cheat-sheet/
```

When copying `Claude-Support/`, include:

```text
ADO-Deployment/
Branching-And-Group-Review/
Claude-Sandboxing/
Skills/
README.md
```

## Destination 2: course-work

Use this participant work convention:

```text
course-work/
  participant-work/
    <FirstName LastName>/
      workshop-1-what-good-looks-like/
```

Do not pre-create participant folders unless the instructor asks you to.

If the instructor asks for a starter exercise copy, copy only the participant-facing starter materials into the relevant participant folder or into the approved `course-work-exercises` location.

Recommended starter material:

```text
Claude-Support/Skills/Claude-Teaching-Assistant/participant-startup-prompt.md
Claude-Support/Skills/Claude-Teaching-Assistant/artifact-checklist.md
Claude-Support/Skills/Claude-Teaching-Assistant/templates/
Claude-Support/Branching-And-Group-Review/README.md
Workshop-1-What-Good-Looks-Like-Expanded/exercises/
Workshop-1-What-Good-Looks-Like-Expanded/resources/
```

## Exclusion Rules

Never copy these to ADO unless the instructor explicitly overrides:

```text
_pipeline/
_overview-internal/
_template/
_instructor-cheat-sheet/
__research/
.git/
.DS_Store
**/.DS_Store
~$*.docx
~$*.pptx
~$*.xlsx
```

Also do not copy:

- secrets
- credentials
- private instructor notes
- raw research source files
- local machine paths
- unreviewed temporary files
- model scratchpads or hidden logs

## Positive Proof Required

After copying, report:

- source repository path used
- destination `aisdlc-resources` path used
- destination `course-work` path used
- exact folders copied
- exact folders excluded
- whether `course-work-exercises` exists
- git status for each ADO repo
- commit hash if committed
- push result if pushed
- anything not verified

## Suggested Copy Strategy

Use a dry-run first when possible.

Prefer explicit copy commands over broad syncs. If using `rsync`, use explicit excludes:

```bash
rsync -av --delete \
  --exclude '.git/' \
  --exclude '.DS_Store' \
  --exclude '**/.DS_Store' \
  --exclude '_pipeline/' \
  --exclude '_overview-internal/' \
  --exclude '_template/' \
  --exclude '_instructor-cheat-sheet/' \
  --exclude '__research/' \
  --exclude '~$*.docx' \
  --exclude '~$*.pptx' \
  --exclude '~$*.xlsx' \
  "<source>/Claude-Support/" \
  "<aisdlc-resources>/2-Applied-Practice/Claude-Support/"
```

Do not run this blindly. Replace paths after confirmation.
