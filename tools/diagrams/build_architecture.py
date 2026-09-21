#!/usr/bin/env python3
"""Build the OIDM architecture diagram (three layers joined by identifiers).
Output: knowledge/overview/architecture.excalidraw; render with render_excalidraw.py."""
from excalib import PRIMARY, SECONDARY, TERTIARY, EXTERNAL, PLANNED, TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, arrow, hline, save

# ---------------------------------------------------------------- layout
W, H = 260, 74                      # box size
C1, C2, C3, C4 = 150, 500, 850, 1200  # columns, 90px gaps for arrow labels; left margin reserved for the Forge arrow
Y_APP, Y_DATA, Y_FOUND = 160, 440, 720

els.append(text("title", 60, 40, "Open Imaging Data Model: three layers joined by identifiers", size=26, color=TITLE))
els.append(text("subtitle", 60, 82, "Each layer depends on the one below it. Codes minted in the semantic foundation are what the data structures carry and the applications exchange.", size=14, color=BODY))

# band labels and dividers
for lbl, y in (("APPLICATIONS", Y_APP - 34), ("DATA STRUCTURES", Y_DATA - 34), ("SEMANTIC FOUNDATION", Y_FOUND - 34)):
    els.append(text("band_" + lbl.split()[0].lower(), C1, y, lbl, size=13, color=SUBTITLE))
hline("div1", 40, Y_DATA - 50, 1440)
hline("div2", 40, Y_FOUND - 50, 1440)

# applications
box("forge", 40, Y_APP, W, H, "Finding Model Forge\nauthoring wizard, fmf.oidm.org", SECONDARY)
box("extract", C2, Y_DATA - 280, W, H, "Report extraction platform\nLLM extraction and coding (dev)", SECONDARY)
box("viewer", C3, Y_APP, W, H, "Imaging Problem List viewer\nimaging-problem-list.pages.dev", SECONDARY)
els.append(text("apps_note", C4, Y_APP + 8, "Also: finding-models-site (catalog),\nmed-ontology-lookup (terminology lookup),\nOpen Imaging Reporting SDK (concept only)", size=12, color=BODY))

# data structures
box("obs", C1, Y_DATA, W, H, "Observation\nfinding + location + attributes", PRIMARY)
box("efl", C2, Y_DATA, W, H, "Exam Finding List\nall observations of one exam", PRIMARY)
box("ipl", C3, Y_DATA, W, H, "Imaging Problem List\none patient, grouped by finding", PRIMARY)
box("persona", C4, Y_DATA, W, H, "Imaging Persona\nplus clinical context (concept)", PLANNED, dashed=True)
arrow("a_obs_efl", "obs", "right", "efl", "left", "per exam")
arrow("a_efl_ipl", "efl", "right", "ipl", "left", "per patient")
arrow("a_ipl_persona", "ipl", "right", "persona", "left", "goal", dashed=True)

# semantic foundation
box("fm", C1, Y_FOUND, W, H, "Finding models\nOIFM_ / OIFMA_ codes", TERTIARY)
box("al", C2, Y_FOUND, W, H, "Anatomic locations\nRadLex RID codes", TERTIARY)
box("et", C3, Y_FOUND, W, H, "Exam types\nLOINC / Playbook (planned)", PLANNED, dashed=True)
box("cde", C4, Y_FOUND, W, H, "ACR/RSNA CDEs at RadElement\nRDES / RDE codes (allied project)", EXTERNAL)
els.append(text("terms", C1, Y_FOUND + H + 40, "Terminologies underneath: RadLex, SNOMED CT, FMA, UMLS, MeSH, LOINC and the RSNA Radiology Playbook. Looked up through med-ontology-lookup.", size=13, color=BODY))

# joins: foundation -> data
arrow("a_fm_obs", "fm", "top", "obs", "bottom", "OIFM and OIFMA codes", label_dx=90)
arrow("a_al_obs", "al", "top", "obs", "bottom", "RID", s_frac=0.5, d_frac=0.85, label_dx=30)
arrow("a_et_efl", "et", "top", "efl", "bottom", "LOINC exam code", s_frac=0.5, d_frac=0.85, dashed=True, label_dx=40)
arrow("a_cde_fm", "cde", "top", "fm", "top", None)  # placeholder, replaced below
els.pop()  # remove placeholder arrow element
find("cde")["boundElements"].pop(); find("fm")["boundElements"].pop()
# CDE <-> finding models: a curved dashed arrow along the bottom would cross; use a short labeled note instead
els.append(text("cde_note", C4, Y_FOUND + H + 12, "finding models graduate to CDEs; CDE definitions seed finding models", size=12, color=EXTERNAL[2]))

# applications -> data / foundation
arrow("a_forge_fm", "forge", "bottom", "fm", "left", "authors", s_frac=0.12, d_frac=0.5, elbow="vertical-first", label_dx=-4, label_dy=-14)
arrow("a_extract_efl", "extract", "bottom", "efl", "top", "extracts from reports")
arrow("a_ipl_viewer", "ipl", "top", "viewer", "bottom", "renders")

# legend
LX, LY = C4, Y_FOUND + H + 80
els.append(text("legend_t", LX, LY, "Legend", size=13, color=SUBTITLE))
for i, (lab, colors, dashed) in enumerate((("solid outline: exists today", ("#ffffff", "#1e3a5f", ""), False), ("dashed outline: documented or planned only", PLANNED, True), ("orange: allied external project", EXTERNAL, False))):
    r = base("rectangle", f"lg{i}", LX, LY + 24 + i * 24, 18, 14, colors[1], colors[0], dashed=dashed, sw=1)
    r["roundness"] = {"type": 3}; r["boundElements"] = None
    els.append(r)
    els.append(text(f"lg{i}_t", LX + 26, LY + 22 + i * 24, lab, size=12, color=BODY))

save("knowledge/overview/architecture.excalidraw")
