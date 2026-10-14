# Draw.io XML Elements

## Base structure

```xml
<mxfile host="app.diagrams.net">
  <diagram name="Page-1" id="page-1">
    <mxGraphModel grid="1" gridSize="10" guides="1" page="1"
      defaultFontFamily="Noto Sans JP">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Vertices

Rectangle:

```xml
<mxCell id="rect-1" value="Label"
  style="rounded=0;whiteSpace=wrap;html=1;fontFamily=Noto Sans JP;fontSize=18;"
  vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry" />
</mxCell>
```

Change `rounded=1;arcSize=20;` for a rounded rectangle, use
`ellipse;whiteSpace=wrap;html=1;...` for an ellipse, and
`rhombus;whiteSpace=wrap;html=1;...` for a decision diamond.

Text-only cell:

```xml
<mxCell id="text-1" value="Text"
  style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;fontFamily=Noto Sans JP;fontSize=18;"
  vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="30" as="geometry" />
</mxCell>
```

## Edges

```xml
<mxCell id="edge-1" value="Label"
  style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontFamily=Noto Sans JP;fontSize=14;"
  edge="1" parent="1" source="rect-1" target="rect-2">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

Add `dashed=1;` for a dashed edge. Keep every source/target ID defined on the same page.
