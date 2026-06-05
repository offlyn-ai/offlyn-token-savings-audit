# Token Savings Calculator

This document describes the formulas used by `scripts/calculate_savings.py` to compute token usage, cost, and savings across all three architectures.

## Inputs

All formulas use configurable values from:
- `assumptions/pricing.yml` — API rates and electricity cost
- `assumptions/workload.yml` — speaking rate, token ratios, meeting profiles, scenarios
- `assumptions/routing.yml` — hybrid fallback rates and compact context ratio
- `assumptions/quality.yml` — quality dimension scores and weights
- `assumptions/carbon.yml` — carbon proxy parameters

---

## Transcript Token Calculation

```
transcript_tokens = meeting_minutes × words_per_minute × tokens_per_word
```

Defaults: 150 words/minute, 1.3 tokens/word.

| Duration | Transcript Tokens |
|---------:|------------------:|
| 30 min | 5,850 |
| 60 min | 11,700 |
| 90 min | 17,550 |

---

## Cloud-First Architecture

### Token Formulas

```
summary_input_tokens = transcript_tokens
summary_output_tokens = configured_summary_output

action_input_tokens = transcript_tokens
action_output_tokens = configured_action_output

embedding_tokens = transcript_tokens

qa_input_tokens = queries_per_meeting × qa_input_per_query
qa_output_tokens = queries_per_meeting × qa_output_per_query

memory_input_tokens = transcript_tokens
memory_output_tokens = configured_memory_output

followup_input_tokens = drafts_per_meeting × followup_input_per_draft
followup_output_tokens = drafts_per_meeting × followup_output_per_draft
```

### Aggregation

```
cloud_llm_input = summary_input + action_input + qa_input + memory_input + followup_input
cloud_llm_output = summary_output + action_output + qa_output + memory_output + followup_output
cloud_embedding = embedding_tokens
cloud_billable = cloud_llm_input + cloud_llm_output + cloud_embedding
```

### Cost Formulas

```
transcription_cost = minutes × transcription_price_per_minute
llm_cost = (cloud_llm_input / 1M × input_price) + (cloud_llm_output / 1M × output_price)
embedding_cost = cloud_embedding / 1M × embedding_price
cloud_total_cost = transcription_cost + llm_cost + embedding_cost
```

---

## Offline-First Architecture

### Token Formulas

```
cloud_llm_input = 0
cloud_llm_output = 0
cloud_embedding = 0
cloud_billable = 0
transcription_cost = 0
cloud_total_cost = 0
```

### Local Compute Cost

```
local_kwh = (local_inference_watts / 1000) × (meeting_minutes / 60)
local_compute_cost = local_kwh × electricity_price_per_kwh
total_cost = local_compute_cost
```

---

## Hybrid Router Architecture

### Token Formulas (Per Task)

For each task with a fallback rate:

```
hybrid_input_for_task = cloud_first_input_for_task × compact_context_ratio × fallback_rate
hybrid_output_for_task = cloud_first_output_for_task × fallback_rate
```

### Aggregation

```
hybrid_llm_input = sum of hybrid_input for all tasks
hybrid_llm_output = sum of hybrid_output for all tasks
hybrid_embedding = 0  (embeddings are local)
hybrid_transcription_cost = 0  (transcription is local)
hybrid_billable = hybrid_llm_input + hybrid_llm_output
```

### Cost Formulas

```
hybrid_cloud_cost = (hybrid_llm_input / 1M × input_price) + (hybrid_llm_output / 1M × output_price)
hybrid_total_cost = hybrid_cloud_cost + local_compute_cost
```

---

## Per-User and Per-Team Scaling

```
monthly_tokens = tokens_per_meeting × meetings_per_month
annual_tokens = monthly_tokens × 12
monthly_cost = cost_per_meeting × meetings_per_month
annual_cost = monthly_cost × 12
monthly_savings = cloud_first_monthly_cost - architecture_monthly_cost
annual_savings = monthly_savings × 12
```

---

## Quality-Adjusted Metrics

### Weighted Quality Score

```
quality_score = Σ (weight_i × score_i) for all dimensions
```

### Quality-Adjusted Value

```
quality_adjusted_value = token_reduction_pct × quality_retention_pct
```

Where quality_retention_pct = architecture_quality_score / cloud_first_quality_score × 100.

### Cost-Quality Efficiency

```
cost_quality_efficiency = quality_score / total_cost_per_meeting
```

### Privacy-Adjusted Score

```
privacy_adjusted_score = quality_score × (privacy_score / 5.0)
```

### Offline Resilience Score

```
offline_resilience = offline_availability_score / 5.0
```

---

## Scenario Definitions

### Scenario A: Solo User
- 20 meetings/month
- 60 minutes average
- 5 Q&A queries per meeting

### Scenario B: Small Team
- 5 people, 100 meetings/month total
- 60 minutes average
- 5 Q&A queries per meeting

### Scenario C: Enterprise Team
- 50 people, 1,000 meetings/month total
- 60 minutes average
- 5 Q&A queries per meeting

---

## Fallback Rate Sensitivity

Varying the hybrid fallback rates changes total cloud token usage:

| Q&A Fallback Rate | Approximate Hybrid Tokens (60-min) | Reduction vs Cloud-First |
|------------------:|------------------------------------:|-------------------------:|
| 0% | minimal | ~99%+ |
| 10% | low | ~98%+ |
| 20% (default) | ~1,354 | ~97.9% |
| 50% | moderate | ~94%+ |
| 100% | higher (still compact) | ~85%+ |

Even at 100% fallback rate, the compact context ratio (20%) means hybrid sends far fewer tokens than cloud-first.

---

## Running the Calculator

```bash
python scripts/calculate_savings.py
```

This generates `analysis/generated_results.md` with full comparison tables.

To render tables to stdout:
```bash
python scripts/render_tables.py
```

To write to a custom file:
```bash
python scripts/render_tables.py -o output.md
```
