# Design alignment proof

Use whenever a screenshot or design visibly specifies alignment, table columns, cell placement, or centered groups. Complete this before changing XML, JS structure, or VCSS.

## 1. Classify the reference model

Assign one model to each region:

- `fixed-grid`: repeated rows share label/value/lock/trend axes;
- `centered-group`: each row’s complete content group is independently centered;
- `distributed`: children occupy named left/center/right slots;
- `edge-aligned`: one or more visible edges share an axis;
- `overlay`: an affordance does not participate in the content group.

Do not replace the reference model with a more convenient CSS model.

For tabular regions, record:

| Row type | Label cell | Value cell | Lock/trend cell | Shared axes | Vertical relation |
| --- | --- | --- | --- | --- | --- |
| normal | alignment and edge | alignment and edge | none/trend | named axes | baseline/center |
| effect | alignment and edge | empty/value | lock cell | named axes | baseline/center |

If normal values share an edge and a lock occupies that same column in the design, the implementation is a grid. Per-row `fit-children` centering is a source-detectable failure.

## 2. Extract reference constraints

Use the design image to record relationships before pixels:

- outer card/content bounds;
- grid center or centered-group center;
- label-column start/end and text alignment;
- value-column start/end and text alignment;
- lock/trend/badge cell;
- normal-row height and special-row gap;
- icon+count group center relative to its button;
- left/right action button centers and widths.

Use screenshot pixels or normalized coordinates only to validate these relationships. Convert measurements into parent-relative axes, cells, gaps, and ratios.

## 3. Extract the code model

For every constrained element, record:

- constructor and direct parent in XML or `$.CreatePanel`;
- current parent before rerender and parent after rerender;
- parent flow and child flow participation;
- final width/height/min/max, padding, margin, alignment, position, transform, and visibility;
- every applicable selector in final cascade order;
- text alignment and overflow behavior;
- rerender/deletion owner for dynamic nodes.

Write the authored equation for each reference axis. Examples:

`right(label_i) = grid_left + label_width`

`right(value_i) = grid_left + label_width + gap + value_width`

`cell(lock) = value_cell`

`center(cost_content) = center(refine_button)`

The code model fails if two reference-aligned elements resolve against unrelated parents without a complete ancestor equation.

## 4. Prove equivalence, not plausibility

Create a one-to-one ledger:

| Reference relation | Code owner | Authored equation | Counterexamples | Result |
| --- | --- | --- | --- | --- |
| lock occupies value column | row grid | `cell(lock)=cell(value)` | locked/unlocked, current/rerendered | pass/fail |

Every reference relation needs exactly one structural owner. Reject:

- a centered wrapper used to justify asymmetric visible children;
- fixed empty columns when the reference centers each row group;
- per-row `fit-children` when the reference shows shared columns;
- a lock positioned by an offset unrelated to the value cell;
- independently tuned margins that are supposed to preserve one shared axis;
- source-parent changes without a proved rerender path;
- arithmetic that ignores padding, border, margin, or collapsed nodes.

## 5. Run counterexample states

Evaluate the same equations for:

- shortest and longest labels;
- minimum and maximum values;
- trend shown/hidden;
- lock shown/hidden and locked/unlocked;
- normal and effect rows;
- empty and populated after-state;
- initial render, already-open state, mode switch, selection switch, and reopened popup.

If content length changes a shared reference axis, the implementation fails unless the design explicitly uses independently centered groups.

## 6. Predictive source gate

Source self-check passes only when:

- every design relation is classified and mapped;
- every mapped relation has a valid parent-chain equation;
- the implementation uses the same grid/group model as the reference;
- every dynamic parent and rerender state is accounted for;
- all counterexamples preserve the required axes, cells, gaps, and bounds;
- no later selector can restore a conflicting width, flow, alignment, or transform;
- all children fit every clipping ancestor;
- accepted regions retain their prior equations.

Do not cite `git diff --check`, compilation, or selector existence as evidence for this gate.

After this gate passes, runtime should confirm rather than discover authored layout errors. If runtime exposes an authored error, mark the source gate failed, add the missing invariant, and stop page iteration until the proof is repaired.

## 7. Required self-check result

Before claiming source self-check passed, produce this result for every alignment-sensitive region:

| Field | Required content |
| --- | --- |
| reference model | fixed grid, centered group, distributed, edge-aligned, or overlay |
| implementation model | actual parent, flow, sizing, alignment, and cell/axis ownership |
| equivalence proof | equations mapping every reference axis/cell to the code owner |
| counterexamples | at least shortest/longest content and every lock/trend visibility state |
| verdict | pass or exact source-level deviation |

A verdict without both models and counterexamples is invalid. “The wrapper is centered,” “the widths match,” “the CSS compiles,” and “`git diff --check` passes” are not equivalence proofs.
