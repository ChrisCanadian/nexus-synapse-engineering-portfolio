# Nexus Synapse — Reconciliation and Publication Control

**Document ID:** `DOC-CTRL-RECON-001`  
**Classification:** PUBLIC-SAFE PROCESS CONTROL  
**Applies to:** engineering portfolio, public bounded repositories, process architecture, production/V5 evidence references, rendered/distribution copies

## Purpose

Nexus changes quickly enough that documentation freshness cannot depend on memory or on a vague promise to “update the README later.” This control defines when public claims must be reconciled, which evidence source answers which question, and how stale material is handled.

## Source-of-truth routing

There is no single source that is authoritative for every question.

| Question | Primary evidence source |
|---|---|
| What is actually executing on the deployed production service? | live deployed evidence / runtime inspection when available |
| What responsibilities exist in the current production code line? | `nexus-synapse-runtime` current production code + reconciled runtime audit |
| What behavior must V5 preserve? | production parity obligations + accepted V5 scope/change decisions |
| What exists in V5 code? | pinned V5 reconstruction commit |
| What has been exercised in V5? | assertion-bearing tests, CI/workflow runs, acceptance evidence |
| What is operationally active on the controlled V5 test/dogfood instance? | deployment/activation receipts and live readback |
| What may be claimed publicly? | the strongest applicable evidence tier, with a pinned source revision and reconciliation date |

Historic repositories and documents are lineage/donor evidence. They do not override current production or accepted V5 evidence.

## Reconciliation cadence

### 1. Change-triggered reconciliation — immediate

A documentation reconciliation is required when any of the following occurs:

- production release or material production behavior change;
- accepted V5 capability/status change;
- V5 deployment/dogfood activation change;
- public repository release/tag or material feature change;
- benchmark/acceptance/validation result changes a claim ceiling;
- architecture/control decision changes a responsibility boundary;
- public-safe/private boundary changes;
- a reviewer identifies a concrete contradiction or stale claim.

The changed claim should not wait for the weekly/monthly cycle.

### 2. Weekly drift scan

Run a lightweight scan across the portfolio and seven public repositories for:

- stale version numbers/tags;
- `release candidate`, `planned`, `current`, `production`, `validated`, `tested`, `deployed`, `live`, or similar status language that no longer matches evidence;
- broken or superseded links;
- Drive links where GitHub is now canonical;
- stale process-architecture version references;
- README/package/release mismatches;
- old architecture wording that silently blends current production and V5.

A weekly scan may conclude “no material drift found.” That conclusion should still advance the reconciliation date in the snapshot only if the pinned heads were actually checked.

### 3. Monthly full reconciliation

Pin and review:

1. current production code head / latest live-runtime receipt available;
2. current V5 reconstruction head and relevant green/failing acceptance evidence;
3. all seven public repository heads and latest published release metadata;
4. engineering portfolio head;
5. process-architecture release/evidence snapshot;
6. current public technical reference and evidence-status documents;
7. rendered/Drive/Research-Library distribution copies that claim to be current.

Walk the public claim path:

```text
README
  ↓
architecture / terminology docs
  ↓
evidence-status + claim-ceiling docs
  ↓
case studies / repository map
  ↓
process architecture / diagrams
  ↓
rendered or presentation copies
```

### 4. Public-release gate

Run a full reconciliation regardless of calendar timing before:

- a major portfolio release;
- formal paper/whitepaper publication;
- funding/grant/application package;
- hackathon or competition submission;
- partner/investor technical packet;
- major public announcement that makes current-system claims.

## Claim-state rule

Use the evidence ladder rather than one overloaded “implemented” label:

```text
DOCUMENTED
   ↓
CODE-BACKED / IMPLEMENTED
   ↓
TESTED / EXERCISED
   ↓
ACTIVATED / DEPLOYED
   ↓
DURABLE / SUSTAINED
   ↓
INDEPENDENTLY VERIFIED (when applicable)
```

A higher tier must not be inferred from a lower tier.

## Correction rule

When drift is found:

1. correct the closest claim-bearing source first;
2. update dependent summaries/navigation next;
3. do not rewrite historical evidence to make it look contemporary;
4. mark genuinely historical/superseded material as such;
5. preserve failed/partial validation results rather than replacing them with a later success from a different test;
6. update the pinned public snapshot after corrections land.

## Public process documentation

For process architecture:

- private Drive binder = working/control source and backup;
- engineering portfolio Git history = canonical approved public record;
- GitHub Pages = executable presentation layer;
- distribution copies may follow GitHub but do not supersede it.

## Review output

A reconciliation pass should leave one of three outcomes:

- **CURRENT** — checked and no material correction required;
- **CORRECTED** — drift found and corrected with commit(s) recorded;
- **REVIEW_REQUIRED** — evidence conflict or inaccessible source prevents a safe current claim.

The current cross-repository state is recorded in [`CURRENT_PUBLIC_SNAPSHOT.md`](CURRENT_PUBLIC_SNAPSHOT.md).
