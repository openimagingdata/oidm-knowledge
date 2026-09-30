#!/usr/bin/env python3
"""Build the OIDM "five pillars" stack diagram -- seam variant B2, "tabs plug
into blocks".

Variant of tools/diagrams/build_pillars.py --seam b. In v4b the four teal tabs
dropped out of the Data Structures band into empty amber ground: the joint was
band-to-band, and the three Foundation blocks sat well below it with no visible
relation to any particular tab. B2 makes the joint block-to-block instead.

  * The three Foundation Context blocks rise until their top edges *are* the
    seam, so there is no amber ground between the joint and the blocks.
  * Each teal tab lands in a named block: "finding" and "diagnosis" both plug
    into "Finding/diagnosis definitions", "location" into "Anatomic locations",
    "exam type" into "Exam types". A tab is drawn over the block's top edge, so
    the edge reads as a notch the tab fills.
  * The Foundation band header moves to a left column beside the blocks (icon +
    wrapped title + subtitle), with the "woven together at every:" lead above
    it, on the tab row, where it was in v4b.
  * The "relationships" plate and the two double-headed arrows between the
    Foundation blocks are gone, and the band is 151px tall including its header.

Everything above the seam (Use Cases / Sample Applications, SDKs, the four Data
Structures cards) is unchanged from v4b.

Because the Foundation band is laid out for this seam, the a/b/c seam switch of
the parent builder is not carried over: this file draws B2 and nothing else.

Block and tab widths here are sized from measured Helvetica advance widths (see
tools/diagrams/README.md, "Measuring text instead of estimating it"), not from
excalib's 0.58-per-character estimate.

Icons: unchanged from build_pillars.py -- Health Icons (CC0/MIT, outline) for
anatomy/exam/person glyphs, Lucide (ISC) for the rest; see icons/LICENSES.md.

Output: knowledge/drafts/pillars-b2.excalidraw (override with --out).
"""
from __future__ import annotations

import argparse
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from excalib import els, base, text, image, save, AMBER, TEAL, VIOLET, ROSE, GREEN, CAPTION

# ---------------------------------------------------------------- layout constants
CONTENT_W = 880
BAND_GAP = 24     # the vertical gap between bands above the seam
PAD_BAND = 20     # a band's own inner padding on all sides
GAP = 20          # gap between sibling blocks inside a band
ICON = 28         # harmonized icon render size
ICON_FILLED = 32  # filled-path icon sets need a bigger box to match optically
CORNER_R = 32     # Excalidraw's adaptive corner radius for a band-sized rectangle

# ---- the seam
TAB_W = 92.0      # a tab is sized to hold "diagnosis"/"exam type" (60px measured) with air
TAB_D = 30.0      # how far a tab descends past the seam into its block
TAB_R = 10.0      # the tab's bottom corner radius
TAB_GAP = 24.0    # between the two tabs that share the first block
TAB_RISE = 14.0   # how far the tab's fill runs up past the seam, to break the seam stroke
LEAD = "woven together at every:"

# ---- the Foundation band's left header column
LEFT_W = 196.0    # holds "shared, curated knowledge" (156 measured) beside the icon, on one line
LEFT_GAP = 20.0
PAD_BOTTOM = 26   # a little more air under the blocks than PAD_BAND, so their
                  # bottom corner radius does not crowd the band's own

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


def left_header(x: float, y: float, icon_path: str, pal: dict, title_lines: list[str],
                sub_lines: list[str], size=20) -> float:
    """The band header as a narrow left column: the icon hangs at the left
    margin beside the first title line, and every line of the title and the
    subtitle shares one text column indented past it -- the same icon/text
    relationship as the full-width band headers, just wrapped. Returns bottom y."""
    image(uid("bicon"), x, y + (size * 1.3 - ICON) / 2 - 1, ICON, ICON, icon_path, color=pal["stroke"])
    tx, yy = x + ICON + 12, y
    for ln in title_lines:
        els.append(text(uid("btitle"), tx, yy, ln, size=size, color=pal["text"]))
        yy += size * 1.3
    yy += 4
    for ln in sub_lines:
        els.append(text(uid("bsub"), tx, yy, ln, size=13, color=pal["mid"]))
        yy += 13 * 1.25
    return yy


