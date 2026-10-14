# Panorama layout proof

Use this process for local alignment, spacing, resizing, clipping, overlap, visibility, and screenshot-feedback corrections. It is deliberately smaller and stricter than the page-design workflow.

## 1. Freeze the contract

Record the delta before editing:

| Item | Required relation or state | Owner | Must remain unchanged |
| --- | --- | --- | --- |
| changed group | exact edge, center, gap, size, or visibility rule | nearest shared parent | accepted siblings, anchors, wiring |

Translate visual language into relationships:

- “left edges align” -> `left(A) = left(B)`;
- “centered between” -> `center(target) = (edge(A) + edge(B)) / 2`;
- “equal spacing” -> `gap(A,B) = gap(B,C)`;
- “do not clip” -> rendered bounds, including approved overflow, stay inside every clipping ancestor;
- “keep size” -> authored box and transform remain invariant unless the user distinguishes them.

Do not replace a relationship with screenshot coordinates.

When a supplied design visibly specifies alignment or columns, complete `design-alignment-proof.md`. First classify whether the reference uses a fixed grid, independently centered groups, distributed slots, edge alignment, or overlays. Do not infer “centered” from the current implementation.

## 2. Build the parent-chain table

For each constrained element, trace the actual XML chain to the stable shell:

| Element | Direct parent | H owner | V owner | Flow status | Size source | Offset source | Clip/visibility ancestors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | selector/id | selector/id | selector/id | normal / ignored / overlay | final VCSS rule | margin/x/y/transform | list |

Rules:

- Alignment is relative to the actual parent content box.
- A visually related panel is irrelevant unless it is an ancestor or both panels are converted into one proven coordinate space.
- If two constrained siblings have different parents, either derive both absolute equations through their ancestors or introduce a shared rail/slot.
- Inspect every applicable selector, including compound classes and later rules. A selector-count check alone is not a cascade audit.
- For JS-created panels, record the constructor parent, the parent of already-existing nodes, and the event that rerenders the subtree. A changed source parent does not move existing nodes by itself.

## 3. Derive authored geometry

### Visible-content centering gate

Apply this gate before changing any button label, text-plus-icon row, reward group, price line,
or other content whose visible center must align with a control or heading.

Define the requested relationship before editing. “Centered” means the center of the visible
content group aligns with the center of the user-named visual target box:

`centerX(visible_content_group) = centerX(target_visual_box)`

For vertical centering, also require:

`centerY(visible_content_group) = centerY(target_visual_box)`

Do not substitute any of these weaker facts for that relationship:

- `text-align: center` only aligns glyphs inside the text panel;
- `horizontal-align: center` only aligns a panel inside its actual parent content box;
- a `100%` text panel may still refer to a padded, reserved, or otherwise narrower content box;
- a centered fixed-width row can still have visibly asymmetric empty columns or trailing margins;
- a native control can reserve space for an icon, arrow, price, or decoration even when that
  element is empty or invisible;
- a selector that exists in source may not match the engine-created final text node or may lose
  to a later, more authoritative rule.

Build and retain this four-layer ownership record:

| Layer | Required evidence |
| --- | --- |
| target visual box | exact panel whose painted rectangle the user means by “the button”, “the title”, or “the card” |
| layout/content box | padding, borders, native reserved regions, flow ownership, and complete derived rectangle |
| text or group panel | actual XML/JS-created or engine-created node, final parent, authored width, margins, alignment, and final selector cascade |
| visible content | ordered text/icons, symmetric outer gaps, and whether transparent resource padding or glyph ink requires runtime evidence |

For a text-plus-icon or reward group, size the group from its occupied children when the design
calls for independent group centering. Remove asymmetric fixed empty slots and trailing-only
margins from the centering equation, or balance them explicitly:

`group_width = sum(occupied child outer widths) + sum(inter-child gaps)`

`left_outer_gap = right_outer_gap`

For native buttons, first locate a source-proven successful instance with the same control type,
class set, content shape, and dynamic text contract. Reuse that structure exactly. Do not add
custom internal-label selectors, switch control types, add wrappers, or move the text to an
overlay unless the final node and content-box ownership prove why the successful native pattern
cannot satisfy the requested visual-box equation. If an explicit wrapper or overlay is justified,
the button chrome and visible content must share one fixed host rectangle, and hit testing plus
state presentation must remain owned by the interactive control.

Alignment work must preserve displayed content, localization tokens, IDs, event wiring, dynamic
price/state bindings, button type, and accepted dimensions unless the user requests one of those
changes or the ownership proof shows it is necessary. Never change text or business state as a
way to diagnose geometry.

