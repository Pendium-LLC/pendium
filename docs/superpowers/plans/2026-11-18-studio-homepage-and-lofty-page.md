# Studio Homepage and Lofty Ambitions Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition pendium.co as a studio with three products, and add a promo page for Lofty Ambitions.

**Architecture:** Two hand-written static HTML files with inline CSS, served by GitHub Pages. Game assets are compressed with ffmpeg and cwebp into `lofty-ambitions/assets/`. No build step.

**Tech Stack:** HTML, CSS, a little vanilla JS, ffmpeg, cwebp.

**Spec:** `docs/superpowers/specs/2026-11-18-studio-homepage-and-lofty-page-design.md`

## Global Constraints

- No release date, price, platform or review claims for the game.
- Never mention "yoot-tower" or other tower games on a public page.
- Fonts from Google Fonts only. No other third-party scripts.
- Copy follows plain technical English. No hype words.
- The email form works without JavaScript. The Buttondown username is one value at the top of the form markup.
- Total weight of `lofty-ambitions/assets/` stays under 15 MB. The trailer is 6–8 MB.

## Review Focus

- A phone on a slow network opens the game page: the trailer must not download until played (`preload="none"`).
- A visitor with reduced motion: loops do not autoplay, and the pendulum shows one still frame.
- A touch device: each homepage card shows its product palette without hover.
- A 320px-wide screen: no horizontal scroll on either page.
- Keyboard only: every link, the form and the screenshot viewer are reachable with a visible focus ring.

---

### Task 1: Game assets

**Files:**
- Create: `lofty-ambitions/assets/` (trailer.mp4, trailer-poster.webp, cover.webp, cover-card.webp, og.jpg, loop-build.mp4, loop-lives.mp4, loop-chaos.mp4, shot-01/03/06/07/08 .webp, icon.png)

- [ ] **Step 1:** Re-encode `Marketing/Steam/video/Lofty-Ambitions-Gameplay-Trailer-1080p.mp4` to 1280×720 H.264, AAC 128k, `+faststart`.
- [ ] **Step 2:** Convert the three GIF loops to muted MP4 (`yuv420p`, even dimensions). Convert capsules and screenshots to WebP.
- [ ] **Step 3:** Verify: `du -sh lofty-ambitions/assets` under 15 MB, trailer 6–8 MB.
- [ ] **Step 4:** Commit.

### Task 2: Lofty Ambitions page

**Files:**
- Create: `lofty-ambitions/index.html`

- [ ] **Step 1:** Build the sections from the spec: header, hero with form, trailer, three feature blocks, screenshot grid, second form, footer. Palette and type from the spec.
- [ ] **Step 2:** Screenshot viewer: native `<dialog>`; each thumbnail is a link to the full image so it works without JS.
- [ ] **Step 3:** Verify in the browser at 1280px and 375px. Check every Review Focus line that applies to this page.
- [ ] **Step 4:** Commit.

### Task 3: Homepage

**Files:**
- Modify: `index.html`

- [ ] **Step 1:** New title, description, Open Graph tags, H1 and lede.
- [ ] **Step 2:** Generalise `.card` so each product sets its palette through custom properties (`--card-bg`, `--card-fg`, `--card-fg-dim`, `--card-accent`, `--card-accent-fg`, `--card-border`). Add the Hollerback and Lofty Ambitions cards.
- [ ] **Step 3:** Verify hover, touch (`hover: none`) and 375px layouts.
- [ ] **Step 4:** Commit.

### Task 4: PRODUCT.md

- [ ] **Step 1:** Rewrite for the studio pitch: purpose, users, three products, tone, anti-references.
- [ ] **Step 2:** Commit.
