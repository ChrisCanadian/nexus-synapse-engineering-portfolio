# Nexus Synapse — Design Principles

This directory preserves the design principles that guided Nexus Synapse as the implementation evolved.

The distinction between **historical principles** and **current engineering controls** is intentional.

- A historical principle records what the project was trying to preserve at a particular point in time.
- A current architecture document records how those responsibilities are implemented or governed now.
- Evidence documents separately record what has actually been exercised, accepted, activated, or demonstrated.

## Start here

### [The Ten Laws of Synthetic Cognition — February 5, 2026](TEN_LAWS_OF_SYNTHETIC_COGNITION_2026-02-05.md)

A preserved historical design artifact written during the earlier Nexus architecture. The terminology and named implementations reflect the system as it existed at that date.

The original wording is retained because the historical ordering matters: these principles predate later Senate/Thinker work, production recovery, V5 reconstruction, bounded public proof kernels, the process architecture/Monster, controlled reconciliation, and the private PLM/configuration-management work.

### [Ten Laws — Architectural Continuity Retrospective](TEN_LAWS_ARCHITECTURAL_RETROSPECTIVE.md)

A current public-safe crosswalk asking a narrower engineering question:

> **Did later Nexus architecture abandon, contradict, refine, or continue the principles written on February 5, 2026?**

It does not claim that these are scientifically established universal laws of artificial cognition. It treats them as dated Nexus design laws and evaluates their continuity against the current public architecture and evidence surfaces.

## Related current records

- [Architectural Evolution](../docs/ARCHITECTURAL_EVOLUTION.md)
- [Public Process Architecture](../docs/PROCESS_ARCHITECTURE.md)
- [Current Production Responsibilities](../docs/CURRENT_PRODUCTION_RESPONSIBILITIES.md)
- [Process Architecture Evidence Status](../process-architecture/EVIDENCE_STATUS.md)
- [Control Traceability](../process-architecture/traceability/CONTROL_TRACEABILITY.md)

## Reading rule

Do not silently reinterpret an old implementation name as current production truth.

For example, an early Law may name `PersonalityBank`, `Operations Manager`, or `Thinking Streams`. Those names are retained as historical evidence of the implementation at the time. The retrospective maps the underlying responsibility to its later architecture without pretending the February document predicted future component names.
