# Studio homepage and Lofty Ambitions page

Date: 2026-11-18. Size: a small project. Two static pages.

## Intent

Pendium makes very different products with AI: a credential, a developer tool and a game. The homepage should present Pendium as one AI-powered studio that makes all kinds of products. It should send visitors to each product. A new page should promote the game Lofty Ambitions and collect emails for launch news.

The audience is people who might use the products. The homepage is not a sales pitch to companies that want to hire Pendium.

## Goals

- The homepage shows three products: Emeri, Hollerback and Lofty Ambitions.
- The homepage headline and lede state the studio pitch in plain words.
- `pendium.co/lofty-ambitions/` sells the game with real footage and collects emails.

## Non-goals

- No client-services section, prices or "hire us" call to action.
- No build step, framework or package manager.
- No release date, price, platform or review claims for the game. None have been supplied.

## Anti-goals

- AI hype words: "revolutionary", "transform", "cutting-edge".
- A game page that looks like a developer tool.
- Any mention of the repo name "yoot-tower" or of other tower games.
- A page that ships 40 MB of video to a phone.

## Constraints

- GitHub Pages serves the repo root as static files. The `CNAME` is `pendium.co`.
- GitHub Pages cannot receive form posts. The email form needs an outside service.
- Fonts load from Google Fonts only.

## Approaches

| | Approach | Trade-off |
|---|---|---|
| **A (picked)** | Each product keeps its own look. The homepage stays Pendium's dark mono design. Each card shows its product's colours on hover. The game page uses the game's own pixel-art look. | Two visual styles to maintain. Shows range, which is the point of the homepage. |
| B | One Pendium look on both pages. | One style to maintain. The game page sells the game poorly and undercuts the "all kinds of products" message. |

Rejected before the choice: a static-site generator for shared header and footer. Two pages do not need one.

## Homepage (`/index.html`)

- Keep the header, the ASCII pendulum, the footer and the colour tokens.
- Rewrite the `<title>`, meta description, H1 and lede for the studio pitch. Draft: H1 "One studio. Every kind of product." Lede: Pendium is an AI-powered product studio. It designs, builds and ships its own products. Today those are a credential, a developer tool and a game.
- Replace the single Emeri card with three cards in a list, numbered NO. 001 to 003. Each card has a category label, the product name or logo, one sentence, and a link out.
  - Emeri (Education): keeps today's copy, logo and navy-and-gold hover. Links to emeri.org.
  - Hollerback (Developer tool): "Let your AI agent call and text people. No phone stack to build." Hover palette: jungle `#111b17` background, peach `#f7dcc4` text, macaw `#d65f51` button. Links to hollerback.dev.
  - Lofty Ambitions (Game): one sentence about building a tower and filling it with tenants. Hover palette: night sky from the cover art, parchment `#f3e8cf` text, gold `#e0b35a` button. Shows a small cover image. Links to `/lofty-ambitions/`.
- On touch screens, each card shows its product palette at all times. Today's Emeri card already does this.
- The footer line "not affiliated with any AI vendor" stays.

## Lofty Ambitions page (`/lofty-ambitions/index.html`)

Look: the game's palette from `Sources/TowerInterface/Palette.swift`. Ink `#2b2433`, parchment `#f3e8cf` and `#e9dcc0`, gold `#e0b35a`, teal accent `#1e7a8c`. Pixelify Sans for headings, from Google Fonts. Square corners, 2px ink outlines and hard shadows, as in the game's interface.

Sections, top to bottom:

1. Header: game logo or title, and a small "A Pendium game" link back to `/`.
2. Hero: cover art, the line "A whole city. One tower.", and the email form.
3. Trailer: the 32-second gameplay trailer, with a poster image. It loads only when played.
4. What you do: three short blocks, each with a GIF loop. Build it up (construction). Little lives (room activity). Pleasant chaos (fire response).
5. Screenshots: 01, 03, 06, 07 and 08 in a grid. Each opens full size.
6. Second email form, then the footer.

Email form: an HTML form that posts to Buttondown's embed endpoint. The Buttondown username is one value at the top of the file. Chris creates the Buttondown account. Until then the form shows a placeholder value. The form has a visible label, and it works without JavaScript.

## Assets

Copied from `~/Projects/yoot-tower/Marketing/Steam` into `lofty-ambitions/assets/`, then compressed:

- Trailer: re-encode to 1280×720 H.264 with fast start, target 6–8 MB. Keep the soundtrack.
- Screenshots and cover art: WebP. Pixel art stays sharp with `image-rendering: pixelated` where shown at whole-number scale.
- GIF loops: convert to muted, looping MP4. Each should be under 1 MB.
- Social share image: the 1232×706 main capsule.

## Also

- Rewrite `PRODUCT.md`. It describes an enterprise design agency, which no longer matches the site.
- Both pages get Open Graph tags and a description.

## Left to the builder

- Final copy wording within the drafts above.
- Exact grid sizes, spacing and breakpoints.
- Which still serves as the trailer poster.
