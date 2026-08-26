#!/usr/bin/env python3
"""Check pinned Nexus public/private source revisions for documentation drift.

Weekly mode checks repository heads plus configured presentation-content markers.
Monthly mode additionally checks package versions and expected GitHub releases.

Private repositories are checked only when NEXUS_RECONCILE_TOKEN is present.
Absence of that token produces a visible PARTIAL result rather than pretending the
private source was verified.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "reconciliation" / "sources.json"
USER_AGENT = "nexus-portfolio-reconciliation/1.0"
API_VERSION = "2022-11-28"


def request_json(url: str, token: str | None, *, allow_anonymous_retry: bool = False) -> object:
    def _do(active_token: str | None) -> object:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": USER_AGENT,
        }
        if active_token:
            headers["Authorization"] = f"Bearer {active_token}"
        req = Request(url, headers=headers)
        with urlopen(req, timeout=25) as response:  # nosec B310 - fixed GitHub API host from controlled manifest fields
            return json.loads(response.read().decode("utf-8"))

    try:
        return _do(token)
    except HTTPError as exc:
        if allow_anonymous_retry and token and exc.code in {401, 403, 404}:
            return _do(None)
        raise


def repo_head(repository: str, ref: str, token: str | None, *, public: bool) -> str:
    ref_path = quote(ref, safe="/")
    url = f"https://api.github.com/repos/{repository}/git/ref/heads/{ref_path}"
    data = request_json(url, token, allow_anonymous_retry=public)
    return str(data["object"]["sha"])


def repo_file_text(repository: str, ref: str, path: str, token: str | None, *, public: bool) -> str:
    path_part = quote(path, safe="/")
    ref_part = quote(ref, safe="")
    url = f"https://api.github.com/repos/{repository}/contents/{path_part}?ref={ref_part}"
    data = request_json(url, token, allow_anonymous_retry=public)
    encoded = data.get("content")
    if not encoded:
        raise ValueError(f"{repository}:{path}@{ref}: no text content returned")
    return base64.b64decode(encoded).decode("utf-8")


def latest_release_tag(repository: str, token: str | None, *, public: bool) -> str:
    url = f"https://api.github.com/repos/{repository}/releases/latest"
    data = request_json(url, token, allow_anonymous_retry=public)
    return str(data["tag_name"])


def package_version(text: str) -> str | None:
    match = re.search(r'^version\s*=\s*["\']([^"\']+)["\']\s*$', text, re.MULTILINE)
    return match.group(1) if match else None


def load_manifest(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("sources"), list):
        raise ValueError("reconciliation manifest must contain a sources list")
    return data


def check_source(source: dict, mode: str, public_token: str | None, private_token: str | None) -> dict:
    repository = source["repository"]
    ref = source["ref"]
    access = source.get("access", "public")
    public = access == "public"

    result = {
        "id": source["id"],
        "repository": repository,
        "ref": ref,
        "status": "CURRENT",
        "details": [],
    }

    if not public and not private_token:
        result["status"] = "SKIPPED_PRIVATE"
        result["details"].append(
            "Private source not checked: NEXUS_RECONCILE_TOKEN is not configured for this workflow."
        )
        return result

    token = public_token if public else private_token

    try:
        observed_sha = repo_head(repository, ref, token, public=public)
        expected_sha = source["pinned_sha"]
        result["observed_sha"] = observed_sha
        result["expected_sha"] = expected_sha
        if observed_sha != expected_sha:
            result["status"] = "DRIFT"
            result["details"].append(f"Head changed: pinned {expected_sha}, observed {observed_sha}.")
        else:
            result["details"].append(f"Head matches pinned revision {expected_sha}.")

        for check in source.get("content_checks", []):
            text = repo_file_text(repository, ref, check["path"], token, public=public)
            missing = [marker for marker in check.get("must_contain", []) if marker not in text]
            if missing:
                result["status"] = "DRIFT"
                result["details"].append(
                    f"{check['path']} is missing required marker(s): {', '.join(missing)}."
                )
            else:
                result["details"].append(f"{check['path']} contains all required release markers.")

        if mode == "monthly":
            package_path = source.get("package_version_path")
            expected_version = source.get("expected_package_version")
            if package_path and expected_version:
                text = repo_file_text(repository, ref, package_path, token, public=public)
                observed_version = package_version(text)
                if observed_version != expected_version:
                    result["status"] = "DRIFT"
                    result["details"].append(
                        f"Package version mismatch: expected {expected_version}, observed {observed_version!r}."
                    )
                else:
                    result["details"].append(f"Package version matches {expected_version}.")

            expected_release = source.get("expected_release_tag")
            if expected_release:
                observed_release = latest_release_tag(repository, token, public=public)
                if observed_release != expected_release:
                    result["status"] = "DRIFT"
                    result["details"].append(
                        f"Latest release mismatch: expected {expected_release}, observed {observed_release}."
                    )
                else:
                    result["details"].append(f"Latest GitHub release matches {expected_release}.")

    except (HTTPError, URLError, ValueError, KeyError, json.JSONDecodeError) as exc:
        result["status"] = "ERROR"
        result["details"].append(f"Check failed: {type(exc).__name__}: {exc}")

    return result


def render_report(mode: str, results: list[dict]) -> str:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    hard = [r for r in results if r["status"] in {"DRIFT", "ERROR"}]
    skipped = [r for r in results if r["status"] == "SKIPPED_PRIVATE"]
    overall = "DRIFT" if hard else ("PARTIAL" if skipped else "CURRENT")

    lines = [
        "# Nexus Reconciliation Report",
        "",
        f"- Generated UTC: `{now}`",
        f"- Mode: `{mode}`",
        f"- Overall: **{overall}**",
        "",
        "| Source | Ref | Status |",
        "|---|---|---|",
    ]
    for item in results:
        lines.append(f"| `{item['id']}` | `{item['ref']}` | **{item['status']}** |")

    lines.extend(["", "## Details", ""])
    for item in results:
        lines.append(f"### {item['id']} — {item['status']}")
        lines.append("")
        lines.append(f"`{item['repository']}@{item['ref']}`")
        lines.append("")
        for detail in item["details"]:
            lines.append(f"- {detail}")
        lines.append("")

    if skipped:
        lines.extend(
            [
                "## Private-source coverage",
                "",
                "This run is **PARTIAL** because at least one private source could not be checked. Configure the repository Actions secret `NEXUS_RECONCILE_TOKEN` with read-only access to the named private repositories to enable those checks. Absence of private access is never reported as a successful verification.",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("weekly", "monthly"), default="weekly")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--report", type=Path, default=ROOT / "reconciliation-report.md")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    public_token = os.environ.get("GITHUB_TOKEN") or None
    private_token = os.environ.get("NEXUS_RECONCILE_TOKEN") or None

    results = [
        check_source(source, args.mode, public_token, private_token)
        for source in manifest["sources"]
    ]

    report = render_report(args.mode, results)
    args.report.write_text(report, encoding="utf-8")
    print(report)

    if any(r["status"] in {"DRIFT", "ERROR"} for r in results):
        return 2
    if any(r["status"] == "SKIPPED_PRIVATE" for r in results):
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
