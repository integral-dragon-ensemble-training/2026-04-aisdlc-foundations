# 040 Reproducible Setup Check

## Objective

Use Claude Code to inspect whether a new engineer could reach a useful development state from the repository alone.

## Key Teaching Point

Reproducibility does not always mean full local production parity. It means the setup path is explicit, bounded, and testable enough for useful development.

## Participant Instructions

1. Ask Claude Code to inspect setup docs, scripts, lockfiles, tool versions, containers, and environment assumptions.
2. Ask it to produce a setup evidence table.
3. Ask for missing or risky assumptions.
4. Pick one small setup improvement.
5. Do not run destructive commands or install global dependencies during the exercise.

## Suggested Claude Code Prompt

```text
Inspect this repository for reproducible developer setup.

Rules:
- Do not install global tools.
- Do not modify files yet.
- Do not run commands that mutate the machine or external services.
- Inspect README files, scripts, package manifests, lockfiles, Docker/devcontainer files, CI workflows, and documented environment variables.

Produce:
1. The documented setup path.
2. The inferred setup path if docs are incomplete.
3. Tool and runtime versions that appear required.
4. Missing environment assumptions.
5. Commands that could safely validate setup.
6. The smallest documentation or automation improvement that would reduce setup friction.

Show the findings before writing anything.
```

## Expected Output

- Setup path summary.
- Tool/version assumptions.
- Missing environment variables or secrets notes.
- Safe validation commands.
- One small improvement proposal.

## Possible Improvements

- Add a `docs/setup.md`.
- Add a prerequisites section to `README.md`.
- Add an environment variable template.
- Add a setup verification script.
- Add a devcontainer proposal.
- Add a clean-machine checklist.

## Scoring Connection

Use the result to revisit the `Reproducible setup` score.

A score should improve only if the setup path becomes more explicit, testable, or easier to repeat.

