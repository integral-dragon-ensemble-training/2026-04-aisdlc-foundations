# 050 Merge Selection And Rescore

## Objective

Compare participant branches and decide what belongs in the real project.

## Claude Prompt

```text
Prepare a group merge selection packet.

Compare participant branches and artifacts.

For each candidate:
- branch
- change summary
- validation evidence
- risk
- scorecard category affected
- recommendation: merge, revise, backlog, discard

Then propose a team rescore after selected changes.
Do not merge anything.
```

## Output

- group merge selection packet
- team rescore proposal

