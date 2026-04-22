# Session 3 — Exercises

Session 3 pushes students from "AI is impressive" to "AI is useful when aimed carefully." The three core exercises each produce an inspectable artifact against a real repository. The three lightweight exercises sharpen prompt and task judgment.

Pair these exercises with the **Student Prompt Template for Codebase Analysis** (see `session-3-prompt-template.md`).

Framing lines for the day:

- Use AI to make the hidden visible.
- Trust evidence, not fluency.
- Small, scoped, reviewable — always.

---

## Core Exercise 3 — Documentation Gap Hunt

**Objective**

Identify where the repo relies on tribal knowledge and produce improved documentation.

**Estimated time**

10–15 minutes

**Format**

Individual or pairs

**Inputs required**

- repo README and visible documentation
- AI assistant (Claude, Gemini, ChatGPT, or similar)

**Instructions**

1. Ask the AI to outline what the repo seems to do based on structure, entry points, and config.
2. Compare that with the repo's actual documentation.
3. List the top missing or misleading documentation items.
4. Draft improved README sections for the biggest gaps.

**Expected output**

- a gap list,
- draft replacement sections,
- one "questions still unanswered" section.

**How AI should be used**

Use AI for first-pass documentation rewrite and for spotting undocumented commands, configs, or architectural assumptions. Do not let AI fabricate details the repo does not support.

**What a good answer looks like**

- points to real missing knowledge,
- distinguishes "not documented" from "not discoverable,"
- includes explicit uncertainty,
- the drafted sections are concrete enough to paste into a README PR.

**Common weak patterns**

- generic README filler,
- missing platform or runtime assumptions,
- no attention to local setup,
- treating stale docs as good docs because they exist.

---

## Core Exercise 4 — Architecture Map from the Repo

**Objective**

Produce a lightweight architecture understanding artifact.

**Estimated time**

20 minutes

**Format**

Pairs or small groups

**Inputs required**

- the repo tree,
- main application entry points,
- AI assistant

**Instructions**

1. Identify the main services, modules, or top-level application pieces.
2. Ask AI to draft a component map and list responsibilities.
3. Mark places where confidence is low and the AI output is speculation.
4. Convert the result into a simple context / container / component narrative (C4-style, at whatever depth the repo supports).

**Expected output**

- a one-page architecture summary,
- a list of knowns and unknowns,
- likely high-coupling hotspots or boundary violations.

**How AI should be used**

AI should propose the first-pass map. Humans must edit it for accuracy and uncertainty. Anything the AI claims about a flow or boundary must be verified against code before it enters the artifact.

**What a good answer looks like**

- honest about ambiguity,
- focused on responsibilities and boundaries, not package names,
- useful as a future onboarding document,
- names at least one area where the AI's first pass was wrong.

**Common weak patterns**

- diagramming package names without meaning,
- hallucinated flows accepted as real,
- pretending uncertainty does not exist,
- a diagram with no narrative.

---

## Core Exercise 5 — AI-Assisted Test Improvement

**Objective**

Use AI to improve confidence in one specific, risky area.

**Estimated time**

20 minutes

**Format**

Pairs

**Inputs required**

- one component, endpoint, or service,
- current tests (if any),
- AI assistant

**Instructions**

1. Select one behavior that seems risky or under-tested.
2. Ask AI to propose test cases.
3. Review which proposed tests reflect true behavior versus implementation trivia.
4. Draft the final test plan or scaffold.

**Expected output**

- a prioritized test list,
- optional scaffold code,
- notes on what still requires human design judgment.

**How AI should be used**

AI can generate candidate cases and scaffolds, but students must filter aggressively. Reject tests that assert implementation details, over-mock, or merely exercise lines without testing behavior.

**What a good answer looks like**

- tests observable behavior,
- includes edge cases or failure paths,
- explains why each test increases confidence,
- names which AI-proposed tests were discarded and why.

**Common weak patterns**

- over-mocking,
- brittle tests that break on refactor,
- shallow assertions that merely exercise lines,
- treating "the AI generated 20 tests" as a win.

---

## Lightweight Exercise A — Prompt Tightening

**Time:** 5–10 minutes. **Format:** individual or pairs.

Start with the weak prompt:

> "Analyze this codebase and improve it."

Rewrite it so the AI must supply:

- **scope** — which repo, which files, which stack, what is out of bounds,
- **criteria** — the quality categories or framework to evaluate against,
- **output structure** — sections, tables, ranked findings, or a specific schema,
- **uncertainty requirements** — confidence levels, assumption flags, distinction between facts and inferences,
- **validation expectations** — what should be verified with tests, observability, or security checks before action.

**Deliverable:** one tightened prompt that a peer could use against a real repo without further clarification.

---

## Lightweight Exercise B — Is This a Good AI Task?

**Time:** 10 minutes. **Format:** small groups.

Sort each task into one of three buckets:

- **strong fit for AI** — safe to use as the primary drafter with light review,
- **acceptable with review** — AI can help but the human owns the decision and must verify,
- **poor fit / high risk** — do not use AI as the primary agent here.

Sample task list:

1. Summarize what each top-level directory of an unfamiliar repo probably does.
2. Pick which authentication library to adopt for a new service.
3. Generate candidate tests for an existing pure function.
4. Rewrite a 2000-line service class into "cleaner" modules.
5. Draft a README section for a documented-but-scattered deployment process.
6. Make a security-sensitive change to password reset handling.
7. Propose three small refactor candidates and rank them by risk.
8. Decide whether to migrate the database from Postgres to DynamoDB.
9. List observability gaps on a given request path.
10. Autonomously apply dependency upgrades across the repo overnight.

Discuss any task the group is split on. The disagreement is the lesson.

---

## Lightweight Exercise C — One Better Question

**Time:** 5–10 minutes. **Format:** individual or pairs.

Given an AI answer (use one produced during Exercise 3, 4, or 5), ask:

> "What one follow-up question would make this answer materially better?"

Good follow-up questions typically:

- demand evidence citations from the repo,
- ask for ranked prioritization,
- request explicit uncertainty,
- narrow scope from "all of it" to "this one component,"
- ask the AI what it would need to be more confident.

**Deliverable:** the single question and one sentence explaining why it is the highest-leverage next move.
