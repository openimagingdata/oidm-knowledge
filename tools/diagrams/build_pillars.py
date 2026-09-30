#!/usr/bin/env python3
"""Build the OIDM "five pillars" technology-stack diagram.

A layered stack, read bottom to top, each layer its own hue (no blue reused
from other diagrams in the bundle) so the picture reads without words:

  1. Foundation Context (bottom) -- shared, curated knowledge: finding and
     diagnosis definitions, anatomic locations, exam types. Short
     double-headed arrows between the three blocks, with one "relationships"
     label over the row, say the three are tied to each other.
  2. Data Structures -- this patient's data, sitting on the foundation.
  3. SDKs -- a thin band between the data layer and the top.
  4/5. Use Cases and Sample Applications -- two panels sharing the top band,
     joined by a short horizontal connector labelled "illustrates".

The seam -- how the Data Structures band and the Foundation Context band show
that the patient graph is woven into the foundation graph -- is pluggable, and
selected with the required `--seam` flag. v3's seam (an overlap crossed by
twelve alternating vertical threads) was rejected; the three candidates are:

  a  Named attachments. The bands separate, and thin connectors run from the
     data cards to named tags sitting on the Foundation band's top edge, each
     tag over the foundation block it attaches to ("is a", "located at", ...).
  b  Dovetail. The bands are flush and the Data Structures band's lower edge
     is cut into four teal tabs that drop into matching slots in the
     Foundation band's top edge, one per attachment kind. No lines.
  c  Shared membrane. A narrow hatched band between the two holds four
     attachment-point nodes, each ticking up into the data band and down into
     the foundation band.

A seam is a dict of four things: how much room the Data band leaves below its
cards, the gap between the two bands, how far below the Foundation band's top
edge its header starts, and a draw() that paints the seam itself once both
band rectangles are placed.

Geometry rules: every band is CONTENT_W wide and starts at x=0; vertical gaps
between bands are all BAND_GAP, except the Data/Foundation seam, which each
seam sets for itself; band heights are computed from their contents, so no
band is taller than its own text needs.

Icons: Health Icons (CC0/MIT, outline style) for anatomy/exam/person glyphs,
Lucide (ISC, with one Feather-derived MIT icon) for everything else -- see
icons/LICENSES.md for the full source list and the two slots where Health
Icons had no matching glyph and Lucide was used instead. Health Icons'
outline set is filled-path art on a 48x48 viewBox with built-in padding, so
it renders optically smaller than Lucide's 24x24 stroke art at the same box
size; ICON_FILLED compensates.

Output: knowledge/drafts/pillars-<seam>.excalidraw (override with --out);
render with render_excalidraw.py.
"""
from __future__ import annotations

import argparse
import math

from excalib import els, base, text, image, save, AMBER, TEAL, VIOLET, ROSE, GREEN, CAPTION

# ---------------------------------------------------------------- layout constants
CONTENT_W = 880
BAND_GAP = 24     # the vertical gap between bands above the seam
PAD_BAND = 20     # a band's own inner padding on all sides
GAP = 20          # gap between sibling blocks inside a band
GAP_REL = 64      # wider gap, so a double-headed arrow reads as an arrow and not a diamond
ICON = 28         # harmonized icon render size
ICON_FILLED = 32  # filled-path icon sets need a bigger box to match optically
CORNER_R = 32     # Excalidraw's adaptive corner radius for a band-sized rectangle

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
    that matters at the seam: whichever band rect is inserted at index 0 last
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
    """An unstroked patch of colour -- used to close the notch two rounded
    bands leave where they meet, and to let a tab sit across a band edge
    without that edge's stroke running through it."""
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


def arc_pts(cx: float, cy: float, r: float, a0: float, a1: float, n=4) -> list[tuple[float, float]]:
    """Points along a circular arc, for rounding a corner of a polyline."""
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n))
            for i in range(n + 1)]


def plate(cx: float, y_top: float, s: str, size=13, color=CAPTION, fill="#ffffff",
          stroke="transparent", pad_x=7, pad_y=3, sw=1) -> tuple[float, float]:
    """An opaque label plate centered on cx with its top at y_top. Returns
    (width, height)."""
    w = len(s) * size * 0.58 + 2 * pad_x
    h = size * 1.25 + 2 * pad_y
    r = base("rectangle", uid("plate"), cx - w / 2, y_top, w, h, stroke, fill, sw=sw)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(uid("platet"), cx - w / 2 + pad_x, y_top + pad_y, s, size=size, color=color,
                    align="center", w=w - 2 * pad_x))
    return w, h


