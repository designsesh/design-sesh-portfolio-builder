# Start here: build a portfolio that feels like you

The skills now include detailed execution procedures, input/output contracts and completion checks. [METHOD.md](METHOD.md) explains the shared working approach behind all 12.

Need setup help? See [INSTALL.md](INSTALL.md) for Claude, ChatGPT Projects and local Codex.

This kit contains **12 skills** for analyzing your references, learning what makes you you, preparing your real project material and building a consistent portfolio. No image generation is needed.

For a guided explanation of the whole process, folder organization and Python file maps, read [WELCOME.md](WELCOME.md).

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

**01 → 02 → 11 → 03 → 08 (repeat for each project) → 12 → 04 → 05 → 09 → 10 → 07 → 06**

The numbers name the skill folders; they are not a straight numerical checklist. In particular, prepare project evidence with 08 before planning the whole site, and build Projects/About before 07 (mobile adaptation), then 06 (design audit).

## 3. Know what each skill needs and produces

All note paths below are relative to `design-notes/` in your website workspace.

| Order | Skill | Give Claude | Main result | Saved notes |
| --- | --- | --- | --- | --- |
| 1 | [Skill 01](skills/01-reference-folder-audit/SKILL.md) — Analyze reference images | Reference images and screenshots | A visual inventory, recurring patterns, contrasts and buildable ideas | `01-reference-audit.md` |
| 2 | [Skill 02](skills/02-personality-interview/SKILL.md) — Discover personality and voice | Your answers, writing samples and existing personal notes | A brief covering audience, goals, voice, interests and public/private boundaries | `02-personality-brief.md` |
| 3 | [Skill 11](skills/11-choose-your-colours/SKILL.md) — Choose website colours | Uploaded images, favourite sites/brands and brief preference answers | Two or three practical palettes and an owner-selected colour system | `11-colour-options.md; 11-selected-palette.md` |
| 4 | [Skill 03](skills/03-personal-design-directions/SKILL.md) — Choose a design direction | Reference audit and personality brief | Distinct visual directions and a recorded choice | `03-design-directions.md; 03-selected-direction.md` |
| 5 | [Skill 08](skills/08-project-folder-to-portfolio/SKILL.md) — Prepare each portfolio project | One project folder with documents, images, prototypes and source files | File index, evidence ledger, curated assets, case-study plan and project-card copy | `projects/<project-slug>/` |
| 6 | [Skill 12](skills/12-find-your-story/SKILL.md) — Find your story | Personality notes, real experiences and prepared project evidence | A factual personal story, introduction and About copy in your voice | `12-personal-story.md` |
| 7 | [Skill 04](skills/04-site-story-and-personal-touches/SKILL.md) — Plan the site and personal details | Chosen direction, personality brief and prepared project stories | Routes, section layouts, copy, asset mapping and purposeful personal touches | `04-site-blueprint.md` |
| 8 | [Skill 05](skills/05-build-personal-site/SKILL.md) — Build the site foundation | Site blueprint, chosen direction and approved assets | A working local site, shared design system and page foundations | `05-build-notes.md; 05-asset-manifest.csv` |
| 9 | [Skill 09](skills/09-build-projects-page/SKILL.md) — Build Projects and agreed case studies | Prepared projects, blueprint and existing site | A Projects collection with real destinations and any agreed detail pages | `projects-page-build.md` |
| 10 | [Skill 10](skills/10-build-about-page/SKILL.md) — Build About in your voice | Confirmed biography, personality brief and approved personal assets | An About page that matches you and the rest of the site | `about-content.md; about-page-build.md` |
| 11 | [Skill 07](skills/07-mobile-responsive-design/SKILL.md) — Mobile Responsive Design | Built pages, component code and selected direction | Implemented responsive layouts and purposeful touch-friendly alternatives | `07-mobile-plan.md; 07-component-adaptations.csv; 07-mobile-review.md` |
| 12 | [Skill 06](skills/06-design-audit/SKILL.md) — Design Audit | Built site, mobile results and the active earlier documentation | Traceable specification audit, fixes/retests and maintenance record | `06-design-audit.md; 06-design-audit-matrix.csv; site-maintenance.md` |

Skill 08 runs once per project and stores separate notes for each. It records actual review coverage, duplicates, evidence, privacy issues and missing material. A file named FINAL is not automatically treated as authoritative.

Skill 05 builds the shared site and reuses the dedicated page skills where appropriate. Skills 09 and 10 extend that same implementation; if a page is already complete, inspect and improve it instead of building it twice.

## 4. Copy-and-paste prompts for all 12 skills

Run these in the order shown. Replace example folder paths and project names with your own. Keep the same website workspace throughout.

### Step 1: Analyze reference images — Skill 01

> Help me build a portfolio that feels like me. My reference images are in `references/`. Read `design-sesh-portfolio-builder/skills/01-reference-folder-audit/SKILL.md` and carry out the reference audit. Do not generate images. Save outputs to `design-notes/` and tell me what you actually inspected.

### Step 2: Discover personality and voice — Skill 02

> Read `design-sesh-portfolio-builder/skills/02-personality-interview/SKILL.md` and run the personality interview using the reference audit and any notes in `personal-content/`. Reuse what I have already told you. Ask about my voice, goals and meaningful personal details, and wait for my answers before treating them as confirmed.

Answer the interview before moving to design directions. It is fine to say you do not know or do not want to share something.

### Step 3: Choose website colours — Skill 11

> Read `design-sesh-portfolio-builder/skills/11-choose-your-colours/SKILL.md`. Help me choose website colours from my reference images, favourite websites and brands. Ask a few focused personal preference questions, show two or three usable palettes and help me choose one. Save the selected roles and colour values for the next skill.

