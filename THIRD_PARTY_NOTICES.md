# Third-Party Notices

ReadPaper2U is licensed under the MIT License (see [LICENSE](./LICENSE)).
At runtime it loads two third-party JavaScript libraries from public CDNs,
each carrying its own license. Their notices are reproduced below.

The avatar image `banni.png` is an original photograph of the author's cat,
released under the same MIT license as the rest of this repository.

The Python helper script `process_avatar.py` is run only when generating a
new avatar; it depends on Pillow, pillow-heif, and rembg, none of which are
distributed inside this repository. They are installed separately via
`pip install -r requirements.txt` and remain governed by their own
licenses (HPND, Apache 2.0, and MIT respectively).

---

## PDF.js

- **Project:** Mozilla PDF.js — <https://mozilla.github.io/pdf.js/>
- **Version pinned by this app:** 3.11.174
- **Loaded from:** `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js`
- **Worker loaded from:** `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js`
- **License:** Apache License 2.0

For offline use, place the corresponding minified files at:

```
lib/pdf.min.js
lib/pdf.worker.min.js
```

The Apache 2.0 license text is available at
<https://www.apache.org/licenses/LICENSE-2.0>.

---

## KaTeX

- **Project:** KaTeX — <https://katex.org/>
- **Version pinned by this app:** 0.16.11
- **CSS loaded from:** `https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css`
- **JS loaded from:** `https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js`
- **License:** MIT License

For offline use, place the corresponding files at:

```
lib/katex/katex.min.js
lib/katex/katex.min.css
lib/katex/fonts/...
```

The full KaTeX MIT license is available at
<https://github.com/KaTeX/KaTeX/blob/main/LICENSE>.

---

## Avatar image (`banni.png`)

- **Source:** Original photograph by the project author (chpebo) of their
  own cat, processed via `process_avatar.py` (HEIC → background-removed
  PNG).
- **License:** MIT, identical to the rest of this repository.
- **Replacement:** Forks may freely substitute their own image; the only
  requirement is that the file at `./banni.png` (or whatever path is set
  in the character configuration) be a valid PNG with transparency.
