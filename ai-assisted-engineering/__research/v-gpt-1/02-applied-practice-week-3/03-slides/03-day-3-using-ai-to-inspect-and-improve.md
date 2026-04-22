ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/03-slides/03-day-3-using-ai-to-inspect-and-improve.md

# Day 3 Slide Deck — Using AI to Inspect and Improve

## Slide 1 — What AI Is Actually Good At in Existing Codebases

**Core message:** AI has high leverage in understanding, summarizing, scaffolding, and repetitive cleanup.

**Bullets**
- Repo summarization and component explanation
- Documentation gap finding
- Test idea generation and initial scaffolding
- Cross-file pattern detection
- Drafting cleanup plans and small refactor proposals

**Suggested visual**
- Capability map: inspect, explain, propose, scaffold, standardize

**Speaker notes**
Make it clear that this is not about giving AI unlimited autonomy.

---

## Slide 2 — Better Prompt Shape for Engineering Work

**Core message:** Specific context and output format produce better engineering results.

**Bullets**
- Give the AI the scope, files, stack, quality criteria, and output format
- Ask for uncertainty and assumptions explicitly
- Ask for ranked findings, not generic advice
- Prefer inspectable outputs over prose

**Suggested visual**
- Before/after prompt comparison

**Speaker notes**
Show one weak prompt and one strong prompt. Students will immediately see the difference.

---

## Slide 3 — AI for Documentation and Architecture Discovery

**Core message:** One of the safest high-value uses of AI is making hidden knowledge explicit.

**Bullets**
- Generate README refresh candidates
- Summarize module roles
- Draft a C4-style component overview
- List unanswered architectural questions

**Suggested visual**
- Codebase map with sticky notes for missing docs

**Speaker notes**
Stress that generated architecture should be treated as a first pass requiring review.

---

## Slide 4 — AI for Tests and Small Refactors

**Core message:** AI can speed up confidence-building work when the scope is constrained.

**Bullets**
- Generate candidate tests for one component
- Suggest seam creation for better isolation
- Propose logging or error-handling improvements
- Perform repetitive cleanup under clear rules

**Suggested visual**
- Small diff example: before/after plus validation gates

**Speaker notes**
Use language like 'small, scoped, reviewable' repeatedly.

---

## Slide 5 — AI Failure Modes

**Core message:** The biggest risk is fluent overreach.

**Bullets**
- Hallucinated architecture
- Shallow tests
- Unsafe refactors
- Oversized diffs
- Confident summaries that hide uncertainty
- Generated complexity no one asked for

**Suggested visual**
- Warning slide with red flags checklist

**Speaker notes**
Students need permission to distrust impressive-looking AI output.

---

## Slide 6 — Human Review Rules for AI-Assisted Changes

**Core message:** The review bar should be clearer, not lower.

**Bullets**
- Require explicit scope
- Require validation steps
- Prefer small diffs
- Check assumptions against the actual repo
- Treat AI output as a draft, not as evidence

**Suggested visual**
- Review checklist card or gate diagram

**Speaker notes**
This slide is where you transition from AI excitement to engineering discipline.

---

## Slide 7 — Day 3 Exercise: Generate a Repo Health Report with AI

**Core message:** The exercise should produce a concrete report students can compare and critique.

**Bullets**
- Analyze one repo against the project-health framework
- Return ranked problems and recommended next steps
- Highlight uncertainty
- Propose one docs improvement, one test improvement, and one refactor candidate

**Suggested visual**
- Example output template with sections and priorities

**Speaker notes**
Debrief by comparing how different prompts changed the quality of the analysis.
