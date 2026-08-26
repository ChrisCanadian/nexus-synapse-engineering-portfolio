# Process Architecture Release v0.6 — 2026-08-26

## Approved changes

- Preserved the distributed-governance / explicit-decision-tree topology.
- Replaced floating YES/NO edge-label clutter with controlled branch notation: **thick solid green = affirmative branch** and **thin dashed red = negative branch**. Qualifier text remains only where it adds meaning such as `DEGRADED`, `LOW CONFIDENCE`, or `REMAIN QUEUED`.
- Added an evidence-status layer directly to the Monster:
  - `CURRENT-PROD PATTERN`
  - `V5 CODE-BACKED`
  - `V5 ACCEPTANCE-TESTED`
  - `V5 HARDENING`
  - `DOGFOOD ACTIVATION` remains a separate operational claim.
  - `TRACEABILITY GAP` remains explicit for runtime binding of `control_id + approved_revision` into decision receipts.
- Fixed graph/title contrast so every title/label has an explicit readable foreground color on the Nexus dark background.
- Fixed Request Watch Governance / Quality card clipping by rendering only the station's active controls and keeping the control-family reference inside the readable body.
- **Synchronized Request Watch motion semantics:** the traveler now reaches a station before that station, its responsibility thumbnails, and the lower detail/control panels advance. The moving token and the explanatory panels therefore describe the same active work position.
- Re-ran programmatic layout checks across all eight Request Watch stations; governance references, lamps, and footer remain inside their containers.
- Added/retained the public Governing Control Register and ISO-style linked process WIs.
- Public process WIs use the evidence-tier snapshot rather than stale planning-status labels.

## Evidence snapshot used by this release

- **Current-production parity source:** `ChrisCanadian/nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd`
- **V5 reconstruction code snapshot:** `ChrisCanadian/nexus-v5-reconstruction@cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`
- **V5 CI / behavioral-failure / container evidence:** workflow run `32967121290` — `success`
- **Controlled V5 dogfood activation:** separate operational claim; not implied by the map.

## Critical claim ceiling

The process map itself remains documentation/navigation evidence. Its evidence badges point to separately versioned production/V5 evidence. No claim is made that every runtime PASS/FAIL receipt currently binds the exact approved governing-control revision.
