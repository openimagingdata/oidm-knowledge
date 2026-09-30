#!/usr/bin/env python3
"""Build the OIDM "three axes of Foundation Context" detail diagram.

A smaller companion to build_pillars.py, zoomed into the Foundation
Context (AMBER) pillar of that stack: the three axes shared knowledge is
organized along -- findings/diagnoses, anatomic locations, exam types --
each a curated layer over an existing external standard, and each with a
hierarchy of its own. Same AMBER palette and same icon files as the main
stack diagram (from excalib.py / icons/), so the two figures read as one
family. Icons: Lucide (tag), Health Icons (lungs, x-ray).

Landscape, three independent columns -- nothing joins them in this
figure, by design. Each column carries:
  - icon, title, a short "WHAT/WHERE/HOW" tagline
  - stacked labelled sections: a full-width band naming the section,
    then that section's example tree indented TREE_INDENT from the
    column's inner edge
  - a small darker block at the bottom: "layered over: <the external
    standard(s) this axis anchors to>"
The figure ends at the bottom of the columns; there is no caption.

All three columns share the band grammar, so they read as one figure:
the findings column bands the next-generation CDE schema's node kinds
(Findings, Diagnoses, Assessments, Data Elements, Measurements), the
anatomy column bands body regions, and the exam column bands modalities.
Each band restarts the connector bookkeeping, so a section's tree never
links back into the section above it.

Tree rows come in three kinds. A "band" is the section header. A "node"
is a concept in the hierarchy, drawn with real line connectors rather
than box-drawing characters so the indentation is exact in a
proportional font. An "ann" is a muted annotation hanging off the node
above it -- a value set, or the unit family a measurement kind implies.
It is half-indented and takes no connector, because it is not a child
concept. A measurement names the KIND of quantity; the units follow from
the kind, so "length" is annotated "mm, cm, ..." rather than one unit.

The columns are the same height and their "layered over" blocks line up.
A column with fewer rows spreads them toward ROW_H_MAX so the leading
stays close across columns; whatever space is still left over falls
above that column's bottom block, because every column's first band must
start on the same line.

Text widths below were measured in headless Chromium at the render font
(`Helvetica, Segoe UI Emoji`), per tools/diagrams/README.md. They place
the muted suffix after a root label and let the build assert that no row
overflows its column, neither of which can be estimated. CONTENT_W is
set by the widest single row (the `presence` value set) plus the margins.

Exam type names are real LOINC/RSNA Playbook LongCommonName values,
checked against ~/exam-types/sources/LoincRsnaRadiologyPlaybook.xlsx --
note the capital V in "XR Knee 2 Views", that the thyroid entry is "US
Thyroid gland" rather than "US Thyroid", and that the Playbook has no
"XR Chest Portable" (its portable names all begin "Portable XR ..."), so
the second XR Chest child here is "XR Chest PA and Lateral". A family
root such as "XR Chest" is a preferred-name family, not itself an entry.

Output: knowledge/drafts/three-axes.excalidraw; render with
render_excalidraw.py at `--width 1010 --scale 1`.
"""
from excalib import els, base, text, image, save, AMBER

ICON = 36
ROOT_SIZE = 14
CHILD_SIZE = 13
BAND_SIZE = 13
BAND_FILL = "#fcd34d"      # one step darker than the column's block fill

