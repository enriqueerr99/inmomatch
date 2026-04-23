---
name: instagram-carousel
description: >
  Generate Instagram carousels as a fully self-contained, swipeable HTML file
  where every slide is export-ready as an individual 1080x1350px PNG for Instagram.
  Use when the user asks to create an Instagram carousel, carrusel de Instagram,
  design slides for IG, or export carousel images. Workflow: collect brand details →
  generate HTML with IG preview frame → export PNGs via Playwright.
---

# Instagram Carousel Generator

## Step 1: Collect Brand Details

Before generating, ask the user for (if not already provided):

1. **Topic / content** — what the carousel is about
2. **Brand name** — shown on first and last slides
3. **Instagram handle** — shown in IG frame header
4. **Primary brand color** — one hex code (derive full palette from this)
5. **Logo** — SVG path, brand initial, or skip
6. **Font preference** — editorial, modern/clean, warm, technical, bold, classic, rounded (or specific Google Fonts)
7. **Tone** — professional, casual, playful, bold, minimal, etc.
8. **Images** — profile photo, screenshots, product images to embed

If the user provides a website URL, derive colors and style from it.
Do not assume defaults — ask before generating.

## Step 2: Derive Color System & Typography

Read [`references/design-system.md`](references/design-system.md) for:
- The full 6-token color derivation rules (BRAND_PRIMARY → BRAND_LIGHT, BRAND_DARK, LIGHT_BG, LIGHT_BORDER, DARK_BG)
- Font pairing table and size scale
- All reusable components (progress bar, swipe arrow, tag labels, feature lists, etc.)

## Step 3: Generate the HTML Carousel

### File location
Save as: `workspace/carousels/{YYYY-MM-DD}-{slug}/carousel.html`

### Structure
Generate a **single self-contained HTML file** containing:
- Google Fonts `<link>` import for chosen font pair
- CSS classes `.serif` and `.sans`
- Instagram Frame wrapper (`.ig-frame` — must be **exactly 420px wide**)
- `.carousel-track` with all slides side by side (each slide: 420×525px, position:relative)
- Pointer-based swipe/drag interaction JS
- Dot indicators + IG actions (heart, comment, share, bookmark icons)

### Every slide must include:
1. **Progress bar** (bottom, absolute position) — see design-system.md for exact code
2. **Swipe arrow** (right edge) — on every slide EXCEPT the last
3. **Tag label** + **heading** + **body text** adapted to slide type
4. Content padding `0 36px 52px` (bottom clears the progress bar)

### Standard sequence (7 slides, flex 5–10):
| # | Type | Background |
|---|------|------------|
| 1 | Hero | LIGHT_BG — hook + logo lockup |
| 2 | Problem | DARK_BG — pain point |
| 3 | Solution | Brand gradient — the answer |
| 4 | Features | LIGHT_BG — feature list with icons |
| 5 | Details | DARK_BG — differentiators |
| 6 | How-to | LIGHT_BG — numbered steps |
| 7 | CTA | Brand gradient — no arrow, full progress bar |

Adapt sequence to the topic. Not every carousel needs all 7 slides.

### Image embedding
All images must be embedded as base64 in the HTML:
```python
import base64
data = open("image.jpg", "rb").read()
b64 = base64.b64encode(data).decode()
# Use: data:image/jpeg;base64,{b64}
# Check actual format with `file` command — may be JPEG despite .png extension
```

**Always use Python (not shell scripts) to generate the HTML file** — shell variable interpolation corrupts `$` signs and numbers in HTML.

## Step 4: Show Preview & Iterate

Present the HTML file path and ask the user to open it in a browser to swipe through the preview. Iterate on specific slides based on feedback — do not rebuild from scratch.

## Step 5: Export PNG Slides

After the user approves, export each slide as 1080×1350px PNG:

```bash
python .claude/skills/instagram-carousel/scripts/export_slides.py \
  workspace/carousels/{slug}/carousel.html \
  workspace/carousels/{slug}/slides \
  --slides {N}
```

Requirements (if not installed):
```bash
pip install playwright
playwright install chromium
```

### Why it works
- Viewport stays at 420×525px; `device_scale_factor=2.5714` scales output to 1080×1350
- Layout never reflows — fonts, spacing, and positions match the HTML preview exactly
- Never set viewport to 1080×1350 — that would break the layout

### Common export mistakes
| Mistake | Fix |
|---------|-----|
| Viewport set to 1080px | Keep at 420px, use device_scale_factor |
| Shell script generates HTML | Use Python's `Path.write_text()` |
| Fonts render as fallback | `wait_for_timeout(3000)` after page load |
| Export includes IG chrome | Script hides `.ig-header,.ig-dots,.ig-actions,.ig-caption` |

## Design Principles

- First slide must stop the scroll — bold hook, not a description
- Last slide: no arrow (signals end), full progress bar, clear CTA
- Light/dark alternation sustains attention across swipes
- Content padding must never overlap the progress bar
- All images embedded as base64 — HTML is fully self-contained
