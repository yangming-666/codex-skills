# Panorama verified regression baseline

Use this process whenever a user says a UI state worked before, a previously accepted defect returned, or a structural/animation change touches an accepted subtree.

## 1. Establish evidence status

Classify the candidate baseline:

- `runtime-verified`: the user or an authorized run observed the required state working.
- `source-only`: the source relationship was inspected but the runtime result was not observed.
- `unknown`: no exact recoverable state or matching evidence exists.

Only `runtime-verified` is a visual acceptance baseline. Never silently promote a source-only snapshot.

## 2. Capture the baseline before further edits

Record:

| Field | Required value |
| --- | --- |
| Oracle | exact visible pass/fail condition and state |
| Source identity | commit plus staged/unstaged status, or full patch/hash when uncommitted |
| Files | loaded XML, VCSS, JS, data, and includes |
| Stable subtree | IDs, direct parents, dynamic constructors, and rerender owner |
| Geometry | authored sizes, offsets, transforms, clip ancestors, z-order |
| Lifecycle | create, show, animate, scroll/recycle, hide, destroy, reopen |
| Forbidden drift | accepted properties and relationships that later work may not change |
| Evidence | screenshot/log/run marker supplied or produced during authorized validation |

An uncommitted working tree is not a recoverable baseline unless its exact diff or file snapshot is preserved.

For ScenePanel work, capture a structural snapshot with:

```powershell
python scripts/audit_scenepanel_contract.py --xml <layout.xml> --css <style.css> --js <script.js> --write-baseline <baseline.json>
```

Keep task-specific baselines with the project acceptance material, not inside the global skill.

## 3. Compare before diagnosing

When the defect returns:

1. Compare the current source with the exact verified baseline.
2. List every change to the stable subtree, its ancestors, selectors, lifecycle, and overlapping compositor surfaces.
3. Treat changes after the baseline as suspects; do not reopen older accepted decisions without contrary evidence.
4. Revert suspect groups in reverse order or bisect them. Do not compensate for a regression with a new unrelated change.

Run structural comparison with:

```powershell
python scripts/audit_scenepanel_contract.py --xml <layout.xml> --css <style.css> --js <script.js> --baseline <baseline.json> --enforce-baseline
```

The tool reports structural drift and risky constructs. It cannot prove rendered correctness.

## 4. Mutation budget

Before editing, enumerate the only owners allowed to change. Any newly discovered required owner expands the contract explicitly before modification.

For a local regression, default to:

- one hypothesis;
- one owning change group;
- one runtime oracle;
- zero unrelated cleanup or redesign.

Do not change content assets, model framing, parent structure, and animation timing in the same attempt.

## 5. Rollback rules

- A contradicted attempt must be reverted before the next attempt.
- After two failed attempts for the same visible relation, restore the verified baseline and stop incremental patching.
- If the baseline cannot be recovered, report that fact. Do not reconstruct it from memory and call it equivalent.
- Preserve the user's staged state and unrelated working changes while restoring task-owned files or hunks.

## 6. Handoff

Report separately:

- baseline status and identity;
- current drift from baseline;
- changes made and reverted;
- source checks completed;
- exact runtime oracle still required;
- whether the result is source-only or runtime-verified.
