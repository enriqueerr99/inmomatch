# Instagram Carousel Design System

## Table of Contents
1. [Color System](#color-system)
2. [Typography](#typography)
3. [Slide Architecture](#slide-architecture)
4. [Required UI Elements](#required-ui-elements)
5. [Content Patterns & Components](#content-patterns--components)
6. [Standard Slide Sequence](#standard-slide-sequence)
7. [Instagram Frame (Preview)](#instagram-frame-preview)
8. [Layout Best Practices](#layout-best-practices)

---

## Color System

Derive 6 tokens from the user's single primary brand color:

```
BRAND_PRIMARY   = {user's color}              // Accent — progress bar, icons, tags
BRAND_LIGHT     = {primary lightened ~20%}    // Tags on dark slides, pills
BRAND_DARK      = {primary darkened ~30%}     // CTA text, gradient anchor
LIGHT_BG        = {warm/cool off-white}       // Light slide background (never pure #fff)
LIGHT_BORDER    = {slightly darker LIGHT_BG}  // Dividers on light slides
DARK_BG         = {near-black with brand tint}// Dark slide background
```

**Derivation rules:**
- LIGHT_BG: tinted off-white complementing primary (warm primary → cream, cool → gray-white)
- DARK_BG: near-black with subtle brand tint (warm → #1A1918, cool → #0F172A)
- LIGHT_BORDER: ~1 shade darker than LIGHT_BG
- Brand gradient: `linear-gradient(165deg, BRAND_DARK 0%, BRAND_PRIMARY 50%, BRAND_LIGHT 100%)`

---

## Typography

Pick heading + body font pair from Google Fonts based on user tone:

| Style | Heading | Body |
|-------|---------|------|
| Editorial / premium | Playfair Display | DM Sans |
| Modern / clean | Plus Jakarta Sans 700 | Plus Jakarta Sans 400 |
| Warm / approachable | Lora | Nunito Sans |
| Technical / sharp | Space Grotesk | Space Grotesk |
| Bold / expressive | Fraunces | Outfit |
| Classic / trustworthy | Libre Baskerville | Work Sans |
| Rounded / friendly | Bricolage Grotesque | Bricolage Grotesque |

**Font size scale (fixed across all brands):**
- Headings: 28–34px, weight 600, letter-spacing -0.3 to -0.5px, line-height 1.1–1.15
- Body: 14px, weight 400, line-height 1.5–1.55
- Tags/labels: 10px, weight 600, letter-spacing 2px, UPPERCASE
- Step numbers: heading font, 26px, weight 300
- Small text: 11–12px

Apply via CSS classes `.serif` (heading) and `.sans` (body).

---

## Slide Architecture

- **Aspect ratio:** 4:5 (Instagram carousel standard) — 420×525px in HTML
- **Export size:** 1080×1350px PNG (via `device_scale_factor=1080/420`)
- Each slide is fully self-contained — all UI baked into the image
- Alternate LIGHT_BG and DARK_BG backgrounds for visual rhythm

---

## Required UI Elements

### Progress Bar (every slide, bottom)

```javascript
function progressBar(index, total, isLightSlide) {
  const pct = ((index + 1) / total) * 100;
  const trackColor = isLightSlide ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.12)';
  const fillColor = isLightSlide ? BRAND_PRIMARY : '#fff';
  const labelColor = isLightSlide ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.4)';
  return `<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 28px 20px;z-index:10;display:flex;align-items:center;gap:10px;">
    <div style="flex:1;height:3px;background:${trackColor};border-radius:2px;overflow:hidden;">
      <div style="height:100%;width:${pct}%;background:${fillColor};border-radius:2px;"></div>
    </div>
    <span style="font-size:11px;color:${labelColor};font-weight:500;">${index + 1}/${total}</span>
  </div>`;
}
```

### Swipe Arrow (every slide EXCEPT the last)

```javascript
function swipeArrow(isLightSlide) {
  const bg = isLightSlide ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.08)';
  const stroke = isLightSlide ? 'rgba(0,0,0,0.25)' : 'rgba(255,255,255,0.35)';
  return `<div style="position:absolute;right:0;top:0;bottom:0;width:48px;z-index:9;display:flex;align-items:center;justify-content:center;background:linear-gradient(to right,transparent,${bg});">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <path d="M9 6l6 6-6 6" stroke="${stroke}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>`;
}
```

**Last slide:** remove arrow entirely (signals end of carousel).

---

## Content Patterns & Components

### Layout rules
- Content padding: `0 36px` standard
- Bottom-aligned + progress bar: `0 36px 52px` to clear the bar
- Hero/CTA slides: `justify-content: center`
- Content-heavy slides: `justify-content: flex-end` (text at bottom)

### Tag / Category Label
```html
<!-- Light slide -->
<span class="sans" style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_PRIMARY};margin-bottom:16px;">TAG TEXT</span>
<!-- Dark slide -->
<span class="sans" style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_LIGHT};margin-bottom:16px;">TAG TEXT</span>
<!-- Gradient slide -->
<span class="sans" style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:rgba(255,255,255,0.6);margin-bottom:16px;">TAG TEXT</span>
```

### Logo Lockup (first and last slides)
- 40px circle (BRAND_PRIMARY bg) + brand initial or icon in white
- Brand name: 13px, weight 600, letter-spacing 0.5px

### Strikethrough pills (problem slides)
```html
<span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);border-radius:20px;color:#6B6560;text-decoration:line-through;">Old tool</span>
```

### Tag pills
```html
<span style="font-size:11px;padding:5px 12px;background:rgba(255,255,255,0.06);border-radius:20px;color:{BRAND_LIGHT};">Label</span>
```

### Prompt / quote box
```html
<div style="padding:16px;background:rgba(0,0,0,0.15);border-radius:12px;border:1px solid rgba(255,255,255,0.08);">
  <p class="sans" style="font-size:13px;color:rgba(255,255,255,0.5);margin-bottom:6px;">Label</p>
  <p class="serif" style="font-size:15px;color:#fff;font-style:italic;line-height:1.4;">"Quote text"</p>
</div>
```

### Feature list row
```html
<div style="display:flex;align-items:flex-start;gap:14px;padding:10px 0;border-bottom:1px solid {LIGHT_BORDER};">
  <span style="color:{BRAND_PRIMARY};font-size:15px;width:18px;text-align:center;">✦</span>
  <div>
    <span class="sans" style="font-size:14px;font-weight:600;color:{DARK_BG};">Label</span>
    <span class="sans" style="font-size:12px;color:#8A8580;"> — Description</span>
  </div>
</div>
```

### Numbered step row
```html
<div style="display:flex;align-items:flex-start;gap:16px;padding:14px 0;border-bottom:1px solid {LIGHT_BORDER};">
  <span class="serif" style="font-size:26px;font-weight:300;color:{BRAND_PRIMARY};min-width:34px;line-height:1;">01</span>
  <div>
    <span class="sans" style="font-size:14px;font-weight:600;color:{DARK_BG};">Step title</span>
    <span class="sans" style="font-size:12px;color:#8A8580;"> — Step description</span>
  </div>
</div>
```

### CTA button (final slide only)
```html
<div style="display:inline-flex;align-items:center;gap:8px;padding:12px 28px;background:{LIGHT_BG};color:{BRAND_DARK};font-family:'{BODY_FONT}',sans-serif;font-weight:600;font-size:14px;border-radius:28px;">
  CTA text
</div>
```

### Color swatches
```html
<div style="width:32px;height:32px;border-radius:8px;background:{color};border:1px solid rgba(255,255,255,0.08);"></div>
```

---

## Standard Slide Sequence

7 slides is ideal (flex 5–10):

| # | Type | Background | Purpose |
|---|------|------------|---------|
| 1 | Hero | LIGHT_BG | Hook — bold statement, logo lockup |
| 2 | Problem | DARK_BG | Pain point — what's broken |
| 3 | Solution | Brand gradient | The answer — optional quote box |
| 4 | Features | LIGHT_BG | What you get — feature list with icons |
| 5 | Details | DARK_BG | Depth — customization, differentiators |
| 6 | How-to | LIGHT_BG | Steps — numbered workflow |
| 7 | CTA | Brand gradient | Call to action. **No arrow. Full progress bar.** |

Adapt sequence to topic — not every carousel needs a "problem" slide.

---

## Instagram Frame (Preview)

Wrap slides in an IG-style preview frame (420px wide, NOT to be changed):

- **Header:** Avatar (BRAND_PRIMARY circle) + handle + subtitle
- **Viewport:** 420×525px, swipeable/draggable `.carousel-track`
- **Dots:** Small dot indicators below viewport
- **Actions:** Heart, comment, share, bookmark SVG icons
- **Caption:** Handle + short description + timestamp

Include pointer-based swipe/drag interaction. The `.ig-frame` must be **exactly 420px wide** — the export depends on it.

---

## Layout Best Practices

1. Content must never overlap the progress bar → `padding-bottom: 52px` on bottom-aligned content
2. User-uploaded images may be JPEG despite `.png` extension — check with `file` command, use correct MIME type in base64 URI
3. All images must be embedded as base64 (`data:image/jpeg;base64,...`) for self-contained HTML
4. Test every slide visually before export — iterate on specific slides, not full rebuilds
