"""News image entry: copy the bundled front page to the output directory."""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", output_dir / "entry.png")


if __name__ == "__main__":
    main()
