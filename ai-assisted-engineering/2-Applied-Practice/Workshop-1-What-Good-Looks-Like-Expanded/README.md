# Workshop 1 Expanded - What Good Looks Like

This expanded version preserves the original Workshop 1 as the baseline and turns it into a hands-on Claude Code workflow.

The central teaching move is simple:

1. Give Claude Code a structured definition of "what good looks like."
2. Use it to inspect a real codebase and collect evidence.
3. Let humans make the scoring judgment.
4. Pick one weak area and improve it with AI assistance.
5. Rerun the scorecard to see whether the improvement changed the repo, not just the conversation.

## Folder Map

```text
Workshop-1-What-Good-Looks-Like-Expanded/
  README.md
  000-expansion-map.md
  narrative/
    workshop-1-expanded-narrative.md
  exercises/
    010-create-scorecard-skill.md
    020-baseline-repository-health-scan.md
    030-architecture-clarity-and-diagrams.md
    040-reproducible-setup-check.md
    050-testing-confidence-and-lockdown-tests.md
    060-improvement-loop-and-rescore.md
  resources/
    repository-health-scorecard-skill.md
    repo-health-scorecard-template.md
    workshop-1-expanded-flow.excalidraw
    workshop-1-expanded-flow-talk-track.md
  _instructor-cheat-sheet/
    README.md
    claude-code-demo-script.md
    participant-assistant-workflow.md
    prompt-blocks.md
```

## Workshop Thesis

AI coding tools do not remove the need for engineering quality. They increase the payoff from having a clear quality target.

In this workshop, participants learn to use Claude Code as an evidence-gathering and improvement partner. The scorecard gives Claude Code a frame. Claude Code helps inspect architecture, setup, tests, and change safety. The engineer decides what matters, applies judgment, and chooses what to improve.

## Expanded Learning Arc

The short version of Workshop 1 was a scorecard exercise. The expanded version becomes a repeatable loop:

```text
define quality target
  -> create scorecard skill
  -> inspect repository evidence
  -> score with human review
  -> pick a weak area
  -> use AI to improve one thing
  -> rerun the scorecard
  -> capture the delta
```

## Claude Teaching Assistant

The reusable participant-facing Claude assistant now lives in:

```text
ai-assisted-engineering/2-Applied-Practice/Claude-Support/Skills/Claude-Teaching-Assistant/
```

The intended model is:

- participant starts Claude with a target repository and local `course-work` repository
- Claude asks for participant name, target repo, course-work repo path, and safety constraints
- target repo work happens on a participant branch
- class artifacts are written to `course-work/participant-work/<FirstName LastName>/`
- Claude maintains a visible learning log
- nothing is merged until group review

## Recommended Delivery

Use a three-day core workshop, with optional day-four and day-five deepening if the cohort has enough real project access.

- Day 1: create the scorecard skill and run the baseline scan.
- Day 2: focus on architecture clarity and reproducible setup.
- Day 3: focus on testing confidence, lockdown tests, one improvement, and rescore.
- Optional Day 4: project team breakout on their own repositories.
- Optional Day 5: report-out, compare score deltas, and identify next workshop inputs.

## Source Relationship

This folder expands the existing baseline:

- `ai-assisted-engineering/2-Applied-Practice/Workshop-1-What-Good-Looks-Like/`

It does not replace the original workshop. Treat this as the candidate expanded version until it is reviewed and promoted.
