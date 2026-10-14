# Draw.io Export

Use an available headless exporter:

```bash
drawio-export -x -f png -s 2 -t -o output.png input.drawio
```

Or use the draw.io CLI when a display-capable installation is available:

```bash
drawio -x -f png -s 2 -t -o output.png input.drawio
```

Relevant options:

- `-x`: export mode;
- `-f png|svg|pdf|vsdx`: output format;
- `-s 2`: scale;
- `-t`: transparent background;
- `-o`: output path;
- `-p`: zero-based page;
- `-b`: border size.

Inspect exported output for clipped text, overlapping connectors/labels, unreadable font sizes,
wrong layering, missing nodes, and insufficient Japanese text width. Fix material defects before
delivery.
