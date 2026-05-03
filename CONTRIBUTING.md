# Contributing to ReadPaper2U

Thanks for your interest. ReadPaper2U is intentionally a single-file
application: the entire UI, styles, and logic live in `index.html`. This
choice keeps the project trivially deployable (any static host works) and
removes every build-step concern, but it does mean the file is long and
needs a small amount of discipline to navigate.

## Single-file architecture

`index.html` contains, in order:
1. The boilerplate `<!DOCTYPE html>` and `<head>`.
2. One large `<style>` block for all CSS.
3. The visible DOM.
4. One large `<script>` block, wrapped in an IIFE, containing all logic.

There are no external `.js` or `.css` files. The only runtime dependencies
are PDF.js and KaTeX, loaded from public CDNs with a local `lib/` fallback.

## Section markers

Inside both the inline `<style>` and the inline `<script>`, sections are
delimited by:

```
/* ---------- Section Name ---------- */
```

A regenerated table of contents lives near the top of the inline script,
between the markers `/* === BEGIN TOC === */` and `/* === END TOC === */`.

When you add or rename a section, regenerate the TOC so line numbers and
section names stay accurate:

```bash
python find-section.py --update-toc
```

`find-section.py` is standard-library only (no installation needed) and
will:

- list every section it finds (`python find-section.py`),
- filter by substring (`python find-section.py --name api`),
- print the TOC block to stdout (`python find-section.py --toc`),
- rewrite the TOC block in place (`python find-section.py --update-toc`).

## Coding conventions

- **Vanilla JavaScript only**, no framework. The app deliberately avoids
  React, Vue, jQuery, and bundlers. New code should keep this constraint.
- **No inline event handlers** (`onclick="..."`). Bind events through
  `addEventListener` in the relevant section.
- **No `eval`, no `innerHTML` for untrusted content.** DOM construction
  goes through the small `createEl()` helper, and dynamic text is set via
  `textContent`.
- **State lives on a single `state` object.** Reach for it rather than
  introducing module-scoped mutables in new sections.
- **CSS uses custom properties** (`--bg-0`, `--accent`, etc.) for theming.
  Avoid hard-coded color values in new components; reference the variables.

## Running locally

The app needs an HTTP origin (the File System Access API and PDF.js worker
are unhappy on `file://`):

```bash
python -m http.server 8765
# then visit http://localhost:8765
```

Settings (API base URL, model, key) are stored in `localStorage`; clear them
through the browser devtools if you need a clean run.

## Pull requests

- Keep changes focused. A PR that touches three sections of `index.html`
  is fine; a PR that reflows the whole file is not.
- Run `python find-section.py --update-toc` before committing if you added
  or renamed a section marker.
- For UI changes, attach a screenshot or short screen recording.
- For changes that affect API request shape (new prompt fields, different
  streaming format), include a short note in the PR description about which
  endpoints you tested against.

## Issues

When reporting a bug, please include:

- Browser and version.
- LLM endpoint and model (e.g. `api.deepseek.com/v1` + `deepseek-chat`).
- Whether the failure is reproducible with a small public PDF (link
  preferred over attaching a private paper).
- Any error text from the in-app error banner and from the browser console.

## Scope

In scope: PDF parsing improvements, dialogue/prompt quality, accessibility,
new languages, additional figure-handling modes, Q&A UX.

Out of scope (without prior discussion): a build system, framework
migration, server-side components, vendoring proprietary models or keys.
