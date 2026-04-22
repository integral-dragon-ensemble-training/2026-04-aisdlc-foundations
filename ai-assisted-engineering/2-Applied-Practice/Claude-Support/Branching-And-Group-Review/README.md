# Branching And Group Review

This defines the Applied Practice branch model for participant work.

## Default Flow

```text
target repo main branch
  -> participant branch
  -> individual Claude-assisted work
  -> course-work/participant-work/<FirstName LastName> artifacts
  -> group review
  -> selected changes merged later through normal team process
```

## Branch Name

Use:

```text
workshop-1-what-good-looks-like/<first-last-kebab>
```

Examples:

```text
workshop-1-what-good-looks-like/jane-smith
workshop-1-what-good-looks-like/carlos-rivera
```

## Rules

- Each participant uses their own branch.
- Participants may take different approaches.
- Branches are candidate work areas, not merge instructions.
- Do not merge into production, main, develop, or a real feature branch during individual work.
- Do not push unless the instructor and team process allow it.
- Preserve a coursework copy of the branch summary, validation results, and rescore delta under `course-work/participant-work/<FirstName LastName>/`.

## Why This Model

Multiple engineers may inspect the same project and reach different conclusions.

That is useful. The course should teach both:

- individual AI-assisted analysis and improvement
- group decision-making about what should become real project practice

## Group Review Packet

Each participant should bring:

- target repo and branch name
- baseline scorecard
- top weak areas
- one selected improvement
- files changed or proposed
- validation run
- rescore delta
- recommendation: merge, revise, or discard
- open questions for the team

## Group Review Decision

As a team, decide:

- which findings are shared across participants
- which branch contains useful work
- which ideas should be merged, rewritten, or dropped
- what needs security, architecture, or manager review
- what should become backlog work
- what the new team score is after selected changes
