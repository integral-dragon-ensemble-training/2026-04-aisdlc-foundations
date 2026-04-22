# Prompt Blocks

Use these as standalone copy/paste blocks during live instruction.

## Boundary Prompt

```text
We are doing an AI-SDLC training exercise.

Do not modify files until I explicitly say APPLY.
Do not commit.
Do not run destructive commands.
Do not install global tools.
Do not call external services unless I approve it.

First inspect, explain, and propose.
Confirm and wait.
```

## Baseline Scorecard Prompt

```text
Use the Repository Health Scorecard skill.

Run a read-only scan and produce a proposed scorecard.

For each category:
- cite concrete evidence by path
- propose a score from 1 to 5
- explain the score
- name uncertainty
- suggest one small improvement if weak

Do not write files yet.
```

## Architecture Clarity Prompt

```text
Focus on architecture clarity and boundaries.

Use the architecture or diagramming skill if available.

Identify major components, entry points, boundaries, dependency directions, integration points, and unclear ownership.
Separate evidence from inference.
Name uncertainty.
Propose one lightweight architecture artifact that would help a new engineer.

Do not write files yet.
```

## Reproducible Setup Prompt

```text
Focus on reproducible developer setup.

Inspect README files, scripts, package manifests, lockfiles, tool versions, Docker/devcontainer files, CI workflows, and environment variable docs.

Do not install global tools or mutate the machine.

Produce the documented setup path, inferred setup path, missing assumptions, safe validation commands, and one small improvement.
```

## Testing Confidence Prompt

```text
Focus on testing confidence.

Inventory test frameworks, test folders, test commands, CI test steps, fixture patterns, and visible coverage or quality signals.

Distinguish coverage from confidence.
Identify protected behavior, unprotected behavior, brittle tests, shallow tests, and candidate lockdown tests.

Recommend one small lockdown test.
Do not write code yet.
```

## Improvement Options Prompt

```text
Based on the baseline scorecard and focused findings, propose three small improvement options.

For each option:
- category improved
- files likely touched
- expected benefit
- validation method
- risk

Recommend one option.
Do not apply it yet.
```

## Apply Prompt

```text
APPLY the selected improvement.

Keep the diff small.
Preserve existing behavior unless we explicitly agreed to change it.
Run the narrowest relevant validation.
Show positive proof of what changed and what was verified.
Do not commit.
```

## Rescore Prompt

```text
Rerun the Repository Health Scorecard for the affected category.

Compare baseline score, new proposed score, concrete evidence that changed, uncertainty that remains, and next recommended action.

Show the delta before writing files.
```