Before delivery, inspect shortest and longest localized strings, with and without every optional
icon, and initial plus rerendered state. Source-proof the layout-panel equation. If glyph ink or a
native control's internal painted region is engine-owned, label that fact runtime-only and do not
claim visual acceptance without current authorized evidence.

When a screenshot or current runtime observation contradicts a centering claim, the claim is
false. Revert the disproved change before another attempt. The next attempt must identify the
specific failed layer from the four-layer record; do not merely increase selector specificity,
add `text-align`, add another wrapper, or introduce an offset. After a second contradiction,
restore the last accepted baseline and stop until a controlled runtime rectangle/text-node probe
or a newly supplied screenshot can distinguish the remaining owner.

### Clipping ownership gate

Apply this gate before changing geometry whenever an ordinary `Panel`, `Image`, badge, arrow,
notification, tooltip decoration, or other 2D element is intended to cross an owner boundary and
is missing, shows only a fragment, disappears after a negative margin, or has a runtime layout
rectangle outside the card while its rendered pixels remain cut off.

Freeze the accepted child geometry first. Record the exact `width`, `height`, alignment,
`position`, margins, transform, and resource. Until the clipping owner is proven, do not change
those values, add safe-area padding, enlarge the child or anchor, substitute another image, or
apply an optical correction. A clipping fix must preserve the frozen rendered anchor relation.

Build the live chain through every structural layer, including nodes that do not appear in the
snippet itself:

`drawing panel -> overlay/anchor -> snippet root -> dynamic constructor host -> wrapping/scrolling container -> stable shell`

For every node, record:

- source constructor and current runtime parent;
- authored and runtime rectangle in one coordinate space;
- `overflow` on both axes, including scroll ownership;
- normal-flow versus `ignore-parent-flow` status;
- sibling creation order and applicable `z-index` selectors;
- visibility, opacity, transforms, masks, and hit-testing ownership;
- the rerender path that can recreate, cache, or reparent it.

Do not infer painted visibility from a layout rectangle. `GetPositionWithinWindow`, actual layout
width/height, or an out-of-bounds right/top value proves geometry only; it does not prove that the
texture pixels survive ancestor clipping, a scroll viewport, or later-painted siblings.

Use controlled substitutions in this order, changing one variable per test:

1. Keep the child geometry unchanged and enable `overflow: noclip` on the nearest source-proven
   clipping candidate.
2. If two candidate parents have the same runtime origin and size, reparent the existing overlay
   to the higher parent without changing child geometry. A result change identifies ownership;
   a result that follows the same position rules also proves the geometry was held invariant.
3. If overflow crosses a sibling boundary, raise only the semantic host carrying the active
   indicator, then its overlay, rather than globally raising every card.
4. Treat a scrolling container as a viewport owner. Do not attempt to defeat its scroll-axis clip
   with increasingly negative margins; place the decoration in a proven non-scrolling overlay or
   reserve an explicit gutter while preserving the accepted child position.
5. Only after the full painted element is visible may a local optical correction compensate for
   transparent resource padding.

Reject these common false fixes:

- moving the child farther outward before proving the clipping owner;
- enlarging an anchor so its layout rectangle crosses the edge while the same parent still clips;
- assuming `z-index` escapes an ancestor clip;
- assuming `overflow: noclip` on the snippet root also applies to its dynamic host;
- treating the visible fragment as proof that the resource itself contains only that fragment;
- changing both parent structure and child offsets in one test;
- accepting a runtime rectangle dump as painted-pixel evidence.

When the same child can be hosted by a snippet root and an equal-sized dynamic host, prefer the
dynamic host as the overflow owner if it is the first node outside the clipped visual surface.
Bind or reparent before creating the indicator, repeat the ownership check on every refresh path,
and preserve unique IDs, events, state classes, and `hittest=false` behavior.

Use layout boxes, not visible pixels inside art.

For a centered child in a fixed parent, the simplified authored relation is:

`child_left = parent_content_left + (parent_content_width - child_outer_width) / 2 + approved_offset`

For two left edges to match, their complete derived expressions must match. Equal child widths are insufficient when `parent_content_left` or `parent_content_width` differs.

For a normal vertical flow:

`child_top = parent_content_top + sum(previous occupied outer heights) + child_top_margin`

Account for:

- parent padding and borders;
- sibling margins and explicit spacer panels;
- collapsed/hidden state behavior used by the source;
- `ignore-parent-flow` or overlays, which reserve no flow space;
- transforms, which alter rendered bounds without changing normal-flow occupancy;
- `fit-children` and flexible regions, whose final size may require runtime evidence.

For a fixed horizontal group, prove:

`left gutter + child outer widths + inter-child gaps + right gutter + approved decoration clearance <= parent content width`

For a reference table, prove shared axes rather than row bounding-box centers:

`right(label_i) = label_axis`

`left_or_right(value_i) = value_axis`

For a lock or trend that replaces/occupies a value cell:

`cell(lock_or_trend) = cell(value)` and `centerY(lock_or_trend) = centerY(row)`

If the design shows shared columns, per-row `fit-children` centering fails even when each row box is mathematically centered. If the design shows independently centered groups, asymmetric fixed empty columns fail even when the grid box is centered.

For a fixed vertical stack, prove:

`top padding + occupied rows + structural gaps + bottom padding <= stable container height`

### Intrinsic image aspect-ratio contract

Unless the user explicitly names an exception, every 2D image uses contain semantics inside its stable content box: show the complete resource, scale both axes uniformly, center it on both axes, and do not crop or stretch it. This default applies to XML `Image` panels, VCSS background images, JS-created image panels, and all state/rerender variants. Cover, crop, independent-axis stretch, tile, and nine-slice behavior require an explicit, local exception in the task contract.

Complete this contract during implementation. Do not use a screenshot, live Dota, Panorama debugger, or user correction to discover or accept ordinary 2D aspect-ratio behavior.

Extend the task image inventory before changing an image drawing/scaling relationship. For every
resource and fallback reachable through that affected path, record its semantic identity, exact resource path, intrinsic pixel dimensions, containing content box, panel type, scaling owner, proven Panorama implementation path, final selector or XML/JS attribute, and every state that can replace or restyle it. Read local raster dimensions directly from the files. Resolve dimensions for external or compiled resources from authoritative resource metadata or a source-proven reference. If the resource identity, dimensions, or supported scaling path cannot be established, stop and report the gap; do not guess, substitute another resource, or defer the decision to runtime.

Use the implementation path owned by the panel type:

- Declarative `Image`: set the proven preserve-aspect scaling attribute on the actual `Image`, give it the stable box dimensions, and center it.
- JS-created `Image`: call the project-proven Image scaling method such as `SetScaling("stretch-to-fit-preserve-aspect")` on the created Image before `SetImage`. Reject direct field assignment such as `image.scaling = ...` unless current authoritative API or source evidence proves that exact assignment contract.
- VCSS background image: set the background resource on the owning panel and explicitly use the Panorama-proven `background-size: contain`, centered position, and no-repeat contract.

Do not assume that setting a container's width and height, making an `Image` panel `100% × 100%`, or writing a preserve-aspect token somewhere in the constructor establishes the texture scaling mode. The scaling owner must be the exact live panel that draws the resource.

For source dimensions `source_w` and `source_h`, containing content-box dimensions `box_w` and `box_h`, and rendered image dimensions `render_w` and `render_h`, prove:

`render_w / render_h = source_w / source_h`

`render_w <= box_w` and `render_h <= box_h`

`render_w = min(box_w, box_h * source_w / source_h)`

`render_h = min(box_h, box_w * source_h / source_w)`

`centerX(image) = centerX(box)` and `centerY(image) = centerY(box)`

Reject independent forced width and height unless the active Panorama-supported scaling contract itself preserves the intrinsic ratio. Verify the exact property or attribute against Panorama evidence; do not substitute a browser CSS spelling by analogy. Transparent padding inside the resource may make visible artwork appear smaller, but it does not permit ratio distortion, cropping, or compensating independent-axis scaling.

For a uniform slot, keep the slot size common and let the proven Image scaling contract contain each resource independently. Never change the slot ratio to the ratio of a representative or majority resource, and never create per-resource panel-size tables to simulate aspect preservation. The resource identity and intrinsic ratio belong to the drawn image; the uniform slot owns only layout occupancy.

Static tests must execute or structurally inspect the actual constructor/selector path and verify resource identity, the exact scaling API/property on the drawing panel, stable box ownership, centering, and absence of later overrides. A regex or string-presence test that merely finds a slot size, `100%` dimensions, and a preserve-aspect token is not evidence and must fail review.

## 4. Own repeated relationships structurally

Use one owner for each invariant:

- equal gaps -> shared spacer class or one parent distribution rule;
- shared left edge -> common rail/column;
- shared center -> common fixed-width slot;
- navigation centered in a semantic gap -> navigation overlay belongs to that gap wrapper;
- large art between text and progress -> explicit upper gap, art row, explicit lower gap.

Avoid duplicated margins for relationships that must stay coupled.

## 5. Distinguish authored and rendered bounds

Source can prove authored boxes. It may not prove:

- transparent padding inside compiled images;
- glyph ink bounds and font fallback;
- particle extents;
- engine-specific scaling or animation state.

Do not “correct” these with layout offsets until the authored relationship is proved. If visual art bounds matter, keep the structural box correct, then apply a documented optical correction local to the art.

