# Session Checkpoint - 2026-04-09

This checkpoint captures the current state of the Ensemble course work so the next session can resume without rereading the entire repo.

## Context

- User: Justin at Integral Dragon
- Client: Ensemble Health Partners
- Course direction: shifted from general AI-accelerated SDLC toward more practical agentic engineering
- Current phase being taught: `1-Foundations`
- Immediate live-teaching content built in this session: `Session 5` and `Session 6`

## Current Course Tree

```text
ai-assisted-engineering/
  1-Foundations/
    Module-2-Spec-Driven-Development-and-Context-Control/
      Session-5-Spec-Driven-Development/
        Source/
        Artifacts/
        Supplemental/
        Packaging-Instructions.md
      Session-6-Plan-Mode-vs-Act-Mode/
        Source/
        Artifacts/
        Supplemental/
        Packaging-Instructions.md
  2-Labs/
  3-Applied/
  Weekly-Scorecard-Template.md
  Weekly-Scorecard-Template.docx
  Weekly-Scorecard-Week-1-Sample.md
  Weekly-Scorecard-Week-1-Sample.docx
```

## What Was Created

### Session 5
- Slides in Markdown
- Practice and feedback handout in Markdown
- Demo blueprints in Markdown
- Reading/resources in Markdown
- Supplemental research on the agentic delivery landscape
- Supplemental research on emerging paradigms
- Standalone HTML renders for the two supplemental research docs

### Session 6
- Slides in Markdown
- Practice and feedback handout in Markdown
- Demo blueprints in Markdown
- Reading/resources in Markdown

### Packaging Layer
- `Packaging-Instructions.md` exists in both Session 5 and Session 6
- Packaging instructions tell Claude how to turn `Source/` into polished `Artifacts/`
- Intended mapping:
  - slides -> PDF
  - session brief + demo blueprints -> facilitator DOCX
  - practice and feedback -> participant DOCX
  - reading/resources -> optional participant or standalone DOCX
- `Supplemental/` is optional presenter material and not part of the default packaging pass

## Key Supplemental Files

```text
ai-assisted-engineering/
  1-Foundations/
    Module-2-Spec-Driven-Development-and-Context-Control/
      Session-5-Spec-Driven-Development/
        Supplemental/
          Agentic-Delivery-Landscape-Overview.md
          Agentic-Delivery-Landscape-Overview.html
          Emerging-Agentic-Engineering-Paradigms.md
          Emerging-Agentic-Engineering-Paradigms.html
```

## Research Conclusions Already Established

- The field is not settled on one label.
- Useful framing terms:
  - `spec-driven development`
  - `harness engineering`
  - `dark factory` / lights-out software delivery
  - `eval-driven agent development`
  - `policy-as-code`
  - `multi-agent orchestration`
- Recommended teaching position:
  - Use `AI-assisted engineering` as the broad umbrella.
  - Use `Spec-Driven Development and Context Control` as the module label.
  - Treat `harness engineering` and `dark factory` as important landscape concepts rather than the sole course identity.

## Survey Analysis Completed

- Survey source was recovered from the baseline XLSX and supporting materials.
- Cohort size: `26`
- High-level findings already derived:
  - experienced, senior-skewed cohort
  - heavily `.NET`-oriented
  - already high AI usage
  - strongest blockers are output quality, security/privacy, access/setup friction, and reviewability
  - strongest use cases are codebase understanding, testing, and debugging
  - strongest optimization goals are test coverage/fewer regressions, PR throughput, and review quality/smaller diffs
- The survey was interpreted as evidence that Ensemble does not need basic AI awareness training as much as a safer, more reviewable, more measurable engineering workflow

## Measurement / Scorecard Work Completed

- A meeting-ready survey analysis one-pager was written in chat
- A lightweight weekly scorecard was designed
- Files created:

```text
ai-assisted-engineering/
  Weekly-Scorecard-Template.md
  Weekly-Scorecard-Template.docx
  Weekly-Scorecard-Week-1-Sample.md
  Weekly-Scorecard-Week-1-Sample.docx
```

- The Week 1 sample is populated from the actual baseline survey

## ADO vs GitHub Position Already Developed

A leadership-safe argument was prepared in chat:

- Recommendation: use GitHub for course materials and PR-based exercises, while keeping Azure DevOps for planning, governance, and reporting if needed
- Core argument:
  - ADO is a reasonable enterprise control plane
  - GitHub is a better fit for Markdown-heavy, repo-native, PR-centric training workflows
  - This is a fit-for-purpose split, not a platform replacement

This argument was not yet saved into a repo file at the time of this checkpoint.

## Likely Next Actions

1. Save the survey analysis one-pager into the repo and render to DOCX if needed
2. Save the ADO vs GitHub leadership one-pager into the repo and render to DOCX if needed
3. Continue redesigning the rest of `1-Foundations`
4. Use Claude with `Packaging-Instructions.md` plus Justin's style template to generate session artifacts
5. Potentially create executive slide versions of:
   - survey findings
   - measurement plan
   - ADO vs GitHub decision framing

## Key Paths To Reopen First

```text
__meta_workflow/
  Session-Checkpoint-2026-04-09.md

ai-assisted-engineering/
  Weekly-Scorecard-Week-1-Sample.docx
  Weekly-Scorecard-Template.docx
  1-Foundations/
    Module-2-Spec-Driven-Development-and-Context-Control/
      Session-5-Spec-Driven-Development/
      Session-6-Plan-Mode-vs-Act-Mode/
```

## Resume Prompt

Use this if you want to restart quickly in a new session:

> Read [__meta_workflow/Session-Checkpoint-2026-04-09.md](/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/__meta_workflow/Session-Checkpoint-2026-04-09.md) first. We are working on the Ensemble Health Partners AI-assisted engineering course in [ai-assisted-engineering/](/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering). Session 5 and Session 6 source packs, supplemental research, packaging instructions, and weekly scorecard docs already exist. Resume from there and help me with the next deliverable.
