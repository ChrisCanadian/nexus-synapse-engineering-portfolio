# CTRL-500 — Provider Route Control

**Document class:** Governing Controlled Artifact / public-safe control-family specification  
**Release:** Process Architecture v0.6  
**Applies to:** Forklift & Inference Dispatch  
**Documentation approval:** APPROVED FOR PUBLIC PROCESS DOCUMENTATION  
**Runtime approved-revision binding:** GAP / NOT YET CLAIMED

[← Control Register](./CONTROL_REGISTER.md)

## Scope

Defines the public-safe decision/control family governing material decisions in **Forklift & Inference Dispatch**. This specification identifies decision responsibilities and evidence expectations, not private implementation tolerances.

## Governed decisions

- Is the route/provider known and enabled?
- Does it satisfy required capabilities?
- Does it preserve the applicable data boundary?
- Did invocation succeed?
- If it failed, is fallback explicitly allowed and can fallback preserve the same constraints? Otherwise fail closed/degrade explicitly.

## Required evidence direction

Where the target runtime makes a governed PASS/FAIL or equivalent disposition, the evidence model should be sufficient to identify the decision result, applicable receipt/evidence references, trusted turn/correlation identity, time, and the governing control revision.

## Claim ceiling

Provider availability is not inferred from a documentation/status label alone. Runtime recording of the exact approved CTRL-500 revision for each route/fallback disposition is not yet claimed.

## Withheld

Exact thresholds, weights, policy expressions, SQL, prompt/preprompt text, credentials, sensitive schemas and proprietary selection/activation logic remain private.
