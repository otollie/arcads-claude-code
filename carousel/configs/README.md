# Carousel Creator — operating rules

This folder holds one config per business. Adding a business = adding a config file,
never a rebuild. Read the relevant config before any build.

## Configs
- `personal-tiktok.md` — Ollie personal brand (TikTok/LinkedIn), active
- `iavrs.md` — IAVRS immigration attorney matching (brand guide on file)
- Uplift (marketing) and Visible Intelligence (AI) — not created yet; ask for brand
  details the first time a carousel is requested for them.

## Build flow (do not skip steps)
1. Ollie picks a business + category.
2. Offer 3 subject options, one line each on why it's valuable (valuable = defines or
   shows how to use a tool or feature).
3. Ollie picks one.
4. If category is Drop: web-search first to verify the feature exists and what it does.
   Never invent specs. Can't confirm = say so.
5. BEFORE drafting copy, read the vendored skills:
   - `skills/viral-tiktok-hooks/SKILL.md` (Apache-2.0, gonzalochale/skills) — PRIMARY for
     TikTok decks. Use its Hook Engine (6 angles x shapes), Format Library (A-H), 15-25
     words per slide cap, 3-line slide structure, anti-repetition rule (never same format
     twice in a row; log format+angle used in the deck's content notes).
   - Then the marketingskills set (MIT, coreyhaines31/marketingskills):
   - `skills/social/references/post-templates.md` — hook formulas (curiosity, story,
     value, contrarian, social proof) + carousel structure. Draft 3+ hooks from these
     formulas, pick the strongest.
   - `skills/copywriting/SKILL.md` — principles: clarity over cleverness, benefits over
     features, specificity over vagueness, customer language, one idea per section.
   - `skills/marketing-psychology/SKILL.md` — pick 1-2 levers (curiosity gap, loss
     aversion, social proof) and build the deck arc around them.
   Assume the audience knows nothing: no insider names/tiers without a plain-English
   gloss. Every "what it does" claim must answer "so what, don't all AIs do that?"
6. Show full slide copy as PLAIN TEXT and wait for approval. Never render first.
7. Run a `skills/copy-editing` pass on approved copy before building slides.
8. BEFORE designing/rendering, read `carousel/design-craft.md` (pro-tier craft:
   type pairing, color-segmented headlines, cutout+backing+shadow depth, kinetic
   bg type, 3D mockups, eye-path). Score the slides against its pre-flight
   checklist. `canvas-philosophy.md` still governs clinical/diagram decks.
9. After approval: render, deliver PNGs, then caption + CTA. No hashtags.

## Categories (fixed skeletons; more may be added)
- **Breakdown** — defines a tool/feature, what it does, how to use it.
  Skeleton: cover (hook) → what it is → what it does → how to use it → CTA.
- **Drop** — breaking-news style for a newly shipped feature: what launched, what it does.
  Skeleton: cover (news flash) → what launched → what it does → why it matters → CTA.

## Design rules (matter most)
- One shared themeable base stylesheet; business config drives colors/fonts/branding.
  Do NOT create a new standalone stylesheet per deck.
- Design first, copy second. Each slide is a visual with a few words, not a paragraph
  with a background. One idea per slide: short headline + max 1–2 support lines. Needs
  more = split the slide.
- Character caps per element so text never clips.
- Product decks: fetch the product's OFFICIAL logo (brand/press kit), crop/cut out the
  background, place the real file. Never redraw or AI-generate a logo. No usable file =
  say so and use a clean text treatment. Echo the product's real colors/type inside;
  Ollie's business stays the outer wrapper.
- Crop and blend images into layouts, no hard pasted rectangles. Consistent margins.
  Clear hierarchy, headline first. Max two font families per slide.
- Read design skills (frontend-design / canvas-design / artifact-design) before building.

## Output
- Final slides: PNG. Size: current TikTok carousel dimensions — verify via web search
  about monthly (don't trust a saved number). **Last verified 2026-07-03: 1080×1920
  (9:16 vertical), native full-screen.** Next re-check ~2026-08. Ollie can override.
- TikTok safe zones (keep headlines/faces/key content centered, away from UI overlays):
  top ~100px = Following/For You tabs; bottom ~300px = caption, handle, sound;
  right ~150px = like/comment/share/bookmark. Design a centered safe column with
  generous top/bottom margins so nothing important sits under the chrome.
- Render pipeline: HTML/CSS per slide → `node render.mjs <files>` (Playwright,
  PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers) → PNG at 2× scale.
- After approval, deliver caption + CTA. No hashtags, no em dashes, no AI jargon.
