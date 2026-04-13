# Reading and Resources

## Session 14

## Secure MCP Governance

Verified on 2026-04-13. Primary sources are prioritized.

### Core references

- Claude Code Docs, Connect Claude Code to tools via MCP
  https://code.claude.com/docs/en/mcp
  Why it matters: current Anthropic guidance on MCP setup, server configuration, and the basic workflow for connecting tools to Claude Code.

- Claude Code Docs, Permissions
  https://code.claude.com/docs/en/permissions
  Why it matters: explains how permission modes fit into the broader control model and why approval and scope are not the same thing as trust.

- Claude Code Docs, Security
  https://code.claude.com/docs/en/security
  Why it matters: documents Anthropic’s current security framing, including why external systems and tool access require explicit care.

### Strongly recommended

- Model Context Protocol, Authorization
  https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
  Why it matters: defines the authorization layer that should exist when an MCP server exposes sensitive capabilities.

- Model Context Protocol, Security best practices
  https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
  Why it matters: highlights practical controls for securing MCP integrations, with emphasis on minimizing trust and protecting data boundaries.

- NIST SP 800-207, Zero Trust Architecture
  https://csrc.nist.gov/pubs/sp/800/207/final
  Why it matters: provides the architectural framing for treating the MCP server as a protected resource rather than assuming internal placement equals safety.

### Suggested follow-through

Review one candidate MCP integration in your environment and answer:

- What is the smallest safe scope to expose first?
- What should remain read-only until a later phase?
- What logging and ownership data would security or platform engineering require before approval?
