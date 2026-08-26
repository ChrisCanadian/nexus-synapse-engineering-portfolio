# Nexus Synapse Engineering Portfolio

### From a stream overlay for my son to a model-agnostic AI runtime

> **The model is not the system.**  
> Nexus Synapse moves continuity, state, context, authority, tools, and evidence into an explicit runtime around interchangeable model inference.

<p align="center">
  <a href="https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/">
    <img src="assets/request-watch-readme.svg" width="960" alt="Animated Nexus Request Watch showing a request moving through runtime stations">
  </a>
</p>

<p align="center"><strong>Request Watch v0.6</strong> — a public-safe animated view of a request moving through Nexus. Click the animation for the live GitHub Pages version.</p>

<p align="center">
  <a href="docs/PROCESS_ARCHITECTURE.md"><strong>Process Architecture</strong></a> ·
  <a href="process-architecture/diagrams/master-process-map-v0.6.svg"><strong>Master Process Map</strong></a> ·
  <a href="process-architecture/diagrams/value-stream-v0.2.svg"><strong>Value Stream</strong></a> ·
  <a href="process-architecture/processes/000-GOVERNED-TURN.md"><strong>000 Scope / Process Index</strong></a> ·
  <a href="process-architecture/EVIDENCE_STATUS.md"><strong>Evidence Status</strong></a>
</p>

*The animation is an explanatory presentation artifact. Its timing is illustrative, not live runtime takt. In v0.6 the moving token is the WIP unit: station/detail/governance state changes after the token arrives.*

---

## The short version

I did not set out to build an AI runtime.

In August 2025, my son wanted to watch me stream games. That is what started the side project: I began building a custom overlay for streaming Rocket League, using GPT to help me write the code. As the overlay project grew, I kept running into the same limitations in the AI-assisted workflow: memory and continuity disappeared, tool use was constrained, and prompt/context limits forced me to rebuild information the model had already seen.

Instead of working around the same problems again, I asked a different question:

> **How would you start building an AI?**

On August 19, 2025, I created `bootstrap.py`. That experiment kept expanding as I tried to move more responsibility out of the prompt and into software I could inspect, persist, govern, and test.

That became Nexus Synapse.

The Rocket League overlay is still unfinished.

---

## What Nexus Synapse became — in plain English

A useful operating system does not expect one worker to remember every rule, every past event, every permission, every exception, every available tool, and every piece of evidence needed to prove the work happened.

The environment around the worker carries much of that responsibility.

Nexus applies a similar systems idea around a language model.

The model can interpret, reason, propose, and communicate. The surrounding runtime is responsible for things such as:

- who the current user/session is;
- what history and current state are relevant now;
- which rules and behavioral settings apply;
- which tools or actions are actually permitted;
- what should persist after the turn;
- what evidence supports a claim that something happened.

That is what I mean when I say:

> **The model is not the system.**

The analogy is not meant to treat an LLM as literally equivalent to a human worker. It is a way to make the responsibility split understandable using familiar systems thinking.

### The engineering definition

**Nexus Synapse is a continuity runtime that prepares, governs, extends, and preserves the operating environment around interchangeable model inference.**

At a public-safe level:

```text
authenticated request
        ↓
analysis + eligible continuity
        ↓
Structured State Reconstruction (SSR)
        ↓
behavior / capability / authority boundaries
        ↓
selected model inference
        ↓
optional governed tool execution
        ↓
deterministic checks
        ↓
persistence + adaptation + evidence
        ↓
response
```

If you only want the current production responsibility chain without the project's historical terminology, use **[Current Production Responsibilities — two-minute orientation](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)**.

---

## Choose your entry point

### I come from operations, manufacturing, logistics, quality, healthcare, finance, legal, research, or another domain

Start with **[Nexus Synapse for Domain Experts](docs/DOMAIN_EXPERT_ORIENTATION.md)**.

It explains the architecture through familiar ideas such as state, work instructions, permissions, handoffs, corrections, tools, approvals, traceability, and proof of completion before introducing Nexus terminology.

A useful question for this path is:

> **How do we make AI operate inside the rules, history, authority, and evidence requirements of real work?**

### I come from AI, software, systems engineering, or architecture

Start with:

