# Welcome to Design Sesh Portfolio Builder

This is a practical workflow for building a portfolio from your own references, work and personality. You do not need to arrive with a perfect biography, tidy project files or a fully formed visual direction. Bring what you have; the skills help you work through it in a useful order.

The process comes from the Design Sesh portfolio build: collect references, understand the work, organize one project at a time, map the strongest evidence into a story, plan layouts, build locally and review the result. This kit adapts that process to your identity. It does not prescribe Design Sesh's colours, interests, museum scenes or other personal motifs. It uses existing assets and code rather than image generation.

Use this page to understand the journey. [START-HERE.md](START-HERE.md) has the exact prompts for each stage, and the [README](README.md) lists all 12 skills.

## Start with a workspace, not a finished filing system

Create one main folder for your portfolio. Download or clone this repository into it. Put visual inspiration, personal content and project sources in separate places so Claude can tell what each file is for.

```text
my-portfolio/
  design-sesh-portfolio-builder/       # This kit; keep its skills and tools together
    WELCOME.md
    START-HERE.md
    skills/
    tools/project_map.py
  references/
    websites/                         # Screenshots of sites you like
    colour-and-brand/                 # Colour references and brand examples
    layouts-and-details/              # Type, spacing, objects or interactions
    reference-links.md                # URLs and what you like about them
  personal-content/
    about-me.md                       # Your own words, interests and boundaries
    writing/                          # Optional examples of how you write
    approved-photos/                   # Images you are comfortable considering
    cv/                               # Optional factual background
  project-sources/
    project-one/                      # One complete project, originals intact
    project-two/
  portfolio-prep/                      # Created during project preparation
    project-one/
  design-notes/                       # Decisions, evidence and handover between skills
    projects/
      project-one/
  site/                               # New local website, or your existing app structure
```

These are suggested names. Preserve a functioning site's existing structure. Paths in the examples assume your terminal or Claude workspace starts in `my-portfolio/`.

You can ask Claude to create the empty folders. Put private material in a local location you deliberately choose; these folder names do not themselves enforce privacy. Keep your reference collection, raw project files, generated notes and local maps out of the public skill repository and the site's published assets. Publish only the selected, reviewed website files. If your website workspace uses Git, review its ignore rules and tracked files before any push.

### What goes in a project folder?

Give each project its own recognisable folder, such as `community-library/` or `navigation-prototype/`. Start with the material you already have:

- Briefs, reports, presentation boards and old portfolio pages.
- Research, sketches, diagrams and process notes.
- Screenshots, prototypes, videos and final deliverables.
- Editable design files, drawings, models and their dependencies.
- Any notes explaining your role, collaborators, dates and what actually happened.

Do not pre-delete files or decide which version is final just to make the folder look tidy. Keep models with textures, code with dependencies and linked documents in their existing structure. If a project has a huge archive, explain that to Claude so it can prioritize review and report coverage.

A short `project-context.md` helps: what the project was, your contribution, whether it was academic/client/personal/team work, what was proposed versus completed, and what must remain private. Unknown answers can stay unknown.

### What goes in reference-links.md?

Record a link and a sentence about why you saved it. For example: “I like the restrained colours and spacious project index, but not the animated cursor.” This lets Claude separate colour preferences from layout or interaction preferences. Include screenshots when a site is difficult to access. You do not need to gather more references simply to fill every folder.

## Phase 1: understand your taste and choose a direction

**01 Reference audit → 02 Personality interview → 11 Choose your colours → 03 Design directions**

Claude first inspects the reference images and records recurring patterns, differences and what was actually reviewed. Then it asks a few questions about your audience, voice, interests and boundaries, reusing information you have already supplied.

The colour skill asks for images, favourite sites and brands, plus a few personal preference questions. It offers two or three palettes applied to the same small website example so you can compare them. You choose one. The design-direction skill then explores composition, typography and image treatment within that colour choice. You select a direction before implementation.

You do not need design vocabulary to respond. “This feels too formal,” “I like the empty space,” or “I like the colours but not the layout” is useful feedback. Claude should translate that into concrete adjustments rather than make you defend a preference.

**You leave this phase with:** a reference audit, personality brief, selected palette and chosen design direction in `design-notes/`.

