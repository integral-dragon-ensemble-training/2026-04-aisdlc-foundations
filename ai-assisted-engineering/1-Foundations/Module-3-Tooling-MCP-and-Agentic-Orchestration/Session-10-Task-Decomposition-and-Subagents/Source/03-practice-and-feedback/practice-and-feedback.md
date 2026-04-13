# Practice and Feedback

## Session 10

## Task Decomposition and Subagents

### In-session practice 01

## Decompose the feature

Take this request:

`Implement an OAuth2 billing dashboard for enterprise customers.`

Break it into three strictly isolated delegated tasks. For each task, specify:

- objective
- scope boundary
- allowed tools
- expected output

### In-session practice 02

## Main conversation or subagent?

For each activity below, decide whether it belongs in the main conversation or a subagent:

- trace a noisy failing test suite and return the top three root causes
- make a tiny one-line bugfix with active back-and-forth clarification
- review one module for security issues with read-only tools
- explore three unrelated codebase areas and summarize findings

### Discussion prompts

- Where does poor decomposition currently create rework in your environment?
- Which types of subagent roles would be most useful for your team first: reviewer, tester, researcher, or debugger?
- When does delegation save context, and when does it just add overhead?

### Between-session fieldwork

Complete all three:

1. Choose one real feature or bug request that currently feels too large.
2. Rewrite it as 2 to 4 bounded delegated tasks.
3. Note which task should remain in the main conversation and why.

### Submission prompt

Write 6 to 8 sentences answering:

- What was the hardest part of decomposing the request cleanly?
- Which delegated task gained the most from isolated context?
- What failure would happen first if you tried to solve the whole request in one giant prompt?

### Survey questions

- What is the largest coding task you have successfully handled with AI in one unbroken prompt?
- After this session, how confident are you in turning a large request into isolated delegated tasks?
- Which benefit matters most in your environment right now: lower context noise, tighter permissions, clearer summaries, or better specialist focus?
