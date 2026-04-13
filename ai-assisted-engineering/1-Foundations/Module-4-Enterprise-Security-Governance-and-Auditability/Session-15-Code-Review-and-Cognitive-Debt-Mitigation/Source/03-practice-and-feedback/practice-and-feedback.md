# Practice and Feedback

## Session 15

## Code Review and Cognitive Debt Mitigation

### In-session practice 01

## AI PR review

Review a 50-line AI-generated diff and identify:

- one architectural violation
- one hidden logic bug
- one assumption that needs verification
- one review comment that would block merge

### In-session practice 02

## Tests versus understanding

Take a change that passes tests but still feels structurally risky. Write two responses:

- one sentence explaining why tests alone are not enough
- one sentence describing the missing structural check

### Discussion prompts

- Where does your team most often confuse “passed tests” with “safe change”?
- Which kind of AI-generated bug is hardest for your reviewers to spot?
- What is the smallest diff that would still require deep human reasoning before approval?

### Between-session fieldwork

Complete all three:

1. Review one recent AI-assisted PR or diff in your codebase.
2. Write a review comment that names the structural risk, not just the visible bug.
3. Note whether automation bias or cognitive debt made the review harder.

### Submission prompt

Write 6 to 8 sentences answering:

- What did you almost miss because the diff looked polished?
- Which checklist item helped most in finding the real issue?
- What would have happened if the code had been merged without structural review?

### Survey questions

- How often do you see AI-generated code that passes tests but still feels wrong?
- After this session, how confident are you that you can review AI output for structural soundness?
- Which review habit would improve your team most right now: smaller diffs, stricter checklists, slower approvals, or stronger ownership of the mental model?
