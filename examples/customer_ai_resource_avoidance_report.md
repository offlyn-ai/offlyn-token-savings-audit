# Customer AI Resource Avoidance Report

> Template for enterprise-facing AI resource avoidance impact statements.

---

## Audit Summary

| Field | Value |
|-------|-------|
| Customer | [Organization Name] |
| Audit period | [Start Date] to [End Date] |
| Baseline architecture | Cloud-first meeting AI notepad |
| Solution architecture | Hybrid local-first router |
| Claim level | Modeled estimate (not verified) |
| Reporting mode | Operational SCI-AI proxy |
| SCI-AI boundary | Consumer |

---

## Key Metrics

| Metric | Baseline (Cloud-First) | Solution (Hybrid) | Avoided |
|--------|------------------------:|-------------------:|--------:|
| Cloud tokens / month | 64,450,000 | 1,354,000 | 63,096,000 |
| API cost / month | $534.48 | $15.84 | $518.65 |
| Cloud inference carbon (gCO2e/month) | 32,225 | 677 | 31,548 |
| Local incremental carbon (gCO2e/month) | 0 | 1,750 | -- |
| Net avoided carbon (gCO2e/month) | -- | -- | 29,798 |
| Direct datacenter cooling water (L/month) | 146.9 | 3.1 | 143.8 |
| Consumer SCI (gCO2e/meeting hour) | 32.2 | 2.4 | -- |
| Quality score (1-5) | 4.14 | 4.42 | -- |
| Privacy score (1-5) | 2.0 | 4.3 | -- |

---

## Consumer SCI Functional Units

| Functional Unit | Cloud-First | Hybrid |
|-----------------|------------:|-------:|
| gCO2e per meeting hour | 32.2 | 2.4 |
| gCO2e per second of audio | 0.009 | 0.001 |
| gCO2e per transcript | 32.2 | 2.4 |
| gCO2e per workflow execution | 32.2 | 2.4 |
| gCO2e per accepted summary | 32.2 | 2.4 |
| gCO2e per 1,000 cloud tokens | 0.50 | 0.50 |

---

## Architecture Decision

Based on the modeled audit:
- **97.9% of cloud tokens avoided** through hybrid local-first routing.
- **92.5% net carbon reduction** (accounting for incremental local energy).
- **97.9% reduction in datacenter cooling-water demand**.
- **Quality preserved** (hybrid score 4.42 vs cloud-first 4.14).
- **Privacy improved** (score 4.3 vs 2.0).

---

## Routing Summary

| Task | Route | Fallback Rate |
|------|-------|:-------------:|
| Transcription | Local | 0% |
| Summarization | Local | 5% |
| Action items | Local | 5% |
| Q&A | Local (cloud fallback) | 20% |
| Memory consolidation | Local | 0% |
| Follow-up drafting | Local (cloud fallback) | 15% |
| Embeddings | Local | 0% |

---

## Disclaimer

During the modeled audit period, Offlyn estimated that the hybrid workflow avoided 63,096,000 cloud tokens, $518.65 in API cost, 31,548 gCO2e of cloud inference emissions, and 143.8 liters of direct datacenter cooling-water demand compared with the cloud-first baseline. The report also estimates Consumer SCI operational proxy metrics such as gCO2e per meeting hour, gCO2e per second of audio processed, and gCO2e per workflow execution.

These figures are modeled estimates for architecture decision support. They are not carbon credits, offsets, certified emissions reductions, or carbon-neutrality claims. This is a self-attested disclosure prepared as a certification-readiness package. It is not a formal ISO certification, Green Software Foundation certification, or verified emissions reduction unless and until an official public certificate is issued. Update assumptions with organization-specific data for production reporting.

---

## Disclosure Status

| Item | Value |
|------|-------|
| Disclosure type | SCI for AI-aligned Consumer SCI operational proxy |
| Standard reference | ISO/IEC 21031:2024-informed |
| Verification | Self-attested modeled disclosure |
| Water | Supplemental, not included in SCI score |
| Embodied carbon | Excluded (M = 0) |
| Certification | Certification-readiness package, not yet certified |

---

## Methodology References

- [SCI for AI Methodology](../analysis/sci_ai_methodology.md)
- [Energy Methodology](../analysis/energy_methodology.md)
- [Water Methodology](../analysis/water_methodology.md)
- [Quality Methodology](../analysis/quality_methodology.md)
- [Avoided Emissions Methodology](../analysis/avoided_emissions_methodology.md)
- [Claims Policy](../analysis/claims_policy.md)
- [Full Disclosure Package](../certification/)
