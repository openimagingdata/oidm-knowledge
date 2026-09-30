#!/usr/bin/env python3
"""Build the OIDM "five pillars" stack diagram -- seam variant B3, v7.

Descended from ../build_pillars.py seam b. Where that file offered three
alternative treatments of one seam, this one uses a single treatment -- a
castellated edge -- at every place two bands meet, so the stack's joints are
one visual language instead of three unrelated devices.

A castellated joint is a square wave drawn once along the boundary of two
bands that overlap by the wave's swing. The upper band is painted over the
lower one throughout the overlap; castellate() then restores the lower band's
fill in the gaps between the teeth and strokes the wave in the upper band's
colour, so the two bands share one interlocking edge with no gap, no tab
shapes and no connectors. Teeth are always twice as wide as the gaps between
them, whatever their count or depth, which is what makes the three joints read
as a family.

The three joints, top to bottom:

  Sample Applications -> SDKs      four green teeth, JOINT_DEPTH deep, labelled
                                   with what an application gets: create, read,
                                   resolve, author. Only the right half of the
                                   SDK band's top edge is joined; Use Cases
                                   keeps a plain BAND_GAP above it, because it
                                   is what the project wants built rather than
                                   something running on the SDKs.
  SDKs -> Data Structures          two wide violet teeth (wraps, manipulates
                                   instances) plus one narrow tooth at the
                                   right margin that does not close: it carries
                                   on down a reserved lane beside the cards.
  Data Structures -> Foundation    one castellated line across the whole of the
                                   Foundation band's top edge, SEAM_DEPTH deep:
                                   four teal teeth carrying the attachment
                                   kinds, then, flush right, one violet tooth
                                   where the lane lands, reading what the SDKs
                                   do to the foundation. The lane stops at that
                                   edge rather than running on into the band,
                                   so the band keeps an even margin both sides,
                                   and the SDKs' reach into the foundation is
                                   shown without an arrow.

Two depths, belonging to the edge rather than to the joint: JOINT_DEPTH for the
two joints above, SEAM_DEPTH for the Foundation band's top edge, which the seam
and the lane's foot share.

Each joint whose upper band has room for it carries a lead line in that band's
gutter, left-aligned on the first tooth so its colon runs into the list; the
SDK/Data joint has no gutter and so no lead.

Icons: Health Icons (CC0/MIT, outline style) for anatomy/exam/person glyphs,
Lucide (ISC, with one Feather-derived MIT icon) for everything else -- see
icons/LICENSES.md. ICON_FILLED compensates for Health Icons' filled-path art
rendering optically smaller than Lucide's stroke art at the same box size.

Output: knowledge/drafts/pillars-b3.excalidraw (override with --out); render
with render_excalidraw.py.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from excalib import els, base, text, image, save, AMBER, TEAL, VIOLET, ROSE, GREEN, CAPTION  # noqa: E402

# ---------------------------------------------------------------- layout constants
CONTENT_W = 880
BAND_GAP = 24     # the vertical gap wherever two bands do NOT join
PAD_BAND = 20     # a band's own inner padding on all sides
GAP = 20          # gap between sibling blocks inside a band, both rows
ICON = 28         # harmonized icon render size
ICON_FILLED = 32  # filled-path icon sets need a bigger box to match optically
CORNER_R = 32     # Excalidraw's adaptive corner radius for a band-sized rectangle

# ---------------------------------------------------------------- joint constants
TOOTH_RATIO = 2      # every joint: a tooth is this many gaps wide
JOINT_OVERRUN = 3.0  # a gap's fill runs this far past the lower level, to bury
                     # the upper band's own border where it crosses the gap
LEAD_GAP = 10.0      # clearance between a lead line and the wave's upper level

SEAM_DEPTH = 36.0    # Data Structures -> Foundation Context
SEAM_WORDS = ["finding", "diagnosis", "location", "exam type"]
SEAM_LEAD = "woven together at every:"

JOINT_DEPTH = 24.0   # the two smaller joints
APP_WORDS = ["create", "read", "resolve", "author"]
APP_LEAD = "an application can:"
SDK_WORDS = ["wraps", "manipulates instances"]

LANE_W = 34.0        # the narrow violet tooth that carries on down. 28 read as a
                     # wire rather than as structure, so this is a little wider.
LANE_CLEAR = 12.0    # clear space between the Data Structures cards and the lane
# The lane's foot: one wide violet tooth cut into the Foundation band's top edge,
# at the same depth as the seam's own teeth, so the whole of that edge is one
# castellated line -- four teal teeth and, where the lane lands, a violet one.
# Two separate teeth were the brief; they cannot be drawn, because a tooth wide
# enough for the longer phrase does not sit under a 34px lane, so the second
# would float unattached. The middot carries the two roles instead.
FOOT_LABEL = "attaches to · authors & maintains"
FOOT_PAD = 20.0      # horizontal padding inside the foot, as in the other wide teeth

DATA_TOP_PAD = 34.0  # Data Structures' header, clear of the violet teeth
FOUND_TOP_PAD = 45.0 # Foundation Context's header, clear of the teal teeth
FOUND_HDR_GAP = 12.0
FOUND_ROW_SHRINK = 11.0
FOUND_BOTTOM_PAD = 15.0

# Measured, not estimated: excalib.text()'s 0.58 * fontSize per character is
# 25-40% wide for these strings, which blew the "illustrates" plate out to twice
# the width of its own text and swallowed the connector either side of it. Only
# strings positioned or sized by their width need an entry; a word centred in a
# tooth does not. Widths in px for Helvetica as headless Chromium resolves it --
# see "Measuring text instead of estimating it" in tools/diagrams/README.md.
MEASURED = {
    ("illustrates", 13): 54.9,
    (SEAM_LEAD, 13): 142.4,
    (APP_LEAD, 13): 108.4,
    (FOOT_LABEL, 13): 190.0,
}
FOOT_W = MEASURED[(FOOT_LABEL, 13)] + 2 * FOOT_PAD

_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def even_teeth(x0: float, x1: float, n: int) -> list[tuple[float, float]]:
    """n teeth evenly spread between x0 and x1, each TOOTH_RATIO units wide with
    a one-unit gap between them and at both ends, filling the span exactly."""
    unit = (x1 - x0) / (n * TOOTH_RATIO + n + 1)
    return [(x0 + ((TOOTH_RATIO + 1) * i + 1) * unit,
             x0 + ((TOOTH_RATIO + 1) * i + 1 + TOOTH_RATIO) * unit) for i in range(n)]


# ---------------------------------------------------------------- primitives
def band_rect(id_: str, x: float, y: float, w: float, h: float, pal: dict, at_front=False) -> dict:
    """Draw a band's background rectangle. Pass at_front=True when the band's
    true height is only known after laying out its header/blocks (they were
    already appended to els) -- this inserts the rect at index 0 so it still
    paints behind its own contents instead of covering them.

    The order this produces is what makes the joints work: each band rect is
    inserted at 0 after the one above it, so the stack paints back to front,
    bottom band first, and every band covers the one below it wherever they
    overlap. castellate() then only has to put the lower band's colour back."""
    r = base("rectangle", id_, x, y, w, h, pal["stroke"], pal["band"])
    r["roundness"] = {"type": 3}
    if at_front:
        els.insert(0, r)
    else:
        els.append(r)
    return r


