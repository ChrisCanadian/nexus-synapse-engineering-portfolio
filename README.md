# Nexus Synapse Engineering Portfolio

### From a stream overlay for my son to a model-agnostic AI runtime

> **The model is not the system.**  
> Nexus Synapse moves continuity, state, context, authority, tools, and evidence into an explicit runtime around interchangeable model inference.

<p align="center">
  <a href="https://raw.githack.com/ChrisCanadian/nexus-synapse-engineering-portfolio/gh-pages/index.html">
    <img src="assets/request-watch-readme.svg" width="960" alt="Animated Nexus Request Watch showing a request moving through runtime stations">
  </a>
</p>

<p align="center"><strong>Request Watch v0.4.1</strong> — a public-safe animated view of a request moving through Nexus. Click the animation for the live HTML version; the <a href="https://drive.google.com/file/d/1NIdSnrbs-ncfEuKrfl8tqVj_mFQYeIDY/view">MP4 playback</a> remains available in Drive.</p>

<p align="center">
  <a href="docs/PROCESS_ARCHITECTURE.md"><strong>Process Architecture</strong></a> ·
  <a href="https://drive.google.com/drive/folders/1IMBTV6jCgvny9R7cHaC7t3xDKwlNgdv6"><strong>Master Process Map</strong></a> ·
  <a href="https://drive.google.com/drive/folders/1nJfxZPd6GO68QfWrTiWQnSuNgLuDU_tj"><strong>Value Stream</strong></a> ·
  <a href="https://docs.google.com/document/d/1QNbGg-9jtjbGt7_wq3ZqSkKxTgRtAwcnGaudEHi7cN8/edit"><strong>000 Scope / Process Index</strong></a>
</p>

*The animation is an explanatory presentation artifact. Its timing is illustrative, not live runtime takt.*

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
2. **[Current Production Responsibilities](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)** — shortest current-architecture view.
3. **[Nexus Terminology → Conventional Systems Concepts](docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)** — translates project terms into conventional engineering concepts.
4. **[Production Evidence Status](docs/PRODUCTION_EVIDENCE_STATUS.md)** — what is production-inspected, isolated, reconstructed, historical, or not demonstrated.
5. **[Public Technical Reference v1.1](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)** — full current public-safe technical reference.

### I mostly want to see the system

Start with **[Public Process Architecture](docs/PROCESS_ARCHITECTURE.md)**, then browse the **[Visual Gallery](docs/NEXUS_VISUAL_GALLERY.md)**.

The process-architecture set includes Request Watch, the full Master Process Map, the compact Value Stream, and an ISO-style linked Process Library.

