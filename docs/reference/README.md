# Public Technical Reference

## Source-of-truth rule

The **version-controlled Markdown document in this directory is the canonical source for Public Technical Reference v1.1**:

- [NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md](NEXUS_PUBLIC_TECHNICAL_REFERENCE_v1_1.md) — canonical source for v1.1
- [Rendered PDF](https://drive.google.com/file/d/1KWoHkrHek5o_3T-FGKK7qLbRgb9Oi19N/view) — distribution/export copy

**Release:** v1.1  
**Production current-state review represented by this revision:** August 14, 2026  
**Public-safe revision:** August 16, 2026

The Markdown source is kept in repository history so claim changes are diffable and reviewable. A PDF should be treated as a rendered artifact of the matching source version, not as a separate or more authoritative document.

## Important current-use note

v1.1 is a **dated production technical reference**, not a self-updating description of every later V5/process-architecture change.

This revision reconciles the earlier July public reference with the August 14 read-only inspection of the deployed production implementation and state. It deliberately distinguishes deployed-code/state findings from the July 11 isolated production-target execution evidence.

For newer public state, use:

- [Current Public Snapshot](../CURRENT_PUBLIC_SNAPSHOT.md) — pinned production/V5/public-repository reconciliation inputs;
- [Public Process Architecture](../PROCESS_ARCHITECTURE.md) — current approved V5 target process model;
- [Process Architecture Evidence Status](../../process-architecture/EVIDENCE_STATUS.md) — production-pattern vs V5 code/test/hardening/activation claim boundaries;
- [Production Evidence Status](../PRODUCTION_EVIDENCE_STATUS.md) — dated production evidence and later production-facing diagnostics.

Do not silently rewrite v1.1's August 14 production facts to make them match a newer V5 target architecture. If the technical reference itself needs a new current-system synthesis, publish a new version and preserve v1.1 as the dated predecessor.

## Change-control expectation

For future technical-reference revisions:

1. identify the evidence question and source revisions being reconciled;
2. update a new/current Markdown reference through repository history;
3. review the architectural/evidence diff;
4. render a matching PDF;
5. publish or mirror the PDF through the Research Library / Drive;
6. keep the same public version identifier across source and export;
7. update [Current Public Snapshot](../CURRENT_PUBLIC_SNAPSHOT.md) and dependent portfolio summaries.

The broader cadence is governed by [Reconciliation and Publication Control](../RECONCILIATION_CONTROL.md).
