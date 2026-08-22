# Carousel design craft — pro-tier reference

Distilled from top creator carousels (Grow With Alex; gent.huruglica "Claude
prompts" series). Read this BEFORE designing any feed/carousel/cover graphic.
These are the moves that separate "clean corporate template" from "stop-scroll
editorial." Apply deliberately; do not cargo-cult all twelve onto one slide.

## The self-critique that prompted this
Earlier decks were clean but safe: single display weight, flat vector boxes,
one accent used timidly, no depth, no photoreal hero, no font pairing. The
references win on exactly those axes. Fixes are below.

---

## 1. Type contrast is the design
- **Pair two voices**, never one: an elegant *italic serif / script* (Instrument
  Serif italic, a brush script) against a *heavy grotesque* (Anton, Archivo
  Black, Poppins/Montserrat 800). Example: script "visual" over massive
  "Identity". The contrast IS the sophistication.
- **Color-segment the headline**: key words in the accent, the rest ink. The
  accent words, read alone, must still tell the story. ("These **6 Claude AI
  prompts** will instantly level up your **graphic design work**.")
- **Brutal scale jumps** in one lockup: tiny tracked kicker (letter-spacing
  .12–.2em, 24–30px) → monster display (120–200px) → mid subhead (36–52px).
- **Negative leading** on multi-line display: `line-height: .88–.95`. Lines
  should almost touch.
- Fonts on disk for this: `Anton`, `ArchivoBlack`, `InstrumentSerif-Italic`,
  `BigShoulders-Bold`, `Boldonse`, `Poppins`, `Sora`, `Lora`, `IBMPlexMono`.

## 2. One accent, temperature-matched to the imagery
- Pick **one** accent and match it to the photo's light (warm amber studio →
  orange accent). Cohesion reads as "expensive."
- Accent appears in exactly three roles: (a) one headline word, (b) bolded
  keywords inside the subhead, (c) a backing/graphic shape. Nowhere else.
- Everything non-accent is ink/paper/gray. Restraint > rainbow.

## 3. Cutout → backing shape → contact shadow (depth recipe)
- Background-remove the hero subject. Never place it bare.
- Put a **colored shape behind it**: radiating rays/spikes, a starburst, a
  blurred glow, or a solid blob in the accent. This is what makes it pop.
- Add a **soft contact shadow** under/behind (`filter: drop-shadow(0 40px 60px
  rgba(0,0,0,.45))`). Subject must feel seated, not pasted.
- Cutout tooling: `rembg`/remove.bg, or the Arcads image endpoints (Nano
  Banana) for generate+matte; PIL luminance/chroma key for simple cases.

## 4. Giant kinetic background typography
- Set one huge word (150–360px) in low-contrast gray behind the subject, and let
  the **subject overlap and occlude it** (word behind, person in front). Adds
  scale + depth without fighting the headline. See "GIVEAWAY!".

## 5. Floating mockup cards with real 3D
- Show the actual content as **rounded, white-stroked, drop-shadowed cards**,
  **rotated** a few degrees or arranged in **isometric perspective** (a phone +
  a receding row of cards). `transform: perspective(1200px) rotateY(-18deg)
  rotateX(6deg)`, staggered translateZ. This is "content about content" proof
  and gives dimensionality flat boxes lack.
- Big faded numerals (#1 #2 #3) label cards at ~140px, 10–15% opacity.

## 6. Organic + directional cues
- Hand-drawn white **squiggle/arrow doodles**, chunky solid arrows pointing to
  the payload, brand asterisks/starbursts. They route the eye and humanize the
  grid. One or two per slide, not more.

## 7. Photoreal hero, hard color grade
- Heroes should be **photoreal** (texture, reflection, dramatic light), not flat
  illustration. Generate via Arcads image models when no photo exists.
- Grade the whole frame to one palette: vignette the edges, add an accent
  **edge glow** (bottom bar of accent gradient), unify temperature.

## 8. Persistent engagement UI (consistent placement every slide)
- `@handle` top-left; page counter (`2/10`) top-right in a gray pill.
- "SAVE POST!" / bookmark tag or a comment-keyword CTA on the last slide.
- Keep these in identical positions across the set — they frame the brand.

---

## Eye-path rules (hierarchy)
1. Biggest element = the accent headline word (attention magnet #1).
2. Face/eyes of the hero (magnet #2) — position on a third, gaze pointing inward.
3. Subhead / mockups (magnet #3).
4. Handle + counter + CTA (frame, read last).
- Compose on a **Z** (cover/CTA) or **F** (text-heavy) path. Left-align dense
  text. Headline should own 40–55% of the frame.

## Pre-flight checklist (score each slide)
- [ ] Two type voices present (script/serif + heavy grotesque)?
- [ ] Headline color-segmented; accent words tell the story alone?
- [ ] Scale jumps dramatic (kicker vs display ≥ 4×)?
- [ ] Exactly one accent, matched to image temperature?
- [ ] Hero cut out WITH backing shape + contact shadow?
- [ ] Any large kinetic bg type or depth layer?
- [ ] At least one organic/directional cue, not more than two?
- [ ] Handle + counter + CTA in consistent positions?
- [ ] Clear 1-2-3 eye path; headline owns 40–55%?

## When NOT to use
- Data/diagram decks (see `canvas-philosophy.md`) stay clinical and flat.
- Ultra-minimal brand covers can skip cutouts/kinetic type — but still pair
  fonts and segment color.
