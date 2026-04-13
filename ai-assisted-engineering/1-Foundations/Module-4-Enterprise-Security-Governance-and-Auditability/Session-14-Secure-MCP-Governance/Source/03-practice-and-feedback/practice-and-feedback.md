# Practice and Feedback

## Session 14

## Secure MCP Governance

### In-session practice 01

## Rapid risk review

Review a proposed MCP integration such as a Jira connector or HR database connector and identify:

- the primary data exposed
- the most likely exfiltration path
- the most likely privilege escalation path
- what should be read-only
- what should be blocked until governance is stronger

### In-session practice 02

## Server-level versus prompt-level control

Take these controls and classify them:

- server-side scope restriction
- prompt instruction to “be careful”
- auth token rotation
- output logging
- model instruction to avoid writing data

Mark each as:

- server-level enforcement
- client-level control
- prompt-level guidance
- governance / audit control

### Discussion prompts

- What would happen if a malicious ticket description or database record tried to influence the agent through an MCP tool response?
- Which of your internal systems would be too sensitive to expose without read-only first?
- Why should the MCP server be the place where access is denied, not the prompt?

### Between-session fieldwork

Complete all three:

1. Pick one internal system that might eventually be exposed through MCP.
2. Write a short governance note covering read/write scope, auth, and logging.
3. State the first risk that would block a production rollout.

### Submission prompt

Write 6 to 8 sentences answering:

- Which server-level control matters most in your environment: read-only mode, scope restriction, logging, or credential control?
- What would go wrong if the integration were trusted because it is “internal”?
- Which kind of poisoned input would worry you most: a malicious ticket, a compromised record, or a bad tool response?

### Survey questions

- Before this session, how strongly did you believe prompt filtering alone could secure an MCP integration?
- After this session, how confident are you in evaluating an MCP endpoint from a governance perspective?
- Which control would reduce your risk the fastest right now: read-only first, server-side scope limits, better logging, or tighter approval gates?
