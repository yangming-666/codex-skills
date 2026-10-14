---
name: dota2-panorama
description: "Author or diagnose Panorama XML/VCSS/JS layout, state, events, lifecycle and rendering. Ordinary Panel/Image alignment, partial overflow or clipping uses layout proof; only a named or source-proven ScenePanel output defect uses compositor research. Excludes backend/Lua/KV/VMAP-only work and localization-only or value-lookup edits without a Panorama contract change."
---

# Dota 2 Panorama

Use addon source and one narrowly selected route. This Skill owns Panorama layout/state/lifecycle/
rendering contracts, not a neighboring Lua/KV/backend fact or unchanged ScenePanel merely present
on a page. Follow host source, validation, path-resolution and runtime authorization rules.

## Select the owning route

| Task | Required reading |
| :--- | :--- |
| Ordinary Panel/Image geometry, alignment, clipping/overflow or screenshot correction | [layout-proof.md](references/layout-proof.md): common source/geometry/reject sections plus only applicable centering, clipping or intrinsic-image subsections |
| Named/source-proven ScenePanel or ParticleScenePanel output/framing/composition/lifecycle defect | [scenepanel-compositor.md](references/scenepanel-compositor.md); select one render layer before edits |
| JS state, navigation, events or rerender | [visual-delivery-loop.md](references/visual-delivery-loop.md), applicable states only; [panorama-api2.md](references/panorama-api2.md) only for unresolved API behavior |
| Strict screenshot/design alignment | [design-alignment-proof.md](references/design-alignment-proof.md); [coordinate-and-replica.md](references/coordinate-and-replica.md) only for coordinate mapping |
| Visual hierarchy/surfaces or page replication | [visual-hierarchy-and-chrome.md](references/visual-hierarchy-and-chrome.md) and applicable delivery-loop sections |
| New page/redesign | Also the matching archetype in [dota2-page-archetypes.md](references/dota2-page-archetypes.md) |
| Named vanilla page/component or explicit reference catalog | [dota2-decompiled-page-cases.md](references/dota2-decompiled-page-cases.md), only matching research route |
| Entity-anchored WorldPanel | [worldpanel.md](references/worldpanel.md) |
| Returned regression, accepted subtree at risk or runtime contradiction | [regression-baseline.md](references/regression-baseline.md) |
| Authorized validation/engine-only fact | [validation.md](references/validation.md), only applicable commands and evidence lane |

Do not load every reference, API catalog or page archetype. Local geometry does not automatically
require compositor/design/vanilla research. Conditional references remain mandatory when their
owner is affected; keep their full applicable contract, not a keyword-only excerpt.

## Source and visual invariants

- Addon implementation reads/edits only `content/<addon>/panorama/`. Missing corresponding source
  blocks implementation; report its expected path. No compiled addon or `game/` Panorama reads.
  Only explicit global vanilla reference-catalog work may inspect compiled vanilla evidence, outside
  addon source, through the reference-catalog route.
- Preserve IDs, events, bindings, localization, hit testing and accepted stable subtrees except where
  the request changes them. XML owns structure, VCSS layout/visuals and JS state/events/rendering.
- Every affected 2D image keeps intrinsic aspect ratio, uniformly contained and centered in its
  stable box by default. Crop/cover/stretch/tile/nine-slice need an explicit user exception. Prove
  resource dimensions, actual drawing panel/API, complete cascade and all changed-resource/rerender
  states through layout-proof. Source/resource proof is required; screenshots are no substitute.
- Use only source/doc-proven Panorama properties and value syntax. Uncertain support requires
  authoritative confirmation before writing. Shadow ownership: Image `img-shadow`, text
  `text-shadow`, box `box-shadow`; no browser `drop-shadow` or `filter` analogy.
- Centering names the requested visual box, layout container, text panel and actual visible group.
  A centered wrapper or `text-align` alone proves nothing. Ordinary clipping fixes freeze the child's
  accepted geometry first; identify the owning ancestor/stacking/parent relationship before moving
  offsets, growing a host or substituting images.

## Work and regression control

1. Locate loaded XML/VCSS/JS/includes, dynamic constructors and rerender owners. Extend one task
   record with requirement, invariants, allowed owner and source/engine evidence needed; no second
   regression/matrix/report merely because another reference is loaded.
2. Inspect complete affected parent chains, cascade, authored geometry, clipping/z-order, hit tests,
   lifetime and repeated states. Trace source uncertainty first. For ScenePanel, name one render-layer
   owner and held-invariant layers; controlled substitution may resolve remaining resource ownership.
3. Capture/reuse the exact baseline for previously accepted behavior or a risky subtree change.
   `SetParent`, child reordering, Carousel recycling, duplicate ScenePanels, ancestor blur/masks/
   transforms/clipping and oversized hosts require a recorded risk and baseline comparison.
   Keep one live ScenePanel per semantic object unless explicit verified requirements need more.
   Preserve accepted inner framing inside a stable crop wrapper.
4. Make the smallest owning change, consolidate temporary selectors and recheck affected
   relationships. Do not compensate with unrelated resources, VMAP/camera or styling changes.
   Run checks only as authorized; source-review obligations do not authorize a gate or new test.
5. If an authorized runtime result contradicts source, invalidate the claim and revert this task's
   disproved change before another hypothesis. Restore frozen child geometry for clipping attempts.
   After two failures of the same relation, restore the recoverable verified baseline and stop
   speculative patches. If none is recoverable, report the baseline gap; never erase unrelated work.

Do not revisit an excluded resource plane without new contradictory evidence. Do not sacrifice an
accepted ScenePanel subtree to keep a new animation; build around the stable owner.

## Acceptance scope

Source can prove parentage, boxes, cascade, events, paths and the complete ordinary 2D contain
contract. Runtime proves engine-only compiled transparency, composition, animation/recycling and
actual black/blank output. Keep `source-inspected`, `source-proved` and `runtime-verified` distinct;
claim only the requested relationship supported by its evidence, not final rendered behavior from
source alone. Diff hygiene, compilation, selector presence or equal wrappers are insufficient.

Use a small early authorized engine check when such an uncertainty actually remains; do not accumulate
speculative edits first. For Dota/Panorama console evidence use only the current authorized VConsole2
session; runner/probe output is separate run evidence, not archived-console substitution.

`scripts/audit_scenepanel_contract.py` records structure/drift when that check is needed and permitted;
it is not a renderer. `check_panorama_layout.py` is for an existing mapping-backed fixed contract,
not a reason to create mappings for a local fix. `check_runtime_layout.py` needs real runtime rectangles.
