# References

Verbatim and near-verbatim source material: migrated specifications, extracted notes, and worked examples built from real data. Each document says where it came from, when, and whether it is current.

* [Status update, January 2026](./status-update-2026-01.md) - A faithful extract of the January 2026 OIDM status deck, "Realizing Object-Oriented Imaging Results", slide by slide.
* [Finding model schema](./finding-model-schema.md) - The Open Imaging Finding Model record format as specified in the findingmodels repository, reconciled field by field against the Pydantic definitions that validate it.
* [Anatomic location record format](./anatomic-location-json-schema.md) - The two JSON record formats for anatomic locations, the original anatomiclocations.org body part schema and the current anatomic-locations package format, with a real record from each.
* [Exam Finding List example](./exam-finding-list-example.md) - A real Exam Finding List from the imaging-problem-list sample data, trimmed to five findings, with a field-by-field walkthrough.
* [Imaging Problem List example](./imaging-problem-list-example.md) - Two findings from a real Imaging Problem List in the imaging-problem-list sample data, with the grouping key and the temporal status derivation as the dev branch implements them.
* [Finding models: overview](./oifm-overview-extract.md) - Near-verbatim extract of the OIFM overview note explaining why finding models exist, what counts as an imaging finding, and how a finding model is structured.
* [Finding model structured metadata fields](./oifm-metadata-fields-extract.md) - Near-verbatim extract of the reference for the structured metadata fields on FindingModelBase and FindingModelFull, with the points where it differs from the branch code it describes.
* [CDE set schema versus the RadElement API](./cde-schema-differences.md) - Near-verbatim extract of the note cataloguing where the CDE set RelaxNG schema and the RadElement API disagree, with the later JSON Schema versions that partly close the gap.
