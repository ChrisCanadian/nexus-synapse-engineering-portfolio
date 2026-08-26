# CTRL-600 — Tool Authorization

**Document class:** Governing Controlled Artifact / public-safe control-family specification  
**Release:** Process Architecture v0.6  
**Applies to:** Tool Workcell & Proof  
**Documentation approval:** APPROVED FOR PUBLIC PROCESS DOCUMENTATION  
**Runtime approved-revision binding:** GAP / NOT YET CLAIMED

[← Control Register](./CONTROL_REGISTER.md)

## Scope

Defines the public-safe decision/control family governing material decisions in **Tool Workcell & Proof**. This specification identifies decision responsibilities and evidence expectations, not private implementation tolerances.

## Governed decisions

- Is the proposed tool advertised and actually dispatchable?
- Is the trusted actor/scope authorized for the capability?
- Are typed arguments and deadline valid?
- Does execution require an async job or can it run synchronously?
- If execution times out/fails, is retry/cancel permitted and truthful?

## Required evidence direction

Where the target runtime makes a governed PASS/FAIL or equivalent disposition, the evidence model should be sufficient to identify the decision result, applicable receipt/evidence references, trusted turn/correlation identity, time, and the governing control revision.

## Claim ceiling

Proposal does not equal authorization. Exact private policy rules are withheld. Runtime binding of the approved CTRL-600 revision into each authorization disposition is not yet claimed.

## Withheld

Exact thresholds, weights, policy expressions, SQL, prompt/preprompt text, credentials, sensitive schemas and proprietary selection/activation logic remain private.