W14 = {
    "pulmonary nodule": 111.3, "pulmonary neoplasm": 130.0, "Lung-RADS": 74.7,
    "Salter-Harris category": 136.2, "presence": 57.6, "severity": 48.2,
    "length": 38.1, "CT density": 66.9,
    "lung": 26.5, "pleural space": 83.3, "mediastinum": 79.4, "kidney": 40.5,
    "liver": 25.7, "spleen": 41.3, "brain": 31.1, "orbit": 27.2,
    "urinary bladder": 93.4, "prostate": 50.6,
    "CT Chest": 59.1, "MR Knee": 58.4, "MR Brain": 58.3, "XR Knee": 56.0,
    "XR Chest": 59.9, "US Abdomen": 83.3, "US Thyroid gland": 108.2,
}
W13 = {
    "solid": 26.7, "part-solid": 53.5, "non-solid": 52.8,
    "non-small cell lung cancer": 150.3, "adenocarcinoma of the lung": 160.4,
    "present · absent · indeterminate · unknown": 247.9,
    "minimal · mild · moderate · severe": 197.2, "mm, cm, ...": 64.3, "HU": 18.8,
    "right lung": 53.5, "left lung": 45.5, "heart": 29.6,
    "upper lobe of right lung": 133.0, "middle lobe of right lung": 138.0,
    "lower lobe of right lung": 130.8, "left kidney": 58.5, "right kidney": 66.5,
    "renal pelvis": 65.8, "cerebellum": 63.6, "frontal lobe": 64.3,
    "CT Chest WO contrast": 130.7, "CT Chest W contrast IV": 136.5,
    "CT Chest WO and W contrast IV": 187.8, "CT Lung parenchyma WO contrast": 200.9,
    "CTA Chest vessels": 109.6, "MR Knee WO contrast": 130.0,
    "MR Knee W contrast IV": 135.8, "MR Brain WO contrast": 130.0,
    "MR Brain WO and W contrast IV": 187.1, "XR Knee 2 Views": 100.9,
    "XR Knee 3 Views": 100.9, "XR Chest 2 Views": 104.5,
    "XR Chest PA and Lateral": 144.3, "US Abdomen limited": 118.5,
    "US Abdomen RUQ": 109.8, "(preferred family)": 99.0,
    "each a LOINC/RSNA Playbook entry": 211.7,
}

_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def rule(x: float, y: float, w: float) -> None:
    ln = base("line", uid("rule"), x, y, w, 0, AMBER["stroke"], "transparent", sw=1)
    ln.update({"points": [[0, 0], [w, 0]], "boundElements": None, "opacity": 35})
    els.append(ln)


def connector(x1: float, y1: float, x2: float, y2: float) -> None:
    ln = base("line", uid("tc"), x1, y1, x2 - x1, y2 - y1, AMBER["stroke"], "transparent", sw=1)
    ln.update({"points": [[0, 0], [x2 - x1, y2 - y1]], "boundElements": None, "opacity": 45})
    els.append(ln)


# ------------------------------------------------------------------ tree
INDENT = 18
ANN_INDENT = 8      # half a step: an annotation is not a child concept
ROW_H = 19
ROW_H_MAX = 23      # a shorter column spreads its rows to fill the region,
                    # but only this far: leading that differs much more than
                    # this between columns stops reading as one figure
BAND_H = 20
BAND_PAD_X = 10
BAND_GAP_ABOVE = 12
BAND_GAP_BELOW = 6

Row = tuple[str, int, str, "str | None", float]


def row_width(kind: str, depth: int, label: str, suffix: str | None, _gap: float = 0) -> float:
    """Rendered width of a row. A band spans the column, so it constrains nothing."""
    if kind == "band":
        return 0.0
    if kind == "ann":
        return depth * INDENT + ANN_INDENT + W13[label]
    w = depth * INDENT + (W14[label] if depth == 0 else W13[label])
    return w + (7 + W13[suffix] if suffix else 0)


def tree_fixed_h(rows: list[Row]) -> float:
    """Height of everything in a tree that does not stretch: bands and gaps."""
    return sum((BAND_GAP_ABOVE if i else 0) + BAND_H + BAND_GAP_BELOW if k == "band" else g
               for i, (k, _d, _l, _s, g) in enumerate(rows))


def n_rows(rows: list[Row]) -> int:
    return sum(1 for r in rows if r[0] != "band")


