---
name: pve-replica-excel
description: Update requested rows in an existing PVE hero-skill Excel workbook whose schema and target rows already exist, converting config/buff/passive/behavior-tree/mobile-unpack evidence into implementation-ready rules, values, evidence, and 复刻说明 while preserving workbook structure. Do not trigger for source-only gameplay analysis, implementing a replica in code, creating a workbook, restructuring sheets, or broad dataset/economy audits; use analyze-excel-data-structure for those spreadsheet-structure tasks.
---

# PVE Replica Excel

Update only requested rows/cells in an existing schema. Preserve workbook sheets, headers, style and
physical columns. A new/restructured workbook belongs to `analyze-excel-data-structure`; use the
appropriate standalone spreadsheet or live Excel execution surface for the actual edit.

## Select row scope before sources

Identify base main skill, display/skill-level summary, unlock/step-up, strengthening/rogue,
special/ultimate or runtime note. Only effects active in that row belong in it. Same-name skill
variants do not justify combining later levels, buffs or progression layers.

| Current need | Required reference |
| :--- | :--- |
| Mobile source ownership, base/star damage, interval/cooldown derivation | [mobile-source-model.md](references/mobile-source-model.md), only used layers/formulas |
| Writing implementation-facing `复刻说明` | [row-wording.md](references/row-wording.md) |
| Sheet separates `程序复刻规则`, numeric payload and evidence | [mobile-replica-columns.md](references/mobile-replica-columns.md) |

Do not load star derivations for a row that only changes control/timing. Follow deeper references
only for unresolved implementation-critical values owned by the row, not every reused base mechanic.

## One mechanism and evidence record

Before drafting, extend the task's existing record for each affected state/branch with:

- trigger, probability/count, owner, target/filter and transition;
- geometry/range/target-count versus independent visual/model/projectile scale;
- damage coefficient, additive/final modifiers, type/critical/layer application;
- delay, interval, duration, ticks, cooldown, reset/removal;
- stacking base and rule: additive, multiplicative, replacement, cap or exclusion.

Include applicable implementation-critical items; this is one completeness record, not separate
mechanism maps, parameter checklists and delivery reports. Confirm each value and scope from direct
source. Mark unresolved items `缺失` or `仍需实机确认`; never infer geometry/visual scale from damage,
chance, a neighbor or summary. Calculate multi-stage results only after proving their reference base
and sequential/independent ownership. Populated cells do not prove a complete replica.

## Source and wording boundaries

- Workbook neighbors own style. Authoritative mobile config, executed rules and relevant runtime
  evidence own facts; old audit notes are locators, not current truth. Keep display text distinct
  from runtime behavior. Resolve custom geometry/timing/filters through the relevant behavior-tree
  or decompiled action, without browsing unrelated skill trees.
- Base rows omit later unlock, rogue, totem, equipment, skin, co-op and ultimate numbers. If needed,
  name their separate layer without importing its values. Explicit unlock/summary rows include that
  layer's values with the base distinguished.
- Units: `1600 = 1格`; convert milliseconds to seconds unless precision needs exact ms. Separate
  source thousandths coefficients from final requested star/effective multipliers. Persistent effects
  include only their complete trigger/target/tick/duration/stack/damage/cap contract; star scaling
  belongs only when requested or actually star-dependent. Ordered-hit final modifiers are not stars.
- Behavior-tree time is relative to its owning action unless cast-start ownership is proved.
  A relevant live observation can contradict config-only geometry; preserve the observed behavior
  and mark the unresolved relationship. If UI duration and Buff duration disagree, identify both
  and which governs runtime. Never turn uncertainty into a concrete formula.
- `复刻说明` contains positive implementation values/behavior/necessary branch cautions. Keep source
  IDs, table/class names, derivations and audit narration in evidence/private notes, unless explicitly
  requested in the workbook. Dedicated `证据` columns retain traceability. Confirmed hard values go in
  the implementation/numeric column, not hidden inside `复核结论`.
- Keep `复核结论` brief: `无确认缺失。`, `无关键缺口；...已确认。` or
  `缺失：...。已确认：...。`. Every unresolved critical item must appear there. No “complete” claim
  while such items remain, even if the sheet is styled and all standard fields are filled.

## Edit and verify once

1. Inspect/render the target area; locate by hero and skill/enhance identity and read current values.
   Start with 2–3 analogous rows for conventions; expand only if styles/scope conflict, not a fixed
   5–10-row quota. Reuse a known convention across the requested rows.
2. Complete the scoped mechanism record, then write concise matching prose. Each cell sentence must
   supply an implementation parameter, behavior relationship or concrete necessary caution; remove
   derivation, proof-only text, irrelevant layers and speculative mechanics.
3. Review against the same record: every branch has trigger/owner/target/transition; damage, geometry
   and visual values stay distinct; units/bases/stacking are proved; gaps are explicit.
4. Inspect the edited range, formulas and preserved structure; render affected output when supported
   by the execution tool. Reuse the execution surface's file/visual checks rather than running a
   second generic workbook audit. Report the saved artifact and unresolved scope once.