def corner_patch(y_top: float, y_bot: float, pal: dict, anchor: dict) -> None:
    """Two rounded bands that meet edge to edge leave a white notch at each
    end, where both corner radii curve away from the seam. Fill those notches
    with the band's own colour and redraw its outer border straight, so the
    stack keeps one silhouette through the seam.

    A notch is CORNER_R deep, which reaches back into the band far enough to
    cover a card corner or a header icon, so the patch is restacked to sit
    directly above `anchor` (its own band rectangle) instead of on top of
    everything the seam is drawn after."""
    made = [
        fill_rect(-1, y_top, CORNER_R + 1, y_bot - y_top, pal["band"]),
        fill_rect(CONTENT_W - CORNER_R, y_top, CORNER_R + 1, y_bot - y_top, pal["band"]),
        stroke_line([(0, y_top), (0, y_bot)], pal["stroke"], sw=2),
        stroke_line([(CONTENT_W, y_top), (CONTENT_W, y_bot)], pal["stroke"], sw=2),
    ]
    for e in reversed(made):
        els.remove(e)
        els.insert(els.index(anchor) + 1, e)


# ============================================================ seam a: named attachments
# Each link: (data card index, exit fraction along its bottom edge,
#             foundation block index, which of that block's two tags, label).
# Exit fractions and tag order run left to right by target, so the six
# connectors cross each other only at clean X points and never a label.
A_LINKS = [
    (0, 0.22, 0, 0, "is a"),
    (0, 0.50, 1, 0, "located at"),
    (0, 0.78, 2, 0, "seen on"),
    (1, 0.50, 2, 1, "of an exam type"),
    (2, 0.35, 0, 1, "per definition"),
    (2, 0.65, 1, 1, "per location"),
]


def draw_seam_a(g: dict) -> None:
    size, pad_x, pad_y = 13, 7, 3
    tag_h = size * 1.25 + 2 * pad_y
    y_tag_top = g["found_top"] - tag_h
    y_card = g["blocks_bottom"]

    labels = {(dj, slot): lab for (_si, _sf, dj, slot, lab) in A_LINKS}
    tag_cx: dict[tuple[int, int], float] = {}
    for j in range(3):
        w0 = len(labels[(j, 0)]) * size * 0.58 + 2 * pad_x
        w1 = len(labels[(j, 1)]) * size * 0.58 + 2 * pad_x
        total = w0 + w1 + 12
        cx = g["f_positions"][j] + g["W3"] / 2
        tag_cx[(j, 0)] = cx - total / 2 + w0 / 2
        tag_cx[(j, 1)] = cx + total / 2 - w1 / 2

    # connectors first, so each tag paints over the end of its own line
    for (si, sf, dj, slot, _lab) in A_LINKS:
        x1 = g["d_positions"][si] + g["W4"] * sf
        stroke_line([(x1, y_card), (tag_cx[(dj, slot)], y_tag_top)], TEAL["stroke"], sw=1, opacity=75)
    for key, lab in labels.items():
        plate(tag_cx[key], y_tag_top, lab, size=size, color=AMBER["text"],
              stroke=AMBER["stroke"], pad_x=pad_x, pad_y=pad_y)

    els.append(text(uid("seaml"), 0, g["found_top"] + 13,
                    "interconnected at every finding, diagnosis, location, and exam type",
                    size=13, color=CAPTION, align="center", w=CONTENT_W))


# ============================================================ seam b: dovetail
B_WORDS = ["finding", "diagnosis", "location", "exam type"]
B_TAB_W = 120.0
B_TAB_D = 34.0
B_TAB_R = 11.0
B_LEAD = "woven together at every:"
B_RIGHT_MARGIN = 60.0   # amber left clear to the right of the last tab


