# Course Thesis and Storyline

## The main claim

**AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.**

That framing is stronger than “AI helps write more code faster” for three reasons:

1. Most real teams are already constrained by friction, not by the raw speed of typing code.
2. New features built on top of a confused or brittle codebase often increase future cost.
3. The best AI usage patterns in real engineering work are often inspection, explanation, cleanup, testing, guardrails, and workflow improvement.

## What this course should teach

By the end of the week, students should be able to:

- describe what a healthy software project looks like,
- identify technical debt in concrete terms,
- explain how technical debt creates “interest” in the form of slower changes,
- use AI tools to inspect a system and propose targeted improvements,
- validate AI-assisted changes using tests, observability, and security checks,
- convert one-off cleanup into a repeatable engineering practice.

## The story arc for the week

### Step 1 — What good looks like

Students need a target state before they can discuss debt intelligently.

The target state is not perfection. It is a system that is:

- understandable,
- reproducible,
- testable,
- observable,
- operable,
- secure enough for its context,
- and easy to change without fear.

### Step 2 — What friction looks like

Technical debt is not just ugly code.

It also includes:

- missing or misleading documentation,
- unclear architecture,
- environment drift,
- fragile or slow builds,
- test gaps,
- migration chaos,
- missing release visibility,
- poor logs and traces,
- hidden secrets,
- weak quality automation,
- and ad hoc team workflow.

### Step 3 — What AI is good at

AI tools are especially useful for:

- summarizing a codebase,
- finding patterns and inconsistencies,
- identifying documentation gaps,
- generating initial tests or scaffolds,
- proposing small refactors,
- tracing cross-cutting logic,
- creating checklists, scorecards, and cleanup plans,
- and accelerating repetitive cleanup work.

### Step 4 — What AI is bad at

AI tools are risky when teams use them to:

- rewrite large parts of a system without sufficient understanding,
- generate tests that assert implementation trivia instead of behavior,
- produce documentation that sounds plausible but is wrong,
- make security-sensitive changes without review,
- or create more code than the system can responsibly absorb.

### Step 5 — What lasting improvement looks like

The goal is not one impressive refactor.

The goal is a team habit:

- inspect,
- prioritize,
- improve,
- validate,
- standardize,
- repeat.

## The practical stance of the course

This is not a rewrite course.

It is a staged-improvement course. Students should leave with a model like this:

1. Make the system visible.
2. Reduce the biggest sources of friction.
3. Add confidence mechanisms.
4. Improve release and operational discipline.
5. Turn improvements into normal engineering workflow.

## Phrases worth repeating in class

- “Good engineering makes AI more useful.”
- “AI amplifies clarity, but it also amplifies confusion.”
- “The point is not more code. The point is easier change.”
- “Technical debt is the tax you pay every time the system resists change.”
- “If you cannot validate the change, AI just helped you move faster in the dark.”
