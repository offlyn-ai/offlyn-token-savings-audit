# SCI for AI-aligned Methodology

This document describes the methodology for the SCI for AI-aligned Consumer SCI operational proxy disclosure used in this repository.

## SCI for AI-aligned Reporting

This repository implements a Green Software Foundation SCI for AI-aligned, ISO/IEC 21031:2024-informed methodology for comparing the operational carbon intensity of AI meeting intelligence workflows.

The SCI (Software Carbon Intensity) specification provides a standardized way to measure and report the carbon intensity of software systems per functional unit. SCI for AI extends this to AI-specific workloads by defining appropriate boundaries, functional units, and emission components for AI inference and training.

This disclosure is a **self-attested, modeled, operational proxy** — not a formal certification or verified measurement.

## Consumer SCI vs Provider SCI

The Green Software Foundation SCI for AI framework defines two boundaries:

| Boundary | Scope | Example Activities |
|----------|-------|-------------------|
| **Consumer SCI** | Operational inference-time usage | API calls, local inference, embedding, retrieval, orchestration |
| **Provider SCI** | Model lifecycle | Data collection, training, fine-tuning, deployment, optimization |

### Why This Repo Defaults to Consumer SCI

1. **Actionable for enterprises**: Architecture decisions (cloud vs local vs hybrid) affect Consumer SCI directly.
2. **Provider SCI is shared**: Training carbon is a sunk cost amortized across all users; it does not change with routing decisions.
3. **Measurable at inference time**: Consumer SCI components can be estimated from token counts, watts, and grid intensity.
4. **Decision support**: Enterprise customers choosing between architectures need Consumer SCI comparisons.

Provider SCI is excluded from the default calculation and documented as a future extension.

## SCI Operational Proxy Formula

The canonical SCI formula:

```
SCI = (O + M) / R
```

Where:
- **O** = Operational emissions (gCO2e)
- **M** = Embodied emissions allocated to the functional unit (gCO2e)
- **R** = Functional unit count

For this disclosure:

```
SCI operational proxy = O / R
```

**M = 0** (embodied emissions excluded).

## Expanded Operational Carbon Formula

```
total_consumer_operational_carbon_gCO2e =
    cloud_inference_carbon_gCO2e
  + local_incremental_inference_carbon_gCO2e
  + asr_carbon_gCO2e
  + embedding_carbon_gCO2e
  + retrieval_carbon_gCO2e
  + orchestration_carbon_gCO2e
  + storage_carbon_gCO2e
  + network_transfer_carbon_gCO2e
  + observability_carbon_gCO2e
```

### Component Implementation Status

| Component | Status | Method |
|-----------|--------|--------|
| Cloud inference carbon | **Included** | (cloud_tokens / 1000) × gCO2e_per_1k_tokens |
| Local incremental inference carbon | **Included** | (incremental_watts / 1000) × hours × grid_intensity |
| ASR carbon | **Included** | Modeled within cloud or local inference totals |
| Embedding carbon | **Included** | Modeled within cloud or local inference totals |
| Retrieval carbon | **Included** | Modeled within cloud or local inference totals |
| Orchestration carbon | Modeled as zero | Negligible inference-time overhead |
| Storage carbon | Modeled as zero | Reliable per-meeting allocation unavailable |
| Network transfer carbon | Modeled as zero | Volume modeled in MB; energy attribution TBD |
| Observability carbon | Modeled as zero | Negligible monitoring overhead |

Components modeled as zero are documented in `certification/limitations.md` and may be included in future disclosures when attribution data improves.

## Functional Units

### Primary Functional Unit

**One 60-minute meeting intelligence workflow.**

A single meeting processed into transcript, summary, action items, key moments, Q&A-ready memory, and follow-up draft.

### Secondary Functional Units

| Unit | Formula | Use Case |
|------|---------|----------|
| gCO2e per meeting hour | total_carbon / meeting_hours | Duration normalization |
| gCO2e per second of audio | total_carbon / (minutes × 60) | Granular time comparison |
| gCO2e per transcript | total_carbon / 1 | Per-document intensity |
| gCO2e per 1,000 cloud tokens | cloud_carbon / (tokens / 1000) | Cloud cost analysis |
| gCO2e per accepted summary | total_carbon / 1 | Output-weighted intensity |
| gCO2e per workflow execution | total_carbon / 1 | Equivalent to primary |

## Embodied Emissions Exclusion Rationale

Embodied emissions (M) are excluded from the default operational proxy because:

- Reliable allocation data for local user devices is unavailable
- Cloud provider hardware embodied carbon per inference request is unpublished
- Networking and storage infrastructure allocation methods are immature
- Including unreliable estimates would undermine disclosure credibility

**Required disclosure language**: "Embodied emissions are excluded from the default operational proxy because reliable allocation data is unavailable. Future disclosures may include embodied emissions when allocation data improves."

## Water as Supplemental Metric

Water is reported as a supplemental infrastructure-efficiency metric. It is **not included in the SCI carbon score**.

Rationale:
- SCI is gCO2e/R — a carbon intensity metric measured in mass units
- Water (liters) is a different physical unit
- Combining them in a single score would conflate distinct environmental impacts
- Supplemental treatment provides transparency without methodological confusion

Water model: `direct_datacenter_water_liters = cloud_IT_energy_kWh × PUE × WUE_L/kWh`

## Avoided Emissions — Separate from SCI Score

Avoided emissions represent the difference between the cloud-first baseline and an alternative architecture:

```
avoided_cloud_carbon = cloud_first_carbon - solution_cloud_carbon
net_avoided_total_carbon = cloud_first_total_carbon - solution_total_carbon
```

Avoided emissions are:
- **Informational** — they show what *would have been* emitted under the baseline
- **Not part of the SCI score** — SCI measures intensity per unit, not reduction claims
- **Not carbon credits or offsets** — they cannot be traded or transferred
- **Not verified emissions reductions** — they are modeled estimates

## Claim Guardrails

### Allowed Terminology

- "SCI for AI-aligned"
- "ISO/IEC 21031:2024-informed"
- "Modeled estimate"
- "SCI operational proxy"
- "Consumer SCI boundary"
- "Self-attested disclosure"
- "Certification-readiness package"
- "Supplemental direct datacenter cooling-water estimate"
- "Not a carbon credit or offset"

### Disallowed Terminology

- "ISO certified"
- "SCI certified"
- "SCI for AI certified"
- "Green Software Foundation certified"
- "Carbon neutral"
- "Zero carbon AI"
- "Water-free AI"
- "Verified emissions reduction"
- "Carbon credit" / "Offset"
- "Guaranteed Scope 3 reduction"

## Relationship to ISO/IEC 21031:2024

This methodology is **informed by** ISO/IEC 21031:2024 (Software Carbon Intensity). It adopts the SCI formula structure, functional unit approach, and boundary definitions. It does not claim ISO certification or conformance unless and until formal certification is obtained.

## Reporting Modes

| Mode | Description |
|------|-------------|
| `operational_proxy` | Operational carbon only; M = 0 (default) |
| `operational_plus_embodied_estimate` | Includes estimated embodied carbon (future) |
| `third_party_verified` | After external verification (future) |

Default: `operational_proxy` with `modeled_not_verified` status.

## References

- Green Software Foundation SCI Specification
- Green Software Foundation SCI for AI
- ISO/IEC 21031:2024 — Software Carbon Intensity
- IEA World Energy Outlook (grid intensity data)
- Uptime Institute (PUE data)
- Published hyperscaler sustainability reports (WUE data)
