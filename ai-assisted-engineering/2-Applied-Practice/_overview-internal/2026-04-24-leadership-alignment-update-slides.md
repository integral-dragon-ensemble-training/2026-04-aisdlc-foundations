# Applied Practice Alignment Update

Leadership alignment update · Ensemble Health Partners

Foundations complete. Applied Practice expanded from one week to four — and the first of those four is now in hand.

Justin Schmidt · Integral Dragon · 24 April 2026

---

# Where we are now

- Phase 1 — **Foundations** — is complete.
- Phase 2 — **Applied Practice** — began as a single week (Week 3 of the ten-week program). We expanded that one week into four so participants can do the work deliberately instead of sprint through it.
- The four weeks of the expanded Applied Practice: **Baseline** (done) → **Inspect & improve** (next) → **Validate** → **Adopt & review**.
- Week 1 is complete. Participants established a project-health baseline and identified the highest-friction risks in their codebase.
- Three weeks remain inside Applied Practice — focused on improvement, validation, and team adoption.

Status chips:
- Phase 1 · Foundations complete
- Phase 2 · Week 1 of 4 complete

---

# What this phase is doing — and why we expanded it

- Applied Practice shifts the emphasis from *tool familiarity* to *improving project health* in real codebases.
- The original one-week compression did not give participants room to inspect, improve, validate, and review deliberately.
- Four weeks gives each of those moves its own week, with evidence and a concrete output at the end of each.

The four weeks:

| Week | Focus | What participants produce |
|---|---|---|
| 1 | **Inspect** | Project-health baseline + highest-friction areas |
| 2 | **Improve** | One bounded, AI-assisted candidate change on a branch |
| 3 | **Validate** | Tests, observability, and security review of the candidate change |
| 4 | **Review & adopt** | Comparison, adoption decision, and repeatable team practice |

What the expansion buys us:
- Room to do the work, not just hear it explained.
- Evidence collected and reviewed each week, not rolled up at the end.
- Structural improvement we can measure — not self-reported "felt better."

The goal this serves:
- Systems that are easier to **understand**.
- Systems that are safer to **change**.
- Systems that are easier to **govern**.

---

# Sample signals from the analysis

Both sides of the picture. **Quantitative** signals answer "how much, how often." **Qualitative** signals answer "what's the pattern." Each signal is sourced to a specific query or evidence pass — nothing floats.

## Qualitative signals

- **Architecture clarity** — can the team quickly explain system boundaries?
- **Documentation drift** — are critical rules written down, or tribal knowledge?
- **Risk hotspots** — where does change repeatedly cost more than estimated?
- **Testing confidence** — do tests protect risky behavior, or chase coverage?
- **Workflow discipline** — are changes reviewable, and actually reviewed?
- **Highest-leverage next move** — one bounded improvement worth doing first.

## Quantitative signals

- **File churn** — top files by commit frequency, window over window.
- **Co-change pairs** — which files keep moving together.
- **Cycle time** — median hours from change opened to merged.
- **Review depth** — reviewers, comment threads, PR-size distribution.
- **Release signals** — CI pass rate, rollbacks, merge-to-prod latency.
- **Coverage snapshots** — observability on hot paths, lockdown-test presence.

## How we treat any one signal

Every signal is run across **two consecutive windows**. A signal that recurs across both is treated as *structural*. A signal that appears in only one window is flagged as *tentative*. That's what lets us tell leadership "this is real" versus "this was a bad week."
