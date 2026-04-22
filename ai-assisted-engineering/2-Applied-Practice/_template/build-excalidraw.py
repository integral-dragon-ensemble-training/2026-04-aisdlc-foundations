#!/usr/bin/env python3
"""
Build 6 Excalidraw "teach-from" board files for the Applied Practice (Week 3) course.

Each file contains 4-6 "slide-frames" (1280x720) stacked vertically with a 100px gap.
Each frame: header zone (eyebrow + title) + body zone (rectangles with container-bound text).

Layout rules (enforced):
  * Frame = 1280 x 720. Frame N origin y = N * 820.
  * All elements must fit inside frame bounds (with ~40px padding).
  * Text goes INSIDE rectangles via containerId binding (auto-centered & wrapped).
  * Never free-float stacked text inside a rect.

Brand (Integral Dragon, light theme):
  Background:      #ffffff
  Navy (ink):      #0b1429
  Cyan accent:     #3ab5cc
  Pale cyan tint:  #e6f4f7
  Pale navy tint:  #f4f7fb
"""

import json
import os

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

ROOT = "/Volumes/pragma-aisdlc_1-foundations/aisdlc-course-pipeline-v3/ai-assisted-engineering/2-Applied-Practice"

NAVY = "#0b1429"
CYAN = "#3ab5cc"
PALE_CYAN = "#e6f4f7"
PALE_NAVY = "#f4f7fb"
WHITE = "#ffffff"
TRANSPARENT = "transparent"

FRAME_W = 1280
FRAME_H = 720
FRAME_GAP = 100
FRAME_STRIDE = FRAME_H + FRAME_GAP  # 820

# Body zone (frame-relative)
BODY_Y = 200
BODY_BOTTOM = 700  # max y offset inside frame
PAD = 40

TS = 1735000000000

_next_seed = [10_000]


def next_seed():
    _next_seed[0] += 1
    return _next_seed[0]


# --------------------------------------------------------------------------
# Element builders
# --------------------------------------------------------------------------

def base_element(id_, type_, x, y, w, h, stroke, bg, *, fill_style="solid",
                 stroke_width=2, roughness=1, frame_id=None, roundness=None,
                 bound=None):
    s = next_seed()
    return {
        "id": id_,
        "type": type_,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "fillStyle": fill_style,
        "strokeWidth": stroke_width,
        "strokeStyle": "solid",
        "roughness": roughness,
        "opacity": 100,
        "groupIds": [],
        "frameId": frame_id,
        "roundness": roundness,
        "seed": s,
        "versionNonce": s,
        "isDeleted": False,
        "boundElements": bound,
        "updated": TS,
        "link": None,
        "locked": False,
    }


def make_frame(slide_index, name):
    y = slide_index * FRAME_STRIDE
    fid = f"frame-{slide_index + 1:02d}"
    el = base_element(
        id_=fid, type_="frame",
        x=0, y=y, w=FRAME_W, h=FRAME_H,
        stroke=NAVY, bg=TRANSPARENT,
        stroke_width=2, roughness=0,
    )
    el["name"] = name
    el["customData"] = None
    return fid, el


def make_rect(id_, frame_id, x, y, w, h, *, fill=WHITE, stroke=NAVY,
              rounded=True, bound=None):
    roundness = {"type": 3} if rounded else None
    return base_element(
        id_=id_, type_="rectangle",
        x=x, y=y, w=w, h=h,
        stroke=stroke, bg=fill, fill_style="solid",
        stroke_width=2, roughness=1, frame_id=frame_id,
        roundness=roundness, bound=bound,
    )


def make_text(id_, frame_id, x, y, text, *, size=20, family=1, color=NAVY,
              align="left", valign="top", w=None, h=None, container_id=None):
    lines = text.split("\n")
    line_count = len(lines)
    max_chars = max((len(l) for l in lines), default=1)
    approx_char_w = size * 0.58
    if w is None:
        w = int(max_chars * approx_char_w) + 10
    if h is None:
        h = int(size * 1.25 * line_count) + 4

    s = next_seed()
    return {
        "id": id_,
        "type": "text",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": color,
        "backgroundColor": TRANSPARENT,
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": frame_id,
        "roundness": None,
        "seed": s,
        "versionNonce": s,
        "isDeleted": False,
        "boundElements": None,
        "updated": TS,
        "link": None,
        "locked": False,
        "text": text,
        "fontSize": size,
        "fontFamily": family,
        "textAlign": align,
        "verticalAlign": valign,
        "containerId": container_id,
        "originalText": text,
        "autoResize": False if container_id else True,
        "lineHeight": 1.25,
    }


# --------------------------------------------------------------------------
# Composition patterns
# --------------------------------------------------------------------------

def slide_header(frame_id, slide_index, title, eyebrow=None, title_color=NAVY):
    """Eyebrow (14 mono cyan) + title (40 Virgil navy) free-floating in header zone."""
    base_y = slide_index * FRAME_STRIDE
    els = []
    if eyebrow:
        els.append(make_text(
            f"{frame_id}-eyebrow", frame_id,
            x=PAD, y=base_y + 40,
            text=eyebrow, size=14, family=3, color=CYAN,
            w=FRAME_W - 2 * PAD,
        ))
    els.append(make_text(
        f"{frame_id}-title", frame_id,
        x=PAD, y=base_y + 70,
        text=title, size=40, family=1, color=title_color,
        w=FRAME_W - 2 * PAD,
    ))
    return els


