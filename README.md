# ReadPaper2U

**English** · [简体中文](./README.zh-CN.md) · [한국어](./README.ko.md)

> Chat with your academic paper as a visual-novel companion.

ReadPaper2U is a single-file web application that turns a PDF research paper
into a conversational reading experience. A customizable companion character
walks you through the paper as a visual-novel-style script, after which you
can ask follow-up questions in a Q&A panel. Equations, figures, and tables
are rendered or summarized inline; conversation state is saved locally.

The whole application lives in one `index.html` (no build step, no server
required beyond a static file host).

---

## Features

- **PDF parsing in the browser** — paper is parsed client-side via PDF.js;
  arXiv links are also accepted.
- **Visual-novel mode** — paper content is rewritten as a turn-by-turn
  dialogue read by a customizable companion character.
- **Q&A mode** — after the visual-novel pass finishes, ask the model
  follow-up questions about the paper.
- **Mind map** — generate an argument-structure mind map from the
  dialogue script with one click, with SVG and PNG export for
  embedding the diagram in notes or slides.
- **Figure/table handling** — four modes: off, caption-only, vision-model
  description, or inline embedding of figure descriptions in the dialogue.
- **Math rendering** — LaTeX rendered with KaTeX.
- **Multilingual** — interface and dialogue available in Simplified
  Chinese, Traditional Chinese, English, and Korean.
- **Light and dark themes** — switch from Settings; both themes share the
  same CSS variable system.
- **Keyboard shortcuts** — Next/Previous, auto-play, dialogue log, and a
  help overlay; the full mapping is visible by pressing `?`.
- **Emotion-specific character animations** — companion sprite reacts to
  dialogue beats with subtle motion cues.
- **Persistent saves** — conversations stored in IndexedDB; optional
  export to a local folder via the File System Access API.
- **Blackboard panel** — sidebar tracking key terms, formulas, and the
  paper's running argument.
- **Bring-your-own LLM** — any OpenAI-compatible chat completion endpoint
  (DeepSeek, OpenAI, Moonshot/Kimi, and similar). API key is stored only in
  your browser's `localStorage` and is sent directly to your configured
  endpoint.

---

## Inspiration and differences from Paper2Gal

ReadPaper2U is a partial reimplementation inspired by
[Paper2Gal](https://paper2gal.com/), a web-based application that turns
papers into Galgame-style visual novels. The two projects share the same
core idea of reading a paper through a companion character. ReadPaper2U
leans more functional and is not anchored in ACG aesthetics, with three
concrete differences in design:

- **Open and self-hosted.** ReadPaper2U ships as a single static HTML file
  under the MIT License. There is no service to sign in to, no usage cap,
  and no proxy between the browser and the LLM. The file talks directly to
  whichever OpenAI-compatible endpoint you supply.
- **A wider lens on the "companion" character.** The character editor
  exposes 12 dimensions (species, appearance, energy level, formality,
  humor style, signature phrase, expertise, and four per-section pacing
  strategies). The default avatar is a photo of the author's own cat.
  Anime-style characters work fine, and so do mentors, colleagues,
  fictional researchers, or pets. The app is not bound to any one
  aesthetic tradition.
- **Figure-aware reading.** When a vision-capable model is configured, the
  app can either describe each figure once and inject the descriptions
  into the dialogue, or feed the figure image directly into the
  script-generation call. Caption-only and figure-off modes remain
  available for text-only models or for cost control.

What ReadPaper2U does not currently include: background music, voice
synthesis, or built-in character art commissioning. The visual novel runs
on text and a static avatar.

---

## Quick start

The app is one HTML file. The simplest path is to open it through a local
static server (the File System Access API and PDF.js worker both prefer
`http://` over `file://`):

```bash
# Python 3 (any platform)
python -m http.server 8765
# then visit http://localhost:8765
```

On first run, click the **Settings** button on the home screen and fill
in:

1. **API base URL** — e.g. `https://api.deepseek.com/v1`,
   `https://api.openai.com/v1`, or any other OpenAI-compatible endpoint.
2. **Model name** — e.g. `deepseek-chat`, `gpt-4o-mini`, etc.
3. **API key** — stored only in `localStorage` on this device.

Then drop a PDF onto the upload card or paste an arXiv link. Once a
session is in progress, the gear icon in the top-right opens the same
settings panel.

### Offline / air-gapped use

By default PDF.js and KaTeX are loaded from public CDNs
(`cdnjs.cloudflare.com`, `cdn.jsdelivr.net`). The app falls back to a
local `lib/` folder if the CDNs are unreachable. To use it offline, place
the following files next to `index.html`:

```
lib/
├── pdf.min.js
├── pdf.worker.min.js
└── katex/
    ├── katex.min.js
    ├── katex.min.css
    └── fonts/...
```

Files are available from the official PDF.js and KaTeX releases listed in
[THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

---

## Privacy

The app runs entirely in the browser. Specifically:

- The PDF is parsed locally; the parsed text is then sent to the LLM
  endpoint **you configure** as part of the chat completion request.
- The API key never leaves your browser except in the `Authorization`
  header of requests to your configured endpoint.
- Saves are stored in your browser's IndexedDB (and optionally exported
  to a folder you choose).

When uploading **unpublished** manuscripts, review your LLM provider's
data-retention and training-use policies before proceeding.

---

## Project layout

```
readpaper2u/
├── index.html              # the entire application
├── banni.png               # default companion-character avatar
├── find-section.py         # navigate the inline section markers
├── process_avatar.py       # one-off: HEIC photo → background-removed PNG
├── LICENSE
├── README.md               # English (this file)
├── README.zh-CN.md         # Simplified Chinese
├── README.ko.md            # Korean
├── CONTRIBUTING.md
├── THIRD_PARTY_NOTICES.md
├── requirements.txt        # deps for process_avatar.py only
└── .gitignore
```

`index.html` is intentionally a single file. See
[CONTRIBUTING.md](./CONTRIBUTING.md) for an explanation of the section-marker
system used to navigate it and the helper script that maintains its
table of contents.

---

## Helper scripts

### `find-section.py`

Lists, filters, and regenerates the table-of-contents block embedded near the
top of `index.html`. Standard library only; no installation needed.

```bash
python find-section.py                # list every section in CSS and JS
python find-section.py --name api     # filter by substring
python find-section.py --update-toc   # rewrite the TOC block in-place
```

### `process_avatar.py`

A one-shot utility that turns a HEIC photograph into a background-removed,
cropped, alpha-channel PNG suitable for use as a companion avatar. Required
only if you want to generate a new avatar; the included `banni.png` works
out of the box.

```bash
pip install -r requirements.txt
# Edit the SRC and DST constants at the top of process_avatar.py, then:
python process_avatar.py
```

---

## License

This project is released under the MIT License. See [LICENSE](./LICENSE).

The default companion avatar `banni.png` is an original photograph of the
author's cat, also released under the MIT license. Third-party libraries
loaded at runtime (PDF.js, KaTeX) carry their own licenses; see
[THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

---

## Acknowledgments

Built on top of [PDF.js](https://mozilla.github.io/pdf.js/) (Apache 2.0) and
[KaTeX](https://katex.org/) (MIT). LLM inference is delegated to whichever
OpenAI-compatible endpoint you supply. Banni, the default companion, is a
real cat.
