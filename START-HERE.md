# A website that feels like you — Claude skill sequence

This pack takes a reference-image folder and your personal input through to a working site. It does not need image generation. Use an environment that can read the reference images and edit site files; browser preview improves verification. In a chat-only environment the early planning stages work, but implementation needs a coding workspace.

## How to run

Put this extracted kit in your own website project alongside your reference folder. Each numbered folder contains a standalone SKILL.md with a name and description. If your Claude setup supports loading skills, load the folders using its supported mechanism. Otherwise ask Claude to read the relevant SKILL.md directly: the instructions also work as sequential prompts. No specific installation path or subscription is assumed.

Start with this message, replacing the example paths:

> Help me build a website that feels like me. My reference images are in `references/` and my website project is this folder. Read `personality-site-kit/skills/01-reference-folder-audit/SKILL.md` and carry out that stage. Do not generate images. Save outputs to `design-notes/`. Tell me what you actually inspected and what you need from me next.

For a general personal site, run stages 1–7 in order by asking Claude to read each SKILL.md. For a portfolio, use the expanded sequence below. It should reuse the previous stage's outputs, not restart the project.

| Stage | Skill folder | What you get / what you provide |
| --- | --- | --- |
| 1 | 01-reference-folder-audit | Traceable visual analysis of your actual images |
| 2 | 02-personality-interview | A short conversation about you, your voice, audience and boundaries; answer before proceeding |
| 3 | 03-personal-design-directions | A few distinct directions; choose one before proceeding |
| 4 | 04-site-story-and-personal-touches | A page plan and specific personal details mapped to useful website elements |
| 5 | 05-build-personal-site | A complete local site using existing imagery, HTML/CSS, simple SVG and appropriate interactions |
| 6 | 06-personality-and-usability-review | Fixes and an honest test report; give feedback on what feels like you |
| 7 | 07-personal-site-handoff | Editing instructions, identity notes and remaining launch work |

For subsequent stages:

> Read `personality-site-kit/skills/02-personality-interview/SKILL.md` and run it using the existing `design-notes/` outputs.

Change the folder name for each next stage. If starting a new chat, supply the project and design-notes folder again. If a decision changes, update its notes and revisit dependent stages. Do not treat previously rejected ideas as current direction.

## Bring these if you have them

Reference images; a little about yourself; what the site is for; real writing/work/photos you'd like to show; things you dislike; and anything that must remain private. It is fine not to know your aesthetic yet. References guide the conversation; they do not define your personality.

## What makes this personal

The process connects a confirmed detail about you to a specific expression on the site. For example, a collection might inform a browsing pattern, your handwriting might become a small approved accent, or your own sign-off might belong in the footer. None of these are defaults. Claude must learn which details are yours and whether you want them public.

Original reference images stay intact. Publication is separate from building locally. These skills contain no requirement for image APIs, paid fonts, a particular framework or a particular hosting service.


## Expanded portfolio sequence

The new folder numbers identify additional skills; they do not mean these should run after handoff. Use this order for a portfolio:

**01 Reference audit → 02 Personality interview → 03 Choose direction → 08 Project folder preparation (repeat for each project) → 04 Site blueprint → 05 Build site foundation → 09 Build Projects → 10 Build About → 06 Review whole site → 07 Handoff.**

| Additional skill | Input | Output |
| --- | --- | --- |
| 08-project-folder-to-portfolio | One project's documents, images, editable files and other sources | Organized curated selection, complete file index, evidence ledger, case-study plan, card copy and asset manifest |
| 09-build-projects-page | Prepared projects, her personality brief, chosen direction and existing site | Projects collection/index; linked case studies when explicitly included in the blueprint or request |
| 10-build-about-page | Her own words, confirmed background, approved personal details and existing site | About page with individual voice and purposeful personal touches |

Stage 08 leaves originals intact by default, preparing a separate curated folder or a manifest of source references. It does not delete files or assume a file called FINAL is the right version. Missing or private material is tracked rather than turned into invented project evidence.

Use these prompts, adjusting paths and project names:

> Read `personality-site-kit/skills/08-project-folder-to-portfolio/SKILL.md`. Analyze and organize the project in `project-sources/project-name/` for my portfolio. Use my existing personality and design notes. Leave originals intact and prepare the evidence, assets and story for the site. Do this project only.

> Read `personality-site-kit/skills/09-build-projects-page/SKILL.md`. Build my Projects index using the prepared projects and my selected website direction. Follow the blueprint for whether individual case-study pages are included. Keep the existing site identity and use only verified project content.

> Read `personality-site-kit/skills/10-build-about-page/SKILL.md`. Build my About page from my personality brief and existing content. Ask only for important missing facts, keep it in my voice, and make its personal touches belong with my Projects page and the rest of the site.

If the site is already built, run 08 → 09 → 10 → 06 → 07 as needed. Read the existing identity notes first; don't redesign the whole site merely to add these pages. If processing several projects, repeat stage 08 and retain a separate notes folder for each project.
