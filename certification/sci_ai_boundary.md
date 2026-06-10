# SCI for AI Boundary Definition

## Disclosure Boundary

Consumer SCI operational boundary for inference-time meeting intelligence.

## Component Inclusion Table

| Component | Cloud-first | Local-first | Hybrid | Included? | Notes |
|-----------|-------------|-------------|--------|-----------|-------|
| Cloud LLM inference | Yes | No | Partial | Included | Token-based operational proxy using gCO2e/1k tokens |
| Local LLM inference | No | Yes | Yes | Included | Incremental energy above baseline device usage |
| ASR / transcription | Cloud | Local | Local | Included | Modeled assumptions for Whisper-class models |
| Embeddings | Cloud | Local | Local or partial | Included | Modeled assumptions for embedding generation |
| Retrieval | Cloud | Local | Hybrid | Included | Modeled assumptions for RAG operations |
| Network transfer | High | Zero | Low | Included | Modeled MB per meeting for cloud uploads |
| Storage | Cloud | Local | Hybrid | Optional | Included only if assumptions exist; currently modeled as zero |
| Observability | Cloud | Local | Hybrid | Optional | Included only if assumptions exist; currently modeled as zero |
| End-user baseline device power | Yes | Yes | Yes | Excluded | Excluded because all architectures require a user device; not a differentiator |
| Incremental local inference power | No | Yes | Yes | Included | Only the additional power above baseline device usage |
| Embodied hardware carbon | Unknown | Unknown | Unknown | Excluded by default | Reliable allocation data unavailable for local devices, cloud hardware, networking, and storage |
| Water | Cloud cooling | None direct | Partial | Supplemental only | Not part of SCI carbon score; reported as separate metric |

## Boundary Rationale

### Why Consumer SCI

This disclosure uses the Consumer SCI boundary because:
- The audit compares architecture choices available to enterprise customers
- Provider SCI (training, deployment) is common across scenarios and not within customer control
- Consumer SCI is actionable for architecture decision-making

### Why Baseline Device Power is Excluded

All three scenarios (cloud-first, local-first, hybrid) require the user to have a computing device running. The baseline device power consumption is identical across architectures and does not contribute to the comparison. Only the incremental inference power above this baseline is included.

### Why Embodied Carbon is Excluded

Embodied carbon allocation requires lifecycle assessment data for:
- End-user devices (laptops, phones)
- Cloud provider server hardware
- Networking infrastructure
- Storage systems

Reliable, publicly available allocation methodologies for these components do not exist at the precision level required for this disclosure. Embodied carbon may be included in future versions when allocation data improves.

### Why Water is Supplemental

Water is an important infrastructure efficiency metric but is not part of the SCI carbon intensity formula (gCO2e/R). It is reported separately to inform decision-making without conflating distinct environmental impacts.

Direct datacenter cooling-water estimates are included as a supplemental enterprise infrastructure-efficiency metric. They are not included in the SCI score, not part of the SCI carbon-intensity calculation, and not part of the SCI conformity claim.
