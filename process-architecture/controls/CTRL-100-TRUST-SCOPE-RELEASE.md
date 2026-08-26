# CTRL-100 — Trust / Scope Release

**Document class:** Governing Controlled Artifact / public-safe control-family specification  
**Release:** Process Architecture v0.6  
**Applies to:** Receiving & Trust Boundary  
**Documentation approval:** APPROVED FOR PUBLIC PROCESS DOCUMENTATION  
**Runtime approved-revision binding:** GAP / NOT YET CLAIMED

[← Control Register](./CONTROL_REGISTER.md)

## Scope

Defines the public-safe decision/control family governing material decisions in **Receiving & Trust Boundary**. This specification identifies decision responsibilities and evidence expectations, not private implementation tolerances.

## Governed decisions

- Is the principal authenticated?
- Can trusted actor/scope be resolved without model-authored authority?
- If team/shared scope is requested, is membership/channel scope authorized?
- If the release conditions are not satisfied, deny or emit an explicit bounded failure.

## Required evidence direction

Where the target runtime makes a governed PASS/FAIL or equivalent disposition, the evidence model should be sufficient to identify the decision result, applicable receipt/evidence references, trusted turn/correlation identity, time, and the governing control revision.

## Claim ceiling

Runtime binding of CTRL-100 plus the approved control revision into every receiving PASS/FAIL receipt is a V5 traceability requirement; it is not yet claimed as implemented.

## Withheld

Exact thresholds, weights, policy expressions, SQL, prompt/preprompt text, credentials, sensitive schemas and proprietary selection/activation logic remain private.
