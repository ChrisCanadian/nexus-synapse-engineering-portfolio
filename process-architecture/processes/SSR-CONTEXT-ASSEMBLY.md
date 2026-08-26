# 400 — SSR & Context Assembly

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-400](../controls/CTRL-400-CONTEXT-RELEASE.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED · V5 HARDENING  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-007 SSR prompt construction; CAP-032 Senate

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [← Context Acquisition & Kitting](./CONTEXT-ACQUISITION-KITTING.md) · [→ Forklift & Inference Dispatch](./FORKLIFT-INFERENCE-DISPATCH.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **SSR & Context Assembly** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

Authorized Context Package + advisory turn state.

## Outputs

Bounded context package + Context Receipt + provider/governance plan.

## Process / decision logic

1. Validate required protected sections.
2. If required material is unavailable, emit explicit bounded failure/degradation.
3. Deterministic composition handles section order, eligibility, budget, provenance and redaction.
4. For each optional section: eligible? → fits protected budget? → include or omit with reason; repeat until complete.
5. Emit Context Receipt.
6. If bounded Senate is enabled, run isolated advisory seats; deadline/seat failure degrades to baseline rather than taking authority.
7. Produce Governance + Provider Plan.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-400**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
