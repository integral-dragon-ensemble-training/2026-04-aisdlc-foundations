# Participant Coursework And Branch Model

This is the recommended structure for participant work.

## Default Structure

```text
<course-work-repo>/
  participant-work/
    <FirstName LastName>/
      workshop-1-what-good-looks-like/
        README.md
        learning-log.md
        target-repo-profile.md
        010-scorecard-skill/
          repository-health-scorecard-skill.md
        020-baseline-scorecard/
          baseline-scorecard.md
        030-architecture-clarity/
          architecture-findings.md
          current-state-diagram.md
        040-reproducible-setup/
          setup-findings.md
        050-testing-confidence/
          testing-confidence-findings.md
          candidate-lockdown-tests.md
        060-improvement-and-rescore/
          improvement-options.md
          selected-improvement.md
          rescore-delta.md
        070-group-review/
          group-review-packet.md
        080-final-reflection/
          reflection.md
```

## Why Keep Coursework Artifacts Outside The Target Repo

Participants should not check workshop artifacts directly into the production project.

Reasons:

- the scorecard is a learning artifact
- early AI output may need review
- target repo teams may have their own contribution process
- the instructor needs a consistent place to review participant work
- analysis artifacts may include uncertainty, drafts, or proposed changes that are not ready for the main project

## Target Repo Branch

Use a target repo branch for candidate project changes.

Recommended branch:

```text
workshop-1-what-good-looks-like/<first-last-kebab>
```

Branch work should still be summarized in the participant coursework folder.

At minimum, copy back:

- branch name
- files changed
- diff summary
- validation run
- what remains unproven
- whether the participant thinks the patch should be proposed to the team

## Instructor Review Surface

The instructor should be able to review `course-work/participant-work/<FirstName LastName>/` and understand:

- what repository was targeted
- what evidence was inspected
- how the participant scored the repo
- where Claude helped
- what the participant accepted, rejected, or changed
- what improvement was attempted
- whether the participant understood the workflow

## Group Review Surface

At group review time, the team should compare:

- participant branches
- baseline scorecards
- proposed changes
- validation results
- rescore deltas
- merge recommendations

Nothing should be merged automatically. The team chooses what belongs in the real project.
