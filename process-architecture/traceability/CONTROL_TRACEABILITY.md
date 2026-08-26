# Nexus Synapse — Control Traceability Matrix

**Traceability release:** 0.1.0  
**Reconciled:** 2026-08-26  
**Classification:** PUBLIC-SAFE

This is the public-safe configuration-management bridge between the process architecture and the evidence behind it.

> **A process map can show where work and decisions belong. It does not, by itself, prove that those responsibilities are implemented, exercised, activated, durable, or independently verified.**

The machine-readable source is [`CONTROL_TRACEABILITY.json`](CONTROL_TRACEABILITY.json).

## Configuration-management model

```text
GOVERNING CONTROLLED ARTIFACT
CTRL-* + approved public revision
        ↓ governs
PROCESS / WORKCELL
100 … 800
        ↓ implemented through
V5 CAPABILITY / FLOW
CAP-* / FLOW-*
        ↓ qualified by
CODE + TEST / CI EVIDENCE
exact SHA + workflow run
        ↓ optionally promoted by
ACTIVATION / RELEASE EVIDENCE
staging → production → durability
        ↓ supports
PUBLIC CLAIM CEILING
```

This deliberately separates **working revision**, **qualified revision**, and **activated/released revision**. A newer commit is not automatically a more strongly evidenced commit.

## Current evidence anchors

### Current production pattern / parity oracle

- Repository: `ChrisCanadian/nexus-synapse-runtime`
- `main`: `2514a11366f8e7f345bb854c0cfaee8c7b40dddd`
- Role: exercised production responsibility-pattern / parity source.

### V5 target reconstruction

- Active working branch: `reconstruction/cloud-benchmark-wrapup-20260824`
- Current working/handoff head: `3c155d1abfbc3945da84c432bb6901212e6a8975`
- Code checkpoint named by that handoff: `cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`
- Current-head CI qualification: run `32991544397` — success.
- Accepted staging release: `cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`, protected run `32967673812` — accepted on `test.nexussynapse.app`.
- Production changed by that staging release: **false**.

The accepted staging run included the gated CI/container path, immutable release build, protected test-VM deployment, public HTTPS smoke, authenticated staging chat/persistence acceptance, and release acceptance. That supports **STAGING ACTIVATED**, not production deployment or long-duration durability.

## Control-family matrix

| Control | Process family | Primary V5 capability anchors | Family evidence | Current activation ceiling |
|---|---|---|---|---|
| `CTRL-100` Trust / Scope Release | 100 Receiving & Trust | CAP-001, CAP-002 | Production pattern · V5 code · V5 test | Staging activated |
| `CTRL-200` Analysis Quality | 200 Analysis & Inspection | CAP-006 | Production pattern · V5 code · V5 test | Staging activated |
| `CTRL-300` Context Eligibility / Scope | 300 Context Kitting | CAP-003/004/005/008/011/020 + supporting continuity state | Production pattern · V5 code · V5 test · hardening | Staging activated |
| `CTRL-400` Context Release | 400 SSR / Context Assembly | CAP-007 | Production pattern · V5 code · V5 test · hardening | Staging activated |
| `CTRL-500` Provider Route Control | 500 Forklift / Inference | CAP-019 | Production pattern · V5 code · V5 test · hardening | Staging activated |
| `CTRL-600` Tool Authorization | 600 Tool / Proof | CAP-020, CAP-021, CAP-040 | Production pattern · V5 code · V5 test · hardening | Staging activated |
| `CTRL-610` Artifact Verification | 600 Tool / Proof | CAP-022 plus artifact families | Production pattern · V5 code · V5 test · hardening | Staging activated |
| `CTRL-700` Response Release | 700 Final Inspection | CAP-033/034/035/036 | Production pattern · V5 code · V5 test · hardening | Staging activated |
| `CTRL-800` Transaction / Async Control | 800 Transaction Close / Async | CAP-040 plus continuity/learning workers | Production pattern · V5 code · V5 test · hardening | Staging activated |

The matrix is intentionally family-level. Individual mapped capabilities may have different lifecycle/status values inside the V5 capability registry. **Family evidence does not silently upgrade every mapped capability to TESTED or ACTIVATED.**

## Remaining traceability gap

The documentation can now answer:

> Which public control family governs this process/decision family, which V5 capabilities implement it, and which code/test/activation snapshots support the family-level claim?

It cannot yet universally answer at runtime:

> Which exact approved revision of `CTRL-*` was bound into the receipt that caused this specific PASS/FAIL disposition?

The target receipt relationship is:

```text
control_id
approved_revision
        ↓
material decision
        ↓
result
        + evidence_refs
        + trusted actor/scope
        + turn/correlation
        + timestamp
```

Until that binding is implemented and acceptance-tested, it remains **TRACEABILITY GAP**, not a hidden assumption.

## Next refinement

This 0.1 registry establishes **control → process → CAP/FLOW → versioned evidence**. The next refinement is symbol-level implementation/test anchoring where publication-safe, so a control family can point to exact V5 source/test paths rather than only capability and CI-level evidence.
