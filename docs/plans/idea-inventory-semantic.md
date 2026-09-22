# Idea inventory: the semantic ideas

Step 1 of [restructure-around-project-ideas.md](restructure-around-project-ideas.md), Claude side.
Area: finding models and their relationship to ACR/RSNA common data elements; anatomic locations
and their relationship to RadLex; exam types; the terminologies underneath.

This is a working inventory, not a draft of any page. It records distinct ideas the team has
expressed or demonstrated, with pinned evidence. It does not reconcile disagreements and does not
supply motivation the sources do not state.

## How to read an entry

**Status** is one of *stated goal*, *working proposal*, or *implemented example*. One idea can carry
several.

**Implemented** says what the code or content actually does about the idea, in the idea's own terms,
with a pointer. It does not reproduce install steps, usage documentation, or schemas.

**Evidence** names the specific document, prompt, skill, or data file and what it says. Prompts are
primary sources: they are where the team's operational definitions are written down and enforced.
Pointers take the form `path @ branch commit`. Manuscripts under peer review are paraphrased, never
quoted, and are not treated as accepted fact; their reviewer correspondence was not read. People are
not named; organizations and roles are.

## Commit pins

| Repository | Branch | Commit |
|---|---|---|
| `findingmodel` | `main` | `75afd39` |
| `findingmodel` | `dev` | `504a42a` |
| `findingmodel` | `feature/metadata-cleanup` | `1942b06` |
| `findingmodels` | `main` | `4475ac1` |
| `findingmodels` | `taxonomy-export-2026-08-15` | `a30c3c9` |
| `findingmodels` | `content/chestcts` | `0472a46` |
| `findingmodels` | `findingmodels-metadata` | `dcc6c4c` |
| `ACR-RSNA-CDEs` | `next-gen-2026` | `44836c1` |
| `CDEStaging` | `main` | `b814a10` |
| `anatomiclocations.org` | `main` | `1f39fa4` |
| `anatomiclocations.org` | `content_work` | `35624d7` |
| `BodyPartIndex.py` | `main` | `388ae0a` |
| `BodyPartIndex.ts` | `main` | `dec578e` |
| `RadLex` | `main` | `13a5abe` |
| `RadLex` | `experiment/kg-radlex-parsing` | `5162a65` |
| `med-ontology-lookup` | `main` | `a1fd3ae` |
| `med-ontology-lookup` | `issue-3-typed-provider-failures` | `9cc3eec` |
| `med-ontology-lookup` | `docs/reviewed-proposal-backlog` | `f059792` |

Non-repository sources: the Anatomic Locations Index manuscript under review at JDIM
(`sources/bucket/text/jdim-02183.md`, manuscript body pages 3 to 17 only); the SIIM Enterprise
Imaging webinar of 15 July 2026 (`sources/bucket/text/ipl-webinar-deck.md`); the Next Gen Object
Oriented Reporting Schema deck of 15 September 2026 (`sources/bucket/REPORT.md` §6); fifteen
Excalidraw boards (`sources/excalidraw-diagrams.md`); the project lead's goals recorded in
`knowledge/plans/2026-09-20-knowledgebase-build-plan.md`.

---

# A. What a finding model is

## A1. Finding model

**Idea.** A finding model is "a structured, machine-readable definition of an observation a
radiologist would name in a report." The library of models is framed not as a label set but as the
knowledge base that lets downstream systems turn unstructured report text into structured
observation objects, each tagged with the finding type and its attribute values. Two guiding
principles are stated together: a finding is a noun phrase and everything else is an attribute; and
findings exist in time, because a report is a snapshot while the findings it describes persist
across exams.

**Status.** Implemented example, with the rationale stated.

**Implemented.** Two model classes with the same docstring express the authoring lifecycle: a base
model carrying name, description, synonyms, tags and attributes with no identifiers, and a full
model adding the finding identifier, per-attribute identifiers, per-value codes, index codes,
anatomic locations and contributors. An abstract protocol names the surface both share.
`packages/findingmodel/src/findingmodel/finding_model.py @ main 75afd39`;
`packages/findingmodel/src/findingmodel/abstract_finding_model.py @ main 75afd39`.

**Evidence.**
- The `core_concept.md` prompt fragment, "What a finding model is" and "Two guiding principles" —
  the definition, the noun-phrase principle, and the findings-exist-in-time argument that justifies
  a change-from-prior attribute on every model.
  `prompts/fragments/core_concept.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Finding Models: Overview" authoring document, "Why Finding Models Exist" — the report to
  observation to downstream pipeline, and the claim that the definitions carry meaning rather than
  names. `notes/oifm-overview.md @ next-gen-2026 44836c1` (a verbatim copy of the upstream
  `prompts/overview.md`).
- The "Finding Model Schema" document, "Main Finding Model Object" — required identifier, name,
  description and attributes; optional synonyms, tags, contributors and index codes.
  `schema/finding_model_schema.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "OIFM Repo" Excalidraw board, handwritten explainer panel — the team's own plain-language
  framing: "Writing the dictionary to translate from radiologist language to computer-speak and
  back." `sources/excalidraw-diagrams.md`

**Related.** A2, A3, A5, A6, A9, B1.

**Disagreements.** Naming differs across the allied work: *finding model / attribute / value* in the
finding model documents, *FindingClass / DataElement / Value* in the next-generation vocabulary,
*Finding / Attribute* in an earlier committee-facing deck. The rename decision and the table of who
said what are recorded in "Next-Generation CDE Schema: Current Understanding" §6
(`docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`).

**Undetermined.** Whether one vocabulary absorbs the other. Issue F of that same document states the
open alternatives and does not choose.

---

## A2. What counts as a finding

**Idea.** The boundary is drawn by a test: would a radiologist write "there is [X]" or "no [X]" as a
standalone statement? Findings include pathology, physiologic observations, devices and hardware,
postsurgical states, anatomic variants, image-quality observations, and diagnoses. What is excluded
is enumerated just as carefully: a state of a finding ("stable cardiac silhouette"), a qualified
version of another finding ("large pleural effusion"), normal anatomy, radiographic signs and
interpretation techniques ("silhouette sign", "double density sign", "air-fluid level"), and exam
metadata, history or recommendations. A generic descriptor can become a finding when anatomic
context makes it reportable on its own: "air-fluid level" is not a finding, "air-fluid levels in
bowel" is.

**Status.** Stated as doctrine in prompts; enforced as a review checklist item, not by code.

**Implemented.** The quality-review checklist opens with the noun-phrase and level-of-abstraction
checks, and the review skill runs that checklist against one file at a time.
`prompts/fragments/quality_checklist.md @ taxonomy-export-2026-08-15 a30c3c9`;
`.claude/skills/finding-review/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The `core_concept.md` fragment, "What counts as a finding" and "What is NOT a finding" — the six
  inclusion categories and the five exclusion categories, with the air-fluid-level boundary case.
  `prompts/fragments/core_concept.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Finding Models: Overview" document, "The 'Would a radiologist report it?' Test" — the same
  test with worked yes and no cases. `notes/oifm-overview.md @ next-gen-2026 44836c1`
- The "Open Imaging Finding Models" Excalidraw board, box "Finding Model Rules" — an earlier draft
  of the same guidance, adding two rules the current fragments do not state in those words: avoid
  "associated findings" where a related finding is clinically distinct, and consider splitting
  clearly distinguishable sub-types into separate models. `sources/excalidraw-diagrams.md`

**Related.** A1, A3, A4, A5, B7.

**Disagreements.** The board's sub-type rule (split solid from part-solid pulmonary nodule) sits
against the next-generation vocabulary's stated presumption to lean toward the general class with
location carried separately, which "What the Vocabulary Must Express" §2.4 calls "the
highest-frequency modelling decision in the corpus" and records as unresolved.
`docs/next-gen-schema/01-what-the-vocabulary-must-express.md @ next-gen-2026 44836c1`

**Undetermined.** Whether the board rules were superseded deliberately. The board is undated in the
transcription.

---

## A3. Specificity, splitting, and the right level of abstraction

**Idea.** Three related questions are answered by one document: is this one finding or several; is
this subtype a value on the parent or its own model; is this name at the right level. Compound names
joining two entities split when one part can be present while the other is absent. A subtype becomes
its own model when it is a fundamentally distinct observation rather than the same observation with
a qualifier, with a practical signal offered: you would need different attributes to describe it.
"Tension pneumothorax" is not "pneumothorax, type: tension" because it has its own signs and its own
management implications. A descriptor plus entity earns its own model when the combined phrase
carries meaning beyond the sum of its parts: "calcified nodule" implies a benign fully calcified
lesion while "nodule with calcifications" implies one that may still warrant follow-up. Findings at
several levels may coexist when radiologists report at both.

**Status.** Stated as authoring doctrine; applied by judgment.

**Implemented.** The review sub-agent returns extraction candidates naming the exact attributes that
should become their own model, and those candidates are recorded rather than auto-applied.
`.claude/skills/finding-review/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`, steps 4 and 5.

**Evidence.**
- The `scope_and_specificity.md` fragment — the compound-splitting test, the subtype decision
  question, the descriptor-plus-entity test, and the too-broad / too-narrow / right-level worked
  lists. `prompts/fragments/scope_and_specificity.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Finding Models: Overview" document, "Specificity and Scope" — the same material in the
  upstream authoring guidance. `notes/oifm-overview.md @ next-gen-2026 44836c1`

**Related.** A2, A4, A7, B7.

**Disagreements.** None within the finding model documents.

---

## A4. Negative assertion as a first-class finding

**Idea.** "No fracture" and "the upper abdomen is unremarkable" are active observations of absence,
so the library deliberately carries broad scoped findings such as "chest wall fracture" and "upper
abdominal abnormality" purely so that absence can be asserted against something. The scope of such a
finding is set by what is assessable on an exam: "fracture" is too broad because it spans the whole
body, "chest wall fracture" is right for a chest radiograph, "upper abdominal abnormality" is right
for a chest CT because the upper abdomen is in the field of view.

**Status.** Stated as an authoring rule; implemented in every model's first attribute; reappears as
a structural requirement in the next-generation vocabulary.

**Implemented.** Every model carries `presence` as its first attribute with the four values absent,
present, indeterminate and unknown, and the creation script emits it unconditionally. Any source
offering only yes/no or bare present/absent is upgraded to the full four-value set.
`prompts/fragments/presence_and_change.md @ taxonomy-export-2026-08-15 a30c3c9`;
`packages/findingmodel/src/findingmodel/create_stub.py @ main 75afd39`.

**Evidence.**
- The `scope_and_specificity.md` fragment, "Findings must cover negative assertions" and "Scoped
  broad findings (for 'no X' assertions)" — the rule and the two worked names.
  `prompts/fragments/scope_and_specificity.md @ taxonomy-export-2026-08-15 a30c3c9`
- "What the Vocabulary Must Express" §1 — why a finding class must be a term rather than a set of
  actual lesions, so that an observation carrying `presence: absent` is not pointing at a nodule
  that does not exist; and §5, where `grouping` is dropped as a classification value and returns as
  a narrow node type for negative-only nodes such as "renal abnormality".
  `docs/next-gen-schema/01-what-the-vocabulary-must-express.md @ next-gen-2026 44836c1`
- The SIIM webinar worked Exam Finding List — a pertinent negative, "no filling defect to suggest
  pulmonary embolism," coded as present/absent rather than omitted.
  `sources/bucket/text/ipl-webinar-deck.md`

**Related.** A2, A5, B5, C1.

**Disagreements.** Whether negation propagates down the finding hierarchy is open. "Current
Understanding" Issue A records the motivating case and states the three conditions it depends on,
including a closed-world assumption that the radiologist actually assessed everything beneath the
class. `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`

---

## A5. Description and diagnosis both count

**Idea.** Radiologists both describe what they see and name what they conclude, and the team models
what radiologists actually say rather than what a cleaner ontology would prefer. The authoring
guidance is explicit that diagnostic terms are first-class findings and instructs authors not to
question whether a diagnosis "should" be one.

**Status.** Stated as an authoring rule; implemented as data in two different ways.

**Implemented.** In the exam-oriented sub-taxonomies the distinction is a column, `finding_type`,
separating an observation from a diagnosis on every row; the CT head list types 261 rows observation
and 222 diagnosis, the CT chest/abdomen/pelvis list 1,371 and 448.
`lists/README.md @ taxonomy-export-2026-08-15 a30c3c9`. In the metadata work it becomes a model-level
enumeration, `entity_type`, whose assignment prompt draws the line: diagnosis for named diseases,
disorders, injuries, complications, syndromes and disease entities; finding for broad observations,
descriptive lesions, morphology, enhancement patterns, effusions and umbrella abnormality labels.
`packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/entity_type.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The `core_concept.md` fragment, "What counts as a finding" — diagnoses listed with the
  instruction "Do not question whether a diagnosis 'should' be a finding."
  `prompts/fragments/core_concept.md @ taxonomy-export-2026-08-15 a30c3c9`
- The `entity_type.md` assignment prompt — the operational rule set, including that source tags are
  weak context and must not alone determine the type, and that negative findings, artifacts,
  assessments and recommendations must not be converted into diseases merely because they imply
  clinical consequences.
  `packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/entity_type.md @ feature/metadata-cleanup 1942b06`
