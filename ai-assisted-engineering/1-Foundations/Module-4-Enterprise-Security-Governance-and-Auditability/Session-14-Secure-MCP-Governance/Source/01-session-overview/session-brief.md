# Session Brief

## Session 14

## Secure MCP Governance

### Purpose

Teach students how to secure MCP endpoints and servers so that tool access does not become a path for data poisoning, exfiltration, or unauthorized action.

### Why this session matters

MCP makes agents operational by connecting them to real systems. That same connection also creates a security boundary that must be governed explicitly. If the MCP server is weak, prompt-level caution is not enough to protect the enterprise.

### Learning outcomes

By the end of this session, students should be able to:

- explain why MCP server governance is a security boundary
- distinguish prompt-level guardrails from server-level enforcement
- identify the minimum controls needed for a safe MCP rollout
- describe why read-only access should be the default first step
- recognize how prompt injection, data poisoning, and exfiltration change the threat model

### Core ideas

#### 1. The server is part of the trust boundary

An MCP server is not just a connector. It is a capability boundary that mediates access to data, tools, and actions. If the server is compromised, the model does not need to be “tricked” in the abstract; it can be handed dangerous capabilities directly.

#### 2. Prompt filtering is not enough

Security controls that only exist in the prompt can be bypassed by malicious tool output, hidden instructions, or compromised upstream content. Governance has to exist at the server, transport, and authorization layers.

#### 3. Read-only is the safest starting mode

The first rollout of an internal MCP server should usually be read-only. Let the team prove value, logging, and boundary behavior before enabling write actions.

#### 4. Access must be scoped and auditable

Teams need to know who can connect, which tools exist, which scopes are granted, and what every tool call did. If that cannot be answered, the integration is not ready for broader use.

#### 5. Server-level enforcement beats hope-based policy

The strongest controls are enforced where the action occurs. MCP governance should deny, limit, or log dangerous behavior at the server instead of expecting the model to self-police reliably.

### Engineering implications

- internal MCP servers should be treated like production services
- auth, scopes, and transport security matter as much as the tool catalog
- data returned from a server must be treated as potentially hostile
- write access should be staged and separately approved
- Session 14 closes the foundations arc by hardening the integration surface

### 23-minute flow

- `00:00-04:00`: Why MCP governance is a security problem
- `04:00-09:00`: What belongs at the server boundary
- `09:00-14:00`: Read-only first and authorization scope
- `14:00-18:00`: Live read-only HR database demo
- `18:00-21:00`: Risk review and control checklist
- `21:00-23:00`: Debrief and bridge to Session 15

### Key takeaway

If MCP is the bridge to real systems, then MCP governance is the guardrail on that bridge. The server, not the prompt, is where the enterprise should enforce trust.
