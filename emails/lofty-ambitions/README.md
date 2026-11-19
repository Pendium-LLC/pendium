# Lofty Ambitions welcome emails

New subscribers from the lobby sign-up get six emails from the people of Hanami Bay. Each email looks like a video call from the game. It tells part of the story and teaches one thing about the game. By launch day, readers know the premise, the cast and the cozy side of the tower.

## The series

| # | Sends | From | Subject | Teaches |
|---|---|---|---|---|
| 1 | On sign-up | Mr. Kanemochi | Your last assignment | The premise: your last chance, one tower in Hanami Bay |
| 2 | 3 days later | Marisol | Boss! It's Marisol (calling from a beam) | Build up, fill it, elevators earn rent |
| 3 | 7 days later | Mr. Kanemochi | Complaints from your tenants | The ramen bar, music, mishaps, day and night |
| 4 | 12 days later | Yuki | Do not forward this | The mystery: a press release about your failure already exists |
| 5 | 18 days later | Jo | Why did they give you that lot? | Asks the reader to share the page with one friend |
| 6 | Launch day, by hand | Mr. Kanemochi | The doors are open | The buy button |

## Rules for the copy

- Every character speaks as they do in the game's calls (`yoot-tower/Sources/TowerCore/StoryScript.swift`).
- The emails never mention Mr. Mochikane, the buyout or the ending. The game pays those off.
- Every email ends with an out-of-character footer that names Pendium and says the people are characters.
- Each email offers two replies, like the game's calls. A reply opens a pre-filled email to hello@pendium.co.

## Files

- `0N-*.md`: the copy and settings for each email. Edit these.
- `html/0N-*.html`: paste-ready email HTML with absolute image URLs. Generated.
- `preview.html`: all six emails in order, for review. Generated.
- `../../lofty-ambitions/assets/email/`: the call stills. Generated.

Rebuild after editing:

```bash
python3 scripts/build-emails.py
```

Rebuild the call stills from the game repo:

```bash
python3 scripts/build-email-stills.py ~/Projects/yoot-tower
```

## Setting it up in Buttondown

1. Merge this to `main`, so the stills are live at `https://pendium.co/lofty-ambitions/assets/email/`. The emails load their images from there.
2. In Buttondown, create an automation that starts when someone subscribes. Add emails 1 to 5 with the delays in the table. Check that your Buttondown plan includes automations.
3. For each email, paste the subject, the preview text from the `.md` file, and the HTML from `html/`.
4. Make sure someone reads hello@pendium.co, because the reply buttons write there.
5. Send each email to yourself first. Check it in Gmail, Apple Mail and Outlook.
6. On launch day, replace `STORE_LINK` in `06-launch.md`, rebuild, and send email 6 as a broadcast to everyone.
