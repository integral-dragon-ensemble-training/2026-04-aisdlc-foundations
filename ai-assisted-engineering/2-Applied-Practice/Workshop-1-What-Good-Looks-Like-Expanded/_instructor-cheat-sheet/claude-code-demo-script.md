# Claude Code Demo Script

This is the instructor-run demo. It is designed to be copied into Claude Code in stages.

## Setup

Choose a repo that is safe to inspect and modify lightly.

Recommended starting conditions:

- use a training repo or non-production branch
- avoid secrets and sensitive data
- start from a clean git status if possible
- decide ahead of time whether edits are allowed
- do not commit during the demo unless that is explicitly part of the lesson

## Talk Track

Use this framing:

```text
I am going to show you the loop we want you to practice.

First, I am not going to ask Claude Code whether this repo is good.
That is too vague.

I am going to give it a scorecard, make it collect evidence, review the evidence myself,
then choose one improvement and measure again.
```

## Step 1 - Establish Read-Only Boundary

Paste into Claude Code:

```text
We are doing a live AI-SDLC training demo.

Safety boundary:
- Do not modify files until I explicitly say APPLY.
- Do not commit anything.
- Do not run destructive commands.
- Do not install global tools.
- Do not contact external services unless I approve it.
- First, inspect and propose.

Confirm you understand the boundary, then wait.
```

## Step 2 - Create The Scorecard Skill

Paste:

```text
Create a repo-local Repository Health Scorecard skill or instruction file.

If this repo already has a Claude Code skill convention, use it.
If not, create docs/ai-sdlc/repository-health-scorecard-skill.md.

Use the content I will provide next.
Do not scan the repo yet.
After creating the file, summarize where you placed it and wait.
```

Then paste the contents of:

```text
Workshop-1-What-Good-Looks-Like-Expanded/resources/repository-health-scorecard-skill.md
```

Instructor line:

```text
Notice that I am not asking for a vibe check. I am giving the tool a standard.
```

## Step 3 - Run Baseline Scan

Paste:

```text
Use the Repository Health Scorecard skill.

Run a read-only baseline scan of this repository.

For each category:
- inspect concrete repo artifacts
- cite paths
- propose a score from 1 to 5
- explain the score
- name uncertainty
- suggest one small improvement if weak

Do not write files yet. Show me the proposed scorecard first.
```

Instructor line:

```text
This is where I review the evidence. If the evidence is weak, the score is weak.
```

If the draft is acceptable, paste:

```text
Write the reviewed baseline scorecard to docs/ai-sdlc/repo-health/baseline-scorecard.md.
```

## Step 4 - Architecture Clarity Deep Dive

Paste:

```text
Now focus only on Architecture clarity and boundaries.

Use the architecture analysis or diagramming skill if available.

Analyze:
- major components
- entry points
- module boundaries
- dependency direction
- integration points
- unclear ownership or responsibilities

Separate evidence from inference.
Name uncertainty.

Propose one lightweight current-state architecture diagram and one small docs improvement.
Do not write files yet.
```

Instructor line:

```text
The goal is not a perfect diagram. The goal is a shared map that is honest about uncertainty.
```

Optional apply:

```text
APPLY the smallest architecture clarity improvement.

Keep it documentation-only unless you explain why a code change is required.
Store the artifact under docs/architecture/.
Report exactly what changed.
```

## Step 5 - Reproducible Setup Deep Dive

Paste:

```text
Now focus only on Reproducible developer setup.

Inspect:
- README setup instructions
- scripts
- package manifests
- lockfiles
- tool versions
- Docker/devcontainer files
- CI setup commands
- environment variable documentation

Do not install global tools.
Do not mutate the machine.

Produce:
- documented setup path
- inferred setup path
- missing assumptions
- safe validation commands
- one small improvement that would reduce setup friction

Do not write files yet.
```

Optional apply:

```text
APPLY the smallest setup clarity improvement.

Prefer docs, env template, or validation command.
Keep the diff small.
Run only safe validation commands.
Report positive proof of what was verified.
```

## Step 6 - Testing Confidence And Lockdown Tests

Paste:

```text
Now focus only on Testability and quality confidence.

Inspect:
- test framework
- test folders
- test commands
- CI test steps
- fixture and test data patterns
- visible coverage or quality signals

Distinguish test coverage from real confidence.

Identify:
- important behavior that appears protected
- important behavior that appears unprotected
- brittle or shallow tests
- candidate lockdown tests for current behavior before refactoring

Recommend one small lockdown test.
Do not write code yet.
```

Optional apply:

```text
APPLY the smallest recommended lockdown test.

Keep it minimal.
Avoid refactoring production code unless a tiny seam is necessary.
Run the narrowest relevant test command.
Report what passed, failed, and remains unproven.
```

## Step 7 - Rerun The Scorecard

Paste:

```text
Rerun the Repository Health Scorecard for only the categories affected by our changes.

Compare:
- original score
- new proposed score
- concrete evidence that changed
- uncertainty that remains
- next recommended improvement

Show me the delta first.
Do not overwrite the baseline.
```

If acceptable:

```text
Write the rescore delta to docs/ai-sdlc/repo-health/rescore-delta.md.
```

## Closing Talk Track

```text
The important thing is not that Claude Code produced a score.
The important thing is that we now have a repeatable loop:
define the quality target, collect evidence, improve one weak area, validate, and score again.
```

