# Prompts and feedback

Guide 4 of 5. Use alongside [03 — Start here](03-START-HERE.md). The stage-launch prompts live there; this guide helps you describe a task, react to a preview and continue work without losing decisions. The assistant's shared execution rules are in [05 — Working method](05-WORKING-METHOD.md).

You do not need elaborate prompts or design terminology. Give the assistant the material it needs, a concrete outcome and any boundaries that matter. It should inspect the workspace and use the relevant skill rather than ask you to repeat everything already documented.

## A useful brief has five parts

| Part | What to say |
| --- | --- |
| Context | The website workspace, current stage and relevant notes. |
| Material | Exact folders/files/links it should inspect and what they are for. |
| Outcome | What should exist or work when this task is complete. |
| Boundaries | Approved areas to preserve, public/private limits and scope. |
| Evidence | What to show or check so you can assess the result. |

Use only the parts relevant to the task. Replace `[bracketed placeholders]` in the examples with your information. Prompts are task instructions, not commands to bypass tool restrictions. A file path alone does not give the assistant access: supply the workspace or uploads/connection first.

## Start the workflow

> Work in `[website workspace]`. Read `design-sesh-portfolio-builder/01-WELCOME.md` and `design-sesh-portfolio-builder/03-START-HERE.md`. My reference images are in `[reference folder]`, my personal notes are in `[personal-content folder]`, and my project sources are in `[project-sources folder]`. Start with Skill 01 only. Inspect the images you can access, report coverage and write the reference audit. Ask only for missing information that changes the result. Do not generate images or begin building the site yet.

If the assistant is chat-only, attach the active skill and relevant images/notes, and request a planning deliverable it can actually produce. File organization, Python maps and implementation need an execution-capable workspace.

## Continue to the next stage

> Use Skill `[number and name]` from the current kit. Read the existing outputs it depends on before asking me questions. Reuse selected decisions and completed work. Produce the skill's documented outputs, record important new decisions and tell me what remains unresolved. Do not rerun completed discovery just because this is a new chat.

Follow **01 → 02 → 03 → 04 → 05 (each project) → 06 → 07 → 08 → 09 → 10 → 11 → 12**. Some stages need your answers or selection; this prompt does not authorize the assistant to guess them.

## Explain what you like in a reference

> In `[image or website]`, I like `[specific visible quality]`. I do not want `[other quality]`. Compare it with `[another reference]` and explain which layout or colour principles could transfer to my site. Keep the selected identity and use my own assets and wording. Inspect the reference before describing it; tell me if you cannot access it.

Useful observations include “the image is much larger than the headline,” “the captions are quiet,” “the colour appears only in a few places,” or “the sections feel too repetitive.” You do not need to identify a font or name an aesthetic.

## Choose colours without restarting the whole design

> Use Skill 03, Choose Your Colours. Consider `[images]`, `[favourite site links]` and `[brands]`. I like them because `[what appeals to you]`; my dislikes are `[dislikes]`. Reuse my personality brief and ask only the missing preference questions. Show two or three palettes on the same heading, text, link, button and project image. Recommend one, explain its tradeoff and check the intended colour pairings. Wait for my palette choice before calling it selected.

A favourite brand is context, not an instruction to copy its identity. If you like its photographs rather than its interface colours, say so.

## Compare design options fairly

> Use the same content and project image to show `[two options or one controlled change]`. Keep `[palette/type/content choices]` fixed so I can judge `[composition/density/image scale/etc.]`. Explain what changed and why. Keep both as local experiments until I select the active version.

Avoid asking for many complete styles at once. A small comparison often answers a specific question faster. “I like this option's opening and that option's captions” is useful; the assistant should propose a coherent combination rather than combine every feature.

## Organize one project and make its sources findable

> Use Skill 05 on `[one complete project folder]`. Inventory the files before selecting them, review the documents and visuals, preserve originals/dependencies and account for unreviewed material. Prepare the evidence ledger, curated selection, project-card copy, case-study plan and asset manifest. Build the Python JSON map if available and add descriptions/tags only after reviewing sources. Work on this project only. Report counts, uncertain claims and publication limits.

Add what you know about your role, team, context and completion status. Unknowns can stay unknown. Do not tidy the source folder by deleting files before the inventory.

## Ask the assistant to use the map while designing

> Read `[project audit]`, `[case-study plan]` and `[project-map.json]`. Find candidate assets for `[specific section or point]` using the reviewed tags/summaries. Open the actual sources, check what they prove and whether the selected exports can be public. Explain the chosen asset and crop, then update its manifest. A map entry alone is not proof of review or permission.

