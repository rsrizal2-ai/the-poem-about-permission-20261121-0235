#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no keys, no external calls: the poem is embedded below.
"""

import os

POEM = """For years I waited at the door,
hand raised, asking to be let in —
until I saw the key was mine all along,
and the asking was the lock.

Now I open it for others
and hand them the key,
because the power to act
is only real when it is given away."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
