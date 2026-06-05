# Clipper vs Cloud GreenOps Report

> Side-by-side GreenOps comparison for a 50-person enterprise team.

---

## Scenario Parameters

| Parameter | Value |
|-----------|------:|
| Team size | 50 |
| Meetings per month | 1,000 |
| Average meeting duration | 60 min |
| Q&A queries per meeting | 5 |
| Audit period | 12 months |

---

## Annual Resource Comparison

| Resource | Cloud-First | Offlyn Clipper (Offline) | Hybrid Router |
|----------|------------:|-------------------------:|--------------:|
| **Cloud tokens** | 773,400,000 | 0 | 16,248,000 |
| **API cost** | $6,414 | $0 | $190 |
| **Cloud inference carbon (kgCO2e)** | 386.7 | 0 | 8.1 |
| **Local incremental carbon (kgCO2e)** | 0 | 21.0 | 21.0 |
| **Net total carbon (kgCO2e)** | 386.7 | 21.0 | 29.1 |
| **Direct datacenter water (L)** | 1,763 | 0 | 37 |
| **Sensitive transcripts sent to cloud** | 12,000 | 0 | 0 |
| **Offline availability** | Limited | Full | Core features full |

---

## Annual Savings vs Cloud-First

| Metric | Offlyn Clipper | Hybrid Router |
|--------|---------------:|--------------:|
| Tokens avoided | 773,400,000 | 757,152,000 |
| API cost saved | $6,414 | $6,224 |
| Cloud carbon avoided (kgCO2e) | 386.7 | 378.6 |
| Net carbon reduction (kgCO2e) | 365.7 | 357.6 |
| Water demand avoided (L) | 1,763 | 1,726 |
| Token reduction % | 100% | 97.9% |
| Carbon reduction % | 94.6% | 92.5% |

---

## Consumer SCI Comparison

| Functional Unit | Cloud-First | Clipper | Hybrid |
|-----------------|------------:|--------:|-------:|
| gCO2e / meeting hour | 32.2 | 1.75 | 2.43 |
| gCO2e / second audio | 0.0090 | 0.0005 | 0.0007 |
| gCO2e / transcript | 32.2 | 1.75 | 2.43 |
| gCO2e / workflow execution | 32.2 | 1.75 | 2.43 |

---

## Quality and Privacy

| Dimension | Cloud-First | Clipper | Hybrid |
|-----------|:-----------:|:-------:|:------:|
| Quality score (1-5) | 4.14 | 4.07 | 4.42 |
| Privacy score (1-5) | 2.0 | 5.0 | 4.3 |
| Offline resilience (0-1) | 0.20 | 1.00 | 0.90 |

---

## GreenOps Recommendation

For this 50-person team:

1. **Hybrid router** is the recommended default: captures 97.9% of token savings with best quality score (4.42) and strong privacy (4.3).
2. **Offlyn Clipper offline-first** is recommended for sensitive meetings (executive, legal, HR) and field operations.
3. **Cloud fallback** reserved for complex reasoning, external knowledge, and explicit user requests.

---

## Reporting Standards

- SCI-AI-aligned, ISO/IEC 21031:2024-informed
- Consumer SCI boundary (operational AI consumption)
- Operational proxy reporting mode
- Modeled estimates, not verified
- See [Claims Policy](../analysis/claims_policy.md)
