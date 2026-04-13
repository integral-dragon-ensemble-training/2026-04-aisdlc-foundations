# Practice and Feedback

## Session 06

## Plan Mode vs. Act Mode

### In-session practice 01

## Plan interrogation

Use Plan Mode on a change request such as:

`Refactor the login flow to support OAuth2 while preserving existing sessions.`

Then challenge the plan with these questions:

- Which files do you think you need to touch?
- What are the highest-risk assumptions?
- What would break backward compatibility?
- What tests must exist before this is safe to merge?

### In-session practice 02

## Approval gate checklist

Take the proposed plan and decide whether you would approve execution.

Approve only if the plan:

- names the boundary clearly
- keeps the diff small
- preserves stated invariants
- includes a test approach
- surfaces unresolved questions instead of hiding them

### Discussion prompts

- Where would Plan Mode reduce risk most in your current environment?
- What does your team currently approve too late: scope, file impact, or test strategy?
- When does planning become enough detail, and when does it become waste?

### Between-session fieldwork

Complete all three:

1. Run one real task through Plan Mode instead of going directly to execution.
2. Reject the first plan at least once and force a refinement.
3. Capture which change in the plan made you more willing to approve it.

### Submission prompt

Write 6 to 8 sentences answering:

- What did the first plan miss?
- Which question most improved the second plan?
- What risk would have hit the repo if you had skipped the planning gate?

### Survey questions

- How often do you currently let an AI start editing before you have reviewed its approach?
- After this session, how confident are you in using Plan Mode as a real approval gate rather than a courtesy preview?
- Which control matters most for your environment right now: plan review, tighter permissions, smaller diffs, or stronger tests?
