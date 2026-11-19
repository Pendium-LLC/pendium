"""Cut the Lofty Ambitions page sprites out of the game's runtime sheets.

Run from the repo root:
    python3 scripts/build-lofty-sprites.py ~/Projects/yoot-tower

Writes PNGs to lofty-ambitions/assets/sprites/. Each floor is one PNG with one
row per room state, in the order listed in STATES (or CHAOS_STATES).
"""

import json
import sys
from pathlib import Path

from PIL import Image

GAME = Path(sys.argv[1]).expanduser()
RUNTIME = GAME / "Assets/Tokyo/Runtime"
SHEETS = RUNTIME / "Sheets"
OUT = Path("lofty-ambitions/assets/sprites")
OUT.mkdir(parents=True, exist_ok=True)

frames = json.loads((RUNTIME / "atlas.json").read_text())["frames"]
_sheet_cache = {}


def crop(name):
    frame = frames[name]
    path = SHEETS / frame["sheet"]
    if path not in _sheet_cache:
        _sheet_cache[path] = Image.open(path).convert("RGBA")
    x, y, w, h = frame["rect"]
    return _sheet_cache[path].crop((x, y, x + w, y + h)), frame


# Floors from the roof down. Each floor's rooms fill 960 px, 88 px tall.
FLOORS = {
    "f88": ["observatory", "flowerShop"],
    "f64": ["arcade", "disco"],
    "f41": ["ramen", "boba", "bakery", "candyStore"],
    "f23": ["restaurant", "fitness"],
    "f09": ["cafe", "bookshop", "garden"],
}
STATES = ["rebuilding", "vacant", "open"]
CHAOS_STATES = ["rebuilding", "vacant", "open", "damaged"]
CHAOS_FLOOR = "f23"

for floor, rooms in FLOORS.items():
    states = CHAOS_STATES if floor == CHAOS_FLOOR else STATES
    width = sum(frames[f"room.{r}.open"]["rect"][2] for r in rooms)
    sheet = Image.new("RGBA", (width, 88 * len(states)))
    for row, state in enumerate(states):
        x = 0
        for room in rooms:
            image, _ = crop(f"room.{room}.{state}")
            sheet.paste(image, (x, row * 88))
            x += image.width
    sheet.save(OUT / f"{floor}.png", optimize=True)
    print(floor, sheet.size)

lobby, _ = crop("room.lobby.gatsby.open")
lobby.save(OUT / "lobby.png", optimize=True)
print("lobby", lobby.size)

# Walk cycles: four frames in a strip of equal cells, feet on the bottom edge,
# each frame centred on its anchor so the walker does not wobble.
CELL_W, CELL_H = 28, 46
for person in ["civilian0", "civilian1", "civilian2", "civilian3", "chef", "barista"]:
    strip = Image.new("RGBA", (CELL_W * 4, CELL_H))
    for i in range(4):
        image, frame = crop(f"person.{person}.walk{i}")
        ax = frame.get("anchor", [image.width / 2, 0])[0]
        strip.paste(image, (int(i * CELL_W + CELL_W / 2 - ax), CELL_H - image.height), image)
    strip.save(OUT / f"walk-{person}.png", optimize=True)
print("walkers", (CELL_W * 4, CELL_H))
