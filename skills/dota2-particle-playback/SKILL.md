---
name: dota2-particle-playback
description: Identify, implement, recreate, modify, or debug a Dota 2 gameplay particle playback contract using authoritative ability association and real `.vpcf` evidence for attachment, control points, movement, lifetime, children, cleanup, and precache. Use when particle behavior/resource identity is a requested or unresolved artifact. Do not trigger when a verified particle path is merely preserved, displayed as text, copied unchanged, or added to an existing proven preload list, nor for cosmetic VMAP-owned particle composition.
---

# Dota 2 Particle Playback

Establish the requested root's caller, CP, movement and lifetime contract from current evidence.
A verified unchanged path or preload entry does not need a new playback investigation.

## Evidence and lookup

- Current native DLL strings prove ability/resource association, not attach mode or CP values.
  VPCF operators prove consumers/drivers/lifetime; current Lua/native calls prove caller inputs.
  Preview drivers do not necessarily describe production callers. Authorized runtime resolves only
  remaining engine ambiguity or visual parity.
- Use the project's path resolver; without one use configured Dota roots/known install evidence.
  Unknown native association uses the existing extractor route in
  [vpcf-inspection.md](references/vpcf-inspection.md). Known custom/root paths skip DLL extraction.
  Do not load ability-authoring templates merely for association lookup or scan whole hero folders.
- Read the exact root and only active children affecting caller CPs, movement, timing or the requested
  visual/endcap. Do not recursively dump unrelated visual leaves. Reuse already-established evidence.

## Native replication and restoration

- Before rewriting a native effect, establish a baseline using the unmodified packaged root,
  its active child hierarchy and source-supported caller inputs within the native parameter range.
  Reuse verified baselines; unavailable runtime leaves visual parity unverified.
- Preserve native movement, model-renderer and snapshot ownership unless evidence identifies an
  incompatibility. Spawned model entities are not equivalent substitutes for particle models;
  account for animation, skinning and lifetime before proposing a replacement.
- For test-only work, isolate callers, resources and reload paths from production. When asked to
  restore, recover the identified historical caller, affected dependencies and compiled resources;
  do not reconstruct an approximation or include new fixes.

## Establish the contract

1. Match actual caller attach mode/CP values against VPCF consumers. Separate caller inputs from
   internally generated CPs; never infer a CP from index, filename or native string order.
2. Name one movement owner before choosing APIs: projectile engine, particle operators or Lua caller.
   Use tracking projectiles only for a proved standard contract, not arbitrary manual CPs.
3. Verify emit duration, particle lifetime, decay/stop/endcap and every owning cleanup path. For a
   buff/follow effect include attachment and endcap removal; for a one-shot use its finite lifecycle.
4. Verify the repository's narrowest root-resource precache owner. Children are not extra entries
   unless project/runtime evidence requires them.

Use the lightest sufficient depth: proven one-shot caller → relevant CPs/lifetime only; buff/follow →
attachment and cleanup; projectile → destination/speed/orientation/cutoff. Packed, conflicting or
undocumented vectors need component-level consumers and confidence. No full CP table for a simple
proven call. The inspection reference supplies field details only when needed.

## Playback invariants

- `m_Children` signals a wrapper; inspect relevant active branches. `m_nOverrideCP` is an input
  reference whose meaning comes from operator and caller, not its name.
- Set particle-driven destinations once; avoid per-frame Lua motion when particle/projectile owns it.
- Do not guess HSV/tint CPs or overwrite internal CPs. A proven root/child component conflict may
  require a minimal wrapper/remap; do not force incompatible meanings into one vector.
- Suppress/separate endcaps only if they obscure movement diagnosis. Preserve the complete effect's
  accepted terminal behavior when implementing the final playback contract.

## Bounded validation and handoff

Use a focused authorized test only for a remaining hypothesis: short/long distance, once/updated
CP when ownership is unclear, source-supported packed values, or lifetime/speed cutoff. Stop broad
sweeps when caller and VPCF agree; do not retry rejected candidates without new evidence. A runtime
need does not authorize launching, controlling or capturing a game/remote session.

Build success is not visual acceptance. Observe movement and termination across frames when those
contracts are affected. Attribute a cause only to an isolated change or independent evidence;
success after several simultaneous changes proves the combination, not a unique root cause.
Native-range success does not establish parity for extended parameters or concurrent instances.

Record once in the existing task evidence: root/relevant children, ability association, attach/caller
CPs, movement/update owner, lifetime/cleanup, precache and unresolved facts. No second CP/report
ledger is required for already-proved facts.
