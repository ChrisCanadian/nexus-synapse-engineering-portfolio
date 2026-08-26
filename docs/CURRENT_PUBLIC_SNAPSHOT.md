# Nexus Synapse — Current Public Snapshot

**Snapshot date:** 2026-08-26  
**Classification:** PUBLIC-SAFE  
**Purpose:** pin the repository/evidence revisions used by the latest public-documentation reconciliation

This is a reconciliation snapshot, not a claim that every repository changed on this date. A later repository head makes this snapshot historical until the next reconciliation pass.

## Runtime / reconstruction evidence anchors

| Surface | Pinned revision / evidence | Interpretation |
|---|---|---|
| Current production runtime code | `ChrisCanadian/nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd` | Production parity/code reference. Live deployment claims still require live/deployment evidence. |
| V5 reconstruction | `ChrisCanadian/nexus-v5-reconstruction@cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5` | V5 code snapshot used by Process Architecture v0.6 evidence labels. |
| V5 CI evidence | GitHub Actions run `32967121290` — `success` | Canonical capability validation, compile/migrations, behavioral/failure tests, browser event-contract tests, deployable image build, Compose/single-writer validation, and container tests. Does not by itself claim dogfood activation/durability. |

## Public bounded repositories

| Repository | Audited / reconciled head | Reconciliation result |
|---|---|---|
| Nexus Proof Runtime | `8660a3c3477d64fe203d5cda8335bbd367c5df9d` | **CORRECTED** — README/checklist no longer describe published `v0.1.1` as a pending release candidate. |
| Live Runtime Acceptance Rig | `db87ff7fb61932379a366fea94035f3134602d4b` | **CURRENT** in initial drift pass; no material README/release contradiction found. |
| Nexus Mode Card Creator | `468cae066142a73edfc4e9845f4dfd8a2e9e2ccc` | **CURRENT** in initial drift pass; bounded authoring claim remains explicit. |
| Nexus Memory Kernel | `a29bdb88f9569ac416522261deabe27f50226916` | **CURRENT** in initial drift pass; public reference-kernel boundary remains explicit. |
| Nexus Black-Box Validation Gateway | `8dbfc04d40ba068cfd2d0d32a7228ac705db307e` | **CURRENT** in initial drift pass; failed August 18 fixed-invariant result remains controlling, separate unseen challenge pass remains separate. |
| OpenAI-compatible Router | `f7e27f89` (full head pinned by the 2026-08-26 audit record) | **CURRENT** in initial drift pass; generic infrastructure boundary remains explicit. |
| ChrisAI Runtime | `8a692b93` (full head pinned by the 2026-08-26 audit record) | **CURRENT** in initial drift pass; historical reconstruction boundary remains explicit. |

> The shortened Router/ChrisAI hashes above are retained from the reconciliation record. The next monthly full pass should refresh them to full SHAs in this table.

## Engineering portfolio / process architecture

- Process Architecture v0.6 controlled release commit: `dca16981e742755164968d4fb47b824935226b78`.
- Request Watch GitHub Pages v0.6 deployment branch was updated during the same release sequence; the live page is: `https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/`.
- Portfolio reconciliation baseline immediately before this snapshot: `29056755714fa32808fa0c3fa074e6aea535211f`.
- The snapshot file itself is a subsequent documentation-control commit; use Git history for the exact snapshot-file revision.

## Corrections made in this reconciliation pass

1. Published Process Architecture v0.6 and moved canonical public process documentation into GitHub.
2. Updated Request Watch to v0.6 and synchronized traveler arrival with station/detail/governance activation.
3. Updated Master Process Map to v0.6 with governing-control and evidence-tier semantics.
4. Reconciled `docs/PROCESS_ARCHITECTURE.md` to v0.6 and GitHub-first public authority.
5. Reconciled `docs/NEXUS_VISUAL_GALLERY.md` to current Request Watch/Master/Value Stream versions.
6. Reconciled the portfolio README to current process versions, evidence-tier language, and GitHub/Pages/Drive roles.
7. Reconciled `docs/REPOSITORY_MAP.md` and added the Process Architecture release set.
8. Corrected Nexus Proof Runtime's stale `v0.1.1` release-candidate wording and archived the completed initial-release checklist.
9. Added `RECONCILIATION_CONTROL.md` so future drift checks have explicit triggers/cadence/source routing.

## Next reconciliation triggers

This snapshot should be refreshed immediately if any of the following changes materially:

- production release/live-runtime evidence;
- V5 code/test/dogfood status;
- any public bounded repository release/head in a claim-bearing way;
- process architecture version/evidence status;
- public technical reference revision;
- validation/benchmark result that changes a claim ceiling.

See [Reconciliation and Publication Control](RECONCILIATION_CONTROL.md).
