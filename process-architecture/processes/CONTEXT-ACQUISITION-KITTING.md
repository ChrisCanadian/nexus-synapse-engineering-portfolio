# 300 — Context Acquisition & Kitting

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-300](../controls/CTRL-300-CONTEXT-ELIGIBILITY-SCOPE.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED · V5 HARDENING  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-003/004/005; CAP-008–012; CAP-020; CAP-025/027/028/029

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [← Analysis & Inspection](./ANALYSIS-INSPECTION.md) · [→ SSR & Context Assembly](./SSR-CONTEXT-ASSEMBLY.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **Context Acquisition & Kitting** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

TurnRequest + advisory analysis + canonical state owners.

## Outputs

Authorized Context Package.

## Process / decision logic

1. Parallel acquisition begins from trusted actor/scope.
2. Identity/Character Sheet projection; validate mode/version permission or fall back to baseline.
3. Session/CAG continuity acquisition.
4. Memory query scope authorization → structured prefilter → semantic/temporal/topic/project/relationship ranking → candidate safe/current/in-scope?
5. Continuity owner acquires tasks/pins/decisions/outcomes/follow-ups/relationships.
6. Goals: user-authorized active goal vs emergent candidate.
7. Tool discovery: handler/manifest dispatchable? enabled for actor/mode/policy? If not, hide from model.
8. Join into Authorized Context Package.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-300**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
