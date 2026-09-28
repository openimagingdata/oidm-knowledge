#!/usr/bin/env python3
"""Build the OIDM "five pillars" technology-stack diagram (v3).

A layered stack, read bottom to top, each layer its own hue (no blue reused
from other diagrams in the bundle) so the picture reads without words:

  1. Foundation Context (bottom) -- shared, curated knowledge: finding and
     diagnosis definitions, anatomic locations, exam types. Short
     double-headed arrows between the three blocks, with one "relationships"
     label over the row, say the three are tied to each other.
  2. Data Structures -- this patient's data, sitting on the foundation. The
     two bands overlap by OVERLAP px and a row of thin alternating teal and
     amber threads runs through the overlap, so the layers look stitched
     together rather than merely stacked. No arrows, and never the word
     "pointer": the structures are interconnected with the foundation at
     every finding, diagnosis, location and exam type, not pointing at one.
  3. SDKs -- a thin band between the data layer and the top.
  4/5. Use Cases and Sample Applications -- two panels sharing the top band,
     joined by a short horizontal connector labelled "illustrates".

Geometry rules: every band is CONTENT_W wide and starts at x=0; vertical
gaps between bands are all BAND_GAP, except the Data/Foundation seam, which
is a deliberate overlap; band heights are computed from their contents, so
no band is taller than its own text needs.

Icons: Health Icons (CC0/MIT, outline style) for anatomy/exam/person glyphs,
Lucide (ISC, with one Feather-derived MIT icon) for everything else -- see
icons/LICENSES.md for the full source list and the two slots where Health
Icons had no matching glyph and Lucide was used instead. Health Icons'
outline set is filled-path art on a 48x48 viewBox with built-in padding, so
it renders optically smaller than Lucide's 24x24 stroke art at the same box
size; ICON_FILLED compensates.

Output: knowledge/drafts/pillars.excalidraw; render with render_excalidraw.py.
"""
from excalib import els, base, text, image, save, AMBER, TEAL, VIOLET, ROSE, GREEN, CAPTION

# ---------------------------------------------------------------- palette
# The five-hue palette (matched lightness steps, no hue repeats, no blue
# reused from any prior diagram) lives in excalib.py as AMBER/TEAL/VIOLET/
# ROSE/GREEN so other diagrams -- e.g. build_three_axes.py, a detail view
# of the Foundation Context/AMBER pillar -- can match it exactly.

# ---------------------------------------------------------------- layout constants
CONTENT_W = 880
BAND_GAP = 24     # the one vertical gap between bands (the seam overlaps instead)
PAD_BAND = 20     # a band's own inner padding on all sides
GAP = 20          # gap between sibling blocks inside a band
GAP_REL = 64      # wider gap, so a double-headed arrow reads as an arrow and not a diamond
ICON = 28         # harmonized icon render size
ICON_FILLED = 32  # filled-path icon sets need a bigger box to match optically
OVERLAP = 36      # how far the Data Structures band sits over the Foundation band

