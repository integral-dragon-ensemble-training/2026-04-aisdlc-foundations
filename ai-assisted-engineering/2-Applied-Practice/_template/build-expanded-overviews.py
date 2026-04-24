#!/usr/bin/env python3
"""Generate overview Excalidraw diagrams for all 5 expanded workshops.

Output is one `.excalidraw` file per workshop, written to
`Workshop-N-*-Expanded/resources/workshop-N-expanded-flow.excalidraw`.
Text that sits inside a rectangle is always container-bound, so Excalidraw
auto-centers and wraps it — overlap is impossible. Free-floating labels
(titles, section headers) get an explicit width wide enough to never wrap.

The generator validates that:
  - every container-bound text references an existing rectangle
  - rectangles don't overlap each other
  - all element ids are unique
  - the canvas stays within a declared frame

Running this script is idempotent.
"""
from __future__ import annotations
import json
import random
import string
import time
from pathlib import Path

# --------- palette ----------
NAVY   = ("#1e3a5f", "#dbeafe")   # input / start
PURPLE = ("#6d28d9", "#ddd6fe")   # work / mid
TEAL   = ("#047857", "#a7f3d0")   # output / synthesis
ORANGE = ("#c2410c", "#fed7aa")   # candidate / risk
RED    = ("#dc2626", "#fee2e2")   # guardrails
SLATE  = ("#334155", "#f1f5f9")   # neutral

# --------- helpers ----------
random.seed(42)  # deterministic ids

_counter = [0]
def _id():
    _counter[0] += 1
    return f"el-{_counter[0]:04d}-" + "".join(random.choices(string.ascii_letters + string.digits, k=6))

def _base(index_char):
    return {
        "isDeleted": False,
        "locked": False,
        "link": None,
        "frameId": None,
        "groupIds": [],
        "index": index_char,
        "angle": 0,
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "fillStyle": "solid",
        "boundElements": [],
        "updated": int(time.time() * 1000),
        "seed": random.randint(1, 2**31 - 1),
        "version": 2,
        "versionNonce": random.randint(1, 2**31 - 1),
    }

_index_counter = [0]
def _next_index():
    n = _index_counter[0]
    _index_counter[0] += 1
    # simple a, b, ... aa, ab style
    if n < 26:
        return "a" + chr(ord("a") + n)
    return "b" + chr(ord("a") + (n - 26))

def rect(x, y, w, h, stroke, bg, text=None, font_size=16, round=True):
    """Rectangle, optionally with container-bound text (always auto-centered)."""
    rid = _id()
    r = {
        **_base(_next_index()),
        "id": rid,
        "type": "rectangle",
        "x": x, "y": y,
        "width": w, "height": h,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "roundness": {"type": 3} if round else None,
    }
    elements = [r]
    if text is not None:
        tid = _id()
        r["boundElements"] = [{"type": "text", "id": tid}]
        elements.append({
            **_base(_next_index()),
            "id": tid,
            "type": "text",
            "x": x, "y": y,
            "width": w, "height": h,
            "strokeColor": "#1e293b",
            "backgroundColor": "transparent",
            "roundness": None,
            "text": text,
            "originalText": text,
            "fontSize": font_size,
            "fontFamily": 1,  # Virgil — matches Workshop-1 expanded-flow
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": rid,
            "lineHeight": 1.2,
            "autoResize": False,
            "baseline": font_size,
        })
    return elements, rid

def ellipse(x, y, w, h, stroke, bg, text=None, font_size=15):
    eid = _id()
    e = {
        **_base(_next_index()),
        "id": eid,
        "type": "ellipse",
        "x": x, "y": y,
        "width": w, "height": h,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "roundness": None,
    }
    elements = [e]
    if text is not None:
        tid = _id()
        e["boundElements"] = [{"type": "text", "id": tid}]
        elements.append({
            **_base(_next_index()),
            "id": tid,
            "type": "text",
            "x": x, "y": y,
            "width": w, "height": h,
            "strokeColor": "#1e293b",
            "backgroundColor": "transparent",
            "roundness": None,
            "text": text,
            "originalText": text,
            "fontSize": font_size,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": eid,
            "lineHeight": 1.2,
            "autoResize": False,
            "baseline": font_size,
        })
    return elements, eid

