# Session Brief

## Session 08

## Extending Capabilities with MCP

### Purpose

Teach students what MCP is, why it matters, and how it lets Claude connect to external tools and systems through a standard protocol instead of brittle one-off integrations.

### Why this session matters

Without tool access, the agent is mostly a reasoning surface. With tool access, it can inspect repos, query systems, and work against enterprise context. MCP is the bridge, so teams need to understand both the leverage and the security boundary.

### Learning outcomes

By the end of this session, students should be able to:

- explain MCP in practical enterprise terms
- distinguish MCP servers, tools, resources, and prompts at a high level
- recognize why protocol standardization matters more than custom wrappers
- inspect a tool call as structured context rather than magic
- identify the main security and governance questions created by tool access

### Core ideas

#### 1. MCP standardizes tool connectivity

Teams should not have to reinvent custom integration code for every model, tool, and internal system pairing. MCP creates a common contract.

#### 2. Tool access changes the risk profile

An agent with filesystem or ticket access can do much more than an agent limited to text generation. Governance has to follow capability.

#### 3. Structured context beats hidden glue code

MCP makes the interface legible: what tool was called, what arguments were passed, and what came back. That is much better than mystery middleware.

#### 4. Protocol thinking beats vendor thinking

Open standards reduce lock-in, make integrations more reusable, and let enterprises reason about capability boundaries more clearly.

#### 5. Tool integration is not trust by default

The existence of a connector does not mean it should be broadly exposed. Teams still need permissions, approved servers, credential controls, and auditability.

### Engineering implications

- internal tools can be exposed to agents through a shared protocol instead of bespoke glue
- engineers need to inspect what a tool call actually sends and returns
- MCP should be reviewed as part of enterprise architecture, not just developer convenience
- least privilege still applies when the caller is an agent
- future labs can build on MCP-backed repo, API, and data access

### 23-minute flow

- `00:00-04:00`: Why tool connectivity changes the game
- `04:00-09:00`: What MCP is and why open standards matter
- `09:00-14:00`: Servers, tools, resources, and prompts
- `14:00-18:00`: Live MCP connection and payload inspection
- `18:00-21:00`: Security and governance implications
- `21:00-23:00`: Debrief and bridge to Module 03

### Key takeaway

MCP is not just a plugin mechanism. It is the integration layer that turns a terminal-native model into a tool-using engineering system, which is exactly why it must be understood and governed.
