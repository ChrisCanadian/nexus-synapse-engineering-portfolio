# Nexus Synapse — Public Process Architecture

> **The model is not the system. The runtime is a process.**

This page is the public-safe navigation point for the Nexus Synapse process-architecture artifacts.

The diagrams describe **how Nexus performs work**: receiving, analysis, context kitting, deterministic state reconstruction, inference dispatch, governed tool execution, inspection, transaction close, and asynchronous continuity work.

They do **not** publish the private runtime implementation. Exact thresholds, formulas, SQL, private SSR ranking/eligibility logic, gauge math, prompt/preprompt text, credentials, sensitive schemas, and other implementation-specific tolerances remain private.

## Watch a request move through Nexus

<p align="center">
  <a href="https://drive.google.com/file/d/1NIdSnrbs-ncfEuKrfl8tqVj_mFQYeIDY/view">
    <img src="https://drive.google.com/uc?export=view&id=1tdAB4qAyewZSk8Sm9G_XcLqa75ElU1-m" width="960" alt="Animated Nexus Request Watch showing a request moving through runtime stations">
  </a>
</p>

<p align="center"><strong>Request Watch v0.4.1</strong> — click the animation for the Drive-playable MP4.</p>

The animation is an explanatory presentation artifact. Its dwell/transition timing is illustrative, not live runtime takt.

## The three process views

| View | Purpose | Open |
|---|---|---|
| **Request Watch** | Presentation-scale view of a request moving through the top-level runtime stations while active responsibilities light up | [Play MP4](https://drive.google.com/file/d/1NIdSnrbs-ncfEuKrfl8tqVj_mFQYeIDY/view) |
| **Master Process Map v0.4** | Full public-safe process topology with workcells, equipment, material/state, inspection gates, WIP, custody, forks/joins and rework | [Open public folder](https://drive.google.com/drive/folders/1IMBTV6jCgvny9R7cHaC7t3xDKwlNgdv6) |
| **Value Stream v0.2** | Compact Lean/process view of the governed turn, transaction close, WIP/outbox and async support lane | [Open public folder](https://drive.google.com/drive/folders/1nJfxZPd6GO68QfWrTiWQnSuNgLuDU_tj) |

## ISO-style process library

The public Process Library follows the same basic navigation pattern as a controlled work-instruction system: a high-level **Scope / Process Index** points into the individual process instructions.

**[000 — Governed Turn — Scope & Process Index](https://docs.google.com/document/d/1QNbGg-9jtjbGt7_wq3ZqSkKxTgRtAwcnGaudEHi7cN8/edit)**

```text
Receiving & Trust Boundary
        ↓
Analysis & Inspection
        ↓
Context Acquisition & Kitting
        ↓
SSR & Context Assembly
        ↓
Forklift & Inference Dispatch
        ↓
Tool Workcell & Proof
        ↓
Final Inspection & Delivery
        ↓
Transaction Close & Async Continuity
```

The `000` document hyperlinks to each public-safe process overview so a reader can move through Nexus as a process rather than hunt through folders.

**[Open the full public Process Library](https://drive.google.com/drive/folders/1OxbZuS2WHDs9CJx48WXRSk_6vwIBUwVP)**

## Process notation

The master map uses visual distinctions only where they correspond to a real architectural distinction:

- **Responsibility / workcell** — owns a transformation, decision, authorization, inspection, or domain meaning.
- **Equipment / dependency** — performs computation for a responsibility without owning runtime authority. Examples include Stanza, BART, DistilRoBERTa, VADER, MiniLM, provider adapters, and LLMs where applicable.
- **Material / state handoff** — structured work product moving between responsibilities.
- **Inspection / release gate** — decides whether work may proceed, degrade, retry, fail, or enter bounded rework.
- **Queue / WIP** — durable work that exists but may not yet be processing.
- **Persistent custody** — canonical runtime state.
- **Artifact custody** — binary/document/image artifact storage distinct from canonical structured state.
- **Candidate / proposal boundary** — advisory/inferred work that cannot silently mutate protected state.
- **Solid flow** — synchronous/control dependency.
- **Dashed flow** — asynchronous, advisory, derivative, or non-blocking handoff as labelled.
- **Fork / join** — real parallel fan-out/fan-in.
- **Rework / re-entry** — bounded retry, correction, or continued tool execution.

## One system, not a diagrammatic hybrid

These artifacts depict **V5 as the target Nexus runtime**.

Current production is used as a parity/reconciliation source. When production contains a responsibility V5 is expected to preserve but V5 does not yet contain it, that is a **V5 parity gap**, not permission to silently merge two different systems into one picture.

Likewise, logical state ownership does not imply a separate physical database per subsystem. The process map uses one canonical Nexus durable-state boundary, with separate derived indexes or artifact/object custody only where those storage responsibilities are actually distinct.

## Public / private release discipline

The working process architecture is maintained privately and publication copies are released separately:

```text
PRIVATE CONTROLLED BINDER
        ↓
work · reconcile · review
        ↓
approved PUBLIC-SAFE revision
        ↓
PUBLIC RELEASES
```

`PUBLIC-SAFE` describes what the artifact is safe to disclose. `PUBLIC` describes whether someone can actually access that copy.

The public release folder contains approved distribution copies. It is not the working source of truth for private Nexus engineering.

**[Open Nexus Process Architecture — Public Releases](https://drive.google.com/drive/folders/1uhNpMfOIaJsdOmtT0EFw3HsYbiFiQtHU)**

---

For current evidence labels and claim ceilings, return to the [Engineering Portfolio README](../README.md), [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md), and [Public Technical Reference](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md).