- "What the Vocabulary Must Express" §1 and §5 — the finding and diagnosis definitions taken over
  from the finding model guidance unchanged, with the observation that the classification is of the
  term as used, not of the bodily state.
  `docs/next-gen-schema/01-what-the-vocabulary-must-express.md @ next-gen-2026 44836c1`

**Related.** A1, A9, B5.

**Disagreements.** Three positions coexist. The finding model corpus keeps finding and diagnosis as
values of one field on one kind of object. The next-generation vocabulary makes Diagnosis a separate
node type while keeping one taxonomy that crosses the labels, with the "X without Y" test as the
subsumption criterion ("empyema without effusion" is not a sentence, so empyema is a subtype of
pleural effusion across the label boundary). An external reviewer's alpha implementation declares
the two disjoint in OWL, with probes that expect a finding which is also a diagnosis to be
unsatisfiable. The comparison document records this as decision area ST03, to be worked through
rather than settled. `docs/next-gen-schema/07-relationship-family.md` §2 and
`docs/next-gen-schema/12-alpha-structural-comparison.md` §3 @ `next-gen-2026 44836c1`. Separately,
the profile of the exam-oriented sub-taxonomies notes that no diagnosis is ever placed under an
observation in those files, which the unrestricted taxonomy would change, and marks it "worth
raising with the author". `notes/hood-taxonomies-profile-2026-09-01.md @ next-gen-2026 44836c1`

---

## A6. Presence and change from prior

**Idea.** Every finding model carries two standard attributes first and in order: presence, then
change from prior. Change from prior is not a single vocabulary but a minimum set (unchanged,
stable, new, resolved) plus at least one clinically appropriate direction-of-change pair, and the
instruction is to include every descriptor a radiologist might reach for rather than the single best
one, because "over-inclusion is cheap; under-inclusion causes missed matches." A pleural effusion can
be described as larger, increased, or worsened, so all three pairs go in. Categories that cannot
change that way get the minimum set only: devices and hardware, congenital variants, postsurgical
states, and technique observations. Individual pairs are dropped where they make no sense even when
others apply, so a fracture can be new, resolved or unchanged but does not get larger.

**Status.** Implemented example, with the rationale stated.

**Implemented.** The creation script emits the minimum set by default and takes direction pairs as an
explicit opt-in flag per model or per batch entry; it also strips the awkward leading article from
the generated attribute description. The quality-review step then confirms the pair choice, and a
separate script modifies pairs after the fact.
`prompts/fragments/presence_and_change.md @ taxonomy-export-2026-08-15 a30c3c9`, "What the create
script does, and what review must catch".

**Evidence.**
- The `presence_and_change.md` fragment — the two required attributes and their order, the four
  presence values, the three direction pairs with the finding categories each suits, the exclusion
  categories, and a grammar section governing the attribute description (plural verbs for plural
  nouns, article agreement, no article for mass nouns).
  `prompts/fragments/presence_and_change.md @ taxonomy-export-2026-08-15 a30c3c9`
- The `core_concept.md` fragment, "Findings exist in time" — the temporal justification for
  requiring change from prior on every model.
  `prompts/fragments/core_concept.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Open Imaging Finding Models: Pipeline and Repo" flowchart on the "OIFM Repo" board — the
  same two attributes, plus optional location and size, as the defining shape of a stub.
  `sources/excalidraw-diagrams.md`

**Related.** A1, A4, A8, A12.

**Disagreements.** The upstream-proposals document records that the library's own stub creator
emitted all eight change-from-prior values unconditionally and generated an awkward description, that
12 of 14 models in a head-CT test batch had their pairs winnowed by review, and that every one had
the article flagged; it proposes inverting the default. This is a recorded defect in the library, not
a dispute about the rule. `docs/plans/findingmodel-upstream-proposals.md @ taxonomy-export-2026-08-15 a30c3c9`, item B1.

---

## A7. Synonyms as the matching surface

**Idea.** Synonyms are how unstructured report text reaches a model, so the instruction is to be
aggressive about collecting them: formal and informal forms, acronyms, eponyms, brand names,
spelling variants, plurals, and common report phrasings such as "air under the diaphragm" for
pneumoperitoneum. The strictness rule is the counterweight: every synonym must mean the exact same
thing at the same level of specificity, because "a bad synonym doesn't just fail to match — it
matches the *wrong thing*." Subtypes are never synonyms. A taxonomy of traps is given: sign versus
disease (Kerley B lines are not interstitial pulmonary edema), consequence versus cause, different
pathophysiology (ventricular hypertrophy is not enlargement), different procedure (kyphoplasty is
not vertebroplasty), device subtype, and wrong anatomic scope.

**Status.** Implemented example (the rule is enforced procedurally at authoring time).

**Implemented.** Two checks run before a synonym is added. A collision check searches the corpus and
branches three ways: the term already sits on a model meaning the same thing, which signals a
possible duplicate model and is flagged rather than merged; the term sits on a model meaning
something different, in which case it is added to neither and the ambiguity is flagged; or it is not
found, and is safe. A pre-emptive cross-body-region check then asks whether the term is canonical for
a different finding elsewhere even if the corpus does not yet contain that model, with follicular
cyst, cavernous hemangioma, adenoma, carcinoid and nodule named as traps.
`prompts/fragments/synonym_rules.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The `synonym_rules.md` fragment — the aggressiveness instruction, the same-meaning-same-specificity
  test, the nine-row trap taxonomy, the collision procedure, and the cross-body-region check.
  `prompts/fragments/synonym_rules.md @ taxonomy-export-2026-08-15 a30c3c9`
- The `naming.md` fragment, "When to keep the unscoped short form as a synonym" — the rule that
  generic imaging descriptors such as hypoattenuation, enhancement, calcification, lucency and
  sclerosis fail the test because context does not reliably disambiguate them at the language-model
  layer. `prompts/fragments/naming.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** A1, A8, E2.

**Disagreements.** None recorded.

---

## A8. Naming conventions

**Idea.** Names are lowercase with spaces, acronyms expanded with the acronym kept as a synonym,
eponyms minimized, brand names replaced by the generic term. A name must be self-describing enough
that someone scanning thousands of models can tell what each is about, which means an anatomic
anchor: "pulmonary linear opacity" not "linear opacity". The anchor must be real anatomy rather than
a generic tissue-type modifier, because "parenchymal", "cortical", "stromal" and "medullary" are
ambiguous across organs. Names carry no parenthetical qualifiers, no population qualifiers, no "with"
clauses embedding an associated finding, and no comma lists; slashes are handled by type, splitting
genuinely different findings, converting locations or severities into an attribute, and demoting
truly interchangeable terms to synonyms.

**Status.** Implemented for models the project authored; not yet true of imported content.

**Implemented.** A deterministic linter checks underscores, lowercase, self-synonyms and the rest,
labelling each hit an error (definitely wrong, auto-fixable), a warning (needs human confirmation),
or a review item (needs language-model judgment). Filenames are derived mechanically from the name,
and the rule that a name producing consecutive underscores must be simplified is a naming rule
justified by that derivation.
`prompts/fragments/mechanical_lint.md` and `prompts/fragments/naming.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The `naming.md` fragment — casing, canonical forms with worked substitutions, the self-describing
  rule with the tissue-modifier trap, the conciseness rules, and the slash typology.
  `prompts/fragments/naming.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Definition Cleanup Plan" — nine mechanical defect classes traceable to imported content,
  including title case on common-data-element and institutional models, "with" clauses, and
  population qualifiers such as "cerebellar mass in a child", each with worked examples.
  `docs/plans/definition_cleanup.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** A7, A11, B12.

**Disagreements.** None on the rules. The cleanup plan's own corpus counts disagree with the
identifier registry shipped in the same tree, because the plan was written at an earlier commit.

---

## A9. Assessment schemes modeled apart from what they assess

**Idea.** A scoring system is a valid finding model but a different model from the observation it
scores. A pulmonary nodule model captures what the nodule looks like; a Lung-RADS model captures the
risk category assigned to it. The stated reason is that different radiologists can describe the same
nodule identically and assign different categories, so systems need to reason about the two
independently. Measurement groupings are also valid findings, where "the 'finding' is the act of
performing a structured quantitative assessment, and the attributes are the measurements within it."

**Status.** Stated as an authoring rule; implemented as a metadata value; extended into a node type
in the next-generation vocabulary.

**Implemented.** `assessment` is a value of the entity-type enumeration, and its assignment prompt
defines it as a score, grading scale, classification, reporting category, or grouped
measurement-and-interpretation package, distinct from `measurement`, which is one quantitative
metric.
`packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/entity_type.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The `scope_and_specificity.md` fragment, "Scoring systems and structured assessments are valid
  findings" — the rule with its stated reason, and the measurement-grouping paragraph.
  `prompts/fragments/scope_and_specificity.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Definition Cleanup Plan", reclassification section — pushback from the data side, flagging
  imported entries such as "Alpha Angle Measurement" as quantification tools rather than
  observations, which is why they lack presence.
  `docs/plans/definition_cleanup.md @ taxonomy-export-2026-08-15 a30c3c9`
- "The Finding and Diagnosis Relationship Family" §1 — `ASSESSED_BY` from a finding or diagnosis to
  an assessment, with `INTERPRETED_FROM` as its finer twin naming the specific inputs a scheme is
  computed from. `docs/next-gen-schema/07-relationship-family.md @ next-gen-2026 44836c1`

**Related.** A5, B6, B8.

**Disagreements.** None recorded.

---

## A10. Associated findings versus components

**Idea.** Two different kinds of related thing get two different treatments, distinguished by an
independence test. An associated finding is separate and independent with its own lifecycle —
pneumonia and pleural effusion each occur alone — and is modelled as one multichoice attribute on
the index model, presence-level only, whose values name real finding models. A component is an
intrinsic part of the finding itself — the solid component of a mixed pulmonary nodule — and is
extracted into its own model; the parent may record only its presence or its count, never its size,
density or morphology, because those belong to the component's own model. Three signals mean
something needs extraction: prefixed attributes such as "solid component size", groups of attributes
all describing the same sub-entity, and characterization beyond presence of something other than the
index finding.

**Status.** Stated as an authoring rule and enforced as a lint check on one branch; contradicted by
another branch.

**Implemented.** The deterministic linter checks the associated-findings shape, flagging attributes
scattered as separate "presence of X" entries rather than consolidated into one multichoice
attribute. Extraction candidates surface in the review sub-agent's output field rather than being
applied automatically.
`prompts/fragments/mechanical_lint.md` and `prompts/fragments/associated_vs_component.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The `associated_vs_component.md` fragment — both independence tests, the one-attribute rule with
  its worked shape, the parent-may-record-count rule, and the three extraction signals.
  `prompts/fragments/associated_vs_component.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "Open Imaging Finding Models" board, "Finding Model Rules" — the earlier and stricter form of
  the same instinct: avoid associated findings, give a clinically distinct related finding its own
  model. `sources/excalidraw-diagrams.md`

**Related.** A2, A3, B8.

**Disagreements.** Direct and unresolved. The chest CT content branch's project specification
forbids an associated-findings attribute outright and requires separate findings instead, the
opposite of the main rule. Its own output does neither cleanly: a converted model carries exactly the
scattered per-finding presence attributes the main linter treats as a defect.
`PROJECT_SPECIFICATION.md` parts 4 and 9, and `defs/from_cdestaging_ct_chest/aberrant_subclavian_artery.fm.json`,
both `@ content/chestcts 0472a46`.

---

# B. How the content is made

## B1. Identifiers that carry provenance

**Idea.** A finding model identifier has the form `OIFM_{ORG}_{six digits}`, an attribute
`OIFMA_{ORG}_{six digits}`, and a choice value a code derived from its attribute's identifier. The
three-or-four-letter middle segment is the contributing organization, so provenance is legible from
the identifier itself and different institutions can mint without a central allocator.

**Status.** Implemented example.

**Implemented.** Identifier allocation queries the published index for identifiers already used by
that organization code, then draws random six-digit candidates with collision retry; promoting a base
model to full mints the model identifier and any missing attribute identifiers. Choice-value codes
are generated mechanically from the parent attribute's identifier. A validator enforces global
uniqueness of both identifier kinds and additionally detects case-folded name conflicts, normalized
slug conflicts, and an attribute identifier owned by a different model — duplicate detection at the
identifier level, not the semantic level.
`packages/findingmodel/src/findingmodel/index.py` and
`packages/findingmodel/src/findingmodel/index_validation.py @ feature/metadata-cleanup 1942b06`;
`packages/findingmodel/src/findingmodel/finding_model.py @ main 75afd39`.

**Evidence.**
- The "Finding Model Structured Metadata Fields" reference, identity fields — the pattern and the
  statement that the prefix is the contributing organization code, with a worked identifier.
  `notes/oifm-metadata-fields.md @ next-gen-2026 44836c1`
- The repository's own `CLAUDE.md` — the identifier patterns, the rule that generated artifacts are
  never hand-edited, and the validator workflow that regenerates them.
  `CLAUDE.md @ taxonomy-export-2026-08-15 a30c3c9`
- The "OIFM Repo" board, notes "Identifier format" and "Prelim OIFM ID" — the earlier form
  `OIFM_CRTR_123456`, the source-organization list, and a serial scheme of days since 2025-01-01
  plus random digits. `sources/excalidraw-diagrams.md`