def rect_with_text(frame_id, key, x, y, w, h, text, *,
                   fill=WHITE, stroke=NAVY,
                   text_color=NAVY, text_size=18, text_family=2,
                   text_align="center", text_valign="middle"):
    """
    One rect with a single container-bound text element.
    Text is centered (horizontally + vertically) and wrapped by Excalidraw.
    """
    rid = f"{frame_id}-{key}-rect"
    tid = f"{frame_id}-{key}-text"

    rect = make_rect(rid, frame_id, x, y, w, h, fill=fill, stroke=stroke,
                     bound=[{"id": tid, "type": "text"}])

    # Bound text: positioned relative to rect, width = rect width - 20
    txt = make_text(
        tid, frame_id,
        x=x + 10, y=y + 10,
        text=text, size=text_size, family=text_family, color=text_color,
        align=text_align, valign=text_valign,
        w=w - 20, h=h - 20,
        container_id=rid,
    )
    return [rect, txt]


def free_text(frame_id, key, x, y, text, **kw):
    return make_text(f"{frame_id}-{key}", frame_id, x=x, y=y, text=text, **kw)


# --------------------------------------------------------------------------
# File builder with layout sanity check
# --------------------------------------------------------------------------

def validate_layout(elements):
    """Each non-frame element must sit inside its frame rectangle."""
    frames = {e["id"]: e for e in elements if e["type"] == "frame"}
    for el in elements:
        if el["type"] == "frame":
            continue
        fid = el.get("frameId")
        if fid is None or fid not in frames:
            continue
        fr = frames[fid]
        fx, fy = fr["x"], fr["y"]
        fw, fh = fr["width"], fr["height"]
        ex, ey = el["x"], el["y"]
        ew, eh = el["width"], el["height"]
        if not (fx <= ex and ex + ew <= fx + fw and
                fy <= ey and ey + eh <= fy + fh):
            raise AssertionError(
                f"Element {el['id']} ({el['type']}) overflows frame {fid}: "
                f"el=({ex},{ey},{ew},{eh}) frame=({fx},{fy},{fw},{fh})"
            )


def build_file(out_path, frames_data):
    elements = []
    for i, fd in enumerate(frames_data):
        fid, frame_el = make_frame(i, fd["name"])
        elements.append(frame_el)
        elements.extend(fd["builder"](i, fid))

    validate_layout(elements)

    doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://integraldragon.com/applied-practice",
        "elements": elements,
        "appState": {
            "gridSize": 20,
            "viewBackgroundColor": "#ffffff",
        },
        "files": {},
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(doc, f, indent=2)
    return len(elements)


# --------------------------------------------------------------------------
# Helpers for common grid layouts inside body zone
# --------------------------------------------------------------------------
# Body zone: x in [PAD, FRAME_W-PAD] = [40, 1240], width 1200
# Body zone: y-offset in [BODY_Y, BODY_BOTTOM] = [200, 700], height 500

def frame_y(i, offset):
    return i * FRAME_STRIDE + offset


def grid_positions(cols, rows, *, x0=PAD, y0=BODY_Y, total_w=FRAME_W - 2*PAD,
                   total_h=500, gap_x=16, gap_y=16):
    """Return list of (x, y, w, h) cell rects, frame-relative."""
    cell_w = (total_w - gap_x * (cols - 1)) // cols
    cell_h = (total_h - gap_y * (rows - 1)) // rows
    out = []
    for r in range(rows):
        for c in range(cols):
            x = x0 + c * (cell_w + gap_x)
            y = y0 + r * (cell_h + gap_y)
            out.append((x, y, cell_w, cell_h))
    return out


# --------------------------------------------------------------------------
# FILE 1 — Overview (5 slide-frames)
# --------------------------------------------------------------------------