### Step 4: Choose a design direction — Skill 03

> Read `design-sesh-portfolio-builder/skills/03-personal-design-directions/SKILL.md`. Use my reference audit and personality brief to propose distinct, buildable directions. Help me choose one, then record the selected direction. Do not generate images.

Choose a direction before the site blueprint and build. Project file inventory can proceed independently if you need more time to choose.

### Step 5: Prepare each portfolio project — Skill 08

> Read `design-sesh-portfolio-builder/skills/08-project-folder-to-portfolio/SKILL.md`. Analyze and organize the project in `project-sources/project-one/` for my portfolio. Leave originals intact. Prepare its verified story, curated assets, card copy and case-study plan. Work on this project only and report anything you could not review.

Repeat this step for each project, changing the source path. Keep a separate project slug and notes folder each time.

### Step 6: Find your story — Skill 12

> Read `design-sesh-portfolio-builder/skills/12-find-your-story/SKILL.md`. Help me find a clear story from my real experiences, personality notes and prepared projects. Ask only what is missing, offer two concise angles, and help me choose wording that feels accurate for my home and About pages.

### Step 7: Plan the site and personal details — Skill 04

> Read `design-sesh-portfolio-builder/skills/04-site-story-and-personal-touches/SKILL.md`. Plan the portfolio around my selected direction, personality brief and prepared project notes. Include my Projects and About pages, decide what each section is for, and map a few meaningful personal touches. Identify whether individual case-study pages belong in the scope.

### Step 8: Build the site foundation — Skill 05

> Read `design-sesh-portfolio-builder/skills/05-build-personal-site/SKILL.md` and implement the agreed site blueprint in this workspace. Reuse an existing working stack where present. Build the shared design foundation, navigation and local site; use the dedicated Projects and About skills for those pages. Reuse existing assets and code without image generation.

### Step 9: Build Projects and agreed case studies — Skill 09

> Read `design-sesh-portfolio-builder/skills/09-build-projects-page/SKILL.md`. Build or complete my Projects page using the prepared project notes and selected direction. Include individual case-study pages only where the blueprint or my request calls for them. Use real destinations, verified claims and personal details that fit the rest of my site.

### Step 10: Build About in your voice — Skill 10

> Read `design-sesh-portfolio-builder/skills/10-build-about-page/SKILL.md`. Build or complete my About page using my own voice, confirmed background and approved personal content. Ask only for important missing facts. Make its personal touches feel natural and consistent with my Projects page and the rest of the site.

### Step 11: Build and check mobile/touch layouts — Skill 07

> Read `design-sesh-portfolio-builder/skills/07-mobile-responsive-design/SKILL.md`. Inspect and improve the built site for narrow screens and touch input. Identify desktop components that need a different mobile form, recommend purposeful alternatives, and implement the in-scope adaptations. Preserve content and the selected identity, test actual tasks and record desktop regressions and unavailable checks.

### Step 12: Audit the result against the documentation — Skill 06

> Read `design-sesh-portfolio-builder/skills/06-design-audit/SKILL.md`. Audit the implemented site against my active personality brief, palette, direction, story, blueprints, project evidence and mobile decisions. Map requirements to actual output, fix supported mismatches and retest. Record intentional deviations and unverified items. Reconcile the current editing/maintenance notes as part of the audit; do not publish.

## 5. Continue without starting over

In a new Claude chat, give access to the same website files and `design-notes/`, then say:

> Continue this portfolio from the existing files. Read `design-notes/02-personality-brief.md`, `design-notes/03-selected-direction.md`, the current site blueprint and relevant build/review notes. Tell me which stage is already complete, then run the next requested skill. Preserve current decisions and reuse finished work.

If your preferences change, update the selected direction and name which downstream plans/pages need revision. Rejected ideas should remain distinguishable from the active design.

## 6. Use a shorter route when appropriate

- **General personal website:** 01 → 02 → 11 → 03 → 12 → 04 → 05 → 07 → 06. Omit the portfolio-specific stages if you do not need them.
- **Add a project to an existing portfolio:** 08 for the new project → 09 to integrate the collection and any agreed detail page → 07 → 06.
- **Refresh only About:** 10 → 07 → 06, using the existing personality brief and direction. Revisit 02 only if important personal context is missing or changed.
- **Existing site needs both pages:** prepare projects with 08 as needed → 09 → 10 → 07 → 06. Keep its approved identity unless you request a redesign.

## Migration from the previous review/handoff skills

The former `06-personality-and-usability-review` and `07-personal-site-handoff` definitions have been replaced. Skill **06 is now Design Audit**, combining requirement-based verification with useful maintenance reconciliation. Skill **07 is now Mobile Responsive Design**, which runs before the audit. Keep any existing `06-review.md` or `07-owner-guide.md` as project history; the audit reads and reconciles useful content without deleting it. For locally linked installations, remove only obsolete discovery links and point to the new folders. For uploaded copies, disable/remove the retired definitions and upload the replacements using [INSTALL.md](INSTALL.md).

## 7. What to expect

Bring references, real work, any writing or images you want to use, dislikes and privacy boundaries. Your personality can appear through a quiet sign-off or an object that matters to you; it does not require a decorative theme or elaborate animation.

Existing photos, honest crops, CSS, live text and simple SVG are enough. No generated portraits, fabricated project results or borrowed identity are required. Unsupported claims and missing permissions stay visible in the notes. Originals remain intact by default. Only actual permitted checks are reported as passed, and local completion does not mean the site is published.
