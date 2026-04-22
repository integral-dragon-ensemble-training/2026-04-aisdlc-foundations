# Workshop 1 Expanded Narrative

Workshop 1 starts by changing the question.

The question is not "Can AI write code for us?" The question is "Can AI help us make a codebase easier to understand, change, test, and operate?"

That distinction matters. If a team only uses AI to generate more code, weak project fundamentals become more expensive. The agent writes faster than the team can understand, test, review, or safely deploy. But if the team gives the agent a clear quality target, AI becomes useful for inspection, documentation, test scaffolding, architecture exploration, and incremental cleanup.

The scorecard is the quality target.

Participants begin by turning the Workshop 1 health rubric into a reusable Claude Code instruction or skill. The skill tells Claude Code what to look for across documentation, architecture, reproducible setup, testing confidence, build/release discipline, data discipline, observability, security, and workflow. The goal is not to make Claude Code the judge. The goal is to make Claude Code a structured evidence collector.

The first pass is read-only. Claude Code inspects the repository, identifies visible artifacts, names uncertainty, and drafts a baseline scorecard. Participants then review the evidence and adjust the scores. This is where the instructor reinforces the central behavior: trust evidence, not fluency.

Once the baseline exists, the workshop becomes practical.

For architecture clarity, participants use Claude Code and the architecture or diagramming skill to produce a current-state map. The point is not a beautiful diagram. The point is to make responsibilities, boundaries, and confusing dependencies visible enough to discuss. A weak diagram that accurately names uncertainty is more valuable than a polished diagram that invents confidence.

For reproducible setup, participants ask Claude Code to inspect the setup path: README instructions, scripts, lockfiles, tool versions, environment variables, containers, build commands, and hidden assumptions. The question is concrete: could a competent engineer get from clone to useful development state without oral tradition? Claude Code can suggest setup checks, docs updates, bootstrap scripts, or environment validation commands. The team chooses the smallest improvement that reduces repeated friction.

For testing confidence, participants use Claude Code to inspect what tests exist and what confidence they actually provide. The workshop should distinguish coverage from confidence. Participants ask AI to suggest missing behavior tests and lockdown tests. Lockdown tests are characterization tests that protect current known behavior before refactoring. They are especially useful in brownfield systems where the team needs safety before cleanup.

After those focused scans, participants pick one weak area. They do not try to fix the whole repo. They use Claude Code to propose a small improvement, review the proposal, apply the change, and rerun the scorecard. The rescore matters because it shifts the conversation from opinions to visible progress.

The workshop ends with a before/after artifact:

- baseline scorecard
- evidence behind the lowest scores
- one selected improvement
- rescore delta
- remaining risks and next actions

This sets up the rest of Applied Practice. Workshop 2 can take the weak areas and frame them as friction and technical debt. Workshop 3 can teach deeper AI inspection and improvement workflows. Workshop 4 can harden validation, observability, security, and governance. Workshop 5 can turn the loop into a repeatable team operating practice.

The instructor message is:

```text
We are not using AI to skip engineering judgment.
We are using AI to make the evidence visible faster,
so engineers can make better decisions and improve the repo in smaller, safer steps.
```

