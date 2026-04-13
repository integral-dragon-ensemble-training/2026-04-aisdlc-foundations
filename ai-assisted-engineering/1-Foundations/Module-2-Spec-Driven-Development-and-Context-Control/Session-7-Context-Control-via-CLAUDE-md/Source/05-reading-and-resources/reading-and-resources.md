# Reading and Resources

## Session 07

## Context Control via CLAUDE.md

Verified on 2026-04-10. Primary sources are prioritized.

### Core references

- Anthropic, Claude Code settings
  https://code.claude.com/docs/en/settings
  Why it matters: documents the current scope hierarchy for settings, subagents, MCP servers, plugins, and `CLAUDE.md`, including where user, project, local, and managed controls live.

- Anthropic, Claude Code memory
  https://code.claude.com/docs/en/memory
  Why it matters: explains how Claude Code uses memory files and why stable instructions belong in durable memory rather than repeated prompting.

- Anthropic, Claude Code tutorials
  https://code.claude.com/docs/en/tutorials
  Why it matters: shows real workflow patterns where project rules, plans, and execution work together in the CLI rather than as disconnected prompt tricks.

### Strongly recommended

- Anthropic, Claude Code overview
  https://code.claude.com/docs/en/overview
  Why it matters: useful for framing `CLAUDE.md` as one part of a broader harness that also includes permissions, hooks, MCP, and terminal workflows.

- Addy Osmani, "Comprehension Debt — the hidden cost of AI generated code"
  https://medium.com/@addyosmani/comprehension-debt-the-hidden-cost-of-ai-generated-code-285a25dac57e
  Why it matters: helps explain why persistent project rules matter when teams need outputs that remain reviewable and maintainable over time.

### Suggested follow-through

Review your current repeated prompting habits and answer:

- Which instruction are you repeating often enough that it should become a persistent rule?
- Which rules genuinely need to be shared with the team?
- Which rules are personal preferences that should stay local?