def left_header_h(n_title: int, n_sub: int, size=20) -> float:
    return n_title * size * 1.3 + 4 + n_sub * 13 * 1.25


def icon_block_h(lines: list[str], desc: str | None = None) -> float:
    """Height an icon_block needs for this many label lines/descriptor."""
    n_title = len(lines)
    return 12 + ICON + 8 + n_title * 15 * 1.25 + (13 * 1.25 + 2 if desc else 0) + 10


def icon_block(x: float, y: float, w: float, h: float, icon_path: str, pal: dict,
               lines: list[str], desc: str | None = None, filled_icon=False,
               top_inset: float = 0.0) -> dict:
    """Icon centered on top, label line(s) centered below, optional lighter
    descriptor line last. Background is the band's own deeper pastel so the
    block reads as 'inside' the band, not a separate object.

    top_inset reserves that much of the block's top edge for something else --
    here, the notch a seam tab plugs into -- and centres the contents in what
    is left, so a tab never lands on the icon."""
    r = base("rectangle", uid("blk"), x, y, w, h, pal["stroke"], pal["block"], sw=1)
    r["roundness"] = {"type": 3}
    els.append(r)
    cx = x + w / 2
    content_h = icon_block_h(lines, desc) - 22  # minus this fn's fixed 12+10 top/bottom pad
    top = y + top_inset + (h - top_inset - content_h) / 2
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
    bands leave where they meet, to square off a block's rounded top corners
    where that top edge has become the seam, and to let a tab sit across a
    band edge without that edge's stroke running through it."""
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


# ============================================================ the seam
def tab_xs(bx: float, bw: float, n: int) -> list[float]:
    """Left edges of the n tabs that plug into a block of width bw at bx."""
    total = n * TAB_W + (n - 1) * TAB_GAP
    x0 = bx + (bw - total) / 2
    return [x0 + i * (TAB_W + TAB_GAP) for i in range(n)]


