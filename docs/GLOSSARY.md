# Term Glossary — Nexus Synapse

Terms in this project changed meaning over time. This glossary records reconciled usage for public communication and flags where drift risk is high.

For current evidence/status questions, pair terminology with [Current Public Snapshot](CURRENT_PUBLIC_SNAPSHOT.md) and [Reconciliation and Publication Control](RECONCILIATION_CONTROL.md). A term definition is not an activation claim.

## SSR

**Current canonical meaning:** **Structured State Reconstruction**.

For current architecture claims, SSR refers to the runtime responsibility that reconstructs a bounded operating context from eligible state before inference. At a public-safe level, that can include identity/profile data, gauges, active mode, user rules, learned preferences, selected continuity/memory, reflections, tool/capability facts, and optional advisory context.

**Historical terminology:** Earlier Nexus documents used the acronym in several related but different ways, including Semantic SQL Retrieval, Structured-SQL-RAG, SQL-guided RAG, SSR personality engine, and SSR prompt builder. Those terms are preserved as historical source language rather than treated as the current expansion.

**Retrieval lineage:** One important early SSR ancestor used structured/SQL filtering to narrow candidates before semantic ranking. That retrieval pattern is historically significant, but **SSR does not currently mean vector search**, and not every SSR path implies an embedding stage.

**Drift risk:** High in historical material; low when using the current canonical expansion above.

## CAG

**Observed expansions**

- Conversation Archive/Cache — implemented `CAGManager` meaning.
- Context Adaptive Generator — explanatory/book meaning.
- Context-Augmented Generation — explanatory expansion in manuscript material.

**Reconciled usage**

Use **Conversation Archive/Cache** for code/runtime claims where an expansion is necessary. Preserve other expansions only as source-specific historical/public metaphors.

**Drift risk:** High.

## Engine2_0 / Engine2_1

- **Engine2_0:** Early integrated monolithic engine (Aug–Sep 2025). Named historical epoch.
- **Engine2_1:** Large modular response, personality, memory, emotion, multimodal, and routing system (Sep–Oct 2025). Named historical epoch.

**Drift risk:** Medium for Engine2_0; low for Engine2_1.

## V1–V4 retrospective labels

Book/manuscript material uses labels such as V1 monster file, V2 false architecture, V3 over-reach, and V4 SSR Minimal.

**Reconciled usage**

Use the named epochs in the architectural history. Treat V1–V4 labels as retrospective/source-specific, not formal releases.

**Drift risk:** High.

## V5

**Observed usage:** Reconstruction repository/branch family (Jul–Aug 2026) intended to become the target Nexus runtime.

**Reconciled usage:** **V5 target reconstruction/runtime line.** Current public evidence supports a code-backed and acceptance-tested reconstruction of the production responsibility pattern, with additional approved hardening. Controlled dogfood activation, sustained durability, and production replacement remain separate evidence claims.

Avoid both extremes:

- do not call V5 a production release unless deployment evidence establishes that state;
- do not reduce current V5 to merely an aspirational/isolated design when pinned code and CI/acceptance evidence exist.

See [Process Architecture Evidence Status](../process-architecture/EVIDENCE_STATUS.md).

**Drift risk:** Very high.

## Production

Historical usage has included several different meanings:

- implemented locally;
- developer rig passed;
- considered production-ready;
- present on the VM;
- enabled on the request path;
- operational but silently degraded;
- repaired through temporary infrastructure;
- durably deployed at an exact commit.

**Reconciled usage**

Where possible, split claims into:

1. implementation/code-backed;
2. test/exercise;
3. deployment target;
4. activation;
5. durability;
6. independent verification, where applicable.

For existing production, attach a date/source when saying “current” unless the fact was just re-observed live.

**Drift risk:** Very high.

## Current-production pattern

**Reconciled usage:** The responsibility/behavior shape reconciled from the existing production runtime and used as the V5 parity source.

This does **not** mean every V5 hardening guard/receipt/recovery path already exists in production.

## V5 hardening

**Reconciled usage:** An explicit V5 guard, contract, receipt, recovery path, authority boundary, validation step, job/outbox treatment, or failure behavior added/refined beyond the production parity shape.

A `V5 HARDENING` label is not a production claim.

## Dogfood activation

**Reconciled usage:** Evidence that the controlled V5 test/dogfood deployment is operationally enabled/reachable. Code/CI success alone does not establish this tier.

## Governing controlled artifact

**Reconciled usage:** A versioned specification/control family that governs a material decision family. Public process documentation currently uses `CTRL-*` control-family identifiers.

**Important current gap:** The public docs can identify the control family, but V5 is not yet claimed to bind the exact `control_id + approved_revision` into every runtime PASS/FAIL decision receipt.

## Dyad

**Observed usage:** Twelve stackable cognitive nodes with activation and overrides (Feb 2026).

**Reconciled usage:** Explicit cognitive-state subsystem with global definitions/rules and per-user overrides.

**Drift risk:** Medium.

## Senate

**Observed usage:** Multiple advisory/deliberative implementations and seat rosters across snapshots.

**Reconciled usage**

Never draw “the Senate” with one timeless roster. Attach a roster to a source date/version and identify whether it describes an implementation, debate path, fallback path, or behavioral example.

Senate is advisory; advisory output does not inherit execution authority.

**Drift risk:** High.

## Thinker

**Observed usage:** Conversation observer plus between-session reflection daemon (Mar–May 2026), with later V5 background-worker reconstruction work.

**Reconciled usage:** Background/maintenance cognition responsibility. Existing-production activation and V5 code/test status are separate claims; do not infer one from the other.

**Drift risk:** High.

## Learning

**Observed usage:** Vocabulary, emotional, personality, preference, feedback, reflection, and candidate updates from Sep 2025 onward.

For a strong learning claim, identify:

1. signal source;
2. transformation/candidate logic;
3. persistence or state mutation;
4. active call site / worker;
5. whether downstream behavioral effect was actually exercised.

**Drift risk:** Very high.

## Proof Runtime

**Observed usage:** Standalone receipt-backed reference kernel.

**Reconciled usage:** Never call it a production Nexus subsystem. `v0.1.1` is a published security-hardening reference release, not a release candidate, security audit, or production certification.

**Drift risk:** High.

## Acceptance campaign

A framework execution can validly produce a target `FAIL`.

**Reconciled usage:** Separate campaign integrity from target outcome. A defect can produce a valid failure result while the acceptance campaign itself operated correctly and preserved evidence.

**Drift risk:** Medium.

## Process Architecture

**Reconciled usage:** The controlled public documentation system for how Nexus performs work: Request Watch, Value Stream, Master Process Map, linked process WIs, governing control families, and evidence-status references.

The map itself is documentation/navigation evidence. It does not promote itself into activation/durability evidence.

## Reading rules

Prefer:

- **code-backed / implemented** over **live** when only source evidence exists;
- **tested / exercised by a retained run** over **fully tested** when the exercise is bounded;
- **operational at the recorded date** over **durable** without lifecycle evidence;
- **V5 target reconstruction, code-backed/tested** over either **V5 release** or **merely aspirational V5 design** when using the current pinned evidence;
- **reference kernel** over **production subsystem** for bounded public projects;
- **evidence supports** over **proves** when logs or data are partial;
- **latest retained production audit as of DATE** over an undated “current production” claim.

These rules do not weaken the history. They make the strongest parts harder to dismiss.