**Related.** A1, B2, C3.

**Disagreements.** The next-generation vocabulary mints from a single fresh namespace with no
organization segment, and "Current Understanding" Issue E records as open "whether the ID space is
partitioned for distributed minting", naming the finding model organization segment as the existing
mechanism for exactly that.
`docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`

---

## B2. Corpus as a merge of uneven provenance streams

**Idea.** The corpus is not one authoring effort but several merged. Counted from the identifier
registry, 2,382 finding models come from five sources: 1,933 derived from the Radiology Gamuts
Ontology, 256 authored by the project, 115 from ACR/RSNA common data elements, 47 from an
institutional contributor, and 31 from a vendor. Each stream carries its own defects, and the cleanup
plan traces nine mechanical defect classes to specific streams.

**Status.** Implemented example (the corpus); stated cleanup plan, still marked draft.

**Implemented.** Conflicting imports are quarantined rather than deleted: eighteen files sit in a
`conflicts/` tree under subdirectories named for the collision they represent, held out of the live
corpus. `conflicts/ @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The identifier registry — the per-organization counts above.
  `ids.json @ taxonomy-export-2026-08-15 a30c3c9`
- The "Definition Cleanup Plan" — the nine defect classes with per-class counts and worked examples,
  and the observation that some Gamuts-derived entries are differential-diagnosis patterns rather
  than findings at all. `docs/plans/definition_cleanup.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** A8, B3, B12.

**Disagreements.** The cleanup plan's counts (2,379 models) differ from the registry shipped beside
it (2,382), because the plan was written at an earlier commit. The webinar states 2,458 as of July
2026. These are freshness differences, not conflicting claims.

---

## B3. Stub creation and iterative improvement

**Idea.** Most of a finding model can be produced mechanically. A list of finding names is drawn
from three sources — an existing ontology, subject-matter experts, and a model reading real report
text — and every name becomes a stub carrying presence and change from prior, plus location and size
where the finding has them. Stubs get identifiers immediately so they can be used at once, and are
then improved through four named iteration modes: experts propose changes and a model edits the JSON
for them; a model proposes improvements from reference material it may find itself; sites download a
kit, combine their own report text with published models, and submit pull requests; and outside
groups review models and endorse them.

**Status.** Implemented example for stub creation and two iteration modes; working proposal for the
site kit and the endorsement mode.

**Implemented.** Stub creation emits a base model with exactly the two canned attributes. A separate
optional step drafts a richer description with citations and prints it for review without touching
the model file; a fix script writes an approved description and synonym list back in. The enrichment
fragment restricts this to single-finding work and tells batch flows to skip it as too slow.
`packages/findingmodel/src/findingmodel/create_stub.py @ main 75afd39`;
`prompts/fragments/enrichment.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The "Open Imaging Finding Models: Pipeline and Repo" flowchart on the "OIFM Repo" board — the
  three sources, the stub fields, and the four iteration modes with their descriptions; the
  "Community Connect 2024-11-07" note on the same board gives the same approach as a method for
  creating data models at scale. `sources/excalidraw-diagrams.md`
- The `enrichment.md` fragment — when to use the description-drafting step and when not to.
  `prompts/fragments/enrichment.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** A6, B4, B5, B12.

**Undetermined.** Whether the downloadable site kit or the endorsement mode were ever built. No
artifact was found for either.

---

## B4. Triage before create

**Idea.** Nothing is authored before the corpus has been searched properly. Two or three
complementary search targets are generated per candidate, run, and the pooled results judged for
exact semantic match by the agent itself, which reports one of three outcomes: an exact match, no
match after reasonable search, or true ambiguity. The instruction "Do not forward raw result lists to
the user" makes the judgment the agent's job rather than the reader's.

**Status.** Implemented example.

**Implemented.** The search-and-triage fragment lists six specificity traps that the judgment must
avoid. On the chest CT content branch the triage becomes a persisted artifact: each source record
gets its search targets, a decision, the matched identifier, and the full candidate list with the
query that surfaced each, committed alongside the converted models.
`prompts/fragments/search_and_triage.md @ taxonomy-export-2026-08-15 a30c3c9`;
`reviews/triage_cdestaging_chunk_1.json @ content/chestcts 0472a46`.

**Evidence.**
- The `search_and_triage.md` fragment — the procedure, the three outcomes, and the traps.
  `prompts/fragments/search_and_triage.md @ taxonomy-export-2026-08-15 a30c3c9`
- The `finding-author` skill, step 1 — the same procedure as the first step of interactive
  authoring, with the no-raw-lists instruction restated.
  `.claude/skills/finding-author/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** A7, B3, B5, B6.

---

## B5. Review in three tiers, with context isolation

**Idea.** Review is layered, and each layer does only what it is good at. A deterministic linter
runs pure pattern checks and labels each hit an error, a warning, or a review item. A language-model
quality review then applies a checklist that the linter deliberately does not attempt, and is given
one file path and nothing else. A human sign-off through a terminal interface is mandatory for batch
and review flows. The context rule is stated as a requirement rather than a preference: "Cross-finding
context isolation is mandatory: each finding is drafted and reviewed by a fresh sub-agent with no
exposure to its neighbors."

**Status.** Implemented example.

**Implemented.** The review skill refuses to run against a dirty working tree so that its edits can
be diffed cleanly, with a conversational override and no command-line flag for it. Fan-out runs in
parallel groups of five, each sub-agent receiving a single file path with the instruction "No
neighbors, no batch context, no prior conversation." Concrete suggested fixes are applied;
extraction candidates and warnings are recorded into a review file rather than applied.
`.claude/skills/finding-review/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`, steps 1 through 5;
`.claude/skills/finding-batch/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The `mechanical_lint.md` fragment — the deterministic checks and the three severity levels with
  their meanings. `prompts/fragments/mechanical_lint.md @ taxonomy-export-2026-08-15 a30c3c9`
- The `quality_checklist.md` fragment — the checklist, the required output shape, and an explicit
  section naming what it intentionally does not flag.
  `prompts/fragments/quality_checklist.md @ taxonomy-export-2026-08-15 a30c3c9`
- The `finding-batch` skill — the isolation requirement stated as mandatory, the accepted input
  shapes, and the cross-row duplicate check surfaced to the user before drafting.
  `.claude/skills/finding-batch/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** B4, B6, C6.

---

## B6. Prompts as loadable fragments, sized against measured degradation

**Idea.** The authoring rules live in small fragment documents that a skill loads at the step where
they apply, and the skill files are "pure orchestration". The reason is written down and measured
rather than asserted: instruction-following degrades as the number of simultaneous instructions
rises, material in the middle of a long prompt gets less attention than material at either end, and
extraneous but semantically similar context measurably harms structured output. The team's own
diagnosis of its earlier prompts is that a review agent with about forty checklist items plus a
thirty-rule conventions document was "deep in degradation territory", and that appending conventions
after the task instructions pushed the agent's own task rules into the lost middle.

**Status.** Implemented example, with the research written up as the justification.

**Implemented.** Fifteen fragments sit under a prompts directory with a defaults file, and each
skill names the fragment to load at each step rather than inlining the rules. The `finding-author`
skill loads orientation once per session, then names a different fragment at search, at synonym
editing, at drafting, at creation, and at lint.
`prompts/fragments/ @ taxonomy-export-2026-08-15 a30c3c9`;
`.claude/skills/finding-author/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- "Prompt Length and Instruction Complexity: Research and Recommendations" — the question as the
  team posed it (about 19 KB of shared documents inlined into every agent call, roughly 25,000
  characters of instructions per call), the five research findings, and the analysis of the team's
  own three agent prompts against them.
  `docs/plans/prompt_length_research.md @ taxonomy-export-2026-08-15 a30c3c9`
- The three skill files — each states "All rules, CLI cheatsheets, and procedures live in
  `prompts/fragments/`. This file is pure orchestration."
  `.claude/skills/{finding-author,finding-batch,finding-review}/SKILL.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** B5, C6.

**Disagreements.** None recorded. The related rule on the metadata side is stricter still: when an
evaluation miss exposes a general rule, add it to the field-standards document and cover it with an
evaluation rather than pasting the missed case into the prompt, and never copy active evaluation
fixtures into prompt text.
`docs/metadata/enrichment/prompt-guidance.md @ feature/metadata-cleanup 1942b06`

---

## B7. Exam-oriented finding sub-taxonomies

**Idea.** Content direction is now six per-exam-context finding hierarchies — chest radiograph,
musculoskeletal radiograph, head CT, chest/abdomen/pelvis CT, mammography, spine MRI — 3,789 rows in
total. Each file is one hierarchy in which a row names its parent by name, "Parents are generic,
children add specificity". An anatomic category sits beside the hierarchy as an independent grouping
rather than part of it. The project lead stated on 2026-09-21 that this branch is "the immediate
direction for all of the content, probably replacing a lot of the Gamuts-based models", and asked
that the taxonomies be called the MGB exam-oriented sub-taxonomies.

**Status.** Stated goal (the direction); implemented example (the six files).

**Implemented.** The taxonomy doubles as a coverage ledger. An identifier is filled only where a row
matched a model that already exists, by exact name, and "Nothing was minted here"; 1,028 of 3,789
rows matched, so the files measure as data how much of each exam type the corpus covers, very
unevenly — 305 of 403 for chest radiographs against 5 of 198 for mammography. "Blank rows are the
ones needing triage." A writeback loop fills that column, runs only after full review and human
sign-off, and is idempotent.
`lists/README.md @ taxonomy-export-2026-08-15 a30c3c9`;
`prompts/fragments/csv_writeback.md @ taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The taxonomy README — the six files with row and identifier counts, the column meanings, the
  parent semantics, the nothing-was-minted rule, and the warning that an identifier can appear on
  two rows where earlier writebacks mapped two findings onto one model.
  `lists/README.md @ taxonomy-export-2026-08-15 a30c3c9`
- "Profile of the Hood Finding Taxonomies" — the measured shape: 411 of 414 untyped rows are parents
  of other rows; 73 parents in the CT list have both observation and diagnosis children; a recurring
  three-part naming pattern of abnormality, anatomic variant and postsurgical change per region;
  eight rows sharing an identifier with another row.
  `notes/hood-taxonomies-profile-2026-09-01.md @ next-gen-2026 44836c1`
- The project lead's recorded content direction.
  `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`

**Related.** A5, B2, B12, D1.

**Disagreements.** The profile records that a morphology axis derived from a name-suffix census was
proposed and rejected on 2026-09-02, on the grounds that the suffixes describe how names are formed
rather than categories radiologists reason about. It also records the duplicate identifiers as unmade
synonym-or-subtype decisions.

**Undetermined.** Whether the hierarchy is meant to enter the schema. No branch read carries a
parent, hierarchy or taxonomy field on a finding model; the parent relation exists only in the CSV
files. What `finding_cluster` means is declared in the README but never explained, and is populated
in one file only.

---

## B8. Convert and merge, with a fixed direction

**Idea.** Converting an outside definition set into finding models is a merge with a fixed direction:
incoming definitions merge into the existing corpus, never the reverse. A specificity guard prevents
matching an incoming specific term to a general existing model, so "tunneled catheter" must not match
"detectable hardware". Merge decisions are typed rather than ad hoc: enhanced, identical, subset,
needs review, and no similarities, each with its own action.

**Status.** Implemented example on a content branch, six of twenty-one planned chunks converted.

**Implemented.** A special case discards an incoming two-value presence attribute when the existing
model already carries the standard four values. The per-chunk flow is fixed — triage, convert, lint,
quality review, apply fixes, review file, human handoff, apply feedback — and the branch's own
instruction file says "User triggers one chunk at a time — never auto-run all 21 chunks."
`PROJECT_SPECIFICATION.md` parts 6 and 7, and `CLAUDE.md`, both `@ content/chestcts 0472a46`.

**Evidence.**
- The chest CT project specification — the direction rule, the specificity guard with its worked
  case, and the five merge-decision types. `PROJECT_SPECIFICATION.md @ content/chestcts 0472a46`
- The batch progress document and the conversion skill — the chunked workflow in practice.
  `docs/cdestaging_ct_chest_batch_progress.md` and
  `.claude/skills/finding-cdestaging-batch/SKILL.md @ content/chestcts 0472a46`

**Related.** A10, B4, B12.

**Undetermined.** How extracted sub-findings link back to their parents is named as an open design
problem on that branch: they are "identified and logged but not written to disk". No mechanism exists
on any branch read.

---

## B9. Content repository proposes changes upstream to the library

**Idea.** The content effort is treated as a source of requirements for the tooling, not only a
consumer of it. A document analyses what should move upstream into the library based on patterns
built while authoring, sizes each entry to become one issue, and states its evidence base as a
fourteen-model test batch plus a review pass plus three sessions of fragment refinement.

**Status.** Implemented example (the proposals document and one filed issue); working proposals (the
rest).

**Implemented.** The content repository carries a reference implementation of each proposal as a
local script, and the document points at it — direction-pair selection and article stripping are done
client-side in the content repo's creation script pending the library change.
`docs/plans/findingmodel-upstream-proposals.md @ taxonomy-export-2026-08-15 a30c3c9`, item B1.

