---
name: mobile-responsive-design
description: Build and verify responsive layouts and touch-friendly component alternatives for an existing website while preserving its selected identity, content and desktop behaviour. Run during implementation and before the final design audit.
---

# Mobile Responsive Design

Execute in the current website workspace. Read [METHOD.md](../../METHOD.md) once per workflow. Use available code/browser tools and existing assets; no image generation. This is an implementation and verification skill, not simply a checklist or a narrow-screen screenshot pass.

## Purpose and timing

Run after representative pages/components exist, or alongside their implementation. Complete it across the agreed routes before [Design Audit](../12-design-audit/SKILL.md). Identify where desktop components become difficult on smaller screens or imprecise input, propose purposeful alternatives and implement supported improvements within scope.

Responsiveness is not shrinking the desktop. Preserve each section's purpose, meaningful content and site identity while changing composition, controls or interaction when needed. Width, input precision and hover ability are different conditions. A tablet can have a keyboard/mouse; a wide screen can have touch. Do not identify devices solely by user agent or assume every small viewport lacks a keyboard.

## 1. Read the contract and establish a baseline

Read the selected direction, palette, personality brief/story, site blueprint, per-project case-study plans, existing build notes and any current audit findings. Inspect shared tokens, navigation, page structures, media loading and responsive/motion code. Identify generators/templates and edit the durable source.

List routes in scope, desktop features to preserve, existing mobile provisions, supported environments and actual tool access. Capture a representative wide baseline and narrow states where possible. Protect approved desktop intent without assuming byte-identical shared CSS is required: a shared change may be appropriate but needs regression review.

Identify the content that must remain reachable on mobile: project names/metadata, evidence captions, selected images, biography, navigation, contact actions and scope notes. Do not hide content just because it does not fit, reduce text until it is unreadable or substitute a static image for an accessible interactive interface without considering the lost function.

## 2. Inventory components by task and failure

Create a component matrix before making blanket substitutions:

| Route/component | User task and essential content | Desktop behaviour | Narrow/touch failure | Proposed mobile behaviour | Content/state parity | Trigger | Evidence/status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project index cards | Choose a project | Caption on hover | Touch cannot reveal it reliably | Persistent caption and full card link | All title/metadata retained | No-hover or layout constraint | Actual check |

Inspect navigation, chapter rails, project cards, layered scenes, annotation hotspots, tabs, comparisons, galleries, tables, forms, overlays and sticky elements. Test actual behaviours rather than assume a visual pattern is wrong. A simple desktop component that already works may need spacing changes only.

For significant alternatives, offer a concrete recommendation with a small preview or wireframe, retained function, tradeoff and implementation effort. Do not overwhelm the owner with several replacements per component. Implement clear within-scope usability fixes; ask only if an alternative changes the chosen concept, content, significant navigation or scope. Record such decisions before representing a proposal as approved.

## 3. Select alternatives that fit the task

Use this as a decision library, not a mandatory list of widgets:

| Desktop pattern | Useful mobile/touch alternative | Preserve and check |
| --- | --- | --- |
| Wide header navigation | Wrapping visible links when few; labelled expandable menu when needed | All destinations, current-page state, real controls and predictable focus |
| Long chapter rail | Compact chapter disclosure with native anchor links, or wrapping inline anchors | Current location where useful; anchor target clearance; no essential hover |
| Hover-reveal project cards | Persistent title/metadata with a clear card link | Same project information and destination; no first tap consumed only to simulate hover |
| Dense side tabs | Wrapping tabs when labels fit, native select for simple selection, or inline disclosures for independent content | Correct semantics and state; do not use a select when side-by-side comparison is essential |
| Hover hotspots | Numbered visible callouts with in-flow explanations or accessible tap disclosures | Every explanation linked to its visual location; touch/keyboard operation |
| Pinned scroll sequence/parallax | Ordinary stacked frames with short labels, or a concise controlled stepper when sequencing benefits understanding | All meaningful steps; direct access to text; reduced-motion alternative |
| Swipe/drag-only comparison | Explicit buttons/toggle and labelled views; side-by-side or stacked images when comparison needs both | Both originals/variants, captions and a non-drag way to operate |
| Very wide gallery | Single-column reading sequence or deliberate grid; controlled gallery only when justified | Captions, navigation, position and keyboard/touch access; no auto-advance |
| Data table | Keep an accessible contained horizontal scroll area, or turn suitable independent rows into labelled records | Relationships and comparison; do not lose header associations or silently omit columns |
| Desktop overlay/side panel | In-flow disclosure or carefully implemented dialog when the task requires it | Labels, focus, close/back behaviour and scroll; modal semantics only if modal |
| Tiny icon controls/tool dock | Labelled buttons, simpler action list or fewer primary actions with the rest available | Accessible names, action availability and adequate target separation |
| Layered decorative scene | Reflowed composition or simplified still using existing assets | Readable content, recognizable motif and actual links; decoration may simplify |

Choose based on the section's documented purpose. An accordion is not the automatic answer to everything. Avoid adding app-like bottom navigation, carousels or sheets merely to make the site appear mobile. Prefer existing primitives/native controls when they satisfy the task.

## 4. Recompose layout at content-driven breakpoints

Start from a readable narrow layout, then expand or adapt the existing system. Select breakpoints where content actually fails, not only device labels. Inspect just below/above transitions. Retain fluid widths, natural wrapping and useful maximum reading widths. Let the content determine section height; avoid fixed viewport heights that clip text or force empty space.

Check long titles, long URLs, unbroken content, fallback fonts, grid/flex minimum sizing, nested scroll areas and positioned decoration. Fix the source of horizontal overflow rather than hide it globally. Stacking should follow a meaningful DOM order, not a desktop visual trick that becomes confusing for keyboard or screen-reader users.