## Phase 2: turn project folders into usable evidence

**08 Project folder to portfolio — repeat for each project**

Run this skill on one source folder at a time. It inventories the material, reviews its substance, identifies distinct versions and exact duplicates, and separates useful public evidence from private or uncertain material. Originals remain intact by default. Curated folders or manifests point to what is useful without destroying the source archive.

The skill prepares these notes under `design-notes/projects/<project-slug>/`:

| File | Why it exists |
| --- | --- |
| `project-audit.md` | What was reviewed, what the project is and what remains uncertain |
| `file-index.csv` | Where each file is, its review status, duplicates and selection reason |
| `evidence-ledger.md` | Which source supports each claim about your work |
| `case-study-plan.md` | The narrative, sections, image choices, captions and layout ideas |
| `project-card.md` | A concise title, summary and cover proposal for the Projects page |
| `asset-manifest.csv` | Original sources and any exported/cropped derivatives |
| `project-map.json` | A machine-readable lookup map built with the Python helper |
| `project-map-annotations.json` | Reviewed descriptions, tags and selection notes used by the map |

Project stories should show your actual decisions and contribution. If an outcome was never measured, the site should not invent a statistic. If two documents disagree, keep the discrepancy visible until resolved or omit the disputed claim.

## Make project files easy for AI to find

In the original build, file indexes, manifests and per-project notes made it possible to return to the right source while designing. This kit adds a small Python helper to make that lookup repeatable. A “Python map” here means **a JSON file catalog created and searched with Python**, rather than a diagram or a generated Python file for every project.

The helper reads files and records relative paths, stable path-based IDs, sizes, SHA-256 checksums and exact-duplicate relationships. It does not open a PDF to understand its story, inspect an image, transcribe video or decide publication permission. Claude's review adds that meaning in a separate annotations file.

### 1. Create an initial map

Ask Claude to run this, or run it yourself if Python 3 is available:

```bash
python3 design-sesh-portfolio-builder/tools/project_map.py index \
  --source project-sources/community-library \
  --output design-notes/projects/community-library
```

Replace `community-library` with your folder name. Keep output outside the source folder. The command writes `project-map.json` and reports indexed/skipped counts. Symlinks are skipped; unreadable or changing files are reported. A nonzero exit with skipped entries means the map is incomplete and needs attention. Large sources take longer because hashes require reading their bytes.

### 2. Add reviewed descriptions and tags

After actually inspecting sources, Claude creates `project-map-annotations.json` in that project's notes folder. Keys must match the source-relative paths exactly. For example:

```json
{
  "Final presentation/Section drawing.png": {
    "summary": "Section drawing showing the courtyard and circulation",
    "tags": ["section", "courtyard", "circulation"],
    "category": "drawing",
    "review_status": "visually-reviewed",
    "public_use": "unknown",
    "selected_for": ["spatial-strategy"],
    "location_notes": "Drawing labels inspected; public export still needs title-block review"
  }
}
```

This is an illustrative record, not a claim about a supplied project. Only set `public_use` to `approved` once the owner has authorized its use and the particular export has been reviewed. Selection for a chapter is a design decision; it is separate from permission to publish.

Use `location_notes` for page numbers, drawing labels or video timestamps that were actually inspected. Summaries must describe observed content, not guesses from filenames. `review_status` can distinguish text extraction, partial review and visual review rather than imply all formats received the same inspection.

Rebuild the map using those annotations:

```bash
python3 design-sesh-portfolio-builder/tools/project_map.py index \
  --source project-sources/community-library \
  --output design-notes/projects/community-library \
  --annotations design-notes/projects/community-library/project-map-annotations.json
```

The helper rebuilds generated data and reads annotations from their separate file. It reports annotation paths no longer found in the source. IDs stay stable while relative paths stay unchanged; a rename changes the ID. Content changes alter the checksum. Compare checksums after updates and re-review changed material: annotations are not automatically revalidated, and the script does not verify permissions.

### 3. Search before designing a section

```bash
python3 design-sesh-portfolio-builder/tools/project_map.py find \
  --map design-notes/projects/community-library/project-map.json \
  --query "courtyard section"
```

Search matches all query words against paths and annotation text. It searches metadata, not the file contents. To retrieve only records marked approved and selected for a particular chapter:

