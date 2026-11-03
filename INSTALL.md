# Add this kit to Claude, ChatGPT or Codex

Choose the instructions for the product you actually use. A GPT model, a ChatGPT Project, Claude's uploaded skills and a local coding agent do not all load skills the same way.

For this portfolio workflow, the simplest starting point is to give a file-capable assistant the whole kit and ask it to read one skill at a time. Native skill installation is optional. Keep the kit intact: several skills refer to other skills, the welcome guide or `tools/project_map.py`.

Product instructions checked against the official documentation on **3 November 2026**. Interfaces and workspace policies may change. These instructions have not been tested in every product/account.

## Download the kit first

Open [design-sesh-portfolio-builder](https://github.com/designsesh/design-sesh-portfolio-builder), choose **Code → Download ZIP**, and extract it. You can also clone the repository with Git. A downloaded folder may end in `-main`; rename it to `design-sesh-portfolio-builder` if you want the guide's example paths to match exactly.

Place it inside your portfolio workspace as shown in [WELCOME.md](WELCOME.md). Keep your references and personal/project source files separate from the kit. Installing skills does not automatically grant access to those materials.

## Option 1: use the files directly — no installation

In an environment that can read your workspace, open the portfolio folder and send:

> My website workspace is this folder. Read `design-sesh-portfolio-builder/WELCOME.md`, then `design-sesh-portfolio-builder/START-HERE.md`. Start by executing `design-sesh-portfolio-builder/skills/01-reference-folder-audit/SKILL.md`. My references are in `references/`. Use the existing kit files for any linked skills or Python tools. Save outputs to `design-notes/`. Do not generate images or run all stages at once.

If the assistant cannot read local paths, upload the relevant files or provide a supported connection. A path written in a message is not file access. Upload reference images as images if archive contents are not visually accessible. Supply the whole extracted kit or its ZIP only when the environment can actually inspect/extract it; otherwise attach the active instructions and supporting files separately.

Use [START-HERE.md](START-HERE.md) to select the next skill. Keep completed notes available in later chats. This approach avoids installation differences and preserves the kit's relative links.

## Option 2: install in Claude Code locally

For terminal/local Claude Code, project skills live in `.claude/skills/`; personal skills live in `~/.claude/skills/`. Folder discovery and `/name` invocation are supported. These instructions target local sessions; Cowork and cloud access follow different loading rules. [Official Claude Code skill documentation](https://code.claude.com/docs/en/skills)

For this kit, preserve the original folder relationships by linking the numbered skill folders into your project's discovery directory. On macOS/Linux, from your portfolio workspace:

```bash
mkdir -p .claude/skills
for skill in design-sesh-portfolio-builder/skills/*; do
  target=".claude/skills/$(basename "$skill")"
  if [ ! -e "$target" ] && [ ! -L "$target" ]; then
    ln -s "$(pwd)/$skill" "$target"
  else
    echo "Already exists: $target"
  fi
done
```

These commands create links and do not overwrite existing entries. If a link already exists, inspect it before replacing it. On Windows or where links are unavailable, use Option 1; copying individual folders requires also preserving or resolving their cross-skill/tool references.

Open Claude Code in the portfolio workspace, check its skill menu and explicitly ask for `reference-folder-audit`. Its frontmatter name differs from its numbered folder name. Give Claude the original kit path for linked resources. If discovery fails, reopen the session or use the direct-file prompt.

## Option 3: upload custom skills in Claude web/desktop

Enable file creation/code execution if needed, then open **Customize → Skills**, use the add/upload option and enable the uploaded skill. Organizational policies can restrict this. Follow the official guide for the interface available on your account. [Using skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

Upload **one skill package at a time**, not the whole repository as one skill. Each package needs a root folder named after the `name:` value in its `SKILL.md`. For example:

```text
reference-folder-audit.zip
  reference-folder-audit/
    SKILL.md
```

Make a packaging copy of the numbered folder and name the copy `reference-folder-audit`; leave the original kit unchanged. Zip that folder, not just its loose contents. [Official custom-skill packaging instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

**This kit has shared dependencies.** Uploading an individual skill does not include sibling skills, WELCOME.md or the Python helper. Also provide the intact kit and needed notes in the current working environment, then tell Claude: “Resolve this skill's supporting files from the uploaded/extracted `design-sesh-portfolio-builder` kit.” If Claude cannot resolve them, use Option 1 rather than treating the upload as a self-contained installation. For the full local build and file organization, local Claude Code with workspace access is the clearest route.

## Option 4: use a ChatGPT Project

Create a ChatGPT Project for the portfolio. Add the guides, active skill instructions, relevant reference images and current design notes as project sources. Give separate uploaded copies of the active `SKILL.md` distinctive filenames, such as `01-reference-folder-audit.md`, to avoid confusion among identically named files. Keep their original content.

Project instructions can say:

> Follow the Design Sesh Portfolio Builder workflow. Read the active skill before executing it. Reuse the personality brief, selected palette/direction and current project notes. Ask for missing inputs, distinguish inspected sources from assumptions, and keep each stage's output available for the next stage. Do not invent personal or project facts.

Then ask for one stage by its uploaded filename. This is an instruction-file workflow, not a claim that uploading Markdown installs a native skill. ChatGPT Projects share files/instructions across their chats but do not directly expose a local computer folder; upload or connect the relevant sources. [Official Projects guidance](https://learn.chatgpt.com/docs/projects)

For actual website editing and Python maps, use an environment with access to the site files and execution tools, such as a configured local Codex workspace. Chat uploads alone do not give access to your original project folders.

## Option 5: discover the skills in local Codex

Codex discovers project skills under `.agents/skills/` and supports symlinked skill folders. It also supports personal skills at `~/.agents/skills/`. Use the current product's documented locations rather than assuming Claude's directories work in Codex. [Official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)

From the portfolio workspace on macOS/Linux:

```bash
mkdir -p .agents/skills
for skill in design-sesh-portfolio-builder/skills/*; do
  target=".agents/skills/$(basename "$skill")"
  if [ ! -e "$target" ] && [ ! -L "$target" ]; then
    ln -s "$(pwd)/$skill" "$target"
  else
    echo "Already exists: $target"
  fi
done
```

Open that workspace in Codex and ask it to use `reference-folder-audit`, or choose the skill in the available selector. Include the original kit path so shared resources resolve. If it is not listed, reopen the workspace/session or use the direct-file prompt. Links point to this checkout; rebuild them if you move it. The linked kit must exist inside whichever local/cloud execution environment runs the task.

## Check setup before continuing

Ask the assistant to name the active skill, read its instructions, identify the available inputs and point to the output location. Then run the first real stage. A skill being listed does not prove it can inspect your images, access your folders or run Python.

If something is missing:

| Symptom | What to do |
| --- | --- |
| Skill not listed | Check the folder, exact `SKILL.md` filename, product-specific location and current workspace. Use direct-file instructions if needed. |
| Skill listed, references unavailable | Give the environment access to your images; ask which were actually inspected. |
| Linked skill or Python helper missing | Provide the intact original kit; do not copy only one dependent instruction file. |
| Python unavailable | Continue with the CSV index and notes; generate JSON maps later in an execution-capable workspace. |
| A new chat starts from scratch | Supply the current design notes, chosen direction and relevant project audit/map again. |
| Installation needs an update | Update the original checkout for linked installations; repackage/re-upload individually uploaded copies. Avoid duplicate installations. |

## Run the portfolio sequence

**01 → 02 → 03 → 04 → 05 (per project) → 06 → 07 → 08 → 09 → 10 → 11 → 12**

Use [WELCOME.md](WELCOME.md) for the overall process and [START-HERE.md](START-HERE.md) for prompts. Keep your own private source material and generated project maps outside this public repository.

## Updating an installation from the earlier kit

Folders now run in execution order from 01 through 12. Replace obsolete discovery links with links to the current numbered folders; do not leave duplicate installations. For uploaded skills, update their packages while preserving the unnumbered `name:` value. The old separate review/handoff definitions are retired; install Mobile Responsive Design (11) and Design Audit (12) instead. Keep generated project notes and reconcile earlier filenames by document role rather than deleting them. The current build sequence ends with **09 → 10 → 11 → 12**.
