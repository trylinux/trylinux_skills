# Design decisions and how to make them

## Evidence vocabulary

**Recorded** means the repository documents the reason. **Observed** means code demonstrates behavior but does not establish why it was originally chosen. **Transferable inference** is a useful interpretation, not a historical claim. The repository does not contain a complete transcript of every decision.

## Architecture

| Choice | Evidence and rationale |
|---|---|
| Flask/Jinja web with a shared server API and native Compose Android | Observed architecture. Transferable inference: domain rules can remain on the server while each client uses its platform's UI. The records inspected do not establish a formal Flask-versus-SPA or native-versus-cross-platform selection study. |
| Shared tokens and native Material roles | Recorded: fixed light colors and mismatched surfaces made Android inconsistent. Explicit light/dark semantic roles let menus, dialogs and existing screens adopt one theme without rewriting the data/API layer. |
| Durable worker for identification | Observed: jobs report progress and have bounded retries and a shared elapsed deadline. They save a usable result before optional enrichment. Inference: separate long model work from HTTP request lifetime and avoid making optional research block the result. |
| Private, editable AI evidence | Recorded: estimates remain distinguishable from facts, users review/correct results, and original reader evidence is retained. AI does not invent remaining inventory, acquisition history or measured machine gauge. |
| Local accessibility preferences | Recorded behavior: usable before sign-in and retained across sign-out. Inference: access needs should not depend on the currently authenticated account. This is distinct from private content/history, which is cleared at session boundaries. |

## Visual language

Web tokens use warm paper (`#f4efe6`), dark ink (`#251f24`), plum (`#5d294f`), coral (`#cf765d`), ochre and muted green; serif headings, system/sans body text, rounded panels and pill buttons. These are observed values, not proof each original pair meets every contrast requirement.

Android's reviewed redesign uses warm stone and mulberry in light mode, warm charcoal and muted pink in dark mode. Explicit Material 3 surface/container/on-color roles avoid accidental default-purple dialogs. Shape radii are 12/18/24 dp. Match the product's visual character across platforms, not every hex value.

Recorded naming principle: playful destinations with plain descriptions; precise measurements, actions, privacy and security language. Nook = home, Hoard = inventory, Makes = projects, Cupboard = references/equipment. Keep that principle when adapting, not necessarily those names.

## Journey improvements with documented reasons

| Problem | Decision | Reason/evidence |
|---|---|---|
| Wrapping text navigation consumed phone space | Five compact icon destinations; rail at 600 dp; Explore sheet below 360 dp or above 130% font scale | Android UI review applied platform navigation guidance; short/narrow/large-text layouts were exercised. Use full accessible labels and a scrollable, expanded sheet. |
| Collections began with many controls | Search and Add stay visible; View & filters holds secondary controls | Review identified weak hierarchy and crowding. Maintenance/photos move into expandable details. |
| Editing controls preceded pattern instructions | Read pattern / Prepare / Track progress; immediately readable transcription drafts | Journey review applied visibility of system status and progressive disclosure. Sections remain freely navigable; they are not mandatory wizard gates. |
| Setup facts were scattered | Group size, materials, gauge and tools; support manual editing | Pattern-reading references distinguish preparation from instructions. Unknown is empty/unknown, not zero. |
| Generated text looked final or disappeared behind editors | Show drafts with review status; save confirmed text separately; preserve original wording/line breaks | Row/repeat punctuation and abbreviations carry meaning. AI transcription is not authoritative until reviewed. |
| Failures discarded work | Retain drafts on failed saves, section changes and Android recreation; retry in context | Testing exposed draft loss and led to fixes. Return the user to the relevant result/section. |
| Long yarn forms were hard to navigate | Photos → Clues → Review, and grouped editing sections | Explicit submission is the boundary for sending selected photos; settings can open without discarding the draft. |

## Reuse the research method

1. Map complete journeys, including first use, return use, no results, failures, archive/restore and offline conflicts.
2. Capture the actual problem in screenshots or a reproducible interaction.
3. Consult primary platform guidance and relevant domain guidance for the specific problem. The historical reviews referenced Android navigation, Material 3, dark theme/system bars, Nielsen Norman Group status/disclosure articles, and TKGA/Craft Yarn Council pattern-reading guidance.
4. Explain how a principle changes this screen; citing a principle alone does not prove the design.
5. Implement at the smallest coherent layer: shell/theme, then crowded flows, then domain-specific details.
6. Test real composables/templates using synthetic data and blocked network fixtures where practical. Exercise normal/large text, narrow/short screens, keyboards, failed writes and restoration.
7. Record what was actually checked. Historical emulator tests and screenshots are evidence about those fixtures, not a real-maker usability study or proof of TalkBack/OEM behavior.

When new standards or platform recommendations matter, read current official guidance. Historical links and thresholds describe the example; do not present them as a current compliance certification.

## Guidance cited by the original reviews

These are provenance links from the reviewed documents, not newly verified standards:
- [Android layout/navigation](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns)
- [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
- [Android dark theme](https://developer.android.com/develop/ui/views/theming/darktheme)
- [Compose system bars](https://developer.android.com/develop/ui/compose/system/system-bars)
- [Visibility of system status](https://www.nngroup.com/articles/visibility-system-status/)
- [Progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- [Craft Yarn Council pattern reading](https://www.craftyarncouncil.com/standards/how-to-read-knitting-pattern)
- [TKGA pattern reading](https://tkga.org/wp-content/uploads/2019/03/How%20to%20Read%20a%20Knitting%20Pattern.pdf)
