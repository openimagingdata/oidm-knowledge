# Data structures

OIDM records findings as Observations, groups them into Exam Finding Lists and Imaging Problem Lists, and proposes adding clinical context through the Imaging Persona. Codes link these structures to the semantic foundation. Start with the hierarchy.

* [The data structure hierarchy](./hierarchy.md) - The four data structure levels, their identifiers, and implementation status.
* [Observation](./observation.md) - The atomic unit of OIDM: one finding, seen or explicitly excluded, on one exam, with its location and attribute values, as it exists today inside an Exam Finding List and in the extraction pipeline.
* [Exam Finding List](./exam-finding-list.md) - Findings from one exam, their fields and sources, and planned FHIR and IHE encodings.
* [Imaging Problem List](./imaging-problem-list.md) - A patient's observations grouped by finding, with fields, grouping rules, computed status, and planned FHIR encoding.
* [Imaging Persona](./imaging-persona.md) - The fourth level of the hierarchy, a stated goal with no artifact: the clinical context around a patient's Imaging Problem List, and the life-cycle uses the 2026 deck gives for it.
* [Anatomic location assignment rules](./anatomic-location-assignment-rules.md) - Migrated rules for assigning anatomy, laterality, and specificity to Exam Finding List observations.
* [Technical imaging findings](./technical-imaging-findings.md) - A migrated draft catalog of modality-specific findings and search terms for coding them.
* [FHIR mapping](./fhir-mapping.md) - Everything OIDM has documented about representing its data structures in FHIR, from the CDE-labeled Observation pattern of the lineage repositories to the current Exam Finding List and Imaging Problem List mappings, and the plain fact that no current code emits FHIR.
* [IHE IDR alignment](./ihe-idr-alignment.md) - What the IHE Imaging Diagnostic Report profile specifies for encoding findings as FHIR Observations, the deck's claim that the Exam Finding List connects to it, and the fact that no OIDM repository mentions it.
* [Sample data](./sample-data.md) - Synthetic exam and problem list samples, branch differences, viewer bundles, and generation scripts.