![Nexus Synapse visual tour](https://drive.google.com/uc?export=view&id=1OM2jeCOqsgvPKtwLNkFtp2cLGchtY7BY)

*Animated Nexus system tour. It is an orientation aid, not a literal runtime trace.*

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

For formal purpose/evidence/claim-ceiling language, see **[Public Repository and Artifact Map](docs/REPOSITORY_MAP.md)**.

Current validation status: the public Gateway and Router are released and tested at v0.2. A retained August 18, 2026 campaign against the existing Nexus deployment completed, but the fixed-invariant result **failed**: deterministic session mapping and all six persistence barriers were observed, while cross-conversation continuity and correction persistence failed. A separate unseen challenge passed. Those partial results do not convert the campaign into a pass, so no deployed-Nexus validation-pass claim is made.

---

## Where the public Nexus material lives

The public Nexus work is intentionally split by purpose. These surfaces are related, but they are **not interchangeable sources of truth**.

| Surface | What belongs there | Why it exists |
|---|---|---|
| **This engineering portfolio** | Current public-safe architecture, terminology translation, evidence status, case studies, visual orientation, and the canonical Markdown technical reference | Version-controlled engineering front door and public claim/evidence map |
| **[Public Process Architecture](docs/PROCESS_ARCHITECTURE.md)** | Request Watch, Master Process Map, Value Stream, linked Process Library, notation and publication boundary | Shows how Nexus performs work without publishing private implementation tolerances |
| **Seven public GitHub repositories** | Executable bounded artifacts, validation/infrastructure surfaces, and a historical reconstruction | Let specific responsibilities and historical lineage be inspected without publishing the private runtime |
| **Nexus Synapse Research Library (Google Sites)** | Long-form research, project history, explanatory material, visuals, and reader-friendly presentation copies | Research/presentation layer; it does **not** supersede the version-controlled engineering claims here |
| **`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`** | Current public-safe technical reference | Canonical, diffable source for the technical reference |
| **Rendered PDF / Drive technical reference** | Rendered export of the canonical Markdown | Distribution convenience; follows the repository source rather than replacing it |
| **Historical SSR gist** | Early Structured-SQL-RAG / warehouse-style retrieval lineage and historical benchmark material | Shows where part of the architecture came from; not the current SSR implementation |

Quick routing rule:

- **Want to see how a turn moves through Nexus?** Open [Public Process Architecture](docs/PROCESS_ARCHITECTURE.md).
- **Current architecture or evidence ceiling?** Stay in this portfolio.
- **Runnable/testable code for one bounded claim?** Open the corresponding public repository.
- **Longer narrative, history, or presentation material?** Use the Research Library.
- **Rendered technical document?** Use the PDF, but treat the Markdown source here as authoritative.

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

The **version-controlled Markdown file in this repository is the canonical public technical reference**:

- **Canonical source:** [`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
- **Rendered distribution copy:** [PDF in the Nexus Synapse Research Library / Drive](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view)

The current reference was reconciled against an **August 14, 2026 read-only inspection of the deployed production implementation and state**. Older July execution evidence remains useful, but is labeled as isolated production-target execution rather than silently treated as a current live-production trace.

The change-control rule is simple: **Markdown first, PDF second.** Architectural claim changes should be diffable in repository history before a new rendered export is published.

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
| **IMPLEMENTED** | Concrete executable code/schema materially represents the responsibility |
| **TESTED** | Assertion-bearing tests, retained runs, benchmarks, or audits support the claim |
| **DOCUMENTED / PLANNED** | The design is documented but evidence is insufficient for implemented/tested |
| **ARCHIVED / SUPERSEDED** | The path existed but was replaced, disabled, or is no longer authoritative |
| **LINEAGE-INFERRED** | The relationship was reconstructed across sources rather than stated contemporaneously |

![Nexus evidence-strength dashboard](https://drive.google.com/uc?export=view&id=1t_iO2oe8ZaH7BCGQwrX35v0pcVliOXxr)

*Visual orientation only. The version-controlled evidence pages remain authoritative if a visual and current text ever disagree.*

For the distinction between deployed inspection, isolated execution, public proof, and historical/reconstructed evidence, see **[Production Evidence Status](docs/PRODUCTION_EVIDENCE_STATUS.md)** and **[Sanitized Evidence Receipts](evidence/SANITIZED_EVIDENCE_RECEIPTS.md)**.

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
3. [`docs/NEXUS_OVERVIEW.md`](docs/NEXUS_OVERVIEW.md)
4. [`docs/NEXUS_VISUAL_GALLERY.md`](docs/NEXUS_VISUAL_GALLERY.md)
5. [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md)
6. [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md)
7. [`docs/VERIFICATION_AND_EVIDENCE.md`](docs/VERIFICATION_AND_EVIDENCE.md)

### AI / software / systems path

1. [`docs/PROCESS_ARCHITECTURE.md`](docs/PROCESS_ARCHITECTURE.md)
2. [`docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md`](docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)
3. [`docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md`](docs/NEXUS_TO_CONVENTIONAL_SYSTEMS_MAP.md)
4. [`docs/PRODUCTION_EVIDENCE_STATUS.md`](docs/PRODUCTION_EVIDENCE_STATUS.md)
5. [`docs/NEXUS_OVERVIEW.md`](docs/NEXUS_OVERVIEW.md)
6. [`docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md`](docs/reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
7. [`docs/ARCHITECTURAL_EVOLUTION.md`](docs/ARCHITECTURAL_EVOLUTION.md)
8. [`docs/VERIFICATION_AND_EVIDENCE.md`](docs/VERIFICATION_AND_EVIDENCE.md)
9. [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md)
10. [`case-studies/`](case-studies/) — including the [Memory Kernel case study](case-studies/memory-kernel.md), [Black-Box Validation + BYO Router case study](case-studies/blackbox-validation-and-byo-router.md), and [ChrisAI Runtime case study](case-studies/chrisai-runtime.md)
11. [`CREDITS_AND_ATTRIBUTION.md`](CREDITS_AND_ATTRIBUTION.md) — authorship, provenance operations, permission boundaries, and Moon Source reference lineage
12. [`docs/GLOSSARY.md`](docs/GLOSSARY.md)
13. [`evidence/claims-and-evidence.json`](evidence/claims-and-evidence.json)

---

## What I am not claiming

This portfolio does **not** claim:

- AGI or consciousness;
- that every historical Nexus subsystem is still active;
- that every implemented subsystem is fully tested;
- independent certification of the private runtime;
- that the retained August 18, 2026 deployed-target campaign passed the fixed-invariant suite;
- that isolated V5 reconstruction work is automatically the accepted production path;
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

- [Nexus Process Architecture — Public Releases](https://drive.google.com/drive/folders/1uhNpMfOIaJsdOmtT0EFw3HsYbiFiQtHU)
- [Public Process Architecture guide](docs/PROCESS_ARCHITECTURE.md)
- [Nexus Synapse Research Library](https://sites.google.com/view/nexus-synapse-research-library/home)
- [Historical SSR gist](https://gist.github.com/ChrisCanadian/7e9891eeadea9dc4cdfc2af7a4367752)
- [Christopher Campbell on GitHub](https://github.com/ChrisCanadian)
- [Credits and Attribution](CREDITS_AND_ATTRIBUTION.md)

---

## Status

This portfolio is a living engineering record.

Where current evidence changes, the intended practice is to update the **evidence label first**, then update the claim.

**Architecture can evolve. Evidence should remain traceable.**