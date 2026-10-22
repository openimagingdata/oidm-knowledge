---
type: History
title: CDE template rendering
description: How CDETemplateDemo rendered structured Observations through Mustache templates in 2023, a precedent for the proposed reporting SDK.
tags: [history, reporting, observation, cde]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
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

`CDETemplateDemo` renders a [CDE](/glossary/cde.md)-labeled [Observation](/glossary/observation.md) as report prose through a text template, without a language model. Written in 2023 and unchanged since 2023-06-15, it was shown at SIIM in June 2023 as a web service that generated customizable prose from FHIR Observations.[^siim-post]

It is the project's earliest working generator of prose from structured data. See [lineage repositories](/history/lineage-repositories.md) for the repository's status.

# The pattern in three parts

**The Observation.** A sample pneumothorax Observation carries `code` as the RadElement set code RDES44, a `bodySite` coded against the anatomic locations system, and a `component` array whose entries each carry an element code and a value.[^observation] Six components appear: lung tissue collapse, presence, pleural separation in millimeters, side, size, and associated chest tube, plus signs of tension.

**The mapper.** `obsToMustache.ts` flattens the Observation's components into a plain key-value dictionary keyed by the component display name.[^mapper] It sets a boolean flag for each value to control template sections. Presence has two flags, one for present and one for absent.

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

Rendered against the sample Observation, that produces: "There is a Medium Left pneumothorax (pleural separation: 28 mm). There is Partial lung tissue collapse." The absent branch produces a single sentence. [Extraction approaches](/history/extraction-approaches.md) describes the reverse task of extracting explicit negatives.

# What the demo also shows by accident

The internal Observation class stores components as string key-value pairs and reduces the code and body site to an identifier and display string.[^obs-model] The sample files contain full FHIR Observations. The FHIR-based Observation in `OpenImagingDataModel.py` superseded this simplified internal model. Flattening remained a rendering step.

Only presence receives special treatment. Other values become boolean flags. Presence is also near-universal in the current [finding model format](/semantic-foundation/finding-models/finding-model-format.md).

# Relation to the reporting SDK idea

The January 2026 status deck names an Open Imaging Reporting SDK under its applications pillar, for vendors to use OIDM structures in reporting tools.[^deck] No such artifact exists; see [the reporting SDK](/applications/reporting-sdk.md), which records it as stated direction only.

The 2023 next-generation reporting assistance framework post described a plugin container whose scripts inspect standard report context and insert generated text. This demo provides a precedent for that rendering operation. See [site articles](/history/site-articles.md).

Each CDE set has a template in a directory named for its identifier, so templates describe findings rather than reports. A site can change template wording without modifying the renderer. The renderer is about thirty lines because the codes carry the semantics.

[^mapper]: CDETemplateDemo obsToMustache.ts, the Observation to template-data mapper
[^template]: CDETemplateDemo pneumothorax Mustache template
[^observation]: CDETemplateDemo pneumothorax sample Observation
[^obs-model]: CDETemplateDemo Observation model, the flat component variant
[^siim-post]: "SIIM Update", 2023-06-26, the hackathon demonstration of the rendering web service
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026, applications pillar