def tree(x: float, y: float, rows: list[Row], row_h: float, band_x: float, band_w: float) -> float:
    """Draw the banded sections of one column; returns the y it ends at.

    x is the tree's own left edge (indented from band_x); bands are drawn
    full width from band_x. Connectors are lines, not characters: a
    vertical dropping from just under the parent's label to the child
    row's center at the parent's connector column, and a short horizontal
    stub into the child label.
    """
    centers: dict[int, float] = {}
    cy = y
    for i, (kind, depth, label, suffix, gap) in enumerate(rows):
        if kind == "band":
            if i:
                cy += BAND_GAP_ABOVE
            b = base("rectangle", uid("tb"), band_x, cy, band_w, BAND_H,
                     "transparent", BAND_FILL, sw=1)
            b["roundness"] = {"type": 3}
            els.append(b)
            els.append(text(uid("tbt"), band_x + BAND_PAD_X,
                            cy + (BAND_H - BAND_SIZE * 1.25) / 2, label,
                            size=BAND_SIZE, color=AMBER["text"]))
            cy += BAND_H + BAND_GAP_BELOW
            centers.clear()     # a new section starts its own hierarchy
            continue

        cy += gap + row_h / 2
        if kind == "ann":
            els.append(text(uid("ta"), x + depth * INDENT + ANN_INDENT,
                            cy - CHILD_SIZE * 1.25 / 2, label,
                            size=CHILD_SIZE, color=AMBER["mid"]))
            cy += row_h / 2
            continue

        size = ROOT_SIZE if depth == 0 else CHILD_SIZE
        color = AMBER["text"] if depth == 0 else AMBER["stroke"]
        tx = x + depth * INDENT
        if depth > 0:
            col_x = x + (depth - 1) * INDENT + 7
            # start below the parent's text, not at its center, or the
            # vertical strikes through the parent label's first glyph
            connector(col_x, centers[depth - 1] + 10, col_x, cy)
            connector(col_x, cy, tx - 4, cy)
        els.append(text(uid("tn"), tx, cy - size * 1.25 / 2, label, size=size, color=color))
        if suffix:
            els.append(text(uid("tns"), tx + W14[label] + 7, cy - CHILD_SIZE * 1.25 / 2,
                            suffix, size=CHILD_SIZE, color=AMBER["mid"]))
        centers[depth] = cy
        cy += row_h / 2
    return cy


# ---------------------------------------------------------------- column
MARGIN = 18         # column inner margin: nothing sits against the border
TREE_INDENT = 16    # trees hang this far inside the band's left edge
PAD_TOP = 16
PAD_BOTTOM = 16
TITLE_SIZE = 17
TAG_SIZE = 14
NOTE_SIZE = 13
BLOCK_H = 8 + 2 * NOTE_SIZE * 1.25 + 8
NOTE_GAP = 20
TREE_BLOCK_GAP = 18

ICON_Y = PAD_TOP
TITLE_Y = ICON_Y + ICON + 9
TAG_Y = TITLE_Y + TITLE_SIZE * 1.25 + 5
RULE_Y = TAG_Y + TAG_SIZE * 1.25 + 11
TREE_TOP = RULE_Y + 12


def notes_h(notes: list[str]) -> float:
    return NOTE_GAP + len(notes) * NOTE_SIZE * 1.25 if notes else 0.0


def column_group_h(rows: list[Row], notes: list[str], row_h: float = ROW_H) -> float:
    return tree_fixed_h(rows) + n_rows(rows) * row_h + notes_h(notes)


def fitted_row_h(rows: list[Row], notes: list[str], region_h: float) -> float:
    """Spread a short column's rows to fill the shared region, up to a cap,
    so a column with fewer rows does not sit in a hole."""
    spare = region_h - notes_h(notes) - tree_fixed_h(rows)
    return max(ROW_H, min(ROW_H_MAX, spare / n_rows(rows)))


