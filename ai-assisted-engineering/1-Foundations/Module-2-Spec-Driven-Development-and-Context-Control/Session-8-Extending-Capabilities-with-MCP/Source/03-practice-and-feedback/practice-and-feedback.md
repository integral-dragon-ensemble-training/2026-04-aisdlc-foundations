# Practice and Feedback

## Session 08

## Extending Capabilities with MCP

### In-session practice 01

## Capability mapping

Take three candidate MCP integrations such as:

- GitHub
- internal ticketing system
- read-only production telemetry

For each one, answer:

- what value does it provide to the agent?
- what is the highest-risk capability it exposes?
- what should be read-only vs write-enabled?
- what approval or audit requirement should apply?

### In-session practice 02

## Payload inspection

Review one MCP tool-call payload or mock payload and identify:

- the tool name
- the arguments passed
- the sensitive fields
- the likely result shape
- the security question you would ask before enabling it broadly

### Discussion prompts

- Which internal systems would create the most leverage if exposed through MCP?
- Which systems should stay out of reach until governance is stronger?
- Why is an open protocol better for enterprise adoption than custom per-vendor plugins?

### Between-session fieldwork

Complete all three:

1. Pick one internal system that could be exposed safely through MCP.
2. Write a short access proposal describing scope, read/write boundary, and audit expectations.
3. Identify the first governance concern security or platform engineering would raise.

### Submission prompt

Write 6 to 8 sentences answering:

- Which system would you expose first through MCP and why?
- What is the minimum permission boundary you would allow?
- What would go wrong if tool access were enabled before ownership, logging, and scope were clear?

### Survey questions

- Prior to this session, how familiar were you with MCP as an enterprise integration standard?
- After this session, how confident are you that you can evaluate an MCP integration beyond the demo value alone?
- Which concern feels most important in your environment right now: access scope, credential handling, auditability, or vendor lock-in?
