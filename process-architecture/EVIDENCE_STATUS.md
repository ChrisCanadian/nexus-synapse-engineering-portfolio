# Process Architecture — Evidence Status

**Document ID:** `PA-EVIDENCE-001`  
**Release:** v0.6  
**Classification:** PUBLIC-SAFE  

> **The map is a navigation layer over evidence. It is not Exercise, Activation, or Durability evidence by itself.**

## Evidence snapshot

| Badge | Meaning in this release | Evidence basis / claim ceiling |
|---|---|---|
| `CURRENT-PROD PATTERN` | The responsibility family / process shape is reconciled against the current-production parity oracle. | Production service/runtime composition and reachable local code. This does **not** mean every V5 hardening guard is already present in production. |
| `V5 CODE-BACKED` | The represented responsibility family exists in the current V5 reconstruction branch. | `nexus-v5-reconstruction@cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5` |
| `V5 ACCEPTANCE-TESTED` | The V5 branch has green behavioral/failure/container/contract evidence across implementation-required scope. | GitHub Actions run `32967121290` concluded `success`, including canonical capability validation, compile/migrations, behavioral and failure tests, browser event-contract tests, deployable image build, Compose/single-writer validation, and container tests. |
| `V5 HARDENING` | The V5 representation includes an additional guard, receipt, recovery, explicit authority boundary, or failure treatment beyond the production parity shape. | V5 contracts/tests; this is not a claim that the same hardening path exists in current production. |
| `DOGFOOD ACTIVATION` | Operational activation of the controlled V5 test instance. | **Separate claim.** Code/test status does not imply deployment activation or sustained durability. |
| `TRACEABILITY GAP` | The public documentation can identify the governing `CTRL-*` family, but the runtime is not yet claimed to bind `control_id + approved_revision` into every PASS/FAIL decision receipt. | Must be implemented and acceptance-tested before promoting this claim. |

## Production parity snapshot

Current-production reference: `ChrisCanadian/nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd`.

The current production architecture is the behavioral/parity source for the V5 reconstruction. It establishes the exercised responsibility pattern; V5 reconstructs that pattern behind clearer contracts and adds hardening where approved.

## V5 code/test snapshot

V5 reference: `ChrisCanadian/nexus-v5-reconstruction@cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`.

CI reference: `https://github.com/ChrisCanadian/nexus-v5-reconstruction/actions/runs/32967121290`.

The cited CI run completed successfully. Public process architecture therefore distinguishes **code-backed / acceptance-tested** from **activated / durable in dogfood or production** instead of collapsing all evidence tiers into one badge.