A specific question such as “show the circulation decision” is better than “find a nice image.” It gives the asset a purpose in the story.

## Give feedback when a preview feels wrong

> On `[page/section]` at `[viewport or device]`, `[what feels wrong or what happened]`. I want the section to `[communication goal]`. Keep `[specific things that work]`. Suggest the likely cause, make one focused revision and show the same state again. Record the active choice and retain the previous version only if useful.

Examples of concrete feedback:

- “The opening feels too formal. Keep the layout, but use shorter wording closer to my writing sample.”
- “There is too much empty space between the drawing and explanation. Bring them together without making the text tiny.”
- “Every chapter looks equally important. Give the main design decision more emphasis and make the supporting process quieter.”
- “The project image looks cropped accidentally. Keep the title and card dimensions; try a crop that preserves the full subject.”

You can also say you do not know the cause. Ask for a limited comparison of likely explanations instead of demanding a complete redesign.

## Make a revision with clear boundaries

> Change `[specific area]` to achieve `[outcome]`. Preserve `[approved pages/components/assets]`. Use the selected direction and existing source-of-truth templates/data. Check affected shared components after the edit. Record the changes and actual verification. If the change needs a different identity decision or removes meaningful content, explain that before treating it as approved.

Do not use “nothing else should ever change” when shared styles genuinely need adjustment. State what is approved and why; the assistant can verify the relevant boundary with diffs, snapshots and rendered checks.

## Correct a fact or remove a personal detail

> Correct `[claim/detail]` to `[supported wording]` using `[source or my clarification]`. Update the active notes and affected copy, not just one visible occurrence. Mark the earlier decision superseded. `[Private detail]` should not appear in public assets or pages. Check the actual exports and links that might contain it and report the scope reviewed.

A factual correction does not require reinventing the visual direction. For sensitive material, distinguish raw private sources from the sanitized public derivative.

## Design a better mobile component

> Use Skill 11 on `[routes/components]`. At `[viewport/input/device]`, the current `[component]` makes `[task]` difficult because `[observed problem]`. Propose a touch-friendly alternative preserving the same information, task and selected identity. Show its reading order and control states, implement the in-scope fix and check keyboard/touch behaviour and affected desktop layouts. Record emulated versus real-device checks accurately.

For example: “The project descriptions appear only on hover. Make them visible and easy to open on touch without changing the desktop card composition unnecessarily.” Do not ask simply to shrink the entire desktop or replace every section with an accordion.

## Audit against the earlier documentation

> Use Skill 12, Design Audit. Compare the actual site with the active personality brief, palette, direction, story, site/project blueprints and mobile decisions. Map each requirement to a page/component/state and evidence. Fix supported mismatches within scope, retest affected routes and record intentional deviations. Do not rewrite the specification merely to make the current output pass. Reconcile the actual editing/maintenance notes and list unverified checks separately.

For a focused pass, name the changed pages and shared components. For the whole site, specify the routes and intended audience. Neither a polished screenshot nor an automated checker alone establishes that every requirement is met.

## Resume in a new chat

> Continue this existing portfolio workspace. Read `design-notes/progress.md`, `design-notes/decision-log.md`, the selected palette/direction and current blueprint, then the notes for `[relevant project/page]`. Inspect the implementation before editing. Summarize the active choices and next incomplete action briefly, then continue `[specific task]`. Preserve finished work and ask only for missing information that is necessary.

Keep the actual files accessible. A summary of decisions cannot replace missing source assets or a project evidence ledger when making public claims.

## When a tool or check is unavailable

> Complete the work that does not depend on `[blocked tool/input]`. Explain the specific limitation and preserve the current implementation. Label the affected check unverified, give a concrete remaining check and continue independent tasks. Do not invent screenshots, claim a pass from static inspection or switch to a method that bypasses the restriction.

A blocked browser can still allow source-level work, but it does not establish the rendered result. If the missing item is an essential personal choice, supply your answer before the assistant performs dependent work.

## Add another project later

> Keep the current website identity. Run Skill 05 on `[new project folder]`, then Skill 09 to add its collection entry and the detail page included in scope. Run Skill 11 on affected mobile components, then Skill 12 to audit the integration and update maintenance notes. Preserve the existing project order and approved pages unless I specify a change. Do not reopen the colour or personal-story process without a concrete reason.

## End a work session with useful continuity

> Update the relevant build/status notes, active decisions and progress file. Tell me what exists now, what was actually checked, what remains unresolved and the next useful action. Link the important local artifacts. Keep the summary concise and distinguish local completion from publication.

Use these patterns when helpful, not as an extra ceremony for every edit. The most effective request is usually a clear task, real evidence and a small number of meaningful constraints.
