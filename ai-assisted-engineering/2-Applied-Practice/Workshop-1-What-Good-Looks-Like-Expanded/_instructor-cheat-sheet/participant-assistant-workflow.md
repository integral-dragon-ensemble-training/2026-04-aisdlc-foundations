# Participant Claude Teaching Assistant Workflow

This explains the participant-facing Claude assistant model.

## What Is Happening

Participants will use Claude Code as a guided teaching assistant while they work through Workshop 1.

Claude's role is to:

- explain the workflow
- ask for the target repo
- create a participant workspace
- walk the participant through each step
- provide copy/paste prompts when needed
- keep the target project safe by default
- maintain a visible learning log
- help produce artifacts you can review

## Recommended Operating Model

Default to artifact-only work.

Participants inspect a target repo, but their workshop outputs live in a separate homework/workspace folder.

Recommended participant workspace:

```text
<homework-root>/
  participants/
    <first-last-kebab>/
      workshop-1-what-good-looks-like/
```

This avoids filling production repos with early training artifacts while still giving you something consistent to review.

## Target Repo Branch Advice

Do not make target repo branches mandatory.

Use this default:

- analysis artifacts go into the homework folder
- target repo remains read-only
- patch work is optional and instructor-approved

If a patch is allowed, use:

```text
workshop-1-what-good-looks-like/<first-last-kebab>
```

Even then, the participant should copy the branch name, diff summary, validation, and rescore delta back into the homework folder.

## Learning Log Positioning

Use a visible learning log, not hidden time tracking.

The log should capture:

- timestamped work entries
- what the participant attempted
- what Claude helped with
- artifacts created
- decisions made
- blockers and uncertainty
- next step

This gives you enough signal to evaluate engagement and understanding. It also helps participants resume work without losing context.

Suggested framing:

```text
Claude will keep a short learning log so you can resume your work and so I can see where the class needs more support.
```

Avoid framing it as surveillance. Also do not hide that it includes timestamps.

## What Might Not Work

Several risks need management:

- Participants may let Claude score without reviewing evidence.
- Participants may accidentally write artifacts into the target repo.
- Participants may produce polished but unsupported analysis.
- Some target repos may be too locked down for local inspection.
- Sensitive repos may require redaction rules before artifacts are copied.
- Patch work can distract from the core learning loop.

## Instructor Checks

When reviewing participant work, look for:

- target repo and access mode are clear
- learning log has enough entries to reconstruct the work
- scores cite concrete evidence
- uncertainty is named
- one weak area is selected deliberately
- improvement is small and reviewable
- rescore delta explains what changed and what remains unproven

## Recommended Instructor Explanation

Use this short explanation:

```text
You are going to use Claude Code as a teaching assistant, not as an answer machine.

It will help you inspect the repo, collect evidence, and generate prompts for the next step.
Your job is to review the evidence, make the scoring decision, and choose a small improvement.

Keep your work in your class workspace, not in the production repo by default.
Claude will keep a short learning log so you can resume work and so I can see where the class needs more support.
```

