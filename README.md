# Design Sesh Portfolio Builder

A set of **12 Claude-compatible skills** for turning visual references, your personality and your project files into a portfolio that feels like you. Uses existing images, live text, HTML/CSS, simple SVG and appropriate interactions. **No image generation required.**

Read [WELCOME.md](WELCOME.md) for the complete workflow, folder setup and searchable Python project maps. Then use [START-HERE.md](START-HERE.md) for workspace setup, a prompt for every skill and instructions for continuing across chats.

## Recommended portfolio workflow

**01 → 02 → 11 → 03 → 08 (repeat for each project) → 12 → 04 → 05 → 09 → 10 → 06 → 07**

Folder numbers are stable skill IDs, not the execution order. Project preparation happens before site planning; Projects and About are built before the final review and handoff.

## All 12 skills

| Run order | Skill | What it does | What you get |
| --- | --- | --- | --- |
| 1 | [Skill 01](skills/01-reference-folder-audit/SKILL.md) — Analyze reference images | Uses reference images and screenshots | A visual inventory, recurring patterns, contrasts and buildable ideas |
| 2 | [Skill 02](skills/02-personality-interview/SKILL.md) — Discover personality and voice | Uses your answers, writing samples and existing personal notes | A brief covering audience, goals, voice, interests and public/private boundaries |
| 3 | [Skill 11](skills/11-choose-your-colours/SKILL.md) — Choose website colours | Uses uploaded images, favourite sites/brands and brief preference answers | Two or three practical palettes and an owner-selected colour system |
| 4 | [Skill 03](skills/03-personal-design-directions/SKILL.md) — Choose a design direction | Uses reference audit and personality brief | Distinct visual directions and a recorded choice |
| 5 | [Skill 08](skills/08-project-folder-to-portfolio/SKILL.md) — Prepare each portfolio project | Uses one project folder with documents, images, prototypes and source files | File index, evidence ledger, curated assets, case-study plan and project-card copy |
| 6 | [Skill 12](skills/12-find-your-story/SKILL.md) — Find your story | Uses personality notes, real experiences and prepared project evidence | A factual personal story, introduction and About copy in your voice |
| 7 | [Skill 04](skills/04-site-story-and-personal-touches/SKILL.md) — Plan the site and personal details | Uses chosen direction, personality brief and prepared project stories | Routes, section layouts, copy, asset mapping and purposeful personal touches |
| 8 | [Skill 05](skills/05-build-personal-site/SKILL.md) — Build the site foundation | Uses site blueprint, chosen direction and approved assets | A working local site, shared design system and page foundations |
| 9 | [Skill 09](skills/09-build-projects-page/SKILL.md) — Build Projects and agreed case studies | Uses prepared projects, blueprint and existing site | A Projects collection with real destinations and any agreed detail pages |
| 10 | [Skill 10](skills/10-build-about-page/SKILL.md) — Build About in your voice | Uses confirmed biography, personality brief and approved personal assets | An About page that matches you and the rest of the site |
| 11 | [Skill 06](skills/06-personality-and-usability-review/SKILL.md) — Review and refine the whole site | Uses working site, identity notes and your feedback | Supported fixes and a report of actual checks and remaining limits |
| 12 | [Skill 07](skills/07-personal-site-handoff/SKILL.md) — Make the site easy to maintain | Uses finished implementation, review and active design choices | Editing instructions, identity notes and remaining launch work |

## How to use

1. Download or clone this repository into your website workspace.
2. Give Claude access to your reference images, project folders and the skill files. Implementation needs a file-editing coding environment; visual analysis needs image access, and browser preview improves verification.
3. Ask Claude to read the relevant `SKILL.md` and execute it. If your environment supports loading skills, its supported loader is another option.
4. Keep the generated `design-notes/` outputs so later skills and new chats can reuse your decisions.

You provide answers during Skill 02, choose colours with Skill 11, select a direction with Skill 03 and shape your story with Skill 12. Claude should not guess your personality from a mood board. Later, tell it which copy and details feel natural or forced.

For a general personal site without a project collection, use **01 → 02 → 11 → 03 → 12 → 04 → 05 → 06 → 07**. For an existing portfolio, run only the needed preparation/page skills, followed by **06 → 07**.

## What makes this personal

Confirmed details about you inform specific design choices: your voice, a meaningful object, a small annotation, a useful interaction or your own sign-off. The skills do not prescribe a scrapbook, museum, desk scene or someone else's interests. A quiet site can be personal too.

## Files and boundaries

- [`WELCOME.md`](WELCOME.md) explains the process from source folders to a reviewed site.
- [`tools/project_map.py`](tools/project_map.py) builds and searches local JSON catalogs using Python 3, without extra packages.
- [`skills/`](skills/) contains all 12 standalone skill folders.
- [`START-HERE.md`](START-HERE.md) explains inputs, outputs, run order and copy-and-paste prompts.
- Your own working notes are written to `design-notes/` in your website project.
- Project originals remain intact by default. Project claims must have evidence; unknown facts stay unknown.
- Projects means the collection/index by default. Individual case studies are built when included in your request or agreed blueprint.
- Building locally and publishing are separate actions. No particular image API, paid font, framework or hosting provider is required.

The skill files have basic structural checks; they have not been behavior-tested inside Claude.