**Evidence.**
- The upstream-proposals document — section A bugs (a release version-contract mismatch reproduced
  against published package versions) and section B library enhancements, each with a problem
  statement, an evidence count from the test batch, and a proposed interface.
  `docs/plans/findingmodel-upstream-proposals.md @ taxonomy-export-2026-08-15 a30c3c9`

**Related.** A6, B6.

---

# C. Foundation context and metadata

## C1. Lean published models versus the full metadata schema

**Idea.** The published finding model is deliberately lean — identifier, name, description, synonyms,
tags, attributes, index codes. A forward schema adds eight structured fields the team calls
foundation context: body regions, subspecialties, etiologies, entity type, applicable modalities,
expected time course, age profile, sex specificity. Four of these are presented in the team's own
webinar as what lets an agent judge whether a finding *should still be there* on a new exam: where it
is anatomically, what type of finding it is, how long it lasts, and whether it is transient or
permanent. The worked justification is that an aneurysm should be expected on every future exam and
tracked for growth, a resolved pulmonary embolism treated as gone, and an ovarian cyst known to clear
and recur with the cycle so that every cyst is not linked into one thread.

**Status.** Stated goal ("Definition formats, needs overhaul for increased metadata"); implemented
example on the work edge; explicitly labelled in the July 2026 webinar as "the forward, AI-populated
schema, not yet carried by the published definitions".

**Implemented.** All eight fields are typed Pydantic fields on both model classes on the development
and metadata branches, and absent from the released branch. The schema absorbs legacy vocabularies
rather than migrating data: normalizing validators map old title-cased regions, a legacy "ALL" value,
a coarse `traumatic` etiology, two film-modality codes, and a free-text "pediatric" age label onto
current values, with unknown values falling through to an ordinary enumeration error. Only entity
type is required; the rest may be null.
`packages/findingmodel/src/findingmodel/types/models.py` and `types/metadata.py @ feature/metadata-cleanup 1942b06`;
contrast `packages/findingmodel/src/findingmodel/finding_model.py @ main 75afd39`.

**Evidence.**
- "Canonical Structured Metadata and Enrichment Rewrite", "Canonical Model Shape" — the eight fields,
  the full value lists, and the stated goal of making metadata "canonical `FindingModel` state rather
  than disposable enrichment output", with the recorded reason that two earlier pathways both
  produced sidecar output instead.
  `docs/canonical-structured-metadata-and-enrichment-rewrite.md @ feature/metadata-cleanup 1942b06`
- "Finding Model Structured Metadata Fields" — the field-by-field reference with each enumeration and
  its meanings. `notes/oifm-metadata-fields.md @ next-gen-2026 44836c1`
- The webinar's "Lean vs full" and "Foundation card" slides — the framing, the four dimensions with
  their justification, and the etiology taxonomy on screen with a subdural hematoma carrying both a
  traumatic and a vascular code. `sources/bucket/text/ipl-webinar-deck.md`, slides 28 to 30
- The project lead's stated goals. `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`

**Related.** A5, C2, C3, C4, D2.

**Disagreements.** The entity-type value sets differ. The finding model enumeration keeps `grouping`
and `recommendation`; "What the Vocabulary Must Express" §5 drops both, on the grounds that a
recommendation has no subject in the patient and that grouping is a structural role rather than a
kind of finding, then reinstates Grouping as a node type. That document also removes `measurement` as
a classification in favour of a separate definition type.
`docs/next-gen-schema/01-what-the-vocabulary-must-express.md @ next-gen-2026 44836c1`. The subspecialty
and etiology enumerations also differ between the development and metadata branches: one code was
removed as "not an official RSNA specialty content code", another renamed, two added, and two new
parent etiology codes introduced, so data valid on one branch will not validate on the other.
`docs/metadata/subspecialties.md` and `CHANGELOG.md @ feature/metadata-cleanup 1942b06`.

**Undetermined.** Whether the eight fields will land on the released branch. The branch's readiness
assessment is recorded as not yet passing and nothing has been merged.

---

## C2. Each metadata field is defined by what it excludes

**Idea.** The metadata fields are specified less by what they mean than by the near-miss they must
not admit. Subspecialty is which radiology service would *read and report* the finding, not which
service *orders* the study, and the policy document lists what was deliberately kept out: modality
codes, education, policy, informatics, physics and research tracks, and radiation oncology, each with
a reason. Expected time course is how long a finding stays *visible on imaging*, "not the clinical
duration of the underlying disease". Sex specificity is about anatomy, not prevalence. Applicable
modalities covers only modalities routinely used to demonstrate, evaluate, quantify or follow the
finding, not theoretical detection or incidental visibility. Etiologies name the common process types
the finding implies, "not a differential diagnosis". Age profile separates what a finding *can occur
in* from what it is *more common in*.

**Status.** Working proposal (the policy); implemented example (the enumerations and the prompts that
apply them).

**Implemented.** The assignment prompts encode the exclusions as operational rules with defaults that
differ per field. The etiology and time-course prompt states that "The two fields have opposite
defaults. **Etiology defaults to null** — assign only with direct support from the finding name or
description. **Time course defaults to a committed value**", and orders the work: decide etiology
first, then use it when choosing time course. It forbids inferring cause from anatomy, modality,
appearance, age context or generic clinical association, and caps output at about three codes.
`packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/etiology_tempo.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The `etiology_tempo.md` assignment prompt — the goal statement, the opposite-defaults rule, the
  allowed code lists, and the specific negative rules (a nonspecific descriptive finding gets no
  benign/malignant differential; metabolic activity does not by itself imply neoplasm; calcified
  lymph nodes do not inherit lymphadenopathy's etiologies).
  `packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/etiology_tempo.md @ feature/metadata-cleanup 1942b06`
- The subspecialty policy document — the kept and not-kept tables with a reason per exclusion, and a
  tie-breaker between two overlapping codes.
  `docs/metadata/subspecialties.md @ feature/metadata-cleanup 1942b06`
- The field-standards document — about fifteen decision standards for modality applicability
  including three named negative rules, and the specific etiology adjudications.
  `docs/metadata/fields.md @ feature/metadata-cleanup 1942b06`
- The project vocabulary document — an "avoid" line under each domain term, for example ordering
  specialty under subspecialty and clinical disease duration under time course.
  `CONTEXT.md @ feature/metadata-cleanup 1942b06`

**Related.** C1, C3, C4.

**Disagreements.** None recorded.

---

## C3. Index codes must be exact

**Idea.** A code stored on a finding model must be an exact match or a clinically substitutable
near-equivalent for the whole model concept. Broader, narrower, related, complication-specific,
severity-specific and temporally qualified codes do not belong there unless the model itself is
defined at that narrower level; they belong in a separate review artifact where they can be
categorized. The code object stays a plain system, code and display triple, and relationship
semantics do not live on it — if the project later needs them, it should add a typed wrapper rather
than overload the existing object.

**Status.** Working proposal as policy; implemented as prompt rules and evaluation scoring, not as
schema enforcement.

**Implemented.** The ontology assignment prompt operationalizes the rule in both directions: reject a
candidate that *adds* unsupported detail (material, device subtype, location, named vessel, pattern,
disease context, benign or malignant status, histology, grade, stage) and reject one that *drops* a
meaningful modelled qualifier (patient group, pregnancy, timing, acuity, chronicity, severity,
location, modality, laterality, focality, pattern, composition). It adds that an unqualified tumour
includes benign and malignant forms, that a measurement or score used to evaluate a disease is not
the disease, and that non-canonical concepts should be preserved as review evidence with a
relationship and a rejection reason.
`packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/ontology_decision.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The `ontology_decision.md` assignment prompt — the rules above, and the instruction to return no
  canonical candidate when none is good enough.
  `packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/ontology_decision.md @ feature/metadata-cleanup 1942b06`
- "Canonical Structured Metadata and Enrichment Rewrite", index-code semantics — the policy with the
  do-not-overload instruction.
  `docs/canonical-structured-metadata-and-enrichment-rewrite.md @ feature/metadata-cleanup 1942b06`
- "Index code target fixture integration" — the measured consequence: adding missing source-code
  targets alone would have lifted index-code scoring only from about 0.674 to about 0.736, so
  coverage was necessary but not sufficient, and the four miss buckets are coverage, retrieval,
  matching and abstention.
  `docs/plans/index-code-target-fixture-integration-2026-06-23.md @ feature/metadata-cleanup 1942b06`

**Related.** C2, C5, E1, E2.

**Disagreements.** "Current Understanding" Issue J keeps open the option this rule closes: "index
codes as open system URIs, distinguishing exact-match from broader/narrower".
`docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`

**Undetermined.** Nothing enforces the rule at runtime. It is policy carried by prompts, review and
evaluation.

---

## C4. Focused assignment agents, advisory audit, and null as an answer

**Idea.** Metadata is assigned by seven narrow agents rather than one broad classifier — entity type,
etiology and tempo, patient applicability, subspecialty domain, modality applicability, ontology
decision, anatomy decision — each with a lean prompt and a typed decision output, assembled by one
orchestrator that never decides a field value itself. The recorded reason is that focused agents
allow concise prompts, per-field evaluation, and targeted tuning of weak fields; the recorded cost is
more agents, more orchestration, and more model calls per finding. Candidate discovery is a separate
role: search agents propose, assignment agents dispose. A final pass audits rather than enforces, and
the repository insists on calling it an auditor because "validators enforce structure; the auditor is
advisory". Null is a legitimate answer with four enumerated meanings, and scoring penalizes
unsupported additions more heavily than omissions.

**Status.** Working proposal recorded as an architecture decision; implemented on the work edge.

**Implemented.** Agents run in three parallel batches with etiology and tempo gated on entity type.
Candidate lists are capped and candidate identifiers use a system-and-code form the output validator
checks, retrying on invented identifiers. The auditor emits severity-tagged flags only, combining
deterministic checks (missing evidence, display mismatch against a cached preferred term,
anatomy-versus-sex conflicts) with an optional second-opinion pass. An ontology evidence cache
accumulates across runs and is explicitly "evidence only, never authority" when stale.
`docs/adr/0002-split-agent-assignment-architecture.md`,
`docs/metadata/enrichment/enrichment-agent-architecture.md`, and
`packages/findingmodel-ai/src/findingmodel_ai/metadata/ontology_cache.py @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The split-agent architecture decision record — the seven agents named, the decision, and its
  stated consequences. `docs/adr/0002-split-agent-assignment-architecture.md @ feature/metadata-cleanup 1942b06`
- The enrichment agent architecture document — the agent, prompt, output and evaluation table, and
  the search-proposes/assignment-disposes boundary.
  `docs/metadata/enrichment/enrichment-agent-architecture.md @ feature/metadata-cleanup 1942b06`
- The metadata README and evaluation document — "Unsupported additions are usually more harmful than
  omissions", the four meanings of null, conservative-abstention credit, and the separation of gates
  from quality scores. `docs/metadata/README.md` and `docs/metadata/enrichment/evaluation.md @ feature/metadata-cleanup 1942b06`
- The `anatomy_decision.md` assignment prompt — "Select the smallest candidate set that covers the
  modelled anatomic scope", the instruction that candidate support levels are evidence and not
  commands, and the rule to select no anatomic candidate at all rather than use a narrower child or
  landmark as a proxy.
  `packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts/anatomy_decision.md @ feature/metadata-cleanup 1942b06`

**Related.** C1, C2, C3, C5, E1.

**Disagreements.** The rewrite document records that two earlier enrichment pathways are to be removed
with no compatibility shims. That is a recorded reversal within the repository, not an open dispute.

---

## C5. Human review is the only authority

**Idea.** Generated metadata does not reach the corpus on its own. Review actions are approved,
skipped or feedback, and only approved records may be written back. Sub-agent triage may organize a
queue but is not authority, and generated source diffs are not gold. Feedback has four named routes —
human promotion, conversion into a general rule plus an evaluation, a source-model authoring fix, or
deferral — none of which write source directly.

**Status.** Stated as policy; implemented as gates and fixtures.

**Implemented.** Writeback runs through a command that verifies review-package and reviewed-payload
hashes, records before and after hashes, validates each model before writing, and refuses any record
not in the approved-output fixture; a refusal check against a feedback record returned a refusal, "the
intended authority boundary". A commit-time gate blocks source writeback unless about thirteen named
conditions hold, on the principle that "Source commits must be derived from the source-apply
manifest, not from `git diff`". A second gate blocks deleting the legacy code path until the new one
passes a real end-to-end run, with mocked unit tests explicitly not counting. Unapproved diffs are
quarantined rather than discarded.
`docs/metadata/enrichment/human-review-and-writeback.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The human review and writeback document — the three review actions, the feedback routing, the two
  gates, and the reconciliation of 180 review events over 150 unique records into a 78-definition
  source baseline. `docs/metadata/enrichment/human-review-and-writeback.md @ feature/metadata-cleanup 1942b06`
- The metadata enrichment plan history — the decisions stated as such: human review is authoritative;
  generated source diffs are not gold; feedback records must be dispositioned before another corpus
  batch. `docs/plans/metadata-enrichment-plan-history-2026-05-24.md @ findingmodels-metadata dcc6c4c`

**Related.** B5, C4, C7.

---

## C6. Documents record judgment; the schema is the specification

