# Session 15
## Code Review and Cognitive Debt Mitigation
### A passing test suite is not the same thing as a safe change

---

# AI can ship code that looks right and still be wrong

- syntax can be clean
- tests can pass
- the architecture can still drift
- the hidden bug can still survive review

---

# Review must go beyond correctness theater

- what changed in the control flow?
- what changed in ownership or boundaries?
- what failure modes were introduced?
- what assumptions got smuggled in?

---

# Passing tests are evidence, not proof

- tests only cover what they express
- untouched paths can still break
- integration and architectural behavior can still drift
- the reviewer still owns the mental model

---

# Automation bias is a review risk

- polished output feels trustworthy
- confident narration can suppress scrutiny
- people accept the AI answer too quickly
- “it looks fine” is not a review criterion

---

# Cognitive debt accumulates when we approve what we do not understand

- the repo grows
- comprehension shrinks
- future changes get harder
- the team loses its ability to reason about the system

---

# What a strong review checklist looks for

- clear and readable code
- correct boundaries and ownership
- no duplicated or dead logic
- proper error handling
- good test coverage
- performance and maintainability risks

---

# The reviewer’s job is to find the load-bearing bug

- not every AI issue is obvious
- the dangerous ones are often small
- subtle logic errors are the ones that survive formatting and tests

---

# Live demo pattern

- present a short AI-generated PR
- review the diff line by line
- identify one architectural or business-logic flaw
- write a review comment that explains the structural risk

---

# Review output should be actionable

- name the issue
- explain the impact
- point to the affected boundary
- suggest the smallest useful fix

---

# Common failure modes

- approving because tests passed
- reviewing style instead of structure
- trusting the model’s confidence too much
- leaving the reviewer unable to explain the change later

---

# Key takeaway

- Good review is understanding plus evidence.
- If the reviewer cannot explain the diff, the review is incomplete.

---

# Bridge to Session 16

- Session 15 tightens human review.
- Session 16 adds traceability and narration so the work can be audited after the fact.