## 6. Impact audit after every structural change

Recompute affected descendants and siblings when changing:

- parent width/height or padding;
- `flow-children`;
- direct parent or wrapper structure;
- child authored size;
- margin, x/y, alignment, or transform;
- overflow, clipping, visibility, or z-order.

Check accepted invariants again. A local fix fails if it silently moves a previously accepted navigation axis, button row, background edge, or hit target.

For dynamic subtree changes, also check initial render, already-open state, mode/selection rerender, and reopened state. CSS and JS must agree on the actual parent in every live state; otherwise source proof fails before runtime.

## 7. Static reject gate

For the affected contracts, require the applicable items below before runtime. Reuse the task's
parent-chain/evidence record; this checklist does not mandate new tests or gate execution. Image
inventory covers the affected drawing paths, resources and reachable fallbacks, not unrelated pages:

- [ ] Every constrained panel has a complete parent chain.
- [ ] Every design-owned alignment has a classified grid/group model and named axis/cell.
- [ ] Every centered control or content group has a named target visual box and a four-layer ownership record; its visible-content center equation is satisfied rather than inferred from `text-align`, a centered wrapper, or selector presence.
- [ ] Centering changes preserve content, localization, IDs, events, bindings, control type, and accepted dimensions unless a proven owner-level exception is in scope.
- [ ] Shortest/longest localized text, optional-icon variants, and initial/rerendered states preserve the same center relation without asymmetric empty slots or trailing-only margins.
- [ ] The actual H/V owners are named.
- [ ] Requested edge, center, and gap equations are shown and satisfied.
- [ ] Normal-flow occupancy and overlays are distinguished.
- [ ] Total width and height fit stable owners.
- [ ] All clipping and overflow ancestors are checked.
- [ ] For overflow/clipping work, child geometry was frozen until ownership was proven; the live chain includes snippet roots, dynamic hosts, scroll viewports, sibling stacking, and rerender/reparent paths.
- [ ] No runtime rectangle is treated as proof of painted visibility, and no offset, anchor growth, safe-area change, image substitution, or optical correction precedes clipping-owner proof.
- [ ] If reparenting is used, old and new parent coordinate equations prove the requested position is unchanged, and initial plus repeated refresh paths preserve the new parent.
- [ ] Visibility and z-order cannot hide required panels.
- [ ] Final VCSS rules are authoritative and non-conflicting.
- [ ] Every reachable 2D image and fallback has an inventoried semantic identity, exact resource path, mandatory intrinsic dimensions, stable containing box, named drawing/scaling owner, and audited XML/VCSS/JS state path.
- [ ] Every dynamic `Image` calls a source-proven scaling method on the created drawing panel before setting the resource; unproved direct `scaling` field assignment is rejected.
- [ ] Every declarative `Image` and VCSS background uses the proven contain implementation for its own panel type rather than inheriting intent from a wrapper.
- [ ] Every image without an explicit local exception is fully visible, centered, uniformly scaled, and satisfies the intrinsic-ratio contain equations.
- [ ] No container width/height change, later selector, dynamic constructor, or rerender path silently replaces contain behavior with crop, cover, tile, or independent-axis stretch.
- [ ] No image identity is guessed or silently replaced by a different item's art, and no representative/majority resource ratio is used as proof for other resources.
- [ ] Proportion tests inspect the actual drawing path and equations; no pass relies on regex/string presence for slot size, `100%` dimensions, or a preserve-aspect token.
- [ ] IDs, events, and state selectors remain valid.
- [ ] Dynamic constructors, current parents, and rerender paths agree.
- [ ] Every frozen invariant is rechecked.
- [ ] Shortest/longest, lock/trend, empty/populated, and initial/rerendered counterexamples preserve the design relations.
- [ ] No pass claim relies on `git diff --check`, compilation, selector presence, or centered outer boxes alone.

“Looks plausible from the values” is a failure. If the containing blocks are not the same, show the ancestor equations or change the structure.

A source pass is predictive: every design-owned authored relation has a corresponding code equation and survives the selected counterexamples. Runtime is not a substitute for any relation that the design and source can determine.

## 8. Runtime boundary

Use a runtime dump or screenshot only after the source proof passes, and only to resolve engine-only facts. Do not request or require runtime evidence for ordinary 2D image identity, intrinsic ratio, contain scaling, centering, or clipping; those must already be correct and accepted from resource and source proof. A runtime image must not be used to discover an authored parent-chain or image-scaling error that source already exposes.

When runtime evidence disproves the model:

1. state the disproved assumption;
2. revert or replace the smallest owning change;
3. update the contract and parent-chain table;
4. rerun the static reject gate;
5. avoid compensating offsets unless the remaining difference is explicitly optical.