**Idea.** The metadata documents hold decisions and policy — field standards, subspecialty policy,
review gates, release strategy — while field types, patterns, the code object's shape and
normalization behaviour live in code and are read from code. The stated cause is that
hand-maintained structural documents drift, and that a prior consolidation lost and duplicated
exactly that kind of detail.

**Status.** Stated as an architecture decision.

**Implemented.** Enumeration value tables may appear in the field-standards document but are to be
generated or checked against the enumerations rather than hand-authored. The decision record's own
consequence section instructs a future reader who finds no field types in that document to look at
the models rather than re-add them.
`docs/adr/0001-lean-metadata-docs-schema-is-spec.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The lean-metadata-docs architecture decision record — the decision, its cause, and its two
  consequences. `docs/adr/0001-lean-metadata-docs-schema-is-spec.md @ feature/metadata-cleanup 1942b06`
- The project vocabulary document — system vocabulary separated from domain vocabulary, each term
  with an "avoid" line, plus a flagged-ambiguities section resolving prior collisions such as
  "tagging" against the tags field and "finding" meaning both the container and a classification
  value. `CONTEXT.md @ feature/metadata-cleanup 1942b06`

**Related.** B6, C2.

---

## C7. Two databases from one source commit

**Idea.** Publish two database artifacts built from the same enriched source: one in the legacy shape
readable by the currently published runtime, and one carrying the structured-metadata columns, the
enriched JSON, and a provenance table recording schema name and version, source commit, build
timestamp, package versions and embedding model. The stated reason is that existing consumers keep
working unchanged while metadata-aware consumers get the new data, rather than forcing a breaking
single-database migration.

**Status.** Stated as an architecture decision; partly implemented.

**Implemented.** A manifest key controls when the metadata-aware database becomes the default, and a
package-release gate moves the data-repository scripts off a local wheelhouse onto released package
pins before publication.
`docs/adr/0003-dual-db-pre-post-metadata-release.md` and
`docs/metadata/enrichment/database-artifacts-and-package-pinning.md @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- The dual-database architecture decision record — the decision, its reason, and its three
  consequences. `docs/adr/0003-dual-db-pre-post-metadata-release.md @ feature/metadata-cleanup 1942b06`
- "Schema Versioning (Future Work)" — the related and deferred idea, that a package version requires
  exactly one schema version and backward compatibility comes from the manifest keeping old-schema
  databases available, with schema version (structure) separated from content version (freshness).
  `tasks/schema-versioning-future.md @ main 75afd39`

**Related.** C5, E1.

---

## C8. Three retrieval modes over the corpus

**Idea.** The registry answers three different questions with three different mechanisms rather than
overloading one. Query-driven search combines full-text and vector retrieval with metadata filters
pushed into the query before ranking. Browse is filter-only with pagination, and explicitly replaces
an earlier overload where an empty search string carried tag filters. Related-model lookup is
deterministic with no language model, scoring metadata overlap with configurable weights.

**Status.** Implemented example on the development and metadata branches; absent from the released
branch.

**Implemented.** Related-model scoring weights anatomic location highest, then index code, then
entity type, then body region, etiology and subspecialty, then modality, age, sex and time course,
with a minimum score below which nothing is returned; the weights are recorded as "provisional and
must be tuned against a gold case set before release". Filters are OR within a facet and AND across
facets, while tags keep all-of semantics. A pre-authoring overlap check runs five phases — an exact
name and synonym fast path, model-assisted planning that emits alternate search terms and metadata
hypotheses, multi-pass candidate gathering, model-assisted selection with a rejection taxonomy, and
assembly — where deterministic code gathers and merges and the model only makes the edit-versus-create
judgment, with an unfiltered text path always preserved so a wrong facet guess cannot collapse
recall. The registry is also exposed to agents as a tool server.
`packages/findingmodel/src/findingmodel/index.py`,
`packages/findingmodel-ai/src/findingmodel_ai/search/similar.py`, and
`packages/findingmodel/src/findingmodel/mcp_server.py @ feature/metadata-cleanup 1942b06`.

**Evidence.**
- "Canonical Structured Metadata and Enrichment Rewrite", retrieval section — the three modes, the
  filter semantics, the weight table, and the provisional-weights caveat.
  `docs/canonical-structured-metadata-and-enrichment-rewrite.md @ feature/metadata-cleanup 1942b06`
- The similar-models planning prompt — "Prefer MORE GENERAL terms" and "NEVER more specific than the
  finding itself", the rule that keeps recall wide during candidate gathering.
  `packages/findingmodel-ai/src/findingmodel_ai/search/similar.py @ feature/metadata-cleanup 1942b06`

**Related.** B4, C1, E2.

---

# D. Anatomic locations

## D1. Spatial containment as a single-parent tree to the whole body

**Idea.** Every anatomic structure gets exactly one containing parent, defined as the smallest
anatomic entity that fully encloses it, so every entry has one unambiguous chain of enclosing regions
to a single root, the whole body. A structure spanning several subregions takes the smallest region
containing the whole of it, so the pancreatic duct is contained by the pancreas rather than by any
one of its parts. The purpose stated is deterministic, auditable traversal: software that extracts "3
mm cyst in the pancreatic tail" has no representation of the pancreas, the retroperitoneum and the
abdomen to consult, and this supplies one.

**Status.** Implemented example.

**Implemented.** The shipped index data is a strict rooted tree with a single self-referencing root
and no multi-parent entries. The libraries walk it: ancestors terminate at the hard-coded whole-body
identifier, and a containment predicate answers whether one structure lies inside another. The
current package exposes the same traversal from a command line, printing the chain from whole body
down to a named structure with its children.
`body_part_index/body_part.py @ BodyPartIndex.py main 388ae0a`;
`docs/anatomic-locations.md @ findingmodel feature/metadata-cleanup 1942b06`.

**Evidence.**
- The Anatomic Locations Index manuscript under review at JDIM, Methods "Hierarchy construction" and
  Results "Hierarchy structure" — the single-parent rule, the smallest-fully-containing-region rule
  with the pancreatic duct case, verification that every chain reaches the root, a longest chain of
  seven hops, and a depth distribution consistent with whole body to major region to subregion to
  structure. `sources/bucket/text/jdim-02183.md`
- The project site's homepage — "a directed, rooted tree hierarchy, starting from the whole body and
  ramifying through body regions", with the curated set described as "Complete-ish" and
  "Non-degenerate: no uncertainty as to which node represents a structure".
  `docs/index.markdown @ anatomiclocations.org main 1f39fa4`
- "Current Understanding" §2.6 — independent verification against the data file on 2026-07-28:
  strict rooted tree, single root, every node exactly one containing parent, no multi-parent entries
  anywhere. `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`
- The anatomic locations research task — the traversal chosen for the current database is an
  adjacency list with recursive queries and an explicit depth limit "to prevent infinite loops in case
  of data errors", judged optimal for a read-only hierarchy of this size.
  `tasks/anatomic-locations-graph-research.md @ findingmodel main 75afd39`

**Related.** D2, D3, D5, D6, F1.

**Disagreements.** The manuscript records the cost of the single-parent rule as a limitation: a
structure spanning sibling subregions is assigned to their common parent, so the pancreatic duct's
course through the individual subdivisions is not represented. It also records that the hierarchy
uses deliberately coarse regional grouping. The next-generation gap log notes that the data places
the lung inside the pleural space, "an anatomic oddity that affects containment traversal".

**Undetermined.** Three node counts coexist across sources — 2,890 in the published file, 2,891 in
the manuscript, 2,926 in the current package data — because they were read from different releases.
That is freshness, not disagreement.

---

## D2. Containment and part-of are different relations

**Idea.** Where a structure physically sits and what functional structure it belongs to are two
different questions, and conflating them breaks spatial reasoning. The abdominal aorta is contained
by the retroperitoneum but is part of the aorta; the aortic arch is contained by the mediastinum but
is part of the aorta; the appendix is contained by the pelvis but is part of the colon. The
single-parent constraint applies only to containment; a structure may have zero, one or more
functional part-of associations. Anything walking the hierarchy must declare which relation it means,
because for the upper lobe of the right lung containment yields right lung, thorax, whole body while
part-of yields right lung and stops.

**Status.** Implemented example.

**Implemented.** The two relations are separate fields, one required and one optional, and the
authoring guidance tells a curator which to use: containment for "X is inside Y" (the hilum is inside
the lung), part-of for "X is a component of Y" (the stomach is part of the gastrointestinal tract).
The older TypeScript library mirrors the containment traversal for the functional hierarchy with its
own ancestor, child and predicate functions; the Python library exposes only a single part-of hop.
`.claude/skills/manage-anatomic-locations/reference/json-schema.md @ findingmodel main 75afd39`;
`README.md @ BodyPartIndex.ts main dec578e`; `body_part_index/body_part.py @ BodyPartIndex.py main 388ae0a`.

**Evidence.**
- The anatomic locations field reference, "containedByRef vs partOfRef" — the spatial-versus-
  mereological distinction with worked cases and the note that many entries have both.
  `.claude/skills/manage-anatomic-locations/reference/json-schema.md @ findingmodel main 75afd39`
- The project site's code page — the same two hierarchies named and illustrated, kidney in the
  retroperitoneum against adnexa as part of a system.
  `docs/code.markdown @ anatomiclocations.org main 1f39fa4`
- The Anatomic Locations Index manuscript, Methods "Hierarchy construction" and Results "Index
  composition" — the distinction with the abdominal aorta case, and 991 functional links each tying a
  structure to a system. `sources/bucket/text/jdim-02183.md`
- "Current Understanding" §2.6 — a three-row worked table and the statement that the two traversals
  answer different questions. `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`

**Related.** D1, D6, F1.

**Disagreements.** Which hierarchy a given check walks is an open item that "must be stated each
time". `docs/next-gen-schema/11-anatomy-axis.md @ next-gen-2026 44836c1`

---

## D3. Laterality as explicit triads

**Idea.** Left, right and unsided variants of a bilateral structure are three distinct entries joined
by explicit links, rather than one entry plus a modifier. The stated reason is an implementation
convenience: the links permit direct deterministic navigation among corresponding forms without
reconstructing or searching for a post-coordinated expression at runtime. The consequence drawn in
the next-generation vocabulary is that laterality is carried by the location, so there will be no
laterality data elements.

**Status.** Implemented example; working proposal for the consequence.

**Implemented.** The curation rule is a three-entry pattern: an unsided entry carrying links to both
sided variants, and each sided entry carrying a link to its counterpart and back to the unsided form,
with the sided entry's container pointing at the sided version of its container where one exists. The
libraries navigate this in both directions from either end. Where a lateralized code does not exist
in an external terminology, the guidance is to use the unsided code for all three entries and say so
in the change description.
`.claude/skills/manage-anatomic-locations/reference/laterality-conventions.md @ findingmodel main 75afd39`;
`README.md @ BodyPartIndex.py main 388ae0a`.

**Evidence.**
- The laterality conventions reference — the compound identifier pattern using two modifier
  identifiers, the three-entry pattern with a worked example, and the container rule.
  `.claude/skills/manage-anatomic-locations/reference/laterality-conventions.md @ findingmodel main 75afd39`
- The Anatomic Locations Index manuscript, Methods "Cross-referencing and technical implementation" —
  complete triads for all 795 bilateral structures with the implementation-convenience reason stated.
  `sources/bucket/text/jdim-02183.md`
- "Current Understanding" §2.6 — "Laterality is carried by the location, not by a DataElement.
  Accordingly there will be no laterality DataElements", superseding an earlier committee draft
  element list. `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`

**Related.** D1, D4, F1.

**Disagreements.** An external reviewer's alpha implementation offers a laterality data element
including a bilateral value, against the sided-location approach; recorded as decision area ST08.
`docs/next-gen-schema/12-alpha-structural-comparison.md @ next-gen-2026 44836c1`

---

## D4. Synthetic post-coordinated terms

**Idea.** Where a clinically routine localization concept has no pre-coordinated term — almost always
because laterality or enumeration is missing — an identifier is minted by joining existing RadLex
identifiers with an underscore, so the composition is transparent and machine-readable. Three
patterns account for all of them: laterality only, enumeration only, and enumeration plus laterality.

**Status.** Implemented example.

**Implemented.** The identifier pattern in the published schema admits arbitrarily many joined
identifiers, and 1,010 of 2,890 shipped entries carry a composite identifier.
`data/body_parts_schema.json` and `data/body_parts.json @ anatomiclocations.org main 1f39fa4`.

**Evidence.**
- The Anatomic Locations Index manuscript, Methods "Synthetic term generation" — the three patterns
  with worked identifiers and counts, and the Discussion caveat that the count should not be read as
  evidence that established ontologies lack mechanisms for adding concepts, because these gaps are
  specific to one lexicon and do not generalise. `sources/bucket/text/jdim-02183.md`
- The laterality conventions reference — the modifier identifiers and the compound form as a curation
  rule rather than a description.
  `.claude/skills/manage-anatomic-locations/reference/laterality-conventions.md @ findingmodel main 75afd39`
- "The Anatomy Axis, Current State" §1 — the compound identifiers named as "the exception the RadLex
  track will remove by minting real ids".
  `docs/next-gen-schema/11-anatomy-axis.md @ next-gen-2026 44836c1`

**Related.** D1, D3, D6.

**Disagreements.** The manuscript records the cost as a limitation: systems built on the underlying
lexicon will not recognize compound identifiers without an added mapping layer.

