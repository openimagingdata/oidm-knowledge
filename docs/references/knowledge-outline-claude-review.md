# Claude review of the initial knowledge-node outline

Captured October 6, 2026, from the Claude agent in Herdr pane `wA:p5`. This is the full agent reply with terminal whitespace and table borders normalized. It reviewed the initial October 5 outline, before the owner's subsequent corrections and Applications additions. Its coded labels refer to that earlier outline. These are agent findings and proposals, not owner decisions, current implementation facts, or instructions to change the organization. Technical claims require source verification before use.

## Subsequent review and correction

Recorded at the October 14 restart checkpoint from the later review in the same conversation. This is a summary of Claude's later assessment, not a second verbatim transcript or owner approval.

Claude considered the restored hierarchy and the distinction between shared definitions and finding assertions sound. Its remaining suggestions concerned the Applications/Use Cases boundary, patient concepts needed by the proposed uses, content guidelines and identity/versioning, and repeated material across conceptual, SDK, and application documents.

Claude explicitly withdrew its earlier claim that Imaging Diagnostic Report was necessarily the IHE profile and encoded positive findings as FHIR Condition. It had relied on a single CDE repository note without checking the primary supplement. Do not use that earlier claim to determine the EFL/IDR relationship or FHIR mappings; both remain questions to investigate.

The owner's subsequent guidance governs the active outline: patient-concept development is unfinished work leading toward Imaging Persona; content guidelines evolve through community authoring; SDKs cover library capabilities; and actual implementation distinguishes Sample Applications, including demos and prototypes, from Use Cases. The green findings feature was an implemented vendor prototype demonstrated at RSNA, according to the owner. The owner also supplied the preliminary content-versioning concept and proposed a dedicated SDK node for longitudinal finding linking. These statements are preserved in [owner guidance](knowledge-organization-owner-guidance.md) and reflected in [the plan](../plans/implementation.md).

## Initial review reply

I reviewed the October 5 outline. I read docs/HANDOFF.md, the outline, project-direction.md, idea-coverage.md, the draft headings (not their bodies) and the CDE repo's IDR note.
I edited nothing and read no reviewer correspondence. Where I cite the owner, I give the date of the recorded statement; everything else is my proposal.

Top-line

1. The scope is mostly right, but some nodes are duplicated and some substantive ideas have no home. FC-02/FC-04, FC-12/FC-13/SDK-06–08 and DS-18–20/SDK-15–17 overlap. Several
inventoried ideas are missing (listed under each section).
2. The two-graph interconnection has no primary home. The owner put it at the centre of Data Structures: "most ESPECIALLY in the Observation layer, and how there are two graphs
and they work together" (Sept 22). The outline splits it between FC-01 and DS-01, and DS-01 is really about structures versus transport.
3. DS-07 pairs EFL with an external standard as if they were peers. The "Imaging Diagnostic Report" is the IHE IDR Phase II supplement (public-comment draft, 2026-03-04, per
ACR-RSNA-CDEs/notes/ihe-idr-extract.md). It is a FHIR encoding profile, not an OIDM structure, so it belongs in the mapping account (DS-19). That note also shows IDR encodes
positive findings as FHIR Condition and negatives as Observation. That bears directly on DS-17/DS-18.

Foundation Context

ID: FC-02 / FC-04
Finding: Near-duplicates: both cover the "kinds of subject" distinction. Subtype hierarchy is already in FC-06 (taxonomy edges).
Recommendation: Merge into FC-02 using the schema's node classes (FindingClass, Diagnosis, Grouping; AssessmentScheme membership left open) and the owner's "defines, not is-a"
rule (Sept 30). Ask the owner what their "Taxonomy" heading meant. If it meant content organization, repurpose FC-04 to the MGB exam-oriented sub-taxonomies (Sem-B7). The owner
called those "the immediate direction for all of the content" (Sept 21), and they currently have no node.
ID: gap
Finding: No node for moving from document-oriented definitions to the graph. The owner called this urgent (Sept 22) and gave the direction "likely using RDF/OWL… more ergonomic
data structures… for SDKs and via an API" (Sept 30).
Recommendation: New FC node: schema evolution and migration. It separates current from intended and covers the OIFM document format, the findingmodel metadata rewrite
(feature/metadata-cleanup) and the RDF/OWL direction. FC-03 stays the schema overview.
ID: gap
Finding: No node for the content build-out, which the owner placed explicitly in Foundation Context (Sept 22). This covers the Gamuts corpus and its replacement, content
pipelines, and the build-out ideas Sem-B2, B3, B4 and F7.
Recommendation: New FC node: content build-out and coverage.
ID: gap
Finding: Content guidelines have no home. The "Guideline / check / human decision" connection points at nothing. The guidelines exist in inventoried ideas Sem-A2, A3, A7 and A8,
plus Groupings "usually used in the negative" (Sept 30).
Recommendation: New FC node: definition content guidelines. SDK-07 checks against it.
ID: gap
Finding: No node for identity, versioning and lifecycle. Identifiers carry provenance (Sem-B1); there are OIFM and RDE IDs; cross-links persist after promotion (owner, Sept
27–29). SDK-02 names "definition versions" with no FC source. Patient assertions need to say which definition version they reference.
Recommendation: Split this out of FC-05 as its own node. FC-11 links to it for cross-collection identity.
ID: FC-05
Finding: Should carry the metadata-rewrite fields (body region, subspecialty, etiology, time course, age, sex, modalities), plus Sem-C1 and C2.
Recommendation: Record as an open question, not a decision. The owner said time course and etiology "may need to be a property of the edge connecting it to a diagnosis" (Sept
30).
That conflicts with the node-level fields on the findingmodel branch.
ID: FC-06
Finding: Missing "Deriving the differential." It is a heading on the owner-reviewed relationships draft, and the owner said the distinction "enable[s] inference" (Sept 30). Edge
properties should name the specificity scale (pathognomonic / highly suggestive / suggestive).
Recommendation: Add inference as a section of FC-06, plus an SDK capability (see SDK-03).
ID: FC-08
Finding: Sem-F6 ("measurement, method, and interpretation are three things") is missing. Measurements are typed by kind of quantity, not explicit units (owner, Sept 29); the
"permissible units" wording should follow that.
Recommendation: Add both.
ID: FC-12 / FC-13
Finding: One idea in three homes: FC-12, FC-13 and SDK-06/07/08. FC-13 has no substance apart from Forge's requirements.
Recommendation: Refocus FC-12 on the authoring and review workflow: triage, three-tier review, human review as the only authority (Sem-B4, B5, C4, C5), and OIFM-to-CDE promotion.

