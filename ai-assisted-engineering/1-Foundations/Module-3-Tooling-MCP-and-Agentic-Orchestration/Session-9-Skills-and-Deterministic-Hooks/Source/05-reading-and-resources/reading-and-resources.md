# Reading and Resources

## Session 09

## Skills and Deterministic Hooks

Verified on 2026-04-10. Primary sources are prioritized.

### Core references

- Claude Code Docs, Automate workflows with hooks
  https://code.claude.com/docs/en/hooks-guide
  Why it matters: practical quickstart for lifecycle hooks with concrete examples such as notifications, auto-formatting, and protected-file controls.

- Claude Code Docs, Hooks reference
  https://code.claude.com/docs/en/hooks
  Why it matters: documents hook lifecycle events, configuration schema, scope, and the distinction between command, prompt, agent, and HTTP hooks.

- Claude Code Docs, Create custom subagents
  https://code.claude.com/docs/en/sub-agents
  Why it matters: current official docs explicitly describe skills as reusable context that can be loaded into subagents and clarify where skills fit relative to isolated agent execution.

### Strongly recommended

- Claude Code Docs, Settings
  https://code.claude.com/docs/en/settings
  Why it matters: explains scope hierarchy so teams can decide whether a hook belongs in user, project, local, or managed configuration.

- Claude Code Docs, Common workflows
  https://code.claude.com/docs/en/tutorials
  Why it matters: useful broader operational framing for how hooks and extensibility fit into everyday development rather than stand-alone demos.

### Suggested follow-through

Pick one repeated workflow rule in your environment and answer:

- Is this guidance, enforcement, or both?
- If it is mandatory, what is the earliest lifecycle point where a hook should run?
- If it is reusable but not mandatory, should it become a skill instead?
