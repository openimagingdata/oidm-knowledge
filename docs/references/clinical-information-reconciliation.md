# Clinical-information reconciliation for Imaging Persona

Researched October 6, 2026, at the owner's request. This is a focused search of primary sources, not a systematic review. It records research findings and proposed implications for the knowledge outline, not an agreed Imaging Persona schema.

The owner distinguishes the broader clinical-informatics problem from the project's preliminary work identifying observations of the same imaging finding across a patient's imaging history. The latter has a proposed dedicated SDK node in [the implementation outline](../plans/implementation.md).

## Problems to distinguish

Our interpretation of the sources is that three questions need separate treatment:

- Do records describe the same clinical event or condition?
- Does a difference represent clinical change, differing specificity, disagreement, or a correction?
- Which information should an application use now, and on what evidence or review decision?

The sources below offer representation elements, reconciliation considerations, and experimental methods. They do not establish an automatic solution applicable to all clinical information.

## Primary sources

### IHE reconciliation profile

[Reconciliation of Clinical Content and Care Providers, revision 3.2](https://www.ihe.net/uploadedFiles/Documents/PCC/IHE_PCC_Suppl_RECON_Rev3.2_TI_2016-11-11.pdf), November 11, 2016. The [current IHE PCC listing](https://profiles.ihe.net/PCC/index.html) still identifies this revision under Trial Implementation, rather than Final Text.

Section X.4.2 considers original identifiers, coded concepts, timing, anatomy, and information sources when reconciling records. Timing can distinguish recurrent events while repeated mentions of a chronic condition or past surgery may describe one instance. Differences in anatomic specificity can also describe the same condition. The profile considers overlapping, conflicting, and superseded information and records who reconciled information, when, and which sources were considered.

Its examples of FHIR structures reflect the profile's older FHIR context. They are not current R5 mappings to copy into this project.

### FHIR representation elements

[FHIR R5 Condition](https://hl7.org/fhir/R5/condition.html), published March 26, 2023, distinguishes clinical status from verification status. Resolution of a disease, refutation of a diagnosis, and an erroneous entry have different meanings. Onset, abatement, recorded date, and evidence are useful elements to examine. This does not prescribe adjudication of conflicting records.

[FHIR R5 Provenance](https://hl7.org/fhir/R5/provenance.html), published March 26, 2023, records activities and agents involved in producing or revising resources and the sources used. References can identify particular resource versions. Recording the origin of information supports investigation of its reliability; it does not itself determine clinical truth.

These are version-specific references for research, not a decision that the project will use R5 exclusively.

### Structured clinical-document consolidation

[Hosseini and colleagues, 2017 author manuscript](https://scholarworks.indianapolis.iu.edu/server/api/core/bitstreams/a9045c3b-3cf5-40c9-80ae-5f76012f11a2/content), also indexed in [PubMed](https://pubmed.ncbi.nlm.nih.gov/28903073/).

The study tested consolidation of problems, medications, and allergies from Continuity of Care Documents. Missing semantic codes and differences between coded and narrative information hindered matching. The authors distinguished conflict detection from the harder problem of conflict resolution. This is evidence from a particular consolidation system, not a general performance guarantee.

### Temporal reasoning with LLMs

[TIMER](https://www.nature.com/articles/s41746-025-01965-9), September 26, 2025, peer-reviewed research.

The study examines LLM reasoning across longitudinal records and reports improvements with time-aware instruction tuning. Its findings include recency bias in the evaluated models. It motivates explicit evaluation of temporal interpretation, rather than assuming that an extracted statement has been assigned the correct clinical time. It does not establish a completed clinical-reconciliation method.

### Narrative and structured-data consistency

[Towards Error-Free EHRs: Reasoning-Intensive Consistency Verification Between Clinical Notes and Structured Tables in Electronic Health Records](https://arxiv.org/html/2605.26463v1), May 26, 2026, preprint describing EHR-Inspector.

The method extracts entities and temporal context, searches structured tables, and checks narrative consistency. The analysis distinguishes conflicting values from missing supporting records, although its benchmark uses a binary consistency label. Its small note sample, preprocessed MIMIC data, and use of LLM-based evaluation limit conclusions about general clinical use. Its labels are not an Imaging Persona truth model.

## Proposed implications for this project

Keep broader reconciliation linked to Imaging Persona's node about information to retrieve and how to represent it. Keep the specific longitudinal finding-linking capability under SDKs, connected to the Imaging Problem List's representation of the resulting history.

Questions to develop with the community include how to retain source statements and evidence, proposed links, corrections, disagreements, and reviewed conclusions. Missing documentation needs to remain distinguishable from an explicit negative statement. The representation of those distinctions is still open.

Evaluate extraction, linking, temporal interpretation, and conflict handling separately. Successful extraction of a statement does not establish that its identity, timing, or relationship to conflicting information is correct.

The distinctions and implications above are agent interpretations for discussion. The owner's decisions remain in [the owner-guidance reference](knowledge-organization-owner-guidance.md).
