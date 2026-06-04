# Migrating mytarotpulse.com to the Unified Brand

**Good news up front:** mytarotpulse.com is already built in **GoHighLevel** (it's served off LeadConnector). Same platform as the funnel — so this is a *restyle inside the tool you already use*, not a rebuild or a migration to anywhere. The brand CSS from this kit drops straight in.

---

## 0. Before you touch anything
- **Duplicate the site/funnel first** and work on the copy. Keep the live site up until the new one is QA'd.
- Have this kit open in another tab — the colors, the fonts, and the homepage comp (`site-refresh.html`).

## 1. Global brand settings — do this once
In the site builder → **Settings → Custom CSS** (or the page Head/Custom Code), paste:

```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Space+Mono:wght@400;700&display=swap');

h1,h2,h3,.headline{font-family:'Cinzel',serif !important;color:#E2CF98;}
body,p,li{font-family:'Cormorant Garamond',serif !important;font-size:20px;color:#ECE7D8;}
.eyebrow,.label,button,.cta,nav a{font-family:'Space Mono',monospace !important;letter-spacing:1px;}
body,.page,section{background:#16204A;}
a,button,.cta{background:#C8A44D;color:#1A1530;}
```

Brand colors to register in the builder's color picker:
- Background: **#16204A** (navy) / **#0F1330** (deep sections)
- Primary / buttons: **#C8A44D** (antique gold)
- Headings on dark: **#E2CF98** (soft gold)
- Body text: **#ECE7D8** (ivory)
- Accent, sparingly: **#B9A3E3** (lavender)

## 2. The swaps (current → target)

| Element | Current live site | Change to |
|---|---|---|
| Page background | white | **navy #16204A** |
| CTA button | bright yellow `#F0D878` | **antique gold #C8A44D** |
| Body / nav text | slate `#4C566A` | ivory `#ECE7D8` |
| Heading font | Cinzel **Decorative** | **Cinzel** (cleaner) |
| Body fonts (3, mixed) | Open Sans / Montserrat / Lato | **Cormorant Garamond** (body) + **Space Mono** (labels) |
| Feature icons | pastel watercolor | **gold line-art** (see comp) |
| Hero | purple photo + broken video | **navy + cover/gold-frame + pulse-waveform** |

## 3. Fix the broken hero video (do this regardless of rebrand)
The live hero has a YouTube embed that isn't loading — it currently shows a **large black box**. Either re-embed a working video, or replace that slot with the **cover image in a gold frame** (as in the comp). Don't ship the black box.

## 4. Page-by-page
1. **Nav** — gold pulse-mark + gold "TAROTPULSE" wordmark; links in Space Mono; the CTA button gold.
2. **Hero** — navy ground; Cinzel gold headline; Cormorant subhead; gold "Start Your Journey" button; cover/video in a thin gold frame. Optional: the founder's-data stat line ("2.5 years · 1,167 pulls · …") — this is the real positioning from the sales-page work.
3. **Feature trio** (*Arcana Insights / Healing Analytics / Sacred Data*) — navy cards with **gold line-icons**, Cinzel titles, Space Mono numbers. Swap out the pastel watercolor images. Copy stays; it's already on-message.
4. **Dividers** — drop a **gold pulse-waveform** between sections (one per break — don't over-decorate).
5. **Footer** — pulse-mark + the tagline *"Track your trends. See your patterns. Change your world."*, gold-on-navy.
6. **Blog template** — apply the same global CSS so posts inherit the brand automatically.

## 5. QA checklist
- [ ] No leftover white backgrounds, yellow buttons, or slate text
- [ ] One CTA color (gold), one CTA label, everywhere
- [ ] Gold-on-navy contrast reads; ivory body is legible
- [ ] Hero video works (or is replaced) — no black box
- [ ] Mobile: sections stack, CTA full-width, contrast holds
- [ ] Fonts consolidated to the three — no stray Times/Open Sans/Lato

## Effort
- **Fast pass (~½ day):** global CSS + background/CTA/fonts + fix the video. ~70% uniform immediately; the site stops clashing with the funnel.
- **Full refresh (+~1 day):** hero rebuild, gold feature icons, pulse/filigree motifs.

The homepage comp (`site-refresh.html` in this kit) is the target to build against.