Images need intentional aspect ratio, crop and source size. Do not shrink a detailed drawing or UI screenshot until labels become meaningless; provide an uncropped enlargement or focused steps plus a text explanation. Keep the surrounding page readable while a genuinely two-dimensional diagram or table has its own inspection treatment.

The reflow check should include the equivalent of 320 CSS pixels for vertically scrolling content, preserving information/function except genuinely two-dimensional content. See [W3C Reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html). Treat this as an accessibility check, not a requirement to make every image fit as readable text at that size.

Check browser chrome, portrait/landscape, short-height viewports and virtual-keyboard clearance where tools permit. Use appropriate dynamic/small viewport units and safe-area padding if needed rather than blindly applying 100vh or fixed bottom offsets. Keep pinch zoom available.

## 5. Design for touch and mixed input

Essential content/actions must work without hover. Optional hover effects may remain for precise pointers. Use width conditions for composition and hover/pointer capability queries for interaction enhancements as appropriate; do not treat pointer precision as a complete device detector. See [MDN pointer media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/pointer).

Make frequent actions comfortable to tap. An approximately 44 CSS pixel target is a practical design aim for important standalone controls, not a blanket AA minimum. Verify the actual hit area and separation. WCAG 2.2 AA target-size minimum is 24 × 24 CSS pixels with specified exceptions/spacing alternatives; record the actual condition rather than claim all small inline links fail. See [W3C target-size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

Do not require a precision drag, rapid gesture or hover to reach an action. Provide direct controls for any useful swipe/drag interaction. Preserve native page scrolling and avoid nested gesture traps. Use appropriate link/button elements, accessible names and visible focus; larger hit areas must not overlap adjacent targets or create nested interactive controls.

For menus/disclosures, expose expanded state and make content discoverable. For modal dialogs, manage entry/return focus, close behaviour and background interaction correctly; do not apply modal roles to ordinary inline expansion. Test keyboard operation even in a touch-oriented layout.

Forms need visible labels, suitable input types/autocomplete where appropriate, clear errors and controls reachable above the virtual keyboard. Do not claim submission works without verifying its actual integration. Static contact links may be sufficient for this site.

## 6. Keep one coherent implementation

Prefer a shared semantic content source with responsive presentation. Avoid duplicate desktop/mobile copies unless needed; if separate presentations exist, coordinate state, remove hidden interactive content from focus and prevent duplicate IDs or divergent text. Keep meaningful URLs/anchors stable across layouts when possible.

Handle transitions while a menu, tab or dialog is open. Resizing/rotation should not leave the page locked, focus lost, stale state visible or pinned spacer remnants. Clean up breakpoint-dependent event listeners/animations. Reduced motion and JavaScript failure must leave usable reading/navigation paths.

Use responsive media, explicit image dimensions and deferred offscreen loading where appropriate. Do not initialize desktop pinned sequences or load/decode every hidden high-resolution frame on a constrained view without a reason. Avoid content shifts from unloaded imagery or layout measurements. Record large-media exceptions and measure performance only with available tools.

Maintain the approved type, colour, image treatment and personal motifs. Change their arrangement or intensity where readability demands it; explain significant departures in the adaptation plan. Mobile is a designed form of the same site, not an unrelated theme.

## 7. Exercise tasks, not just screenshots

Build a verification matrix with actual environment, viewport, input, state, action, result and evidence. Useful coverage includes:

- Narrow reflow at 320 CSS pixels, common phone widths such as 360/390, tablet/intermediate layout and wide desktop regression. Adjust the range to real requirements.
- Portrait and landscape/short-height cases; just below/above layout transitions.
- No-hover/coarse-pointer and keyboard interactions where the browser supports simulation; physical-device checks when actually available.
- Reduced motion, no-JavaScript fallback where applicable, image loading failure and long/fallback-font content.
- Browse projects, open a detail page, navigate chapters, inspect a drawing/image, operate replacement controls, reach About/contact and use back navigation.
- Open/close menus or dialogs, rotate/resize while open, scroll to the footer and confirm fixed elements do not cover content, focus or anchor targets.
- Text enlargement/zoom without forced scale restrictions; keyboard/form behaviour and safe-area checks when testable.

Screenshots demonstrate appearance for captured states. DOM overflow checks can support them but do not prove touch usability, screen-reader access, real-device performance or smooth animation. Label device emulation, actual hardware testing and static-only review distinctly. If browser access is missing, implement justified source-level improvements and supply exact pending manual tasks; do not mark visual/mobile checks passed.

## Outputs and audit handoff

Write:

- `design-notes/11-mobile-plan.md`: route/component inventory, failures, proposed alternatives, selected decisions, triggers, retained content/function and desktop protections.
- `design-notes/11-component-adaptations.csv`: component, source requirement, desktop pattern, mobile replacement, trigger, implementation path, status and verification reference.
- `design-notes/11-mobile-review.md`: actual test matrix, issues/fixes/retests, environments and limitations.
- Supporting previews/screenshots under `design-notes/mobile-evidence/` when available.

Update the blueprint, affected build notes, decision log and progress with authorized adaptations. Mark changes as proposed, implemented or verified accurately. Hand the design audit the mobile results and unresolved findings. Do not rerun unrelated discovery stages or publish the site.

## Completion criteria

The agreed mobile scope retains essential information/actions, selected component replacements are implemented and exercised, the site identity is coherent, desktop regressions have been checked appropriately and known limits have concrete next steps. A narrow screenshot with no overflow is insufficient evidence of completion. If some checks are unavailable, report the implementation state and unverified tasks explicitly.
