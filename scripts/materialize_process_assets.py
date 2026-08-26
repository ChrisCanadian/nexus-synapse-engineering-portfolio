#!/usr/bin/env python3
"""Materialize generated public process assets from controlled compressed sources."""

from __future__ import annotations

import argparse
import base64
import gzip
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "process-architecture" / "diagrams" / "source" / "master-process-map-v0.6.svg.gz.b64"


def materialize(out_dir: Path) -> None:
    encoded = "".join(SOURCE.read_text(encoding="utf-8").split())
    svg = gzip.decompress(base64.b64decode(encoded)).decode("utf-8")

    required = (
        "NEXUS SYNAPSE V5 — PUBLIC-SAFE MASTER PROCESS MAP v0.6",
        "Governing Controlled Artifact",
        "YES BRANCH · thick solid green",
        "NO BRANCH · thin dashed red",
        "CURRENT-PROD PATTERN",
        "V5 CODE-BACKED",
    )
    missing = [marker for marker in required if marker not in svg]
    if missing:
        raise SystemExit(f"Monster source failed release validation; missing: {missing}")
    if "<svg" not in svg or "</svg>" not in svg:
        raise SystemExit("Monster source is not a complete SVG document")

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "master-process-map-v0.6.svg").write_text(svg, encoding="utf-8")

    viewer = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nexus Synapse — Master Process Map v0.6</title>
<style>
html,body{margin:0;height:100%;background:#07131f;color:#f3f7fa;font-family:Arial,sans-serif}
body{display:flex;flex-direction:column}.bar{display:flex;align-items:center;gap:18px;padding:10px 16px;background:#0c1b28;border-bottom:1px solid #29485c;flex:0 0 auto}.bar strong{color:#43d9e8}.bar span{color:#9cb0bd;font-size:13px}.bar a{margin-left:auto;color:#43d9e8;text-decoration:none}object{width:100%;height:calc(100vh - 48px);border:0;background:#07131f}
</style>
</head>
<body>
<div class="bar"><strong>NEXUS SYNAPSE · MASTER PROCESS MAP v0.6</strong><span>Public-safe · controlled GitHub release representation</span><a href="master-process-map-v0.6.svg">Open SVG directly</a></div>
<object data="master-process-map-v0.6.svg" type="image/svg+xml" aria-label="Nexus Synapse V5 Master Process Map v0.6"></object>
</body>
</html>
"""
    (out_dir / "master-process-map-v0.6.html").write_text(viewer, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    materialize(args.out)
