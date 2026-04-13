# Practice and Feedback

## Session 07

## Context Control via CLAUDE.md

### In-session practice 01

## Rule triage

Take these instructions and decide where they belong:

- `Always narrate which tests were run or skipped.`
- `Use my preferred terminal theme.`
- `Do not modify database schemas without approval.`
- `Prefer the existing payments service rather than adding a new integration layer.`
- `For today's bugfix, only touch the retry logic.`

Classify each as:

- user scope
- project scope
- local scope
- task-specific instruction

### In-session practice 02

## Draft a high-signal `CLAUDE.md`

Write five rules for a regulated enterprise microservice. Include:

- one architecture boundary
- one testing expectation
- one review expectation
- one security constraint
- one scope-limit rule

Then remove any rule that is too vague to change behavior.

### Discussion prompts

- Which team rules are you currently retyping in chat instead of versioning?
- What should never live in a personal local file if the whole team depends on it?
- Where does your environment need stronger persistent context: style, architecture, testing, or review discipline?

### Between-session fieldwork

Complete all three:

1. Draft a real `CLAUDE.md` for one active project.
2. Run one repeated task before and after adding the file.
3. Note which rule most clearly changed the agent's behavior.

### Submission prompt

Write 6 to 8 sentences answering:

- Which repeated instruction in your environment should become a persistent rule first?
- What rule did you remove because it was too vague or too temporary?
- What is the risk if project-wide standards remain trapped in individual prompts?

### Survey questions

- Does your team currently use a shared, version-controlled place to store recurring AI workflow rules?
- After this session, how confident are you that you can separate durable project policy from one-off task instructions?
- Which persistent rule would deliver the most value in your environment right now: testing expectations, architecture boundaries, review narration, or security constraints?
