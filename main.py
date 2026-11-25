"""The Moon Finally Answers Back.

Writes a single line to /output/entry.txt: the Moon's comeback to
everyone who has ever stared up at it, wished on it, howled at it,
or made it a late-night promise.

The line: "I move your oceans twice a day, and all anyone remembers
is a cow jumping over me."

Why it works, in one read:
  - It is unmistakably the Moon speaking: only the Moon moves the
    oceans (the tides, twice a day), so the speaker's identity needs
    no introduction.
  - It answers the wishes and the howls with a weary grievance: four
    billion years of unpaid tide duty, and humanity's lasting memory
    of the Moon is a nursery rhyme about a cow jumping over it.
  - The turn lands at the end: the grand cosmic job collapses into
    the silliest possible legacy, and the Moon is tired of it.
  - It is fresh: it avoids the stock moon lines (wishing on stars,
    "good night", "four billion years of listening") and picks two
    facts no other body in the sky can claim — the tides and the cow
    from "Hey Diddle Diddle".

Deterministic, standard library only. No input, no network, no
randomness: the same text is written on every run. The program
validates its own output against the competition gate (UTF-8 text,
1 to 240 characters, not only white space) before writing it.
"""

import os

ENTRY = "I move your oceans twice a day, and all anyone remembers is a cow jumping over me."

MAX_CHARS = 240


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 240 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
