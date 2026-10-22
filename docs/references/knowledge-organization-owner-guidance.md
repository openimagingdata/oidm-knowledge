# Owner guidance for the knowledge graph organization

Recorded October 6, 2026, from the current organizing conversation. The quotations below preserve the owner's words, including abbreviations and spelling. They are distinct from the assistant's additions in the implementation plan and from Claude's review proposals. The working outline is in [the implementation plan](../plans/implementation.md).

## Original outline for the first two sections

The owner supplied this outline. SDKs, Applications, and Use Cases were headings to develop collaboratively.

```text
FOUNDATION CONTEXT
* Introduction: Interconnected Knowledge (as separate from patient-specific assertions)
* Assertion Subjects/Finding Definitions (including diagnoses, etc., abbrev FDe)
  - Overview of the knowledge graph schema
    - Taxonomy of "assertion subjects": findings, diagnoses, assessments, etc (abbrev FDe)
    - Properties of FDe
    - Relationships BETWEEN FDes
    - Categorical attributes of FDes: Data Elements
    - Measurements of FDEs
  - Examples of some actual graphs
  - OIFM and CDE repositories (and relationship)
  - Using LLMs to drive creation of the system
  - Proposed authoring tool (evolution of FindingModelForge)
* Anatomy
  - Anatomic locations: curation, first additions ("contained by", sex-specific, laterality, etc.)
  - Incorporation into RadLex: including proposed added metadata such as tissue type
  - Relationships to other ontologies (SNOMED CT, TA2, FMA, LOINC)
* Exam types
  - RadLex/LOINC Playbook
  - Exam families (see ../exam-types)
* Overall integration
  - FDe definitions: "anatomic scope" (relationship to anatomy)
  - FDe definitions: exam types
  - Anatomic locations <-> exam types (and link to a proposed application: smarter relevant priors)
  - FDes associated with non-imaging diagnoses (and procedures, such as surgeries?)

DATA STRUCTURES
* Assertions/Observations
  - Overview, focusing on this is an application-layer data structure
  - What's contained: POINTERS to FDe, to an anatomic location
  - Attributes: pointers to sub-assertions with DataElement and Measurement subjects
  - Sub-components
  - FHIR representation: Objservation, components, connections
  - Provenance: AI generated, technologist/modality generated (DICOM SR?), LLM-extracted from report text, LLM-generated from radiologist interaction, radiologist review of AI-based tools
* "Exam Finding List" / Imaging Diagnostic Report
  - Exam information
    - Pointer to exam type information
    - Maybe information on protocol, etc.
    - Other exam performance information: pointers to DICOM data?
  - Collection of Assertions/Observations (noting sections: Findings, Impression)
  - More relationships between assertions: findings/diagnoses, sub-components, associations, finding -> impression
  - FHIR Imaging Diagnostic Report represetation
* Imaging Problem List / Patient Imaging History
  - Finding-based organization
  - Basic applications, use as context information
  - Longitudinal tracking
  - FHIR representation--?
* Imaging persona
  - Incorporates IPL
  - Exam-planning information (MRI safety, allergies, body habitus)
  - Clinical history extraction (e.g., imaging-relavant oncology history, operative notes)
  - Pathology results -> diagnoses, interconnected to IPL elements
  - Other non-imaging diagnoses POSSIBLY associated with imaging findings
  - Availability via FHIRCast

SDKs
...

APPLICATIONS
...

USE CASES
...
```

## SDK additions and clarifications

> For patient data structures KEY is using LLM agents to do automated extraction of report text to data structures (see imaging-problem-list extraction work)
> Also for the data structures, DESPERATELY need to be able to go back and forth from FHIR representations.

> The patient data structures needs to ahve SOMETHING about the larger patient history information.
> The "imaging Persona" concept--the patient facts RELEVANT TO IMAGING organized in a standard way
> I think FHIR converstion is probably its own OVERALL page on the philosophy, and then SPECIFICs on the Observation object itself, the EFL, and the IPL.

In response to including LLM extraction from clinical notes, operative reports, and pathology:

> Yes, INCLUDING the idea that the FOUNDATION CONTEXT can have appropriate information about LIKELY associates (e.g., history of cholecystictomy [LOINC, CPT] code and diagnosis [ICD, LOINC, SNOMED CT], and the finding and diagnoses definitions in our system and how to access all of that IN THE CONTEXT of the patient)

