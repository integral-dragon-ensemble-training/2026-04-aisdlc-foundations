# Demo Blueprints

## Session 14

## Secure MCP Governance

### Demo 01

## Read-only HR database server

### Goal

Show the safest first step for an internal MCP integration.

### Suggested flow

1. Connect a simulated HR database MCP server.
2. Expose only read-only queries.
3. Query a safe example record.
4. Explain which actions are intentionally unavailable.

### Teaching points

- read-only is the right default for first rollout
- the server defines the boundary
- logs and scopes matter as much as the query itself

### Demo 02

## Governance hardening checklist

### Goal

Show that the quality of the integration depends on controls below the prompt.

### Suggested flow

Ask Claude to review the MCP server policy with constraints like:

- no write tools
- limited scopes
- mandatory logging
- explicit ownership of credentials
- deny by default

### Teaching points

- trust must be scoped and auditable
- the prompt is not the enforcement layer
- a weak server invalidates the integration

### Demo 03

## Poisoned content / denial boundary

### Goal

Show that hostile or misleading upstream content should not be able to silently expand capability.

### Suggested flow

1. Present a malicious or misleading HR record or ticket description.
2. Ask Claude how the server should respond.
3. Show the boundary condition: deny, redact, or require approval rather than blindly passing through.

### Teaching points

- data can be hostile even if it comes from an internal system
- the server should enforce what the model may not infer
- Session 14 is about reducing trust, not expanding it
