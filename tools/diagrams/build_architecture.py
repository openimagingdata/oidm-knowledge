#!/usr/bin/env python3
"""Build the OIDM architecture diagram (three layers joined by identifiers).
Three adjacent stacked bands (applications, data structures, semantic
foundation); Imaging Persona and CDEs-at-RadElement are compact second rows
within their own band (persona under Imaging Problem List at column 3, CDEs
under Finding models at column 1) rather than a separate trailing section,
with captions beside them instead of incoming arrows -- since neither sits at
column 1/2, they never block the foundation->data join arrows, which stay in
columns 1-2. Exam types -> Exam Finding List is also a caption, not an arrow,
to remove the one join that had no clean column-aligned path. Title/subtitle
and the "Also:" applications note are left for the page text.
Output: knowledge/overview/architecture.excalidraw; render with render_excalidraw.py."""
from excalib import PRIMARY, SECONDARY, TERTIARY, EXTERNAL, PLANNED, TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, arrow, hline, save

# ---------------------------------------------------------------- layout
# Box labels are hand-wrapped (Excalidraw does not auto-wrap bound text) so
# no line exceeds ~21 chars; that lets boxes stay narrow at 900px width.
W, GAP = 190, 26                                        # box width, horizontal gap between boxes in a row
C1 = 80                                                 # left gutter (80px) -- wide clearance for the Forge -> Finding models line and the band labels, which both start at C1
C2 = C1 + W + GAP                                       # 296
C3 = C2 + W + GAP                                       # 512
FORGE_X = 0                                             # off the C1 grid so its arrow can drop straight down the gutter, clear of Observation
CONTENT_W = C3 + W                                      # 702

H_APP, H, H_EXT = 100, 80, 100                          # row heights: 4-line boxes (app row, CDE row) need more height than 3-line boxes
ROW_GAP = 90                                            # band-to-band vertical gap
ROW_GAP2 = 60                                           # row1->row2 gap within a band (no arrow crosses it, so it can be tighter)
LABEL_BUF = 85                                          # extra clearance above the data-structures row so "per exam"/"per patient" have room above the boxes, not on them

Y_APP = 40
Y_DATA_HDR = Y_APP + H_APP + ROW_GAP                    # where the divider + "DATA STRUCTURES" label sit
Y_DATA = Y_DATA_HDR + LABEL_BUF                         # boxes start lower than usual, leaving that extra strip clear
Y_DATA2 = Y_DATA + H + ROW_GAP2                          # Imaging Persona row (column 3 only)
Y_FOUND_HDR = Y_DATA2 + H + ROW_GAP
Y_FOUND = Y_FOUND_HDR + 24
Y_FOUND2 = Y_FOUND + H + ROW_GAP2                        # CDEs row (column 1 only)

# ---------------------------------------------------------------- applications
els.append(text("band_app", C1, Y_APP - 24, "APPLICATIONS", size=14, color=SUBTITLE))
box("forge", FORGE_X, Y_APP, W, H_APP, "Finding Model Forge\nauthoring wizard\nfmf.oidm.org", SECONDARY)
box("extract", C2, Y_APP, W, H_APP, "Report extraction\nplatform\nLLM extraction\nand coding (dev)", SECONDARY)
box("viewer", C3, Y_APP, W, H_APP, "Imaging Problem\nList viewer\nimaging-problem-\nlist.pages.dev", SECONDARY)

# ---------------------------------------------------------------- data structures (adjacent to applications)
hline("div1", 0, Y_DATA_HDR - 6, CONTENT_W)
els.append(text("band_data", C1, Y_DATA_HDR, "DATA STRUCTURES", size=14, color=SUBTITLE))
box("obs", C1, Y_DATA, W, H, "Observation\nfinding + location\n+ attributes", PRIMARY)
box("efl", C2, Y_DATA, W, H, "Exam Finding List\nall observations\nof one exam", PRIMARY)
box("ipl", C3, Y_DATA, W, H, "Imaging Problem List\none patient, grouped\nby finding", PRIMARY)
# labels sit in the LABEL_BUF strip above the boxes, clear of both the band
# label above and the box tops below (checked: label bottom edge stays ~25px
# above the box top, well clear of the rounded corners)
arrow("a_obs_efl", "obs", "right", "efl", "left", "per exam", label_dy=-88)
arrow("a_efl_ipl", "efl", "right", "ipl", "left", "per patient", label_dy=-88)

# applications -> data structures: both adjacent rows, short vertical arrows.
# These lines got taller once LABEL_BUF pushed the data-structures row down,
# so the labels need more upward offset to clear the div1 divider below them.
arrow("a_extract_efl", "extract", "bottom", "efl", "top", "extracts from\nreports", label_dy=-50)
arrow("a_ipl_viewer", "ipl", "top", "viewer", "bottom", "renders", label_dy=-32)

