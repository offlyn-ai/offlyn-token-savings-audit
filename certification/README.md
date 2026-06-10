# SCI for AI-aligned Disclosure Package

## Disclosure Title

**Offlyn Meeting Intelligence Hybrid Routing Benchmark — SCI for AI-aligned Consumer SCI Operational Proxy Disclosure**

## Purpose

This folder contains a complete, self-attested, SCI for AI-aligned disclosure package for a modeled 60-minute meeting intelligence workflow. It is designed to support enterprise architecture comparison, FinOps, GreenOps, and Green Software Foundation SCI self-certification readiness.

## Boundary

Consumer SCI operational boundary for inference-time meeting intelligence. Provider SCI (model training, deployment) is excluded from the default calculation.

## Primary Functional Unit

One 60-minute meeting intelligence workflow.

## Status

| Item | Status |
|------|--------|
| Disclosure type | SCI for AI-aligned Consumer SCI operational proxy |
| Standard reference | ISO/IEC 21031:2024-informed |
| Boundary | Consumer SCI — 60-minute meeting intelligence workflow |
| Primary functional unit | One meeting workflow |
| Water | Supplemental metric, not included in SCI score |
| Embodied carbon | Excluded by default (reliable allocation data unavailable) |
| Verification | Self-attested modeled disclosure |
| Certification status | Certification-readiness package, not yet certified |

## Package Contents

| File | Description |
|------|-------------|
| [sci_ai_disclosure.md](sci_ai_disclosure.md) | Main disclosure document |
| [sci_ai_boundary.md](sci_ai_boundary.md) | Component inclusion/exclusion boundary table |
| [sci_ai_functional_unit.md](sci_ai_functional_unit.md) | Functional unit definitions and rationale |
| [sci_ai_calculation.md](sci_ai_calculation.md) | SCI formula and operational carbon breakdown |
| [sci_ai_calculation.csv](sci_ai_calculation.csv) | Machine-readable calculation results |
| [sci_ai_attestation.md](sci_ai_attestation.md) | Self-attestation statement |
| [assumptions_register.yml](assumptions_register.yml) | Consolidated assumptions register |
| [evidence_log.md](evidence_log.md) | Evidence trail and source file links |
| [limitations.md](limitations.md) | Known limitations and exclusions |
| [certification_readiness_checklist.md](certification_readiness_checklist.md) | 25-item readiness checklist |
| [certification_readiness_score.json](certification_readiness_score.json) | Generated readiness score |
| [reviewer_notes.md](reviewer_notes.md) | Notes for GSF reviewer |
| [submission_metadata.yml](submission_metadata.yml) | GSF submission metadata |
| [data_sources.md](data_sources.md) | Assumption data sources and validation status |
| [gsf_submission_checklist.md](gsf_submission_checklist.md) | Pre-submission checklist |
| [release_notes_v0.1.md](release_notes_v0.1.md) | Release notes for v0.1 |

## How to Regenerate

```bash
python scripts/export_sci_ai_disclosure.py
python scripts/validate_sci_ai_disclosure.py --strict
```

## Disclaimer

This is a certification-readiness package. It is not a formal ISO certification, Green Software Foundation certification, carbon credit, offset, certified emissions reduction, or carbon-neutrality claim unless and until an official public certificate is issued.
