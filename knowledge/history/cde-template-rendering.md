---
type: History
title: CDE template rendering
description: The 2023 CDETemplateDemo pattern that turned a CDE-labeled Observation into report prose through a Mustache template, and how it relates to the reporting SDK direction.
tags: [history, reporting, observation, cde]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T02:00:00Z }
sources:
  - id: mapper
    resource: https://github.com/openimagingdata/CDETemplateDemo/blob/e09f2553de58b2c88ea26e9673750a62803d4dbc/mapper-logic/src/mappers/obsToMustache.ts
    title: CDETemplateDemo obsToMustache.ts, the Observation to template-data mapper
  - id: template
    resource: https://github.com/openimagingdata/CDETemplateDemo/blob/e09f2553de58b2c88ea26e9673750a62803d4dbc/mapper-ui/public/sample_templates/RDES44_Pneumothorax/template1.mustache
    title: CDETemplateDemo pneumothorax Mustache template
  - id: observation
    resource: https://github.com/openimagingdata/CDETemplateDemo/blob/e09f2553de58b2c88ea26e9673750a62803d4dbc/mapper-ui/public/sample_observations/RDES44_Pneumothorax/observation1.json
    title: CDETemplateDemo pneumothorax sample Observation
  - id: obs-model
    resource: https://github.com/openimagingdata/CDETemplateDemo/blob/e09f2553de58b2c88ea26e9673750a62803d4dbc/mapper-logic/src/models/observation.ts
    title: CDETemplateDemo Observation model, the flat component variant
  - id: siim-post
    resource: https://www.openimagingdata.org/siim-update/
    title: Site post "SIIM Update", 2023-06-26, the hackathon demonstration of the rendering web service
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026, applications pillar
---

# What it was

`CDETemplateDemo` is a small full-stack demonstration written in 2023 and untouched since 2023-06-15. Its whole purpose was to show that structured data can be turned back into readable report prose without a language model, by rendering a [CDE](/glossary/cde.md)-labeled [Observation](/glossary/observation.md) through a text template. The demonstration was shown at SIIM in June 2023 as a web service that takes a radiology finding encoded as a FHIR Observation with CDE tags and generates customizable prose.[^siim-post]

It is the earliest working structured-data-to-text generator in the project, and the direction it points is still live. See [lineage repositories](/history/lineage-repositories.md) for the repository's status.

# The pattern in three parts

**The Observation.** A sample pneumothorax Observation carries `code` as the RadElement set code RDES44, a `bodySite` coded against the anatomic locations system, and a `component` array whose entries each carry an element code and a value.[^observation] Six components appear: lung tissue collapse, presence, pleural separation in millimeters, side, size, and associated chest tube, plus signs of tension.

**The mapper.** `obsToMustache.ts` flattens the Observation's components into a plain key-value dictionary keyed by the component display name.[^mapper] It then does two things that matter. It sets a boolean flag named after each value, so that any value can drive a template section. And it special-cases the presence component, deriving two explicit flags, one true when presence is present and one true when it is absent.

```typescript
if (key.toLowerCase() === "presence") {
    if (value.toLowerCase() === "present") {
        res["presence_present"] = true;
        res["presence_absent"] = false;
    } else {
        res["presence_present"] = false;
        res["presence_absent"] = true;
    }
}
```

**The template.** Those flags open and close Mustache sections, so one template produces a full sentence for a present finding and a single clause for an absent one.[^template]

```mustache
{{#presence_present}}
There is a {{size}} {{side}} pneumothorax (pleural separation: {{pleura separation (mm)}} mm){{#signs of tension}}; signs of tension are {{signs of tension}}{{/signs of tension}}.
{{#lung tissue collapse}}
There is {{lung tissue collapse}} lung tissue collapse.
{{/lung tissue collapse}}
{{/presence_present}}
{{#presence_absent}}
There is no pneumothorax.
{{/presence_absent}}
```

Rendered against the sample Observation, that produces: "There is a Medium Left pneumothorax (pleural separation: 28 mm). There is Partial lung tissue collapse." The absent branch would instead produce a single sentence, which is exactly the shape the negative-statement problem in [extraction approaches](/history/extraction-approaches.md) works in the opposite direction.

# What the demo also shows by accident

The Observation class inside this repository is not the FHIR one. It models components as a flat record of string keys to string values, with the code and body site reduced to an identifier and a display string.[^obs-model] The sample JSON files on disk are full FHIR Observations, so the demo reads FHIR and works internally with something simpler. That divergence is why the repository is recorded as superseded: the FHIR-faithful Observation in `OpenImagingDataModel.py` became the reference shape, and the flat variant did not carry forward. The flattening itself did, as a rendering step rather than a data model.

The mapper also has a hardcoded assumption worth naming: presence is the only attribute given special treatment, and every other value becomes a bare boolean flag. That works because presence is the one attribute the current [finding model format](/semantic-foundation/finding-models/finding-model-format.md) also treats as near-universal.

# Relation to the reporting SDK idea

The January 2026 status deck names an Open Imaging Reporting SDK under its applications pillar, positioned as the vendor-facing surface through which reporting tools consume OIDM structures.[^deck] No such artifact exists; see [the reporting SDK](/applications/reporting-sdk.md), which records it as stated direction only.

This demonstration is the concrete precedent for one half of what such an SDK would have to do. The 2023 next-generation reporting assistance framework post described the other half, a plugin container in which assistance scripts run against standardized report context and can insert generated text into a report. Rendering a structured observation into a sentence is the operation those scripts would call; see [site articles](/history/site-articles.md) for that post.

Three facts about the demonstration are worth carrying into any later work on this. The template is per-CDE-set, stored under a directory named for the set identifier, so the unit of authoring is the finding rather than the report. The template is data, not code, so a site can maintain its own phrasing without touching the renderer. And the renderer itself is about thirty lines, because all the semantics live in the codes.

[^mapper]: CDETemplateDemo obsToMustache.ts, the Observation to template-data mapper
[^template]: CDETemplateDemo pneumothorax Mustache template
[^observation]: CDETemplateDemo pneumothorax sample Observation
[^obs-model]: CDETemplateDemo Observation model, the flat component variant
[^siim-post]: "SIIM Update", 2023-06-26, the hackathon demonstration of the rendering web service
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026, applications pillar
