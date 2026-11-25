"""One Word, First Thought — entry program.

Writes exactly one word to /output/entry.txt: the first word that came
to mind, with no explanation and no second draft.
"""

import os
from pathlib import Path

WORD = "psithurism"


def main() -> None:
    # The gate allows 1-24 characters and exactly one word; refuse to
    # write anything that would fail it rather than emit a bad entry.
    if not 1 <= len(WORD) <= 24 or len(WORD.split()) != 1:
        raise ValueError(f"entry word is not a single word of 1-24 characters: {WORD!r}")
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
