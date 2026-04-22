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
claude-teaching-assistant/
  README.md
  CLAUDE.md
  participant-startup-prompt.md
  workspace-model.md
  artifact-checklist.md
  templates/
    learning-log-template.md
    target-repo-profile-template.md
    workshop-1-workspace-readme-template.md
```

## Recommended Use

Participants should start Claude Code in their homework/workspace repository or directory, not in the production target repo.

They should paste:

```text
participant-startup-prompt.md
```

Claude should then ask for:

- participant first and last name
- target repository path or URL
- homework/workspace root
- whether target repo access is read-only or patch-allowed
- whether any security or confidentiality constraints apply

## Default Safety Model

Default mode is artifact-only:

- inspect the target repo
- write all work products to the participant homework folder
- do not modify the target repo
- do not commit to the target repo
- do not push branches

If patch work is allowed, use a separate branch and still copy the relevant summaries, diffs, and results into the homework folder.

Recommended branch name:

```text
workshop-1-what-good-looks-like/<first-last>
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
