# Reading and Resources

## Session 11

## Parallel Orchestration: Agent Teams

Verified on 2026-04-13. Primary sources are prioritized.

### Core references

- Claude Code Docs, Orchestrate teams of Claude Code sessions
  https://code.claude.com/docs/en/agent-teams
  Why it matters: official guide for when to use agent teams, how they differ from subagents, how shared tasks and teammate messaging work, and which best practices matter most.

- Claude Code Docs, Create custom subagents
  https://code.claude.com/docs/en/sub-agents
  Why it matters: useful for making the architectural comparison clear, since Session 11 explicitly depends on understanding where subagents stop and agent teams begin.

- Claude Code Docs, Manage costs effectively
  https://code.claude.com/docs/en/costs
  Why it matters: the current Anthropic docs explicitly call out agent team token costs, recommend small teams, and explain why extra coordination should be reserved for work with real parallel value.

### Strongly recommended

- Claude Code Docs, Settings
  https://code.claude.com/docs/en/settings
  Why it matters: clarifies where environment flags, teammate display settings, and shared configuration live.

- Claude Code Docs, Hooks reference
  https://code.claude.com/docs/en/hooks
  Why it matters: useful because current agent team docs explicitly support hook-based quality gates around teammate idle, task creation, and task completion events.

### Suggested follow-through

Take one candidate task from your environment and answer:

- Does this work have enough independent parallel tracks to justify a team?
- What is the smallest useful team that could handle it?
- What coordination or permission risk would increase the fastest if you added more teammates?
