# Quality Methodology

This document describes how answer quality is assessed across cloud-first, local-first, and hybrid architectures.

## Quality Dimensions

| Dimension | Description | Measurement Method |
|-----------|-------------|-------------------|
| Correctness | Factual accuracy of generated outputs | Human evaluation or LLM-as-judge |
| Completeness | Coverage of key topics and action items | Rubric-based scoring |
| Citation coverage | Grounding in transcript evidence | Source attribution analysis |
| Hallucination risk | Rate of unsupported or fabricated claims | Fact-checking against transcript |
| Action-item usefulness | Specificity and actionability of extracted items | Human acceptance rate |
| Fallback appropriateness | Quality of hybrid routing decisions | Precision/recall of cloud escalation |
| Human acceptance | End-user satisfaction with outputs | Accept/reject/edit rate |
| LLM-as-judge | Automated quality scoring via evaluator model | Correlation with human judgment |

## Current Status

**Default quality scores are modeled assumptions unless generated from an evaluation run.**

The default scores in `assumptions/quality.yml` represent expected quality based on model capability assessments, not measured human evaluations. They are suitable for architecture comparison and cost-quality tradeoff analysis but should not be cited as measured performance.

| Architecture | Default Score | Basis |
|-------------|--------------|-------|
| Cloud-first | 4.1/5.0 | Frontier model capability assumption |
| Local-first | 3.9/5.0 | Local SLM capability assumption |
| Hybrid | 4.1/5.0 | Local + selective cloud fallback |

## Scoring Rubric

| Score | Quality Level |
|-------|--------------|
| 5.0 | Excellent — exceeds human baseline |
| 4.0 | Good — production-ready for routine tasks |
| 3.0 | Acceptable — correct but may miss nuance |
| 2.0 | Below standard — frequent errors or omissions |
| 1.0 | Unacceptable — unreliable for production use |

## Quality-Carbon Tradeoff

The hybrid router architecture attempts to maximize quality-per-gCO2e by:
1. Running routine tasks (summarization, action items) locally at acceptable quality
2. Escalating complex queries (multi-hop reasoning, external knowledge) to cloud
3. Achieving near-cloud quality at a fraction of the carbon intensity

## Future Measured Evaluation

To upgrade quality scores from modeled to measured:

```bash
python scripts/evaluate_quality.py --input examples/meetings/ --output reports/quality_eval.json
```

This command (planned, not yet implemented) will:
1. Process sample meetings through each architecture
2. Score outputs across all 8 quality dimensions
3. Compare against human reference answers
4. Optionally run LLM-as-judge for automated scoring
5. Output measured scores with confidence intervals

## Requirements for Measured Quality Claims

Before claiming measured quality:
- Minimum 30 diverse meeting samples
- Human evaluation on at least correctness and completeness
- Inter-rater reliability > 0.7 (Cohen's kappa)
- Results versioned with evaluation date and model versions
- Disclosure of any cherry-picking or filtering

## Relationship to SCI Disclosure

Quality scores are not part of the SCI carbon intensity calculation. They are reported alongside carbon metrics to show that lower-carbon architectures maintain acceptable quality for enterprise use.

Quality methodology is referenced in:
- `certification/limitations.md` (modeled vs measured status)
- `certification/assumptions_register.yml` (quality_scores_are_modeled_defaults: true)
- `benchmarks/quality_methodology.md` (benchmark-specific quality details)
