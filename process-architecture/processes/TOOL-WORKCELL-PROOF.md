# 600 — Tool Workcell & Proof

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-600](../controls/CTRL-600-TOOL-AUTHORIZATION.md); [CTRL-610](../controls/CTRL-610-ARTIFACT-VERIFICATION.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED · V5 HARDENING  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-020–024

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [← Forklift & Inference Dispatch](./FORKLIFT-INFERENCE-DISPATCH.md) · [→ Final Inspection & Delivery](./FINAL-INSPECTION-DELIVERY.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **Tool Workcell & Proof** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

Validated model proposal + trusted actor + authorized tool view.

## Outputs

Observed Tool Result / Artifact Receipt / continuation evidence.

## Process / decision logic

1. Parse typed tool proposal.
2. Decision: advertised + dispatchable?
3. Decision: trusted actor/scope authorized?
4. Decision: arguments/deadline valid?
5. Decision: async job required? Otherwise synchronous execution.
6. Multiple synchronous calls may fork/join.
7. Observe result including timing/attempt/error state.
8. Timeout/failure: retry/cancel permitted?
9. Artifact produced? If yes, verify bytes exist then hash/version/integrity before success receipt.
10. Return observed receipt to model continuation.
11. Decision: another tool proposal? If yes, V5 target re-enters the bounded tool loop.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-600 + CTRL-610**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
