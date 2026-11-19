"""Build the Lofty Ambitions welcome emails from their Markdown sources.

Run from the repo root:
    python3 scripts/build-emails.py

Reads emails/lofty-ambitions/0*.md and writes:
- emails/lofty-ambitions/html/<name>.html: one paste-ready email each, with absolute image URLs.
- emails/lofty-ambitions/preview.html: every email in order, for review in a browser.

Email HTML uses tables and inline styles, because email clients ignore most CSS.
"""

import html
import re
from pathlib import Path
from urllib.parse import quote

SRC = Path("emails/lofty-ambitions")
OUT = SRC / "html"
OUT.mkdir(exist_ok=True)

LIVE_IMAGES = "https://pendium.co/lofty-ambitions/assets/email/"
PREVIEW_IMAGES = "../../lofty-ambitions/assets/email/"
REPLY_TO = "hello@pendium.co"

# Colours from the game: ink, parchment, panel, gold, coral.
INK = "#2b2433"
INK_DEEP = "#17121d"
PARCHMENT = "#f3e8cf"
PANEL = "#e9dcc0"
GOLD = "#e0b35a"
MUTED = "#6e6259"
# The letterhead colour tells you who is writing before you read a word.
ACCENT = {"Mr. Kanemochi": GOLD, "Marisol": "#f08a3c", "Yuki": "#c9cfe0", "Jo": "#f2a7a0"}

SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"
PIXEL = "'Pixelify Sans', 'Courier New', Courier, monospace"


def parse(path):
    text = path.read_text()
    _, front, body = text.split("---", 2)
    meta = {}
    for line in front.strip().splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body.strip()


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)",
                  lambda m: f'<a href="{m.group(2)}" style="color:{INK};text-decoration:underline;">{m.group(1)}</a>',
                  text)
    return text


def paragraph(block):
    block = " ".join(line.strip() for line in block.splitlines())
    # A paragraph that is only a link becomes a quiet button.
    link = re.fullmatch(r"\[(.+?)\]\((.+?)\)", block)
    if link:
        return (f'<p style="margin:26px 0 6px;"><a href="{link.group(2)}" style="display:inline-block;'
                f'font:700 15px/1 {PIXEL};color:{INK};background:{PANEL};border:2px solid {INK};'
                f'padding:11px 16px;text-decoration:none;">{html.escape(link.group(1))}</a></p>')
    # A paragraph in single asterisks is a stage direction, like the game's call notes.
    direction = re.fullmatch(r"\*([^*].*[^*])\*", block)
    if direction:
        return (f'<p style="margin:0 0 18px;font:italic 15px/1.55 {SANS};color:{MUTED};">'
                f'{inline(direction.group(1))}</p>')
    return f'<p style="margin:0 0 18px;font:17px/1.6 {SANS};color:{INK};">{inline(block)}</p>'


def reply_button(subject, reply):
    href = f"mailto:{REPLY_TO}?subject={quote(f'Re: {subject} — {reply}')}"
    return (f'<a href="{href}" style="display:block;margin:0 0 10px;font:700 16px/1.3 {SANS};color:{INK};'
            f'background:#fffaf0;border:2px solid {INK};padding:12px 16px;text-decoration:none;">'
            f'&ldquo;{html.escape(reply)}&rdquo;</a>')


