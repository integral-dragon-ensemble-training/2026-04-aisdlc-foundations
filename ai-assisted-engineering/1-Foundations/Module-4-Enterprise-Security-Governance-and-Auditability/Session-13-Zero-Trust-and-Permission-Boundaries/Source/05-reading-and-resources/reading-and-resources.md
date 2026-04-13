# Reading and Resources

## Session 13

## Zero Trust and Permission Boundaries

Verified on 2026-04-13. Primary sources are prioritized.

### Core references

- Anthropic, Claude Code Security
  https://code.claude.com/docs/en/security
  Why it matters: current official guidance on safe usage, permissioning, and security controls around agentic workflows.

- Anthropic, Claude Code Permissions
  https://code.claude.com/docs/en/permissions
  Why it matters: documents the current permission model and reinforces why scoped approvals matter more than convenience.

- NIST SP 800-207, Zero Trust Architecture
  https://csrc.nist.gov/pubs/sp/800/207/final
  Why it matters: the canonical Zero Trust reference for treating every access path as explicit, bounded, and continuously verified.

### Strongly recommended

- Anthropic, Claude Code Settings
  https://code.claude.com/docs/en/settings
  Why it matters: useful for understanding where project, local, and managed controls live and how permission-related settings are organized.

- Anthropic, Claude Code Overview
  https://code.claude.com/docs/en/overview
  Why it matters: helpful for framing the CLI as a controlled engineering environment, not a conversational toy.

- Anthropic, Claude Code Authentication
  https://code.claude.com/docs/en/iam
  Why it matters: current official documentation for individual, team, and enterprise authentication paths, which is directly relevant when thinking about AI identities, ownership, and access scope.

### Suggested follow-through

Take one agentic workflow and answer:

- What is the narrowest useful permission set?
- Which action would require approval every time?
- Where would you deny access immediately rather than negotiate it?