def overview_slide_1(i, fid):
    """Course thesis — navy hero."""
    els = slide_header(fid, i,
        title="The point is not more code.",
        eyebrow="APPLIED PRACTICE  ·  COURSE THESIS")
    # Subtitle line free-floating under title
    els.append(free_text(fid, "subtitle",
        x=PAD, y=frame_y(i, 125),
        text="The point is easier change.",
        size=32, family=1, color=CYAN, w=FRAME_W - 2*PAD,
    ))
    # Navy hero rect
    text = ("AI-assisted engineering is most valuable\n"
            "when it helps teams see, reduce, and pay down\n"
            "the friction that makes software hard to change.\n"
            "\n"
            "Most teams are constrained by friction, not typing speed.\n"
            "AI's best patterns: inspect, explain, clean up, validate.")
    els += rect_with_text(fid, "hero",
        x=PAD, y=frame_y(i, 220), w=FRAME_W - 2*PAD, h=440,
        text=text,
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


def overview_slide_2(i, fid):
    """Five-part method — 5 columns."""
    els = slide_header(fid, i,
        title="The Five-Part Method",
        eyebrow="FROM FRICTION TO FLOW")
    steps = [
        ("1  INSPECT",      "Make the system\nvisible. Scan docs,\ncode, deploys."),
        ("2  PRIORITIZE",   "Rank friction by\nchange cost, risk,\nand frequency."),
        ("3  IMPROVE",      "Small, scoped\nchanges. Docs, tests,\nrefactors."),
        ("4  VALIDATE",     "Tests, observability,\nsecurity gates."),
        ("5  STANDARDIZE",  "Turn wins into team\nhabit: checklists,\ntemplates, CI."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE, PALE_CYAN]
    cells = grid_positions(5, 1, y0=frame_y(i, BODY_Y) + 60, total_h=380, gap_x=12)
    for idx, (lbl, body) in enumerate(steps):
        x, y, w, h = cells[idx]
        text = f"{lbl}\n\n{body}"
        els += rect_with_text(fid, f"s{idx}",
            x=x, y=y, w=w, h=h,
            text=text,
            fill=fills[idx], stroke=NAVY,
            text_size=16, text_family=2)
    return els


def overview_slide_3(i, fid):
    """Five sessions at a glance — 5 rows."""
    els = slide_header(fid, i,
        title="Five Sessions at a Glance",
        eyebrow="WEEK-LONG ARC")
    sessions = [
        ("DAY 1", "What Good Looks Like",          "Project health across 9 categories. A scoreable target."),
        ("DAY 2", "Technical Debt as Friction",    "Debt as a repeated tax on change. The nine categories."),
        ("DAY 3", "Using AI to Inspect & Improve", "Capability map, prompt shape, review discipline."),
        ("DAY 4", "Validation: Tests, Obs, Sec",   "Confidence beats coverage. Evidence for every change."),
        ("DAY 5", "Making It Repeatable",          "Staged modernization. 30-day team plan."),
    ]
    y0 = frame_y(i, BODY_Y)
    row_h = 82
    gap = 10
    for idx, (day, title, body) in enumerate(sessions):
        ry = y0 + idx * (row_h + gap)
        # Day tag (navy)
        els += rect_with_text(fid, f"d{idx}-tag",
            x=PAD, y=ry, w=140, h=row_h,
            text=day,
            fill=NAVY, stroke=NAVY,
            text_color=WHITE, text_size=22, text_family=1)
        # Body (title \n body)
        els += rect_with_text(fid, f"d{idx}-body",
            x=PAD + 150, y=ry, w=FRAME_W - 2*PAD - 150, h=row_h,
            text=f"{title}\n{body}",
            fill=WHITE, stroke=NAVY,
            text_color=NAVY, text_size=16, text_family=2)
    return els


def overview_slide_4(i, fid):
    """Where AI helps vs. where AI risks — 2 columns."""
    els = slide_header(fid, i,
        title="Where AI Helps  ·  Where AI Risks",
        eyebrow="USE IT WELL, NOT WIDELY")
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 460

    helps_text = ("AI HELPS\n\n"
                  "Summarize a codebase\n"
                  "Find patterns & inconsistencies\n"
                  "Identify doc gaps\n"
                  "Generate initial tests / scaffolds\n"
                  "Propose small refactors\n"
                  "Draft cleanup plans & checklists")
    risks_text = ("AI RISKS\n\n"
                  "Rewrites without understanding\n"
                  "Tests that assert trivia\n"
                  "Plausible but wrong docs\n"
                  "Unreviewed security changes\n"
                  "Oversized diffs no one absorbs\n"
                  "Confident summaries hiding uncertainty")

    els += rect_with_text(fid, "helps",
        x=PAD, y=y0, w=col_w, h=h,
        text=helps_text,
        fill=PALE_CYAN, stroke=CYAN,
        text_size=18, text_family=2)
    els += rect_with_text(fid, "risks",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text=risks_text,
        fill=WHITE, stroke=NAVY,
        text_size=18, text_family=2)
    return els


def overview_slide_5(i, fid):
    """Mature usage — AI vs humans."""
    els = slide_header(fid, i,
        title="Mature Use of AI in Engineering",
        eyebrow="THE OPERATING MODEL")
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 340

    els += rect_with_text(fid, "ai",
        x=PAD, y=y0, w=col_w, h=h,
        text="AI\n\nInspect. Explain.\nPropose. Scaffold.\nStandardize repetitive work.",
        fill=PALE_CYAN, stroke=CYAN,
        text_size=22, text_family=1)
    els += rect_with_text(fid, "humans",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text="HUMANS\n\nDecide. Validate. Own.\nPrioritize & trade off.\nApprove production risk.",
        fill=PALE_NAVY, stroke=NAVY,
        text_size=22, text_family=1)

    # Closing line as a rect for consistent placement
    els += rect_with_text(fid, "close",
        x=PAD, y=y0 + h + 20, w=FRAME_W - 2*PAD, h=100,
        text="Treat AI output as draft material with a burden of proof.",
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


OVERVIEW_FRAMES = [
    {"name": "Slide 01 - Course Thesis",        "builder": overview_slide_1},
    {"name": "Slide 02 - Five-Part Method",     "builder": overview_slide_2},
    {"name": "Slide 03 - Five Sessions",        "builder": overview_slide_3},
    {"name": "Slide 04 - AI Helps vs AI Risks", "builder": overview_slide_4},
    {"name": "Slide 05 - Mature AI Usage",      "builder": overview_slide_5},
]


# --------------------------------------------------------------------------
# FILE 2 — Session 1: What Good Looks Like (5 frames)
# --------------------------------------------------------------------------

def s1_slide_1(i, fid):
    els = slide_header(fid, i,
        title="What Good Looks Like",
        eyebrow="DAY 1  ·  PROJECT HEALTH")
    text = ("A healthy project is not perfection.\n"
            "It is a system that is easy to change safely.\n"
            "\n"
            "Understandable   Reproducible   Testable\n"
            "Observable   Operable   Secure-enough\n"
            "\n"
            "Good engineering fundamentals make AI more useful.")
    els += rect_with_text(fid, "target",
        x=PAD, y=frame_y(i, BODY_Y), w=FRAME_W - 2*PAD, h=460,
        text=text,
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


def s1_slide_2(i, fid):
    """Nine categories grouped into three buckets — 3 cols."""
    els = slide_header(fid, i,
        title="Nine Health Categories, Three Buckets",
        eyebrow="BEYOND CLEAN CODE")
    buckets = [
        ("CODE & STRUCTURE", PALE_CYAN, CYAN,
         "1  Documentation\n2  Architecture\n3  Testability"),
        ("OPS & RUNTIME", PALE_NAVY, NAVY,
         "4  Setup & Environment\n5  Build, Deploy, Release\n6  Data & Schema\n7  Observability"),
        ("WORKFLOW & TRUST", WHITE, NAVY,
         "8  Security & Supply Chain\n9  Workflow & Review"),
    ]
    cells = grid_positions(3, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=20)
    for idx, (lbl, fill, stroke, items) in enumerate(buckets):
        x, y, w, h = cells[idx]
        text = f"{lbl}\n\n{items}"
        els += rect_with_text(fid, f"b{idx}",
            x=x, y=y, w=w, h=h,
            text=text,
            fill=fill, stroke=stroke,
            text_size=18, text_family=2)
    return els


def s1_slide_3(i, fid):
    """Top-12 checklist — 2 columns."""
    els = slide_header(fid, i,
        title="The Top-12 Checks",
        eyebrow="COMPACT SCORECARD")
    left = ("1  README is trustworthy\n"
            "2  Architecture is legible\n"
            "3  Local setup is reproducible\n"
            "4  Builds in a clean environment\n"
            "5  Tests provide real confidence\n"
            "6  Schema changes are versioned")
    right = ("7  Test data is intentional\n"
             "8  Versions & releases are visible\n"
             "9  Deployments can be verified\n"
             "10  Logs, metrics, traces explain\n"
             "11  Secrets & dep risk are managed\n"
             "12  Workflow supports improvement")
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 460
    els += rect_with_text(fid, "left",
        x=PAD, y=y0, w=col_w, h=h,
        text=left,
        fill=WHITE, stroke=NAVY,
        text_size=20, text_family=2, text_align="left")
    els += rect_with_text(fid, "right",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text=right,
        fill=PALE_CYAN, stroke=CYAN,
        text_size=20, text_family=2, text_align="left")
    return els


def s1_slide_4(i, fid):
    """Where AI helps on Day 1 — 4 columns."""
    els = slide_header(fid, i,
        title="Where AI Helps on Day 1",
        eyebrow="INSPECTION LEVERAGE")
    items = [
        ("SUMMARIZE", "Repo tour.\nModule roles.\nEntry points."),
        ("COMPARE",   "Docs vs. actual code.\nREADME claims\nvs. reality."),
        ("SCORECARD", "First-pass rating\nof the 9\ncategories."),
        ("FLAG",      "Missing docs.\nUnclear setup.\nUndocumented\nscripts."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE]
    cells = grid_positions(4, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=16)
    for idx, (lbl, body) in enumerate(items):
        x, y, w, h = cells[idx]
        text = f"{lbl}\n\n{body}"
        els += rect_with_text(fid, f"c{idx}",
            x=x, y=y, w=w, h=h,
            text=text,
            fill=fills[idx], stroke=NAVY,
            text_size=18, text_family=2)
    return els


def s1_slide_5(i, fid):
    els = slide_header(fid, i,
        title="Set the Target Before You Measure Debt",
        eyebrow="CLOSING")
    text = ("Project health = Changeability + Confidence.\n"
            "\n"
            "If you cannot define healthy qualities,\n"
            "AI will happily optimize the wrong thing.\n"
            "\n"
            "Exercise: score one real repo against the Top-12.\n"
            "Pick the three weaknesses that cost the team most.")
    els += rect_with_text(fid, "close",
        x=PAD, y=frame_y(i, BODY_Y), w=FRAME_W - 2*PAD, h=460,
        text=text,
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


SESSION_1_FRAMES = [
    {"name": "Slide 01 - The Target",        "builder": s1_slide_1},
    {"name": "Slide 02 - Nine Categories",   "builder": s1_slide_2},
    {"name": "Slide 03 - Top 12 Checklist",  "builder": s1_slide_3},
    {"name": "Slide 04 - Where AI Helps",    "builder": s1_slide_4},
    {"name": "Slide 05 - Closing",           "builder": s1_slide_5},
]


# --------------------------------------------------------------------------
# FILE 3 — Session 2: Technical Debt as Friction (5 frames)
# --------------------------------------------------------------------------

def s2_slide_1(i, fid):
    els = slide_header(fid, i,
        title="Technical Debt Is Friction",
        eyebrow="DAY 2  ·  DEFINITION")
    text = ("Technical debt is any deficiency\n"
            "that raises the cost, risk, or time\n"
            "of future changes.\n"
            "\n"
            '"The repeated tax paid when the system resists change."\n'
            "\n"
            "It lives in code, docs, env, data, release, and ops.")
    els += rect_with_text(fid, "def",
        x=PAD, y=frame_y(i, BODY_Y), w=FRAME_W - 2*PAD, h=460,
        text=text,
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


def s2_slide_2(i, fid):
    """Nine debt categories — 3x3 grid."""
    els = slide_header(fid, i,
        title="The Nine Debt Categories",
        eyebrow="DIAGNOSE, DON'T VENT")
    cats = [
        ("1  KNOWLEDGE",           "Missing or misleading\nunderstanding."),
        ("2  DESIGN",              "Structure that makes\nchange unnecessarily hard."),
        ("3  ENVIRONMENT",         "Drift in dev and\ntest environments."),
        ("4  QUALITY-CONFIDENCE",  "You can't tell if a\nchange is safe."),
        ("5  RELEASE",             "Build, version,\ndeploy friction."),
        ("6  DATA & SCHEMA",       "Fragile migrations,\nmystery state."),
        ("7  OBSERVABILITY",       "Can't understand\nruntime efficiently."),
        ("8  SECURITY",            "Exposure or supply-\nchain weakness."),
        ("9  WORKFLOW",            "Processes that\nresist healthy change."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY,
             WHITE, PALE_CYAN, PALE_NAVY,
             PALE_NAVY, PALE_CYAN, WHITE]
    cells = grid_positions(3, 3, y0=frame_y(i, BODY_Y), total_h=460,
                           gap_x=14, gap_y=12)
    for idx, (lbl, body) in enumerate(cats):
        x, y, w, h = cells[idx]
        text = f"{lbl}\n{body}"
        els += rect_with_text(fid, f"d{idx}",
            x=x, y=y, w=w, h=h,
            text=text,
            fill=fills[idx], stroke=NAVY,
            text_size=15, text_family=2)
    return els


def s2_slide_3(i, fid):
    els = slide_header(fid, i,
        title="Debt and Interest",
        eyebrow="WHY FRICTION COMPOUNDS")
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 460
    els += rect_with_text(fid, "principal",
        x=PAD, y=y0, w=col_w, h=h,
        text=("PRINCIPAL\n\n"
              "The underlying deficiency.\n\n"
              "Unreliable setup\n"
              "Stale docs\n"
              "Unclear boundaries\n"
              "Manual deploys"),
        fill=PALE_NAVY, stroke=NAVY,
        text_size=18, text_family=2)
    els += rect_with_text(fid, "interest",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text=("INTEREST\n\n"
              "The repeated extra cost.\n\n"
              "+2 days per new hire\n"
              "Slack archaeology before every change\n"
              "Read 5 modules for a 1-line fix\n"
              "Fear of production changes"),
        fill=PALE_CYAN, stroke=CYAN,
        text_size=18, text_family=2)
    return els


def s2_slide_4(i, fid):
    """Prioritization 2x2."""
    els = slide_header(fid, i,
        title="Prioritize by Leverage",
        eyebrow="IMPACT ON FLOW  x  COST TO FIX")
    # 2x2 grid centered
    grid_w = 900
    grid_h = 440
    gx = (FRAME_W - grid_w) // 2
    gy = frame_y(i, BODY_Y)
    cw = (grid_w - 16) // 2
    ch = (grid_h - 16) // 2

    quads = [
        ("QUICK WINS",        "High impact, low cost.\nDo first.",             PALE_CYAN, CYAN, NAVY),
        ("STRUCTURAL BETS",   "High impact, high cost.\nPlan and stage.",      NAVY, NAVY, WHITE),
        ("FILLERS",           "Low impact, low cost.\nBatch opportunistically.", WHITE, NAVY, NAVY),
        ("DEFER / REJECT",    "Low impact, high cost.\nBeautification trap.",  PALE_NAVY, NAVY, NAVY),
    ]
    coords = [
        (gx, gy),
        (gx + cw + 16, gy),
        (gx, gy + ch + 16),
        (gx + cw + 16, gy + ch + 16),
    ]
    for idx, ((lbl, body, fill, stroke, txt_c), (x, y)) in enumerate(zip(quads, coords)):
        els += rect_with_text(fid, f"q{idx}",
            x=x, y=y, w=cw, h=ch,
            text=f"{lbl}\n\n{body}",
            fill=fill, stroke=stroke,
            text_color=txt_c, text_size=18, text_family=1)
    return els


def s2_slide_5(i, fid):
    els = slide_header(fid, i,
        title="AI's Role on Day 2",
        eyebrow="ACCELERATE INSPECTION, NOT TRADEOFFS")
    steps = [
        ("REPO TOUR",   "Summarize structure\nand ownership."),
        ("INVENTORY",   "List friction sources\nand symptoms."),
        ("CLASSIFY",    "Map findings to the\nnine categories."),
        ("RANK BACKLOG","Quick wins vs.\nstructural work."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE]
    cells = grid_positions(4, 1, y0=frame_y(i, BODY_Y), total_h=380, gap_x=16)
    for idx, (lbl, body) in enumerate(steps):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"s{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fills[idx], stroke=NAVY,
            text_size=18, text_family=2)

    # Note card below grid
    note_y = frame_y(i, BODY_Y) + 400
    els += rect_with_text(fid, "note",
        x=PAD, y=note_y, w=FRAME_W - 2*PAD, h=70,
        text="AI does not decide the tradeoffs. Humans do.",
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=20, text_family=1)
    return els


SESSION_2_FRAMES = [
    {"name": "Slide 01 - Debt = Friction",     "builder": s2_slide_1},
    {"name": "Slide 02 - Nine Categories",     "builder": s2_slide_2},
    {"name": "Slide 03 - Debt & Interest",     "builder": s2_slide_3},
    {"name": "Slide 04 - Prioritization 2x2",  "builder": s2_slide_4},
    {"name": "Slide 05 - AI's Role on Day 2",  "builder": s2_slide_5},
]


# --------------------------------------------------------------------------
# FILE 4 — Session 3: Using AI to Inspect and Improve (5 frames)
# --------------------------------------------------------------------------

def s3_slide_1(i, fid):
    els = slide_header(fid, i,
        title="The AI Capability Map",
        eyebrow="DAY 3  ·  WHAT AI IS GOOD AT")
    caps = [
        ("INSPECT",  "Scan a repo.\nFind patterns &\ninconsistencies."),
        ("EXPLAIN",  "Summarize modules.\nTrace cross-cutting\nlogic."),
        ("PROPOSE",  "Cleanup plans.\nSmall refactor &\ntest ideas."),
        ("SCAFFOLD", "Draft tests, docs,\nlogging, checklists,\nmigration notes."),
    ]
    fills = [PALE_CYAN, PALE_NAVY, PALE_CYAN, PALE_NAVY]
    strokes = [CYAN, NAVY, CYAN, NAVY]
    cells = grid_positions(4, 1, y0=frame_y(i, BODY_Y), total_h=380, gap_x=16)
    for idx, (lbl, body) in enumerate(caps):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"c{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fills[idx], stroke=strokes[idx],
            text_size=18, text_family=2)

    note_y = frame_y(i, BODY_Y) + 400
    els += rect_with_text(fid, "note",
        x=PAD, y=note_y, w=FRAME_W - 2*PAD, h=70,
        text='"Use AI to inspect, explain, propose, and scaffold.  Humans decide, validate, and own."',
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=18, text_family=1)
    return els


def s3_slide_2(i, fid):
    els = slide_header(fid, i,
        title="The Shape of a Strong Prompt",
        eyebrow="SPECIFIC CONTEXT, USEFUL OUTPUT")
    parts = [
        ("SCOPE",            "Which files, modules,\nor commits?"),
        ("STACK",            "Language, framework,\nversion constraints."),
        ("QUALITY CRITERIA", "What 'good' means.\nEdge cases to cover."),
        ("OUTPUT FORMAT",    "Ranked findings.\nTables, checklists,\ndiffs - not prose."),
        ("UNCERTAINTY",      "Ask it to flag\nassumptions it made."),
    ]
    cells = grid_positions(5, 1, y0=frame_y(i, BODY_Y), total_h=380, gap_x=12)
    for idx, (lbl, body) in enumerate(parts):
        x, y, w, h = cells[idx]
        fill = PALE_CYAN if idx % 2 == 0 else WHITE
        els += rect_with_text(fid, f"p{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fill, stroke=NAVY,
            text_size=16, text_family=2)

    note_y = frame_y(i, BODY_Y) + 400
    els += rect_with_text(fid, "note",
        x=PAD, y=note_y, w=FRAME_W - 2*PAD, h=70,
        text="Prefer inspectable outputs over fluent prose.",
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=20, text_family=1)
    return els


def s3_slide_3(i, fid):
    """AI failure modes — 3x2 grid."""
    els = slide_header(fid, i,
        title="AI Failure Modes",
        eyebrow="FLUENT OVERREACH")
    items = [
        ("HALLUCINATED ARCHITECTURE", "Structure that sounds plausible\nbut doesn't match the code."),
        ("SHALLOW TESTS",             "Assert implementation trivia,\nnot behavior."),
        ("UNSAFE REFACTORS",          "Edits whose impact surface\nwasn't understood."),
        ("OVERSIZED DIFFS",           "Changes too large for anyone\nto review well."),
        ("CONFIDENT SUMMARIES",       "Smooth prose that hides\nuncertainty."),
        ("UNREQUESTED COMPLEXITY",    "Generated abstractions no\none asked for."),
    ]
    cells = grid_positions(2, 3, y0=frame_y(i, BODY_Y), total_h=460,
                           gap_x=20, gap_y=10)
    for idx, (lbl, body) in enumerate(items):
        x, y, w, h = cells[idx]
        fill = PALE_NAVY if idx % 2 == 0 else WHITE
        els += rect_with_text(fid, f"f{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fill, stroke=NAVY,
            text_size=16, text_family=2)
    return els


def s3_slide_4(i, fid):
    els = slide_header(fid, i,
        title="Human Review Rules",
        eyebrow="THE BAR IS CLEARER, NOT LOWER")
    rules = [
        ("1  EXPLICIT SCOPE",     "What is in and\nout of the change."),
        ("2  SMALL DIFFS",        "Reviewable by a\nreal human."),
        ("3  ASSUMPTIONS STATED", "Check AI's claims\nagainst the repo."),
        ("4  VALIDATION",         "Tests, logs, or eyes.\nEvidence, not vibes."),
        ("5  DRAFT, NOT PROOF",   "AI output never\nstands alone."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE, PALE_CYAN]
    cells = grid_positions(5, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=12)
    for idx, (lbl, body) in enumerate(rules):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"r{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fills[idx], stroke=NAVY,
            text_size=16, text_family=2)
    return els


def s3_slide_5(i, fid):
    els = slide_header(fid, i,
        title="Safe, High-Value Uses on Day 3",
        eyebrow="SMALL, SCOPED, REVIEWABLE")
    cols = [
        ("DOCS & ARCHITECTURE",
         "README refresh\ncandidates.\nModule role summaries.\nC4 component\nfirst pass.\nUnanswered questions\nlist.",
         PALE_CYAN, CYAN),
        ("TESTS",
         "Candidate tests for\none component.\nSeams for isolation.\nFixture cleanup\nsuggestions.\nRegression-risk\nmapping.",
         WHITE, NAVY),
        ("REFACTOR & CLEANUP",
         "Small scoped\nrefactors.\nLogging or error-\nhandling lifts.\nRepetitive cleanup\nunder clear rules.",
         PALE_NAVY, NAVY),
    ]
    cells = grid_positions(3, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=20)
    for idx, (lbl, body, fill, stroke) in enumerate(cols):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"u{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fill, stroke=stroke,
            text_size=17, text_family=2)
    return els


SESSION_3_FRAMES = [
    {"name": "Slide 01 - AI Capability Map",     "builder": s3_slide_1},
    {"name": "Slide 02 - Strong Prompt Shape",   "builder": s3_slide_2},
    {"name": "Slide 03 - AI Failure Modes",      "builder": s3_slide_3},
    {"name": "Slide 04 - Human Review Rules",    "builder": s3_slide_4},
    {"name": "Slide 05 - Safe High-Value Uses",  "builder": s3_slide_5},
]


# --------------------------------------------------------------------------
# FILE 5 — Session 4: Validation (5 frames)
# --------------------------------------------------------------------------

def s4_slide_1(i, fid):
    els = slide_header(fid, i,
        title="Improvements Only Count if Validated",
        eyebrow="DAY 4  ·  THE GUARDRAIL")
    text = ("AI-generated change  +  validation\n"
            "=  trustworthy improvement\n"
            "\n"
            '"If you cannot validate the change,\n'
            'AI only helped you move faster in the dark."\n'
            "\n"
            "A plausible diff is not a safe diff.")
    els += rect_with_text(fid, "eq",
        x=PAD, y=frame_y(i, BODY_Y), w=FRAME_W - 2*PAD, h=460,
        text=text,
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


def s4_slide_2(i, fid):
    els = slide_header(fid, i,
        title="Coverage vs. Confidence",
        eyebrow='"COVERAGE IS A COUNT. CONFIDENCE IS A CAPABILITY."')
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 460
    els += rect_with_text(fid, "coverage",
        x=PAD, y=y0, w=col_w, h=h,
        text=("COVERAGE\n\n"
              "A percentage.\n\n"
              "Can be high while tests\n"
              "assert implementation trivia,\n"
              "run flakily, or test the\n"
              "wrong behavior."),
        fill=PALE_NAVY, stroke=NAVY,
        text_size=18, text_family=2)
    els += rect_with_text(fid, "confidence",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text=("CONFIDENCE\n\n"
              "A capability.\n\n"
              "Tests tied to important\n"
              "behaviors and failure modes.\n"
              "Fast feedback. Trustworthy\n"
              "fixtures. No flakes."),
        fill=PALE_CYAN, stroke=CYAN,
        text_size=18, text_family=2)
    return els


def s4_slide_3(i, fid):
    els = slide_header(fid, i,
        title="Observability Is Part of Maintainability",
        eyebrow="A SYSTEM THAT EXPLAINS ITSELF IS SAFER TO CHANGE")
    pillars = [
        ("LOGS",              "Structured.\nCorrelation IDs.\nSupport diagnosis,\nnot guesswork."),
        ("METRICS",           "Reflect behavior\nand failure,\nnot just uptime."),
        ("TRACES",            "Connect the\nrequest path\nacross service\nboundaries."),
        ("DEPLOY VISIBILITY", "Know what version\nis live, where,\nand if it's\nhealthy."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE]
    cells = grid_positions(4, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=16)
    for idx, (lbl, body) in enumerate(pillars):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"o{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fills[idx], stroke=NAVY,
            text_size=17, text_family=2)
    return els


def s4_slide_4(i, fid):
    els = slide_header(fid, i,
        title="Baseline Security + Validation Checklist",
        eyebrow="MINIMUM EVIDENCE TO MERGE")
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 460
    els += rect_with_text(fid, "sec",
        x=PAD, y=y0, w=col_w, h=h,
        text=("BASELINE SECURITY\n\n"
              "Secrets management\n"
              "Dependency review\n"
              "Code scanning\n"
              "Vulnerability visibility\n"
              "Safer defaults\nin code & config"),
        fill=PALE_NAVY, stroke=NAVY,
        text_size=18, text_family=2)
    els += rect_with_text(fid, "checklist",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text=("VALIDATION CHECKLIST\n\n"
              "What behavior changed?\n"
              "What tests prove it?\n"
              "What logs or metrics verify?\n"
              "What security/dep risk changed?\n"
              "What assumptions were made?"),
        fill=PALE_CYAN, stroke=CYAN,
        text_size=18, text_family=2)
    return els


def s4_slide_5(i, fid):
    els = slide_header(fid, i,
        title="Validation Gates by Change Type",
        eyebrow="DIFFERENT CHANGES NEED DIFFERENT EVIDENCE")
    rows = [
        ("DOCS",          "Accuracy review against the actual repo"),
        ("REFACTOR",      "Regression tests + behavior checks"),
        ("OBSERVABILITY", "Log / trace verification in a real flow"),
        ("DEPENDENCY",    "Dependency review + scanning results"),
        ("MIGRATION",     "Rollback plan + compatibility thinking"),
    ]
    y0 = frame_y(i, BODY_Y)
    row_h = 82
    gap = 10
    tag_w = 260
    for idx, (kind, gate) in enumerate(rows):
        ry = y0 + idx * (row_h + gap)
        els += rect_with_text(fid, f"k{idx}",
            x=PAD, y=ry, w=tag_w, h=row_h,
            text=kind,
            fill=NAVY, stroke=NAVY,
            text_color=WHITE, text_size=20, text_family=1)
        els += rect_with_text(fid, f"g{idx}",
            x=PAD + tag_w + 16, y=ry, w=FRAME_W - 2*PAD - tag_w - 16, h=row_h,
            text=gate,
            fill=WHITE, stroke=NAVY,
            text_size=18, text_family=2)
    return els


SESSION_4_FRAMES = [
    {"name": "Slide 01 - Validation Equation",    "builder": s4_slide_1},
    {"name": "Slide 02 - Coverage vs Confidence", "builder": s4_slide_2},
    {"name": "Slide 03 - Observability Pillars",  "builder": s4_slide_3},
    {"name": "Slide 04 - Security + Checklist",   "builder": s4_slide_4},
    {"name": "Slide 05 - Gates by Change Type",   "builder": s4_slide_5},
]


# --------------------------------------------------------------------------
# FILE 6 — Session 5: Making It Repeatable (6 frames)
# --------------------------------------------------------------------------

def s5_slide_1(i, fid):
    els = slide_header(fid, i,
        title="Staged Improvement, Not Rewrite Fantasy",
        eyebrow="DAY 5  ·  SET THE FRAME")
    y0 = frame_y(i, BODY_Y)
    col_w = (FRAME_W - 2*PAD - 20) // 2
    h = 460
    els += rect_with_text(fid, "rewrite",
        x=PAD, y=y0, w=col_w, h=h,
        text=("REWRITE FANTASY\n\n"
              "Big-bang clean slate.\n\n"
              "Usually unaffordable,\n"
              "unsafe, and slow.\n"
              "Often fails to reach parity."),
        fill=PALE_NAVY, stroke=NAVY,
        text_size=20, text_family=1)
    els += rect_with_text(fid, "staged",
        x=PAD + col_w + 20, y=y0, w=col_w, h=h,
        text=("STAGED MODERNIZATION\n\n"
              "Small, compounding wins.\n\n"
              "Start where friction is\n"
              "high and validation\n"
              "is possible."),
        fill=PALE_CYAN, stroke=CYAN,
        text_size=20, text_family=1)
    return els


def s5_slide_2(i, fid):
    els = slide_header(fid, i,
        title="The Five-Step Improvement Sequence",
        eyebrow="OPERATIONALIZED THESIS")
    steps = [
        ("1  MAKE VISIBLE",    "Scan the system.\nInspect docs, code,\ndeploys."),
        ("2  UNBLOCK BASICS",  "Fix setup and\ndocumentation\nblockers."),
        ("3  BUILD CONFIDENCE","Tests and data\ndiscipline."),
        ("4  SEE IN OPERATION","Observability and\nrelease visibility."),
        ("5  STANDARDIZE",     "Workflow, review,\nand team norms."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE, PALE_CYAN]
    cells = grid_positions(5, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=12)
    for idx, (lbl, body) in enumerate(steps):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"s{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fills[idx], stroke=NAVY,
            text_size=16, text_family=2)
    return els


def s5_slide_3(i, fid):
    els = slide_header(fid, i,
        title="What to Standardize",
        eyebrow="LIGHTWEIGHT GOVERNANCE")
    items = [
        ("REPO HEALTH\nSCORECARDS", "Revisit quarterly.\nTrack trends."),
        ("PR TEMPLATES",            "Including AI-assisted\nchange evidence."),
        ("SMALL-DIFF\nPREFERENCE",  "Explicit team norm.\nReject oversized diffs."),
        ("BASELINE\nCI CHECKS",     "Scanning, lint, tests,\nsecret checks."),
        ("DEBT REVIEW\nCADENCE",    "Periodic prioritization\nconversation."),
    ]
    fills = [PALE_CYAN, WHITE, PALE_NAVY, WHITE, PALE_CYAN]
    cells = grid_positions(5, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=12)
    for idx, (lbl, body) in enumerate(items):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"i{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fills[idx], stroke=NAVY,
            text_size=15, text_family=2)
    return els


def s5_slide_4(i, fid):
    els = slide_header(fid, i,
        title="The 30-Day Team Plan",
        eyebrow="SEVEN ACTIONS, NOT THIRTY")
    items = [
        ("3  QUICK WINS",              "High-leverage fixes\nyou can ship fast.",   PALE_CYAN, NAVY),
        ("2  STRUCTURAL\nIMPROVEMENTS","Bigger bets,\nstarted deliberately.",       PALE_NAVY, NAVY),
        ("1  WORKFLOW\nCHANGE",        "A habit,\nnot a tool.",                      PALE_CYAN, NAVY),
        ("1  VALIDATION\nIMPROVEMENT", "Evidence that the\nsystem is healthier.",   PALE_NAVY, NAVY),
        ("1  RE-CHECK IN\n30 DAYS",    "Run the scorecard\nagain and compare.",     NAVY,      WHITE),
    ]
    cells = grid_positions(5, 1, y0=frame_y(i, BODY_Y), total_h=460, gap_x=12)
    for idx, (lbl, body, fill, txt_c) in enumerate(items):
        x, y, w, h = cells[idx]
        els += rect_with_text(fid, f"p{idx}",
            x=x, y=y, w=w, h=h,
            text=f"{lbl}\n\n{body}",
            fill=fill, stroke=NAVY,
            text_color=txt_c, text_size=15, text_family=2)
    return els


def s5_slide_5(i, fid):
    els = slide_header(fid, i,
        title="Mature Use of AI in Engineering",
        eyebrow="OPERATING MODEL")
    text = ("AI: inspect, explain, propose, standardize.\n"
            "Humans: decide, validate, own the change.\n"
            "\n"
            "Require human review and evidence.\n"
            "Treat AI output as draft material.\n"
            "Prefer repeatable prompts and checklists\n"
            "over improvisation.")
    els += rect_with_text(fid, "model",
        x=PAD, y=frame_y(i, BODY_Y), w=FRAME_W - 2*PAD, h=460,
        text=text,
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=22, text_family=1)
    return els


def s5_slide_6(i, fid):
    els = slide_header(fid, i,
        title="Final Takeaways",
        eyebrow="FIVE LINES TO REMEMBER")
    takeaways = [
        "Good engineering makes AI more useful.",
        "Technical debt is friction that compounds.",
        "AI is strongest in understanding and improvement work.",
        "Validation turns plausible output into trustworthy change.",
        "Small repeatable improvements beat heroic cleanups.",
    ]
    y0 = frame_y(i, BODY_Y)
    row_h = 66
    gap = 10
    for idx, line in enumerate(takeaways):
        ry = y0 + idx * (row_h + gap)
        fill = PALE_CYAN if idx % 2 == 0 else WHITE
        els += rect_with_text(fid, f"t{idx}",
            x=PAD, y=ry, w=FRAME_W - 2*PAD, h=row_h,
            text=line,
            fill=fill, stroke=NAVY,
            text_size=20, text_family=1)

    # Closing line as a colored strip below
    close_y = y0 + 5 * (row_h + gap) + 4
    els += rect_with_text(fid, "close",
        x=PAD, y=close_y, w=FRAME_W - 2*PAD, h=60,
        text="The point is not more code.  The point is easier change.",
        fill=NAVY, stroke=NAVY,
        text_color=WHITE, text_size=20, text_family=1)
    return els


SESSION_5_FRAMES = [
    {"name": "Slide 01 - Staged vs Rewrite",   "builder": s5_slide_1},
    {"name": "Slide 02 - Five-Step Sequence",  "builder": s5_slide_2},
    {"name": "Slide 03 - What to Standardize", "builder": s5_slide_3},
    {"name": "Slide 04 - 30-Day Plan",         "builder": s5_slide_4},
    {"name": "Slide 05 - Mature AI Use",       "builder": s5_slide_5},
    {"name": "Slide 06 - Final Takeaways",     "builder": s5_slide_6},
]


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

FILES = [
    (f"{ROOT}/overview/overview.excalidraw", OVERVIEW_FRAMES),
    (f"{ROOT}/Session-1-What-Good-Looks-Like/session-1.excalidraw", SESSION_1_FRAMES),
    (f"{ROOT}/Session-2-Technical-Debt-as-Friction/session-2.excalidraw", SESSION_2_FRAMES),
    (f"{ROOT}/Session-3-Using-AI-to-Inspect-and-Improve/session-3.excalidraw", SESSION_3_FRAMES),
    (f"{ROOT}/Session-4-Validation-Tests-Observability-Security/session-4.excalidraw", SESSION_4_FRAMES),
    (f"{ROOT}/Session-5-Making-It-Repeatable/session-5.excalidraw", SESSION_5_FRAMES),
]


def main():
    for path, frames in FILES:
        n = build_file(path, frames)
        print(f"wrote {path}  ({len(frames)} frames, {n} elements)")


if __name__ == "__main__":
    main()