_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def band_rect(id_: str, x: float, y: float, w: float, h: float, pal: dict, at_front=False) -> dict:
    """Draw a band's background rectangle. Pass at_front=True when the band's
    true height is only known after laying out its header/blocks (they were
    already appended to els) -- this inserts the rect at index 0 so it still
    paints behind its own contents instead of covering them. Note the order
    that matters at the seam: whichever band rect is inserted at index 0 last
    ends up furthest back, so Foundation Context must be built last for the
    Data Structures band to sit on top of it in the overlap."""
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
    block reads as 'inside' the band, not a separate object. h is passed in
    (not computed per-block) so every block in a row shares the same height
    even when label line counts differ. Returns the block rectangle."""
    r = base("rectangle", uid("blk"), x, y, w, h, pal["stroke"], pal["block"], sw=1)
    r["roundness"] = {"type": 3}
    els.append(r)
    cx = x + w / 2
    # center this block's own (possibly shorter) content within the shared h
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


# ============================================================ 5/4. Use Cases | Sample Applications
# Top band: two panels, title + one-line subtitle each, so the band is only
# as tall as that text needs.
Y_TOP = 0
GAP_MID = 104                       # wide enough for the "illustrates" label to sit clear of both panels
PANEL_PAD = 14
PANEL_INSET = PAD_BAND - 2   # same left inset as the full-width band headers
PANEL_TITLE = 18
PANEL_H = PANEL_PAD + PANEL_TITLE * 1.3 + 13 * 1.25 + PANEL_PAD
panel_w = (CONTENT_W - GAP_MID) / 2

band_rect(uid("panel"), 0, Y_TOP, panel_w, PANEL_H, ROSE)
band_rect(uid("panel"), panel_w + GAP_MID, Y_TOP, panel_w, PANEL_H, GREEN)
band_header(PANEL_INSET, Y_TOP + PANEL_PAD, "icons/lucide-lightbulb.svg", ROSE,
            "Use Cases", "what the project wants built", size=PANEL_TITLE)
band_header(panel_w + GAP_MID + PANEL_INSET, Y_TOP + PANEL_PAD, "icons/lucide-app-window.svg", GREEN,
            "Sample Applications", "what has been built", size=PANEL_TITLE)

# "illustrates": a short horizontal connector at the panels' mid-height,
# spanning only the gap between them, with its label on a plate above it.
conn_y = Y_TOP + PANEL_H / 2
hconn(panel_w + 2, panel_w + GAP_MID - 2, conn_y, CAPTION)
chip(panel_w + GAP_MID / 2, conn_y - 7 - (13 * 1.25 + 6), "illustrates",
     "#ffffff", "transparent", CAPTION)

Y_SDK = Y_TOP + PANEL_H + BAND_GAP

# ============================================================ 3. SDKs (thin full-width band)
sdk_hdr_bottom = band_header(PAD_BAND - 2, Y_SDK + 16, "icons/lucide-package.svg", VIOLET,
                             "SDKs", "wrap the structures · attach the shared knowledge · support authoring",
                             size=18)
SDK_BOTTOM = sdk_hdr_bottom + 16
band_rect(uid("band"), 0, Y_SDK, CONTENT_W, SDK_BOTTOM - Y_SDK, VIOLET, at_front=True)

Y_DATA = SDK_BOTTOM + BAND_GAP

# ============================================================ 2. Data Structures
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

# The seam: the Foundation band's top edge runs OVERLAP px above the Data
# band's bottom edge, behind it, so the two bands interlock instead of
# stacking. Everything in the Data band clears that line.
FOUND_TOP = DATA_BLOCKS_BOTTOM + 18
DATA_BAND_BOTTOM = FOUND_TOP + OVERLAP
band_rect(uid("band"), 0, Y_DATA, CONTENT_W, DATA_BAND_BOTTOM - Y_DATA, TEAL, at_front=True)

# ============================================================ 1. Foundation Context (bottom)
# Built last so its rect lands behind the Data Structures band at the seam.
SEAM_CAP_Y = DATA_BAND_BOTTOM + 50
seam_cap_bottom = SEAM_CAP_Y + 13 * 1.25
hdr_bottom_f = band_header(PAD_BAND - 2, seam_cap_bottom + 16, "icons/lucide-book-open.svg", AMBER,
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

# double-headed arrows in the two gaps between the three blocks
arrow_y = F_ROW_Y + ROW_H_FOUND / 2
for i in range(2):
    x1 = f_positions[i] + W3 + 6
    hconn(x1, x1 + GAP_REL - 12, arrow_y, AMBER["stroke"], sw=2, both=True)

FOUND_BAND_BOTTOM = FOUND_BLOCKS_BOTTOM + PAD_BAND
band_rect(uid("band"), 0, FOUND_TOP, CONTENT_W, FOUND_BAND_BOTTOM - FOUND_TOP, AMBER, at_front=True)

# ============================================================ the stitch, drawn over both bands
# Thin threads alternating the two bands' colors, running through the
# overlap and out either side of it, so the seam reads as stitched.
N_THREADS = 12
margin = 62
span = CONTENT_W - 2 * margin
SEAM = DATA_BAND_BOTTOM   # the visible boundary: the Data band's lower edge
# A row of identical verticals reads as a fence, so the two colors
# interdigitate instead: every amber thread runs up out of the Foundation
# band and well into the Data Structures band, every teal thread runs down
# out of the Data band and well into the Foundation band, and they overlap
# across the seam. Each layer is threaded through the other.
for i in range(N_THREADS):
    x = margin + span * i / (N_THREADS - 1)
    if i % 2 == 0:
        y1, y2, color = SEAM - 44, SEAM + 4, AMBER["stroke"]
    else:
        y1, y2, color = SEAM - 4, SEAM + 40, TEAL["stroke"]
    ln = base("line", uid("thread"), x, y1, 0, y2 - y1, color, "transparent", sw=2)
    ln.update({"points": [[0, 0], [0, y2 - y1]], "boundElements": None})
    els.append(ln)

els.append(text(uid("seaml"), 0, SEAM_CAP_Y,
                "interconnected at every finding, diagnosis, location, and exam type",
                size=13, color=CAPTION, align="center", w=CONTENT_W))

save("knowledge/drafts/pillars.excalidraw")
