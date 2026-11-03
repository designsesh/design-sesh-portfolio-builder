# Start here: build a portfolio that feels like you

This kit contains **10 skills** for analyzing your references, learning what makes you you, preparing your real project material and building a consistent portfolio. No image generation is needed.

## 1. Set up your workspace

Download or clone this repository. The examples below assume you keep it in a folder named `design-sesh-portfolio-builder/` inside your website project:

```text
my-portfolio/
  design-sesh-portfolio-builder/
    README.md
    START-HERE.md
    skills/
  references/
  project-sources/
    project-one/
    project-two/
  personal-content/
  design-notes/                 # Created as you run the skills
  ...your website files...
```

Adjust paths if your folder layout differs. Keep originals in `project-sources/`; Skill 08 prepares a separate curated selection or a source manifest. `personal-content/` is optional: use it for writing, biography, a CV or photos you actually want Claude to consider. Supply public/private boundaries rather than opening unrelated personal folders.

Use Claude in an environment that can inspect images and read/edit project files. A chat-only environment can help with planning if the relevant materials are supplied, but the build needs a coding workspace. Browser access improves visual checks. The skills do not depend on a specific installation path, subscription or skill loader: ask Claude to read the files directly, or use a loader supported by your environment.

## 2. Follow this portfolio sequence

**01 → 02 → 03 → 08 (repeat for each project) → 04 → 05 → 09 → 10 → 06 → 07**

The numbers name the skill folders; they are not a straight numerical checklist. In particular, prepare project evidence with 08 before planning the whole site, and build Projects/About before 06 and 07.

## 3. Know what each skill needs and produces

All note paths below are relative to `design-notes/` in your website workspace.

| Order | Skill | Give Claude | Main result | Saved notes |
| --- | --- | --- | --- | --- |
| 1 | [Skill 01](skills/01-reference-folder-audit/SKILL.md) — Analyze reference images | Reference images and screenshots | A visual inventory, recurring patterns, contrasts and buildable ideas | `01-reference-audit.md` |
| 2 | [Skill 02](skills/02-personality-interview/SKILL.md) — Discover personality and voice | Your answers, writing samples and existing personal notes | A brief covering audience, goals, voice, interests and public/private boundaries | `02-personality-brief.md` |
| 3 | [Skill 03](skills/03-personal-design-directions/SKILL.md) — Choose a design direction | Reference audit and personality brief | Distinct visual directions and a recorded choice | `03-design-directions.md; 03-selected-direction.md` |
| 4 | [Skill 08](skills/08-project-folder-to-portfolio/SKILL.md) — Prepare each portfolio project | One project folder with documents, images, prototypes and source files | File index, evidence ledger, curated assets, case-study plan and project-card copy | `projects/<project-slug>/` |
| 5 | [Skill 04](skills/04-site-story-and-personal-touches/SKILL.md) — Plan the site and personal details | Chosen direction, personality brief and prepared project stories | Routes, section layouts, copy, asset mapping and purposeful personal touches | `04-site-blueprint.md` |
| 6 | [Skill 05](skills/05-build-personal-site/SKILL.md) — Build the site foundation | Site blueprint, chosen direction and approved assets | A working local site, shared design system and page foundations | `05-build-notes.md; 05-asset-manifest.csv` |
| 7 | [Skill 09](skills/09-build-projects-page/SKILL.md) — Build Projects and agreed case studies | Prepared projects, blueprint and existing site | A Projects collection with real destinations and any agreed detail pages | `projects-page-build.md` |
| 8 | [Skill 10](skills/10-build-about-page/SKILL.md) — Build About in your voice | Confirmed biography, personality brief and approved personal assets | An About page that matches you and the rest of the site | `about-content.md; about-page-build.md` |
| 9 | [Skill 06](skills/06-personality-and-usability-review/SKILL.md) — Review and refine the whole site | Working site, identity notes and your feedback | Supported fixes and a report of actual checks and remaining limits | `06-review.md` |
| 10 | [Skill 07](skills/07-personal-site-handoff/SKILL.md) — Make the site easy to maintain | Finished implementation, review and active design choices | Editing instructions, identity notes and remaining launch work | `07-owner-guide.md` |

Skill 08 runs once per project and stores separate notes for each. It records actual review coverage, duplicates, evidence, privacy issues and missing material. A file named FINAL is not automatically treated as authoritative.

Skill 05 builds the shared site and reuses the dedicated page skills where appropriate. Skills 09 and 10 extend that same implementation; if a page is already complete, inspect and improve it instead of building it twice.

## 4. Copy-and-paste prompts for all 10 skills

Run these in the order shown. Replace example folder paths and project names with your own. Keep the same website workspace throughout.

### Step 1: Analyze reference images — Skill 01

> Help me build a portfolio that feels like me. My reference images are in `references/`. Read `design-sesh-portfolio-builder/skills/01-reference-folder-audit/SKILL.md` and carry out the reference audit. Do not generate images. Save outputs to `design-notes/` and tell me what you actually inspected.

