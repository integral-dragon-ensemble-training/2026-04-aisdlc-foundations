# Session Brief

## Session 15

## Code Review and Cognitive Debt Mitigation

### Purpose

Teach students how to review AI-generated diffs for structural soundness, not just syntax correctness, and how to recognize cognitive debt and automation bias before they turn into team-wide habits.

### Why this session matters

AI can produce code that compiles, tests, and still quietly breaks the architecture. The risk is not only bad code. It is human overconfidence in code that looks polished. Review has to move beyond “does it run?” and into “do we understand what this change really does?”

### Learning outcomes

By the end of this session, students should be able to:

- explain why passing tests do not prove structural soundness
- identify the difference between syntax quality and architectural safety
- review an AI-generated diff for hidden logic, boundary, or integration failures
- recognize automation bias in their own review behavior
- describe how cognitive debt accumulates when teams approve code they do not fully understand

### Core ideas

#### 1. Tests are evidence, not proof

Passing tests are useful, but they only cover the cases the tests actually express. A clean test run does not guarantee the change preserved the intended structure, invariants, or operational behavior.

#### 2. Review must examine the load-bearing behavior

The most dangerous AI bugs are often not syntax mistakes. They are subtle changes to control flow, data ownership, assumptions, or failure handling that still look tidy in a diff.

#### 3. Automation bias is a real review risk

When code looks fluent and the AI sounds confident, reviewers tend to trust the output too quickly. That is how weak reasoning slips past human oversight.

#### 4. Cognitive debt compounds quietly

Every time a reviewer approves code they do not really understand, the team increases the amount of implicit knowledge it must carry forward. The repo gets bigger, but comprehension gets thinner.

#### 5. Good review has a checklist and a position

A good reviewer knows what to look for, what not to trust, and how to say “this is structurally risky” with specific evidence.

### Engineering implications

- review comments should focus on structural risk, not just style
- AI-generated code needs human ownership, not passive acceptance
- small diffs are easier to reason about and review
- tests should be paired with architecture and logic review
- Session 15 prepares the cohort for Session 16’s auditability and traceability concerns

### 23-minute flow

- `00:00-04:00`: Why green tests are not enough
- `04:00-09:00`: Structural diff review versus syntax review
- `09:00-14:00`: Automation bias and cognitive debt
- `14:00-18:00`: Live AI diff review demo
- `18:00-21:00`: Writing high-signal review comments
- `21:00-23:00`: Debrief and bridge to Session 16

### Key takeaway

If a reviewer cannot explain the change in their own words, the review is not done. Understanding is the deliverable, not just approval.