> For authoring/maintaining, also mention LLM-assistance for enforcing guidelines for this content
> Also mention an LLM-based approach to extract proposed FDes and associated information from corpuses (corpi?) of radiology reports
> Also include explicit tools on connections to external ontologies (helps in authoring)

## Knowledge nodes, precision, and hierarchy

> Also, I'm concerned here that we're not considering this in the context of, "What are the ACTUAL KNOWLEDGE GRAPH NODES we're creating here?"

On the subject of a measurement:

> It's not an assertion about a PATIENT. There's nothing "8 mm" about a PATIENT. It's about a FINDING!

On coded references and unnecessary detail:

> Oh, that shorthand with those references like this is UNACCEPTABLE. ENGLISH, please--comprehensible.

> Why all that noise about FHIR in the Measurement entry?

> You have a page called "Incorporation into RadLex"?! Um, maybe there's some context missing?!

> And you've flattened the structure I provided you! What happened to the actual levels of the outline? No wonder I can't understand the context of these things--they were part of an outline layer that you just THREW AWAY!

## Applications additions

> Also need an explicit anatomy browsing site, and probably in interface for looking at our view of the exams (exam families, etc) with the linked anatomy.
> For "reporting assistance", we can mention the "green findings" application (it's an older one--you can see some mention of it in one of the older Excalidraw boards). The basic idea was that there are a BUNCH of fixed findings in radiology reports, and every draft of a report should START with those things we KNOW are going to be in the report because they were in a prior report. (Which is NOT everyhting that was in the last report, it's an interesting issue!) But there is a DEFINITE subset of findings that will ALWAYS carry forward.
> But we should get into the idea as well of "object-oriented reporting" and include the idea of the objects being created from within the PACS imaging viewing interface.

> I'd also like to get into applications around outcome tracking.

## Patient concepts, community development, and implemented examples

> What do YOU think is actually missing in terms of "patient concepts"? Right now, that work has only been done at a high, fairly imprecise level. Figuring out the imaging-relevant patient concepts and data structures is the first step in the thread of work that leads to defining the Imaging Persona.

> "Content guidelines" are, again, something that the community will continue to develop over time. We have some IDEAS about these currently, which you have access to, but these are EXPECTED to be part of iterating on the ongoing content creation process.

> I don't understand what "definitions explain the concepts" would actually look like. I do agree that we need to separate out the underlying LIBRARY code (SDK) from APPLICATIONS (Applications or Use Cases).

> I think the "actually implemented" is the right dividing line between Use Case and Sample Application, but even simple demos count as Sample Applcations. And the whole "green findings" thing was an actual prototype feature implemented by one of the reporting software vendors and demonstrated at RSNA.

> Yes, there's an node in the Imaging Persona area about the pieces of information we're going to pull and how we're going to represent them there specifically.
>
> In the introduction to data structures in general, we can make the point that one of the important threads of work is the ongoing definition of these data structures by the community, especially by those implementing solutions using these ideas who can ground their contributions in real use.

## Versioning and longitudinal finding linking

> 1. THere needs to be a versioning scheme for managing content updates, likely deprecation with pointers to updated or replacing nodes. And we can also have the idea of pointers referring to specific versions of the definitions. These ideas need to be further fleshed out, but that's the concept.
> 2. In terms of reconciling clinical information, this is clearly a significant question in clinical informatics. (In fact, it would be good to dispatch a research subagent to do some lookup on the current state of it.) We've done some preliminary work SPECIFICALLY on the issue of identifying observations of imaging findings across an imaging history, and making the appropriate connections. THAT SPECIFIC ISSUE of longitudinal tracking of findings across time should probably be its own node, probably in SDK, don't you think?

## Fresh reconstruction and temporary archive

> I worry that if we take an edit-in-place approach here, we'll end up anchored on existing garbage rather then clean thinking.

> How about just "archive/knowledge" and build INTO the plan that we're going to nuke it when we've gotten the pieces that matter out of it?

The implementation plan records the fresh-writing method and required final archive deletion. It also distinguishes the separately developed outward-facing pages under `site/` from the internal graph.
