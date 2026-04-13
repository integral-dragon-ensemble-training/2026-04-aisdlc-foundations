# Reading and Resources

## Session 08

## Extending Capabilities with MCP

Verified on 2026-04-10. Primary sources are prioritized.

### Core references

- Claude Code Docs, Connect Claude Code to tools via MCP
  https://code.claude.com/docs/en/mcp
  Why it matters: documents the current Claude Code MCP workflow, configuration model, and operational patterns for adding servers and using tool-connected capabilities.

- Model Context Protocol, Introduction
  https://modelcontextprotocol.io/docs/getting-started/intro
  Why it matters: official high-level explanation of MCP as an open protocol for connecting models to tools, resources, and prompts.

- Model Context Protocol, Core architecture
  https://modelcontextprotocol.io/legacy/concepts/architecture
  Why it matters: gives a practical architecture view of clients, servers, transports, and message flow so students can reason about the integration boundary.

### Strongly recommended

- Model Context Protocol specification, Basic transports
  https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
  Why it matters: useful for advanced learners who need to understand how MCP messages move and what operational choices exist around transport.

- Anthropic, Claude Code settings
  https://code.claude.com/docs/en/settings
  Why it matters: clarifies where MCP servers are configured and how project, local, and managed scopes affect rollout and governance.

### Suggested follow-through

Take one candidate tool integration in your environment and answer:

- What business value does it unlock?
- What is the minimum safe scope for first exposure?
- What audit trail would your platform or security team require?
