"""News image entry: copy the bundled front page to the output directory.

The bundled image is a newspaper front page summing up Friday 20 November
2026: the Kyiv bridge attacks, the burning tankers in the Strait of Hormuz,
Anthropic's record IPO, and the COP31 talks. The program only copies the
file, so repeated runs write identical bytes.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(here / "entry.png", target)
    if target.stat().st_size == 0:
        raise SystemExit("entry.png was copied empty")


if __name__ == "__main__":
    main()
