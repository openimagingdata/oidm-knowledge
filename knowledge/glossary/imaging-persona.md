---
type: Glossary Term
title: Imaging Persona
description: The stated goal of surrounding a patient's Imaging Problem List with clinical context, orders, baseline history, and prior interventions.
tags: [glossary, data-structures, roadmap]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026, Imaging Persona
---

# Imaging Persona

The fourth and outermost level of the OIDM data structure hierarchy, and a stated goal rather than an implemented artifact. The 2026 status deck describes it as "the big picture" around a patient's [Imaging Problem List](/glossary/imaging-problem-list.md), composed of four kinds of context: clinical context such as orders and indications; a medical baseline such as the problem list, allergies, and laboratory results; specialized history such as oncologic treatment; and surgical history such as operative reports, pathology, and implants.[^deck]

The deck's argument for it runs through the imaging life cycle. Planning needs magnetic resonance safety information and mobility status. Intra-exam protocoling needs rules over prior history. Interpretation needs findings-oriented views of what came before. Post-interpretation needs passive screening, research, and outcomes work. Each of those draws on context that sits outside imaging results proper.[^deck]

No schema, sample, or implementation exists. Everything recorded here is the deck's own statement of direction.

## Synonyms and near-synonyms

- **Patient imaging context** describes the same idea without the coined term.
- **[Imaging Problem List](/glossary/imaging-problem-list.md)** is the level below, and is implemented.
- **FHIR Patient** and the electronic medical record problem list are external structures the persona would draw on, not the persona itself.

## Identifier form

None. No format exists.

## Where it is used

[Hierarchy](/data-structures/hierarchy.md), [Imaging Persona](/data-structures/imaging-persona.md), and [Roadmap 2026](/roadmap/roadmap-2026.md). This knowledgebase documents it as a goal and says so wherever it appears.

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