def label(x, y, text, font_size=20, color="#1e40af", width=None, align="left"):
    """Free-floating label. Provide explicit width to prevent wrapping."""
    tid = _id()
    lines = text.split("\n")
    if width is None:
        # approximate pixel width per character for Virgil at this size
        ch_w = font_size * 0.65
        width = int(max(len(l) for l in lines) * ch_w) + 40
    height = int(len(lines) * font_size * 1.2) + 8
    return {
        **_base(_next_index()),
        "id": tid,
        "type": "text",
        "x": x, "y": y,
        "width": width, "height": height,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "roundness": None,
        "text": text,
        "originalText": text,
        "fontSize": font_size,
        "fontFamily": 1,
        "textAlign": align,
        "verticalAlign": "top",
        "containerId": None,
        "lineHeight": 1.2,
        "autoResize": True,
        "baseline": font_size,
    }

def arrow(x1, y1, x2, y2, color="#1e3a5f", points=None):
    """Arrow from (x1,y1) with optional waypoints. Last point gets arrowhead."""
    aid = _id()
    if points is None:
        pts = [[0, 0], [x2 - x1, y2 - y1]]
    else:
        pts = [[0, 0]] + [[p[0] - x1, p[1] - y1] for p in points]
    # width/height are bounding-box size
    all_x = [p[0] for p in pts]
    all_y = [p[1] for p in pts]
    w = max(all_x) - min(all_x) or 1
    h = max(all_y) - min(all_y) or 1
    return {
        **_base(_next_index()),
        "id": aid,
        "type": "arrow",
        "x": x1, "y": y1,
        "width": w, "height": h,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "roundness": {"type": 2},
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow",
        "lastCommittedPoint": None,
        "points": pts,
    }

# --------- layout validation ----------
def validate(elements, frame=(0, 0, 1800, 1100)):
    fx, fy, fw, fh = frame
    ids = set()
    rects_bounds = []
    for el in elements:
        assert el["id"] not in ids, f"duplicate id {el['id']}"
        ids.add(el["id"])
        if el["type"] in ("rectangle", "ellipse"):
            x, y, w, h = el["x"], el["y"], el["width"], el["height"]
            assert fx <= x and x + w <= fx + fw, f"{el['id']} x out of frame"
            assert fy <= y and y + h <= fy + fh, f"{el['id']} y out of frame"
            for other in rects_bounds:
                if _overlap((x, y, w, h), other):
                    raise AssertionError(f"overlap: {el['id']} with {other}")
            rects_bounds.append((x, y, w, h, el["id"]))
        if el["type"] == "text" and el.get("containerId"):
            assert el["containerId"] in ids, f"text {el['id']} binds missing container"

def _overlap(a, b):
    ax, ay, aw, ah = a[:4]
    bx, by, bw, bh = b[:4]
    return not (ax + aw <= bx or bx + bw <= ax or ay + ah <= by or by + bh <= ay)

# --------- serialize ----------
def write_excalidraw(path, elements):
    doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "gridSize": 20,
            "gridStep": 5,
            "gridModeEnabled": False,
            "viewBackgroundColor": "#ffffff",
            "exportScale": 2,
            "exportBackground": True,
            "exportWithDarkMode": False,
            "theme": "light",
        },
        "files": {},
    }
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(doc, indent=2) + "\n")

# --------- diagram builder ----------
def build(num: int, title: str, subtitle: str, intent_box: str,
          flow_steps: list[tuple[str, tuple[str, str]]],
          outputs: list[str], core_idea: str, guardrails: list[str]):
    """Generate a consistent layout:

    +--- title ----+
    +--- subtitle-+
    +--- section: this workshop takes → produces ---+
    [INTENT BOX ..................................................] [OUTPUTS BOX]
    +--- section: the flow ---+
    [step1]→[step2]→[step3]→[step4]→[step5]→[step6]
    +--- section: core idea ---+
    [CORE IDEA BOX .....................................] [GUARDRAIL BOX]
    """
    # reset global counters per diagram
    _counter[0] = 0
    _index_counter[0] = 0

    elements = []

    # --- title row
    elements.append(label(60, 40,
        title, font_size=28, color="#1e40af", width=1400))
    elements.append(label(60, 86,
        subtitle, font_size=16, color="#64748b", width=1400))

    # --- row 1: intent + outputs
    elements.append(label(60, 150, "What this workshop does",
                          font_size=18, color="#1e3a5f", width=400))
    els, intent_id = rect(60, 184, 860, 120, *NAVY, text=intent_box, font_size=16)
    elements.extend(els)

    elements.append(label(960, 150, "What it produces",
                          font_size=18, color="#047857", width=400))
    out_text = "\n".join(f"• {o}" for o in outputs)
    els, _ = rect(960, 184, 500, 120, *TEAL, text=out_text, font_size=14)
    elements.extend(els)

    # --- row 2: flow of steps
    elements.append(label(60, 340, "The expanded flow",
                          font_size=18, color="#6d28d9", width=600))

    step_count = len(flow_steps)
    gap = 30
    total_w = 1400  # x=60..1460
    step_w = (total_w - gap * (step_count - 1)) // step_count
    step_h = 110
    step_y = 380
    prev_right = None
    for i, (text_, palette) in enumerate(flow_steps):
        sx = 60 + i * (step_w + gap)
        els, sid = rect(sx, step_y, step_w, step_h, *palette,
                        text=text_, font_size=14)
        elements.extend(els)
        if prev_right is not None:
            ax1 = prev_right
            ax2 = sx
            ay = step_y + step_h // 2
            elements.append(arrow(ax1 + 4, ay, ax2 - 4, ay, color="#475569"))
        prev_right = sx + step_w

    # --- row 3: core idea + guardrails
    elements.append(label(60, 550, "Core idea",
                          font_size=18, color="#c2410c", width=400))
    els, _ = rect(60, 584, 860, 130, *ORANGE, text=core_idea, font_size=17)
    elements.extend(els)

    elements.append(label(960, 550, "Guardrails",
                          font_size=18, color="#dc2626", width=400))
    gtext = "\n".join(f"• {g}" for g in guardrails)
    els, _ = rect(960, 584, 500, 130, *RED, text=gtext, font_size=13)
    elements.extend(els)

    validate(elements, frame=(0, 0, 1540, 760))
    return elements

