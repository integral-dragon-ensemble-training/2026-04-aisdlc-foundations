# Practice and Feedback

## Session 12

## OWASP Top 10 for Agentic Apps

### In-session practice 01

## Incident trace review

Review a short incident trace in which an agent performed an unauthorized action. Identify:

- the initial injection or trust failure
- the tool or memory boundary that was crossed
- the most likely OWASP-style risk class
- the control that should have stopped the chain earlier

### In-session practice 02

## Map the control layer

For each of the following, decide whether the primary control belongs in:

- prompt / instruction layer
- permissions / sandbox layer
- tool server layer
- identity / authorization layer
- human review / audit layer

Scenarios:

- a malicious ticket description tries to steer the agent
- an agent should only read, not write, to a data source
- a compromised context window tries to trigger a destructive tool call
- an external document injects a false instruction

### Discussion prompts

- Where does your current environment confuse content quality with action safety?
- Which agentic risk would be hardest for your team to notice before damage occurs?
- What changes when the system can touch data instead of only generating text?

### Between-session fieldwork

Complete all three:

1. Choose one agentic workflow in your environment.
2. Write a minimal threat model with at least three attack paths.
3. Identify one control you would add at each of the following layers: prompt, permission, tool server, and review.

### Submission prompt

Write 6 to 8 sentences answering:

- Which agentic attack path felt most realistic in your environment?
- Which control layer would have stopped it earliest?
- What false sense of safety disappears once the agent can take action?

### Survey questions

- Does your organization have documented security policies specifically for autonomous agents?
- After this session, how confident are you that you can distinguish content risk from action risk?
- Which security concern feels most urgent right now: prompt injection, tool misuse, identity spoofing, or memory poisoning?
