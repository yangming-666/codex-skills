# Mobile Source and Star Model

Read only the source layers and formulas used by the target row. Existing workbook conventions own
wording, not factual authority. Behavior/config/runtime evidence owns values and mechanics.

## Mobile PVE Concept Layers

Keep these layers separate before writing `复刻说明`:

- `主技能入口`: `SkillData__data_skill_lev_up.lua` defines the hero display skill, display levels, and links to `logic_dmg_skill_id` / `logic_cooling_skill_id`. Use this to decide which skill row is the main active/passive being documented.
- `合成星级设计`: `HeroData__data_get_base.lua` defines `hero_dmg_rate`, `star_atk_factor`, `star_atk_speed_factor`, and `star_buff`. `tools/build_hero_merge_star_md.py` is the canonical planning derivation for main-skill 1-4 star damage and cooldown/interval curves.
- `底层逻辑技能`: `SkillData__data_skill_lev.lua` gives base skill coefficients such as `dmg_factor`, `interval_time`, `cooling_time`, target counts, bullet counts, passives, and config ranges. These are bottom-layer anchors, not final per-star replica multipliers by themselves.
- `Buff/Passive机制`: `BuffData` and `PassiveData` define DOT ticks, debuffs, triggered skills, durations, and condition chains. Express these as their own behavior contracts, then project star-only coefficients only when the damage path supports that formula.
- `局内强化/增强`: `RogueData`, `LevelEventData`, strengthening buffs, and hero-specific enhancement passives alter the base skill. Do not fold them into base 1-4 star main-skill coefficients unless the user explicitly asks for a strengthened-state row.
- `行为树/反编译运行时`: extracted skill blocks and C# sources resolve custom geometry, visual timing, runtime hitbox construction, target filters, and display/runtime disagreements. Use them to audit facts, especially when screenshots conflict with table geometry.


## Star planning

For main skill star planning, use this design口径:

- Direct skill damage multiplier: `hero_dmg_rate / 1000 * logic_dmg.dmg_factor / 1000 * star_atk_factor / 100`, equivalent to `hero_dmg_rate * dmg_factor * star_atk_factor / 100000000`.
- Skills driven by `interval_time`: `actual interval = interval_time / (star_atk_speed_factor / 100)`.
- Fixed cooldown skills: start from `cooling_time`, then apply confirmed star cooldown/passive modifiers only if present.
- Persistent damage effects: describe only the fields needed to reproduce that specific effect. Typical fields include trigger, target, duration, tick cadence, stack/refresh rule, damage倍率, damage type, and caps, but do not force every effect into the same template.
- Runtime internal modifiers such as ordered-hit `finalDmgRatio` tables are hit-distribution or final-damage adjustments, not star multipliers. Add them only when they must be implemented; keep them out when they do not affect the requested row.
