# Panorama visual hierarchy and chrome ownership

Use this reference when a task creates or changes backgrounds, borders, dividers, shadows, glows,
accent lines, or material styling. Apply it in proportion to the task so the guardrail improves
decisions without turning a local correction into a page-design exercise.

## 1. Choose review depth

- **Local correction:** write a short note naming the affected focal/supporting relationship and the
  treatments being added, changed, or removed.
- **Component or secondary modal:** use a compact ledger for materially visible changed treatments.
- **Page redesign, three or more nested framed surfaces, or repeated hierarchy feedback:** use the
  full hierarchy and chrome ledger.

Do not inventory untouched decoration or nonexistent states. Increase review depth only when scope,
uncertainty, nesting, or repeated failure justifies it.

## 2. State the applicable hierarchy

Identify only the roles present in the target:

- focal object, outcome, message, or decision;
- primary and secondary actions, when the UI is interactive;
- supporting information needed to understand or act;
- tertiary help, metadata, or status;
- background support and atmosphere.

An informational HUD, notification, or passive display may have no primary action. A browse table may
deliberately distribute emphasis across repeated rows. Judge hierarchy against function rather than
forcing every interface into a reward-modal pattern.

## 3. Review chrome ownership

At the selected depth, review materially visible treatments changed by the task:

| Panel/selector | Treatment | Owner role | Meaning or state | Evidence | Keep/change/remove |
| --- | --- | --- | --- | --- | --- |
| reward card | rarity border | item state | quality | shared rarity selector | keep |
| wrapper | one-pixel line | none | none | current implementation only | remove |

Useful reasons include, but are not limited to:

- the page or modal shell when it needs separation from the world;
- the primary content surface when it is the focal object;
- a selected, focused, hovered, disabled, locked, owned, or equipped state;
- rarity, team, danger, success, or another data-backed semantic state;
- a repeated table axis where a divider materially improves scanning;
- an interactive control whose boundary communicates its hit target or priority.
- a material or decorative treatment present in the selected prototype that supports hierarchy and
  does not compete with stateful or interactive emphasis.

“Dota style,” “more detailed,” “adds depth,” “fills empty space,” and “looks unfinished without it”
are insufficient reasons by themselves. They may describe intent, but the implementation still needs
a prototype, material, hierarchy, interaction, or state relationship. Current addon styling is wiring
evidence, not design evidence.

## 4. Choose separators deliberately

Consider these tools from quieter to stronger:

1. spacing and grouping;
2. typography, alignment, and contrast;
3. one shared surface owned by the group;
4. a divider or border with a recorded scanning, state, or containment purpose.

Prefer the least intrusive option that preserves the selected prototype, scanning behavior, and
interaction clarity. This is a heuristic, not a mandatory sequence: dense tables, exact references,
focus states, and compact controls may require borders or dividers directly. A visual surface may
exist without an outline, and a layout wrapper does not automatically need a surface.

## 5. Review frame nesting

Trace changed visible surfaces through their XML ancestors. Repeated background, border, shadow,
inset, or accent treatment is a risk, not an automatic failure. Keep it when layers express distinct
containment, material, interaction, state, or prototype roles and the combined result preserves priority.

Common failures:

- modal border + header border + section border + card border with equal emphasis;
- a framed content area containing framed rows that contain framed stat cells;
- top and bottom accent lines plus a complete outer border expressing the same shell edge;
- decorative dividers between regions already separated by spacing and contrast;
- identical gold edges on shell, metadata, reward cards, and buttons, erasing priority.

When nested chrome has no useful distinction, remove the lowest-information treatment first.
Preserve stateful borders such as selection and rarity before decorative container borders.

## 6. Control emphasis

- Allocate the strongest contrast, glow, saturation, or warm accent to the intended focal region or
  interaction state. Balanced browse and comparison layouts may intentionally have multiple peers.
- Keep supporting surfaces lower contrast than their content and lower emphasis than the focal region.
- Use semantic color locally. Do not wash an entire page in success, rarity, or faction color unless
  that state owns the whole page.
- Let atmosphere particles and background art support the shell; they must not create a second focal
  region or become a substitute for content hierarchy.
- Keep disabled styling visibly subordinate without changing geometry or hiding required costs.

## 7. Check applicable states

Audit only states supported by the component contract, such as initial, loading, empty, populated,
maximum-density, error, enabled, disabled, hover, active, selected, or reopened. The shell must remain
stable where required, and state chrome must appear only when its owning state is true.

For dynamic cards, record constructor parent, applied semantic classes, deletion owner, and rerender
events. Confirm that a neutral base does not override rarity or selection selectors in the final
cascade.

## 8. Proportional reject gate

Reject delivery only for a material failure in an applicable item:

- Does the visual priority match the interface's function and selected prototype?
- Do materially visible treatments changed by the task have a defensible hierarchy, state,
  interaction, material, or prototype reason?
- Are stateful borders and glows absent when their state is false?
- Do repeated nested frames preserve priority and express distinct roles?
- Does the final selector cascade preserve semantic rarity, selection, focus, disabled, and error states?
- If the same accent is reused across shell, content, metadata, and actions, does the resulting contrast
  still communicate priority?

Report only what the selected review depth proves. Use runtime for engine-specific material,
particle, glyph, or compiled-image appearance, not to compensate for an unresolved source relationship.
