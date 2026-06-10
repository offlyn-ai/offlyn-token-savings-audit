# Offlyn Meeting Intelligence Hybrid Routing Benchmark — SCI for AI-aligned Disclosure

## Disclosure Status

This is a self-attested, modeled, SCI for AI-aligned Consumer SCI operational proxy disclosure. It is not a formal ISO certification, Green Software Foundation certification, carbon credit, offset, certified emissions reduction, or carbon-neutrality claim unless and until an official public certificate is issued.

## Software System

Offlyn AI Resource Avoidance Audit for a 60-minute meeting intelligence workflow.

## Purpose

To compare the operational carbon intensity, token cost, answer-quality tradeoffs, privacy exposure, and supplemental datacenter cooling-water impact of cloud-first, local-first, and hybrid local-first AI routing.

## Boundary

Consumer SCI operational boundary for inference-time meeting intelligence.

The boundary includes operational AI usage during inference-time workflow execution. Provider SCI (model training, fine-tuning, deployment infrastructure) is excluded from the default calculation and may be added as a future extension.

See [sci_ai_boundary.md](sci_ai_boundary.md) for the complete component inclusion table.

## Functional Unit

**Primary:** One 60-minute meeting intelligence workflow.

A single 60-minute meeting processed into transcript, summary, action items, key moments, Q&A-ready memory, and follow-up draft.

**Secondary functional units:**
- gCO2e per meeting hour
- gCO2e per second of audio processed
- gCO2e per transcript generated
- gCO2e per 1,000 cloud tokens
- gCO2e per accepted summary
- gCO2e per workflow execution

See [sci_ai_functional_unit.md](sci_ai_functional_unit.md) for definitions and rationale.

## Formula

```
SCI operational proxy = total operational carbon emissions / functional unit count
```

Where:
- SCI = (O + M) / R
- O = operational emissions (included)
- M = embodied emissions (excluded, M = 0)
- R = functional unit count

See [sci_ai_calculation.md](sci_ai_calculation.md) for the full component breakdown.

## Scenarios

| Scenario | Description |
|----------|-------------|
| Cloud-first | All intelligence via cloud APIs (baseline) |
| Local-first | All intelligence on Apple Silicon (Offlyn Clipper) |
| Hybrid local-first router | Local by default, selective cloud fallback |

## Embodied Emissions

Embodied emissions are excluded from the default operational proxy because reliable allocation data for local user devices, cloud provider hardware, networking, and storage infrastructure is not currently available. Future disclosures may include embodied emissions when reliable allocation data is available.

## Water

Water is reported as a supplemental metric. It is not included in the SCI carbon score.

The default water model estimates direct datacenter cooling water for cloud-routed workloads. Local-first AI is not water-free — local devices still use electricity, and electricity generation may have indirect water impacts. The default model only estimates reduction in direct cloud datacenter cooling-water demand.

## Limitations

- This disclosure is modeled, not measured.
- Quality scores are modeled defaults unless measured evaluations are added.
- Cloud emissions are estimated from configurable token-to-carbon assumptions.
- Local energy is modeled as incremental inference energy above baseline device usage.
- Embodied carbon is excluded by default.
- Water is supplemental and not part of the SCI score.
- Avoided emissions are reported separately and are not part of the SCI score.
- This is not a certification claim.

See [limitations.md](limitations.md) for the complete limitations register.

## Attestation

See [sci_ai_attestation.md](sci_ai_attestation.md).

## Version

- Disclosure version: 0.1.0
- Disclosure type: SCI for AI-aligned Consumer SCI operational proxy
- Verification status: Self-attested, modeled, not third-party verified