### Step 2: Discover personality and voice — Skill 02

> Read `design-sesh-portfolio-builder/skills/02-personality-interview/SKILL.md` and run the personality interview using the reference audit and any notes in `personal-content/`. Reuse what I have already told you. Ask about my voice, goals and meaningful personal details, and wait for my answers before treating them as confirmed.

Answer the interview before moving to design directions. It is fine to say you do not know or do not want to share something.

### Step 3: Choose a design direction — Skill 03

> Read `design-sesh-portfolio-builder/skills/03-personal-design-directions/SKILL.md`. Use my reference audit and personality brief to propose distinct, buildable directions. Help me choose one, then record the selected direction. Do not generate images.

Choose a direction before the site blueprint and build. Project file inventory can proceed independently if you need more time to choose.

### Step 4: Prepare each portfolio project — Skill 08

> Read `design-sesh-portfolio-builder/skills/08-project-folder-to-portfolio/SKILL.md`. Analyze and organize the project in `project-sources/project-one/` for my portfolio. Leave originals intact. Prepare its verified story, curated assets, card copy and case-study plan. Work on this project only and report anything you could not review.

Repeat this step for each project, changing the source path. Keep a separate project slug and notes folder each time.

### Step 5: Plan the site and personal details — Skill 04

> Read `design-sesh-portfolio-builder/skills/04-site-story-and-personal-touches/SKILL.md`. Plan the portfolio around my selected direction, personality brief and prepared project notes. Include my Projects and About pages, decide what each section is for, and map a few meaningful personal touches. Identify whether individual case-study pages belong in the scope.

### Step 6: Build the site foundation — Skill 05

> Read `design-sesh-portfolio-builder/skills/05-build-personal-site/SKILL.md` and implement the agreed site blueprint in this workspace. Reuse an existing working stack where present. Build the shared design foundation, navigation and local site; use the dedicated Projects and About skills for those pages. Reuse existing assets and code without image generation.

### Step 7: Build Projects and agreed case studies — Skill 09

> Read `design-sesh-portfolio-builder/skills/09-build-projects-page/SKILL.md`. Build or complete my Projects page using the prepared project notes and selected direction. Include individual case-study pages only where the blueprint or my request calls for them. Use real destinations, verified claims and personal details that fit the rest of my site.

### Step 8: Build About in your voice — Skill 10

> Read `design-sesh-portfolio-builder/skills/10-build-about-page/SKILL.md`. Build or complete my About page using my own voice, confirmed background and approved personal content. Ask only for important missing facts. Make its personal touches feel natural and consistent with my Projects page and the rest of the site.

### Step 9: Review and refine the whole site — Skill 06

> Read `design-sesh-portfolio-builder/skills/06-personality-and-usability-review/SKILL.md`. Review the whole built site against my personality brief, selected direction and blueprint. Fix clear defects and mismatches, check the available responsive and accessibility behaviours, and distinguish checks performed from anything unverified. Ask me which details feel like me or feel forced.

### Step 10: Make the site easy to maintain — Skill 07

> Read `design-sesh-portfolio-builder/skills/07-personal-site-handoff/SKILL.md`. Prepare the owner guide for the completed site, including preview instructions, where to edit content and assets, active identity decisions and remaining launch work. Update it to include the Projects and About pages. Do not publish as part of this handoff.

## 5. Continue without starting over

In a new Claude chat, give access to the same website files and `design-notes/`, then say:

> Continue this portfolio from the existing files. Read `design-notes/02-personality-brief.md`, `design-notes/03-selected-direction.md`, the current site blueprint and relevant build/review notes. Tell me which stage is already complete, then run the next requested skill. Preserve current decisions and reuse finished work.

If your preferences change, update the selected direction and name which downstream plans/pages need revision. Rejected ideas should remain distinguishable from the active design.

## 6. Use a shorter route when appropriate

- **General personal website:** 01 → 02 → 03 → 04 → 05 → 06 → 07. Omit the portfolio-specific stages if you do not need them.
- **Add a project to an existing portfolio:** 08 for the new project → 09 to integrate the collection and any agreed detail page → 06 → 07.
- **Refresh only About:** 10 → 06 → 07, using the existing personality brief and direction. Revisit 02 only if important personal context is missing or changed.
- **Existing site needs both pages:** prepare projects with 08 as needed → 09 → 10 → 06 → 07. Keep its approved identity unless you request a redesign.

## 7. What to expect

Bring references, real work, any writing or images you want to use, dislikes and privacy boundaries. Your personality can appear through a quiet sign-off or an object that matters to you; it does not require a decorative theme or elaborate animation.

Existing photos, honest crops, CSS, live text and simple SVG are enough. No generated portraits, fabricated project results or borrowed identity are required. Unsupported claims and missing permissions stay visible in the notes. Originals remain intact by default. Only actual permitted checks are reported as passed, and local completion does not mean the site is published.
