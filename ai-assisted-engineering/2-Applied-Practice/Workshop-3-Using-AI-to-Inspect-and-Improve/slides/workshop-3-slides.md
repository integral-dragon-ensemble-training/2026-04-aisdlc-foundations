# Workshop 3 — Using AI to Inspect and Improve

Module 02 · Workshop 03
Subtitle: Targeted, reviewable AI use against a real codebase.

---

## Slide 1 — Title

- Module 02 · Workshop 03
- Title: **Using AI to Inspect and Improve**
- Subtitle: Targeted, reviewable AI use against a real codebase.
- Program: AI-Accelerated Software Development | Applied Practice

---

## Slide 2 — What AI Is Actually Good At in Existing Codebases

**Core message:** AI has high leverage in understanding, summarizing, scaffolding, and repetitive cleanup — not in owning architecture decisions.

**Capability map — five reliable jobs:**

- **Inspect** — repo summarization, structure scans, cross-file pattern detection.
- **Explain** — module roles, call paths, legacy logic walkthroughs.
- **Propose** — ranked findings, small refactor candidates, test ideas.
- **Scaffold** — first-draft docs, test skeletons, migration outlines.
- **Standardize** — checklists, review templates, repeatable prompts.

Framing line: *Use AI to make the hidden visible.*

---

## Slide 3 — Better Prompt Shape for Engineering Work

**Core message:** Specific context and explicit output format produce better engineering results.

**Weak prompt:**
> "Analyze this codebase and improve it."

**Tightened prompt:**
> "Act as a senior architect. Evaluate this Python/FastAPI repo against nine project-health categories. For each category: confirmable evidence, weaknesses, likely debt, 1–5 rating, and confidence level. Rank the top 5 problems. Distinguish facts from inferences. Do not hallucinate architecture."

**Five levers that tighten any prompt:** scope, quality criteria, output structure, uncertainty requirements, validation expectations.

---

## Slide 4 — AI for Documentation and Architecture Discovery

**Core message:** Making hidden knowledge explicit is one of the safest high-value uses of AI.

- Generate **README refresh candidates** grounded in actual repo structure.
- Summarize **module roles** and likely responsibilities.
- Draft a **C4-style component overview** as a first-pass map.
- List **unanswered architectural questions** the repo does not resolve.

Treat every generated artifact as a first pass. Confidence should be annotated, not assumed.

---

## Slide 5 — AI for Tests and Small Refactors

**Core message:** AI accelerates confidence-building work when scope is constrained.

- Generate **candidate tests** for one component, then filter for real behavior.
- Suggest **seam creation** for better isolation before bigger changes.
- Propose **logging, error-handling, and small cleanup** under clear rules.
- Keep diffs **small, scoped, and reviewable**.

Discipline line: *small, scoped, reviewable — always.*

---

## Slide 6 — AI Failure Modes

**Core message:** The biggest risk is fluent overreach.

**Red flags to distrust:**

- Hallucinated architecture described with confidence.
- Shallow tests that assert implementation trivia.
- Unsafe refactors that expand scope silently.
- Oversized diffs no reviewer can reason about.
- Summaries that hide uncertainty behind smooth prose.
- Generated complexity no one asked for.

Framing line: *Trust evidence, not fluency.*

---

## Slide 7 — Human Review Rules for AI-Assisted Changes

**Core message:** The review bar should be clearer, not lower.

- **Require explicit scope** — name the files, the behavior, the acceptance.
- **Require validation steps** — tests, run output, or concrete verification.
- **Prefer small diffs** — split large proposals before reviewing.
- **Check assumptions against the repo** — do not accept claims without evidence.
- **Treat AI output as a draft** — fluency is not a review signal.

This is where AI excitement becomes engineering discipline.

---

## Slide 8 — Workshop 3 Exercises

**Core message:** Produce concrete, inspectable artifacts against a real repo.

- **Documentation Gap Hunt** — AI outline vs. real docs; list missing/misleading items; draft replacements.
- **Architecture Map from the Repo** — first-pass component map, responsibilities, uncertainty flags.
- **AI-Assisted Test Improvement** — propose candidate tests, filter for real behavior, build a test plan.
- **Supporting prompt template:** Participant Prompt Template for Codebase Analysis.

Debrief question: *What AI-generated outputs would you trust after review, and which would you never trust without deeper verification?*

---

## Slide 9 — Close

Use AI to **inspect, explain, propose, and scaffold.**
Leave the architecture decisions to humans who can validate them.
