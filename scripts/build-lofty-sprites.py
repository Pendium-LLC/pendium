"""Cut the Lofty Ambitions page sprites out of the game's runtime sheets.

Run from the repo root:
    python3 scripts/build-lofty-sprites.py ~/Projects/yoot-tower

Writes PNGs to lofty-ambitions/assets/sprites/:
- room-<name>.png: one row per state, in the order given in ROOMS.
- lobby.png: the lobby.
- walk-<person>.png: a four-frame walk cycle in equal cells, feet on the bottom edge.
- act-repairer.png: the repairer's four work frames.
- meatball.png: the two frames of the pizza parlor mishap.
- lift-cab.png, lift-doors.png: the elevator, open and closed.
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
for old in OUT.glob("*.png"):
    old.unlink()

frames = json.loads((RUNTIME / "atlas.json").read_text())["frames"]
_sheets = {}


def crop(name):
    frame = frames[name]
    path = SHEETS / frame["sheet"]
    if path not in _sheets:
        _sheets[path] = Image.open(path).convert("RGBA")
    x, y, w, h = frame["rect"]
    return _sheets[path].crop((x, y, x + w, y + h)), frame


ROOMS = {
    # Rooms you can play with.
    "apartment": ["rebuilding", "open"],
    "apartment2": ["rebuilding", "open"],
    "apartment3": ["rebuilding", "open"],
    "ramen": ["closed", "open"],
    "pizza": ["open"],
    # Rooms that fill out the rest of the tower.
    "luxuryApartment": ["open"],
    "bookshop": ["open"],
    "coworking": ["open"],
    "toyShop": ["open"],
    "laundromat": ["open"],
    "garden": ["open"],
    "petShop": ["open"],
    "chinaShop": ["open"],
    "daycare": ["open"],
    "scienceLab": ["open"],
}
for room, states in ROOMS.items():
    first, _ = crop(f"room.{room}.{states[0]}")
    sheet = Image.new("RGBA", (first.width, first.height * len(states)))
    for row, state in enumerate(states):
        image, _ = crop(f"room.{room}.{state}")
        sheet.paste(image, (0, row * first.height))
    sheet.save(OUT / f"room-{room}.png", optimize=True)
    print("room", room, sheet.size)

# The tower is 704 units wide (384 room + 64 shaft + 256 room); keep the middle of the lobby.
lobby, _ = crop("room.lobby.gatsby.open")
lobby = lobby.crop((160, 0, 160 + 704, lobby.height))
lobby.save(OUT / "lobby.png", optimize=True)
print("lobby", lobby.size)


def strip(names, cell_w, cell_h, out):
    sheet = Image.new("RGBA", (cell_w * len(names), cell_h))
    for i, name in enumerate(names):
        image, frame = crop(name)
        ax = frame.get("anchor", [image.width / 2, 0])[0]
        sheet.paste(image, (int(i * cell_w + cell_w / 2 - ax), cell_h - image.height), image)
    sheet.save(OUT / out, optimize=True)
    print(out, sheet.size)


for person in ["civilian0", "civilian1", "civilian2", "civilian3", "chef", "repairer"]:
    strip([f"person.{person}.walk{i}" for i in range(4)], 28, 46, f"walk-{person}.png")
strip([f"person.repairer.act{i}" for i in range(4)], 28, 46, "act-repairer.png")
strip(["incident.meatball.0", "incident.meatball.1"], 40, 28, "meatball.png")

for part in ["cab", "doors"]:
    image, _ = crop(f"lift.gatsby.standard.{part}")
    image.save(OUT / f"lift-{part}.png", optimize=True)
    print("lift", part, image.size)
