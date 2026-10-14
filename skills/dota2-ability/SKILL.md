---
name: dota2-ability
description: Author, materially rewrite, or diagnose the gameplay contract of a Dota 2 ability/modifier in Lua or KV, including vanilla replication, targeting, projectiles, buffs, debuffs, and damage. Use when the ability/modifier itself is the primary changed or audited artifact. Do not trigger for generic game-mode/test/shop/backend/UI logic, ability-name lookup, localization, config-only registration, or particle/sound-only work; add particle or sound Skills only when their playback contracts are independently in scope.
---

# Dota 2 Ability

Own the requested ability/modifier Lua/KV gameplay contract. Follow current project integration,
config, precache and validation rules; do not load this Skill for generic systems or name lookup.

## Evidence and routes

Current project Lua/KV proves addon behavior; current vanilla KV proves native data/cast fields;
`server.dll` proves native resource association; VPCF/soundevent plus actual callers prove playback;
authorized runtime comparison proves residual timing/visual facts. Older/public replicas and
`tools/Dota2 ability` are fallback hypotheses, never overrides for current authoritative evidence.
Read only the needed route:

- KV authoring: [ability-kv-format.md](references/ability-kv-format.md).
- Lua hooks/patterns: matching section of [lua-ability-patterns.md](references/lua-ability-patterns.md).
- Unresolved engine modifier name: [built-in-modifier-names.md](references/built-in-modifier-names.md).
- Awakening: [awaken-ability-architecture.md](references/awaken-ability-architecture.md), then only the
  matching example in [awaken-ability-examples.md](references/awaken-ability-examples.md).
- New ability scaffolding: `assets/ability-template/`; do not load templates for an existing fix.

## Scope work before extraction

1. Inspect the owning ability/KV and classify data-only, behavior, presentation or full replication.
   Read current vanilla hero/ability fields only when that native relationship is in scope.
   Complete ability/ultimate creation includes applicable sound phases unless the user scopes them
   out; omitted audio wording is not a silent-design requirement. Inspect the actual cast, travel,
   impact and termination paths, including reused helpers and early returns. A narrow gameplay fix
   only rechecks sound relationships it affects.
2. Resolve only required sources through the project's path resolver when supplied. Do not repeat
   environment/Steam probing that the project already owns. Without one, use explicit
   `DOTA2_VANILLA_KV_ROOT`, `DOTA2_CONTENT_ROOT` / `DOTA2_VANILLA_CONTENT_ROOT`, and
   `DOTA2_SERVER_DLL` or the bundled source resolver. Fail with the missing source; no hardcoded drive.
3. Unknown native presentation association uses the bundled
   `scripts/inspect-server-ability-resources.ps1 -Query <raw_ability_or_exact_native_class>`.
   Select its highest-confidence matching resource block. Skip DLL extraction for established
   unchanged resources; never scan a whole hero directory when the native association is known.
4. DLL string order does not prove attach/CP/projectile API/lifetime. Add `dota2-particle-playback`
   only for changed/unproved playback, and `dota2-sound-lookup` only for changed/unproved sound.
   Reuse verified contracts without loading both specialists.
   For new or missing sound phases, follow the project's audio integration rules and add the sound
   specialist; verify event ownership, resources, spatial source/range, stop lifecycle and precache.
5. Edit the smallest owning contract: tunables in committed config, behavior/sequencing in Lua.
   Integrate new assets through the repository's narrowest sanctioned preload owner. Resolve
   remaining uncertainty with the smallest applicable authorized evidence, not broad candidate sweeps.

## Implementation invariants

- Guard server-owned logic with `IsServer`; forward-declare early-called locals.
- Use established `Timers:CreateTimer` sequencing and entity/ability state instead of unowned globals.
- Reuse targeting, battlefield bounds, projectiles, damage and ConfigRuntime helpers required by the
  project. Random projectile directions use analytically legal battlefield intervals, not rejection
  sampling or obstacle AABBs substituted for the playable frame.
- Do not cast a vanilla ability merely for visuals unless engine cast/gameplay side effects are
  explicitly requested. Built-in modifier names remain engine-owned.
- Precache the called root resource; add children only when project/runtime evidence requires it.
  Prefer owning ability/unit or sanctioned maintenance path, not an unrelated global list. If a
  maintenance command would rewrite unrelated work, make the narrow source edit and report it deferred.

## Replication and acceptance

Only requested layers apply: cast targeting/point/gesture/presentation; travel movement/speed/radius/
lifetime; impact damage/control/area/cleanup; state immunity/dispels/interruption/death/refresh.
A full-parity claim needs authorized runtime timing and visible behavior evidence; source-only work
must name that limit. Report consumed KV, selected native class/resources, established playback,
precache and deviations/gaps once in the existing task record. No particle, DLL or runtime matrix is
needed for a local behavior fix whose relevant evidence is already established.
For complete ability creation, every applicable sound phase needs a verified playback owner or an
evidenced intentional absence. Particle completion and a sound-bearing helper do not prove the
actual ability path plays audio. Unresolved sound contracts prevent a complete-delivery claim;
report engine-only listening gaps separately without assuming permission to launch the game.
