---
type: Glossary Term
title: Contained by and part of
description: The two orthogonal hierarchies over anatomic locations, one physical containment and one structural or functional membership.
tags: [glossary, semantic-foundation, anatomy]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org data file description, the two hierarchies
  - id: al-package
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/location.py
    title: Containment and part-of fields in the anatomic-locations package
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage, hierarchy description
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract, anatomical tree traversal in queries
---

# Contained by and part of

The two hierarchies over [anatomic locations](/glossary/anatomic-location.md), kept separate because they answer different questions.

- **Contained by**: "physically contained in (e.g., kidney in the retroperitoneum)."[^al-code]
- **Part of**: "a component of a larger structure/system (e.g., adnexa part of female genital system)."[^al-code]

Containment is the primary axis. The curated set is "organized into a directed, rooted tree hierarchy, starting from the whole body and ramifying through body regions," and containment is required on every node while part-of is optional.[^al-site] Part-of records organ-system membership. A structure can be contained in one region and belong to a system spanning several.

The newer package precomputes both hierarchies. Each location has `containment_path`, `containment_parent`, `containment_depth`, and `containment_children`, and the same four fields again with a `partof_` prefix, so ancestors and descendants on either axis resolve without walking the graph at query time.[^al-package]

## Synonyms and near-synonyms

- **`containedById`** and **`partOfId`** are the field names in the original JSON file.
- **Containment hierarchy** and **part-of hierarchy** are the usual long forms.
- **Is-a** is neither of these. It is subtype classification, used for [FindingClass](/glossary/finding-class.md) taxonomies, not for anatomy.
- **`Part_Of`** and **`Has_Part`** are the RadLex OWL properties that express anatomy inside the ontology itself.

## Identifier form

None. Both are references to other [RadLex RIDs](/glossary/radlex-id.md).

## Where it is used

[Data model](/semantic-foundation/anatomic-locations/data-model.md), [Tooling](/semantic-foundation/anatomic-locations/tooling.md), and [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md).

## Conflicts

RadLex itself expresses anatomy through `Part_Of` and `Has_Part` restrictions and has no separate physical-containment axis, so the containment hierarchy is a curation product rather than something the source ontology supplies. IHE IDR's query design assumes "fuzzy matching over an anatomical tree" so that a query for liver finds the caudate lobe, without saying which of the two axes that tree is.[^idr]

[^al-code]: anatomiclocations.org data file description
[^al-package]: Containment and part-of fields in the anatomic-locations package
[^al-site]: anatomiclocations.org site homepage
[^idr]: IHE IDR Phase II extract
