#!/usr/bin/env python3
"""Build the repository data-flow map: one row per theme, each a short
left-to-right chain of at most three boxes, stacked top to bottom so every
cross-row flow is a short arrow to an ADJACENT row only -- rows are ordered
(CDE staging, finding models, applications, anatomy, terminology lookup) so
that CDE staging and applications both sit directly next to finding models,
and applications sits directly next to anatomy. Two edges that would have to
skip a row (CDEStaging -> RadElement, med-ontology-lookup -> findingmodel)
are dropped as captions instead -- both are already stated in the page prose.
Output: knowledge/repositories/repository-map.excalidraw"""
from excalib import PRIMARY, SECONDARY, TERTIARY, EXTERNAL, PLANNED, TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, arrow, save

W, H = 190, 80
GAP = 115                                   # wide enough that the longest horizontal-arrow label ("CDE-derived") fits centered above its arrow with room on each side
C1, C2, C3 = 0, W + GAP, 2 * (W + GAP)     # 0, 305, 610
ROW_GAP = 90
CONTENT_W = C3 + W                          # 800

row_names = ["cde_stage", "fm_pipeline", "apps", "anatomy", "terms"]
row_labels = ["CDE STAGING", "FINDING MODELS", "APPLICATIONS", "ANATOMY", "TERMINOLOGY LOOKUP"]
Y = {}
y = 40
for name, lbl in zip(row_names, row_labels):
    Y[name] = y
    els.append(text(f"hdr_{name}", C1, y - 24, lbl, size=14, color=SUBTITLE))
    y += H + ROW_GAP

# row 1: CDE staging (2 boxes; columns line up with row 2's RadElement/findingmodels)
box("cdesnap", C1, Y["cde_stage"], W, H, "common_data_elements\nRadElement snapshot", TERTIARY)
box("cdes", C2, Y["cde_stage"], W, H, "CDEStaging\n259 draft CDE\ndefinitions", TERTIARY)

# row 2: finding model pipeline
box("radelement", C1, Y["fm_pipeline"], W, H, "RadElement (ACR/RSNA)\nRDES and RDE codes", EXTERNAL)
box("fms", C2, Y["fm_pipeline"], W, H, "findingmodels\n2,382 finding models", TERTIARY)
box("fm", C3, Y["fm_pipeline"], W, H, "findingmodel\nOIFM format, index,\nCLIs, MCP", SECONDARY)
arrow("f1", "radelement", "right", "fms", "left", "CDE-derived")
arrow("f2", "fms", "right", "fm", "left", "definitions")

# row1 <-> row2: both adjacent, straight verticals (same columns).
# cdesnap/cdes sit ABOVE radelement/fms on the page, so the "ascending" arrow
# (radelement -> cdesnap) binds radelement's top to cdesnap's bottom, and the
# "descending" one (cdes -> fms) binds cdes's bottom to fms's top.
arrow("f3", "radelement", "top", "cdesnap", "bottom", "snapshot")
arrow("f4", "cdes", "bottom", "fms", "top", "content batches")

# row 3: applications (fed from row 2 above and row 4 below -- both adjacent)
box("ipl", C1, Y["apps"], W, H, "imaging-problem-list\nuses models +\nlocations", PRIMARY)
box("site", C2, Y["apps"], W, H, "finding-models-site\ncorpus catalog", PRIMARY)
box("forge", C3, Y["apps"], W, H, "Finding Model Forge\nfmf.oidm.org", PRIMARY)
arrow("f5", "fms", "bottom", "site", "top", "git submodule")   # row2->row3, same column, straight vertical
arrow("f6", "fm", "bottom", "forge", "top", "engine")          # row2->row3, same column, straight vertical
# C1 has no arrow through this gap (imaging-problem-list is fed from row 4
# below, not row 2 above), so it is clear for this caption
els.append(text("cdes_note", C1, Y["fm_pipeline"] + H + 12, "(CDEStaging also has an\ninformal path to RadElement)", size=13, color=BODY, w=W))

# row 4: anatomy
box("radlex", C1, Y["anatomy"], W, H, "RadLex (RSNA)\nRID codes", EXTERNAL)
box("alorg", C2, Y["anatomy"], W, H, "anatomiclocations.org\n+ BodyPartIndex", TERTIARY)
box("alpkg", C3, Y["anatomy"], W, H, "anatomic-locations pkg\ninside findingmodel", SECONDARY)
arrow("f7", "radlex", "right", "alorg", "left", "subset")
arrow("f8", "alorg", "right", "alpkg", "left", "lineage", dashed=True)

# row3 <-> row4: adjacent rows -- one clean line, no bends, even though it
# spans the row's full width (alpkg is the rightmost box in row 4, ipl the
# leftmost in row 3, to keep each row's own left-to-right reading intact)
arrow("f9", "alpkg", "top", "ipl", "bottom", "used by", s_frac=0.5, d_frac=0.5)

# row 5: terminology lookup
box("others", C1, Y["terms"], W, H, "SNOMED CT, FMA,\nLOINC, UMLS", EXTERNAL)
box("molu", C2, Y["terms"], W, H, "med-ontology-lookup\nmolu", SECONDARY)
box("mvp", C3, Y["terms"], W, H, "IPL-MVP-\nExtractionAndLabeling\n(superseded)", PLANNED, dashed=True)
arrow("f10", "others", "right", "molu", "left", "lookups")
els.append(text("molu_note", C2, Y["terms"] + H + 14, "molu also enriches findingmodel\nmetadata by ontology search (see text)", size=13, color=BODY))

# ---------------------------------------------------------------- legend / footnote
Y_END = Y["terms"] + H + 60
els.append(text("legend", 0, Y_END, "Orange: external terminology.  Light blue: content repository.\nMid blue: library.  Dark blue: application.  Dashed: lineage or superseded.", size=13, color=BODY))

save("knowledge/repositories/repository-map.excalidraw")
