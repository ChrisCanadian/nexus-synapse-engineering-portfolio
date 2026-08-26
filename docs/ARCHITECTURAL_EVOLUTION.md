# Architectural Evolution — Nexus Synapse

This page adapts the existing **public-safe Architectural Epochs** record into repository Markdown. It preserves the named epochs, design problems, and public evidence language while omitting private APIs, schemas, deployment specifics, and reproducibility-sensitive internals.

![Nexus architectural evolution timeline](https://drive.google.com/uc?export=view&id=16Ir4bMmUlz7Rqkrj5hT1r3HjeyWlMRfo)

*Public evolution map showing concurrent research arcs and subsystem development. It is an architectural synthesis, not a literal deployment topology. Where this older visual conflicts with current process/evidence text, the version-controlled text wins.*

## Before Epoch A — the stream-overlay side project

Nexus did not begin as an AI-runtime project.

In August 2025, Chris's son wanted to watch him stream games. That prompted a custom OBS overlay project for streaming Rocket League, built with GPT assisting the implementation. Repeated friction around memory/continuity, context limits, and constrained tool use changed the question from "how do I finish this overlay?" to:

> **How would you start building an AI?**

On August 19, 2025, `bootstrap.py` was created. That is the concrete start of the code lineage that became Nexus Synapse.

The overlay itself remained unfinished.

## Epoch A — ChrisAI bootstrap (Aug–Sep 2025)

**Problem:** Can a single integrated engine provide personalized assistance with memory, learning, and multimodal capabilities?

**Key characteristics**

- Monolithic engine combining persona, memory, learning, providers, safety, and images.
- Responsibilities discovered before they were separated.

**Evidence state:** `DOCUMENTED / ARCHIVED`; supported by later local inspection and the bounded ChrisAI historical reconstruction.

**Architectural significance:** Not modularity, but responsibility discovery. Most later Nexus concerns existed in rough form before they were separated.

## Epoch B — Engine2_1 subsystem expansion (Sep–Oct 2025)

**Problem:** How do we make the discovered responsibilities visible, testable, and independently evolvable?

**Key characteristics**

- 350+ Python files, 45+ core modules, and 80+ test files in the retained historical inventory.
- Separate areas for orchestration, personality, memory, emotion, routing, multimodal processing, and project support.
- The runtime already owned model selection, memory storage, personality records, and task routing.

**Architectural significance:** Responsibilities became named subsystems rather than implicit behaviors. Consolidation and cleanup became part of the architecture rather than an afterthought.

## Epoch C — Original SSR and retrieval (Nov–Dec 2025)

**Problem:** How do we prevent the model from receiving an undifferentiated memory blob and make context selection query-dependent?

**Key characteristics**

- SQL-guided candidate filtering before semantic ranking.
- Personality and memory selection became context-conditioned.
- Comparative 60-prompt benchmark work against a bare-model path.

**Architectural significance:** The runtime determined eligible scope and selected context first. The model received a curated, scoped context rather than everything.

The retained public warehouse-style SSR gist is a historical artifact from this lineage. It should not be treated as documentation of the current private SSR implementation.

## Epoch D — SSR_Minimal extraction (Jan 2026)

**Problem:** Can the most valuable runtime responsibilities be extracted into a simpler, cleaner orchestration path?

**Key characteristics**

- Clean-sheet extraction from the larger framework.
- Structured prompt/context assembly around identity, capabilities, profile, tools, and context.
- Three-role prompt placement became an architectural control.
- Trait Architecture V2 separated constants, gauges, learned preferences, and session context.

**Architectural significance:** Identity became explicit state rather than one static system string. Prompt construction became composable and testable.

## Epoch E — Dyad cognitive state (Feb 2026)

**Problem:** Can cognitive functions such as attention, curiosity, and caution be made explicit, configurable, and testable?

**Key characteristics**

- Twelve cognitive nodes with thresholds and activation logic.
- Global definitions with per-user overrides.
- Node-specific prompt projection.

**Architectural significance:** Cognitive profile became runtime data rather than hard-coded behavior. A rejected single-node design was superseded by multi-node coordination.

## Epoch F — Senate and Thinker (Mar–Apr 2026)

**Problem:** Can multi-model deliberation and between-session reflection be added without breaking baseline chat?

**Key characteristics**

- Senate: specialized advisory model calls with scoped/per-seat context.
- Thinker: conversation observation and between-session reflection.
- Both were designed as advisory lanes; baseline chat could continue on failure.

**Architectural significance:** Distributed cognition became fault-tolerant advisory support, not a replacement orchestrator.

## Epoch G — Production continuity and recovery (Apr–May 2026)

**Problem:** Does “implemented” mean “actually running in production”? What breaks under real operational conditions?

**Key characteristics**

- Verified production source snapshots and recovery work.
- Broader parity source, tests, docs, and repair records existed on separate recovery paths.
- Operational incidents demonstrated cases where local health could pass while live parity/routing still failed.
- Temporary repairs and durable deployment were treated as different evidence states.

**Architectural significance:** Operational evidence became part of the architecture.

```text
code presence ≠ activation ≠ durability
```

## Epoch H — V5 target reconstruction (Jul–Aug 2026)

**Problem:** Can the runtime be reconstructed with more explicit boundaries, typed events, evidence gates, recovery behavior, and deployment discipline while preserving the functional heart of the production system?

**Key characteristics**

- Separate V5 reconstruction repository/branch family, intended to become the target Nexus runtime rather than remain a permanent parallel architecture.
- Production responsibilities used as the parity/behavioral source; V5 rebuilds them behind clearer owned contracts.
- Memory relevance/scope repairs, explicit tool/job/artifact boundaries, receipt/provenance work, correction/validation controls, and deployment hardening.
- Container/CI, behavioral/failure, event-contract, migration, deployment-image, Compose and single-writer checks provide code/test evidence on the pinned reconstruction line.
- Controlled dogfood activation, sustained durability, and production replacement remain separate operational evidence claims.

**Architectural significance:** V5 is no longer best summarized merely as “an isolated experiment.” The public evidence supports a **target reconstruction that is code-backed and acceptance-tested**, while still refusing to infer deployment activation/durability from those lower evidence tiers.

See [Process Architecture Evidence Status](../process-architecture/EVIDENCE_STATUS.md) and [Current Public Snapshot](CURRENT_PUBLIC_SNAPSHOT.md) for the pinned current evidence boundary.

## Epoch I — Proof, validation, and bounded public surfaces (Jul–Aug 2026)

**Problem:** Can mature Nexus control, authoring, memory, portability, validation, and historical patterns be made independently inspectable without publishing the private parent runtime?

The public corpus developed into several deliberately different artifact classes:

- **Nexus Proof Runtime** — receipt-backed execution/evidence reference kernel.
- **Live Runtime Acceptance Rig** — protected-state, live-boundary acceptance framework.
- **Nexus Mode Card Creator** — bounded behavioral-profile authoring surface that stops before private activation/integration.
- **Nexus Memory Kernel** — bounded scoped-memory/correction/provenance/capability reference kernel.
- **Nexus Black-Box Validation Gateway** — public challenge boundary around an opaque target.
- **OpenAI-compatible Router** — generic short-lived BYO-provider infrastructure used by validation and portability work.
- **ChrisAI Runtime** — evidence-constrained historical reconstruction of the flat-file predecessor architecture.

These projects were not created as modules to combine into Nexus. They expose separate claims, contract boundaries, validation responsibilities, or lineage evidence.

**Architectural significance:** Public proof evolved from “show some code” into a controlled publication strategy:

```text
private parent responsibility / historical claim
        ↓
define a narrow public question
        ↓
build or retain the smallest inspectable surface
        ↓
state evidence + claim ceiling
        ↓
keep private composition private
```

The August 18 black-box campaign also reinforced another principle: **the validation mechanism can work correctly while the tested target legitimately fails.** The fixed-invariant failure remains part of the public evidence record.

## Epoch J — Process architecture and controlled public reconciliation (Aug 2026)

**Problem:** How do we make the whole runtime understandable without collapsing it into a component diagram or overstating what a diagram proves?

**Key characteristics**

- Request Watch for presentation-scale turn flow.
- Lean-style Value Stream for the dominant governed work path and async support lane.
- Master Process Map (“the Monster”) for decision trees, forks/joins, queues/WIP, custody, governing control families and evidence tiers.
- ISO-style `000` Scope / Process Index with linked process WIs.
- `CTRL-*` governing controlled-artifact families for material decision families.
- GitHub as canonical approved public process record; Pages as presentation layer; Drive as working/distribution/backup surface.
- Formal reconciliation control: change-triggered, weekly drift scan, monthly full reconciliation, and pre-release gate.

**Architectural significance:** The documentation itself began following the same responsibility/evidence discipline as the runtime. A process map is treated as navigation/documentation evidence; separate badges and snapshots identify the production pattern, V5 code/test evidence, hardening, activation boundary, and remaining traceability gaps.

## The through-line

Across the public epoch record:

1. A responsibility starts as implicit model behavior.
2. It becomes explicit runtime state or service.
3. It is scoped, tested, and governed.
4. Evidence is required to support claims about it.
5. Public documentation is reconciled to the evidence tier rather than allowed to silently become timeless.

That is the central architectural progression.

```text
model-centered behavior
        ↓
runtime-selected state
        ↓
explicit scope and policy
        ↓
bounded execution
        ↓
receipts / durable evidence
        ↓
acceptance and claim verification
        ↓
controlled public reconciliation
```

The arrow is not a claim that model-mediated cognition disappeared.

The change is that fluent model output progressively ceased to be sufficient authority for identity, memory, consequence, or completion.

## Evidence note

The history does **not** represent a formal `V1 → V5` release train. Named epochs are preferred because production, recovery, reconstruction, proof work, and public documentation sometimes proceeded in parallel.

For terminology rules, see [GLOSSARY.md](GLOSSARY.md). For the testing lineage, see [VERIFICATION_AND_EVIDENCE.md](VERIFICATION_AND_EVIDENCE.md). For the current pinned public state, see [CURRENT_PUBLIC_SNAPSHOT.md](CURRENT_PUBLIC_SNAPSHOT.md).
