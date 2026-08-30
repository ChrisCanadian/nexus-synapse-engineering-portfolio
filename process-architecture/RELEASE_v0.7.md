# Nexus Synapse Process Architecture — Release v0.7

**Release:** v0.7  
**Classification:** PUBLIC-SAFE  
**Status:** approved public process-architecture release record

## Purpose

v0.7 advances the public process architecture from the v0.6 release by making evidence, governance, controlled publication, and staging-activation semantics more explicit without rewriting the existing production runtime as V5.

The release remains a **process/documentation layer over separately pinned evidence**. A detailed map does not certify its own runtime state.

## Primary released surfaces

- Request Watch v0.6 remains the presentation-scale journey.
- Master Process Map / Monster advances to **v0.7**.
- Value Stream remains the compact governed-turn view.
- Process WIs remain the ISO-style navigation layer.
- Governing `CTRL-*` control families and control traceability remain part of the controlled public binder.
- [`EVIDENCE_STATUS.md`](./EVIDENCE_STATUS.md) defines the release evidence badges and claim ceilings.

## Material v0.7 changes

### 1. Explicit V5 staging activation semantics

The process architecture records a protected V5 staging release separately from V5 code/test qualification and separately from production replacement.

Accepted staging checkpoint:

`ChrisCanadian/nexus-v5-reconstruction@cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`

Protected Actions run:

`32967673812`

The run completed `build-test-image`, `validate`, `prod-parity-gate`, and `deploy-test`; `deploy-production` was skipped.

This supports **V5 STAGING ACTIVATED**. It does not support V5 production replacement or sustained durability.

### 2. Evidence-addressable process families

Major process families distinguish current-production pattern, V5 code-backed/tested status, V5 hardening, staging activation, durability ceilings, and traceability gaps rather than forcing the reader to infer implementation state from the visual alone.

### 3. Distributed governance and control-family traceability

Governance is represented at the decision points where authorization, inspection, release, fallback, retry, promotion, and evidence decisions occur.

Public-safe governing control families and the Control Traceability Matrix provide process → control → capability/flow → evidence navigation.

The stronger runtime claim remains withheld: V5 is not yet claimed to bind the exact approved `control_id + approved_revision` into every material PASS/FAIL decision receipt.

### 4. Controlled-source publication for the Monster

The v0.7 Monster publication flow uses a controlled-source manifest and checksum verification for joined Base64, gzip, and final SVG output. Corrupt/truncated source chunks fail closed rather than publishing a damaged representation.

The publisher was also corrected so brand-new/untracked generated SVG/HTML assets are staged before change detection.

### 5. Pointer/reconciliation hardening

The process-pointer reconciler was corrected after malformed relative-prefix URL forms were found. The primary Master Process Map pointer targets the GitHub Pages HTML viewer while the released SVG remains a separate vector representation.

### 6. ISO-style design-audit disposition

[`AUDIT_DISPOSITION_v0.7.md`](./AUDIT_DISPOSITION_v0.7.md) reconciles the earlier design review against v0.7 and records which findings are materially corrected, partially closed, or intentionally retained as open control-specification work.

It is a design-control disposition, not ISO certification.

## Primary evidence anchors

- Current-production parity reference: `ChrisCanadian/nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd`
- V5 working/qualified head: `ChrisCanadian/nexus-v5-reconstruction@3c155d1abfbc3945da84c432bb6901212e6a8975`
- V5 current-head qualification: Actions run `32991544397`
- V5 accepted staging release: `cea8d9c3cea1c17b4cffc0a70f195582fedd5fb5`, protected run `32967673812`
- [Process Architecture Evidence Status](./EVIDENCE_STATUS.md)
- [Control Traceability Matrix](./traceability/CONTROL_TRACEABILITY.md)
- [Governing Control Register](./controls/CONTROL_REGISTER.md)
- [ISO-Style Design Audit Disposition](./AUDIT_DISPOSITION_v0.7.md)

## Claim ceilings

v0.7 does **not** claim:

- that the process map itself proves runtime activation or durability;
- that every V5 hardening guard exists in the existing production runtime;
- that V5 has replaced the existing production runtime;
- that one staging deployment establishes sustained durability;
- that exact approved control revisions are bound into every runtime PASS/FAIL receipt;
- that the process architecture has been independently certified to a named standard.

## Historical relationship

[`RELEASE_v0.6.md`](./RELEASE_v0.6.md) remains the historical record for the previous approved process-architecture release. v0.7 does not rewrite that history.

For later evidence-ontology interpretation corrections that do not change the v0.7 process topology, see [`../docs/EVIDENCE_INTERPRETATION.md`](../docs/EVIDENCE_INTERPRETATION.md) and the current public snapshot.
