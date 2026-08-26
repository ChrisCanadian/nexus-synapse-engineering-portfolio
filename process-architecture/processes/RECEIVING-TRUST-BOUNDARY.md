# 100 — Receiving & Trust Boundary

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-100](../controls/CTRL-100-TRUST-SCOPE-RELEASE.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-001 Governed turn orchestration; CAP-002 Trusted actor/scope; CAP-038 team/shared state; CAP-039 auth/account privacy

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [→ Analysis & Inspection](./ANALYSIS-INSPECTION.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **Receiving & Trust Boundary** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

Trusted request / actor identity / scope.

## Outputs

Immutable TurnRequest or explicit denial/failure.

## Process / decision logic

1. Surface request arrives through Web or Discord adapter.
2. Gateway/API resolves authentication.
3. Decision: authenticated? If no, deny explicitly.
4. Resolve trusted user/team/session scope.
5. Decision: team/shared scope requested? If yes, membership/channel authorization must pass.
6. Create immutable TurnRequest + correlation/turn identity.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-100**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
