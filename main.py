#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry runner.

Writes the locked entry line to /output/entry.txt with no trailing
newline. Standard library only; no network access needed.

End-to-end check: verified by running — output entry.txt is UTF-8,
120 characters, 120 bytes, not whitespace-only.
"""

import os

ENTRY_LINE = (
    "LGTM. parseInvoice() works, all 214 tests pass, and I have "
    "accepted that no living person will ever understand it again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
