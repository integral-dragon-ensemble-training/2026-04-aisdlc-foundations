# Practice and Feedback

## Session 05

## Spec-Driven Development

### In-session practice 01

## Ticket triage

Take a weak ticket such as:

`Add MFA support to login`

Rewrite it into a compact engineering spec with:

- one clear goal
- three constraints
- four acceptance criteria
- two explicit non-goals

### In-session practice 02

## Acceptance-criteria hardening

Given these weak criteria:

- "make the endpoint faster"
- "improve security"
- "keep the UX simple"

Rewrite each one so a reviewer could actually verify it.

### Discussion prompts

- Where does your team currently confuse a ticket with a specification?
- What is the smallest amount of structure that would materially improve your PR quality?
- Which work types in your environment most need specs before AI touches them: auth, billing, migrations, CI, or docs?

### Between-session fieldwork

Complete all three:

1. Take one real ticket from your backlog and rewrite it into a compact spec.
2. Ask Claude Code to critique the spec for ambiguity, hidden assumptions, and missing edge cases.
3. Revise the spec once, then note what changed and why.

### Submission prompt

Write 6 to 8 sentences answering:

- What ambiguity did you discover only after forcing the request into a spec?
- Which acceptance criterion was hardest to make binary?
- What would have gone wrong if the agent had started coding before this rewrite?

### Survey questions

- How often do you currently prompt an AI from a ticket that has not been upgraded into a spec?
- After this session, how confident are you that you can write acceptance criteria an engineer can actually review?
- Which part of SDD feels most valuable right now: clearer scope, less rework, better tests, or safer reviews?
