---
name: dota2-sound-lookup
description: Identify or verify a Dota 2 sound event, its resource/dependency closure, loop/stop relationship, playback API, or precache ownership from source or VPK evidence. Use when sound identity/playback is requested, changed, missing, disputed, or unverified. Do not trigger when an already-proven event/resource is merely preserved, renamed only in prose/localization, or appears incidentally in gameplay/UI code with no sound change.
---

# Dota 2 Sound Lookup

Resolve the exact event and underlying resource. Never guess from an ability, hero, or voice-line name.

## Workflow

1. Extract the token and originating API/KV field from source code.
2. Search local source `.vsndevts` files before compiled or vanilla sources.
3. When the workspace provides `tools/soundevent_finder_gui`, use it for VPK event-block lookup.
4. Resolve `pak01_vpk` through the workspace path resolver when available. Otherwise pass `--vpk-path`, use `DOTA2_VPK_PATH`, or let `scripts/lookup_sound.py` probe standard Steam library layouts.
5. Search the most specific soundevent scope first: hero, item, addon/UI, then global.
6. Inspect the full matching event block and follow layer, limiter, block, loop, and stop dependencies.
7. Resolve every referenced `sounds/*.vsnd` or compiled resource when available.
8. Report event, resource, source file, originating API, loop/stop relationship, and unresolved ambiguity.
9. When integrating playback, follow project custom-event and spatial-tuning rules. Trace the actual
   emitting entity/location and each audible layer's spatial fields or proven inheritance; distinguish
   spread from attenuation distance and from gameplay radius/diameter. Verify moving-source ownership,
   applicable stop paths, sequence/concurrency policy and precache in the existing task evidence record.
   A lookup-only request does not require changing these integration owners.

## Rules

- Treat sound API strings and precache entries as lookup inputs, not proof of a complete mapping.
- Prefer source `.vsndevts` over compiled `.vsndevts_c`.
- If only compiled assets exist, extract printable strings and label the evidence accordingly.
- Keep the API call and resolved string together in reports.
- Do not claim completion until both the event block and resource mapping have been checked when both exist.
- When copying an event, copy its complete verified parameter and dependency closure before applying project-local overrides.
- Project-specific tuning belongs in project documentation, not this global skill.
- Fail fast when the VPK or required event/resource cannot be resolved.

## Commands

In a workspace with the standard resolver, resolve this Skill's directory as
`$skillRoot` from the current `SKILL.md`:

```powershell
$paths = & tools/resolve_project_paths.ps1
python (Join-Path $skillRoot "scripts/lookup_sound.py") --vpk-path $paths.pak01_vpk "<event-or-resource>"
```

From this Skill directory without a project resolver:

```powershell
python scripts/lookup_sound.py --vpk-path "<pak01_dir.vpk>" "<event-or-resource>"
python scripts/lookup_sound.py --vpk-path "<pak01_dir.vpk>" --source "<lua-kv-or-panorama-source>"
```

Use `tools/soundevent_finder_gui` instead when it is present and suitable; pass the resolved VPK path explicitly rather than relying on tool-local machine defaults.

See `references/sound-workflow.md` for search order and reporting.
