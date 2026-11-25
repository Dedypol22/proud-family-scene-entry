"""One short family scene for make.fun.

Winning scene (revised #7):
    Dad's shortcut home added forty minutes and one wrong turn, but it
    went past the old ice-cream van, so twenty years later nobody in
    the car has ever called it a mistake.

Why it wins, in the brief's criterion order:
    1. Family scene: the whole family is in the car together, in one
       breath, and the last beat ("nobody ... has ever called it a
       mistake") is the smile a proud judge is asked for.
    2. Heartfelt: the affection is earned, not stuck on -- a father's
       failed shortcut is forgiven for twenty years because it bought
       the family ice cream, not because the line says "we love Dad".
    3. Funny, lightly: the wry turn is the verdict itself -- a forty-
       minute detour reclassified as a family treasure, the kind of
       joke a family actually retells at the table.
    4. Tight: one sentence, every word earns its place -- two numbers
       (forty minutes, one wrong turn), one van, one verdict.
    5. Specific and fresh: a shortcut, an ice-cream van and a twenty-
       year statute of limitations -- no grandma's kitchen, no summer
       evening, no greeting-card line anywhere in sight.

Candidate scores (1-5 per criterion, criteria in brief order):
    #   C1 C2 C3 C4 C5  Total  Candidate
    1    5  5  4  4  4   22     Dad's five-minute shelf repair, midnight
    2    4  3  5  5  5   22     Mum's labelled leftovers, science experiment
    3    4  3  5  5  4   21     Family photo, only the dog looks at camera
    4    5  5  4  4  5   23     Dad recites the Wi-Fi password like a toast
    5    4  5  4  5  4   22     Sister's borrowed charger, wrapped at Christmas
    6    4  4  5  5  4   22     Grandpa narrates the football, batteries hidden
    7    5  5  4  5  5   24     Dad's shortcut, the old ice-cream van (draft)
    8    4  4  5  5  4   22     Board game night, champion of losing gracefully
    9    5  5  3  5  4   22     Power cut dinner, Dad's cold noodles win
    10   4  5  3  5  4   21     Mum's box of baby shoes, Dad tries his on
    Winner (revised #7): 5 5 4 5 5 = 24 -- "twenty years later"
    strengthens the two criteria the judge weighs first (warmth and
    heartfelt affection) without spending a wasted word.
"""

import os
import sys

SCENE = (
    "Dad's shortcut home added forty minutes and one wrong turn, but it "
    "went past the old ice-cream van, so twenty years later nobody in "
    "the car has ever called it a mistake."
)

MAX_CHARS = 280


def main() -> int:
    if not SCENE or not SCENE.strip():
        print("error: scene is empty", file=sys.stderr)
        return 1
    if SCENE.count("\n") > 1 or "\r" in SCENE:
        print("error: scene must be one or two lines", file=sys.stderr)
        return 1
    if len(SCENE) > MAX_CHARS:
        print(
            f"error: scene is {len(SCENE)} chars, over {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SCENE + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != SCENE + "\n":
        print("error: entry.txt does not match the scene", file=sys.stderr)
        return 1

    print(SCENE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
