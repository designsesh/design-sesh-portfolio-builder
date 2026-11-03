# Design Sesh Portfolio Builder

A set of **12 Claude-compatible skills** for turning visual references, your personality and your project files into a portfolio that feels like you. Uses existing images, live text, HTML/CSS, simple SVG and appropriate interactions. **No image generation required.**

## Read the guides in this order

| Guide | Purpose |
| --- | --- |
| [01 — Welcome](01-WELCOME.md) | Understand the full workflow and arrange references, personal content and project folders. |
| [02 — Set up Claude or GPT](02-SETUP-CLAUDE-AND-GPT.md) | Use the kit with Claude, ChatGPT Projects or Codex; choose direct-file use or skill installation. |
| [03 — Start here](03-START-HERE.md) | Run skills 01–12 with their inputs, outputs and a prompt for each stage. |
| [04 — Prompts and feedback](04-PROMPTS-AND-FEEDBACK.md) | Give clear briefs, useful visual feedback, bounded revision requests and continuation prompts. |
| [05 — Working method](05-WORKING-METHOD.md) | The shared rules the assistant follows for evidence, design decisions, iteration and verification. |

Guide numbers indicate reading order. The separate `skills/01-…` to `skills/12-…` folders indicate execution order. Keep `SKILL.md` filenames unchanged so skill loaders can discover them.

## Recommended portfolio workflow

**01 → 02 → 03 → 04 → 05 (repeat for each project) → 06 → 07 → 08 → 09 → 10 → 11 → 12**

Folder numbers match execution order: run 01 through 12, repeating 05 for each project. Project preparation happens before site planning. Projects and About are followed by mobile/touch adaptation, then a design audit against the earlier documentation.

## All 12 skills

| Run order | Skill | What it does | What you get |
| --- | --- | --- | --- |
| 1 | [Skill 01](skills/01-reference-folder-audit/SKILL.md) — Analyze reference images | Uses reference images and screenshots | A visual inventory, recurring patterns, contrasts and buildable ideas |
| 2 | [Skill 02](skills/02-personality-interview/SKILL.md) — Discover personality and voice | Uses your answers, writing samples and existing personal notes | A brief covering audience, goals, voice, interests and public/private boundaries |
| 3 | [Skill 03](skills/03-choose-your-colours/SKILL.md) — Choose website colours | Uses uploaded images, favourite sites/brands and brief preference answers | Two or three practical palettes and an owner-selected colour system |
| 4 | [Skill 04](skills/04-personal-design-directions/SKILL.md) — Choose a design direction | Uses reference audit and personality brief | Distinct visual directions and a recorded choice |
| 5 | [Skill 05](skills/05-project-folder-to-portfolio/SKILL.md) — Prepare each portfolio project | Uses one project folder with documents, images, prototypes and source files | File index, evidence ledger, curated assets, case-study plan and project-card copy |
| 6 | [Skill 06](skills/06-find-your-story/SKILL.md) — Find your story | Uses personality notes, real experiences and prepared project evidence | A factual personal story, introduction and About copy in your voice |
| 7 | [Skill 07](skills/07-site-story-and-personal-touches/SKILL.md) — Plan the site and personal details | Uses chosen direction, personality brief and prepared project stories | Routes, section layouts, copy, asset mapping and purposeful personal touches |
| 8 | [Skill 08](skills/08-build-personal-site/SKILL.md) — Build the site foundation | Uses site blueprint, chosen direction and approved assets | A working local site, shared design system and page foundations |
| 9 | [Skill 09](skills/09-build-projects-page/SKILL.md) — Build Projects and agreed case studies | Uses prepared projects, blueprint and existing site | A Projects collection with real destinations and any agreed detail pages |
| 10 | [Skill 10](skills/10-build-about-page/SKILL.md) — Build About in your voice | Uses confirmed biography, personality brief and approved personal assets | An About page that matches you and the rest of the site |
| 11 | [Skill 11](skills/11-mobile-responsive-design/SKILL.md) — Mobile Responsive Design | Uses the built site, blueprint and existing components | Responsive implementation, touch-friendly alternatives and mobile verification |
| 12 | [Skill 12](skills/12-design-audit/SKILL.md) — Design Audit | Uses the rendered site and active documentation from earlier skills | Requirement-to-output audit, scoped fixes, retests and current maintenance notes |

## How to use

1. Download or clone this repository into your website workspace.
2. Give Claude access to your reference images, project folders and the skill files. Implementation needs a file-editing coding environment; visual analysis needs image access, and browser preview improves verification.
3. Ask Claude to read the relevant `SKILL.md` and execute it. If your environment supports loading skills, its supported loader is another option.
4. Keep the generated `design-notes/` outputs so later skills and new chats can reuse your decisions.

You provide answers during Skill 02, choose colours with Skill 03, select a direction with Skill 04 and shape your story with Skill 06. Claude should not guess your personality from a mood board. Later, tell it which copy and details feel natural or forced.

For a general personal site without a project collection, use **01 → 02 → 03 → 04 → 06 → 07 → 08 → 11 → 12**. For an existing portfolio, run only the needed preparation/page skills, followed by **11 (mobile adaptation) → 12 (design audit)**.

## What makes this personal

Confirmed details about you inform specific design choices: your voice, a meaningful object, a small annotation, a useful interaction or your own sign-off. The skills do not prescribe a scrapbook, museum, desk scene or someone else's interests. A quiet site can be personal too.

## Files and boundaries

- [`skills/`](skills/) contains the 12 detailed skill definitions, numbered in execution order.
- [`tools/project_map.py`](tools/project_map.py) builds/searches local file catalogs; the welcome guide explains the process.
- `design-notes/` belongs in your website workspace and records decisions, source evidence and stage outputs.
- Originals remain intact by default. Unknown facts stay unknown; project claims require evidence.
- The Projects skill builds the collection and detail pages included in the agreed scope.
- Mobile Responsive Design (11) adapts components for touch and constrained layouts; Design Audit (12) checks the result against the active documentation.
- Local implementation does not authorize publication. No image generation or particular hosting/framework is required.

The skill files and guide links have structural checks. Product setup and agent behaviour have not been tested across every Claude/ChatGPT/Codex environment.
