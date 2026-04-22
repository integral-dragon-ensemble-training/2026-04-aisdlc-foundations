# AI-Accelerated Software Development — Applied Practice

**Integral Dragon** · Delivered for Ensemble Health Partners
**Phase 2 of 3** (Foundations → **Applied Practice** → Applied)
**Five workshops**

---

## Course thesis

> AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.

## The five-part method

1. **Define what good looks like.** Establish the quality target before discussing AI.
2. **Identify the debt that blocks it.** Treat technical debt as friction, not just messy code.
3. **Use AI to analyze and improve it.** Targeted inspection, scaffolding, and cleanup.
4. **Validate improvements.** Tests, observability, and security are part of change safety.
5. **Make it repeatable.** Staged modernization and workflow norms beat heroic rewrites.

## Workshops

| # | Title | Theme |
|---|---|---|
| [01](./Workshop-1-What-Good-Looks-Like/) | What Good Looks Like | Define project health in practical terms. |
| [02](./Workshop-2-Technical-Debt-as-Friction/) | Technical Debt as Friction | Friction is the tax the system charges on every change. |
| [03](./Workshop-3-Using-AI-to-Inspect-and-Improve/) | Using AI to Inspect and Improve | Targeted, reviewable AI use on existing codebases. |
| [04](./Workshop-4-Validation-Tests-Observability-Security/) | Validation: Tests, Observability, Security | Confidence beats raw speed. |
| [05](./Workshop-5-Making-It-Repeatable/) | Making It Repeatable | Cleanup becomes a team habit, not a sprint. |

## Overview materials

See [`./overview/`](./overview/) for:
- Course thesis and storyline
- Course map across the five workshops
- Topic bank and cut list
- Course-overview slide deck (HTML + PDF)

## Per-workshop structure

Every workshop folder follows this layout:

```
Workshop-N-<Title>/
├── README.md                        — workshop summary and asset index
├── slides/                          — .md source, .html deck, .pdf render
├── exercises/                       — exercises + rubrics (.md + .docx)
├── resources/                       — curated readings + repos (.md + .docx)
└── instructor/                      — instructor notes, discussion prompts, sample answers, handout
```

## Authoring toolchain

Everything needed to rebuild these decks lives under [`./_template/`](./_template/):

- `slide-template.html` — reference HTML template (McKinsey-blue Integral Dragon style)
- `render-pdf.sh` — HTML → PDF via headless Chrome (1280×720)
- `render-docx.sh` — Markdown → DOCX via pandoc
- `AGENT-BRIEF.md` — instructions for LLM agents building new workshops

## Brand tokens (quick reference)

| Role | Token |
|---|---|
| Background | `#0b1429` (deep navy) |
| Surface | `#17233f` |
| Accent | `#3ab5cc` (cyan/teal) |
| Text | `#f7f9fc` |
| Card background | `#f6f9fc` |
| Card text | `#0b1429` |

Display/body font: Segoe UI / Inter. Monospace labels: SF Mono / Consolas.
Wordmark: `INTEGRAL DRAGON` (uppercase monospace, 0.28em tracking).
