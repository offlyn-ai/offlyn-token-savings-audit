# Evidence Log

This document links to all source files supporting the SCI for AI-aligned disclosure.

## Methodology Documentation

| Evidence | File | Description |
|----------|------|-------------|
| SCI-AI methodology | [analysis/sci_ai_methodology.md](../analysis/sci_ai_methodology.md) | Full SCI for AI methodology explanation |
| Carbon methodology | [analysis/carbon_methodology.md](../analysis/carbon_methodology.md) | Carbon accounting approach |
| Energy methodology | [analysis/energy_methodology.md](../analysis/energy_methodology.md) | Incremental energy model |
| Water methodology | [analysis/water_methodology.md](../analysis/water_methodology.md) | Supplemental water metric |
| Quality methodology | [analysis/quality_methodology.md](../analysis/quality_methodology.md) | Quality assessment dimensions |
| Claims policy | [analysis/claims_policy.md](../analysis/claims_policy.md) | Allowed and disallowed claims |
| Avoided emissions | [analysis/avoided_emissions_methodology.md](../analysis/avoided_emissions_methodology.md) | Avoided vs net avoided carbon |

## Assumptions

| Evidence | File | Description |
|----------|------|-------------|
| Carbon assumptions | [assumptions/carbon.yml](../assumptions/carbon.yml) | Carbon intensity parameters |
| SCI-AI assumptions | [assumptions/sci_ai.yml](../assumptions/sci_ai.yml) | SCI boundary and reporting config |
| Water assumptions | [assumptions/water.yml](../assumptions/water.yml) | WUE and water parameters |
| Network assumptions | [assumptions/network.yml](../assumptions/network.yml) | Network transfer estimates |
| Pricing assumptions | [assumptions/pricing.yml](../assumptions/pricing.yml) | API and compute pricing |
| Workload assumptions | [assumptions/workload.yml](../assumptions/workload.yml) | Meeting workload parameters |
| Quality assumptions | [assumptions/quality.yml](../assumptions/quality.yml) | Quality scoring parameters |
| Routing assumptions | [assumptions/routing.yml](../assumptions/routing.yml) | Hybrid routing configuration |
| Consolidated register | [certification/assumptions_register.yml](assumptions_register.yml) | All key assumptions in one file |

## Benchmarks

| Evidence | File | Description |
|----------|------|-------------|
| Cloud baseline | [benchmarks/cloud_baseline.md](../benchmarks/cloud_baseline.md) | Cloud-first architecture model |
| Local (Clipper) | [benchmarks/clipper_local.md](../benchmarks/clipper_local.md) | Offline-first architecture model |
| Hybrid router | [benchmarks/hybrid_router.md](../benchmarks/hybrid_router.md) | Hybrid local-first router model |
| Quality methodology | [benchmarks/quality_methodology.md](../benchmarks/quality_methodology.md) | Quality benchmark approach |

## Calculation Scripts

| Evidence | File | Description |
|----------|------|-------------|
| Token savings calculator | [scripts/calculate_savings.py](../scripts/calculate_savings.py) | Token and cost calculations |
| SCI-AI calculator | [scripts/calculate_sci_ai.py](../scripts/calculate_sci_ai.py) | Carbon, energy, water, SCI calculations |
| Disclosure export | [scripts/export_sci_ai_disclosure.py](../scripts/export_sci_ai_disclosure.py) | CSV and score generation |
| Readiness validator | [scripts/validate_sci_ai_disclosure.py](../scripts/validate_sci_ai_disclosure.py) | 25-item certification readiness check |

## Generated Outputs

| Evidence | File | Description |
|----------|------|-------------|
| Calculation CSV | [certification/sci_ai_calculation.csv](sci_ai_calculation.csv) | Machine-readable results |
| Readiness score | [certification/certification_readiness_score.json](certification_readiness_score.json) | Validator output |
| SCI-AI results | [analysis/generated_sci_ai_results.md](../analysis/generated_sci_ai_results.md) | Generated markdown report |
| Token results | [analysis/generated_results.md](../analysis/generated_results.md) | Generated token savings report |

## Tests

| Evidence | File | Description |
|----------|------|-------------|
| SCI-AI tests | [tests/test_sci_ai.py](../tests/test_sci_ai.py) | Core SCI-AI calculation tests |
| Calculation tests | [tests/test_sci_ai_calculations.py](../tests/test_sci_ai_calculations.py) | Pure function tests |
| Validation tests | [tests/test_sci_ai_disclosure_validation.py](../tests/test_sci_ai_disclosure_validation.py) | Validator tests |
| Claims tests | [tests/test_claims_policy.py](../tests/test_claims_policy.py) | Claims policy tests |
| Water tests | [tests/test_water_supplemental.py](../tests/test_water_supplemental.py) | Water supplemental tests |
| Token savings tests | [tests/test_calculate_savings.py](../tests/test_calculate_savings.py) | Original calculator tests |

## Schemas

| Evidence | File | Description |
|----------|------|-------------|
| Audit run schema | [schemas/audit_run.schema.json](../schemas/audit_run.schema.json) | JSON schema for audit output |
| SCI-AI assumptions schema | [schemas/sci_ai_assumptions.schema.json](../schemas/sci_ai_assumptions.schema.json) | Assumptions validation |

## Submission Package

| Evidence | File | Description |
|----------|------|-------------|
| Submission metadata | [certification/submission_metadata.yml](submission_metadata.yml) | GSF submission metadata and signatory |
| Data sources | [certification/data_sources.md](data_sources.md) | Assumption data sources and validation status |
| GSF submission checklist | [certification/gsf_submission_checklist.md](gsf_submission_checklist.md) | Pre-submission manual checklist |
| Release notes | [certification/release_notes_v0.1.md](release_notes_v0.1.md) | v0.1 release notes |
