# Engineering Insight Dashboard — Executive Preview

Three HTML pages and two markdown documents you can show executives to communicate what Claude-assisted engineering analysis actually produces. All values are illustrative — these are mockups, not live data — but each one is built so you can walk from the number back to the ADO query that would produce it.

## The four files to read in order

1. **[`engineering-signals-dashboard.html`](./engineering-signals-dashboard.html)** — *95% confidence.* Direct measurements only. Month-1 vs month-2 comparison showing which findings recur. This is what we can commit to delivering with read-only repo + ADO access. Every tile resolves to a row count or aggregate from `az devops` / `git`.
2. **[`engineering-insight-dashboard.html`](./engineering-insight-dashboard.html)** — *Ambitious.* Adds narrative friction hotspots, dollar/hour cost framing, and forward-looking insights. This is the story we can tell once the signals dashboard has established credibility.
3. **[`engineering-insight-dashboard-reasoning.html`](./engineering-insight-dashboard-reasoning.html)** — Interactive proof layer. Every claim on the ambitious dashboard is an expandable row showing the specific `az devops` / `git` command that would produce it.
4. **[`evidence-sources.md`](./evidence-sources.md)** — The same mapping in plain text, for handoff or print.

Plus:

5. **[`historic-analysis-project-plan.md`](./historic-analysis-project-plan.md)** — 6–9-day project plan to produce real numbers against historic data, recommended as a two-month consistency view.

## Why "insights," not "metrics"

"Metrics" has become political. Teams argue about what to count, and dashboards full of counts rarely answer the question executives actually ask: **"Where is our engineering investment paying off, and where is it leaking?"**

These dashboards use the word **insight** deliberately. Every tile answers a specific engineering question — and the reasoning page shows where the answer came from.

## Tiered confidence

| Dashboard | Confidence | When to use it |
|---|---|---|
| Signals (2-month consistency) | ~95% | First-run. Proves the method works. |
| Ambitious (narrative + cost) | ~85% overall; ~55% on dollar/hour numbers | Second-run, once signals dashboard is accepted. |

**The signals dashboard answers "is this real?"** The ambitious dashboard answers **"so what?"** Lead with the first; earn the right to the second.

## How to use this in an executive conversation

1. **Open `engineering-signals-dashboard.html` first.** Lead with the consistency headline: *"8 of 10 top findings recurred across both months."*
2. **Then open `engineering-insight-dashboard.html`** to show the story the signals can tell, explicitly labeled as a mockup.
3. **If someone pushes back**, open `engineering-insight-dashboard-reasoning.html` and click any row. The query is right there.
4. **Close with the project plan.** "Here's what it takes to produce a real version — one service, two months, six to nine working days."

That framing turns this from an overcommitment into a credible proof-of-concept ask.

## Customizing for a specific pitch

The example codebase is a fictional **Claims Adjudication Service**. To tailor for a real audience:

- Update the hero-tile headline to something specific about their system.
- Swap the three friction hotspots for three real examples from their team's backlog.
- Adjust the scorecard to match what Claude would likely find in their most painful repository.

You don't need to be precise. The dashboards are selling the *shape* of the conversation the methodology produces — not a specific number.

## Rendering notes

All HTML pages are single self-contained files. No build, no server, no external dependencies. Open in any modern browser.

To capture a PDF for a deck or handout:

```bash
/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice/_template/render-pdf.sh \
    engineering-signals-dashboard.html \
    engineering-signals-dashboard.pdf
```

(The standard PDF renderer prints at 1280×720 landscape. For a full-page screenshot at dashboard resolution, use a browser's built-in "Save as PDF" with custom page size.)
