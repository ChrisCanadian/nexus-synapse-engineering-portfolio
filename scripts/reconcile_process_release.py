#!/usr/bin/env python3
"""Reconcile current public process-document pointers after a controlled process release.

This intentionally touches only current-summary documents. Historical release records
are never rewritten.
"""

from __future__ import annotations

import argparse
from pathlib import Path

PAGES = "https://chriscanadian.github.io/nexus-synapse-engineering-portfolio"
MONSTER_HTML = f"{PAGES}/master-process-map-v0.7.html"
MONSTER_SVG = f"{PAGES}/master-process-map-v0.7.svg"

TARGETS = (
    "README.md",
    "docs/PROCESS_ARCHITECTURE.md",
    "docs/NEXUS_OVERVIEW.md",
    "docs/NEXUS_VISUAL_GALLERY.md",
    "docs/REPOSITORY_MAP.md",
    "process-architecture/README.md",
)

# Exact text/version updates. URL normalization is handled separately below so an
# absolute URL can never be accidentally prefixed by an old relative path.
REPLACEMENTS = (
    ("Master Process Map v0.6", "Master Process Map v0.7"),
    ("the full Master Process Map v0.6", "the full Master Process Map v0.7"),
    ("Open the Monster v0.6", "Open the Monster v0.7"),
    ("## v0.6 evidence + governance release", "## v0.7 evidence + governance release"),
    ("DOGFOOD ACTIVATION", "V5 STAGING ACTIVATED"),
    ("dogfood activation / durability", "staging activation / durability"),
    ("dogfood activation/durability", "staging activation/durability"),
    ("dogfood activation", "staging activation"),
)

# Known historical/current pointer shapes that should resolve to the primary HTML
# presentation. Keep the raw SVG published, but do not make it the default viewer.
MONSTER_POINTERS = (
    "process-architecture/diagrams/master-process-map-v0.6.svg",
    "process-architecture/diagrams/master-process-map-v0.6.html",
    "./diagrams/master-process-map-v0.6.svg",
    "./diagrams/master-process-map-v0.6.html",
    "master-process-map-v0.6.svg",
    "master-process-map-v0.6.html",
    "https://drive.google.com/file/d/101Sgnz2eD5c4zHYq49Hu-d2LBuDHmyAR/view",
    # Repair the malformed absolute URLs produced by the earlier naive replacement.
    f"process-architecture/diagrams/{MONSTER_SVG}",
    f"process-architecture/diagrams/{MONSTER_HTML}",
    f"./diagrams/{MONSTER_SVG}",
    f"./diagrams/{MONSTER_HTML}",
)


def reconcile(root: Path) -> int:
    changed = 0
    for relative in TARGETS:
        path = root / relative
        if not path.exists():
            raise SystemExit(f"Missing controlled summary document: {relative}")
        original = path.read_text(encoding="utf-8")
        updated = original

        for old, new in REPLACEMENTS:
            updated = updated.replace(old, new)

        for old in MONSTER_POINTERS:
            updated = updated.replace(old, MONSTER_HTML)

        updated = updated.replace(
            "code/test evidence does not imply controlled deployment activation or durability",
            "code/test evidence does not imply production activation or sustained durability; a separate accepted V5 staging release now exists",
        )
        updated = updated.replace(
            "code/test status does not imply deployment activation or sustained durability",
            "code/test status does not imply production activation or sustained durability; staging activation is evidenced separately",
        )
        updated = updated.replace(
            "code/test evidence does not imply deployment activation or sustained durability",
            "code/test evidence does not imply production activation or sustained durability; staging activation is evidenced separately",
        )

        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"reconciled {relative}")

    print(f"current-summary documents changed: {changed}")
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    reconcile(args.root.resolve())
