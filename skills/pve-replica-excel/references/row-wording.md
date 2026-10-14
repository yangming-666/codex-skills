# Replica Row Wording

Use when authoring `复刻说明`; match the existing sheet. Do not impose this format on distinct logical
columns governed by `mobile-replica-columns.md`.

## Required Output Voice

Match the target sheet's actual口径 before editing. In `复刻_技能配置`, most rows use this shape:

- `【技能定位】`: one sentence describing the gameplay role.
- `【基础机制】`: behavior chain and hard parameters needed to implement it. Complex active skills usually fit most runtime facts here.
- Optional named paragraph such as `【召唤物属性】`, `【行为时序】`, `【中毒/降疗】`, or `【吞噬结算】`: use only when that sub-mechanic would make `【基础机制】` too dense.
- `【合成星级】`: active skill star damage/cooldown/interval summary.
- `【技能等级】`: passive or display-level summaries. Use this for rows whose `索敌范围` is `被动`.
- `【复刻注意】`: implementation cautions, branch ownership, and what not to collapse.

Do not write a pure program dump. Do not include source IDs, config table names, code class names, formula names, or audit-only anchors in workbook cells unless the user explicitly asks for source traceability in the workbook. Prefer "吞噬索敌半径4格，冷却60秒，单目标" over "40505 geometry_atk_range radius=6400 target_num=1 cooling_time=60000".

Keep row style consistent with neighbors:

- Active complex rows may mention separate behavior links by design name only, not by source ID.
- Simple active rows should stay short: positioning, main mechanism, star curve.
- Passive rows should use `【技能定位】初始被动技能。`, `【基础机制】`, then `【技能等级】`.
- Avoid more than one or two optional named paragraphs unless the row is summon/entity-heavy like 安妮.
