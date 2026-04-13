# Reading and Resources

## Session 06

## Plan Mode vs. Act Mode

Verified on 2026-04-09. Primary sources are prioritized.

### Core references

- Anthropic, Claude Code common workflows
  https://code.claude.com/docs/en/tutorials
  Why it matters: Anthropic's current workflow guide explicitly describes Plan Mode as read-only analysis for exploring codebases, planning complex changes, and safe review. It also gives the canonical startup command and examples.

- Anthropic, Configure permissions
  https://code.claude.com/docs/en/permissions
  Why it matters: documents the current permission-mode set and clarifies that `plan` is one mode inside a broader permissions model. Useful for keeping the course technically current without collapsing the teaching model into product trivia.

- Anthropic, Claude Code settings
  https://code.claude.com/docs/en/settings
  Why it matters: shows how `defaultMode`, `CLAUDE.md`, project settings, managed settings, and plans directory settings interact. Important for enterprise framing and for the bridge into Session 07.

### Strongly recommended

- Anthropic, Claude Code overview
  https://code.claude.com/docs/en/overview
  Why it matters: useful high-level framing for why terminal-native workflows, MCP, hooks, and permissions belong in one operational system.

- Addy Osmani, "Vibe coding is not the same as AI-Assisted engineering"
  https://medium.com/@addyosmani/vibe-coding-is-not-the-same-as-ai-assisted-engineering-3f81088d5b98
  Why it matters: sharp language for why execution without review discipline becomes operational debt.

### Suggested follow-through

Read the Anthropic workflow page and answer these questions:

- Which of your real tasks should default to Plan Mode?
- Which tasks are small enough to execute directly?
- What approval questions would your team want answered before the first edit is allowed?
