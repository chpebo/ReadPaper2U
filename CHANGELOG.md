# Changelog

All notable changes to ReadPaper2U are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-05-14

First public release.

### Added

- **Embedded offline demo** of *Attention Is All You Need* on the upload
  screen. A 32-scene walkthrough is pre-baked in Simplified Chinese,
  English, and Korean; clicking the demo card loads it without any API
  call. The translate button in demo mode cycles between the three
  pre-baked language versions instead of calling a model.
- **Script translation.** A new top-bar button translates the current
  script in place to the user's UI language. When the app detects that a
  loaded script's language differs from the UI language, it prompts the
  user once and then can perform the translation on confirmation.
- **Mermaid mind map** of the paper's argument structure, generated from
  the dialogue script. Supports pan, zoom, and SVG / PNG export. Mermaid
  is loaded lazily and only on first use.
- **Light theme** alongside the existing dark theme. Both themes share a
  CSS custom-property system and can be switched from the top bar or the
  Settings panel. The palette is warm-neutral, drawing from a desaturated
  cinematic warm-light reference rather than the original purple/pink
  scheme.
- **Keyboard shortcuts overlay.** Press `?` (or click the help icon) for
  a printable list of shortcuts: Space / Enter to advance, Left to go
  back, `A` to toggle auto-play, `L` for the dialogue log, Esc to close
  overlays.
- **Adaptive auto-play.** Per-scene dwell time scales with the scene's
  text length and the script's dominant character set (CJK
  characters-per-minute vs. Latin words-per-minute).
- **Emotion-specific character animations.** The companion avatar's idle
  motion changes per emotion tag — calmer for `thinking`, bouncier for
  `happy`, jolt + settle for `surprised`.
- **Subtle grain texture and stage floor gradient** on the visual-novel
  scene to ground the character against the background.
- **Hand-drawn drop zone** on the upload screen, replacing the standard
  CSS dashed border with a rounded-linecap outline that follows the
  theme.
- **Real-time language switching.** Changing the UI language in Settings
  now applies immediately (rather than waiting for the Save button).

### Changed

- **Visual identity overhaul.** Dropped the 135° purple-to-pink gradient
  used throughout buttons, badges, tags, and the brand mark. The brand
  gradient now appears at most once per surface, and most components use
  a solid accent color for higher contrast and a cleaner profile.
- **Title-screen button hierarchy.** START is now a prominent CTA with a
  solid accent fill, dark text, breathing-glow animation, and a slight
  skew; secondary buttons (PARTNER, SAVES, SETTINGS) are clearly de-
  emphasized outline buttons.
- **Dialogue box** uses a larger border radius (24px), no border, and a
  deeper inset-glow shadow for depth.
- **Default UI language** is now English (was Simplified Chinese).
- **First-run flow.** The Settings overlay no longer forces itself open
  on first launch; new users land on the title screen.
- **Topbar tooltips** are now fully internationalized; switching language
  updates hover labels in real time.

### Removed

- **In-scene "chapter" transition cards.** The auto-detected section
  divider that flashed large chapter titles between major paper sections
  has been removed; users found it disruptive without adding insight.

### Fixed

- Title subtitle no longer interpolates the partner's name into the
  English / Korean variants, which previously produced jarring mixed-
  language hero text like "Let's read papers with 班尼!" when the
  partner name was set in a different script.
- Mind map: the overlay can no longer be dismissed by clicking the
  backdrop while generation is in flight; the Cancel button properly
  aborts the request and the second-click protection prevents
  duplicate-generation overlap.
- Mind map: switched from a one-shot non-streaming call to a streaming
  request with a live character counter, cutting perceived latency on
  long scripts from minutes to seconds.
- Internationalization gaps: error banners, confirm dialogs, quiz
  feedback, save-list metadata, character-editor validation, and several
  loading-step strings that previously stayed in Chinese regardless of
  UI language now go through the `t()` translation helper.
- Dark theme no longer has a noticeable warm cast on neutral surfaces;
  backgrounds, borders, and dim/text colors are anchored on neutral
  greys, while the accent (peach) and secondary (amber) hues remain for
  buttons and highlights.
- Topbar button tooltips localize on language change.
- `_lastShownSection`-style stale state is fully cleared when loading a
  save (no longer carries between papers).

### Security

- All dynamic DOM construction goes through `createEl()` /
  `textContent` / safe `DOMParser` paths; the Mermaid SVG output is
  parsed via `DOMParser` rather than assigned via `innerHTML`.

[0.1.0]: ../../releases/tag/v0.1.0
