#!/usr/bin/env python3
"""Materialize generated public process assets from controlled compressed sources."""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "process-architecture" / "diagrams" / "source"
SOURCE_MANIFEST = SOURCE_DIR / "master-process-map-v0.7.source.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def materialize(out_dir: Path) -> None:
    manifest = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))
    chunks = []
    for name in manifest["chunks"]:
        path = SOURCE_DIR / name
        if not path.exists():
            raise SystemExit(f"Monster controlled source is incomplete; missing chunk: {name}")
        chunks.append("".join(path.read_text(encoding="utf-8").split()))

    encoded = "".join(chunks)
    if sha256_bytes(encoded.encode("ascii")) != manifest["joined_base64_sha256"]:
        raise SystemExit("Monster source failed joined base64 checksum")

    compressed = base64.b64decode(encoded, validate=True)
    if sha256_bytes(compressed) != manifest["gzip_sha256"]:
        raise SystemExit("Monster source failed compressed checksum")

    try:
        svg_bytes = gzip.decompress(compressed)
    except (EOFError, OSError) as exc:
        raise SystemExit(f"Monster source failed gzip integrity: {exc}") from exc

    if sha256_bytes(svg_bytes) != manifest["svg_sha256"]:
        raise SystemExit("Monster source failed SVG checksum")

    if len(svg_bytes) != manifest["svg_bytes"]:
        raise SystemExit("Monster source byte count does not match controlled manifest")

    svg = svg_bytes.decode("utf-8")
    required = (
        "PUBLIC&#45;SAFE MASTER PROCESS MAP v0.7",
        "Governing Controlled Artifact",
        "YES BRANCH · thick solid green",
        "NO BRANCH · thin dashed red",
        "CURRENT&#45;PROD PATTERN",
        "V5 CODE&#45;BACKED",
        "V5 ACCEPTANCE&#45;TESTED",
        "V5 STAGING ACTIVATED",
        "TRACEABILITY GAP",
    )
    missing = [marker for marker in required if marker not in svg]
    if missing:
        raise SystemExit(f"Monster source failed release validation; missing: {missing}")
    if "<svg" not in svg or "</svg>" not in svg:
        raise SystemExit("Monster source is not a complete SVG document")

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "master-process-map-v0.7.svg").write_bytes(svg_bytes)

    viewer = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nexus Synapse — Master Process Map v0.7</title>
<style>
html,body{margin:0;height:100%;background:#07131f;color:#f3f7fa;font-family:Arial,sans-serif}
body{display:flex;flex-direction:column}.bar{display:flex;align-items:center;gap:18px;padding:10px 16px;background:#0c1b28;border-bottom:1px solid #29485c;flex:0 0 auto}.bar strong{color:#43d9e8}.bar span{color:#9cb0bd;font-size:13px}.bar a{margin-left:auto;color:#43d9e8;text-decoration:none}object{width:100%;height:calc(100vh - 48px);border:0;background:#07131f}
</style>
</head>
<body>
<div class="bar"><strong>NEXUS SYNAPSE · MASTER PROCESS MAP v0.7</strong><span>Public-safe · controlled GitHub release representation</span><a href="master-process-map-v0.7.svg">Open SVG directly</a></div>
<object data="master-process-map-v0.7.svg" type="image/svg+xml" aria-label="Nexus Synapse V5 Master Process Map v0.7"></object>
</body>
</html>
"""
    (out_dir / "master-process-map-v0.7.html").write_text(viewer, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    materialize(args.out)
