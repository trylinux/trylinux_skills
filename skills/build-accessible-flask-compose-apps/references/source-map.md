# Source map and provenance

Extracted from Skeinwise, repository `trylinux/FAIRF`, commit
`da3404de0a8a055a961e98fffd900e5146d677d4`, on November 23, 2026.
The source repository may require access. These references describe its implementation without shipping private photos, records, benchmark outputs, credentials or production infrastructure values.

Base for commit-pinned file links:
https://github.com/trylinux/FAIRF/tree/da3404de0a8a055a961e98fffd900e5146d677d4

| Topic | Source paths |
|---|---|
| Setup and dependencies | README.md; pyproject.toml; requirements.txt; .env.example; Dockerfile; docker-compose.yml |
| Server tests/deploy | .github/workflows/test.yml; docs/AUTODEPLOY.md; scripts/migrate.sh; scripts/install_debian.sh; scripts/deploy_debian.sh |
| Web design/preferences | app/static/css/app.css; app/static/css/accessibility.css; app/static/js/accessibility.js; app/templates/base.html; app/templates/accessibility.html |
| Android build | android/README.md; android/build.gradle.kts; android/app/build.gradle.kts; .github/workflows/android-ci.yml |
| Android theme/accessibility | android/app/src/main/java/art/myfiber/skeinwise/ui/Accessibility.kt; AccessibilityTheme.kt; SkeinwiseTheme.kt (same directory) |
| Tests | tests/test_accessibility.py; tests/js/accessibility.test.cjs; android/app/src/test/java/art/myfiber/skeinwise/ui/AccessibilityTest.kt; ThemeTest.kt (same directory); android/app/src/androidTest/java/art/myfiber/skeinwise/ui/AccessibilityLayoutTest.kt |
| Design reasons and screenshots | docs/ANDROID_UI_REVIEW.md (November 1); docs/USER_JOURNEY_REVIEW.md (November 21); docs/ANDROID_GUIDED_WORKFLOWS.md |
| PDF/workspace behavior | docs/ANDROID_PDF_READER.md; docs/PATTERN_READER.md; docs/PROJECT_WORKSPACE.md; docs/ANDROID_KNITTING_MODE.md |
| AI boundaries | docs/YARN_IDENTIFICATION_PIPELINE.md; docs/PATTERN_MODEL_PIPELINE.md |

Relevant history: accessibility `9ab6348` (#121); PDF zoom/reading `ccd29b6` (#114); benchmark tools `cacb7b8` (#122); journey improvements `334b87c`; bounded job progress `da3404d`.

The source files establish implementation and recorded reasons, not every original conversation. No broad framework-selection study, real-maker usability study, complete accessibility certification or independent replication of model benchmark claims was established during skill extraction. Do not manufacture those claims.