def draw_seam_b(g: dict) -> None:
    seam = g["found_top"]                      # the two bands are flush here
    corner_patch(seam - CORNER_R, seam, TEAL, g["teal_band"])
    corner_patch(seam, seam + CORNER_R, AMBER, g["amber_band"])
    stroke_line([(0, seam), (CONTENT_W, seam)], TEAL["stroke"], sw=2)

    lead_w = len(B_LEAD) * 13 * 0.58
    x0 = PAD_BAND + lead_w + 22
    span = CONTENT_W - B_RIGHT_MARGIN - x0
    step = (span - B_TAB_W) / (len(B_WORDS) - 1)
    els.append(text(uid("bl"), PAD_BAND, seam + (B_TAB_D - 13 * 1.25) / 2, B_LEAD,
                    size=13, color=AMBER["mid"]))

    for i, word in enumerate(B_WORDS):
        x = x0 + i * step
        # the tab's fill runs up past the seam, so the band edge's stroke stops
        # at the tab: what is left reads as a slot cut into the Foundation band.
        fill_rect(x, seam - 12, B_TAB_W, B_TAB_D + 12, TEAL["band"], rounded=True)
        pts = [(x, seam - 7)]
        pts += arc_pts(x + B_TAB_R, seam + B_TAB_D - B_TAB_R, B_TAB_R, math.pi, math.pi / 2)
        pts += arc_pts(x + B_TAB_W - B_TAB_R, seam + B_TAB_D - B_TAB_R, B_TAB_R, math.pi / 2, 0.0)
        pts += [(x + B_TAB_W, seam - 7)]
        stroke_line(pts, TEAL["stroke"], sw=2)
        els.append(text(uid("bw"), x, seam + (B_TAB_D - 13 * 1.25) / 2, word,
                        size=13, color=TEAL["text"], align="center", w=B_TAB_W))


# ============================================================ seam c: shared membrane
C_WORDS = ["finding", "diagnosis", "location", "exam type"]
C_H = 64.0
C_TITLE = "attachment points"
C_PILL_H = 28.0
C_TICK = 9.0


def draw_seam_c(g: dict) -> None:
    top = g["data_band_bottom"]
    bot = g["found_top"]
    corner_patch(top - CORNER_R, top, TEAL, g["teal_band"])
    corner_patch(bot, bot + CORNER_R, AMBER, g["amber_band"])

    # membrane ground, then a fine two-colour hatch clipped to it
    fill_rect(0, top, CONTENT_W, bot - top, "#ffffff")
    step, i, c = 16.0, 0, top - CONTENT_W
    while c < bot:
        x1, x2 = max(0.0, top - c), min(CONTENT_W, bot - c)
        if x2 - x1 > 1:
            stroke_line([(x1, x1 + c), (x2, x2 + c)],
                        TEAL["stroke"] if i % 2 == 0 else AMBER["stroke"], sw=1, opacity=25)
        c += step
        i += 1
    stroke_line([(0, top), (CONTENT_W, top)], TEAL["stroke"], sw=2)
    stroke_line([(0, bot), (CONTENT_W, bot)], AMBER["stroke"], sw=2)
    stroke_line([(0, top), (0, bot)], CAPTION, sw=1, opacity=55)
    stroke_line([(CONTENT_W, top), (CONTENT_W, bot)], CAPTION, sw=1, opacity=55)

    pill_top = top + (C_H - C_PILL_H) / 2
    tw, _ = plate(PAD_BAND + len(C_TITLE) * 13 * 0.58 / 2 + 7, pill_top + (C_PILL_H - (13 * 1.25 + 6)) / 2,
                  C_TITLE, size=13, color=CAPTION)
    x0 = PAD_BAND + tw + 20
    widths = [len(w) * 13 * 0.58 + 28 for w in C_WORDS]
    span = CONTENT_W - PAD_BAND - x0
    gap = (span - sum(widths)) / (len(C_WORDS) - 1)
    x = x0
    for word, w in zip(C_WORDS, widths):
        cx = x + w / 2
        stroke_line([(cx, top - C_TICK), (cx, pill_top)], TEAL["stroke"], sw=2)
        stroke_line([(cx, pill_top + C_PILL_H), (cx, bot + C_TICK)], AMBER["stroke"], sw=2)
        r = base("rectangle", uid("pill"), x, pill_top, w, C_PILL_H, CAPTION, "#ffffff", sw=1)
        r["roundness"] = {"type": 3}
        els.append(r)
        els.append(text(uid("pillt"), x, pill_top + (C_PILL_H - 13 * 1.25) / 2, word,
                        size=13, color="#334155", align="center", w=w))
        x += w + gap


