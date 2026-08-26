# Nexus Synapse — Visual Gallery

This page is intentionally visual-first.

The portfolio documents and evidence files remain the claim-bearing source. These graphics are **orientation aids**: they show Nexus as a system, its history, and its engineering philosophy without reducing the project to the public repositories extracted from it.

## Request Watch — watch the runtime move

<p align="center">
  <a href="https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/">
    <img src="../assets/request-watch-readme.svg" width="960" alt="Animated Nexus Request Watch showing a request moving through runtime stations">
  </a>
</p>

*Request Watch v0.6. Click the animation for the live GitHub Pages version. Its timing is illustrative, not live runtime takt. The moving token is the WIP unit; station/detail/governance state changes after arrival so the viewer has one unambiguous active station.*

The current process-architecture release set gives three complementary views:

- **[Master Process Map v0.7](../process-architecture/diagrams/https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/master-process-map-v0.7.svg)** — the deliberately monstrous full topology, including governing control families, material decision trees, and evidence-tier badges.
- **[Value Stream v0.2](../process-architecture/diagrams/value-stream-v0.2.svg)** — compact governed-turn + WIP/outbox + async-support view.
- **[000 — Governed Turn — Scope & Process Index](../process-architecture/processes/000-GOVERNED-TURN.md)** — ISO-style hyperlink navigation through the eight process families.

For notation, governing controls, evidence tiers, publication boundaries, and the public/private release model, see **[Public Process Architecture](PROCESS_ARCHITECTURE.md)** and the **[canonical GitHub process binder](../process-architecture/README.md)**.

## Process-architecture evidence rule

The Monster is a navigation/documentation artifact; it does not promote itself into runtime evidence. v0.6 therefore shows separate evidence classes such as **CURRENT-PROD PATTERN**, **V5 CODE-BACKED**, **V5 ACCEPTANCE-TESTED**, and **V5 HARDENING**, while keeping staging activation/durability as a separate operational claim.

See **[Process Architecture Evidence Status](../process-architecture/EVIDENCE_STATUS.md)**.

## Animated system tour

![Nexus animated system tour](https://drive.google.com/uc?export=view&id=1OM2jeCOqsgvPKtwLNkFtp2cLGchtY7BY)

*Quick Nexus-only visual tour. This older presentation animation is retained as an orientation aid and should not be read as a literal runtime execution trace or as superseding Request Watch.*

## Architectural evolution

![Nexus architectural evolution timeline](https://drive.google.com/uc?export=view&id=16Ir4bMmUlz7Rqkrj5hT1r3HjeyWlMRfo)

A chronological synthesis of the major architectural shifts. Use the [Architectural Evolution](ARCHITECTURAL_EVOLUTION.md) document for the evidence labels and limitations behind the timeline.

## Runtime authority shift

![Nexus runtime authority shift](https://drive.google.com/uc?export=view&id=1iqL3Gjzn6ljr1nto5KRbW5EHL9Mr6Om6)

A visual explanation of the movement from model-owned implication toward explicit runtime-owned responsibility, authority, persistence, and verification.

## Subsystem lineage

![Nexus subsystem lineage](https://drive.google.com/uc?export=view&id=1XZVhB3NE5aN1XV-ryNgX4BiNsVEBg_jy)

A lineage map showing how subsystem responsibilities split, changed, and converged. Historical lineage is not the same thing as the current deployed call graph.

## Verification maturity

![Nexus verification maturity map](https://drive.google.com/uc?export=view&id=1oH06oBn2Kk8ffKBqP2W1-7L2dLRAdnKy)

The evolution from exploratory testing toward assertion-bearing tests, commit-addressed CI, durable-state acceptance, and receipt/artifact verification.

## Branch continuity

![Nexus branch continuity map](https://drive.google.com/uc?export=view&id=183BQFx1pZeR_zGczZTn0XJ2CNO18J8qe)

Useful for understanding why production, recovery, reconstruction, and public proof work should not be flattened into one linear “version” story.

## Warehouse/logistics-to-runtime translation

![Warehouse logistics to runtime](https://drive.google.com/uc?export=view&id=1U4UtSyGJTsp-JjLelmoHFpXe27Raz5G7)

The systems-thinking bridge behind much of Nexus: scope the work, identify eligible state, assemble the right context, execute through controlled boundaries, and verify the result.

## Research program overview

![Nexus research program overview](https://drive.google.com/uc?export=view&id=1dPQGztAmgwjkFyx3y3faBgENpmtfz5bR)

A broader view of the research and evaluation surfaces around Nexus Synapse.

## Evidence-strength dashboard

![Nexus evidence strength dashboard](https://drive.google.com/uc?export=view&id=1t_iO2oe8ZaH7BCGQwrX35v0pcVliOXxr)

This dashboard is a visual orientation aid for the portfolio's evidence vocabulary. If a visual label ever conflicts with a current evidence page, the version-controlled text wins.

---

## Start with the text behind the pictures

- [Public Process Architecture](PROCESS_ARCHITECTURE.md)
- [Process Architecture Evidence Status](../process-architecture/EVIDENCE_STATUS.md)
- [Current Public Snapshot](CURRENT_PUBLIC_SNAPSHOT.md)
- [Reconciliation and Publication Control](RECONCILIATION_CONTROL.md)
- [Current Production Responsibilities](CURRENT_PRODUCTION_RESPONSIBILITIES.md)
- [Production Evidence Status](PRODUCTION_EVIDENCE_STATUS.md)
- [Architectural Evolution](ARCHITECTURAL_EVOLUTION.md)
- [Verification and Evidence](VERIFICATION_AND_EVIDENCE.md)
- [Canonical Public Technical Reference](reference/NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md)
