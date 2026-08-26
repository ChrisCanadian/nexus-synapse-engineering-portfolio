# Nexus Synapse — Public Governing Control Register

**Document ID:** `PA-CTRL-000`  
**Release:** Process Architecture v0.6  
**Classification:** PUBLIC-SAFE  
**Authority:** Owner-approved public process documentation  
**Runtime control-revision binding:** **V5 TRACEABILITY GAP — NOT YET CLAIMED**

## Purpose

This register answers the documentation side of the ISO-style question: **which controlled requirement family governs a material release/authorization/inspection decision?**

The control IDs below are public-safe documentation/control families. They describe what is governed without exposing private thresholds, scoring, SQL, prompt content, SSR selection/ranking rules, credentials, or other implementation tolerances.

> **Important claim ceiling:** Nexus V5 is not yet claimed to bind every runtime PASS/FAIL decision receipt to `control_id + approved_revision`. That provenance is a target traceability requirement to implement and acceptance-test.

## Control families

| ID | Controlled artifact | Primary process | Public status | Runtime revision-binding status |
|---|---|---|---|---|
| [CTRL-100 — Trust / Scope Release](./CTRL-100-TRUST-SCOPE-RELEASE.md) | Trust / Scope Release | Receiving & Trust Boundary | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-200 — Analysis Quality](./CTRL-200-ANALYSIS-QUALITY.md) | Analysis Quality | Analysis & Inspection | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-300 — Context Eligibility / Scope](./CTRL-300-CONTEXT-ELIGIBILITY-SCOPE.md) | Context Eligibility / Scope | Context Acquisition & Kitting | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-400 — Context Release](./CTRL-400-CONTEXT-RELEASE.md) | Context Release | SSR & Context Assembly | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-500 — Provider Route Control](./CTRL-500-PROVIDER-ROUTE-CONTROL.md) | Provider Route Control | Forklift & Inference Dispatch | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-600 — Tool Authorization](./CTRL-600-TOOL-AUTHORIZATION.md) | Tool Authorization | Tool Workcell & Proof | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-610 — Artifact Verification](./CTRL-610-ARTIFACT-VERIFICATION.md) | Artifact Verification | Tool Workcell & Proof | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-700 — Response Release](./CTRL-700-RESPONSE-RELEASE.md) | Response Release | Final Inspection & Delivery | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |
| [CTRL-800 — Transaction / Async Control](./CTRL-800-TRANSACTION-ASYNC-CONTROL.md) | Transaction / Async Control | Transaction Close & Async Continuity | APPROVED PUBLIC-SAFE CONTROL FAMILY | GAP / not yet claimed |

## Decision traceability target

The target evidence chain is:

```text
GOVERNING CONTROLLED ARTIFACT
control_id + approved revision
            ↓ governs
AUTHORIZED PROCESS / WORKCELL
            ↓
EXECUTION / TRANSFORMATION
            ↓
INSPECTION / RELEASE GATE
            ↓
DECISION RECEIPT
result + control provenance + evidence refs + turn/correlation + time
```

The public process diagrams show the control family now. They do **not** imply that the runtime already emits the full provenance structure above.
