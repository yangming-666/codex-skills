# Draw.io Style and Layout

## Typography

- Set `defaultFontFamily="Noto Sans JP"` on `mxGraphModel`.
- Add `fontFamily=Noto Sans JP;` to every text-bearing cell.
- Use about 18 px for ordinary node text and 14 px for edge labels unless an existing diagram
  establishes another scale.
- Budget roughly 30–40 px per Japanese character when calculating a new node's width, then verify
  the rendered result.

## Common colors

| Use | Value |
| :--- | :--- |
| White | `#ffffff` |
| Light blue | `#dae8fc` |
| Light green | `#d5e8d4` |
| Light yellow | `#fff2cc` |
| Light red | `#f8cecc` |
| Light gray | `#f5f5f5` |

Use `fillColor`, `strokeColor`, and `fontColor` in the semicolon-separated style string. Match an
existing diagram before introducing new colors.

## Layering and spacing

XML order is render order: earlier cells are behind later cells. Put edges first, then nodes, then
standalone labels that must sit on top. Keep at least 20 px between connectors and unrelated labels
and avoid edge routes through node text.

Preserve the existing grid, page size, zoom-independent geometry, and alignment rhythm during
edits. Do not restyle the entire diagram for a local change.
