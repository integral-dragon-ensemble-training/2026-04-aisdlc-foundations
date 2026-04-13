# Session 14
## Secure MCP Governance
### Secure the server boundary before you let the model reach enterprise data

---

# MCP changes the threat model

- The model is no longer only generating text.
- It is connected to tools, data, and potentially write-capable systems.
- That means the risk is no longer just bad output.
- The risk is bad action.

---

# Prompt-level filtering is not enough

- Malicious tool output can carry hidden instructions.
- Compromised content can poison the agent’s context.
- A server that is too permissive can hand over dangerous capabilities directly.
- Governance has to exist below the prompt.

---

# The MCP server is part of the trust boundary

- tools
- credentials
- scopes
- transport
- logging
- approval policy

The server is not a convenience layer. It is security infrastructure.

---

# Read-only first is the safest rollout default

- prove value before enabling writes
- observe actual call patterns
- validate logs and audit trails
- minimize blast radius during early adoption

---

# What server-level controls should answer

- Who can connect?
- Which tools exist?
- Which tools are read-only?
- Which tools are write-capable?
- What gets logged?
- What is denied by default?

---

# Data poisoning and exfiltration are real MCP threats

- a poisoned upstream record can change downstream behavior
- a compromised server can return hostile context
- a write-capable tool can move data out of the boundary
- trust must be earned at the server, not assumed in the prompt

---

# Live demo: simulated HR database MCP server

- connect a read-only HR database server
- query safe example data
- show the allowed tool surface
- explain why write access stays off

The point is governance, not database performance.

---

# Security questions to ask before broader rollout

- Is the server authenticated and scoped?
- Are credentials rotated and owned?
- Can the integration be read-only first?
- Are outputs logged and reviewable?
- Would a poisoned result change downstream decisions?

---

# Zero Trust applies here too

- do not trust by network location
- do not trust by “internal” branding
- do not trust by default because the tool exists
- verify every boundary that can act on data

---

# Key takeaway

- MCP governance is server-level governance.
- If the server is weak, the prompt cannot save you.

---

# Bridge to Session 15

- Session 14 hardens tool access.
- Session 15 shifts the focus to the human review layer and the cognitive debt that AI-generated code can leave behind.
