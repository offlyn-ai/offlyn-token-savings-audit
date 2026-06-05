# Claims Policy

This document defines the allowed and disallowed sustainability claims for the Offlyn AI Resource Avoidance Audit. The policy prevents greenwashing and ensures all communications remain technically accurate and legally defensible.

---

## Allowed Claims

The following language may be used in documentation, reports, marketing, and customer communications:

| Claim | Context |
|-------|---------|
| "SCI-AI-aligned" | Reporting structure follows SCI-AI specification |
| "SCI-aligned" | Carbon intensity reporting follows SCI methodology |
| "ISO/IEC 21031:2024-informed" | Methodology is informed by the standard |
| "Modeled estimate" | All default values are assumptions-based |
| "Operational SCI-AI proxy" | Carbon intensity excludes embodied carbon |
| "Consumer SCI reporting" | Boundary covers AI service consumption |
| "Estimated avoided cloud resource use" | Comparative reduction vs baseline |
| "Estimated avoided cloud inference emissions" | Carbon not emitted due to local routing |
| "Estimated reduction in datacenter cooling-water demand" | Water metric |
| "Not an offset or carbon credit" | Clarification of what avoidance means |
| "Assurance-ready methodology" | Structure supports future verification |

---

## Disallowed Claims

The following language must NOT be used anywhere in this repository, generated reports, documentation, or derived communications:

| Disallowed Claim | Reason |
|------------------|--------|
| "ISO certified" | No ISO certification has been obtained |
| "SCI certified" | No SCI certification exists or has been obtained |
| "SCI-AI certified" | No SCI-AI certification exists or has been obtained |
| "Carbon neutral" | Would require offsets and third-party verification |
| "Zero carbon AI" | No AI system has zero carbon impact |
| "Water-free AI" | Local devices still consume electricity with water footprint |
| "Verified emissions reduction" | No third-party verification has been performed |
| "Carbon credit" | Avoided emissions are not tradeable credits |
| "Offset" | Architecture comparison is not an offset mechanism |
| "Guaranteed Scope 3 reduction" | Modeled estimates cannot guarantee supply-chain reductions |
| "Net zero" | Would require comprehensive lifecycle accounting and offsets |
| "Climate positive" | Would require removal credits exceeding total footprint |

---

## Reporting Labels

All generated reports must include one of the following labels:

| Label | Meaning |
|-------|---------|
| `operational_proxy` | Operational energy and carbon only, embodied excluded |
| `operational_plus_embodied_estimate` | Includes allocated embodied carbon estimate |
| `third_party_verified` | Independently verified by qualified assessor |
| `modeled_not_verified` | Based on configurable assumptions, not measured |

This repo defaults to `modeled_not_verified` with `operational_proxy` boundary.

---

## Standard Disclaimer

Include in all customer-facing reports:

> These figures are modeled estimates for architecture comparison and decision support. They are not carbon credits, offsets, certified emissions reductions, or ISO/SCI certifications. Update assumptions with organization-specific data for production reporting.

---

## Review Cadence

This claims policy should be reviewed:
- When new sustainability standards are published
- When new regulatory guidance affects AI carbon reporting
- Before any customer-facing sustainability claim is made
- Annually as part of methodology review

---

## References

- Green Software Foundation SCI Specification
- Green Software Foundation SCI-AI Specification
- ISO/IEC 21031:2024 (Software Carbon Intensity)
- GHG Protocol: guidance on avoided emissions
- Science Based Targets initiative: guidance on beyond-value-chain mitigation
