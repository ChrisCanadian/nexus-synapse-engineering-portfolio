# Public Repository and Artifact Map

This page explains how the public Nexus-related artifacts fit together without implying that they are deployed as one public system.

For a fuller domain-first explanation, see [Nexus Synapse for Domain Experts](DOMAIN_EXPERT_ORIENTATION.md). For the exact heads used in the latest reconciliation, see [Current Public Snapshot](CURRENT_PUBLIC_SNAPSHOT.md).

## Public bounded repositories

| Repository | Public purpose | Relationship to Nexus | Current public status / claim ceiling |
|---|---|---|---|
| [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime) | Receipt-backed execution/evidence reference kernel | Extracts a mature control principle into a standalone public project | `v0.1.1` published security-hardening reference release. Implemented/tested as its own repository; not a third-party security audit, production certification, or proof of the full Nexus execution path. |
| [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | Safe real-boundary acceptance framework with durable readback and evidence bundles | Encodes verification discipline that emerged during Nexus development | `v0.1.1` released/tested as its own framework. Framework execution success does not itself certify Nexus or convert a system-specific failed invariant into PASS. |
| [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Guided conversion of fuzzy behavioral intent into a portable Mode Card | Bounded extraction of behavioral-mode authoring work | Public creator contract is implemented/tested. It deliberately stops before private activation, weighting, persistence, SSR integration, authority, or identity composition. |
| [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) | Scoped persistent memory, recall, correction/supersession, provenance, and memory-capability execution | Bounded reference extraction of memory responsibility/authority patterns | `v0.1.0` public implementation with capability/isolation/persistence/temporal/semantic-scope tests. Does not expose production schemas/queries, private SSR memory composition, or the general Nexus runtime. |
| [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway) | Public challenge boundary for opaque targets with sanitized evidence envelopes | Allows selected private-runtime claims to be challenged without exposing private composition | `v0.2` public implementation/CI. August 18 deployed-target fixed-invariant campaign remains **FAILED**; a separate unseen challenge passed. Partial observations do not become a deployed-Nexus validation pass. |
| [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router) | Reusable short-lived BYO provider routing with model locks, streaming, tool pass-through and provider-safety controls | Generic inference transport supporting validation/provider portability without Nexus composition logic | `v0.2` public implementation/tests. Independent infrastructure only; use in one campaign does not establish provider parity or Nexus validation. |
| [ChrisAI Runtime](https://github.com/ChrisCanadian/chrisai-runtime) | Runnable historical reconstruction of the early flat-file, pre-database, pre-SSR ChrisAI architecture | Historical predecessor/lineage evidence, not a current Nexus extraction | `v0.1.0` reconstruction line constrained by surviving evidence. Not a byte-for-byte original checkout and not evidence of modern/deployed Nexus internals. |

## Public documentation / process artifacts

| Artifact | Purpose | Authority / claim ceiling |
|---|---|---|
| [Process Architecture binder](../process-architecture/README.md) | Canonical approved public Request Watch/Master/Value Stream documentation, linked WIs, governing controls and evidence status | Git history is the canonical public process-documentation revision record. The map itself is documentation/navigation evidence; its badges point to separately pinned production/V5 evidence. |
| [Request Watch v0.6](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/) | Presentation-scale animated view of the governed turn with active responsibilities and per-station Governance / Quality Control | Explanatory presentation artifact; timing is illustrative, not live runtime takt. |
| [Master Process Map v0.7](../https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/master-process-map-v0.7.html) | Full public-safe process topology including decision trees, control families, evidence tiers, WIP/custody and rework | Does not itself prove activation/durability. `CURRENT-PROD PATTERN`, `V5 CODE-BACKED`, `V5 ACCEPTANCE-TESTED`, etc. are defined in the linked evidence status. |
| [Value Stream v0.2](../process-architecture/diagrams/value-stream-v0.2.svg) | Compact Lean/process projection of the main governed turn and async support lane | No fabricated live takt, WIP count or queue-age metrics. |
| [Historical SSR gist](https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752) | Historical Structured-SQL-RAG / warehouse-style context-selection demonstration | Historical lineage/benchmark material; not current SSR and not a current production implementation claim. |
| [Nexus Synapse Research Library](https://sites.google.com/view/nexus-synapse-research-library/home) | Long-form public research, history and explanatory/presentation material | Research/presentation surface; does not supersede version-controlled engineering claims. |
| [Public Technical Reference v1.1](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md) | Public-safe technical responsibility/evidence reference | Canonical Markdown for that reference revision; its stated production reconciliation date remains part of its evidence ceiling. Newer V5/process evidence lives in the current process/snapshot documents rather than silently rewriting the historical date. |
| This portfolio | Curated map of current public-safe engineering claims, evidence, process architecture and public artifacts | Public engineering front door; does not make the private runtime reproducible. |

## Why separate repositories?

The private Nexus parent runtime is intentionally not being reduced to one sanitized public monolith.

Instead, public work is extracted around a narrow question:

```text
What claim are we trying to make inspectable?
        ↓
What is the smallest useful public artifact that demonstrates it?
        ↓
What evidence supports that artifact?
        ↓
What does it explicitly NOT establish?
```

That keeps each artifact falsifiable and easier to review.

The black-box validation work adds another pattern:

```text
public challenge contract
        ↓
opaque target boundary
        ↓
observable behavior / evidence
```

The challenge surface can be public while the target's private composition remains undisclosed.

## Artifact classes

- **Reference kernel:** small executable implementation of one control/responsibility pattern. Examples: Proof Runtime, Memory Kernel.
- **Acceptance framework:** reusable framework for exercising a real boundary and retaining evidence. Example: Live Runtime Acceptance Rig.
- **Black-box validation surface:** public challenge/evidence boundary around an opaque target. Example: Black-Box Validation Gateway.
- **Reusable infrastructure:** generic integration infrastructure without Nexus-specific composition logic. Example: OpenAI-compatible Router.
- **Authoring surface:** bounded creator that ends before private runtime consequence/activation. Example: Mode Card Creator.
- **Historical reconstruction:** modern executable artifact constrained by surviving historical evidence. Example: ChrisAI Runtime.
- **Historical artifact:** retained earlier implementation/benchmark showing lineage rather than current architecture. Example: SSR gist.
- **Process/documentation surface:** diagrams, WIs, terminology, evidence-status and research material used to understand/evaluate the architecture.

## Important

These artifacts are related by lineage, validation strategy, and design philosophy. They are **not** presented as a set of public modules that can be assembled into the private Nexus Synapse runtime.

The Black-Box Validation Gateway's retained August 18, 2026 campaign observed deterministic session mapping and all six persistence barriers, but the fixed invariants still failed: cross-conversation continuity was displaced by a blocked memory-tool result, and correction persistence lost the replacement value during extractive summarization. A separate unseen challenge passed through all-session CAG. The failed fixed-invariant outcome remains controlling; deployed Nexus is not presented as having passed that validation campaign.

The public Process Architecture v0.6 separately documents the V5 target flow and evidence tiers. It does not overwrite current-production evidence, and V5 code/test evidence does not automatically imply staging activation, durability, or production deployment.

For reconciliation cadence and source routing, see [Reconciliation and Publication Control](RECONCILIATION_CONTROL.md).
