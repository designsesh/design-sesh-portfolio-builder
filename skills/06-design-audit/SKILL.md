---
name: design-audit
description: Audit and correct an implemented website against its selected visual direction, palette, personality brief, content evidence and page blueprints. Reconcile the final implementation and maintenance notes after desktop and mobile work.
---

# Design Audit

Execute in the current website workspace. Read [METHOD.md](../../METHOD.md) once per workflow. Use available inspection, browser and file tools; do not assume a particular framework, connector or runtime. Preserve original assets and the agreed scope. This skill audits the actual output against prior decisions; it does not invent a new identity or generate images.

## Purpose and place in the workflow

Run after the foundation, Projects, About and [mobile adaptation](../07-mobile-responsive-design/SKILL.md) work, or after a meaningful revision. Check whether the site delivers what the earlier skills documented. Fix supported implementation defects, retest them and leave an accurate record of the delivered system.

This combines design/usability review and the useful parts of handoff: current identity, editable source locations, actual verification and remaining work. There is no separate handoff stage. Do not require earlier stages to be rerun when their existing outputs remain valid.

## 1. Establish the active specification

Read the current versions of:

- `design-notes/01-reference-audit.md` and relevant reference IDs/images.
- `02-personality-brief.md`, `11-selected-palette.md` and `03-selected-direction.md`.
- `12-personal-story.md` and `04-site-blueprint.md`.
- Per-project audits, evidence ledgers, case-study plans, asset manifests and maps.
- `05-build-notes.md`, Projects/About build notes and mobile plan/review.
- `decision-log.md`, `progress.md`, repository instructions and existing implementation status.

Use actual paths if the project uses a different convention. Inspect code, templates, content data and the rendered pages. Read notes as specifications, not proof that the described behaviour exists.

Resolve precedence explicitly: the latest applicable user instruction takes priority, then active selected decisions, then current plans. Earlier rejected experiments are historical. If notes conflict, record the conflict and use clear later decisions where available. Ask only when the conflict affects identity, facts or scope and cannot be resolved. Do not silently rewrite the specification to make the implementation pass.

For absent documents, record the coverage gap and audit what can be established. A missing personality brief does not justify inventing traits; a missing browser does not establish visual fidelity.

## 2. Build a specification-to-output matrix

Translate the active documentation into concrete checks before adjusting CSS. Include source paths/headings or decision IDs and actual routes/components.

| Requirement source | Expected output | Route / component / state | Observed output | Evidence | Status | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Selected palette, link role | Links use the approved role and usable state contrast | Home, Projects and About | Actual values and appearance | Computed value / measured pair / screenshot | matched / mismatch / unresolved / unverified | Specific fix or decision |
| Case-study plan, chapter 3 | The drawing explains the recorded design decision | Project detail | Figure, caption and source | Asset ID and inspected source | Same status set | Specific fix |

Cover at least these requirement classes:

1. **Visual direction:** composition, type hierarchy, density, imagery, crop/scale, alignment, rhythm and chosen personal details.
2. **Shared system:** active palette roles, fonts/fallbacks, spacing, surfaces, header/footer and documented exceptions.
3. **Content/voice:** confirmed introduction, intended tone, role/contribution, chapter emphasis, correct metadata and next actions.
4. **Evidence/assets:** correct selected version, source-derived claims, labels, privacy/permission, captions and inspectable drawings/interfaces.
5. **Behaviour:** navigation, actual destinations, interactive states, motion/static fallbacks and progressive enhancement.
6. **Mobile adaptations:** approved substitutions preserve the original purpose, information and identity while supporting touch.

“Looks good” is not a status. Matching hex values is not proof that the overall composition matches. A selected direction's scale contrast or negative-space principle should be visible in the actual layout. Do not demand literal reproduction of an inspiration image where the selected direction intentionally differs.

## 3. Inspect complete visitor journeys

Walk Home → Projects → one detail page → About → contact/next step, plus direct entry to a detail URL. Inspect every changed page and representative pages consuming changed shared code. Prioritize longest titles, densest text, largest drawings, unusual aspect ratios, interactive sections and the final footer.

Use narrow, intermediate and wide sizes appropriate to the implementation; useful starting widths are 390, 768 and 1440 CSS pixels. Include mobile review evidence rather than rerunning every specialist check without a reason. Inspect relevant scroll positions and states, not only the first viewport.

