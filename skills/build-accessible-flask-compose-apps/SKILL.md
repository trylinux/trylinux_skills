---
name: build-accessible-flask-compose-apps
description: Set up and extend Flask/PostgreSQL web and Kotlin/Jetpack Compose Android apps using the Skeinwise development and design approach, including interface zoom, PDF zoom, color-vision palettes, OpenDyslexic, and evidence-backed design decisions.
---

# Build accessible Flask and Compose apps

Use the Skeinwise/FAIRF implementation as a worked example, adapting its decisions to the requested product. Preserve an existing stack unless a change is justified; this skill does not require a rewrite.

## Choose the relevant reference

- Environment, services, tests, Android tooling, and deployment: [development-environment.md](references/development-environment.md).
- Architecture, visual language, journeys, and why decisions were made: [design-decisions.md](references/design-decisions.md).
- Color vision, typography, scaling, persistence, PDF rendering, and verification: [accessibility.md](references/accessibility.md).
- Historical source locations and evidence limits: [source-map.md](references/source-map.md).

Read only the references needed for the work. They are self-contained; access to FAIRF helps inspect the original but is not required to apply the approach.

## Working method

1. Inspect the target's instructions, dependency manifests, application factory, service boundaries, migrations, theme, UI preferences, and tests. Record what is implemented, what documentation explicitly explains, and what is your proposed rationale.
2. For setup, select a coherent database/network topology before executing commands. Start in mock AI mode and verify both web and background worker paths. Inspect current manifests rather than installing versions from a historical narrative.
3. Map the user's journey and identify its primary action, draft state, submission boundary, successful destination, and retry behavior. Keep original content, AI proposals, confirmed values, and inventory movements distinct.
4. Implement visual changes through shared semantic colors, typography, spacing, and preferences. Preserve accurate photos, swatches, source documents, ownership, and existing drafts.
5. Verify the affected journey at ordinary and enlarged text/display settings, with keyboard/insets and relevant themes. Check visible controls as well as reserved touch targets. Record actual results and remaining device checks.
6. Write a concise decision record: problem → alternatives considered → choice → evidence → tradeoffs → validation → revisit trigger. Never invent alternatives or historical deliberations that were not recorded.

## Delivery

Provide reproducible setup steps or the requested implementation, a source-backed rationale for material decisions, and verification evidence. Label new recommendations separately from historical facts. Use exact commands and paths from the target checkout. Adopting this skill alone does not authorize production deployment, paid AI calls, or publishing private user data.

For choosing models, keep that evaluation separate from UI design; use a task-specific benchmark rather than treating historical configured model IDs as recommendations.
