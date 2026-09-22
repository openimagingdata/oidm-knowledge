# Drafts: the restructured pages

Staging area for the restructure agreed on 2026-09-22 (see `docs/plans/restructure-joint-notes.md`). Each pillar's anchor page is drafted here beside the current pages, which stay in place until cross-review. After review, each anchor becomes the `index.md` of its own pillar directory with child sections beside it, and this directory is removed.

Planned files, each session adding its link line when the file exists:

* [Introduction](./introduction.md) - What the Open Imaging Data Model is, the two contexts it distinguishes, the five pillars of the work, and how the project expects agreement to happen.
* [Foundation Context](./foundation-context.md) - The shared, non-patient-specific layer of definitions, relationships, and citations that imaging results point into, and the work of building its content.
* [Finding models and CDEs](./finding-models-and-cdes.md) - One content in two collections - the common graph being drafted for both, the OIFM and RadElement formats that hold it today, what the inclusive collection contains, and the authoring and review principles behind it.
* [Anatomic locations](./anatomic-locations.md) - The curated anatomic location index as a reference layer - identity, containment, part-of, laterality, synthetic terms, curation rules, the RadLex overlay, and the two dated implementations.
* [Exam types](./exam-types.md) - A stated goal with no artifact - preferred high-level exam entries over the LOINC/RSNA Radiology Playbook, the Playbook properties they would expose, and the anatomy coverage edges in the project lead's two dated phrasings.
* [Standards the foundation layers over](./standards.md) - Which existing standard each Foundation Context axis layers over, the role each terminology plays, the external citations the deck names, and search recall as the gate.
* [SDKs](./sdks.md) - The tools that wrap the data structures and resolve their codes into Foundation Context, plus the libraries that help author that context.
* [Data Structures](./data-structures.md) - Observations connect a patient's imaging results to shared definitions and to one another across reports and examinations.
* [Use Cases](./use-cases.md) - Proposed reporting assistance, longitudinal care, outcome tracking, and information products built on OIDM context and structures.
* [Sample Applications](./sample-applications.md) - Applications that author shared definitions, display imaging histories, extract and review findings, and demonstrate structured exchange.
