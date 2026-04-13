# Practice and Feedback

## Session 11

## Parallel Orchestration: Agent Teams

### In-session practice 01

## Design the team

Take a complex Jira ticket and design a 3-agent team. For each teammate, specify:

- role
- scope boundary
- likely owned files or workstream
- what they should send through the mailbox
- what the lead should review before accepting their work

### In-session practice 02

## Team or subagents?

For each situation below, decide whether to use:

- one main session
- subagents
- an agent team

Situations:

- run three independent review lenses on the same PR
- implement a tiny bugfix with one file change
- investigate a production issue with competing root-cause hypotheses
- refactor one module where all edits land in the same two files

### Discussion prompts

- What kinds of work in your environment would justify the extra cost of agent teams?
- What is the biggest governance risk when teammates can communicate directly?
- When does coordination overhead erase the gain from parallelism?

### Between-session fieldwork

Complete all three:

1. Choose one real work item that might benefit from parallel teammates.
2. Design a team of 3 to 5 roles with explicit boundaries.
3. Identify one reason the same work might still be better with subagents or a single session.

### Submission prompt

Write 6 to 8 sentences answering:

- What specific characteristic of the work makes agent teams worth considering?
- Which teammate role would be most likely to collide with another if the boundaries were weak?
- What would the lead need to monitor closely to keep the team from wasting tokens or drifting?

### Survey questions

- How comfortable are you with multiple AI sessions interacting with one another in the background?
- After this session, how confident are you in deciding when agent teams are justified versus overkill?
- Which concern feels largest in your environment right now: token cost, coordination drift, permissions, or oversight?
