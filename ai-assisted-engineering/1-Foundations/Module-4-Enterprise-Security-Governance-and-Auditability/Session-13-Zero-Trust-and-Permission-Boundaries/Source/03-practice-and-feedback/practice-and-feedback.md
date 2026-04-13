# Practice and Feedback

## Session 13

## Zero Trust and Permission Boundaries

### In-session practice 01

## Permission triage

Classify each request as:

- allow
- deny
- allow only with approval

Requests:

- read a repository file
- edit a production config file
- run a destructive shell command
- query a connector that can write to a ticketing system
- inspect logs from a read-only service

### In-session practice 02

## Tool whitelist sketch

Write a JSON-style permission policy for a read-only review agent that:

- allows file reads
- denies shell execution
- denies file writes
- allows only one named connector
- requires approval for any write-capable action

### Discussion prompts

- Where does your current workflow rely on implicit trust instead of explicit approval?
- Which permission boundary is hardest to enforce because teams want convenience?
- What would change if every AI identity had a named owner and a narrow role?

### Between-session fieldwork

Complete all three:

1. Review one real agentic workflow in your environment.
2. Identify the weakest permission boundary.
3. Propose one narrower role or approval gate that would reduce risk immediately.

### Submission prompt

Write 6 to 8 sentences answering:

- Which permission is too broad today?
- What control would you add first: read-only default, approval mode, tool whitelist, or identity scoping?
- What is the downside if teams keep treating the agent like a trusted coworker instead of a controlled system component?

### Survey questions

- Have you ever used an AI coding tool with overly broad local privileges because it was easier?
- After this session, how confident are you that you can separate helpful access from excessive access?
- Which control feels most urgent in your environment right now: tool whitelists, RBAC, approval modes, or audit logging?
