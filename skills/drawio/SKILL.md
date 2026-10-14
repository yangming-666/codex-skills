---
name: drawio
description: Create or edit an actual draw.io `.drawio` XML artifact, including its shapes, connectors, styling, layout, and optional export. Use when the user explicitly requests draw.io/diagrams.net output or provides a `.drawio` file to modify. Do not trigger for Mermaid, prose explanations, code-native diagrams, UI mockups, charts, or generic requests to visualize something without a draw.io deliverable.
---

# Draw.io Diagrams

Create or edit draw.io XML directly. Preserve existing page IDs, node IDs, styles, geometry, and
connections unless the request changes them.

## Route details

- Creating a diagram or adding new node/edge types: read
  [references/xml-elements.md](references/xml-elements.md).
- Changing layout, typography, colors, layering, or Japanese text sizing: read
  [references/style-and-layout.md](references/style-and-layout.md).
- Exporting PNG/SVG/PDF or validating rendered output: read
  [references/export.md](references/export.md).
- Starting from a blank file: reuse `references/templates/basic.drawio`.

Do not load export instructions for an XML-only edit. Do not load the blank template when editing
an existing diagram.

## Core contract

- Use one `mxCell` ID per semantic node/edge and keep source/target references valid.
- Put edges before vertices when they must render behind nodes.
- Set `defaultFontFamily="Noto Sans JP"` on `mxGraphModel` and explicit
  `fontFamily=Noto Sans JP;` on every text-bearing cell when Japanese text is present.
- Use sufficient text width and spacing to avoid clipping and connector-label overlap.
- Inspect the resulting XML for duplicate IDs, missing parents/targets, and malformed styles.
- When visual output is requested, export and inspect it before delivery.