---

## D5. Measuring what existing ontologies actually populate

**Idea.** Rather than asserting qualitatively that existing ontologies are unsuitable, measure how
completely each one populates the containment or part-whole relation it declares, each against its
own anatomy term set so that no resource is penalized for covering more or less anatomy. The reported
result is that in none of the three can software start at a structure and follow the declared
relations up to a whole-body class. The stated interpretation is not that the resources are defective
but that none was built to answer what encloses the structures radiologists name.

**Status.** Implemented example (a reproducible measurement); under review, not published.

**Implemented.** The measurement is specified to be recomputable: each count derives from a named
relation and a stated term set, with per-resource derivations given in supplementary methods, and a
best-case re-measurement pools every declared relation plus subproperty and inverse forms and repeats
the analysis. `sources/bucket/text/jdim-02183.md`, Methods.

**Evidence.**
- The Anatomic Locations Index manuscript, Methods "Measuring containment in existing resources" and
  Results — the method, the pooled best case, and the finding that nearly half of one resource's
  anatomy concepts have more than one taxonomic parent so that following it branches rather than
  yielding a single chain. `sources/bucket/text/jdim-02183.md`
- The project site's homepage, Introduction — the earlier qualitative version of the same argument:
  lack of desired terms, too many unnecessary or degenerate terms, limited anatomic organization.
  `docs/index.markdown @ anatomiclocations.org main 1f39fa4`

**Related.** D1, D6, F2.

**Disagreements.** The webinar compresses the result into a ratio, "11.5× the containment coverage of
RadLex", which appears in no other source in that form.
`sources/bucket/text/ipl-webinar-deck.md`, slide 31

**Undetermined.** The manuscript states plainly that the study does not measure downstream utility:
no benchmark, user study or deployment demonstrates that the hierarchy improves retrieval, tagging,
labeling or correlation. It asks to be read as a descriptive resource paper.

---

## D6. An overlay on RadLex, not a competitor

**Idea.** The curated set began outside RadLex because RadLex lacked the coverage and structure
imaging needed, but was keyed to RadLex identifiers throughout, and its relationship is now stated as
an overlay: RadLex concepts and predicates sit underneath, and the file adds identifiers RadLex lacks,
its own containment and part-of hierarchies, and laterality. It is described as the basis of the
RadLex anatomy axis going forward because the RadLex anatomy track is editing it, with aiming at the
published release compared to editing a three-year-old version of a document others have been
editing. A location's identifier is its RadLex identifier, and a RadLex code is never shown beside a
location because the location code *is* the RadLex code.

**Status.** Stated goal ("this will be blended in with RadLex"); working proposal recorded as agreed
on 2026-09-13; incorporation in progress.

**Implemented.** The current package data is pointed to at a pinned commit rather than copied. The
gap between what the file has and what it lacks is tracked as a running list of specific node
requests fed upstream — lung parenchyma, perirenal space and its sided forms, pericardial space,
subarachnoid space, and real identifiers for the compound sided variants.
`docs/next-gen-schema/11-anatomy-axis.md` and `docs/next-gen-schema/04-anatomy-gaps.md @ next-gen-2026 44836c1`.

**Evidence.**
- "The Anatomy Axis, Current State" §1 and §4 — the overlay statement dated 13 September 2026, the
  three-year-old-document argument, and a dated record of what was agreed on three occasions.
  `docs/next-gen-schema/11-anatomy-axis.md @ next-gen-2026 44836c1`
- "Current Understanding" §2.6 — "It is now a subproject of RadLex and is imminently becoming an
  identified collection within RadLex itself", with the synthetic nodes expected to receive real
  identifiers. `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`
- The Anatomic Locations Index manuscript, Discussion, future work — incorporation by the RSNA RadLex
  Committee described as underway, covering the terms themselves, with the note that a prospective
  process for revising and periodically reviewing the hierarchy still needs to be defined.
  `sources/bucket/text/jdim-02183.md`

**Related.** D4, D5, D7, F2.

**Disagreements.** An external reviewer's alpha extracts a RadLex subset with local wrappers where the
agreed substrate is the pinned overlay; recorded as decision area ST06.
`docs/next-gen-schema/12-alpha-structural-comparison.md @ next-gen-2026 44836c1`

---

## D7. The missing is-a and structure-type layer

**Idea.** The curated set has containment and part-of but no taxonomic relation and no structure-type
nodes, so a statement like "this finding applies to tendons" cannot be made. This is recorded as the
major shortcoming and the first thing to resolve. RadLex can supply a first layer without inventing
anything, because every plain-identifier location has a taxonomic chain in the published ontology,
yielding several hundred locations under each of muscle, artery, vein, tendon and bone. Two cautions
accompany it: the ontology's own release note warns that some taxonomic categorizations were
converted from part-of and may be wrong, and the deep formal chain is not the clinically useful
layer.

**Status.** Working proposal (a derived, pinned overlay handed to the anatomy track); stated goal
(two scope families to develop).

**Implemented.** The second-generation record model on an unmerged content branch already carries
taxonomic identifiers alongside new relations for vascular structure — branch-of and flows-to — on
several hundred records, so the shape has been tried as data even though it was never merged.
`updates/ @ anatomiclocations.org content_work 35624d7`.

**Evidence.**
- "The Anatomy Axis, Current State" §2, §3 and §5 — the has-and-lacks table, the derived
  structure-type counts with both cautions, and the two scope families (tissue types and structure
  types) with their connections to the location hierarchy explicitly still open.
  `docs/next-gen-schema/11-anatomy-axis.md @ next-gen-2026 44836c1`
- The anatomy gap log — the running node-request list and the coverage figures behind it.
  `docs/next-gen-schema/04-anatomy-gaps.md @ next-gen-2026 44836c1`

**Related.** D6, F1, F2.

**Disagreements.** The anatomy axis document separates the project lead's two scope families from
"exploratory ideas from the assistant, not adopted".

**Undetermined.** Whether the second-generation per-file record model was adopted, rejected, or
superseded. Its field vocabulary differs from the published schema on nearly every field and its
naming is internally inconsistent; there is no design note. Several of its fields do reappear in the
current package's field reference, including a region field and an ACR Common identifier, which the
reference documents but does not explain the provenance of.

---

## D8. Curation rules that make the codes usable

**Idea.** The value of the index is less the terms than the discipline of the mappings, and the
curation rules are written down. External anatomy coding uses one member of a three-concept family:
the "Structure of ..." concept always, never the "Entire ..." or "... part" forms, because the
structure concept is what the terminology intends for finding sites and procedure sites. Definitions
prefer authoritative sources in a stated order. Synonyms are the clinical shorthand radiologists
actually use.

**Status.** Implemented example (a curation rule applied by a skill with validation scripts).

**Implemented.** The management skill ships a lookup script, a sampling script and a validation
script beside the field reference, so a curator adding entries checks candidate codes and validates
the result rather than hand-editing.
`.claude/skills/manage-anatomic-locations/scripts/ @ findingmodel main 75afd39`.

**Evidence.**
- The anatomic locations field reference, "SNOMED Coding Guidance — The SEP Triad" — the three
  concept types with an always/never/never instruction and the reason; and the fallback rule when a
  lateralized code does not exist.
  `.claude/skills/manage-anatomic-locations/reference/json-schema.md @ findingmodel main 75afd39`
- The same reference, text fields — the region value list and the ranked preference for definition
  sources.

**Related.** D3, D6, F2.

---

## D9. A reference layer, not a labeling algorithm

**Idea.** The index is a reference and normalization layer, not an automatic labeling system.
Identifiers may be applied at exam or series level to describe anatomy covered, or at report or
finding level to represent where an observation is. Labels may be generated by rules, language
processing or AI and then normalized, but whatever route generates a label, a person or a downstream
check confirms the assigned structure before anything relies on it. Containment then supplies the
broader context without further annotation. The team is explicit that localization is only one
dimension: knowing where a finding is does not establish what kind of process it is, how long it has
been present, whether it is transient, or whether it is the same lesion recorded elsewhere.

**Status.** Stated goal; implemented example of the roll-up.

**Implemented.** Every finding is anchored to a specific location code and the containment hierarchy
rolls it up to a top-level body region, so a patient is presented as an anatomy dashboard organized
by where findings are rather than by which report they came from. The demonstrated viewer shows the
gap honestly, with a banner admitting two findings have no specific anatomic location.
`sources/bucket/text/ipl-webinar-deck.md`, slides 31 and 33.

**Evidence.**
- The Anatomic Locations Index manuscript, Discussion — the reference-layer statement, the
  confirm-before-relying rule, the roll-up example, and the explicit one-dimension limit.
  `sources/bucket/text/jdim-02183.md`
- The anatomic location assignment rules — the three-step precedence ladder used by the extraction
  platform: explicit anatomy in the text, then the finding's own target organ, then the exam-scoped
  coarse region, with laterality following the same shape.
  `knowledge/data-structures/anatomic-location-assignment-rules.md`

**Related.** C1, D1, E2.

**Disagreements.** None recorded. The webinar's four foundation-context dimensions are the team's own
answer to the one-dimension limit the manuscript states.

---

# E. Exam types

## E1. Preferred high-level exam entries over the Playbook

**Idea.** Exam types should be a thin wrapper over an existing governed knowledge graph — the
LOINC/RSNA Radiology Playbook together with RadLex — rather than a new vocabulary. What the wrapper
adds is a set of *preferred* high-level entries at the granularity clinicians and systems use, such
as CT Chest, MRI Brain and X-ray Knee, marked as preferred among the many codes describing variants
of the same study. The idea is four years old in nearly the same words.

**Status.** Stated goal only, restated across four years and three documents. No artifact exists.

**Implemented.** Nothing models exams, studies, procedures or protocols in the finding model
repositories; there is no exam-type entity and no exam-to-finding relationship. Exam identity does
real work in the extraction platform only as a bare code in an exam header and as the bottom rung of
the anatomy precedence ladder.
`knowledge/semantic-foundation/exam-types/existing-building-blocks.md`.

**Evidence.**
- The project lead's stated goals — "Needs wrapper tooling around the knowledge graph represented by
  RadLex LOINC playbook" and "Need to define the PREFERRED high-level entries".
  `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`
- The project site's roadmap — a companion for exam types based on Playbook exam definitions, listed
  under content tasks and unchanged since January 2023.
  `docs/index.markdown @ anatomiclocations.org main 1f39fa4`
- The "Common Anatomic Locations" board, "Active Issues" box — exam type definitions of the most
  common exams based on LOINC with common identifiers, listed as an active issue beside the anatomy
  work. `sources/excalidraw-diagrams.md`
- "Product direction: an agent-ready medical terminology graph gateway" — the only written design: a
  radiology domain profile in which "orderables live in the LOINC/RSNA Radiology Playbook, while
  findings, anatomy, and report language live in RadLex", with Playbook-weighted ranking, legacy
  identifier detection, and taught crosswalk correspondences. Recommended direction, not built.
  `docs/product-roadmap.md @ med-ontology-lookup main a1fd3ae`
- The chest CT coverage roadmap — an earlier, cruder form of the same coupling: a per-exam finding
  table with frequency, priority, a RadElement set link where one exists, and a RadLex identifier
  column. `definitions/upmedic/roadmap.md @ CDEStaging main b814a10`

**Related.** B7, D9, E2, F1.

**Undetermined.** Nothing found states why the exam-type library was never built while the anatomic
location library was.

---

## E2. Exam-to-anatomy inclusion edges and the imaging region

**Idea.** What makes an exam type more than a code list is typed edges to the anatomy it covers,
distinguishing anatomy that is *always* included, which may be expressed as a hierarchy rather than a
flat list, anatomy that is *usually* included for edge cases, and anatomy that is *possibly* included
and would have to be checked. The 2024 board states the same requirement as defining an imaging
region: a CT chest region contains the chest but also what a radiology exam of the chest would
include, such as the lower neck, the upper abdomen and the shoulders. The 2023 roadmap puts it as
exam definitions specifying all *included* body parts.

**Status.** Stated goal only. No artifact.

**Implemented.** Nothing. The nearest running behaviour is the finding-scope rule applied by
judgment: a finding model's scope should match what is assessable on a given exam type, which is why
"chest wall fracture" and "upper abdominal abnormality" exist as models. Nothing checks a model's
scope against a coded exam type, because there is nothing to check against.
`prompts/fragments/scope_and_specificity.md @ findingmodels taxonomy-export-2026-08-15 a30c3c9`.

**Evidence.**
- The project lead's stated goals — the three edge kinds named, with the hierarchy note on "always
  included". `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`
- The "Common Anatomic Locations" board, "Exam Types" box — the imaging-region definition with the
  lower-neck, upper-abdomen and shoulders example. `sources/excalidraw-diagrams.md`
- The Anatomic Locations Index manuscript, Discussion — the same capability named from the other
  side, as something the index does not supply: relating a finding's location to what an exam covers
  would additionally require a model of scan-protocol coverage. The use case it would serve,
  identifying relevant prior studies covering overlapping anatomy even when acquired for different
  purposes, is stated in the same section. `sources/bucket/text/jdim-02183.md`

**Related.** A4, D1, D9, E1.

**Undetermined.** Whether "always / usually / possibly" means three edge types, one edge with a
strength property, or something else. The goal statement does not say. The strength-bearing guidance
model in F1 is a different mechanism for a different purpose.

