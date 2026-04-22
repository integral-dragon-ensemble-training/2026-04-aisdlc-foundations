# Claude Teaching Assistant Package

This folder contains instructions participants can give to Claude Code so it can act as a guided teaching assistant for Workshop 1.

The assistant's job is not to do the assignment for the participant. Its job is to:

- explain the workflow
- ask for the target repository
- create a participant workspace
- guide the participant through the scorecard loop
- keep work products outside the production project by default
- maintain a transparent learning log
- nudge the participant forward when they get stuck

## Files

```text
Claude-Teaching-Assistant/
  README.md
  SKILL.md
  participant-startup-prompt.md
  workspace-model.md
  artifact-checklist.md
  templates/
    learning-log-template.md
    target-repo-profile-template.md
    workshop-1-workspace-readme-template.md
```

## Recommended Use

Participants should start Claude Code from the target repository working copy when possible. They should also provide the local `course-work` repository path where all class artifacts will be written.

They should paste:

```text
participant-startup-prompt.md
```

Claude should then ask for:

- participant first and last name
- target repository path or URL
- coursework root directory, expected to be the local `course-work` repository
- whether Claude may create the participant branch
- whether any security or confidentiality constraints apply

## Default Safety Model

Default mode is coursework workspace plus participant target branch:

- inspect the target repo
- write all class artifacts to `course-work/participant-work/<FirstName LastName>/`
- create or request a participant branch before candidate changes
- do not merge into the production branch
- do not push unless explicitly approved

All branch summaries, diffs, validation results, and rescore deltas still get copied back into the participant coursework folder.

Recommended branch name:

```text
workshop-1-what-good-looks-like/<first-last-kebab>
```

## Transparency Note

The learning log is intentionally visible. Do not hide that it exists.

It is framed as a working journal:

- what the participant tried
- what Claude helped with
- what artifacts were produced
- what decisions were made
- what remains confusing

This gives the instructor enough signal to see whether the participant is engaging and understanding the material without turning the exercise into covert monitoring.

## Group Review Model

Multiple participants on the same team may produce different branches and different improvement proposals.

That is intentional. The team should compare the candidate branches and coursework artifacts, decide which ideas are actually worth merging, and then rescore together.
