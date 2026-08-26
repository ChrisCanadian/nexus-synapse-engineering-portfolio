# 700 — Final Inspection & Delivery

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-700](../controls/CTRL-700-RESPONSE-RELEASE.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED · V5 HARDENING  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-033 self-correction; CAP-034 trust calibration; CAP-035 inspector; CAP-036 frontend rendering

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [← Tool Workcell & Proof](./TOOL-WORKCELL-PROOF.md) · [→ Transaction Close & Async Continuity](./TRANSACTION-CLOSE-ASYNC-CONTINUITY.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **Final Inspection & Delivery** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

Draft response + context/tool/artifact/evidence receipts.

## Outputs

Released response events or bounded failure/incident.

## Process / decision logic

1. Draft response enters receipt-aware self-correction.
2. Decision: hard claim/policy checks pass? If yes, release.
3. If no, bounded correction/reinspection.
4. Decision: Tier-1/bounded attempt limit reached? If exhausted, bounded failure/incident; otherwise recheck.
5. Final event stream is emitted.
6. Delivery decision: ordered and duplicate-free?
7. If gap/disconnect occurs, resume from monotonic cursor or emit explicit partial/error rather than inventing completion.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-700**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