For visual review, compare the selected specimen and rough maps with the rendered content. Look for accidental empty regions, mismatched image heights, repeated equal-weight chapters, crops that hide evidence, oversized typography, unreadable small notes and excessive scrolling between sparse content. A project's distinct composition should still feel part of the shared identity.

For interaction review, exercise actual links, chapter anchors, menu/disclosure state, image enlargement, filters if any, media controls and contact/download paths. Check keyboard focus visibility/order, touch alternatives, browser back and fixed-element clearance. A button's presence does not prove its action works.

Inspect content against sources: confirm contribution and completion claims, supported numbers, prototype versus final labels and public-use status of the selected exports. Do not expose private source paths, raw participant data or native project archives through public links.

For resilience, inspect no-JavaScript content access where applicable, reduced motion, failed/slow images and fallback font wrapping. Measure contrast on actual pairs, including text over imagery and controls in non-default states. Automated checks support, rather than replace, visual and interaction review. Record browser/version, viewport/input mode and tools actually used.

## 4. Classify findings before fixing

Use practical priorities:

- **Blocking:** content cannot be accessed, destinations are broken, confidential material is exposed, public claims are false, or key actions fail.
- **Major:** output contradicts selected direction/content; reading is obstructed; mobile or keyboard use fails; substantial evidence is missing or misleading.
- **Minor:** localized drift, alignment/crop issues, inconsistent states or other bounded polish.
- **Suggestion:** a potential improvement not required by the active specification.

Keep preferences separate from defects. Offer suggestions without using them to justify an unrequested redesign. For each finding name its source requirement, exact route/section/state, evidence and proposed correction. If the source requirement is obsolete, record the owner's decision that superseded it; do not quietly delete the mismatch.

## 5. Correct within scope and retest

Fix clear mismatches and defects using the existing source of truth. Edit content/templates/generators when they own the output; ensure regeneration preserves changes. Establish snapshots, diffs or hashes for genuinely protected regions and inspect rendering when shared styles/scripts can affect them.

Work in bounded passes: shared token/component issues first when they explain multiple failures, then page-specific composition/content, then optional polish. Record intentional deviations and why they are allowed. A new identity direction, unresolved personal fact or material scope change requires an owner decision; ordinary implementation fixes do not.

Retest the exact failure and affected consumers. Do not repeat a full performance run for a caption correction. Conversely, shared header, font, motion or component changes require broader checks. A failed complex effect may become a documented static alternative that preserves content and the selected intent.

If tools block a check, complete independent work and mark the result unverified. Do not generate fake screenshots, infer smoothness from source code, treat device emulation as physical-device testing or report a site-wide accessibility guarantee from a small sample.

## 6. Reconcile what was delivered

Update the active decision log, build/status notes and progress. Keep historical notes recoverable and mark superseded decisions clearly. Documentation may be corrected to reflect an authorized implementation change, but not merely to hide a defect. Preserve unresolved owner decisions until actually answered.

Create `design-notes/site-maintenance.md` as the concise operational record:

- Actual preview/build commands and deployable root, verified from the project.
- Routes, shared components and source-of-truth content/template/data files.
- Where to edit biography, project copy, contact details, covers and body assets.
- How to add a project, refresh evidence/maps and regenerate pages if applicable.
- Active identity references, mobile adaptations and where they are implemented.
- Remaining placeholders, integrations, unsupported environments and launch work.
- Recovery guidance grounded in actual snapshots/version control, when available.

If legacy `06-review.md` or `07-owner-guide.md` exists, read it as prior context, link or reconcile useful content, and label it superseded where appropriate. Do not delete existing project documentation or assume old outstanding questions have been resolved. Local audit completion does not authorize deployment or sending messages.

## Outputs

- `design-notes/06-design-audit.md`: scope, active source documents, findings, fixes, retests, owner decisions and remaining limits.
- `design-notes/06-design-audit-matrix.csv`: requirement-to-output traceability and final status.
- Screenshots or other evidence under `design-notes/audit-evidence/` when tools permit; name page, width and state.
- `design-notes/site-maintenance.md`, updated decisions/progress and affected implementation notes.

Use pass, fail, fixed-and-retested, not-applicable and unverified for actual checks. Explain any not-applicable classification. Include exact evidence locations so another session can reproduce a result.

## Completion criteria

Finish when the documented requirements are mapped to observed output, scoped defects have been corrected and retested, intentional deviations are recorded, remaining issues are actionable and maintenance instructions point to real files. A clean-looking site with unverified requirements is not a fully passed audit. State what matches, what changed and what still needs evidence without requiring an extra handoff ceremony.
