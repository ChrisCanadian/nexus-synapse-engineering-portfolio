# 000 — Governed Turn — Scope & Process Index

**Document ID:** `PA-000`  
**Release:** v0.7  
**Classification:** PUBLIC-SAFE  
**Canonical public record:** this GitHub repository and its commit history  
**Governing control register:** [PA-CTRL-000](../controls/CONTROL_REGISTER.md)

## Scope

This work instruction is the high-level navigable scope for one governed Nexus V5 turn. It treats V5 as the single target runtime. Current production is used only as parity/reconciliation evidence.

## Process route

[100 Receiving & Trust Boundary](./RECEIVING-TRUST-BOUNDARY.md) → [200 Analysis & Inspection](./ANALYSIS-INSPECTION.md) → [300 Context Acquisition & Kitting](./CONTEXT-ACQUISITION-KITTING.md) → [400 SSR & Context Assembly](./SSR-CONTEXT-ASSEMBLY.md) → [500 Forklift & Inference Dispatch](./FORKLIFT-INFERENCE-DISPATCH.md) → [600 Tool Workcell & Proof](./TOOL-WORKCELL-PROOF.md) → [700 Final Inspection & Delivery](./FINAL-INSPECTION-DELIVERY.md) → [800 Transaction Close & Async Continuity](./TRANSACTION-CLOSE-ASYNC-CONTINUITY.md)

```text
Receiving / Trust
      ↓
Analysis / Inspection
      ↓
Context Kitting
      ↓
SSR / Context Assembly
      ↓
Forklift / Inference
      ↓
Tool Workcell / Proof (when invoked; may re-enter inference)
      ↓
Final Inspection / Delivery
      ↓
Transaction Close / Async Continuity
```

## Per-turn interpretation

This is the governed process model for **one turn**, not a catalog of optional subsystems that Nexus occasionally bolts onto inference. Every turn is processed through this responsibility chain. Conditional gates decide whether a branch performs work, is skipped, degrades, retries, re-enters, or emits a bounded failure for that particular turn. Therefore, **per-turn process scope does not imply that every conditional branch fires on every turn**.

## Governing controls

Each process WI links to its applicable `CTRL-*` public control family. Those documents identify what is governed at each release/authorization/inspection point. **They are not evidence that V5 already binds an approved control revision into every runtime decision receipt.**

## Visuals

- [Request Watch v0.6 — live presentation](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/)
- [Master Process Map v0.7 — primary HTML viewer](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/master-process-map-v0.7.html)
- [Master Process Map v0.7 — released SVG](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/master-process-map-v0.7.svg)
- [Value Stream v0.2](../diagrams/value-stream-v0.2.svg)

## Evidence discipline

The process library separates documentation from evidence tiers. See **[Process Architecture Evidence Status](../EVIDENCE_STATUS.md)** and the **[Control Traceability Matrix](../traceability/CONTROL_TRACEABILITY.md)**. A visual tree never promotes code/test evidence to deployment Activation, sustained Durability, or independent verification by itself.
