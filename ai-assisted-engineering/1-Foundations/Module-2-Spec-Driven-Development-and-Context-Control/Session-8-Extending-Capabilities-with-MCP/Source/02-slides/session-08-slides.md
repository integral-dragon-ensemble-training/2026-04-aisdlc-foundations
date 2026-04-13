# Session 08
## Extending Capabilities with MCP
### Connect the agent to tools without inventing a new integration every time

---

# Tool access changes what the agent can do

- Without tools, the model can reason and draft.
- With tools, it can inspect systems, query live context, and act through integrations.
- That changes both capability and risk.

---

# MCP is the shared protocol layer

- Model Context Protocol standardizes how LLM applications connect to external capabilities.
- It reduces brittle one-off wrapper code.
- It gives teams a common way to expose tools, resources, and prompts.

---

# Useful framing: MCP is infrastructure, not a chat feature

- It belongs in enterprise architecture discussions.
- It affects security, access, logging, and operational boundaries.
- It is how agents connect to the real environment.

---

# Core concepts students should recognize

- MCP server
- client
- tools
- resources
- prompts
- transports and message exchange

---

# Why open protocols matter

- less vendor lock-in
- reusable integration patterns
- clearer boundary ownership
- easier enterprise governance than ad hoc plugin ecosystems

---

# What the payload tells you

- which tool was called
- what arguments were passed
- what context the agent received back
- where authorization and capability boundaries matter

---

# MCP should remove mystery, not add it

- A good integration is inspectable.
- Engineers should understand what a tool call is allowed to do.
- "Claude talked to the system somehow" is not an acceptable enterprise explanation.

---

# Live demo options

- connect a GitHub MCP server
- connect a local database-backed MCP server
- inspect one tool call and review the returned structure

---

# Security questions to ask immediately

- What authority does this server grant?
- Which credentials back it?
- Which tools should be exposed at all?
- How is usage logged and reviewed?

---

# MCP and governance belong together

- permissions
- approved servers
- scoped credentials
- auditable usage
- minimal exposed surface area

---

# The enterprise mistake to avoid

- treating every connector as harmless convenience

Tool access is a real capability boundary.

---

# Key takeaway

- MCP is the standard integration layer for agent tooling.
- That is exactly why teams need to understand both the leverage and the guardrails.

---

# Bridge to Module 03

- Module 02 taught intent, plans, persistent rules, and connectivity.
- Module 03 builds on that foundation with hooks, skills, subagents, and orchestration patterns.