1. **[Public Process Architecture](docs/PROCESS_ARCHITECTURE.md)** — see the governed runtime as a process before diving into the code/evidence surfaces.
2. **[Process Architecture Evidence Status](process-architecture/EVIDENCE_STATUS.md)** — separates production pattern, V5 code/test evidence, hardening, activation, durability and traceability claims.
3. **[Current Production Responsibilities](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)** — shortest current-production architecture view.
4. **[Nexus Terminology → Conventional Systems Concepts](docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)** — translates project terms into conventional engineering concepts.
5. **[Production Evidence Status](docs/PRODUCTION_EVIDENCE_STATUS.md)** — what is production-inspected, isolated, reconstructed, historical, or not demonstrated.
6. **[Public Technical Reference v1.1](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)** — public-safe technical reference; its production reconciliation date is stated inside the document.

### I mostly want to see the system

Start with **[Request Watch](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/)**, then **[Public Process Architecture](docs/PROCESS_ARCHITECTURE.md)** and the **[Visual Gallery](docs/NEXUS_VISUAL_GALLERY.md)**.

The process-architecture set includes Request Watch v0.6, the full Master Process Map v0.6, the compact Value Stream v0.2, an ISO-style linked Process Library, governing control families, and explicit evidence-tier labels.

![Nexus Synapse visual tour](https://drive.google.com/uc?export=view&id=1OM2jeCOqsgvPKtwLNkFtp2cLGchtY7BY)

*Older animated Nexus system tour retained as an orientation aid. It does not supersede Request Watch and is not a literal runtime trace.*

---

## Seven public repositories

Nexus Synapse itself remains private. These seven repositories expose bounded, inspectable responsibilities, validation surfaces, and one historical reconstruction from the larger body of work.

| Repository | In plain English | Engineering view |
|---|---|---|
| [**Nexus Proof Runtime**](https://github.com/ChrisCanadian/nexus-proof-runtime) | An AI saying "I did it" should not count as proof that the action actually happened. | Authorization → execution → receipt/artifact → claim verification. |
| [**Live Runtime Acceptance Rig**](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig) | A test returning "success" is not enough if the real target did not actually change. | Exercise a real boundary, verify durable effects, retain reviewable evidence. |
| [**Nexus Mode Card Creator**](https://github.com/ChrisCanadian/nexus-mode-card-creator) | Turn how you want an AI to behave into a reusable profile without pretending the profile grants system authority. | Guided authoring → clarification → human confirmation → portable behavioral artifact. |
| [**Nexus Memory Kernel**](https://github.com/ChrisCanadian/Nexus-Memory-Kernel) | Useful memory needs scope, corrections, history, and provenance — not just "remember everything." | Scoped persistence → recall → correction/supersession → provenance → bounded memory capabilities. |
| [**Nexus Black-Box Validation Gateway**](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway) | Let outsiders challenge a closed runtime without giving them the private runtime. | Public challenge contracts → opaque target → sanitized observable evidence. |
| [**OpenAI-compatible Router**](https://github.com/ChrisCanadian/OpenAI-compatible-router) | Change or supply the model/provider without rebuilding the application around it. | Reusable OpenAI-compatible BYO transport, model locks, streaming, tools pass-through, provider-safety controls, and usage readback. |
| [**ChrisAI Runtime**](https://github.com/ChrisCanadian/chrisai-runtime) | Run a historically grounded reconstruction of the flat-file runtime that preceded Nexus. | Evidence-constrained pre-database, pre-SSR reconstruction; not a modern Nexus extraction or byte-for-byte archive. |

These seven repositories are related by lineage, validation strategy, and design philosophy. They are **not public modules intended to be assembled into a copy of Nexus Synapse**.

For formal purpose/evidence/claim-ceiling language, see **[Public Repository and Artifact Map](docs/REPOSITORY_MAP.md)**. For the pinned heads used in the latest cross-repository reconciliation, see **[Current Public Snapshot](docs/CURRENT_PUBLIC_SNAPSHOT.md)**.

Current validation status: the public Gateway and Router are released and tested at v0.2. A retained August 18, 2026 campaign against the existing Nexus deployment completed, but the fixed-invariant result **failed**: deterministic session mapping and all six persistence barriers were observed, while cross-conversation continuity and correction persistence failed. A separate unseen challenge passed. Those partial results do not convert the campaign into a pass, so no deployed-Nexus validation-pass claim is made.

---

## Where the public Nexus material lives

The public Nexus work is intentionally split by purpose. These surfaces are related, but they are **not interchangeable sources of truth**.

| Surface | What belongs there | Why it exists |
|---|---|---|
| **This engineering portfolio** | Current public-safe architecture, terminology translation, evidence status, case studies, visual orientation, reconciliation controls, and the canonical Markdown technical reference | Version-controlled engineering front door and public claim/evidence map |
| **[`process-architecture/`](process-architecture/README.md)** | Canonical approved public Request Watch/Master/Value Stream documentation, linked Process Library, governing controls, evidence status, and release records | Git-addressable public process binder with exact revision history |
| **[GitHub Pages Request Watch](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/)** | Executable public presentation of Request Watch | Presentation layer; follows the version-controlled public release rather than replacing it |
| **Seven public GitHub repositories** | Executable bounded artifacts, validation/infrastructure surfaces, and a historical reconstruction | Let specific responsibilities and historical lineage be inspected without publishing the private runtime |
| **Nexus Synapse Research Library (Google Sites)** | Long-form research, project history, explanatory material, visuals, and reader-friendly presentation copies | Research/presentation layer; it does **not** supersede the version-controlled engineering claims here |
| **`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`** | Public-safe technical reference with its own stated reconciliation date | Canonical, diffable source for that technical-reference revision |
| **Rendered PDF / Drive copies** | Rendered exports, playback/distribution copies, and private working/control binder material | Distribution/working convenience; follows GitHub-approved public sources where applicable rather than replacing them |
| **Historical SSR gist** | Early Structured-SQL-RAG / warehouse-style retrieval lineage and historical benchmark material | Shows where part of the architecture came from; not the current SSR implementation |

Quick routing rule:

- **Want to watch how a turn moves through Nexus?** Open [Request Watch](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/).
- **Want the current approved process architecture?** Open the [`process-architecture/` binder](process-architecture/README.md).
- **Current production architecture or evidence ceiling?** Use the current-production/evidence documents in this portfolio.
- **What exists or is tested specifically in V5?** Use the pinned V5 snapshot and acceptance evidence referenced from [Process Architecture Evidence Status](process-architecture/EVIDENCE_STATUS.md).
- **Runnable/testable code for one bounded public claim?** Open the corresponding public repository.
- **Longer narrative, history, or presentation material?** Use the Research Library.

---

## How to evaluate Nexus terminology

Nexus accumulated its own subsystem names while the architecture evolved. Those names are useful for project history, but **the name itself is not the novelty claim**.

For outside evaluation, use this pattern:

```text
Nexus term
    ↓
closest conventional systems concept
    ↓
Nexus-specific responsibility / composition decision
    ↓
measured or retained evidence
```

A few examples:

| Nexus term | Closest conventional concept | The Nexus-specific question |
|---|---|---|
| **SSR** | Context assembly / state hydration / context compiler | What eligible operating state should be reconstructed before inference, and who owns that selection? |
| **CAG** | Session-context cache / rolling continuity buffer | How should bounded conversation continuity feed broader state reconstruction? |
| **Gauges** | Scalar behavioral/configuration controls | How can behavior intensity persist as runtime state without becoming identity or authority? |
| **Modes** | Behavioral policy/profile overlay | How can a temporary role alter behavior without replacing durable identity or granting execution rights? |
| **Senate** | Multi-agent / ensemble advisory | How can deliberation contribute context while remaining subordinate to runtime authority? |
| **Thinker** | Background worker / reflection daemon | Which cognition/maintenance responsibilities can run outside the immediate model call, and is that path actually active? |
| **Tool/capability execution** | Command dispatcher / capability gateway / authorization middleware | How do proposal, scope, authority, execution, evidence, and narration stay separate? |

If those terms are unfamiliar, that is expected. Start with the [Domain Expert Orientation](docs/DOMAIN_EXPERT_ORIENTATION.md) and come back to the terminology map later.

The full translation — including current caveats for Dyad/nodes, reflections, self-model, continuity, memory, Senate, and Thinker — is in **[Nexus Terminology → Conventional Systems Concepts](docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)**.

---

## Public technical reference: source of truth

The **version-controlled Markdown file in this repository is the canonical public technical reference for that revision**:

- **Canonical source:** [`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
- **Rendered distribution copy:** [PDF in the Nexus Synapse Research Library / Drive](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view)

The current reference states the deployed-production evidence date against which it was reconciled. Newer V5/process-architecture evidence does not silently rewrite the reference's historical evidence date; use [Process Architecture Evidence Status](process-architecture/EVIDENCE_STATUS.md) and [Current Public Snapshot](docs/CURRENT_PUBLIC_SNAPSHOT.md) for newer pinned V5/public-repository state.

The change-control rule is simple: **Markdown first, rendered copy second.** Architectural claim changes should be diffable in repository history before a new rendered export is published.

---

## Why this portfolio exists

The private Nexus runtime is large enough that publishing a sanitized copy would create a different problem:

> **What exactly is the public code supposed to demonstrate?**

Instead, I publish **bounded public proof/reference surfaces from a private runtime**.

```text
private parent runtime
        ↓
identify one architectural claim
        ↓
extract the smallest useful public surface
        ↓
state what it demonstrates
        ↓
state what it does NOT demonstrate
        ↓
test that surface independently
```

These artifacts are not fragments that combine to recreate Nexus. Each is a bounded public surface intended to make one architectural idea inspectable.

The newer black-box validation work adds a second pattern: expose the **challenge contract and observable evidence**, while keeping the private target's assembly logic opaque.

The Memory Kernel has its own portfolio case study: **[Nexus Memory Kernel](case-studies/memory-kernel.md)**.

The black-box validation strategy and reusable model transport are documented together here: **[Black-Box Validation Gateway + BYO Model Router](case-studies/blackbox-validation-and-byo-router.md)**.

The historical reconstruction class and its evidence ceiling are documented here: **[ChrisAI Runtime — Historical Reconstruction](case-studies/chrisai-runtime.md)**.

---

## Current SSR terminology

In current portfolio documentation, **SSR means Structured State Reconstruction**.

At a public-safe level, SSR is the runtime responsibility that reconstructs a bounded operating context from eligible state before inference. That can include identity/profile state, gauges, mode, user rules, learned preferences, selected continuity/memory, reflections, tool/capability facts, and optional advisory context.

In conventional systems language, the closest category is **context assembly / state hydration / context compilation**. What matters in Nexus is the responsibility boundary: the runtime owns eligibility and composition rather than expecting the generator to reconstruct trustworthy system state by itself.

Earlier Nexus documents used `SSR` in several related ways. One important historical ancestor used structured/SQL filtering to narrow memory candidates before semantic ranking. Those earlier meanings remain part of the engineering history, but they are not the default current expansion.

See the [Glossary](docs/GLOSSARY.md) and [conventional-systems map](docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md) for the terminology trail.

---

## Evidence discipline

A recurring engineering principle in Nexus is:

> **A model statement is not evidence that an external action occurred.**

That leads to a deliberate separation:

```text
proposal
   ≠
authority
   ≠
execution
   ≠
evidence
   ≠
narration
```

In plain language: **seeing something is not permission to act, saying something happened is not proof that it happened, and code existing is not proof that it is active in production.**

The portfolio uses evidence labels because code presence is not automatically a live-system claim.

| Label | Meaning |
|---|---|
| **DOCUMENTED** | Responsibility/design is recorded but no stronger evidence tier is implied |
| **CODE-BACKED / IMPLEMENTED** | Concrete executable code/schema materially represents the responsibility |
| **TESTED / EXERCISED** | Assertion-bearing tests, retained runs, benchmarks, or audits support the claim |
| **ACTIVATED / DEPLOYED** | Evidence shows the path is operationally enabled/reachable in the identified environment |
| **DURABLE / SUSTAINED** | Evidence shows relevant state/effects survive the required lifecycle/restart/time boundary |
| **INDEPENDENTLY VERIFIED** | An applicable external/independent validation event supports the bounded claim |
| **ARCHIVED / SUPERSEDED** | The path existed but was replaced, disabled, or is no longer authoritative |
| **LINEAGE-INFERRED** | The relationship was reconstructed across sources rather than stated contemporaneously |

A higher tier is not inferred from a lower tier. The formal cadence and correction rules are in **[Reconciliation and Publication Control](docs/RECONCILIATION_CONTROL.md)**.

![Nexus evidence-strength dashboard](https://drive.google.com/uc?export=view&id=1t_iO2oe8ZaH7BCGQwrX35v0pcVliOXxr)

*Visual orientation only. The version-controlled evidence pages remain authoritative if a visual and current text ever disagree.*

For the distinction between deployed inspection, isolated execution, public proof, and historical/reconstructed evidence, see **[Production Evidence Status](docs/PRODUCTION_EVIDENCE_STATUS.md)**, **[Process Architecture Evidence Status](process-architecture/EVIDENCE_STATUS.md)** and **[Sanitized Evidence Receipts](evidence/SANITIZED_EVIDENCE_RECEIPTS.md)**.

---

## Architectural evolution

Nexus did not evolve through one clean sequence of perfectly named product releases. Production, recovery, reconstruction, and proof work sometimes moved in parallel.

The strongest through-line is simpler:

> **Responsibility progressively moved out of the language model and into explicit runtime systems whose state and behavior could be inspected, persisted, challenged, and tested.**

![Nexus architectural evolution timeline](https://drive.google.com/uc?export=view&id=16Ir4bMmUlz7Rqkrj5hT1r3HjeyWlMRfo)

*Chronological/architectural synthesis, not a literal current production deployment graph.*

Read the deeper history in [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md).

---

## Public / private boundary

This repository is designed to explain Nexus **without making the private runtime reproducible**.

Public material may include high-level architecture, historical design artifacts, public-safe diagrams, evidence categories, sanitized case studies, bounded reference implementations, public challenge contracts, and public benchmarks where the test conditions can be explained.

Intentionally excluded:

- production database schemas/table structures;
- exact production SQL/query patterns;
- raw SSR contents, ordering, thresholds, selection rules, and weighting logic;
- private prompts and identity-composition mechanics;
- production tool wiring/internal APIs;
- private black-box target adapters that translate public challenge requests into Nexus internals;
- deployment scripts, environment configuration, infrastructure paths, and runbooks;
- credentials, secrets, private endpoints, customer configuration, or user data;
- production conversations, memories, reflections, raw traces, or private logs.

See [`PUBLIC_BOUNDARY.md`](PUBLIC_BOUNDARY.md).

---

## About me

I am **Christopher Campbell**, an independent AI systems builder and logistics analyst based in Ontario, Canada. My professional background is logistics, warehouse/operations systems, SQL, ERP workflows, process improvement, quality thinking, and automation rather than computer science.

My path into this work looks roughly like this:

```text
warehouse / shipping operations
        ↓
ERP + SQL + process automation
        ↓
systems and quality thinking
        ↓
AI-assisted Python development
        ↓
Nexus Synapse
```

That background is not incidental to the architecture. Flow, state, ownership, handoffs, permissions, traceability, failure modes, and proof of completion are the concepts I already knew before I knew the AI terminology for them.

AI coding tools have been implementation partners for syntax, debugging, review, and exploration. The architecture, problem selection, operating concepts, acceptance criteria, and system-level decisions are the work documented here.

Nexus is my first Python project.

More: [`ABOUT_CHRIS.md`](ABOUT_CHRIS.md)

---

## Recommended reading paths

### Domain / operations path

1. [`docs/DOMAIN_EXPERT_ORIENTATION.md`](docs/DOMAIN_EXPERT_ORIENTATION.md)
2. [`docs/PROCESS_ARCHITECTURE.md`](docs/PROCESS_ARCHITECTURE.md)
3. [`process-architecture/processes/000-GOVERNED-TURN.md`](process-architecture/processes/000-GOVERNED-TURN.md)
4. [`docs/NEXUS_OVERVIEW.md`](docs/NEXUS_OVERVIEW.md)
5. [`docs/NEXUS_VISUAL_GALLERY.md`](docs/NEXUS_VISUAL_GALLERY.md)
6. [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md)
7. [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md)
8. [`docs/VERIFICATION_AND_EVIDENCE.md`](docs/VERIFICATION_AND_EVIDENCE.md)

### AI / software / systems path

1. [`docs/PROCESS_ARCHITECTURE.md`](docs/PROCESS_ARCHITECTURE.md)
2. [`process-architecture/EVIDENCE_STATUS.md`](process-architecture/EVIDENCE_STATUS.md)
3. [`docs/CURRENT_PUBLIC_SNAPSHOT.md`](docs/CURRENT_PUBLIC_SNAPSHOT.md)
4. [`docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md`](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)
5. [`docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md`](docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)
6. [`docs/PRODUCTION_EVIDENCE_STATUS.md`](docs/PRODUCTION_EVIDENCE_STATUS.md)
7. [`docs/NEXUS_OVERVIEW.md`](docs/NEXUS_OVERVIEW.md)
8. [`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
9. [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md)
10. [`docs/VERIFICATION_AND_EVIDENCE.md`](docs/VERIFICATION_AND_EVIDENCE.md)
11. [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md)
12. [`case-studies/`](case-studies/) — including the [Memory Kernel case study](case-studies/memory-kernel.md), [Black-Box Validation + BYO Router case study](case-studies/blackbox-validation-and-byo-router.md), and [ChrisAI Runtime case study](case-studies/chrisai-runtime.md)
13. [`CREDITS_AND_ATTRIBUTION.md`](CREDITS_AND_ATTRIBUTION.md) — authorship, provenance operations, permission boundaries, and Moon Source reference lineage
14. [`docs/GLOSSARY.md`](docs/GLOSSARY.md)
15. [`evidence/claims-and-evidence.json`](evidence/claims-and-evidence.json)

---

## What I am not claiming

This portfolio does **not** claim:

- AGI or consciousness;
- that every historical Nexus subsystem is still active;
- that every implemented subsystem is fully tested;
- independent certification of the private runtime;
- that the retained August 18, 2026 deployed-target campaign passed the fixed-invariant suite;
- that V5 code/test evidence automatically means controlled dogfood activation, sustained durability, or production deployment;
- that the public Proof Runtime, Memory Kernel, Acceptance Rig, Validation Gateway, Router, or ChrisAI reconstruction reproduces the private parent system;
- that public artifacts are complete representations of Nexus Synapse;
- that receipt/hash verification establishes semantic truth;
- that Nexus invented memory, RAG, tool use, agent frameworks, multi-agent debate, authorization middleware, background workers, behavioral configuration, context engineering, or OpenAI-compatible routing;
- that a Nexus subsystem name is a novelty claim by itself.

The point is narrower:

**document the architecture I built, translate its project vocabulary into terms both domain experts and outside engineers can evaluate, show how it evolved, publish inspectable pieces where appropriate, and attach claims to the strongest evidence I actually have.**

---

## Research and public artifacts

### Seven public repositories

- [Nexus Proof Runtime](https://github.com/ChrisCanadian/nexus-proof-runtime)
- [Live Runtime Acceptance Rig](https://github.com/ChrisCanadian/Live-Runtime-Acceptance-Rig)
- [Nexus Mode Card Creator](https://github.com/ChrisCanadian/nexus-mode-card-creator)
- [Nexus Memory Kernel](https://github.com/ChrisCanadian/Nexus-Memory-Kernel)
- [Nexus Black-Box Validation Gateway](https://github.com/ChrisCanadian/nexus-blackbox-validation-gateway)
- [OpenAI-compatible Router](https://github.com/ChrisCanadian/OpenAI-compatible-router)
- [ChrisAI Runtime](https://github.com/ChrisCanadian/chrisai-runtime)

### Supporting public material

- [Canonical Public Process Architecture binder](process-architecture/README.md)
- [Live Request Watch](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/)
- [Public Process Architecture guide](docs/PROCESS_ARCHITECTURE.md)
- [Current Public Snapshot](docs/CURRENT_PUBLIC_SNAPSHOT.md)
- [Reconciliation and Publication Control](docs/RECONCILIATION_CONTROL.md)
- [Nexus Synapse Research Library](https://sites.google.com/view/nexus-synapse-research-library/home)
- [Historical SSR gist](https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752)
- [Christopher Campbell on GitHub](https://github.com/ChrisCanadian)
- [Credits and Attribution](CREDITS_AND_ATTRIBUTION.md)

---

## Status

This portfolio is a living engineering record governed by **[Reconciliation and Publication Control](docs/RECONCILIATION_CONTROL.md)**.

Where current evidence changes, update the evidence status/claim ceiling first, then update the dependent summary. The latest pinned cross-repository reconciliation is recorded in **[Current Public Snapshot](docs/CURRENT_PUBLIC_SNAPSHOT.md)**.

**Architecture can evolve. Evidence should remain traceable.**