Fold FC-13's requirements into FC-12. Forge itself goes to Sample Applications.
ID: FC-16
Finding: Scoped to anatomy only, but external codes also appear in FC-05 and FC-22. Mapping semantics (Sem-C3 "index codes must be exact", Sem-F2 terminology roles) apply across
all three axes.
Recommendation: Generalize: external terminologies and mapping semantics for definitions, anatomy and exams, with anatomy detail as a section. This answers review question 2.
ID: FC-15
Finding: Sem-D7 ("missing is-a and structure-type layer") is the motivation for adding tissue type.
Recommendation: Cite it there.
ID: FC-20
Finding: The MGB sub-taxonomies are exam-oriented, so they link definitions to exam types.
Recommendation: Cross-link to FC-04 (if repurposed) or the content node.

Data Structures

ID: gap
Finding: The two-graph interconnection, plus worked patient-side examples. The owner's Sept 22 method item 6 assigns them: the CDE pyelonephritis report shows both graphs; IPL
example2 is patient-side only.
Recommendation: New DS node: patient graph and Foundation interconnection, using those worked examples. Narrow FC-01 to the Foundation side. Keep the owner's latest "pointers"
wording (Oct 5) alongside the Sept 24 "interconnection that attaches knowledge to facts."
ID: DS-02
Finding: Should present the related representations side by side: the CDE report graph, IPL Observation, and the OpenImagingDataModel lineage. These are "related representations…

never the same thing serialized" (Sept 22), and "no specification exists" (Sept 21). The IDR note also records that the CDE committee moved away from the word "observation"
because of FHIR overlap.
Recommendation: Keep the title "Assertions / Observations" but record that terminology collision.
ID: DS-03 / DS-04
Finding: Unclear boundary. Sem-A10 ("associated findings versus components") is the source distinction.
Recommendation: One sentence each: attribute sub-assertions have DataElement or Measurement subjects; components have FDe-subject child assertions. If no source separates them
further, merge into one "sub-assertions" node. Keep the owner's sub-assertion wording marked as proposed (review question 3).
ID: DS-03
Finding: Negatives and normality are missing: Sem-A4, Use-A10, A11, A23.
Recommendation: Name presence, absence, normality and Grouping negatives explicitly.
ID: gap
Finding: Recommendations and follow-up: Use-A18, the live-versus-closed axis, and outcome tracking (Use-B7).
Recommendation: New DS node: recommendations and follow-up, linked to DS-10, DS-11 and assessment assertions.
ID: gap
Finding: Patient assessment assertions (ASSESSED_BY, owner Sept 30) have no DS home, although review question 1 asks about them.
Recommendation: Make this a section of DS-06 rather than a node, unless sources support more.
ID: DS-06 / DS-09
Finding: Both own finding-to-impression links.
Recommendation: DS-09 owns section organization, DS-06 owns relation types; remove the duplicate.
ID: DS-07
Finding: See top-line 3. Use-A3 (faithful translation) and Use-A17 (sections beyond Findings unmodeled) belong here.
Recommendation: Retitle to Exam Finding List. Move IDR to DS-19 as an external alignment target.
ID: DS-11
Finding: Identity within one report (Use-A9: several observations of one finding) differs from identity across exams.
Recommendation: State both. Carry the three source status vocabularies side by side (Sept 21 rule).
ID: DS-12 / DS-16
Finding: The Persona is a single larger graph underpinned by Foundation Context, not data "alongside" it (owner, Sept 24). Use-A16 and Use-B8 (the reporting context object model)

