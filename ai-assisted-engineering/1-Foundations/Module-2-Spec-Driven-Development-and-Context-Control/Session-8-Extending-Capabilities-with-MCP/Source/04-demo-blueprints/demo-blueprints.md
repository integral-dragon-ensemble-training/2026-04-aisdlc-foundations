# Demo Blueprints

## Session 08

## Extending Capabilities with MCP

### Demo 01

## Connect one useful MCP server

### Goal

Show that MCP is a practical integration layer, not just a theoretical standard.

### Suggested flow

1. Configure one safe MCP server such as GitHub.
2. Ask Claude to list available tools or resources.
3. Use one read-only action first.
4. Explain what system access the connection actually created.

### Teaching points

- MCP expands capability quickly
- the first exposure should usually be read-only
- tool access should be explicit and inspectable

### Demo 02

## Inspect the payload boundary

### Goal

Show students what structured tool use looks like beneath the surface.

### Suggested flow

1. Capture or mock one MCP call.
2. Walk through the tool name, arguments, and returned structure.
3. Highlight where secrets, identifiers, or privileged actions would matter.

### Teaching points

- integrations should be legible
- payload review helps teams reason about risk
- protocol literacy reduces blind trust

### Demo 03

## Governance review before expansion

### Goal

Show that an MCP success demo is only the start of the enterprise conversation.

### Suggested flow

Ask follow-ups such as:

- `Which tools from this server should remain disabled?`
- `What credentials back this connection?`
- `How would we audit usage of this tool set?`
- `What is the safest first rollout boundary for the team?`

### Teaching points

- capability review is part of architecture review
- least privilege still applies
- operational rollout should be staged, not assumed
