# Glossary

One term per file: a precise definition drawn from the sources, its synonyms and near-synonyms, its identifier form where it has one, where it is used, and any conflict between sources. Terms are listed alphabetically.

* [Anatomic location](./anatomic-location.md) - A curated anatomic concept identified by a RadLex identifier, placed in containment and part-of hierarchies with laterality variants and cross-ontology codes.
* [Anatomic scope](./anatomic-scope.md) - The eligible anatomical places, tissue types, or structure types for a definition, stated as a constraint rather than as a location.
* [AssessmentScheme](./assessment-scheme.md) - A definition of a standardized assessment system whose dimensions are ordinary data elements, distinct from the findings it assesses.
* [Attribute](./attribute.md) - A property a radiologist uses to characterize a finding, either a choice attribute with an enumerated value set or a numeric attribute with a range and unit.
* [Attribute value](./attribute-value.md) - One permissible option of a choice attribute, carrying its own dot-suffixed value code and optional ontology codes.
* [Body region](./body-region.md) - A coarse anatomic grouping such as thorax or abdomen, used to scope findings, to fall back when no structure is named, and to filter views.
* [CDE](./cde.md) - Common data element, the ACR and RSNA programme of governed, balloted definitions for radiology findings and their elements.
* [CDE element](./cde-element.md) - One property inside a published CDE set, carrying an RDE identifier and a value set, integer, or float definition.
* [CDE set](./cde-set.md) - A published RadElement definition of one finding, grouping the elements that characterize it under an RDES identifier.
* [CDE-labeled FHIR Observation](./cde-labeled-fhir-observation.md) - The project's founding representation of a finding, a FHIR Observation whose code and component codes are drawn from a published CDE set.
* [Change from prior](./change-from-prior.md) - The companion second attribute of a finding model, recording how the finding compares with the previous exam.
* [Coding](./coding.md) - Assigning finding identifiers and anatomic location identifiers to extracted findings, as a job distinct from extraction.
* [Contained by and part of](./contained-by-and-part-of.md) - The two orthogonal hierarchies over anatomic locations, one physical containment and one structural or functional membership.
* [Contributor](./contributor.md) - A person or organization credited on a finding model definition, recorded in a registry keyed by GitHub username or organization code.
* [DataElement](./data-element.md) - In the next-generation CDE vocabulary, a shared categorical descriptor whose permissible values may be ordered, reused across definitions through element bindings.
* [Element binding](./element-binding.md) - The relationship in the next-generation CDE vocabulary that connects a definition to a DataElement it uses, optionally restricting the values in that use.
* [Exam Finding List](./exam-finding-list.md) - All findings declared present or absent on one imaging exam, in one queryable structure keyed to the exam and the report.
* [Exam type](./exam-type.md) - The kind of imaging study an exam is, coded with LOINC today and intended to become a first-class OIDM artifact linking modality, technique, and included body parts.
* [Extraction](./extraction.md) - Deriving structured findings from narrative radiology report text with a language model, producing findings, presence, location, and attributes with verbatim quotes.
* [FHIR Condition](./fhir-condition.md) - The HL7 FHIR resource for a clinical condition, used in the documented Imaging Problem List mapping as the container for one finding type.
* [FHIR DiagnosticReport](./fhir-diagnostic-report.md) - The HL7 FHIR resource for a diagnostic report, used in OIDM as the interchange encoding of an Exam Finding List.
* [Finding model](./finding-model.md) - A machine-readable definition of one radiology finding, its synonyms, and the attributes a radiologist uses to characterize it.
* [Finding taxonomy](./finding-taxonomy.md) - One of the six MGB exam-oriented sub-taxonomies, per-modality hierarchies of finding names exported as CSV, that now set the content direction for the finding model corpus.
* [FindingClass](./finding-class.md) - The next-generation CDE vocabulary's node type for a finding definition, separated from diagnosis and carrying bindings to shared elements.
* [FMA](./fma.md) - The Foundational Model of Anatomy, used in OIDM as a cross-reference on anatomic locations and as the basis of the location type classification.
* [Gamuts](./gamuts.md) - The Radiology Gamuts Ontology, source of the largest single block of finding model definitions and of the GMTS organization code.
* [Imaging Diagnostic Report (IHE IDR)](./imaging-diagnostic-report.md) - The IHE Radiology profile that specifies how a diagnostic imaging report and its findings are encoded as FHIR resources.
* [Imaging Persona](./imaging-persona.md) - The stated goal of surrounding a patient's Imaging Problem List with clinical context, orders, baseline history, and prior interventions.
* [Imaging Problem List](./imaging-problem-list.md) - A patient's imaging findings organized by finding rather than by date, each carrying the observations that support it across exams.
* [Index code](./index-code.md) - A reference from a finding model, attribute, or value to a concept in a standard ontology, carried as system, code, and optional display.
* [Laterality](./laterality.md) - The left, right, or unsided character of an anatomic structure or a finding, represented as a triad of linked variants and resolved by a stated precedence.
* [LOINC](./loinc.md) - Logical Observation Identifiers Names and Codes, the system OIDM uses to identify exam types on Exam Finding Lists and reports.
* [LOINC/RSNA Radiology Playbook](./loinc-rsna-radiology-playbook.md) - The jointly governed radiology part of LOINC that names imaging orderables along modality, anatomy, and technique axes.
* [Measurement](./measurement.md) - A quantitative descriptor, defined in the next-generation CDE vocabulary as distinct from a DataElement and realized in OIFM as a numeric attribute.
* [Observation](./observation.md) - The atomic unit of OIDM data, one finding seen or excluded on one exam, with its anatomic location and attribute values.
* [OIDM](./oidm.md) - The Open Imaging Data Model, the project and the family of specifications it publishes for representing imaging exam results as structured data.
* [OIDM organization code](./oidm-organization-code.md) - The three or four letter uppercase segment inside an OIFM or OIFMA identifier that names the organization which minted it.
* [OIFM](./oifm.md) - Open Imaging Finding Model, the OIDM specification for a finding definition, and the prefix of the identifiers that specification mints.
* [Open Imaging Reporting SDK](./open-imaging-reporting-sdk.md) - A named but unbuilt software development kit intended to let vendors build reporting tools on OIDM structures.
* [Presence](./presence.md) - The near-universal first attribute of a finding model, asserting that a finding was present, absent, indeterminate, or unknown, and the dot-code convention that encodes those values.
* [Provenance](./provenance.md) - The record of where an observation came from, a radiologist, an AI tool, or a language model reading a report, and of the text that supports it.
* [RadElement](./radelement.md) - The ACR and RSNA registry that publishes common data element sets and elements, and the coding system their identifiers belong to.
* [RadLex](./radlex.md) - The RSNA radiology lexicon, the ontology that supplies identifiers for anatomic locations and many finding and attribute codes.
* [RadLex ID (RID)](./radlex-id.md) - The identifier form used by RadLex concepts, and the primary key of OIDM anatomic locations.
* [SNOMED CT](./snomed-ct.md) - The clinical terminology used in OIDM as a secondary coding system on findings, attribute values, and anatomic locations.
* [Tag](./tag.md) - A free-text clinical category attached to a finding model for organization and retrieval, distinct from the typed structured metadata that is replacing it.
* [Technical finding](./technical-finding.md) - A finding stated in modality-specific imaging language, such as a density or signal characteristic, without committing to an underlying diagnosis.
* [UMLS](./umls.md) - The Unified Medical Language System, used in OIDM as the hub for translating identifiers between terminologies and as a cross-reference on anatomic locations.
