# Accessibility implementation

These are recorded implementation patterns. Offer them as preferences, not as diagnoses or a claim that one palette/font helps every person.

## Shared preference contract

| Concern | Web | Android |
|---|---|---|
| Storage | Versioned localStorage key `skeinwise.accessibility.v1` | Private SharedPreferences named `accessibility` |
| Apply | Root dataset/classes, before CSS paints | Observable Compose state and composition locals |
| Palette | Default, protanopia, deuteranopia, tritanopia | Same choices, adapted to light/dark Material roles |
| Text | OpenDyslexic, roomier reading, browser zoom | OpenDyslexic, roomier reading, extra 20% font scale |
| Controls | Larger hit areas, wrapping, min 48 CSS px | 25% UI density increase; Material minimum 64 dp instead of 48 dp |
| Motion | User option plus device reduced-motion preference | No corresponding app-specific switch in the inspected implementation |
| Reset | Reset accessibility defaults | Reset accessibility defaults without changing theme |

Apply immediately, work before sign-in and retain across sign-out/restarts on that installation. No cross-device synchronization. Validate stored enums and boolean types. Web storage failures must leave the page usable and honestly report that settings were not saved; cross-tab storage events reapply settings. Keep appearance preferences separate from private account data.

## Web framework

Load the small preference script before stylesheet paint. Normalize settings against defaults, set `document.documentElement.dataset.vision`, and toggle `a11y-*` classes. CSS variables implement colors centrally; preference selectors override typography, spacing, controls and motion. Native fieldsets, labels, checkboxes/selects, a live save-status area, a skip link and visible keyboard focus make the settings usable.

Do not replace browser zoom with a CSS transform. Preserve responsive reflow and the viewport's ability to zoom. Large-control rules use min sizes and padding, not fixed heights; headers/nav/actions wrap and sticky headers can become ordinary-flow content when expanded.

## Color-vision palettes

Use semantic tokens, never global image filters. In the recorded light themes:

- Protanopia: blue primary `#005a80`, dark blue `#003d58`, warm gold/coral surfaces.
- Deuteranopia: blue primary `#184f91`, dark blue `#103566`, warm gold/coral surfaces.
- Tritanopia: rose primary `#80364e`, dark rose `#582536`, teal secondary `#00665e`.

Android supplies lighter dark-theme counterparts and appropriate on-accent text. High contrast changes surface/ink/border roles independently. Validate combinations, especially palette + contrast + dark theme; do not infer contrast from the hex color name. Keep status labels/icons/borders so errors and selection never depend on hue alone.

Photographs, yarn swatches and source PDFs/images retain their colors. Recoloring evidence would undermine the product's identification task. Palette labels express available choices, not individualized correction.

## OpenDyslexic and reading space

Bundle regular/bold fonts locally with their SIL Open Font License and attribution. The original source was the official OpenDyslexic repository. If obtaining fonts anew, verify the actual downloaded release/license. Do not require a third-party font request.

Web uses `@font-face`, `font-display:swap`, shared serif/sans variables and form/text overrides. Android uses `FontFamily(Font(...Normal), Font(...Bold))` and adapts every Material typography role. Set adequate line height: the example uses at least 1.5× for dyslexic-font styles and 1.8× for roomier reading, with 0.04em-equivalent letter spacing; web also adds word/paragraph spacing and removes truncated table text.

Source PDFs/images are not rewritten by interface font settings. Explain that plainly. Check heading wrapping and all form controls; changing only body text misses important UI.

## Three different forms of enlargement

1. **Web/browser zoom:** browser-managed scaling and reflow. Larger-control preference separately increases hit targets and padding.
2. **Android interface zoom/text:** provide adjusted `LocalDensity` once at the theme boundary:
   - density = inherited density × 1.25 when larger controls is on;
   - fontScale = inherited fontScale × 1.2 when larger text is on.
   - provide `LocalMinimumInteractiveComponentSize` of 64 dp or default 48 dp.
   Preserve inherited device settings. Expanding only Material's reserved target can leave the visible control tiny; density scaling enlarges what the user sees. Avoid applying the multiplier again in nested components/dialogs. Combined options and system scale compound, so layouts must reflow.
3. **PDF zoom:** native PdfRenderer plus Compose gestures, independent of interface typography. The example supports 100–400%, 25-percentage-point button increments, pinch, double tap, pan and Fit page. Retain page/zoom/pan during full-screen transitions.

PDF rendering uses a serial background owner, closes pages/descriptors correctly, renders only the current page and debounces zoom requests. Recorded bitmap caps: 4096 pixels per edge and six million pixels. Never allocate the entire document at high zoom. The 500-page storage/read limit is distinct from the 20-page AI-input limit.

Private reading position/bookmarks are scoped to account, server, session, project/file and content fingerprint. They are cleared on sign-out/revocation; unlike accessibility preferences they must not survive as cross-account history. Handle failed persistence without falsely claiming a save.

## Layout and verification

Compose settings use selectable/toggleable rows with a radio/switch semantic role and null child click callbacks, yielding one labeled target. Use expanding headers, wrapping actions, scrollable content and correct safeDrawing/Scaffold inset consumption. Reserve keyboard space once. Navigation reacts to effective width and font scale.

Exercise palettes in light/dark and high contrast; font + spacing + UI zoom + large system text; 320 dp/narrow and short windows; dialogs/sheets; sign-in and signed-in screens; keyboard and cutouts; restart/reset/sign-out; browser storage denied; draft/save errors; photos/swatches unchanged. Check page zoom and document replacement separately.

Inspect actual contrast pairs (the historical Android tests use a 4.5:1 ordinary-text target), screen reader labels/traversal, focus visibility and keyboard completion. Browser 200%/400% zoom and device font/display enlargement are useful new checks, not claims every historical screen was tested at those settings. Record emulator versus physical-device coverage and remaining assistive-technology checks.
