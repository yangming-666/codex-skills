# Panorama validation

Run validation only when the user requests it or the repository policy requires/allows it. A repository prohibition on automatic Panorama checks overrides the defaults below.

Resolve commands relative to the current skill directory; never embed a user directory or `$CODEX_HOME`.
Choose only the evidence lane required by the task. This page is a command catalog, not a sequence
to run. Reuse valid task/host checks; do not create contract/mapping/relation artifacts for a local
fix unless its design actually requires them. A repository delivery gate still needs the exact request.

## Syntax

```powershell
python scripts/check_panorama_syntax.py --paths <changed-source-files>
```

Use for new layouts, new WorldPanels, include/path changes, or structural refactors when authorized.

## Draw.io contract and shell

```powershell
python scripts/extract_drawio_contract.py --drawio <design.drawio> --out <contract.json>
python scripts/generate_panorama_replica.py --contract <contract.json> --xml-out <layout.xml> --css-out <style.css>
```

## Static layout

```powershell
python scripts/check_panorama_layout.py --contract <contract.json> --xml <layout.xml> --css <style.css> --map <mapping.json> --relation-rules <relations.json> --enforce-direct-parent-mapped --enforce-inside-parent-mapped
```

Add required IDs/selectors, critical selectors, allowed flow selectors, and scroll selectors for the actual task rather than copying an unrelated screen's list.

Mapping entries should identify selector, direct `parent_id`, and geometry properties. Relations should encode center equality, gaps, ratios, and the agreed tolerance.

This checker is only for a mapping-backed fixed contract. It parses authored selectors and pixel properties; it is not a Panorama cascade, flow, `fit-children`, transform, or computed-layout engine. Do not use a passing result as a substitute for `layout-proof.md`. For local corrections without a design contract, the parent-chain proof is the primary static gate.

`git diff --check` only checks patch whitespace/errors. It does not validate XML structure, VCSS cascade, layout, design alignment, dynamic parents, assets, or runtime state. Never cite it as source layout acceptance.

## Relation sheet

```powershell
python scripts/generate_relation_sheet.py --contract <contract.json> --mapping <mapping.json> --relations <relations.json> --out <replica_relations.md>
```

## Runtime

Collect geometry with `scripts/dump_runtime_layout.js` or the project's `GameUI.ReplicaDumpLayout` integration, then run:

```powershell
python scripts/check_runtime_layout.py --contract <contract.json> --dump <runtime_dump.txt> --map <mapping.json> --relation-rules <relations.json> --enforce-inside-parent-mapped
```

Require the selectors and visible selectors appropriate to the current screen. Finish with a screenshot comparison when strict visual fidelity is in scope.

### Restart or drive a running addon

Follow the host project's runtime-acceptance contract. Do not invent a VConsole2 command, use Hammer
as a launch substitute, restart a broader process, or explore desktop launch paths merely because
runtime validation is requested. Prefer project-owned CLI launchers, test-only VConsole2 commands,
runtime probes, and direct screenshot artifacts. Use the changed source's loading contract to select
the smallest sufficient hot reload, reload or process restart within existing lifecycle authorization.
Perform it, await readiness, rediscover current connections/windows and verify that the change loaded;
stale bindings after restart are expected, not task failure. Keep transient connection details in the
runtime owner rather than standing instructions. Choose recovery or an alternate authorized route by
total completion cost, with commands preferred. Official `$computer-use:computer-use` remains available
when command routes cannot efficiently complete the step. Do not request authorization already covering
the target, operation and effect. Resolve uncertain prior effects before replaying, submit verified
console commands one at a time, observe completion and attribute evidence to the route actually used.

## Visual and interaction matrix

Static geometry for the default state is insufficient. Before claiming completion, inspect every state selected in the applicable contract from `visual-delivery-loop.md`, including:

- visibility, selection, enabled, and availability variants that apply;
- meaningful minimum, maximum, empty, populated, loading, and error data;
- navigation or pagination states whose content differs;
- secondary surfaces through open, focus/input, submit, and cancel where applicable;
- repeated interactions and asynchronous responses.

Verify coupled text/data, exact assets, hit targets, focus, hover/active behavior, and stable shell geometry. A local toggle must not flash or rerender unrelated rows.

## Isolated runtime batch and visual oracle

Runtime inspection must have a batch boundary and an explicit visual oracle. A screenshot is not
self-interpreting, and VConsole2 output containing old messages is not evidence about the current build.
Use only the current authorized VConsole2 session for console evidence. Treat runner/probe reports as
separate run-scoped evidence.

Before triggering the affected UI:

1. Record the changed-source scope and the exact runtime action that will exercise it.
2. Clear the current VConsole2 view or insert a unique run marker, then use only VConsole2 messages after that boundary.
3. Reach the target through the repository-approved reload path. Do not restart a broader process when
   the project defines a narrower reload action.
4. State the observable signature in parts. For an animated corner this might be horizontal arm,
   vertical arm, connected joint, hue/falloff, target edge, and required lifetime. Never accept a
   substitute signal merely because it occupies a similar pixel location.
5. Remove confounders before capture: move the pointer away, disable selection/hover where practical,
   and distinguish UI borders, focus rings, image highlights, and particle layers by owner.
6. If two owners can plausibly produce the same pixels, capture a paired control with the target effect
   disabled or absent. The claimed pixels must change with the target owner while the confounder remains.
7. Sample every time/state named by the contract: initial stable frame, steady-state hold, interaction,
   scroll/recycle, close/reopen, and repeated input when applicable.

Classify every post-boundary VConsole2 entry before acting:

- **introduced and owned by the delta:** fix before acceptance;
- **pre-existing or outside the changed owner:** record separately and do not spend the task on it;
- **uncertain ownership:** trace the resource/call owner from source before deciding.

The runtime evidence packet must contain the run boundary, tested action/state, expected signature,
confounders excluded, sampled times, screenshot result, and post-boundary VConsole2 classification. A
visual pass without this packet is observational, not acceptance evidence.

If runtime contradicts a prior pass, invalidate the pass immediately. Identify whether the missing
gate was source geometry, lifecycle, owner identity, state coverage, or the visual oracle itself, and
add that category to the generic process. Keep concrete entity names, pixel offsets, assets, and page
states in the project's acceptance specification or validator rather than this reference.

## VConsole2 evidence

- Inspect warnings only in the current authorized VConsole2 batch.
- Resolve warnings introduced by changed source, including missing resources, invalid VCSS properties, and failed localization.
- Do not attribute a visual defect to compilation, caching, or stale output without a concrete load/compile error in the current VConsole2 batch.
- In auto-compiling Panorama projects, treat the displayed result as the current implementation until evidence proves otherwise.

## Screenshot handoff

Never use a screenshot to discover a parent-chain, flow-order, or authored-box error that source can prove. After `layout-proof.md` passes, use one early smoke screenshot only when runtime structure remains uncertain. Then batch source-proved fixes and request one final screenshot set for the affected state matrix. Report source proof, source inspection, and runtime verification separately.

If runtime exposes an authored relationship error, invalidate the source pass and add the missing invariant to the design/source proof before further implementation.
