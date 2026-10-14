# ScenePanel render-layer and compositor defects

Use this low-freedom workflow only when a named or source-proven `DOTAScenePanel` or `DOTAParticleScenePanel` owns the unresolved output. Applicable defects include subject size, camera framing, render-surface size, overscan, clipping, black/blank output, stale or duplicate output, layering, and lifecycle behavior. Do not route here for ordinary non-ScenePanel geometry, VMAP-only authoring, or a page that merely contains a ScenePanel.

## 1. Render-layer ownership gate

Model the visible result as a strict composition chain:

`visible output = outer layout(clip aperture(ScenePanel surface(render(scene resource, camera))))`

Assign each relationship to exactly one layer before editing:

| Layer | Owns | Does not own |
| --- | --- | --- |
| Scene resource | World-space models, particles, lighting, authored animation, and their spatial completeness. | UI aperture size, compositor-surface dimensions, or outer placement. |
| Camera and projection | View direction, perspective, field of view, near/far clipping, and which world-space content enters the projection. | ScenePanel render-target size, overscan extent, or parent clipping. |
| ScenePanel box | The compositor/render surface width, height, aspect ratio, and its position behind the aperture. | World-space composition or the aperture exposed by the parent. |
| Immediate clip host | The stable visible aperture, overflow boundary, and card/component media geometry. | Camera framing or the ScenePanel's internal render surface. |
| Outer ancestors | Page placement, flow occupancy, scrolling, z-order, and post-composition transforms or masks. | The camera frustum or ScenePanel render-target contract. |

Treat width/height changes to the ScenePanel box as render-surface changes. Treat transforms as operations on an already composited texture; they are not equivalent to changing the render surface. Treat field-of-view changes as projection changes; they are not equivalent to enlarging or shrinking the ScenePanel box.

Before any size, framing, or clipping edit, record:

- accepted scene resource and camera framing;
- ScenePanel width, height, aspect ratio, and position;
- immediate clip-host width, height, and overflow;
- every ancestor transform, mask, clip, scroll, and compositor surface;
- the exact relationship that must change and every layer that must remain invariant.

Select one owner:

- If world-space content is absent, intersects the near/far planes, or is outside the intended projection, own the fix in the scene resource or camera layer.
- If camera framing is accepted and the required result is a larger or smaller compositor output behind an unchanged aperture, own the fix in ScenePanel width/height and centered positioning. Use an explicit stable clip host for overscan and leave camera/FOV unchanged.
- If the amount of output that should be visible is wrong while the ScenePanel surface is correct, own the fix in the immediate clip host.
- If the complete component is misplaced or incorrectly participates in flow, own the fix in an outer layout ancestor.
- If the final output is stretched, blurred, or scaled after rendering, audit aspect-ratio mismatch and post-composition transforms before changing the scene or camera.

Reject a patch that:

- changes FOV to imitate ScenePanel-surface scaling or overscan;
- changes ScenePanel size to compensate for world-space or camera-frustum clipping;
- enlarges the clip host when its visible aperture is an accepted invariant;
- uses a transform as the first substitute for an authored ScenePanel width/height contract;
- edits more than one render layer in the same attempt without controlled evidence that the defect crosses those layers.

## 2. Classify before editing

Create controlled comparisons that change one dimension at a time: resource, XML/JS owner, state transition, lifecycle event, or time. Record which dimension the defect follows and which planes the comparison excludes.

State the classification and the evidence that would disprove it. Do not merge competing hypotheses into one patch, and do not encode a project-specific symptom as a universal cause.

## 3. Freeze the last accepted structure

Follow `regression-baseline.md`. Record for every affected ScenePanel:

- unique ID and semantic content key;
- direct XML or constructor parent;
- every ancestor through the stable shell;
- static and dynamic instance count;
- authored width/height and camera/framing attributes;
- clipping, overflow, opacity, visibility, z-order, transforms, `blur`, and `opacity-mask` on the panel and ancestors;
- scroll, Carousel, reparent, reorder, delete, rerender, close, and reopen paths;
- overlapping ScenePanel, particle, video, and masked surfaces.

Do not change a verified inner ScenePanel size to solve an outer composition-boundary defect. Preserve the verified inner framing and change only a proven outer owner.

## 4. Reject risky structures before runtime

Reject or explicitly justify:

- duplicate live ScenePanels representing the same reward/model;
- runtime `SetParent`, `MoveChildBefore`, or `MoveChildAfter` involving a ScenePanel or any ancestor that owns it;
- ScenePanels inside a recycled Carousel when stable ownership is required;
- animation that rebuilds, hides, or reparents the accepted reward subtree;
- ancestor `blur` or `opacity-mask` added after the verified baseline;
- transformed or oversized compositor hosts without a proven clip wrapper and collision clearance;
- overlapping 3D/particle surfaces whose z-order and bounds are not explicit;
- scheduled callbacks that can mutate a closed, rerendered, or replaced subtree;
- non-unique IDs or a selector that can bind to both the stable and animation copy.

An animation should move a stable container, focus state, or independent decorative layer around the reward subtree. It must not migrate or duplicate the live reward ScenePanels merely to imitate a reference that used 2D images.

## 5. Ownership isolation

For each controlled comparison:

1. Name the resource, stable parent, state transition, and lifecycle boundary being varied.
2. Hold all other dimensions unchanged.
3. Compare the affected parent chain and final selectors with a known-working control.
4. Enumerate overlapping surfaces, including oversized offscreen ScenePanels and particle hosts.
5. Inspect scroll offsets, clip rectangles, transforms, z-order, opacity/masks, recycling, close/reopen, and repeated-input cleanup.
6. Update the ownership classification only when the defect moves with the varied dimension.

## 6. Particle coexistence

- Verify the exact `.vpcf` resource and its camera/control-point contract with the particle playback workflow.
- Give the particle an explicit host box and z-order.
- Keep decorative particles independent of reward ScenePanel ownership and lifecycle.
- For fixed light with scrolling rewards, keep the particle outside the scrolling reward container.
- For moving light, move the particle host or its explicit animation owner; do not reparent rewards into it.
- Runtime must confirm particle bounds, lifetime, and composition.

## 7. Runtime loop

After the minimal static audit, test one hypothesis early because compositor output is engine-owned.

Define an exact project-owned oracle naming the affected UI state, expected pixels or behavior, lifecycle stages, and control case. Keep concrete page names, indices, assets, and expected content in the project's acceptance specification rather than this skill.

On failure:

1. mark the hypothesis disproved;
2. revert that attempt;
3. compare again with the verified baseline;
4. do not add a compensating size, wrapper, offset, or overlay;
5. after the second failure, restore baseline and stop.

## 8. Evidence boundary

Source inspection can prove ownership and identify risk. It cannot prove that a ScenePanel is not black in the engine. Do not report a compositor defect fixed until the runtime oracle passes.