def band_header(x: float, y: float, icon_path: str, pal: dict, title: str,
                subtitle: str | None, size=20, filled_icon=False) -> float:
    """Bold band title with its icon to the left, subtitle below. A band whose
    edges already say what it does takes subtitle=None. Returns bottom y."""
    s = ICON_FILLED if filled_icon else ICON
    image(uid("bicon"), x, y - (s - ICON) / 2 - 2, s, s, icon_path, color=pal["stroke"])
    els.append(text(uid("btitle"), x + ICON + 12, y, title, size=size, color=pal["text"]))
    y2 = y + size * 1.3
    if subtitle is None:
        return y2
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
    block reads as 'inside' the band, not a separate object. Content is
    centered in h, so passing an h below icon_block_h() trims the block's own
    padding without touching the icon or the type."""
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
    w = MEASURED.get((s, size), len(s) * size * 0.58) + 2 * pad_x
    h = size * 1.25 + 2 * pad_y
    r = base("rectangle", uid("chip"), cx - w / 2, y_top, w, h, stroke, fill, sw=1)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(uid("chipt"), cx - w / 2 + pad_x, y_top + pad_y, s, size=size, color=color,
                    align="center", w=w - 2 * pad_x))
    return y_top + h


def hconn(x1: float, x2: float, y: float, color: str, sw=1) -> None:
    """A plain horizontal connector."""
    a = base("line", uid("conn"), x1, y, x2 - x1, 0, color, "transparent", sw=sw)
    a.update({"points": [[0, 0], [x2 - x1, 0]], "boundElements": None})
    els.append(a)


def fill_rect(x: float, y: float, w: float, h: float, fill: str) -> dict:
    """An unstroked patch of colour -- used to carry one band's fill back
    across the other band's, without either border's stroke showing through."""
    r = base("rectangle", uid("fill"), x, y, w, h, "transparent", fill, sw=1)
    r["roundness"] = None
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


def corner_fix(y_top: float, y_bot: float, pal: dict, anchor: dict,
               x_from: float, x_to: float) -> None:
    """A rounded rectangle's corner curves away from its own edge, so where a
    band is overlapped at a joint its corner leaves a notch of bare page. Fill
    the notch with that band's own colour.

    The patch is restacked to sit directly above `anchor` -- the band rect it
    belongs to -- rather than on top of everything the joint is drawn after, so
    it can be as deep as the corner radius without covering a header or a
    card."""
    made = [fill_rect(x_from - 1, y_top, CORNER_R + 1, y_bot - y_top, pal["band"]),
            fill_rect(x_to - CORNER_R, y_top, CORNER_R + 1, y_bot - y_top, pal["band"])]
    for e in reversed(made):
        els.remove(e)
        els.insert(els.index(anchor) + 1, e)


# ============================================================ the castellated joint
def castellate(hi: float, lo: float, teeth: list[tuple[float, float]], words: list[str | None],
               upper: dict, lower: dict, upper_band: dict, lower_band: dict,
               x_from: float = 0.0, x_to: float = CONTENT_W,
               lower_borders: tuple[bool, bool] = (True, True),
               open_teeth: tuple[int, ...] = (), lead: str | None = None) -> None:
    """Draw one interlocking edge between two overlapping bands.

    hi/lo are the wave's upper and lower levels: the lower band's rect starts at
    hi, the upper band's ends at lo, and the upper band owns the whole overlap
    until this runs. x_from/x_to bound the joint, which need not be the full
    width. lower_borders says whether the lower band actually has a side border
    at each end (it does not where the joint stops short of the band's own
    edge). A tooth listed in open_teeth is left unclosed, for something else to
    carry on downwards from.
    """
    corner_fix(lo - CORNER_R, lo, upper, upper_band, x_from, x_to)
    corner_fix(hi, hi + CORNER_R, lower, lower_band, x_from, x_to)

    # The lower band's colour back over the gaps: flush with the upper level,
    # since the wave is stroked along it last, and past the lower one to bury
    # the upper band's border. The end gaps overshoot the side borders too.
    for x1, x2 in zip([x_from] + [t[1] for t in teeth], [t[0] for t in teeth] + [x_to]):
        a = x1 - 1 if x1 == x_from else x1
        b = x2 + 1 if x2 == x_to else x2
        if b - a > 2:   # a tooth flush with the end leaves no gap to fill
            fill_rect(a, hi, b - a, lo - hi + JOINT_OVERRUN, lower["band"])
    for x, has_lower in ((x_from, lower_borders[0]), (x_to, lower_borders[1])):
        stroke_line([(x, hi - CORNER_R), (x, hi)], upper["stroke"], sw=2)
        if has_lower:
            stroke_line([(x, hi), (x, lo + CORNER_R)], lower["stroke"], sw=2)

    # The wave itself, stroked once. An open tooth breaks it into two runs.
    runs: list[list[tuple[float, float]]] = []
    cur: list[tuple[float, float]] = [(x_from, hi)]
    for j, (x1, x2) in enumerate(teeth):
        if j in open_teeth:
            cur.append((x1, hi))
            runs.append(cur)
            cur = [(x2, hi)]
        else:
            cur += [(x1, hi), (x1, lo), (x2, lo), (x2, hi)]
    cur.append((x_to, hi))
    runs.append(cur)
    for run in runs:
        if len(set(run)) > 1:   # an open tooth flush with the end leaves no run
            stroke_line(run, upper["stroke"], sw=2)

    for word, (x1, x2) in zip(words, teeth):
        if word:
            els.append(text(uid("jw"), x1, hi + (lo - hi - 13 * 1.25) / 2, word,
                            size=13, color=upper["text"], align="center", w=x2 - x1))

    # The lead's colon runs into the list, so it starts where the first tooth
    # does; anywhere left of that it reads as a label for the first gap instead.
    if lead:
        els.append(text(uid("jl"), teeth[0][0], hi - LEAD_GAP - 13 * 1.25, lead,
                        size=13, color=upper["mid"]))


def draw_lane(x1: float, x2: float, y_top: float, foot_top: float, depth: float,
              foot_w: float, label: str) -> None:
    """The narrow violet tooth carried on down its lane, ending where the
    Foundation band's top edge begins by widening into one tooth cut into it.
    Drawn last, so it passes in front of every band and joint it crosses."""
    foot_left = x2 - foot_w
    fill_rect(x1, y_top, x2 - x1, foot_top - y_top, VIOLET["band"])
    fill_rect(foot_left, foot_top, foot_w, depth, VIOLET["band"])
    stroke_line([(x1, y_top), (x1, foot_top), (foot_left, foot_top),
                 (foot_left, foot_top + depth), (x2, foot_top + depth), (x2, y_top)],
                VIOLET["stroke"], sw=2)
    els.append(text(uid("lanet"), foot_left, foot_top + (depth - 13 * 1.25) / 2, label,
                    size=13, color=VIOLET["text"], align="center", w=foot_w))


# ============================================================ the stack
def build(out_path: str) -> str:
    # ---------------------------------------- 5/4. Use Cases | Sample Applications
    Y_TOP = 0
    GAP_MID = 120                 # wide enough for "illustrates" to sit on the connector
                                  # with a readable stub of line showing each side
    PANEL_PAD = 16                # same as the SDK band's, so the two headers'
                                  # identically built bands come out the same height
    PANEL_INSET = PAD_BAND - 2    # same left inset as the full-width band headers
    PANEL_TITLE = 18
    PANEL_H = PANEL_PAD + PANEL_TITLE * 1.3 + 13 * 1.25 + PANEL_PAD
    # Sample Applications takes the larger share, so its four teeth get closer to
    # the proportions of the seam's; Use Cases only has to hold its own subtitle.
    use_w = (CONTENT_W - GAP_MID) * 0.4
    app_w = (CONTENT_W - GAP_MID) - use_w
    APP_X = use_w + GAP_MID

    # The SDK band's top edge is where Sample Applications comes down to meet it;
    # Use Cases keeps a plain gap above that same edge.
    SDK_TOP = Y_TOP + PANEL_H + BAND_GAP
    APP_LO = SDK_TOP + JOINT_DEPTH

    band_rect(uid("panel"), 0, Y_TOP, use_w, PANEL_H, ROSE)
    app_panel = band_rect(uid("panel"), APP_X, Y_TOP, app_w, APP_LO - Y_TOP, GREEN)
    band_header(PANEL_INSET, Y_TOP + PANEL_PAD, "icons/lucide-lightbulb.svg", ROSE,
                "Use Cases", "what the project wants built", size=PANEL_TITLE)
    band_header(APP_X + PANEL_INSET, Y_TOP + PANEL_PAD, "icons/lucide-app-window.svg", GREEN,
                "Sample Applications", "what has been built", size=PANEL_TITLE)
    conn_y = Y_TOP + PANEL_PAD + (PANEL_TITLE * 1.3 + 13 * 1.25) / 2
    hconn(use_w + 2, APP_X - 2, conn_y, CAPTION)
    chip(use_w + GAP_MID / 2, conn_y - (13 * 1.25 + 6) / 2, "illustrates",
         "#ffffff", "transparent", CAPTION)

    # ---------------------------------------- 3. SDKs (thin full-width band)
    # No subtitle: the three joints on this band's two edges now say everything
    # the subtitle used to, word for word.
    sdk_hdr_bottom = band_header(PAD_BAND - 2, SDK_TOP + 16, "icons/lucide-package.svg", VIOLET,
                                 "SDKs", None, size=18)
    SDK_BOTTOM = sdk_hdr_bottom + 16
    SDK_LO = SDK_BOTTOM + JOINT_DEPTH
    sdk_band = band_rect(uid("band"), 0, SDK_TOP, CONTENT_W, SDK_LO - SDK_TOP, VIOLET, at_front=True)

    # ---------------------------------------- 2. Data Structures
    # A lane down the right margin is left clear in the card row below, for the
    # narrow violet tooth to travel in. It runs flush with the bands' own right
    # border: inset from it, the strip of band colour left outside the lane reads
    # as a sliver rather than as a lane. It stops at the Foundation band's top
    # edge, so that band keeps an even PAD_BAND margin on both sides.
    LANE_X2 = CONTENT_W
    LANE_X1 = LANE_X2 - LANE_W
    ROW_RIGHT = LANE_X1 - LANE_CLEAR

    Y_DATA = SDK_BOTTOM
    hdr_bottom = band_header(PAD_BAND - 2, Y_DATA + DATA_TOP_PAD, "icons/lucide-layers.svg", TEAL,
                             "Data Structures", "this patient · Patient Context", size=20)
    BLOCK_ROW_Y = hdr_bottom + 14
    W4 = (ROW_RIGHT - PAD_BAND - 3 * GAP) / 4
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

    # room below the cards for the seam's lead line and the seam's own swing
    DATA_BAND_BOTTOM = DATA_BLOCKS_BOTTOM + SEAM_DEPTH + 2 * LEAD_GAP + 13 * 1.25
    teal_band = band_rect(uid("band"), 0, Y_DATA, CONTENT_W, DATA_BAND_BOTTOM - Y_DATA, TEAL, at_front=True)

    # ---------------------------------------- 1. Foundation Context (bottom)
    FOUND_TOP = DATA_BAND_BOTTOM - SEAM_DEPTH
    hdr_bottom_f = band_header(PAD_BAND - 2, FOUND_TOP + FOUND_TOP_PAD,
                               "icons/lucide-book-open.svg", AMBER,
                               "Foundation Context", "shared, curated knowledge", size=20)
    F_ROW_Y = hdr_bottom_f + FOUND_HDR_GAP
    W3 = (CONTENT_W - 2 * PAD_BAND - 2 * GAP) / 3
    f_positions = [PAD_BAND + i * (W3 + GAP) for i in range(3)]
    f_specs = [
        ("icons/lucide-tag.svg", ["Finding/diagnosis definitions"], "finding models · CDEs", False),
        ("icons/healthicons-lungs.svg", ["Anatomic locations"], "anchored in RadLex", True),
        ("icons/healthicons-xray.svg", ["Exam types"], "LOINC/RSNA Playbook", True),
    ]
    ROW_H_FOUND = max(icon_block_h(lines, desc) for _, lines, desc, _ in f_specs) - FOUND_ROW_SHRINK
    for xpos, (ipath, lines, desc, filled) in zip(f_positions, f_specs):
        icon_block(xpos, F_ROW_Y, W3, ROW_H_FOUND, ipath, AMBER, lines, desc=desc, filled_icon=filled)
    FOUND_BAND_BOTTOM = F_ROW_Y + ROW_H_FOUND + FOUND_BOTTOM_PAD
    amber_band = band_rect(uid("band"), 0, FOUND_TOP, CONTENT_W, FOUND_BAND_BOTTOM - FOUND_TOP,
                           AMBER, at_front=True)

    # ---------------------------------------- the three joints, top to bottom
    castellate(SDK_TOP, APP_LO, even_teeth(APP_X, CONTENT_W, len(APP_WORDS)), APP_WORDS,
               GREEN, VIOLET, app_panel, sdk_band, x_from=APP_X, x_to=CONTENT_W,
               lower_borders=(False, True), lead=APP_LEAD)

    sdk_teeth = even_teeth(0, LANE_X1, len(SDK_WORDS)) + [(LANE_X1, LANE_X2)]
    castellate(SDK_BOTTOM, SDK_LO, sdk_teeth, SDK_WORDS + [None], VIOLET, TEAL,
               sdk_band, teal_band, open_teeth=(len(SDK_WORDS),))

    # The seam's own teeth share this edge with the lane's foot, so they are laid
    # out in the width the foot leaves: one more gap, then the foot, flush right.
    castellate(FOUND_TOP, DATA_BAND_BOTTOM, even_teeth(0, CONTENT_W - FOOT_W, len(SEAM_WORDS)),
               SEAM_WORDS, TEAL, AMBER, teal_band, amber_band, lead=SEAM_LEAD)

    draw_lane(LANE_X1, LANE_X2, SDK_BOTTOM, FOUND_TOP, SEAM_DEPTH, FOOT_W, FOOT_LABEL)

    print(f"foundation band below its edge: {FOUND_BAND_BOTTOM - FOUND_TOP:.0f}px; "
          f"figure {FOUND_BAND_BOTTOM:.0f}px tall")
    return save(out_path)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="knowledge/drafts/pillars-b3.excalidraw",
                    help="output path relative to the repo root")
    args = ap.parse_args()
    build(args.out)


if __name__ == "__main__":
    main()
