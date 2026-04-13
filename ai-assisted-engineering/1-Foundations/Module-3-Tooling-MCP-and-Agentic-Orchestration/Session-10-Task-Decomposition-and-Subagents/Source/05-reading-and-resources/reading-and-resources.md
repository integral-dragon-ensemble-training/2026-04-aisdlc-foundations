# Reading and Resources

## Session 10

## Task Decomposition and Subagents

Verified on 2026-04-10. Primary sources are prioritized.

### Core references

- Claude Code Docs, Create custom subagents
  https://code.claude.com/docs/en/sub-agents
  Why it matters: official reference for creating subagents, choosing scope, restricting tools, loading skills, and deciding when subagents are a better fit than the main conversation.

- Claude Code Docs, Settings
  https://code.claude.com/docs/en/settings
  Why it matters: documents where subagents live by scope and how project-shared versus user-local configuration should be managed.

- Claude Code Docs, Common workflows
  https://code.claude.com/docs/en/tutorials
  Why it matters: useful for grounding decomposition in real development tasks such as codebase understanding, debugging, refactoring, and test-writing.

### Strongly recommended

- Claude Code Docs, Hooks reference
  https://code.claude.com/docs/en/hooks
  Why it matters: helpful for understanding that subagents can carry their own hooks and that the main session can also respond to subagent start and stop events.

- Claude Code Docs, Overview
  https://code.claude.com/docs/en/overview
  Why it matters: broader framing for how subagents, MCP, permissions, and terminal-native workflows fit into one operating model.

### Suggested follow-through

Take one large work item from your environment and answer:

- Which parts are independent enough to delegate?
- Which part still requires the main conversation because the context is too coupled?
- What is the smallest useful summary each delegated task should return?
