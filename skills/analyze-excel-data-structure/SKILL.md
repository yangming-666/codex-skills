---
name: analyze-excel-data-structure
description: Analyze game numerical/config/unpacked/runtime data and infer field relationships, evidence strength, curves, or economy specifically to design, restructure, complete, or audit an Excel/CSV/TSV workbook as the requested deliverable. Use for 数值策划表、等级×品质/成本/奖励/属性对照、缺失数据考据补全、曲线经济验证、字段关系驱动的表结构设计，或工作簿完整性/可追溯性审计. Do not trigger for ordinary KV/Lua/config/code analysis, Markdown tables, or source-only reports when no spreadsheet artifact or spreadsheet-structure decision is requested.
---

# Game Numerical Workbook Design

Build a verified numerical/semantic model before formatting the requested workbook. This Skill owns
spreadsheet structure/evidence decisions; ordinary source analysis without a workbook does not use it.

## Required routes

- Values, dependencies, curves or inference: read the relevant sections of
  [senior-planner-reasoning.md](references/senior-planner-reasoning.md).
- Choosing/changing structure: [decision-model.md](references/decision-model.md).
  An explicitly fixed structure needs validation against requirements, not invented alternatives.
- Delivery: [quality-gates.md](references/quality-gates.md), only applicable gates.
- Revising/evaluating this Skill: [evaluation-cases.md](references/evaluation-cases.md); ordinary
  workbook work does not load evaluation fixtures or past solutions.

## One decision/evidence record

Maintain one compact record of requested decision, dimensions/measures, units/full coverage,
mandatory lookup/comparison/edit/import operations, authorized inputs, inference permission and
requested artifact. Add lineage, key/dependencies, coverage, formula/inference verdict and chosen
structure to it as established; do not repeat it as separate gate reports.

Only authorized inputs may be used. Capability tests exclude prior solutions, reference workbooks,
screenshots and generated reports unless explicitly supplied as authorized test inputs. References
can contaminate structure reasoning even without copied numbers. Do not add fields/sheets/provenance
columns unless they serve the requested operation. Resolve material scope ambiguity before authoring,
or make an explicitly reversible assumption when safe.

## Establish the model

1. Separate authoritative config/decoded/runtime/executable rules, reproducibly resolved evidence,
   contextual design/user rules, references and the target artifact. Every requested measure needs
   field-level lineage; unresolved pointer/unit/resource/key facts remain explicit. A directly stored
   requested value remains direct even when an auxiliary lower-level representation is encoded.
2. Profile actual records for grain, minimal unique key, dimensions/measures/units and functional
   dependencies. Enumerate the complete authoritative dimension domain before collapsing it;
   verify every member/exception and identify unobserved members. Remove a dimension only when it
   changes no requested measure and is unnecessary for lookup/comparison. A dedicated measure may
   represent an exceptional category when that fits the operation without redundant dimensions.
3. Verify applicable formulas, rounding, caps, probabilities, unlocks, tiers, breakpoints and
   player-facing source/sink/marginal-cost/refund behavior. Expected keys come from rules, not just
   extracted observations. Never replace requested coverage with a convenient baseline/sample.
4. Classify values `direct`, `resolved`, `estimated` or `unavailable`. Estimates require user permission,
   a causal/structural basis, independent/holdout validation, competing-model comparison and recorded
   error/extrapolation/rounding/breakpoints/confidence. Training fit or an unobserved category does not
   justify an exact value. Keep estimates distinguishable; unsupported numbers stay unavailable or
   in an explicitly separate scenario. Completeness means accounting for every expected key/state.

## Choose and author

- For an open structure decision compare at least two viable shapes; reject mandatory-operation
  failures before scoring. Use scores only when multiple surviving shapes have material tradeoffs.
  Record the decisive reason concisely. A prescribed valid shape needs no alternative-design report.
- Human comparison of two finite ordered dimensions with repeated measures defaults to one continuous
  cross-tab: larger dimension on rows, smaller dimension in grouped columns, measures within groups.
  Filtering/import/record editing as the explicit primary operation can favor a normalized table.
  Width alone cannot justify splitting required comparisons across sheets/sections.
- A composite requires distinct mandatory operations; summary requires requested aggregation.
  Avoid automatic canonical/detail/parameter sheets when one comparison view suffices.
- Reconcile expected combinations and layout arithmetic before writing: data rows = row members;
  columns = row-key columns + column members × measures; data cells = expected keys × measures.
- Canonical tables use typed numbers, stable keys, one header row, filters, auditable formulas and
  no body merges. Comparison views use clear grouped headers, anchored row keys and consistent
  groups. Prefer compact evidence legends/fills/notes over repeated value/state/basis columns.
- Use the spreadsheet execution surface for authoring/rendering. Reconcile all affected views to
  one model and apply the quality reference; reuse its file/formula/render evidence. Formatting
  cannot cure a source, inference, operation or file failure. Deliver only the requested artifact;
  if a required gate fails, investigate or report the exact gap, never label it complete.
