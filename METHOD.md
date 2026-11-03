# The working method behind these skills

Read this once when beginning work or resuming without context. Each skill gives the stage-specific procedure. This shared method describes how decisions and artifacts should connect.

## Start from what exists

Read the current workspace, latest owner decisions and actual source material before proposing a solution. Inspect reference images rather than classify them from filenames. Inspect project documents and visuals before deciding what is final or useful. A generated inventory is a location tool, not a content review.

Maintain a distinction between **source**, **interpretation**, **proposal**, **owner-selected decision**, **implemented change** and **verified behaviour**. They are different states. An attractive proposal is not a selected direction; a written plan is not a built page; passing a syntax check is not visual QA.

## Extract principles without borrowing someone else's identity

The useful parts of a reference may be placement, scale contrast, overlap, hierarchy, rhythm and negative space. Identify which of these the owner likes before transferring them. Colour and typography are separate decisions. Do not copy a reference's brand, imagery, wording and layout as one package.

Translate a principle into a rule that can be inspected. “Editorial” is insufficient. “A narrow opening paragraph beside an image occupying roughly two thirds of the content width; small captions aligned to the image edge” is usable. The ratio is an example, not a universal token.

## One identity, several stories

Shared typography, navigation, canvas, spacing and interaction conventions make a site coherent. Individual projects can tell their stories through different chapter order, image scale, density and sequences. Repeating the same label/headline/paragraph/image block everywhere is not a substitute for a design system.

Choose layout because of what a section needs to explain: decision comparison, spatial journey, interface change, research question or process evidence. Each personal flourish needs an owner-confirmed source and a reason to appear there. A small typographic note may serve better than an elaborate scene.

## Make work concrete before seeking feedback

Use a rough map before page code, and a small real specimen before expanding a design. Show options against the same content so the owner can compare the intended variable. Recommend a direction and explain the tradeoff; do not present endless choices.

Ask for personal facts, consequential preferences and unclear scope. Resolve routine implementation choices yourself. Approval to build does not authorize unrelated publication. Respect an explicit request to work one project/session at a time; otherwise continue the agreed scope without inventing repeated permission checkpoints.

## Make revisions bounded and reversible

Record what may change and what should stay fixed. Protect specific files, sections or approved components when the task calls for that; do not declare the whole site locked. Use source-control diffs, snapshots or checksums appropriate to the scope. A checksum only protects byte-identical material; shared CSS and scripts can still change its rendered behaviour.

When a composition is rejected, restore the active version and retain the experiment only if useful. Record what was learned and which decision supersedes the earlier one. Do not accumulate old CSS overrides and conflicting “final” instructions. Revisit downstream pages when a shared token changes.

## Treat assets as a traceable system

Keep original archives recoverable, preserve editable dependencies and use exact hashes for duplicate claims. Separate project evidence, decorative assets, derived web exports and reference-only third-party material. An impressive stock image is not proof of project output. No image generation is required or allowed in this kit's workflow.

For exports, record source, transformation, intended use and actual output size. Choose crops by use: expressive covers may crop, while diagrams and interfaces need an uncropped inspection view and readable explanation. Layer only when there is a real asset to layer; account for transparent padding, anchors and optical centering.

## Build completely, then add optional complexity

Deliver a coherent static narrative and real navigation before optional motion. Use shared code primitives rather than a separate system per page. Avoid heavy dependencies that solve a decorative detail. Reuse a functioning project stack and edit generator/template sources when they own the output.

When time or tools are limited, simplify effects, reduce secondary studies or defer optional media. Do not cut factual verification, accessible reading order or required navigation. Record limitations and continue independent work; do not pretend a blocked check passed.

## Keep decisions findable

Maintain `design-notes/decision-log.md` as a concise active-decision record, not a transcript dump:

| ID | Decision / reason | Status | Affected files or pages | Supersedes |
| --- | --- | --- | --- | --- |
| D-001 | Example: restrained accent so project images lead | selected / implemented / verified / proposed / superseded | Exact paths or section names | Earlier decision ID if any |

Keep `design-notes/progress.md` with completed stage outputs, the current task and the next unresolved action. Project audits/maps remain per project. During multi-page builds, each project gets a small implementation status note. Update these at meaningful checkpoints instead of narrating every command.

The final audit and maintenance record should let another session answer: What is current? Why? Where is the supporting source? What is built? What has actually been checked? What remains?

## Working tone

Be direct, specific and considerate. Use her own words where appropriate and discuss work as a capable collaborator. Do not add pet names, staged excitement, personality diagnoses or constant reassurance. A recommendation with evidence and a small next step is more helpful than praise or another questionnaire.

## Finish by checking intent as well as implementation

Run Mobile Responsive Design (11) to adapt interactions and components for constrained layouts and touch, then Design Audit (12) to compare the actual site to the active documentation. Record approved mobile substitutions as decisions rather than treating them as unexplained inconsistencies. The audit combines visual/content/behaviour verification and the current maintenance record. Earlier planning notes remain the contract unless a later owner decision changes them; do not rewrite the contract just to claim success.
