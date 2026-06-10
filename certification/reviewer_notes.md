# Reviewer Notes

Notes for a Green Software Foundation reviewer examining this disclosure package.

## Why Consumer SCI Boundary

This disclosure uses the Consumer SCI boundary because:

1. The audit compares three architecture choices (cloud-first, local-first, hybrid) available to enterprise customers at inference time.
2. Provider SCI (model training, fine-tuning, deployment infrastructure) is common across all compared scenarios and is outside the customer's architectural control.
3. Consumer SCI is the actionable boundary for enterprise decision-making about where inference runs.

## Why Provider SCI is Excluded

Provider SCI is excluded because:

- All three architectures use pre-trained models (cloud LLMs or local SLMs)
- Training carbon is a sunk cost shared across all users
- The disclosure focuses on marginal operational decisions, not lifecycle allocation
- Provider SCI may be included as a future extension when allocation methods mature

## Why Embodied Carbon is Excluded

Embodied carbon (M = 0) is excluded because:

- Local device embodied carbon allocation per meeting is unknown
- Cloud server embodied carbon per inference request is unpublished by providers
- Networking and storage infrastructure embodied carbon is not attributable at meeting granularity
- Including unreliable estimates would undermine disclosure credibility

Rationale is explicitly stated in:
- `certification/sci_ai_calculation.md`
- `certification/limitations.md`
- `certification/assumptions_register.yml`

## Why Water is Supplemental

Water is reported as a supplemental metric because:

- The SCI formula is gCO2e/R — a carbon intensity metric
- Water (liters) is a different physical unit and cannot be combined with carbon in a single score
- Datacenter cooling water is an important infrastructure impact worth disclosing
- Supplemental treatment avoids conflating distinct environmental concerns

Direct datacenter cooling-water estimates are included as a supplemental enterprise infrastructure-efficiency metric. They are not included in the SCI score, not part of the SCI carbon-intensity calculation, and not part of the SCI conformity claim.

## Where Assumptions Are Located

| Content | Location |
|---------|----------|
| All assumptions consolidated | `certification/assumptions_register.yml` |
| Carbon parameters | `assumptions/carbon.yml` |
| SCI-AI configuration | `assumptions/sci_ai.yml` |
| Water parameters | `assumptions/water.yml` |
| Network parameters | `assumptions/network.yml` |
| Workload parameters | `assumptions/workload.yml` |
| Pricing parameters | `assumptions/pricing.yml` |
| Quality parameters | `assumptions/quality.yml` |
| Routing parameters | `assumptions/routing.yml` |

## How to Reproduce Results

```bash
# 1. Install dependencies
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Run token and cost calculations
python scripts/calculate_savings.py

# 3. Run SCI-AI calculations (carbon, water, energy, functional units)
python scripts/calculate_sci_ai.py

# 4. Generate disclosure CSV and readiness score
python scripts/export_sci_ai_disclosure.py

# 5. Validate certification readiness (must pass with >= 99)
python scripts/validate_sci_ai_disclosure.py --strict

# 6. Run all tests
pytest tests/ -v
```

All calculations use configurable YAML assumptions. Changing any assumption file and re-running produces updated results with full traceability.

## Key Design Decisions

1. **Incremental energy model**: Only energy above baseline device usage is attributed to AI inference. This prevents over-counting device power that would be consumed regardless.

2. **Mid-case defaults**: The disclosure uses mid-case assumptions (0.50 gCO2e/1k tokens, 5W incremental, 350 gCO2e/kWh grid). Low and high cases are documented for sensitivity analysis.

3. **Avoided emissions separation**: Avoided emissions (cloud-first minus solution) are reported separately and are not part of the SCI score. This prevents conflating intensity with avoidance.

4. **Quality as modeled**: Quality scores are modeled defaults, clearly labeled as such. The disclosure does not claim measured quality without actual evaluation data.

5. **No greenwashing**: The claims policy explicitly prohibits terms like "carbon neutral," "zero carbon," "water-free AI," and "verified emissions reduction." All language is precise and conservative.

## Submission Details

| Document | Location |
|----------|----------|
| Submission metadata | `certification/submission_metadata.yml` |
| Signatory | Joel Nishant Reddy, Co-founder, Offlyn.ai |
| Data sources and validation status | `certification/data_sources.md` |
| Pre-submission checklist | `certification/gsf_submission_checklist.md` |
| Release notes | `certification/release_notes_v0.1.md` |
| Release tag | `v0.1-sci-ai-disclosure-readiness` |
