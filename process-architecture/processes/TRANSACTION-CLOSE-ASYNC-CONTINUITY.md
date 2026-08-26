# 800 — Transaction Close & Async Continuity

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-800](../controls/CTRL-800-TRANSACTION-ASYNC-CONTROL.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED · V5 HARDENING  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-010/013/014–018/026/027/030/031/040 plus applicable persistence workers

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [← Final Inspection & Delivery](./FINAL-INSPECTION-DELIVERY.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **Transaction Close & Async Continuity** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

Delivered/final turn + receipts + queued follow-on work.

## Outputs

Durable turn history + async receipts + eligible future-turn state/candidates.

## Process / decision logic

1. Transactionally persist completed turn + receipts + durable outbox.
2. Decision: commit successful? Failure is explicit.
3. Queued work enters WIP lifecycle.
4. Decision: claim/lease available? Stale leases are recoverable.
5. Workers execute with idempotent retry/dead-letter behavior.
6. Summary worker validates source scope/provenance and usable model route.
7. Reminder worker checks schedule/consent/delivery boundary.
8. Reflection worker asks whether event is novel/recurrent/material enough to persist; otherwise recurrence telemetry only.
9. Thinker is fail-open and proposal-only.
10. Vocabulary/slang worker requires sourced/confirmed meaning before candidate creation.
11. Candidate/proposal boundary asks whether future-state mutation is eligible and authorized; otherwise reject/defer.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-800**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
