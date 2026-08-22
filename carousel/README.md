# Carousel generator

Code-rendered Instagram carousel slides (1080×1350, exported at 2× = 2160×2700).
Zero generation credits — slides are HTML/CSS rendered with headless Chromium,
so text is always pixel-perfect and edits are instant.

Style: warm paper background, Archivo Black condensed headlines, terracotta
(`#DE8B66`) accent, fanned card mockups, `@ollierdz` watermark, slide counter,
SAVE POST button.

## Usage

```bash
./fetch-fonts.sh                      # once per environment (fonts/ is gitignored)
node render.mjs slide-01.html         # renders slide-01.png
node render.mjs slide-*.html          # batch render
```

If Playwright's browser lives in a custom path (e.g. Claude Code web sessions):

```bash
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.mjs slide-01.html
```

If `playwright` isn't installed locally, symlink the global install:

```bash
mkdir -p node_modules && ln -sfn "$(npm root -g)/playwright" node_modules/playwright
```

## Adding slides

Copy `slide-01.html`, keep the `topbar` / `wm` / `save` blocks (brand elements
on every slide), update the counter (`1/10` → `N/10`), and swap the content.
For photoreal elements (faces, product shots), generate a single image via the
Arcads skill and drop it into the layout with an `<img>` — code handles the
typography, AI handles only the photography.
