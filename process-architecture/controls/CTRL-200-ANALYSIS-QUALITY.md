# CTRL-200 — Analysis Quality

**Document class:** Governing Controlled Artifact / public-safe control-family specification  
**Release:** Process Architecture v0.6  
**Applies to:** Analysis & Inspection  
**Documentation approval:** APPROVED FOR PUBLIC PROCESS DOCUMENTATION  
**Runtime approved-revision binding:** GAP / NOT YET CLAIMED

[← Control Register](./CONTROL_REGISTER.md)

## Scope

Defines the public-safe decision/control family governing material decisions in **Analysis & Inspection**. This specification identifies decision responsibilities and evidence expectations, not private implementation tolerances.

## Governed decisions

- Is validated precomputed NLPState available?
- If not, is an NLP adapter available?
- If analysis is unavailable or low-confidence, degrade/omit rather than create canonical fact.
- Does sentence count require batched per-sentence intent/topic/emotion-context classification?
- Does the Focus cascade have enough history; if so, fatigue → deep focus → flow → cruising is evaluated in that order.

## Required evidence direction

Where the target runtime makes a governed PASS/FAIL or equivalent disposition, the evidence model should be sufficient to identify the decision result, applicable receipt/evidence references, trusted turn/correlation identity, time, and the governing control revision.

## Claim ceiling

Analysis remains advisory. Exact confidence thresholds and private focus criteria are withheld. Runtime binding of the approved CTRL-200 revision into analysis-quality dispositions is not yet claimed.

## Withheld

Exact thresholds, weights, policy expressions, SQL, prompt/preprompt text, credentials, sensitive schemas and proprietary selection/activation logic remain private.
