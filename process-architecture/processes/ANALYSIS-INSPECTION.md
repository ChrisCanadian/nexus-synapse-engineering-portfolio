# 200 — Analysis & Inspection

**Document class:** Public-safe process work instruction / ADONIS-style drill-down  
**Parent:** [000 — Governed Turn](./000-GOVERNED-TURN.md)  
**Applicable controlled documents:** [CTRL-200](../controls/CTRL-200-ANALYSIS-QUALITY.md)  
**Decision-receipt control revision:** **V5 GAP — not yet claimed as runtime-bound**  
**Evidence status:** CURRENT-PROD PATTERN · V5 CODE-BACKED · V5 ACCEPTANCE-TESTED  
**Evidence snapshot:** [PA-EVIDENCE-001](../EVIDENCE_STATUS.md) · production `2514a113…` · V5 `cea8d9c…` · CI `32967121290` PASS  
**Capability basis:** CAP-006 NLP turn state; CAP-014–018 learning/adaptation responsibilities

[↑ 000 Governed Turn](./000-GOVERNED-TURN.md) · [← Receiving & Trust Boundary](./RECEIVING-TRUST-BOUNDARY.md) · [→ Context Acquisition & Kitting](./CONTEXT-ACQUISITION-KITTING.md)

## Scope

Defines the public-safe process boundary, responsibility flow, material handoffs, decisions and degraded/failure behavior for **Analysis & Inspection** in the V5 runtime. Current production supplies the exercised parity pattern; V5 reconstructs that responsibility behind explicit contracts and approved hardening. Production and V5 evidence remain separately labeled.

## Inputs

Trusted turn text + session signals + optional validated pre-analysis.

## Outputs

Advisory NLPState / FocusState / emphasis + learning candidates.

## Process / decision logic

1. Use validated precomputed NLPState if available.
2. Otherwise decision: NLP adapter available? Degrade/omit with low confidence if unavailable.
3. Stanza parse + phrase detection.
4. Parallel fork: BART combined zero-shot; DistilRoBERTa emotion; VADER intensity/polarity.
5. Join into overall NLP result.
6. Decision: multiple sentences? Reuse overall for one sentence; otherwise batch sentence intent/topic/emotion-context in parallel.
7. Focus cascade: enough history? → fatigue? → deep focus? → flow? → cruising.
8. Attention routing combines advisory NLP/focus/salience/mode.
9. MiniLM similarity and slang calibration can create background candidates; they do not become canonical fact directly.

## Governing control / applicable controlled documents

This process is governed for public documentation by **CTRL-200**. The control family states what is governed. Exact private thresholds/policy expressions remain withheld.

**Traceability claim ceiling:** the runtime is not yet claimed to attach the exact approved control revision to every PASS/FAIL or equivalent decision receipt. That is a V5 implementation and acceptance-test requirement.

## State / evidence custody

Logical process ownership does not imply a separate subsystem database. Canonical structured state remains inside the shared Nexus durable-state boundary. Derived indexes and artifact/object storage are separate only where their custody responsibility is materially different.

## Failure / degraded behavior

Failure, fallback, retry, fail-open/fail-closed and bounded-rework paths are shown only where supported by current target contracts or production parity evidence. A missing or unsupported path must not be narrated as success.

## Public-safe boundary

Withheld: exact SQL, prompt/preprompt content, private SSR ranking/eligibility, gauge math, thresholds/confidence formulas, sensitive schemas, credentials and private governance logic.