SEAMS = {
    "a": {"pad_below_blocks": PAD_BAND, "band_gap": 60.0, "found_top_pad": 46.0, "draw": draw_seam_a},
    "b": {"pad_below_blocks": PAD_BAND, "band_gap": 0.0, "found_top_pad": B_TAB_D + 18, "draw": draw_seam_b},
    "c": {"pad_below_blocks": PAD_BAND, "band_gap": C_H, "found_top_pad": 20.0, "draw": draw_seam_c},
}


# ============================================================ the stack
def build(seam_key: str, out_path: str) -> str:
    seam = SEAMS[seam_key]

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

    DATA_BAND_BOTTOM = DATA_BLOCKS_BOTTOM + seam["pad_below_blocks"]
    teal_band = band_rect(uid("band"), 0, Y_DATA, CONTENT_W, DATA_BAND_BOTTOM - Y_DATA, TEAL, at_front=True)

    # ---------------------------------------- 1. Foundation Context (bottom)
    # Built last so its rect lands behind the Data Structures band at the seam.
    FOUND_TOP = DATA_BAND_BOTTOM + seam["band_gap"]
    hdr_bottom_f = band_header(PAD_BAND - 2, FOUND_TOP + seam["found_top_pad"],
                               "icons/lucide-book-open.svg", AMBER,
                               "Foundation Context", "shared, curated knowledge", size=20)
    REL_Y = hdr_bottom_f + 12
    rel_bottom = chip(CONTENT_W / 2, REL_Y, "relationships", AMBER["band"], AMBER["stroke"], AMBER["text"])
    F_ROW_Y = rel_bottom + 10
    W3 = (CONTENT_W - 2 * PAD_BAND - 2 * GAP_REL) / 3
    f_positions = [PAD_BAND + i * (W3 + GAP_REL) for i in range(3)]
    f_specs = [
        ("icons/lucide-tag.svg", ["Finding/diagnosis definitions"], "finding models · CDEs", False),
        ("icons/healthicons-lungs.svg", ["Anatomic locations"], "anchored in RadLex", True),
        ("icons/healthicons-xray.svg", ["Exam types"], "LOINC/RSNA Playbook", True),
    ]
    ROW_H_FOUND = max(icon_block_h(lines, desc) for _, lines, desc, _ in f_specs)
    for xpos, (ipath, lines, desc, filled) in zip(f_positions, f_specs):
        icon_block(xpos, F_ROW_Y, W3, ROW_H_FOUND, ipath, AMBER, lines, desc=desc, filled_icon=filled)
    FOUND_BLOCKS_BOTTOM = F_ROW_Y + ROW_H_FOUND

    arrow_y = F_ROW_Y + ROW_H_FOUND / 2
    for i in range(2):
        x1 = f_positions[i] + W3 + 6
        hconn(x1, x1 + GAP_REL - 12, arrow_y, AMBER["stroke"], sw=2, both=True)

    FOUND_BAND_BOTTOM = FOUND_BLOCKS_BOTTOM + PAD_BAND
    amber_band = band_rect(uid("band"), 0, FOUND_TOP, CONTENT_W, FOUND_BAND_BOTTOM - FOUND_TOP, AMBER, at_front=True)

    # ---------------------------------------- the seam, drawn over both bands
    seam["draw"]({
        "blocks_bottom": DATA_BLOCKS_BOTTOM,
        "data_band_bottom": DATA_BAND_BOTTOM,
        "found_top": FOUND_TOP,
        "d_positions": d_positions, "W4": W4,
        "f_positions": f_positions, "W3": W3,
        "teal_band": teal_band, "amber_band": amber_band,
    })

    return save(out_path)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seam", choices=sorted(SEAMS), required=True,
                    help="which Data/Foundation seam to draw: a=named attachments, "
                         "b=dovetail, c=shared membrane")
    ap.add_argument("--out", default=None,
                    help="output path relative to the repo root "
                         "(default knowledge/drafts/pillars-<seam>.excalidraw)")
    args = ap.parse_args()
    build(args.seam, args.out or f"knowledge/drafts/pillars-{args.seam}.excalidraw")


if __name__ == "__main__":
    main()