are its source. FHIRcast synchronizes context; it does not carry data.
Recommendation: Link DS-12 to the context object model. Fold DS-16 into DS-12, or into the interoperability family under DS-17, as a qualified section.
ID: DS-13
Finding: Probably thin.
Recommendation: Make it a section of DS-12 unless sources support a node.
ID: DS-15
Finding: Overlaps DS-14. Its distinctive content is radiology–pathology correlation (Use-B7).
Recommendation: Retitle Pathology correlation and patient diagnoses. Keep its rule that likely associations are not patient facts.
ID: DS-17
Finding: Records only FHIR. The owner's Sept 21 decision names FHIR and DICOM as transport, and DICOM SR is an input in DS-05.
Recommendation: Record DICOM SR as a known transport outside the current scope.
ID: DS-17 / DS-18
Finding: Fidelity and identity questions to record (review question 6).
Recommendation: (a) Positive findings: Observation or IDR's Condition? (b) Sub-assertions as component versus hasMember/derivedFrom. (c) Version-pinned definition references
(canonical URL with version). (d) Provenance as the Provenance resource versus inline. (e) Longitudinal identity: FHIR has no native "same finding over time." (f) Which side is
authoritative after a round trip; extensions versus declared loss. Prior art to cite: FHIRSamples (DiagnosticReport with chained CDE-coded Observations) and the IPL-MVP FHIR
persistence note. The mapping is documented but implemented nowhere (Sept 20–22 snapshot); say so.

SDKs (all assistant proposals)

│ ID │ Finding │ Recommendation │
│ │ Omits the deck's framing: determinative tools versus generative agents, and "resolve, │ │
│ SDK-01 │ don't reinvent." Also the owner's statement that SDKs help "AUTHOR and MAINTAIN" │ Make the determinative/generative split the map's organizing axis. │
│ │ Foundation Context (Sept 30). │ │
│ SDK-02 │ Runtime crosswalk from external codes to FDes is not explicit (molu is the real │ Add both. │
│ │ implementation). Sem-C8 (three retrieval modes) belongs here. │ │
│ SDK-03 │ Inference is missing: deriving a differential, expected findings for a diagnosis, │ Add to SDK-03, or make it a new capability. │
│ │ Grouping negatives. │ │
│ │ Foundation coding is shared by SDK-08, SDK-09 and SDK-12. Use-B3 ("coding is an │ New SDK node: Foundation coding of extracted text (definition and │
│ gap │ independent job, decoupled from extraction") and Use-A24 (generalizing allowed, │ anatomic-location assignment, per the IPL assignment rules). SDK-09 │
│ │ specializing not) support a separate capability. │ keeps extraction. │
│ gap │ Evaluation of extraction is missing: Use-B4 (honesty-first evaluation) and Use-A26 │ New SDK node, or a section of SDK-09. │
│ │ (taxonomy of extraction failures). │ │
│ SDK-09 / │ PHI and local-only operation (Use-B10, IPL local-model plans) are missing; this is │ Add to both. │
│ SDK-12 │ critical for wider clinical history. │ │
│ SDK-06 / │ The boundary should follow the determinative/generative split: mechanical validation │ Restate both on that line. │
│ SDK-07 │ versus LLM guideline checks against the new content-guidelines FC node. │ │
│ │ Three stubs, each just "implements DS-1x." Nothing is implemented. The owner asked for │ Collapse into one SDK node: bidirectional FHIR conversion, with │
│ SDK-15–17 │ one philosophy account plus per-structure mappings, and DS-17–20 already provide them. │ per-structure sections. Split later only when implementations │
│ │ │ diverge. │
│ SDK-14 │ Matches the owner's cholecystectomy example. The "seek missing information" question is │ No change. Verify code systems (ICD-10-CM / CPT / SNOMED │
│ │ correctly left open. │ procedures) at source, as the outline says. │

Separating knowledge nodes, clinical objects and pages

- Clinical objects: I found no per-object nodes. Per-type accounts (FC-07, FC-08), example tables (FC-10) and relationship tables in FC-06 keep the separation.
- Pages: FC-03, FC-06, FC-11, FC-14 and FC-17 roughly track the crafted drafts (next-generation-schema, relationships, finding-models-and-cdes, anatomic-locations, exam-types).
That is acceptable if each node is a fuller account the page distills, not a mirror of the page.
- Using the drafts: Use them only as evidence of owner-agreed wording and as a check for missing ideas (for example "Deriving the differential"). Don't edit them or adopt their
section structure as the node structure.

Owner decisions this surfaces (one at a time)

1. What the "Taxonomy" heading meant: subject-kind distinctions, or the exam-oriented content taxonomies.
2. Whether time course and etiology are edge properties or definition fields.
3. Whether EFL and IDR is an alignment (my reading of the IDR note) or something the owner intends differently.
