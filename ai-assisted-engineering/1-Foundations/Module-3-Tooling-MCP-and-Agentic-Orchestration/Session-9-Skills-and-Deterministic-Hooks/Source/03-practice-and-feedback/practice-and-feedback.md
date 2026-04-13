# Practice and Feedback

## Session 09

## Skills and Deterministic Hooks

### In-session practice 01

## Skill or hook?

Classify each requirement as:

- better implemented as a skill
- better implemented as a hook
- requires both

Requirements:

- enforce formatting after edits
- apply our API error-handling conventions
- block destructive shell commands
- use our incident triage workflow
- stop commits if a plaintext secret appears in the diff

### In-session practice 02

## Hook design sketch

Write a basic project-level hook configuration for one of these controls:

- block edits to protected files
- run a formatter after file writes
- deny commit attempts when a secret pattern is detected

For your design, specify:

- triggering event
- matcher
- command or action
- expected behavior if the check fails

### Discussion prompts

- Where does your current workflow depend too much on the model remembering instructions?
- Which of your existing checks should move closer to the tool lifecycle?
- What should remain flexible and judgment-based rather than forced by automation?

### Between-session fieldwork

Complete all three:

1. Identify one repeated quality check in your environment.
2. Decide whether it belongs in a skill, hook, or CI step.
3. Write a short explanation of why that boundary is the right one.

### Submission prompt

Write 6 to 8 sentences answering:

- Which check in your environment most needs deterministic enforcement?
- What would be lost if you over-automated a workflow that still needs judgment?
- What review burden disappears once a mandatory check becomes a hook?

### Survey questions

- Do you currently use any automated gates aimed specifically at AI-assisted code before it reaches the main branch?
- After this session, how confident are you in distinguishing helpful reusable guidance from true enforcement?
- Which deterministic control would improve your environment fastest right now: secret scanning, file protection, auto-formatting, or test enforcement?