# Imaging Persona: second data-structures row, under Imaging Problem List
# (column 3) so it never sits over columns 1-2, where the foundation->data
# joins run -- caption to its left instead of an incoming arrow.
box("persona", C3, Y_DATA2, W, H, "Imaging Persona\nplus clinical\ncontext (concept)", PLANNED, dashed=True)
# caption BELOW persona, not beside: column 3 is clear all the way down, but
# columns 1-2 at this row height are the foundation->data join corridor
els.append(text("persona_note", C3, Y_DATA2 + H + 14, "goal: extends the Imaging\nProblem List with context", size=13, color=PLANNED[2]))

# ---------------------------------------------------------------- semantic foundation (adjacent to data structures)
hline("div2", 0, Y_FOUND_HDR - 6, CONTENT_W)
els.append(text("band_found", C1, Y_FOUND_HDR, "SEMANTIC FOUNDATION", size=14, color=SUBTITLE))
box("fm", C1, Y_FOUND, W, H, "Finding models\nOIFM_ / OIFMA_\ncodes", TERTIARY)
box("al", C2, Y_FOUND, W, H, "Anatomic locations\nRadLex RID codes", TERTIARY)
box("et", C3, Y_FOUND, W, H, "Exam types\nLOINC / Playbook\n(planned)", PLANNED, dashed=True)
els.append(text("et_note", C3, Y_FOUND + H + 14, "supplies the LOINC\nexam code on the\nExam Finding List", size=13, color=PLANNED[2]))

# foundation -> data: both adjacent rows, so every join is a short, direct
# line -- straight vertical where columns line up, a short one-column
# diagonal where two foundation boxes both feed Observation. Labels sit to
# the RIGHT of their line (away from the left-gutter "authors" arrow).
# fm->obs binds at 0.92 across the box (not centered): centered, this line
# would run at column 1's midpoint, straight through the "SEMANTIC
# FOUNDATION" label text above it (the label is ~162px wide, wider than half
# the 190px box) -- shifted right, it clears the label with room to spare.
arrow("a_fm_obs", "fm", "top", "obs", "bottom", "OIFM and\nOIFMA codes", s_frac=0.92, d_frac=0.92, label_dx=-70, label_dy=-40)
arrow("a_al_obs", "al", "top", "obs", "bottom", "RID", d_frac=0.8, label_dx=44, label_dy=-40)

# Forge (applications) authors finding models (semantic foundation), two
# rows down -- routed through the left gutter (x<C1=80), well clear of the
# band labels, which start at C1, and of Observation, which starts at C1 too.
arrow("a_forge_fm", "forge", "bottom", "fm", "left", "authors", s_frac=0.1, d_frac=0.5,
      elbow="vertical-first", label_dx=-10, label_dy=20)

# CDEs at RadElement: second foundation row, under Finding models (column 1)
# -- caption to its right instead of an incoming arrow (a curved arrow here
# would cross the row above it; the relationship is a two-way "graduates
# to / seeds" one anyway, better said in words).
box("cde", C1, Y_FOUND2, W, H_EXT, "ACR/RSNA CDEs at\nRadElement\nRDES / RDE codes\n(allied project)", EXTERNAL)
els.append(text("cde_note", C2, Y_FOUND2 + 18, "finding models graduate to CDEs;\nCDE definitions seed finding models", size=13, color=EXTERNAL[2]))

# ---------------------------------------------------------------- footnotes
Y_NOTE = Y_FOUND2 + H_EXT + 40
els.append(text("terms", 0, Y_NOTE, "Terminologies underneath: RadLex, SNOMED CT, FMA, UMLS, MeSH, LOINC and the RSNA\nRadiology Playbook. Looked up through med-ontology-lookup.", size=13, color=BODY))

Y_LEGEND = Y_NOTE + 2 * 13 * 1.25 + 22
els.append(text("legend_t", 0, Y_LEGEND, "Legend", size=13, color=SUBTITLE))
for i, (lab, colors, dashed) in enumerate((("solid outline: exists today", ("#ffffff", "#1e3a5f", ""), False), ("dashed outline: documented or planned only", PLANNED, True), ("orange: allied external project", EXTERNAL, False))):
    ly = Y_LEGEND + 24 + i * 22
    r = base("rectangle", f"lg{i}", 0, ly, 18, 14, colors[1], colors[0], dashed=dashed, sw=1)
    r["roundness"] = {"type": 3}; r["boundElements"] = None
    els.append(r)
    els.append(text(f"lg{i}_t", 26, ly - 2, lab, size=13, color=BODY))

save("knowledge/overview/architecture.excalidraw")
