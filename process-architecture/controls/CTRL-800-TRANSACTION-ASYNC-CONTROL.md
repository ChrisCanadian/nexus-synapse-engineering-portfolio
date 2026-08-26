# CTRL-800 — Transaction / Async Control

**Document class:** Governing Controlled Artifact / public-safe control-family specification  
**Release:** Process Architecture v0.6  
**Applies to:** Transaction Close & Async Continuity  
**Documentation approval:** APPROVED FOR PUBLIC PROCESS DOCUMENTATION  
**Runtime approved-revision binding:** GAP / NOT YET CLAIMED

[← Control Register](./CONTROL_REGISTER.md)

## Scope

Defines the public-safe decision/control family governing material decisions in **Transaction Close & Async Continuity**. This specification identifies decision responsibilities and evidence expectations, not private implementation tolerances.

## Governed decisions

- Did turn + receipt + outbox persistence commit transactionally?
- Can queued work be claimed under a valid lease?
- Are stale leases recovered and retries/dead letters visible?
- Does worker output cross the candidate/proposal boundary before protected state changes?
- For summaries/reminders/reflection/Thinker/vocabulary work, are required scope/consent/materiality/fail-open rules satisfied?

## Required evidence direction

Where the target runtime makes a governed PASS/FAIL or equivalent disposition, the evidence model should be sufficient to identify the decision result, applicable receipt/evidence references, trusted turn/correlation identity, time, and the governing control revision.

## Claim ceiling

Queue/WIP lifecycle is implemented/tested in V5, but the exact approved CTRL-800 revision is not yet claimed to be attached to every async disposition receipt.

## Withheld

Exact thresholds, weights, policy expressions, SQL, prompt/preprompt text, credentials, sensitive schemas and proprietary selection/activation logic remain private.
