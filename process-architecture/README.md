# Nexus Synapse — Process Architecture

> **The model is not the system. The runtime is a process.**

This directory is the **canonical approved public record** for the Nexus Synapse process-architecture release set. Git history provides the public revision/provenance record. GitHub Pages renders interactive presentation artifacts; the private Drive binder remains the working/control workspace and backup/distribution surface.

## Start here

1. **[Watch Request Watch v0.6](https://chriscanadian.github.io/nexus-synapse-engineering-portfolio/)** — presentation-scale runtime journey with a Governance / Quality card that lights up per station.
2. **[Open the Value Stream](./diagrams/value-stream-v0.2.svg)** — compact main governed turn + async support lane.
3. **[Open the Monster v0.6](https://drive.google.com/file/d/101Sgnz2eD5c4zHYq49Hu-d2LBuDHmyAR/view)** — full public-safe decision/subprocess topology.
4. **[Use the 000 Scope / Process Index](./processes/000-GOVERNED-TURN.md)** — ISO-style process navigation.
5. **[Open the Governing Control Register](./controls/CONTROL_REGISTER.md)** — which public control family governs each material decision family.
6. **[Read Evidence Status](./EVIDENCE_STATUS.md)** — production-pattern, V5-code, V5-test, hardening, activation and traceability claim ceilings.

## Release rule

```text
PRIVATE CONTROLLED WORKING SOURCE
        ↓ reconcile / review
APPROVED PUBLIC-SAFE CONTENT
        ↓ controlled Git commit
CANONICAL PUBLIC GITHUB RECORD
        ↓ render
GITHUB PAGES / README / DISTRIBUTION COPIES
```

## v0.6 evidence + governance release

The Monster no longer treats governance as one central box. It also no longer asks the reader to guess whether a process family is merely documented, code-backed, tested, or production-derived. Each major family carries evidence-tier labels; the definitions and exact source snapshots are in **[Evidence Status](./EVIDENCE_STATUS.md)**. Governance is distributed across the actual authorization, inspection, release, fallback, retry and promotion decision trees. Major process families point to their applicable `CTRL-*` public control family.

Request Watch intentionally stays simple: a persistent Governance / Quality Control card lights up per active station and explains **what** is governed there.

### Critical claim ceiling

The documentation can identify the governing control family today. **V5 is not yet claimed to bind every PASS/FAIL decision receipt to an exact `control_id + approved_revision`.** That is a traceability requirement/gap until implemented and acceptance-tested.

## Storage model

Logical state owners do not imply separate subsystem databases. The architecture uses one canonical Nexus durable-state boundary for structured state. Derived indexes and artifact/object storage are shown separately only where they have distinct custody responsibilities.
