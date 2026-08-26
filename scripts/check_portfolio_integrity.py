#!/usr/bin/env python3
"""Validate structural integrity of the public engineering portfolio.

Checks only repository-local, publication-safe properties:
- Markdown relative links resolve to files/directories in the checkout.
- JSON files parse successfully.
- Local evidence-ledger source paths exist.
- Control traceability has the complete controlled control-family set.
- Traceability process/control documents exist and CAP references are well formed.
- Reconciliation source pins are structurally valid and uniquely identified.

External URLs are deliberately not fetched so CI stays deterministic and does not
turn third-party availability into a repository failure. Remote drift is handled by
scripts/check_reconciliation.py and the scheduled reconciliation workflow.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
CAP_ID = re.compile(r"^CAP-\d{3}$")
EXPECTED_CONTROLS = {
    "CTRL-100",
    "CTRL-200",
    "CTRL-300",
    "CTRL-400",
    "CTRL-500",
    "CTRL-600",
    "CTRL-610",
    "CTRL-700",
    "CTRL-800",
}
ALLOWED_CAP_ROLES = {"primary", "supporting", "conditional_supporting"}
ALLOWED_FAMILY_EVIDENCE = {
    "CURRENT_PROD_PATTERN",
    "V5_CODE_BACKED",
    "V5_TESTED",
    "V5_HARDENING",
}
ALLOWED_ACTIVATION = {
    "DOCUMENTED",
    "CODE_BACKED",
    "TESTED",
    "STAGING_ACTIVATED",
    "PRODUCTION_ACTIVATED",
    "DURABLE",
    "INDEPENDENTLY_VERIFIED",
}


def normalize_markdown_target(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None

    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]

    if target.startswith("#"):
        return None

    parts = urlsplit(target)
    if parts.scheme.lower() in EXTERNAL_SCHEMES or parts.netloc:
        return None

    path = unquote(parts.path)
    return path or None


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for md in sorted(ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw = match.group(1)
            target = normalize_markdown_target(raw)
            if target is None:
                continue

            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{md.relative_to(ROOT)}: link escapes repository boundary: {raw}"
                )
                continue

            if not candidate.exists():
                errors.append(
                    f"{md.relative_to(ROOT)}: missing relative link target: {raw}"
                )
    return errors


def check_json_files() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    return errors


def check_evidence_sources() -> list[str]:
    ledger = ROOT / "evidence" / "claims-and-evidence.json"
    if not ledger.exists():
        return ["evidence/claims-and-evidence.json: missing evidence ledger"]

    data = json.loads(ledger.read_text(encoding="utf-8"))
    errors: list[str] = []
    for claim in data.get("claims", []):
        claim_id = claim.get("id", "<unknown>")
        for source in claim.get("sources", []):
            if not isinstance(source, str):
                errors.append(f"{claim_id}: non-string evidence source: {source!r}")
                continue
            if source.startswith(("http://", "https://")):
                continue
            target = (ROOT / source).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{claim_id}: evidence source escapes repository: {source}")
                continue
            if not target.exists():
                errors.append(f"{claim_id}: missing local evidence source: {source}")
    return errors


def check_traceability_registry() -> list[str]:
    path = ROOT / "process-architecture" / "traceability" / "CONTROL_TRACEABILITY.json"
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: missing traceability registry"]

    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    controls = data.get("controls")
    if not isinstance(controls, list):
        return [f"{path.relative_to(ROOT)}: controls must be a list"]

    seen: set[str] = set()
    for control in controls:
        control_id = control.get("control_id", "<missing>")
        if control_id in seen:
            errors.append(f"{path.relative_to(ROOT)}: duplicate control_id {control_id}")
        seen.add(control_id)

        for field in ("process_doc", "control_doc"):
            raw = control.get(field)
            if not isinstance(raw, str) or not raw:
                errors.append(f"{control_id}: missing {field}")
                continue
            target = ROOT / raw
            if not target.exists():
                errors.append(f"{control_id}: {field} does not exist: {raw}")

        capabilities = control.get("v5_capabilities", [])
        if not capabilities:
            errors.append(f"{control_id}: no V5 capability mapping")
        for capability in capabilities:
            cap_id = capability.get("id", "")
            role = capability.get("role")
            if not CAP_ID.fullmatch(cap_id):
                errors.append(f"{control_id}: invalid capability id {cap_id!r}")
            if role not in ALLOWED_CAP_ROLES:
                errors.append(f"{control_id}: invalid capability role {role!r} for {cap_id}")

        for evidence in control.get("family_evidence", []):
            if evidence not in ALLOWED_FAMILY_EVIDENCE:
                errors.append(f"{control_id}: unsupported family evidence label {evidence!r}")

        activation = control.get("activation")
        if activation not in ALLOWED_ACTIVATION:
            errors.append(f"{control_id}: unsupported activation label {activation!r}")

        if control.get("traceability") != "TRACEABILITY_GAP":
            errors.append(
                f"{control_id}: universal control-revision receipt binding must remain TRACEABILITY_GAP until separately promoted"
            )

    missing = EXPECTED_CONTROLS - seen
    extra = seen - EXPECTED_CONTROLS
    if missing:
        errors.append(f"traceability registry missing control(s): {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"traceability registry contains unregistered control(s): {', '.join(sorted(extra))}")

    snapshots = data.get("source_snapshots", {})
    production_sha = snapshots.get("production_pattern", {}).get("sha", "")
    if not SHA40.fullmatch(production_sha):
        errors.append("traceability production_pattern.sha must be a full 40-character SHA")

    v5 = snapshots.get("v5_working", {})
    for field in ("working_head_sha", "code_checkpoint_sha", "ci_qualified_sha", "staging_accepted_sha"):
        value = v5.get(field, "")
        if not SHA40.fullmatch(value):
            errors.append(f"traceability v5_working.{field} must be a full 40-character SHA")

    return errors


def check_reconciliation_manifest() -> list[str]:
    path = ROOT / "reconciliation" / "sources.json"
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: missing reconciliation source manifest"]

    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return [f"{path.relative_to(ROOT)}: sources must be a non-empty list"]

    ids: set[str] = set()
    for source in sources:
        source_id = source.get("id", "<missing>")
        if source_id in ids:
            errors.append(f"{path.relative_to(ROOT)}: duplicate source id {source_id}")
        ids.add(source_id)

        if source.get("access") not in {"public", "private"}:
            errors.append(f"{source_id}: access must be public or private")
        if not source.get("repository") or not source.get("ref"):
            errors.append(f"{source_id}: repository and ref are required")
        pinned = source.get("pinned_sha", "")
        if not SHA40.fullmatch(pinned):
            errors.append(f"{source_id}: pinned_sha must be a full 40-character SHA")

    policy = data.get("policy")
    if not isinstance(policy, str) or not (ROOT / policy).exists():
        errors.append(f"{path.relative_to(ROOT)}: policy path is missing or invalid: {policy!r}")

    return errors


def main() -> int:
    errors = []
    errors.extend(check_markdown_links())
    errors.extend(check_json_files())
    errors.extend(check_evidence_sources())
    errors.extend(check_traceability_registry())
    errors.extend(check_reconciliation_manifest())

    if errors:
        print("Portfolio integrity check: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    md_count = len(list(ROOT.rglob("*.md")))
    json_count = len(list(ROOT.rglob("*.json")))
    print("Portfolio integrity check: PASS")
    print(f"- Markdown documents checked: {md_count}")
    print(f"- JSON documents checked: {json_count}")
    print("- Relative Markdown links resolve")
    print("- Evidence-ledger local sources resolve")
    print("- Control traceability registry is structurally valid")
    print("- Reconciliation source manifest is structurally valid")
    print("- External URLs intentionally not fetched here")
    return 0


if __name__ == "__main__":
    sys.exit(main())
