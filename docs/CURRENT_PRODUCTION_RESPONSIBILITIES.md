# Current Production Responsibilities — Two-Minute Orientation

**Latest retained deployed-production reconciliation used by this page:** August 14, 2026 read-only audit, supplemented where stated by later production-facing challenge evidence.  
**Current production code reference used by the 2026-08-26 public reconciliation:** `nexus-synapse-runtime@2514a11366f8e7f345bb854c0cfaee8c7b40dddd`.

This page is the shortest public-safe orientation to the **latest audited production responsibility chain**. “Current” here means the strongest retained production evidence currently published; it does not imply that every line below was re-observed live on August 26.

For newer V5 code/test evidence, use [Process Architecture Evidence Status](../process-architecture/EVIDENCE_STATUS.md) and [Current Public Snapshot](CURRENT_PUBLIC_SNAPSHOT.md). For production implementation detail and evidence limits, use [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md) and the [Public Technical Reference v1.1](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md).

> **The model performs inference. The runtime owns the continuity, boundaries, capabilities, and durable state around that inference.**

## Primary production responsibility chain

```text
authenticated request
        ↓
1. resolve user / session / scope
        ↓
2. analyze the current request
        ↓
3. select eligible continuity + memory
        ↓
4. reconstruct bounded operating context
        ↓
5. apply profile / behavioral configuration / rules
        ↓
6. route to an eligible model/provider
        ↓
7. authorize + execute tools when required
        ↓
8. run deterministic post-generation checks
        ↓
9. persist permitted state / summaries / adaptation
        ↓
response / delivery through the production path
```

This is a responsibility orientation, not the canonical V5 value stream. The V5 target makes inspection, receipts, transaction close, outbox work and bounded continuation more explicit; see [Public Process Architecture](PROCESS_ARCHITECTURE.md).

Not every optional subsystem participates in every turn.

## Responsibility ownership

| Responsibility | Primary owner | Public-safe audited-production note |
|---|---|---|
| Authentication / trusted scope | Runtime | Normal authenticated path is runtime-owned in the audited production code line |
| Session continuity | Runtime | Persistent conversation/session state is external to model weights |
| Request analysis | Runtime services | August 14 deployed-code inspection found active analysis using external inference/static fallback; the older local NLP path was not the active analyzer in that audited path |
| Memory eligibility / selection | Runtime | Relational memory was current; semantic/vector recall was conditional and stale/degraded in the August 14 audited state |
| Context reconstruction | Runtime / SSR V2 | Present and behaviorally consequential in the audited production path |
| Profile, gauges, modes, rules, learned preferences | Runtime state | Populated production state conditions later model context |
| Model inference | Selected LLM/provider | The selected model generates inside the prepared runtime context |
| Tool proposal | Model | Proposal is not authority |
| Tool visibility / authorization / dispatch | Runtime | Runtime decides which tools are visible, allowed, executed, and returned |
| Optional Senate / advisory cognition | Runtime-orchestrated models | Conditional advisory context; not execution authority |
| Reflection context | Runtime state | Populated in the August 14 state audit |
| Self-model projection | Runtime state | Omitted in the August 14 audited main path because of a storage-contract mismatch |
| Post-generation guards | Runtime | Deterministic truth / hallucination checks follow generation in the audited production code |
| Interaction + summary persistence | Runtime | Present; later August 18 challenge evidence also observed persistence barriers while exposing a correction-persistence failure |
| Learned-preference adaptation | Runtime | Persisted and later consumed by SSR V2 in the audited path |
| Thinker / higher-order background cognition | Optional subsystem | Not proven as part of the audited main deployed turn path |

## SSR: current canonical meaning

In current portfolio documentation, **SSR means Structured State Reconstruction**.

Earlier project documents used the acronym differently while the architecture was evolving. Those historical meanings are preserved in the [Glossary](GLOSSARY.md), but they are not the default meaning for current architecture claims.

At the public-safe level, SSR is the runtime responsibility that reconstructs a bounded operating context from eligible state before inference. That can include identity/profile data, gauges, mode, user rules, learned preferences, selected continuity/memory, reflections, tool/capability facts, and optional advisory context.

## Production vs V5

This page describes the **production parity source**, not the V5 target diagram.

V5 preserves/reconstructs these responsibilities behind clearer typed contracts and adds approved hardening such as more explicit receipts, recovery paths, job/outbox semantics, validation and release controls. V5 code/test evidence is tracked separately so production facts are not silently blended into target-state claims.

## Optional / supporting systems

Systems such as Senate, cognitive-node scoring, reflection, and other conditional services may contribute context or critique. They are **supporting runtime services**, not prerequisites for understanding the main responsibility chain above, and they should not be assumed active on every turn.

## What this page does not claim

This one-pager does **not** claim:

- that August 14 evidence is a live August 26 execution trace;
- that every historical subsystem is currently active;
- that every responsibility above has equal evidence strength;
- that one retained audit proves the whole production runtime end to end;
- that the public artifacts reproduce the private parent runtime;
- that implementation presence alone establishes current behavioral activation;
- that V5 code/test evidence establishes V5 dogfood activation or production deployment.

For the production evidence boundary, continue with [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md). For the current cross-repository/V5 snapshot, use [Current Public Snapshot](CURRENT_PUBLIC_SNAPSHOT.md).