def axis_column(x: float, y: float, w: float, region_h: float, icon_path: str, title: str,
                tagline: str, rows: list[Row], notes: list[str], desc_lines: list[str]) -> None:
    r = base("rectangle", uid("col"), x, y, w, COL_H, AMBER["stroke"], AMBER["block"], sw=2)
    r["roundness"] = {"type": 3}
    els.append(r)

    cx = x + w / 2
    image(uid("coli"), cx - ICON / 2, y + ICON_Y, ICON, ICON, icon_path, color=AMBER["stroke"])
    els.append(text(uid("colt"), x + 8, y + TITLE_Y, title, size=TITLE_SIZE,
                    color=AMBER["text"], align="center", w=w - 16))
    els.append(text(uid("coltag"), x + 8, y + TAG_Y, tagline, size=TAG_SIZE,
                    color=AMBER["mid"], align="center", w=w - 16))
    rule(x + MARGIN, y + RULE_Y, w - 2 * MARGIN)    # same span as the bands

    band_x, band_w = x + MARGIN, w - 2 * MARGIN
    row_h = fitted_row_h(rows, notes, region_h)
    # top-aligned, not centered: the first band of every column then sits
    # on the same line just under the rule, which is what makes the three
    # read as one figure. Leftover space falls above the bottom block.
    top = y + TREE_TOP
    tree_bottom = tree(band_x + TREE_INDENT, top, rows, row_h, band_x, band_w)

    ny = tree_bottom + NOTE_GAP
    for ln in notes:
        els.append(text(uid("coln"), band_x, ny, ln, size=NOTE_SIZE, color=AMBER["mid"]))
        ny += NOTE_SIZE * 1.25

    rb = base("rectangle", uid("colblk"), band_x, y + BLOCK_Y, band_w, BLOCK_H,
              AMBER["text"], AMBER["stroke"], sw=1)
    rb["roundness"] = {"type": 3}
    els.append(rb)
    by = y + BLOCK_Y + (BLOCK_H - len(desc_lines) * NOTE_SIZE * 1.25) / 2 + 2
    for ln in desc_lines:
        els.append(text(uid("colblkt"), band_x + 6, by, ln, size=NOTE_SIZE,
                        color="#fef3c7", align="center", w=band_w - 12))
        by += NOTE_SIZE * 1.25


# ---------------------------------------------------------------- content
FINDINGS: list[Row] = [
    ("band", 0, "Findings", None, 0),
    ("node", 0, "pulmonary nodule", None, 0),
    ("node", 1, "solid", None, 0),
    ("node", 1, "part-solid", None, 0),
    ("node", 1, "non-solid", None, 0),
    ("band", 0, "Diagnoses", None, 0),
    ("node", 0, "pulmonary neoplasm", None, 0),
    ("node", 1, "non-small cell lung cancer", None, 0),
    ("node", 2, "adenocarcinoma of the lung", None, 0),
    ("band", 0, "Assessments", None, 0),
    ("node", 0, "Lung-RADS", None, 0),
    ("node", 0, "Salter-Harris category", None, 0),
    ("band", 0, "Data Elements", None, 0),
    ("node", 0, "presence", None, 0),
    ("ann", 0, "present · absent · indeterminate · unknown", None, 0),
    ("node", 0, "severity", None, 0),
    ("ann", 0, "minimal · mild · moderate · severe", None, 0),
    # a measurement names the KIND of quantity; the unit family follows
    ("band", 0, "Measurements", None, 0),
    ("node", 0, "length", None, 0),
    ("ann", 0, "mm, cm, ...", None, 0),
    ("node", 0, "CT density", None, 0),
    ("ann", 0, "HU", None, 0),
]

ANATOMY: list[Row] = [
    ("band", 0, "thorax", None, 0),
    ("node", 0, "lung", None, 0),
    ("node", 1, "right lung", None, 0),
    ("node", 2, "upper lobe of right lung", None, 0),
    ("node", 2, "middle lobe of right lung", None, 0),
    ("node", 2, "lower lobe of right lung", None, 0),
    ("node", 1, "left lung", None, 0),
    ("node", 0, "pleural space", None, 0),
    ("node", 0, "mediastinum", None, 0),
    ("node", 1, "heart", None, 0),
    ("band", 0, "abdomen", None, 0),
    ("node", 0, "kidney", None, 0),
    ("node", 1, "left kidney", None, 0),
    ("node", 1, "right kidney", None, 0),
    ("node", 2, "renal pelvis", None, 0),
    ("node", 0, "liver", None, 0),
    ("node", 0, "spleen", None, 0),
    ("band", 0, "head", None, 0),
    ("node", 0, "brain", None, 0),
    ("node", 1, "cerebellum", None, 0),
    ("node", 1, "frontal lobe", None, 0),
    ("node", 0, "orbit", None, 0),
    ("band", 0, "pelvis", None, 0),
    ("node", 0, "urinary bladder", None, 0),
    ("node", 0, "prostate", None, 0),
]

