# 000 — Governed Turn — Scope & Process Index

**Document ID:** `PA-000`  
**Release:** v0.6  
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

## Governing controls

Each process WI links to its applicable `CTRL-*` public control family. Those documents identify what is governed at each release/authorization/inspection point. **They are not evidence that V5 already binds an approved control revision into every runtime decision receipt.**

## Visuals

- [Request Watch v0.6 — live presentation](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/)
- [Master Process Map v0.6 — SVG](https://drive.google.com/file/d/101Sgnz2eD5c4zHYq49Hu-d2LBuDHmyAR/view)
- [Master Process Map v0.6 — interactive HTML](https://drive.google.com/file/d/1HP5CtbCsoyrhawymOs9kVZM80bdU9xGZ/view)
- [Value Stream v0.2](../diagrams/value-stream-v0.2.svg)

## Evidence discipline

The process library separates documentation from evidence tiers. See **[Process Architecture Evidence Status](../EVIDENCE_STATUS.md)**. A visual tree never promotes code/test evidence to deployment Activation or sustained Durability by itself.