---

# F. The next-generation vocabulary and the terminologies

## F1. Anatomic scope, not location

**Idea.** The vocabulary owes each finding class a statement of which anatomic locations are
congruent with it, and calling that field "location" is wrong because the statement ranges over three
different kinds of thing and only two are spatial: a named structure checked by identity or descent,
a region checked by containment, and a *structure type* such as arteries or tendons checked
taxonomically, "not spatial at all" — tendons are scattered across the body and share no common
container. Guidance is not a location: a clavicle fracture class records the clavicle while an actual
fracture is at the left clavicle. Guidance also varies in strength, from definitional through very
weak to not anatomic at all, so it records its strength. A companion idea removes the need for a
finding class in a whole category of reporting: a location can bind directly to data elements and
measurements, so describing normal anatomy — bile duct calibre, ovarian volume, endometrial thickness
— needs no finding class at all, and a binding on the unsided organ is satisfied by an observation on
a sided one without copying the edge.

**Status.** Working proposal, with several parts recorded as owner decisions and explicitly not
jointly settled.

**Implemented.** Scope resolution works today by plain traversal against the anatomy data for two of
the three kinds; the third waits on the missing taxonomic relation (D7). Worked location and element
examples are committed as data.
`docs/next-gen-schema/examples/common-bile-duct.location.json @ next-gen-2026 44836c1`.

**Evidence.**
- "What the Vocabulary Must Express" §2 — the three kinds with how each is checked, the
  guidance-is-not-a-location distinction, and §2.1's list of places that are not structures
  (potential spaces, cavities, zones, interfaces, positions relative to a landmark) with the warning
  that a vocabulary unable to express them will see authors invent ungrounded value sets again.
  `docs/next-gen-schema/01-what-the-vocabulary-must-express.md @ next-gen-2026 44836c1`
- The same document §2.3 — the strength table from definitional (pulmonary nodule in lung) through
  very weak (metastasis) to not anatomic (free air, "air where air should not be").
- The same document §3 and §3.1 — the breadth argument that finding classes must cover more than
  abnormalities, and the direct-binding decision for normal structures with what it buys and what it
  requires.

**Related.** D1, D2, D7, F3.

**Disagreements.** Recorded as decision areas ST07 and ST08 against an external reviewer's alpha,
where scope kinds and the laterality treatment differ across code paths. Whether guidance records
which kind it is, and how binding it is, remain open as Issue H.
`docs/next-gen-schema/12-alpha-structural-comparison.md` and
`docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`

---

## F2. Terminology roles, and search recall as the gate

**Idea.** Each terminology has a stated role. RadLex is the foundation for findings, anatomy and
report language, chosen for coverage at the granularity radiologists report, governance with a
defined pathway for contributing terms back, and stable identifiers. SNOMED CT is the cross-reference
for enterprise coding, and is what DICOM's anatomic region sequence and FHIR's body-site value sets
already bind to, so the index sits above the coding scheme rather than competing with it and adoption
proceeds through existing bindings. LOINC and the Playbook own orderables. A connected idea concerns
search quality: a lookup that fails silently is worse than one that fails loudly, because an agent
then concludes the concept is missing and proposes a duplicate. The stated target is "recall good
enough that a MISS is real evidence of an ontology gap rather than evidence of unlucky phrasing."

**Status.** Implemented example (the cross-references, the search rework, the lookup gateway); stated
goal (the interoperability-through-existing-bindings argument).

**Implemented.** Search keeps exact label and synonym tiers as the *confidence* signal and adds
full-text relevance ranking as the *recall* layer, emitting a categorical match type rather than a
score because scores are not comparable across queries, with a per-query relative cutoff. A tokenizer
override was required because the default deletes every digit at index and query time, which matters
for vertebral levels, assessment categories, sequence weightings and isotopes. A measured evaluation
compared three arms and concluded that the exact tier earns its place on confidence rather than
ranking, so "the original metric was the flawed part, not the design". The terminology gateway
queries each ontology separately and interleaves results so the largest source cannot hide the
others, resolves a term, code or concept identifier by auto-detecting its shape, and uses medical
shorthand rather than raw type codes in its filters.
`docs/plans/hybrid-fts-search.md @ RadLex experiment/kg-radlex-parsing 5162a65`;
`README.md` and `src/med_ontology_lookup/ @ med-ontology-lookup issue-3-typed-provider-failures 9cc3eec`.

**Evidence.**
- "Hybrid FTS search" — the false-gap failure mode named as the worst one the project has, the
  alphabetical-ranking example, the design, the tokenizer finding with its measured share of affected
  labels, and the evaluation with its own correction.
  `docs/plans/hybrid-fts-search.md @ RadLex experiment/kg-radlex-parsing 5162a65`
- The Anatomic Locations Index manuscript, Methods "Term selection" and Discussion — why RadLex was
  chosen as the foundation, the recommendation of SNOMED CT for enterprise coding and the distinction
  between filling a coding role and populating containment, and the DICOM and FHIR binding argument.
  `sources/bucket/text/jdim-02183.md`
- "RadLex baseline" — direct verification against the published ontology, including that its external
  references run through one untyped string property dominated by one source and that SNOMED mapping
  is effectively absent, contradicting a committee assumption.
  `docs/next-gen-schema/05-radlex-baseline.md @ next-gen-2026 44836c1`
- "Product direction: an agent-ready medical terminology graph gateway" — the stated boundary that
  this is a gateway and not a terminology source, the explicit non-goals, and the insistence that a
  shared concept identifier "is evidence of connection, not proof of exact equivalence".
  `docs/product-roadmap.md @ med-ontology-lookup main a1fd3ae`
- The project review and proposal — typed provider failures with a reproduced authentication failure
  silently converted into an empty result, and the requirement that a collection result distinguish
  complete, partial, failed and capped outcomes because "A plain list cannot communicate whether it
  is complete". `docs/project-review-and-proposal.md @ med-ontology-lookup docs/reviewed-proposal-backlog f059792`

**Related.** C3, D5, D6, E1.

**Disagreements.** The manuscript treats SNOMED CT as the enterprise coding target to cross-reference;
the next-generation vocabulary treats RadLex as the thing to stay close to and treats the SNOMED
mapping gap inside RadLex as a problem to work around.

---

## F3. Contributing terms back, and the two-phase proposal loop

**Idea.** Gaps found while using a terminology are fed back to it rather than patched locally. An
agent reads a report, searches the graph, confirms each hit, redirects obsolete concepts to their
replacements, and decides whether each term is genuinely present — "a loose keyword overlap is not
enough, and a broader or related concept does not count as a match". For each unmatched term it then
proposes a new concept with the closest existing parent, a precise term, a rationale for why this is
a genuine gap and why that parent is the closest fit, and optional typed relationships, under the
rule "Only include a relationship if you found a real existing RID for the other end of it; do not
guess a RID."

**Status.** Implemented example (the mechanism); the corresponding curation gate exists separately.

**Implemented.** Proposals are validated against the graph before being appended: unknown
identifiers, unused relation types and blank names or rationales are rejected, and the whole batch
fails together because the output file is append-only and a candidate pointing at an invented
identifier cannot be reviewed. On the ontology side, every push runs a reasoner consistency check and
report checks, catching inconsistent logic and accidental duplicate or merged terms before they land.
`.claude/skills/radlex-concepts/SKILL.md @ RadLex experiment/kg-radlex-parsing 5162a65`;
`docs/TESTING.md @ RadLex main 13a5abe`.

**Evidence.**
- The extract-concepts and suggest-concepts skill documents — the two phases with their acceptance
  rules and the no-guessed-identifier constraint.
  `.pi/skills/extract-radlex-concepts.md` and `.pi/skills/suggest-new-concepts.md @ RadLex experiment/kg-radlex-parsing 5162a65`
- The ontology testing document — the continuous-integration checks and what they are meant to catch.
  `docs/TESTING.md @ RadLex main 13a5abe`
- The Anatomic Locations Index manuscript, Methods "Term selection" — a defined pathway for
  contributing terms back named as one of three reasons the lexicon was chosen as the foundation.
  `sources/bucket/text/jdim-02183.md`

**Related.** D6, D7, F2.

**Undetermined.** Whether any proposed concepts were actually submitted. The candidate output file is
excluded from version control and absent; the repositories describe the proposal mechanism and the
curation gate but nothing connects the two.

---

## F4. The finding model relationship registry

**Idea.** The finding model source schema draft proposes that a model store only the relationship
assertions authored on it, with authors never maintaining both sides of an inverse pair, and tooling
deriving inverse and symmetric views from a checked-in registry in which each relationship type
declares whether it is inverse-backed, symmetric, or one-way. The same draft separates a *source*
model, which may refer to a canonical shared attribute file instead of redefining presence and change
from prior inline, from a *hydrated* model in which those references are expanded, with runtime
operating on the hydrated form. Governance moves to per-model history sidecars recording who or what
acted.

**Status.** Working proposal only.

**Implemented.** Nothing. The relationship registry exists only in the draft; the live corpus
implements no relationship mechanism at all. The one relationship-shaped construct that does exist in
the corpus is the associated-findings attribute (A10), which references other models by name rather
than by identifier.

**Evidence.**
- "FindingModel Source Schema v2 Draft" — the source-versus-hydrated distinction, canonical attribute
  reuse with the two permitted overrides, the relationship-authorship rule, the registry semantics
  with three worked pairs, and the corpus layout placing models, attributes and registries side by
  side. `notes/oifm-schema-v2-draft.md @ next-gen-2026 44836c1`
- "The Finding and Diagnosis Relationship Family" §6 — the correction recording that this registry
  exists only in the draft and that the live repository implements nothing, verified against the
  repository on 2026-09-01, which makes the finding model work "a potential consumer of this family
  rather than prior art to reconcile with".
  `docs/next-gen-schema/07-relationship-family.md @ next-gen-2026 44836c1`

**Related.** A10, B1, F5.

**Disagreements.** The two designs differ on shared attributes. The draft allows a model to reference
a canonical attribute; the graph design makes a shared element one node with one identity, and
"Current Understanding" §5.1 names the file-based copy-on-reference choice as the reason bringing
models over is "a review step, not a bulk import".

**Undetermined.** Whether this draft is live. It is dated April 2026 and nothing in the finding model
repositories implements it.

---

## F5. The relationship family and the derived differential

**Idea.** Seven relationship pairs plus a catch-all connect finding classes and diagnoses, with
manifestation and causation kept strictly apart: a striated nephrogram *is* pyelonephritis appearing
on imaging, while a renal abscess is a distinct second entity pyelonephritis produced. The test
offered is whether a clinician would say the source "got better" or that "a complication resolved".
Manifestation edges carry two optional independent properties, a typicality scale adopted verbatim
from an existing phenotype-frequency standard with its percentage anchors, and a three-value
specificity scale omitted entirely when uninformative because an absent property means no judgment
was recorded. The differential is not an edge type at all but a derived view: the diagnoses reachable
over the manifestation inverse, filtered by context and ranked. A missing edge between habitually
confused diagnoses means a finding class is missing, not that a workaround edge is needed. A report
edge and a class edge are different assertions, which forces a vocabulary relationship to have
identity of its own so a report edge can cite the potential it expresses.

**Status.** Working proposal, explicitly tentative and non-comprehensive; implemented at prototype
scale.

**Implemented.** The worked pyelonephritis and pleural effusion families exist as committed graph
data and as generated diagrams, and the September 2026 deck renders one report's six observations
against their class definitions, showing report-plane edges as a separate family from class edges.
`docs/next-gen-schema/graph/pyelonephritis.jsonl` and `docs/next-gen-schema/examples/ @ next-gen-2026 44836c1`;
`sources/bucket/REPORT.md` §6.

**Evidence.**
- "The Finding and Diagnosis Relationship Family" §1 to §6 — the family table with domains and
  ranges, the manifestation-versus-causation test, the two property scales with their sources and the
  reason one takes a numeric escape hatch and the other does not, the derived-differential argument
  with its precedent, and the prior-art anchor table.
  `docs/next-gen-schema/07-relationship-family.md @ next-gen-2026 44836c1`
- "Current Understanding" §1.3 — the two-level argument and the identity consequence.
  `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`
- "The Mat and the Tree" §2.3 — the display specification's card frame, whose bottom row carries
  exactly the foundation-context axes of C1: modality, region, subspecialty, sex, age, course,
  etiology. `docs/next-gen-schema/09-mat-and-tree.md @ next-gen-2026 44836c1`

**Related.** A9, C1, F1, F4.

**Disagreements.** Recorded within the document: the negative typicality value "sits oddly" on an edge
named for manifestation and the alternative of a separate negative edge type is flagged; whether the
causal pair also takes typicality is left open. A separate two-sided fork is recorded as undecided:
an external reviewer's engineering memo recommends a condition on the edge where an existing element
value controls a relationship's applicability, reserving subtyping for independently meaningful class
identity, while the project lead's counter-proposal is subtype classes. The memo carries its own
warning that reading only it gives a one-sided picture.
`notes/conditional-relationships-memo.md @ next-gen-2026 44836c1`

---

## F6. Measurement, method, and interpretation are three things

