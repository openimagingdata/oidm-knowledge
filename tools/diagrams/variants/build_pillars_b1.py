#!/usr/bin/env python3
"""Build the OIDM "five pillars" stack diagram -- variant B1, a true finger joint.

This is a variant of ../build_pillars.py (seam b, the dovetail) and exists so
three seam explorations can run without stepping on each other. It differs
from the parent in three ways:

  1. The seam is a finger joint, not a dovetail. In seam b the Data
     Structures band grew four tabs that dropped into the Foundation band --
     one band sitting on the other. Here both bands grow fingers into a
     single joint zone JOINT_D deep: four labelled teal tabs descend from
     Data Structures, and five unlabelled amber fingers rise from Foundation
     Context between and outside them, so the boundary is one square wave and
     neither band is simply on top. The fingers are square, not rounded: a
     finger joint reads as a finger joint because the fingers are square.
  2. The "relationships" plate and the two double-headed arrows between the
     Foundation blocks are gone.
  3. The Foundation band is tightened so everything below the joint -- header,
     subtitle, block row, bottom padding -- fits in under 200px.

Everything else (icons, palette, block content, the bands above) is v4b.

Joint geometry. JOINT_TOP is where the joint zone starts and JOINT_BOT =
JOINT_TOP + JOINT_D where it ends. The teal band rectangle runs down to
JOINT_BOT and the amber band rectangle starts at JOINT_TOP, so the two
overlap by exactly the joint depth; the teal rectangle is in front, so teal
is what shows in the zone by default, and the amber fingers are painted back
over it. That overlap also hides both rectangles' rounded corners inside the
zone, which is why the outermost fingers are amber and at least CORNER_R
wide -- they cover the curves, and two short vertical strokes redraw the
stack's outer edge straight through the joint.

Output: knowledge/drafts/pillars-b1.excalidraw (override with --out).
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from excalib import els, base, text, image, save, AMBER, TEAL, VIOLET, ROSE, GREEN, CAPTION  # noqa: E402

# ---------------------------------------------------------------- layout constants
CONTENT_W = 880
BAND_GAP = 24     # the vertical gap between bands above the seam
PAD_BAND = 20     # a band's own inner padding on all sides
GAP = 20          # gap between sibling blocks inside a band
GAP_F = 24        # gap between the three Foundation blocks (no arrows between them now)
ICON = 28         # harmonized icon render size
ICON_FILLED = 32  # filled-path icon sets need a bigger box to match optically
CORNER_R = 32     # Excalidraw's adaptive corner radius for a band-sized rectangle

# ---------------------------------------------------------------- the finger joint
JOINT_D = 40.0                  # how deep the joint zone is: how far each set of fingers reaches
TAB_W = 118.0                   # width of a labelled teal tab
JOINT_WORDS = ["finding", "diagnosis", "location", "exam type"]
FINGER_W = (CONTENT_W - len(JOINT_WORDS) * TAB_W) / (len(JOINT_WORDS) + 1)  # amber, unlabelled
CAPTION_SPACE = 38.0            # teal room above the joint for the lead caption
LEAD = "woven together at every:"

_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


# ---------------------------------------------------------------- primitives
def band_rect(id_: str, x: float, y: float, w: float, h: float, pal: dict, at_front=False) -> dict:
    """Draw a band's background rectangle. Pass at_front=True when the band's
    true height is only known after laying out its header/blocks (they were
    already appended to els) -- this inserts the rect at index 0 so it still
    paints behind its own contents instead of covering them. Note the order
    that matters at the joint: whichever band rect is inserted at index 0 last
    ends up furthest back, so Foundation Context must be built last."""
    r = base("rectangle", id_, x, y, w, h, pal["stroke"], pal["band"])
    r["roundness"] = {"type": 3}
    if at_front:
        els.insert(0, r)
    else:
        els.append(r)
    return r


def band_header(x: float, y: float, icon_path: str, pal: dict, title: str, subtitle: str,
                size=20, filled_icon=False) -> float:
    """Bold band title with its icon to the left, subtitle below. Returns bottom y."""
    s = ICON_FILLED if filled_icon else ICON
    image(uid("bicon"), x, y - (s - ICON) / 2 - 2, s, s, icon_path, color=pal["stroke"])
    els.append(text(uid("btitle"), x + ICON + 12, y, title, size=size, color=pal["text"]))
    y2 = y + size * 1.3
    els.append(text(uid("bsub"), x + ICON + 12, y2, subtitle, size=13, color=pal["mid"]))
    return y2 + 13 * 1.25


def icon_block_h(lines: list[str], desc: str | None = None) -> float:
    """Height an icon_block needs for this many label lines/descriptor."""
    n_title = len(lines)
    return 12 + ICON + 8 + n_title * 15 * 1.25 + (13 * 1.25 + 2 if desc else 0) + 10


def icon_block(x: float, y: float, w: float, h: float, icon_path: str, pal: dict,
               lines: list[str], desc: str | None = None, filled_icon=False) -> dict:
    """Icon centered on top, label line(s) centered below, optional lighter
    descriptor line last. Background is the band's own deeper pastel so the
    block reads as 'inside' the band, not a separate object."""
    r = base("rectangle", uid("blk"), x, y, w, h, pal["stroke"], pal["block"], sw=1)
    r["roundness"] = {"type": 3}
    els.append(r)
    cx = x + w / 2
    content_h = icon_block_h(lines, desc) - 22  # minus this fn's fixed 12+10 top/bottom pad
    top = y + (h - content_h) / 2
    s = ICON_FILLED if filled_icon else ICON
    image(uid("blki"), cx - s / 2, top - (s - ICON) / 2, s, s, icon_path, color=pal["stroke"])
    ty = top + ICON + 6
    for ln in lines:
        els.append(text(uid("blkt"), x + 6, ty, ln, size=15, color=pal["text"], align="center", w=w - 12))
        ty += 15 * 1.25
    if desc:
        els.append(text(uid("blkd"), x + 6, ty + 2, desc, size=13, color=pal["mid"], align="center", w=w - 12))
    return r


def chip(cx: float, y_top: float, s: str, fill: str, stroke: str, color: str,
         size=13, pad_x=9, pad_y=3) -> float:
    """A short caption on its own opaque rounded plate, centered on cx, so it
    reads as a label for what it sits over and never mixes with a line or a
    band fill behind it. Returns bottom y."""
    w = len(s) * size * 0.58 + 2 * pad_x
    h = size * 1.25 + 2 * pad_y
    r = base("rectangle", uid("chip"), cx - w / 2, y_top, w, h, stroke, fill, sw=1)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(uid("chipt"), cx - w / 2 + pad_x, y_top + pad_y, s, size=size, color=color,
                    align="center", w=w - 2 * pad_x))
    return y_top + h


def hconn(x1: float, x2: float, y: float, color: str, sw=1, both=False) -> None:
    """A plain horizontal connector; both=True gives it two arrowheads."""
    a = base("arrow" if both else "line", uid("conn"), x1, y, x2 - x1, 0, color, "transparent", sw=sw)
    a.update({"points": [[0, 0], [x2 - x1, 0]], "boundElements": None})
    if both:
        a.update({"startArrowhead": "arrow", "endArrowhead": "arrow"})
    els.append(a)


def fill_rect(x: float, y: float, w: float, h: float, fill: str, rounded=False) -> dict:
    """An unstroked patch of colour -- used here to paint an amber finger back
    over the teal band rectangle inside the joint zone."""
    r = base("rectangle", uid("fill"), x, y, w, h, "transparent", fill, sw=1)
    r["roundness"] = {"type": 3} if rounded else None
    els.append(r)
    return r


def stroke_line(pts: list[tuple[float, float]], color: str, sw=2, opacity=100) -> dict:
    """A polyline through pts (absolute coordinates), sharp corners."""
    x0, y0 = pts[0]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ln = base("line", uid("ln"), x0, y0, max(xs) - min(xs), max(ys) - min(ys), color, "transparent", sw=sw)
    ln.update({"points": [[p[0] - x0, p[1] - y0] for p in pts], "boundElements": None, "roundness": None})
    ln["opacity"] = opacity
    els.append(ln)
    return ln


def tab_x(i: int) -> float:
    """Left edge of labelled teal tab i. The run starts and ends with an amber
    finger, so the pattern is A T A T A T A T A across the full width."""
    return FINGER_W + i * (TAB_W + FINGER_W)


def draw_finger_joint(g: dict) -> None:
    top = g["joint_top"]
    bot = top + JOINT_D

    # 1. the amber fingers, painted back over the teal band rectangle. Each runs
    #    a few px past the joint's bottom so it also covers the teal rectangle's
    #    own bottom stroke; below the zone it is amber on amber, so nothing shows.
    finger_xs = [0.0] + [tab_x(i) + TAB_W for i in range(len(JOINT_WORDS))]
    for fx in finger_xs:
        fill_rect(fx, top, FINGER_W, JOINT_D + 3, AMBER["band"])

    # 2. the interlocking boundary as one square wave, left edge to right edge
    pts: list[tuple[float, float]] = [(0.0, top)]
    for i in range(len(JOINT_WORDS)):
        x = tab_x(i)
        pts += [(x, top), (x, bot), (x + TAB_W, bot), (x + TAB_W, top)]
    pts.append((CONTENT_W, top))
    stroke_line(pts, TEAL["stroke"], sw=2)

    # 3. the stack's outer edge through the joint. Both band rectangles curve
    #    away inside the zone; the amber fingers at each end cover those curves,
    #    so the edge is redrawn straight in the amber that is actually there.
    for x in (0.0, CONTENT_W):
        stroke_line([(x, top), (x, bot + 3)], AMBER["stroke"], sw=2)

    # 4. the four words, one per teal tab
    for i, word in enumerate(JOINT_WORDS):
        els.append(text(uid("jw"), tab_x(i), top + (JOINT_D - 13 * 1.25) / 2, word,
                        size=13, color=TEAL["text"], align="center", w=TAB_W))

    # 5. the lead caption, in the teal room kept above the joint
    els.append(text(uid("lead"), 0, top - CAPTION_SPACE + (CAPTION_SPACE - 13 * 1.25) / 2, LEAD,
                    size=13, color=TEAL["mid"], align="center", w=CONTENT_W))


# ============================================================ the stack
def build(out_path: str) -> str:
    # ---------------------------------------- 5/4. Use Cases | Sample Applications
    Y_TOP = 0
    GAP_MID = 104                 # wide enough for "illustrates" to sit clear of both panels
    PANEL_PAD = 14
    PANEL_INSET = PAD_BAND - 2    # same left inset as the full-width band headers
    PANEL_TITLE = 18
    PANEL_H = PANEL_PAD + PANEL_TITLE * 1.3 + 13 * 1.25 + PANEL_PAD
    panel_w = (CONTENT_W - GAP_MID) / 2

    band_rect(uid("panel"), 0, Y_TOP, panel_w, PANEL_H, ROSE)
    band_rect(uid("panel"), panel_w + GAP_MID, Y_TOP, panel_w, PANEL_H, GREEN)
    band_header(PANEL_INSET, Y_TOP + PANEL_PAD, "icons/lucide-lightbulb.svg", ROSE,
                "Use Cases", "what the project wants built", size=PANEL_TITLE)
    band_header(panel_w + GAP_MID + PANEL_INSET, Y_TOP + PANEL_PAD, "icons/lucide-app-window.svg", GREEN,
                "Sample Applications", "what has been built", size=PANEL_TITLE)
    conn_y = Y_TOP + PANEL_H / 2
    hconn(panel_w + 2, panel_w + GAP_MID - 2, conn_y, CAPTION)
    chip(panel_w + GAP_MID / 2, conn_y - 7 - (13 * 1.25 + 6), "illustrates",
         "#ffffff", "transparent", CAPTION)

    # ---------------------------------------- 3. SDKs (thin full-width band)
    Y_SDK = Y_TOP + PANEL_H + BAND_GAP
    sdk_hdr_bottom = band_header(PAD_BAND - 2, Y_SDK + 16, "icons/lucide-package.svg", VIOLET,
                                 "SDKs", "wrap the structures · attach the shared knowledge · support authoring",
                                 size=18)
    SDK_BOTTOM = sdk_hdr_bottom + 16
    band_rect(uid("band"), 0, Y_SDK, CONTENT_W, SDK_BOTTOM - Y_SDK, VIOLET, at_front=True)

    # ---------------------------------------- 2. Data Structures
    Y_DATA = SDK_BOTTOM + BAND_GAP
    hdr_bottom = band_header(PAD_BAND - 2, Y_DATA + 18, "icons/lucide-layers.svg", TEAL,
                             "Data Structures", "this patient · Patient Context", size=20)
    BLOCK_ROW_Y = hdr_bottom + 14
    W4 = (CONTENT_W - 2 * PAD_BAND - 3 * GAP) / 4
    d_positions = [PAD_BAND + i * (W4 + GAP) for i in range(4)]
    d_specs = [
        ("icons/lucide-clipboard.svg", ["Observation"], False),
        ("icons/lucide-clipboard-list.svg", ["Exam Finding", "List"], False),
        ("icons/lucide-list.svg", ["Imaging Problem", "List"], False),
        ("icons/healthicons-person.svg", ["Imaging Persona"], True),
    ]
    ROW_H_DATA = max(icon_block_h(lines) for _, lines, _ in d_specs)
    for xpos, (ipath, lines, filled) in zip(d_positions, d_specs):
        icon_block(xpos, BLOCK_ROW_Y, W4, ROW_H_DATA, ipath, TEAL, lines, filled_icon=filled)
    DATA_BLOCKS_BOTTOM = BLOCK_ROW_Y + ROW_H_DATA

    # the joint zone: the two band rectangles overlap across exactly its depth
    JOINT_TOP = DATA_BLOCKS_BOTTOM + CAPTION_SPACE
    JOINT_BOT = JOINT_TOP + JOINT_D
    band_rect(uid("band"), 0, Y_DATA, CONTENT_W, JOINT_BOT - Y_DATA, TEAL, at_front=True)

    # ---------------------------------------- 1. Foundation Context (bottom)
    # Built last so its rect lands behind the Data Structures band in the joint.
    FOUND_TOP = JOINT_TOP
    hdr_bottom_f = band_header(PAD_BAND - 2, JOINT_BOT + 14,
                               "icons/lucide-book-open.svg", AMBER,
                               "Foundation Context", "shared, curated knowledge", size=20)
    F_ROW_Y = hdr_bottom_f + 10
    W3 = (CONTENT_W - 2 * PAD_BAND - 2 * GAP_F) / 3
    f_positions = [PAD_BAND + i * (W3 + GAP_F) for i in range(3)]
    f_specs = [
        ("icons/lucide-tag.svg", ["Finding/diagnosis definitions"], "finding models · CDEs", False),
        ("icons/healthicons-lungs.svg", ["Anatomic locations"], "anchored in RadLex", True),
        ("icons/healthicons-xray.svg", ["Exam types"], "LOINC/RSNA Playbook", True),
    ]
    ROW_H_FOUND = max(icon_block_h(lines, desc) for _, lines, desc, _ in f_specs)
    for xpos, (ipath, lines, desc, filled) in zip(f_positions, f_specs):
        icon_block(xpos, F_ROW_Y, W3, ROW_H_FOUND, ipath, AMBER, lines, desc=desc, filled_icon=filled)
    FOUND_BAND_BOTTOM = F_ROW_Y + ROW_H_FOUND + PAD_BAND
    band_rect(uid("band"), 0, FOUND_TOP, CONTENT_W, FOUND_BAND_BOTTOM - FOUND_TOP, AMBER, at_front=True)

    print(f"foundation band below the joint: {FOUND_BAND_BOTTOM - JOINT_BOT:.1f}px")

    # ---------------------------------------- the joint, drawn over both bands
    draw_finger_joint({"joint_top": JOINT_TOP})

    return save(out_path)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="knowledge/drafts/pillars-b1.excalidraw",
                    help="output path relative to the repo root")
    args = ap.parse_args()
    build(args.out)


if __name__ == "__main__":
    main()
