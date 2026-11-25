"""Write the warning-label entry to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "WARNING: This human has not been updated since 2019. Known bugs include forgetting names, losing keys, and crying at commercials."


def main():
    out_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