**Idea.** "Peak systolic velocity is 350 cm/s" and "this represents hemodynamically significant
stenosis" are two assertions with different truth conditions, different provenance, and different
failure modes. The stated reason for keeping them apart is durability: thresholds move while
measurands and methods do not, so storing the interpretation makes the data wrong and unrecoverable
when criteria are revised, while storing the value plus a separate interpretive assertion citing the
criteria it applied lets the interpretation be re-derived and the change audited. Three corollaries
follow: confidence belongs to the interpretation, because one does not *possibly* measure 350 cm/s;
measurements must stand alone, because radiologists frequently report them with no interpretation at
all; and measurement becomes a definition type distinct from a data element, with method optional
and by default unspecified, so an absent method must not be filled with an assumed default.

**Status.** Working proposal, recorded as an owner decision within the branch.

**Implemented.** Measurement definitions exist as committed example data with their quantity, units
and range, separate from the categorical element definitions.
`docs/next-gen-schema/examples/size-mean-diameter.element.json @ next-gen-2026 44836c1`.

**Evidence.**
- "What the Vocabulary Must Express" §4 — the two-assertion argument, the
  thresholds-move-measurands-do-not principle with a twenty-five-year illustration from a standard
  measurement atlas, the three corollaries, and the decision separating measurement from data
  element with method optional.
  `docs/next-gen-schema/01-what-the-vocabulary-must-express.md @ next-gen-2026 44836c1`
- The same document §4.2 — the note that this principle is already written down in narrower form in
  the finding model guidance, which separates a nodule model from its risk-category model because
  different radiologists assign different categories.

**Related.** A9, F1, F5.

**Disagreements.** Recorded as decision area ST09 against an external reviewer's alpha: the two
implementations have separate node families but "common binding behavior and interpretation links
need agreement". `docs/next-gen-schema/12-alpha-structural-comparison.md @ next-gen-2026 44836c1`

---

## F7. Finding models as the CDE workbench

**Idea.** Finding models are not a lightweight copy of common data elements; they are the fast,
ungoverned proving ground ahead of them. The January 2026 status deck names this "OIFM: the CDE
workbench" — rapid innovation ahead of adoption, programmatic knowledge for tools and model context,
and exploratory metadata "that can graduate to standards". The allied side states the other half: the
finding model effort "has independently built much of this and is roughly one iteration ahead", and
its models can be treated as drafts for finding classes, brought over for review rather than authored
from scratch. The project lead's own statement is shorter: the common-data-element work "should
dovetail with the OIFM work".

**Status.** Stated goal in both directions; implemented example running in the opposite direction.

**Implemented.** 115 of 2,382 models carry the common-data-element organization code, contributed with
an organization record naming the ACR/RSNA project and an index code in the RadElement system pointing
back at the set they came from. That index code is the join that lets a finding-model pipeline emit
common-data-element-labeled output. The chest CT content branch vendors 145 raw set definitions and a
converter beside them.
`ids.json @ findingmodels taxonomy-export-2026-08-15 a30c3c9`;
`cdes/definitions/` and `scripts/cde_to_finding_model.py @ content/chestcts 0472a46`.

**Evidence.**
- The January 2026 status deck extract — the workbench framing and the "workbench effect" in the
  executive summary. `knowledge/references/status-update-2026-01.md`
- "Current Understanding" §5.1 — a seven-row table of what the finding model work already answers
  (decoupling, source versus hydrated form, quantity kinds, a relationship registry, governance
  sidecars, metadata vocabularies, modelling guidance) and the caveat about bringing models over.
  `docs/next-gen-schema/00-current-understanding.md @ next-gen-2026 44836c1`
- The staging repository's self-description and extraction-process note — "a staging area for
  definitions of radiology common data elements in JSON format ... prior to their entering the review
  pipeline", and a worked conversion of report language into what it calls mini-observations.
  `README.md` and `docs/report_extraction_process.md @ CDEStaging main b814a10`

**Related.** B2, B8, C3, F8.

**Disagreements.** How the crossover works is explicitly open: a shared identity space and canonical
element registry, or a crosswalk maintained as a first-class deliverable. "Current Understanding"
Issue F states both and chooses neither. The practical asymmetry is recorded elsewhere: the IHE draft
prefers a common-data-element set code in the slot a finding model would occupy, and a model that has
not graduated has no set identifier to put there.

---

## F8. Measuring coverage by running real reports against the vocabulary

**Idea.** The gaps in a finding vocabulary are found by taking real report text and recording what it
says that the definitions cannot carry. Three gap classes are catalogued separately, each as a plain
list. *Composite negative statements* are sentences asserting absence across several structures at
once, often bundled with a technique limitation, which no single finding-plus-presence pair
represents. *Uncovered findings* are things reports say for which no definition exists at all.
*Missing attributes* are findings whose definition exists but which the report characterized along an
axis the definition does not carry, each entry linking to the specific definition file that fell
short.

**Status.** Implemented example (the catalogues exist as data); the method is described but not
automated.

**Implemented.** The extraction process document works one real pulmonary angiogram report into a
list of mini-observations, each a finding with a presence value and its attributes, and states the
two follow-up tasks that produced the catalogues: align finding, attribute and value names with the
definitions, and collect blanket negative statements into a separate file to catalogue and examine.
`docs/report_extraction_process.md @ CDEStaging main b814a10`.

**Evidence.**
- The composite negative statements catalogue — real sentences grouped by body region, including
  cases that bundle an absence with a technique caveat about contrast limiting sensitivity.
  `report_representation/negative_statements.md @ CDEStaging main b814a10`
- The uncovered findings catalogue — findings with their reported attributes and no definition behind
  them. `report_representation/uncovered_findings.md @ CDEStaging main b814a10`
- The missing attributes catalogue — each entry naming the finding, the attribute the report used,
  and a link to the definition file lacking it.
  `report_representation/missing_attributes.md @ CDEStaging main b814a10`
- The chest CT coverage roadmap — the same coverage question asked prospectively instead, as a
  frequency-and-priority table per exam with a RadElement set link where one exists.
  `definitions/upmedic/roadmap.md @ CDEStaging main b814a10`

**Related.** A4, B7, F7.

**Disagreements.** None recorded.

**Undetermined.** Whether the three catalogues were ever acted on. They are dated 2024 to 2025 and no
document records a disposition.

---

# What could not be determined

1. **Whether the finding model format and the next-generation vocabulary converge on one artifact.**
   Both sides state the relationship as a direction. Issue F of "Current Understanding" records the
   mechanism as open and nothing decides it.
2. **What the project lead means by "interesting relationship/graph work coming from CDEs" for the
   finding model format.** The relationship family (F5) and the draft registry (F4) are the candidate
   artifacts; no document connects them to that goal statement.
3. **Whether the finding model relationship registry draft is live.** Dated April 2026, implemented
   nowhere, and corrected in the relationship-family document as draft-only.
4. **Whether the exam-oriented sub-taxonomy hierarchy is meant to enter the schema**, and what
   `finding_cluster` means. Declared in the taxonomy README, never explained, populated in one file.
5. **How the sub-taxonomy anatomic category relates to the metadata body-region enumeration.** The
   categories are finer and not obviously mappable; no crosswalk exists on any branch read.
6. **Whether the eight structured metadata fields will land on the released branch.** Implemented on
   a branch, readiness recorded as not passing, nothing merged, and the branch carries breaking
   enumeration and validation changes not stated as agreed.
7. **How extracted sub-findings link to their parents.** Named as an open design problem on the chest
   CT branch; no mechanism anywhere.
8. **Whether the second-generation per-file anatomy record model was adopted, rejected, or
   superseded.** Hundreds of data files on an unmerged branch, inconsistent field names, no design
   note, though several of its fields reappear in the current package's field reference.
9. **What the ACR Common identifier on anatomic location records is** — code system, issuing
   authority, relation to RadLex identifiers. It appears as a bare numeric string in the field
   reference and on the unmerged branch, and the name change from Body Part Index to Anatomic
   Locations Index is nowhere explained.
10. **Why the exam type library was never built.** Four statements of the goal across four years; no
    document explains the gap. How "always / usually / possibly" would be represented is equally
    unstated.
11. **Whether proposed RadLex concepts were ever submitted**, and whether the three report-derived gap
    catalogues were ever acted on.
12. **Whether the RSNA/ACR committee has seen or assented to any decision after June 2026.** The
    decision record's provenance is the project lead and an assistant throughout; the last recorded
    committee event is a meeting on 12 June 2026.

---

# Proposed idea pages for this area

Each page is one explanatory home; the ideas it houses are listed by inventory identifier.

| Page | One line | Houses |
|---|---|---|
| `finding-model` | What a finding model is, what it contains, and the identifiers that carry its provenance. | A1, B1 |
| `what-counts-as-a-finding` | The boundary rules, the specificity rules, negative assertions, and the deliberate blending of description and diagnosis. | A2, A3, A4, A5 |
| `finding-model-conventions` | The operational rules the team enforces: presence and change from prior, synonyms as a matching surface, naming, associated findings versus components. | A6, A7, A8, A10 |
| `assessment-and-measurement` | Why a score is modelled apart from what it scores, and why a measured value is a separate assertion from its interpretation. | A9, F6 |
| `authoring-finding-models` | How content is actually produced: stubs and iteration modes, triage before create, three-tier review with context isolation, and why the prompts are fragments. | B3, B4, B5, B6 |
| `finding-model-content` | The corpus as merged provenance streams, the exam-oriented sub-taxonomies as direction and coverage ledger, convert-and-merge, and the upstream proposal loop. | B2, B7, B8, B9 |
| `foundation-context` | The eight metadata fields, each defined by what it excludes, and the exactness rule for index codes. | C1, C2, C3 |
| `assigning-metadata` | Focused agents, advisory audit, null as an answer, human review as the only authority, and how the artifacts are published. | C4, C5, C6, C7 |
| `finding-model-retrieval` | The three retrieval modes and the overlap check that runs before anything is authored. | C8 |
| `anatomic-location-index` | Containment as a single-parent tree, part-of kept separate, laterality triads, synthetic terms, and the curation rules that make the codes usable. | D1, D2, D3, D4, D8 |
| `why-anatomic-locations` | What was measured about existing ontologies, and what the index is and is not for. | D5, D9 |
| `anatomic-locations-and-radlex` | The overlay relationship, the missing taxonomic layer, and contributing terms back. | D6, D7, F3 |
| `anatomic-scope` | How a finding class says where it belongs, and how normal structures are described without one. | F1 |
| `exam-type` | Preferred entries over the Playbook and the inclusion edges to anatomy. | E1, E2 |
| `next-generation-vocabulary` | The redesign of the common-data-element vocabulary and the relationship family, including the draft finding model registry it corrects. | F4, F5 |
| `finding-models-and-cdes` | The workbench relationship in both directions, and how coverage is measured against real reports. | F7, F8 |
| `terminologies` | The role each vocabulary plays and why search recall is the gate. | F2 |

Seventeen pages. `assessment-and-measurement` is small and may fold into `what-counts-as-a-finding`
if the measurement-versus-interpretation material from the next-generation work is thin once drafted.
Whether `next-generation-vocabulary` stays one page or splits by node types and relationships is a
drafting decision, not an inventory one.

# Existing bundle pages holding unique team-authored material

Each is the only durable copy in this repository of something the team wrote. They must be rehomed
before their current pages are removed.

| Page | Unique material | Proposed home |
|---|---|---|
| `references/oifm-overview-extract.md` | The full upstream finding model guidance, quoted by four other pages. The prompt fragments now supersede it as the live source, but this is the only copy of the consolidated form. | Keep as a supporting reference linked from `what-counts-as-a-finding`. |
| `references/oifm-metadata-fields-extract.md` | The field-by-field metadata reference from a gist that is in no repository. | Keep as a supporting reference linked from `foundation-context`. |
| `references/cde-schema-differences.md` | The analysis of where the CDE set schema and the RadElement API diverge. | Keep as a supporting reference linked from `finding-models-and-cdes`. |
| `references/finding-model-schema.md` | The schema in prose. | Fold the load-bearing parts into `finding-model`; the code is the specification, per the team's own decision record. |
| `references/anatomic-location-json-schema.md` | The record shape in prose. | Fold into `anatomic-location-index`, keeping only what prose says better than the field reference. |
| `semantic-foundation/anatomic-locations/laterality-conventions.md` | Migrated laterality conventions. | Fold into `anatomic-location-index`. |
| `data-structures/anatomic-location-assignment-rules.md` | The three-step precedence ladder and the exam-to-region fallback table. | Belongs to the structures and applications area; flagged because `why-anatomic-locations` and `exam-type` both cite it. |
| `semantic-foundation/exam-types/existing-building-blocks.md` | The LOINC code census in the sample data, the Playbook provenance count in the ontology file, the viewer display table, the template corpus. | Reduce heavily; keep the few facts `exam-type` needs and drop the inventory. |
| `roadmap/open-questions.md` | Team questions mixed with agent-found documentation defects. | Split: team questions move beside the idea they belong to; defects go to `sources/upstream-issues-draft.md`. |
| `roadmap/anatomic-locations-and-radlex.md`, `roadmap/exam-types.md`, `roadmap/finding-model-format-evolution.md`, `roadmap/finding-model-content-direction.md` | Stated directions, already sourced. | Fold each into its idea page's direction section. No separate roadmap area for this material. |