def email_table(meta, body, images):
    accent = ACCENT.get(meta["caller"], GOLD)
    paragraphs = "\n".join(paragraph(b) for b in re.split(r"\n\s*\n", body))
    cta = ""
    if meta.get("cta_url"):
        cta = (f'<tr><td style="padding:4px 32px 26px;"><a href="{meta["cta_url"]}" style="display:inline-block;'
               f'font:700 18px/1 {PIXEL};color:{INK};background:{GOLD};border:3px solid {INK};padding:15px 22px;'
               f'text-decoration:none;">{html.escape(meta["cta_label"])}</a></td></tr>')
    return f"""<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:{PARCHMENT};border:3px solid {INK};">
  <tr><td style="padding:13px 22px;background:{INK};font:700 13px/1.4 {PIXEL};color:{accent};letter-spacing:0.04em;">{html.escape(meta["letterhead"])}</td></tr>
  <tr><td style="padding:0;line-height:0;"><img src="{images}{meta["still"]}" width="600" alt="{html.escape(meta["still_alt"])}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></td></tr>
  <tr><td style="padding:11px 22px;background:{INK_DEEP};font:13px/1.4 {SANS};color:{PARCHMENT};">
    <span style="color:#6fcf7a;">&#9679;</span>&nbsp; Incoming call from <strong style="font-family:{PIXEL};color:{accent};">{html.escape(meta["caller"])}</strong>
    <span style="color:#a89f96;">&nbsp;·&nbsp; {html.escape(meta["title"])}</span></td></tr>
  <tr><td style="padding:30px 32px 6px;">
{paragraphs}
  </td></tr>
{cta}
  <tr><td style="padding:6px 32px 28px;">
    <p style="margin:0 0 10px;font:700 13px/1.4 {PIXEL};color:{MUTED};">Pick a reply</p>
    {reply_button(meta["subject"], meta["reply_a"])}
    {reply_button(meta["subject"], meta["reply_b"])}
  </td></tr>
  <tr><td style="padding:18px 32px 22px;background:{PANEL};border-top:2px solid {INK};font:13px/1.55 {SANS};color:{MUTED};">
    You're getting this because you asked for launch news on <a href="https://pendium.co/lofty-ambitions/" style="color:{MUTED};">the Lofty Ambitions page</a>. Lofty Ambitions is a game by Pendium, and the people in these emails are characters from it. You can unsubscribe at any time with the link below.
  </td></tr>
</table>"""


def full_email(meta, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(meta["subject"])}</title>
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@700&display=swap" rel="stylesheet">
</head>
<body style="margin:0;padding:0;background:#1b1530;">
<div style="display:none;max-height:0;overflow:hidden;">{html.escape(meta["preview"])}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#1b1530;">
<tr><td align="center" style="padding:24px 12px;">
{email_table(meta, body, LIVE_IMAGES)}
</td></tr>
</table>
</body>
</html>
"""


emails = []
for path in sorted(SRC.glob("0*.md")):
    meta, body = parse(path)
    (OUT / f"{path.stem}.html").write_text(full_email(meta, body))
    emails.append((path.stem, meta, body))
    print("built", path.stem)

sections = []
for stem, meta, body in emails:
    sections.append(f"""<section class="email" id="{stem}">
  <dl class="meta">
    <div><dt>Sends</dt><dd>{html.escape(meta["send"])}</dd></div>
    <div><dt>Subject</dt><dd>{html.escape(meta["subject"])}</dd></div>
    <div><dt>Preview text</dt><dd>{html.escape(meta["preview"])}</dd></div>
  </dl>
  {email_table(meta, body, PREVIEW_IMAGES)}
</section>""")

(SRC / "preview.html").write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Lofty Ambitions welcome emails</title>
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@500;700&display=swap" rel="stylesheet">
<style>
  body {{ margin: 0; background: #1b1530; color: {PARCHMENT}; font: 16px/1.5 {SANS}; }}
  main {{ max-width: 640px; margin: 0 auto; padding: 32px 16px 80px; }}
  h1 {{ font: 700 30px/1.2 {PIXEL}; margin: 0 0 8px; }}
  .intro {{ margin: 0 0 40px; color: #c9c2d8; }}
  .email {{ margin: 0 0 64px; }}
  .meta {{ display: grid; gap: 6px; margin: 0 0 14px; padding: 14px 16px; background: #241d3a; border-left: 3px solid {GOLD}; }}
  .meta div {{ display: grid; grid-template-columns: 110px 1fr; gap: 12px; }}
  .meta dt {{ font: 500 14px/1.4 {PIXEL}; color: {GOLD}; }}
  .meta dd {{ margin: 0; font-size: 15px; }}
</style>
</head>
<body>
<main>
  <h1>Lofty Ambitions welcome emails</h1>
  <p class="intro">Six emails from the people of Hanami Bay, in the order a new subscriber gets them. The first five send on a schedule after sign-up. The last one goes out by hand on launch day.</p>
  {"".join(sections)}
</main>
</body>
</html>
""")
print("built preview.html")