EXAMS: list[Row] = [
    ("band", 0, "CT", None, 0),
    ("node", 0, "CT Chest", "(preferred family)", 0),
    ("node", 1, "CT Chest WO contrast", None, 0),
    ("node", 1, "CT Chest W contrast IV", None, 0),
    ("node", 1, "CT Chest WO and W contrast IV", None, 0),
    ("node", 1, "CT Lung parenchyma WO contrast", None, 0),
    ("node", 1, "CTA Chest vessels", None, 0),
    ("band", 0, "MR", None, 0),
    ("node", 0, "MR Knee", "(preferred family)", 0),
    ("node", 1, "MR Knee WO contrast", None, 0),
    ("node", 1, "MR Knee W contrast IV", None, 0),
    ("node", 0, "MR Brain", "(preferred family)", 6),
    ("node", 1, "MR Brain WO contrast", None, 0),
    ("node", 1, "MR Brain WO and W contrast IV", None, 0),
    ("band", 0, "XR", None, 0),
    ("node", 0, "XR Knee", "(preferred family)", 0),
    ("node", 1, "XR Knee 2 Views", None, 0),
    ("node", 1, "XR Knee 3 Views", None, 0),
    ("node", 0, "XR Chest", "(preferred family)", 6),
    ("node", 1, "XR Chest 2 Views", None, 0),
    ("node", 1, "XR Chest PA and Lateral", None, 0),
    ("band", 0, "US", None, 0),
    ("node", 0, "US Abdomen", "(preferred family)", 0),
    ("node", 1, "US Abdomen limited", None, 0),
    ("node", 1, "US Abdomen RUQ", None, 0),
    ("node", 0, "US Thyroid gland", None, 6),
]

specs = [
    ("icons/lucide-tag.svg", "Findings/Diagnoses", "WHAT was found", FINDINGS, [],
     ["layered over: finding models", "· ACR/RSNA CDEs"]),
    ("icons/healthicons-lungs.svg", "Anatomic Locations", "WHERE it is", ANATOMY, [],
     ["layered over: RadLex"]),
    ("icons/healthicons-xray.svg", "Exam Types", "HOW it was seen", EXAMS,
     ["each a LOINC/RSNA Playbook entry"], ["layered over: LOINC/RSNA", "Playbook"]),
]

# ---------------------------------------------------------------- layout
GAP_COL = 20
CUSHION = 8         # clear space between the longest row and the band's right edge
COL_W = 316         # 2*MARGIN + TREE_INDENT + widest row (255.9) + CUSHION
CONTENT_W = 3 * COL_W + 2 * GAP_COL
Y0 = 0

# The widest row sets the column width. A row must end inside the band
# above it, not merely inside the column, or it reads as an overflow --
# so assert that here rather than discovering it in the render.
_fits = COL_W - 2 * MARGIN - TREE_INDENT - CUSHION
_widest = max((row_width(*r), r[2]) for _i, _t, _g, rows, _n, _d in specs for r in rows)
assert _widest[0] <= _fits, f"row {_widest[1]!r} ({_widest[0]}) exceeds {_fits}"

REGION_H = max(column_group_h(rows, notes) for _i, _t, _g, rows, notes, _d in specs)
COL_H = TREE_TOP + REGION_H + TREE_BLOCK_GAP + BLOCK_H + PAD_BOTTOM
BLOCK_Y = COL_H - PAD_BOTTOM - BLOCK_H

for i, (ipath, title, tagline, rows, notes, desc_lines) in enumerate(specs):
    axis_column(i * (COL_W + GAP_COL), Y0, COL_W, REGION_H, ipath, title, tagline,
                rows, notes, desc_lines)

save("knowledge/drafts/three-axes.excalidraw")
print(f"figure {CONTENT_W}x{COL_H}  region {REGION_H}  widest row {_widest[1]!r} {_widest[0]}")
for _i, t, _g, rows, notes, _d in specs:
    print(f"  {t}: {n_rows(rows)} rows, row_h {fitted_row_h(rows, notes, REGION_H):.1f}")