```bash
python3 design-sesh-portfolio-builder/tools/project_map.py find \
  --map design-notes/projects/community-library/project-map.json \
  --public-only --selected-for spatial-strategy
```

Ask Claude: “Read this project's audit and case-study plan. Search its map for section drawings, open the matching files, and choose the image that best explains circulation. Check the evidence and public-use status before exporting.” The map locates candidates; Claude still needs to inspect the actual source and selected export before using them.

Keep these maps local. They may contain private paths and summaries and are not website content. If Python is unavailable, the CSV index and project notes still support the workflow; record that the JSON map was not generated.

## Phase 3: find your story and plan the site

**12 Find your story → 04 Site story and personal touches**

Once the project evidence is available, connect it to your actual background and interests. The story skill offers concise angles and home/About copy based on confirmed experiences. You choose what feels accurate. It does not force an unusual origin story or turn an ambition into a past achievement.

The blueprint then maps that story into routes and sections. Each section has a purpose, content, source assets and a desktop/mobile layout idea. Plan the project pages individually: a research project and an architectural project may need different ways to explain their decisions.

Personal details enter where they have a reason: your phrasing, an object, a small annotation or a sign-off. They should support the work and feel recognisably yours. The same website identity carries across Home, Projects and About without repeating every composition.

**You leave this phase with:** selected story copy, a site blueprint and project-specific case-study plans. These are internal planning documents, not automatically public pages.

## Phase 4: build a complete local version

**05 Build foundation → 09 Projects → 10 About**

Build the shared type, colours, spacing, navigation and footer first. Reuse the selected palette and direction. Use the maps and manifests to locate real project imagery, then make web derivatives instead of sending huge source files to the browser. Keep important text editable in HTML.

The Projects skill builds the collection and individual case studies included in the agreed scope. Each story uses its own evidence and appropriate layout. The About skill builds from the selected personal story instead of starting the interview again. Reuse any pages already completed by the foundation builder rather than implementing them twice.

Before a large revision, record what can change and what is approved to stay as it is. In the Design Sesh build, shared entrances, page areas and homepage selections were protected during specific passes. Your protected areas should reflect your own decisions. Use copies, version control or checksums where useful to verify that scoped changes stayed scoped.

Keep experiments recoverable and label the active choice. If you reject a cover or layout, retain it as an experiment without allowing an old note to override your newer direction. Optional motion comes after a coherent static page, with touch, keyboard and reduced-motion behaviour considered.

## Phase 5: review, refine and hand over

**06 Personality and usability review → 07 Owner handoff**

Review the real site on mobile, tablet and desktop where browser access permits. Check text wrapping, overlaps, scrolling, images, links, keyboard focus and motion alternatives. Review the voice and personal touches too: do they sound natural, and does the work remain easy to understand?

Save useful screenshots and a report of checks actually performed. A static check cannot prove an animation is smooth. Missing browser access should be recorded as unverified rather than as a pass. Resolve clear defects, keep remaining questions visible and update implementation status.

The handoff explains how to preview, edit content, replace assets and add another project. It records the current identity and remaining launch work. Local completion and public deployment are separate steps; only reviewed web assets should be published.

## Keep progress between Claude chats

Your notes are the memory of the project. Preserve the reference audit, selected palette/direction, project maps and evidence, active story, blueprint, build notes and review. In a new chat, provide the same workspace and ask Claude to read those before making changes.

A useful continuation prompt:

> Continue my portfolio from the existing files. Read the current design notes and selected direction, then the relevant project audit, case-study plan and map. Reuse completed work and current decisions. Work on [specific next task], record changes and tell me what remains unverified.

When you add a project later, repeat **08 → 09 → 06 → 07**, refreshing its map and notes. Revisit colour or personal story only when your preferences or goals have changed.

## Your full route

**01 References → 02 Personality → 11 Colours → 03 Direction → 08 Project preparation and maps → 12 Your story → 04 Blueprint → 05 Foundation → 09 Projects → 10 About → 06 Review → 07 Handoff.**

You supply the work, decisions and what feels true to you. Claude helps inspect, organize, propose, build and verify. [Open START-HERE.md](START-HERE.md) when you are ready to run the first skill.
