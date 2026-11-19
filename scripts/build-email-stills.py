"""Compose the call stills for the Lofty Ambitions welcome emails.

Run from the repo root:
    python3 scripts/build-email-stills.py ~/Projects/yoot-tower

Each still copies the game's own call layout (Sources/TowerPresentation/CallRendering.swift):
the caller's background fills the frame, the caller stands at 42% across with the bottom edge
cutting the body, and Saru sits on the right edge for Mr. Kanemochi's calls.

Writes 1200x900 JPGs (shown at 600x450 in email) to lofty-ambitions/assets/email/.
"""

import json
import sys
from pathlib import Path

from PIL import Image

GAME = Path(sys.argv[1]).expanduser()
RUNTIME = GAME / "Assets/Tokyo/Runtime"
SHEETS = RUNTIME / "Sheets"
OUT = Path("lofty-ambitions/assets/email")
OUT.mkdir(parents=True, exist_ok=True)

frames = json.loads((RUNTIME / "atlas.json").read_text())["frames"]
_sheets = {}

W, H = 1200, 900
CALLER_SINK = 0.12
SARU_OVERHANG = 0.25
# Saru's height as a share of the frame height, and the share of that height below the bottom edge.
SARU_PLACEMENT = {"peekLow": (0.42, 0.48), "banana": (0.42, 0.3), "thumbsDown": (0.42, 0.0), "smug": (0.42, 0.3)}


def crop(name):
    frame = frames[name]
    path = SHEETS / frame["sheet"]
    if path not in _sheets:
        _sheets[path] = Image.open(path).convert("RGBA")
    x, y, w, h = frame["rect"]
    return _sheets[path].crop((x, y, x + w, y + h))


def still(out, caller, mood, saru=None, background=None):
    canvas = crop(f"call.background.{background or caller}").resize((W, H), Image.LANCZOS)
    art = crop(f"call.{caller}.{mood}.0")
    h = H
    if h * art.width / art.height > W * 0.8:
        h = W * 0.8 * art.height / art.width
    w = h * art.width / art.height
    art = art.resize((round(w), round(h)), Image.LANCZOS)
    canvas.alpha_composite(art, (round(W * 0.42 - w / 2), round(H - h * (1 - CALLER_SINK))))
    if saru:
        share, hidden = SARU_PLACEMENT[saru]
        monkey = crop(f"call.saru.{saru}")
        sh = H * share
        sw = sh * monkey.width / monkey.height
        monkey = monkey.resize((round(sw), round(sh)), Image.LANCZOS)
        if saru == "thumbsDown":
            monkey = monkey.transpose(Image.FLIP_LEFT_RIGHT)
        canvas.alpha_composite(monkey, (round(W - sw * (1 - SARU_OVERHANG)), round(H - sh * (1 - hidden))))
    canvas.convert("RGB").save(OUT / out, quality=84, optimize=True, progressive=True)
    print(out)


still("01-assignment.jpg", "kanemochi", "yelling", saru="thumbsDown")
still("02-site.jpg", "marisol", "neutral")
still("03-tenants.jpg", "kanemochi", "smug", saru="banana")
still("04-memo.jpg", "yuki", "menace")
still("05-sister.jpg", "jo", "smug")
still("06-launch.jpg", "kanemochi", "neutral", saru="peekLow")