def draw_seam(g: dict) -> None:
    """The joint: the seam line, then one teal tab per attachment kind cut
    into the top edge of the Foundation block it attaches to."""
    seam = g["found_top"]
    corner_patch(seam - CORNER_R, seam, TEAL, g["teal_band"])
    corner_patch(seam, seam + CORNER_R, AMBER, g["amber_band"])

    # The Foundation blocks' top edges are the seam now, so square off their
    # rounded top corners -- otherwise each block reads as a lozenge tucked
    # under the band rather than a block the band rests on.
    for bx, bw in zip(g["f_positions"], g["f_widths"]):
        fill_rect(bx, seam, bw, CORNER_R, AMBER["block"])
        stroke_line([(bx, seam), (bx, seam + CORNER_R)], AMBER["stroke"], sw=1)
        stroke_line([(bx + bw, seam), (bx + bw, seam + CORNER_R)], AMBER["stroke"], sw=1)

    # Over a block, the seam is that block's own top edge, so it is drawn in
    # the block's stroke at the block's own weight: the teal tab then visibly
    # interrupts an amber edge, which is what makes the joint read as a notch
    # cut into this block rather than a scallop in the band above it. Each tab
    # paints over its own stretch of that edge next. Everywhere else the seam
    # is the Data Structures band's own bottom edge, in teal at band weight.
    edges: list[float] = [0.0]
    for bx, bw in zip(g["f_positions"], g["f_widths"]):
        stroke_line([(bx, seam), (bx + bw, seam)], AMBER["stroke"], sw=1)
        edges += [bx, bx + bw]
    edges.append(CONTENT_W)
    for x1, x2 in zip(edges[0::2], edges[1::2]):
        if x2 - x1 > 0.5:
            stroke_line([(x1, seam), (x2, seam)], TEAL["stroke"], sw=2)

    els.append(text(uid("lead"), PAD_BAND, seam + (TAB_D - 13 * 1.25) / 2, LEAD,
                    size=13, color=AMBER["mid"]))

    for x, word in g["tabs"]:
        # the tab's fill runs up past the seam and down over the block's top
        # edge, so both strokes stop at the tab: what is left reads as a notch
        # cut into the block, filled by the tab.
        fill_rect(x, seam - TAB_RISE, TAB_W, TAB_D + TAB_RISE, TEAL["band"], rounded=True)
        pts = [(x, seam)]
        pts += arc_pts(x + TAB_R, seam + TAB_D - TAB_R, TAB_R, math.pi, math.pi / 2)
        pts += arc_pts(x + TAB_W - TAB_R, seam + TAB_D - TAB_R, TAB_R, math.pi / 2, 0.0)
        pts += [(x + TAB_W, seam)]
        stroke_line(pts, TEAL["stroke"], sw=2)
        els.append(text(uid("tabw"), x, seam + (TAB_D - 13 * 1.25) / 2, word,
                        size=13, color=TEAL["text"], align="center", w=TAB_W))


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

    DATA_BAND_BOTTOM = DATA_BLOCKS_BOTTOM + PAD_BAND
    teal_band = band_rect(uid("band"), 0, Y_DATA, CONTENT_W, DATA_BAND_BOTTOM - Y_DATA, TEAL, at_front=True)

    # ---------------------------------------- 1. Foundation Context (bottom)
    # Built last so its rect lands behind the Data Structures band at the seam.
    # The two bands are flush: the seam is this band's top edge, and it is also
    # the top edge of all three blocks, which start at it with no amber ground
    # in between. The header sits in a left column beside them.
    FOUND_TOP = DATA_BAND_BOTTOM

    f_specs = [
        ("icons/lucide-tag.svg", ["Finding/diagnosis definitions"], "finding models · CDEs", False,
         ["finding", "diagnosis"]),
        ("icons/healthicons-lungs.svg", ["Anatomic locations"], "anchored in RadLex", True,
         ["location"]),
        ("icons/healthicons-xray.svg", ["Exam types"], "LOINC/RSNA Playbook", True,
         ["exam type"]),
    ]
    # The first block holds two tabs, so it is the widest; it also holds the
    # longest label ("Finding/diagnosis definitions", 188px measured).
    F_WIDTHS = [236.0, 174.0, 174.0]
    BX0 = PAD_BAND + LEFT_W + LEFT_GAP
    f_positions = []
    x = BX0
    for w in F_WIDTHS:
        f_positions.append(x)
        x += w + GAP

    ROW_H_FOUND = TAB_D + max(icon_block_h(lines, desc) for _, lines, desc, _, _ in f_specs)
    tabs: list[tuple[float, str]] = []
    for xpos, bw, (ipath, lines, desc, filled, words) in zip(f_positions, F_WIDTHS, f_specs):
        icon_block(xpos, FOUND_TOP, bw, ROW_H_FOUND, ipath, AMBER, lines, desc=desc,
                   filled_icon=filled, top_inset=TAB_D)
        tabs += list(zip(tab_xs(xpos, bw, len(words)), words))
    FOUND_BLOCKS_BOTTOM = FOUND_TOP + ROW_H_FOUND

    hdr_top = FOUND_TOP + TAB_D + (ROW_H_FOUND - TAB_D - left_header_h(2, 1)) / 2
    left_header(PAD_BAND, hdr_top, "icons/lucide-book-open.svg", AMBER,
                ["Foundation", "Context"], ["shared, curated knowledge"], size=20)

    FOUND_BAND_BOTTOM = FOUND_BLOCKS_BOTTOM + PAD_BOTTOM
    amber_band = band_rect(uid("band"), 0, FOUND_TOP, CONTENT_W, FOUND_BAND_BOTTOM - FOUND_TOP,
                           AMBER, at_front=True)

    # ---------------------------------------- the seam, drawn over both bands
    draw_seam({
        "found_top": FOUND_TOP,
        "f_positions": f_positions, "f_widths": F_WIDTHS,
        "tabs": tabs,
        "teal_band": teal_band, "amber_band": amber_band,
    })
    print(f"foundation band height: {FOUND_BAND_BOTTOM - FOUND_TOP:.0f}px")

    return save(out_path)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="knowledge/drafts/pillars-b2.excalidraw",
                    help="output path relative to the repo root")
    args = ap.parse_args()
    build(args.out)


if __name__ == "__main__":
    main()
