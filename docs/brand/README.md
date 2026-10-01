# Brand assets

Original assets retrieved from `t3://oidm-public/logos/` on 2026-09-30. [The manifest](./manifest.json) records each source URI, local path, size, and SHA-256. Files were renamed locally but their contents were preserved.

## What the guide establishes

The supplied [2023 style guide](./style-guide-2023.pdf) uses the earlier name **Open Radiology Data Model**. It has two pages covering the logo font and colors. The imported full OIDM logos say **Open Imaging Data Model**.

| Item | Guide | Implication for the site |
|---|---|---|
| Logo font | Arial Rounded MT Bold, page 1 | Use the supplied artwork to preserve the lettering. This is not a specification for website headings or body text. |
| Light blue | `#49b5ea`, Pantone 298 C, page 2 | A candidate accent color, also present in the OIDM SVGs. |
| Dark blue | `#0033cc`, RGB 0, 51, 204, Pantone 2728 C, page 2 | A candidate link and emphasis color on light backgrounds. Both projects' artwork uses it. |

**Color discrepancy:** page 2 prints light blue as RGB **4, 149, 234**, which is `#0495ea`, alongside hex **#49b5ea**, which is RGB **73, 181, 234**. The OIDM SVG fills use `#49B5EA`. Use that artwork-backed value for proposed web accents; the original guide remains unchanged. Some paths also use `#0133CC`, a near-match to the dark blue, preserved in the original files.

The guide gives no website layout, body typography, spacing, minimum logo size, clear-space, or dark-mode rules. It supplies no font files or webfont license. SVG lettering is outlined, so displaying these logos requires no font installation.

## Assets to use

All paths below are relative to [`knowledge/assets/brand/`](../../knowledge/assets/brand/). Each filename is available in both `.svg` and `.png`.

| Project | Full logo variants | Square mark | SVG proportions |
|---|---|---|---|
| OIDM | `oidm/logo-color`, `logo-black`, `logo-white` | `oidm/mark` | Full logo 800 × 197.89; mark 720 × 720 |
| Anatomic Locations | `anatomic-locations/logo-color`, `logo-black`, `logo-white` | `anatomic-locations/mark` | Full logo 538.02 × 179.27; mark 720 × 720 |

Prefer SVG for the website and diagrams. Transparent PNGs support tools that require raster input: OIDM logos are 2000 × 495, Anatomic Locations logos 2000 × 665, and both marks 720 × 720. The square marks came from the supplied favicon files. Their usefulness at very small sizes should be checked when installing a site favicon.

The selection omits duplicate print/editing formats, JPGs, pre-sized raster copies, overview illustrations, backgrounds, and the graveyard. The vector originals cover resizing without adding those copies.

## Suggested application

These are implementation suggestions, not additional rules from the guide:

- Use the color full logo for project identification on light backgrounds, the white full logo on dark backgrounds, and black for monochrome output. Preserve proportions and allow space around the artwork.
- Use the square marks beside project names in diagrams. Keep the name visible when the mark alone would be ambiguous. Do not use a project logo as a generic symbol for an anatomy or data-model concept.
- Use dark blue for candidate light-theme links or emphasis. Keep light blue for accents and larger graphic areas. Calculated contrast against white is about 8.95:1 for dark blue and 2.31:1 for light blue, so they are not interchangeable text colors. Check the actual background when applying either.
- Keep the current reading fonts until typography is addressed separately. The existing Quartz theme is in `site/quartz.config.yaml`; importing these assets does not apply a new theme.

## Use in site content and diagrams

From a document in `knowledge/drafts/`:

```markdown
![Open Imaging Data Model](../assets/brand/oidm/logo-color.svg)
```

The existing staging and Quartz asset steps copy the files to `public/assets/brand/`, making the example available at `/assets/brand/oidm/logo-color.svg` on the built site. Site header and favicon integration remain separate from importing the files.

For a diagram builder using `tools/diagrams/excalib.py`:

```python
image("oidm-logo", x, y, 200, 200 * 197.89 / 800,
      "../../knowledge/assets/brand/oidm/logo-color.svg")
image("anatomic-locations-mark", x, y, 48, 48,
      "../../knowledge/assets/brand/anatomic-locations/mark.svg")
```

Use distinct positions for each element. The helper resolves these paths relative to its own directory and embeds the SVG bytes into the Excalidraw file. Omit the `color` argument to preserve brand colors. Follow the [diagram source-of-truth rule](../../tools/diagrams/README.md#source-of-truth-rule) when adding a logo to an existing graphic.
