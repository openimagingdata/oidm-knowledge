# Changelog

All notable reader-facing changes to this knowledgebase. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Website commands now use `task site:...` from the repository root; knowledge checks and review commands remain separate.
- The website builds only `site/content/`, with its own navigation and OIDM branding. Dev and staging show a draft banner; production builds require page review stamps.

- Moved the old generated bundle to temporary `archive/knowledge`; `knowledge/` now starts a fresh reconstruction from supported sources.

- Consolidated planning into one implementation plan, preserved owner guidance and source inventories in references, and moved temporary review previews out of tracked documentation.

- Tightened 112 knowledge pages and their navigation descriptions, reducing repetition while preserving examples and source extracts; a five-part review then restored qualifiers, disclaimers, and quoted source material the tightening had dropped, and reverted twelve pages.
- Diagrams are Excalidraw-rendered SVGs composed for the text column, with click-to-zoom on the site; Mermaid is no longer used.

### Added

- Source manifest with provenance and handling rules, plus commands to recover and checksum-verify selected source files from Tigris without overwriting local changes.

- Source-grounded summaries of 15 project diagram boards, indexed by idea and pillar with links to the source material.
- Reusable OIDM and Anatomic Locations logos for site content and diagrams, with the original style guide and usage notes.

- First full draft of the knowledgebase: 115 documents in OKF 0.2 covering the overview and vision, a 48-term glossary, the semantic foundation (finding models, common data elements, anatomic locations, exam types, terminologies), the data structures (Observation, Exam Finding List, Imaging Problem List, Imaging Persona, FHIR and IHE alignment), the applications, the roadmap and open questions, project history, a repository map, and verbatim reference extracts.
- Authoring guide, contributing guide, and migration ledger recording every document migrated from a working repository.
- Two validation gates (OKF 0.2 conformance and house rules) run in continuous integration.
- Website built with Quartz, with separate Cloudflare targets for dev, staging, and production.
- All documents are status draft pending the project lead's verification.
