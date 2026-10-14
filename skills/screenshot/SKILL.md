---
name: "screenshot"
description: "Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed."
---

# Screenshot Capture

Capture only the requested/authorized target. Prefer an existing tool-specific capture for browsers,
Figma or other integrated surfaces. OS capture does not authorize opening/controlling an app, changing
focus, or capturing a game/remote session. Follow the global/workspace exact-target safety rules.

## Save and select

- User-specified path wins; a user screenshot without a path uses the OS default screenshot location.
- Agent inspection uses temp storage. Report the actual saved path; inspect every returned image
  needed for the task before describing it. Multiple outputs can mean multiple windows/displays.
- Resolve this Skill directory from its provided locator and use its bundled script. Choose the
  known current OS; do not read/run other OS workflows or derive replacement capture code.
- Prefer the specific authorized app/window/region. An unidentified active window or broad desktop
  capture cannot be used to bypass game/streaming or unrelated-session capture restrictions.

## Windows

Resolve `$skillRoot` from this SKILL.md's directory. Select one invocation using actual values:

```powershell
$capture = Join-Path $skillRoot 'scripts/take_screenshot.ps1'
& $capture                                      # user screenshot, default location
& $capture -Mode temp                            # authorized inspection
& $capture -Path '<requested-output-path>'
& $capture -Mode temp -Region 100,200,800,600      # x,y,width,height from the authorized region
& $capture -WindowHandle 123456                   # supplied/verified handle
& $capture -Mode temp -ActiveWindow              # only when the active target is verified/authorized
```

Full screen is the virtual desktop across monitors. Use the authorized region to isolate one display.
These alternatives are examples, not a sequence of captures. Do not run `-ActiveWindow` just to
identify what is currently active. If focus is needed, use the already-authorized target workflow or
have the user focus it; this Skill supplies no input-control permission.

## macOS / Linux

Read only the applicable sections in [unix-capture.md](references/unix-capture.md). The Python helper
supports default/temp/explicit paths, region and active-window/window-ID options. macOS alone supports
app/title lookup and needs screen-recording preflight once; Linux chooses its available screenshot
tool. Use direct OS commands only if the bundled helper cannot run.

## Errors

Diagnose the exact missing permission, target, prerequisite or output path before a bounded retry.
Escalation is available only when allowed by the host execution policy and capture scope; never
request unsupported escalation or use it to bypass consent. Do not switch to a wider target on failure.
Always report the saved output or the concrete capture gap.
