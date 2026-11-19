# Pendium — Product Context

## Product Purpose

Pendium is an AI-powered product studio. It designs, builds and ships its own products. The products cover very different kinds of work: a professional credential, a developer tool and a game.

The site at pendium.co has two jobs:

1. Show that one studio makes all of these products.
2. Send each visitor to the product that fits them.

The site is not a services pitch. It does not sell design or engineering work to clients.

## Register

brand

## Users

- **Primary:** people who might use one of the products. A professional who wants to prove their AI skills. A developer who wants an AI agent to make phone calls. A player who likes building and management games.
- **Secondary:** people curious about the studio itself, such as press, partners and future collaborators.
- **Decision context:** the visitor decides in a few seconds which product is for them. Each card must say what the product is and who it is for in one sentence.

## Products

| No. | Product | Category | What it is | Link |
|---|---|---|---|---|
| 001 | Emeri | Education | The professional standard for AI proficiency. A free 15-minute check grades how you work with AI. Certify the result and it becomes a verifiable credential. | emeri.org |
| 002 | Hollerback | Developer tool | Lets an AI agent call and text people. The agent sends a goal and facts. Hollerback makes the call, follows up after voicemail and returns one structured result. | hollerback.dev |
| 003 | Lofty Ambitions | Game | A pixel-art tower game. The player adds floors, rooms and elevators, fills the tower with tenants and keeps everyone moving. In development. | pendium.co/lofty-ambitions/ |

## Brand & Tone

- Plain and direct. State what a product does and who it is for.
- Confident without hype.
- Dry wit is welcome. Overt jokes are not.
- Never reveal or hint at team size.

## Visual System

- The homepage uses Pendium's own look: dark neutral background, Outfit and IBM Plex Mono, and the ASCII pendulum.
- Each product gets one large image-led tile, always in its own palette and type: the game's cover art in Pixelify Sans, the Hollerback macaw with a call transcript in Bricolage Grotesque, and an Emeri credential in navy and gold. The whole tile is one link.
- A product's own page uses that product's look, not Pendium's. The Lofty Ambitions page is the game's tower: real room sprites, the game's room music, and an elevator panel for navigation. `scripts/build-lofty-sprites.py` cuts the sprites from the game repo.

## Anti-references

- AI hype: "revolutionary", "transform", "cutting-edge".
- Generic agency language: "full-service", "end-to-end solutions", "we partner with brands".
- Founder-forward or "I" language.
- One visual style forced onto every product.
- Feature-list vendor marketing.

## Lofty Ambitions page rules

- No release date, price, platform or review claims until they are confirmed.
- Never name the source repo ("yoot-tower") or other tower games.
- The main call to action is the launch email sign-up (Buttondown).
