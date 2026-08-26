# CTRL-610 — Artifact Verification

**Document class:** Governing Controlled Artifact / public-safe control-family specification  
**Release:** Process Architecture v0.6  
**Applies to:** Tool Workcell & Proof  
**Documentation approval:** APPROVED FOR PUBLIC PROCESS DOCUMENTATION  
**Runtime approved-revision binding:** GAP / NOT YET CLAIMED

[← Control Register](./CONTROL_REGISTER.md)

## Scope

Defines the public-safe decision/control family governing material decisions in **Tool Workcell & Proof**. This specification identifies decision responsibilities and evidence expectations, not private implementation tolerances.

## Governed decisions

- Did the operation actually produce an artifact?
- Do artifact bytes exist at the expected custody boundary?
- Does existence/hash/version verification pass?
- Only after verification may an artifact/delivery receipt support a success claim.

## Required evidence direction

Where the target runtime makes a governed PASS/FAIL or equivalent disposition, the evidence model should be sufficient to identify the decision result, applicable receipt/evidence references, trusted turn/correlation identity, time, and the governing control revision.

## Claim ceiling

Generation is not validation. Runtime binding of CTRL-610 revision provenance into each artifact PASS/FAIL receipt is a V5 traceability requirement.

## Withheld

Exact thresholds, weights, policy expressions, SQL, prompt/preprompt text, credentials, sensitive schemas and proprietary selection/activation logic remain private.