# --------- per-workshop content ----------
WORKSHOPS = {
    1: dict(
        title="Workshop 1 Expanded — What Good Looks Like",
        subtitle="AI-assisted scorecard + targeted improvement loop. Evidence gathered by Claude; scoring owned by humans.",
        intent_box=("Give Claude Code a structured definition of \"what good\nlooks like\" so it can collect evidence against nine project-\nhealth categories. Participants then score, pick one weak\ncategory, and apply one small improvement they can validate."),
        flow_steps=[
            ("Create\nscorecard\nskill", NAVY),
            ("Baseline\nrepo scan", NAVY),
            ("Architecture\n& setup\ndeep-dive", PURPLE),
            ("Testing &\nconfidence\ndeep-dive", PURPLE),
            ("Small\ncandidate\nimprovement", ORANGE),
            ("Rescore &\nlog delta", TEAL),
        ],
        outputs=[
            "Repo-local scorecard skill",
            "Baseline scorecard w/ evidence",
            "Architecture & setup notes",
            "One validated improvement",
            "Before/after delta",
        ],
        core_idea=("AI coding tools do not remove the need for engineering\nquality. They increase the payoff from a clear quality\ntarget. The scorecard gives Claude Code a frame;\nhumans own the scoring judgment."),
        guardrails=[
            "Humans own every score",
            "Improvements must be small",
            "Lockdown tests before refactor",
            "No production merges from class",
            "No secrets in training repos",
        ],
    ),
    2: dict(
        title="Workshop 2 Expanded — Technical Debt as Friction",
        subtitle="From scorecard to friction map. Name the tax your system charges on every change.",
        intent_box=("Take the baseline scorecard from Workshop 1 and convert\nweak areas into an evidence-backed friction map. Classify\neach item by debt category, estimate the interest rate,\nand prioritize by impact on change, confidence, and flow."),
        flow_steps=[
            ("Import W1\nscorecard &\nweak areas", NAVY),
            ("Friction\ninventory", PURPLE),
            ("Debt\ntaxonomy\nclassify", PURPLE),
            ("Interest-\nrate\nestimate", PURPLE),
            ("Flow-impact\nprioritize", ORANGE),
            ("Candidate\ndebt-\nreduction\nchange", TEAL),
        ],
        outputs=[
            "Friction inventory with evidence",
            "Debt classified by category",
            "Prioritized debt backlog",
            "One candidate reduction change",
            "Group friction-review notes",
        ],
        core_idea=("Debt should be described as observable friction:\nwho pays the cost, how often they pay it, and what\nchange it slows. Interest is what you are already paying\nover and over — measured, not guessed."),
        guardrails=[
            "Friction must cite real evidence",
            "Interest estimates are rough",
            "Do not rewrite — reduce",
            "Prioritize by flow impact",
            "Group review before action",
        ],
    ),
    3: dict(
        title="Workshop 3 Expanded — Using AI to Inspect and Improve",
        subtitle="Aim Claude Code carefully. Bounded questions, cited evidence, small options.",
        intent_box=("Take the prioritized friction from Workshop 2 and use it\nto aim Claude Code. For each priority, write a bounded\ninspection question, gather evidence, propose small\noptions, and stage one reviewable candidate change."),
        flow_steps=[
            ("Friction\npriority\nfrom W2", NAVY),
            ("Inspection\nquestion", PURPLE),
            ("Evidence-\ngathering\nprompt", PURPLE),
            ("Codebase\nunder-\nstanding", PURPLE),
            ("Improvement\noptions &\ncandidate\nchange", ORANGE),
            ("Review &\nvalidation\npacket", TEAL),
        ],
        outputs=[
            "AI inspection plan",
            "Evidence-backed findings",
            "Tightened prompts",
            "Change plan on branch",
            "Review packet for group",
        ],
        core_idea=("AI should not be asked to \"improve the repo.\" It should\nanswer a bounded engineering question, cite evidence, and\npropose small options. The engineer decides what matters\nand what becomes a change."),
        guardrails=[
            "No open-ended improvement prompts",
            "Every finding cites evidence",
            "Small, reviewable diffs only",
            "Humans own option selection",
            "Review packet before merge",
        ],
    ),
    4: dict(
        title="Workshop 4 Expanded — Validation: Tests, Observability, Security",
        subtitle="Turn candidate changes into validation decisions. Confidence beats raw speed.",
        intent_box=("Take the candidate change branch from Workshop 3 and\nwalk it through a validation matrix. Test, observe, and\nsecurity-check the change. End with a group decision:\napprove, revise, or reject — and capture the rationale."),
        flow_steps=[
            ("Candidate\nbranch\nfrom W3", NAVY),
            ("Validation\nmatrix", PURPLE),
            ("Testing\nconfidence\nreview", PURPLE),
            ("Observability\nreview", PURPLE),
            ("Security &\nsupply-\nchain", ORANGE),
            ("Approve\nrevise\nreject", TEAL),
        ],
        outputs=[
            "Validation matrix",
            "Testing confidence findings",
            "Observability gap findings",
            "Security & supply-chain review",
            "AI change review checklist",
            "Approve / revise / reject decision",
        ],
        core_idea=("Validation is not one thing. A change may need tests, logs,\ntraces, dependency checks, secret checks, deployment\nvisibility, or human review. Pick the gates that fit the\nchange, and document what each one proved."),
        guardrails=[
            "Coverage ≠ confidence",
            "Logs must be diagnostic",
            "Never skip security checks",
            "Decisions must have rationale",
            "Revise is a valid outcome",
        ],
    ),
    5: dict(
        title="Workshop 5 Expanded — Making It Repeatable",
        subtitle="From workshop artifacts to team operating practice. A cadence, not a one-off.",
        intent_box=("Combine the artifacts from Workshops 1–4 — scorecards,\nfriction maps, inspection packets, validation decisions —\ninto a 30-day plan and a set of team working agreements.\nConnect them to the team's board and its review cadence."),
        flow_steps=[
            ("All prior\nartifacts\nW1–W4", NAVY),
            ("30-day\nplan", PURPLE),
            ("Team AI\nworking\nagreements", PURPLE),
            ("Board\n& cadence\nwiring", PURPLE),
            ("Group\nmerge\ndecisions", ORANGE),
            ("Repeatable\noperating\nmodel", TEAL),
        ],
        outputs=[
            "30-day improvement plan",
            "Team AI working agreements",
            "ADO board entries & cadence",
            "Merge-decision record",
            "Repeatable operating model",
        ],
        core_idea=("Do not create a rewrite fantasy. Create a working cadence\nfor small improvements. The 30-day plan is a contract\nbetween the team and its backlog — not a pitch deck,\nnot a one-off sprint."),
        guardrails=[
            "Three quick wins cap",
            "Two structural changes cap",
            "One workflow change per cycle",
            "Measure what changed",
            "Report to the team, not just leadership",
        ],
    ),
}

SUFFIXES = {
    1: "Workshop-1-What-Good-Looks-Like-Expanded",
    2: "Workshop-2-Technical-Debt-as-Friction-Expanded",
    3: "Workshop-3-Using-AI-to-Inspect-and-Improve-Expanded",
    4: "Workshop-4-Validation-Tests-Observability-Security-Expanded",
    5: "Workshop-5-Making-It-Repeatable-Expanded",
}

if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent  # 2-Applied-Practice/
    for num, cfg in WORKSHOPS.items():
        out = root / SUFFIXES[num] / "resources" / f"workshop-{num}-expanded-flow.excalidraw"
        elements = build(num, **cfg)
        write_excalidraw(out, elements)
        print(f"wrote {out} ({len(elements)} elements)")
