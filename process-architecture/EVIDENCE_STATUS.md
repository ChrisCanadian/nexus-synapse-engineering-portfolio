# Process Architecture — Evidence Status

**Document ID:** `PA-EVIDENCE-001`  
**Release:** v0.7  
**Classification:** PUBLIC-SAFE  

> **The map is a navigation layer over evidence. It is not Exercise, Activation, Durability, or independent-verification evidence by itself.**

The evidence labels below are target/environment-specific claim dimensions. They must not be collapsed into one project-wide scalar status. For the cross-portfolio interpretation contract, see [`docs/EVIDENCE_INTERPRETATION.md`](../docs/EVIDENCE_INTERPRETATION.md).

## Evidence snapshot

| Badge | Meaning in this release | Evidence basis / claim ceiling |
|---|---|---|
| `CURRENT-PROD PATTERN` | The responsibility family / process shape is reconciled against the current-production parity oracle. | `ChrisCanadian/nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd`. This does **not** mean every V5 hardening guard is already present in production. |
| `CURRENT-PROD ACTIVATED` | The existing Nexus production runtime is operationally deployed/reachable at the retained public evidence boundary. | Aug 14 deployed-code/state inspection plus the Aug 18 campaign traversing the existing deployment. Activation does **not** establish universal invariant success, blanket durability, V5 production replacement, or independent certification. |
| `V5 CODE-BACKED` | The represented responsibility family exists in the authoritative V5 reconstruction line. | Working/qualified branch: `reconstruction/cloud-benchmark-wrapup-20260824`; reconciled head `3c155d1abfbc3945da84c432bb6901212e6a8975`. |
| `V5 ACCEPTANCE-TESTED` | The V5 line has green structural, behavioral, failure, browser-contract, image/Compose and container evidence across implementation-required scope. | GitHub Actions run `32991544397` concluded successfully across `validate` and `container-test`. Code/test evidence remains distinct from operational activation. |
| `V5 HARDENING` | The V5 representation includes an additional guard, receipt, recovery, explicit authority boundary, or failure treatment beyond the production parity shape. | V5 contracts/tests; this is not a claim that the same hardening path exists in current production. |
| `V5 STAGING ACTIVATED` | A protected V5 release was deployed to the controlled staging/test environment and passed the release acceptance path. | Staging release checkpoint `cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`; protected Actions run `32967673812` completed `build-test-image`, `validate`, `prod-parity-gate`, and `deploy-test` successfully. `deploy-production` was skipped. |
| `PRODUCTION ACTIVATION` | V5 has replaced the current production runtime. | **NOT CLAIMED.** Current production remains the separate production/parity line above. Staging activation must not be presented as production activation. |
| `DURABILITY` | Sustained operational evidence over time at the applicable deployment tier. | **SEPARATE CLAIM.** A successful release/deployment event does not by itself establish durability. Current production has bounded persistence evidence, but the portfolio does not promote that into blanket sustained durability. |
| `TRACEABILITY GAP` | The public documentation can identify the governing `CTRL-*` family, but the runtime is not yet claimed to bind `control_id + approved_revision` into every PASS/FAIL decision receipt. | Must be implemented and acceptance-tested before promoting this claim. |

## Production parity snapshot

Current-production reference: `ChrisCanadian/nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd`.

The current production architecture is the behavioral/parity source for the V5 reconstruction. It establishes the exercised responsibility pattern; V5 reconstructs that pattern behind clearer contracts and adds approved hardening.

Separately, the existing production runtime is **ACTIVATED / DEPLOYED** at the retained public evidence boundary. The August 14 inspection addressed actual deployed code/state, and the August 18 validation campaign traversed the existing deployment. This activation claim remains distinct from the failed fixed invariants, bounded persistence evidence, sustained durability, and independent verification.

## V5 working / qualified snapshot

Authoritative V5 branch: `reconstruction/cloud-benchmark-wrapup-20260824`.

Reconciled V5 head: `ChrisCanadian/nexus-v5-reconstruction@3c155d1abfbc3945da84c432bb6901212e6a8975`.

Current-head CI reference: `https://github.com/ChrisCanadian/nexus-v5-reconstruction/actions/runs/32991544397`.

The cited CI run completed successfully. Public process architecture therefore distinguishes **code-backed / acceptance-tested** from deployment tiers rather than collapsing them into one status.

## V5 staging activation snapshot

Accepted staging release checkpoint: `ChrisCanadian/nexus-v5-reconstruction@cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`.

Protected staging release run: `https://github.com/ChrisCanadian/nexus-v5-reconstruction/actions/runs/32967673812`.

That run completed the test-image build, validation, production-parity gate, and controlled `deploy-test` path successfully while `deploy-production` remained skipped. This supports **V5 STAGING ACTIVATED**. It does not support a claim that V5 is the current production release, nor does one accepted deployment establish sustained durability.

## Governing-control traceability ceiling

The process architecture can state which public-safe `CTRL-*` control family governs a decision family. Until the runtime records and acceptance evidence verifies the exact approved control revision associated with each material PASS/FAIL disposition, the stronger statement remains intentionally withheld.
