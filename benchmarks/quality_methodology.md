# Quality Methodology

This document explains how the repository evaluates answer quality across the three architectures without making unsupported claims.

## Approach

Quality scores in this repository are **modeled rubric defaults** designed to illustrate how different architectures compare on key dimensions. They are not measured benchmark results unless explicitly stated.

To produce real quality metrics, organizations should conduct human evaluation or validated automated evaluation on their own meeting data.

## Quality Rubric

Each architecture is scored on multiple dimensions using a 1–5 scale:

| Score | Meaning |
|------:|---------|
| 5 | Excellent — matches or exceeds human quality |
| 4 | Good — minor gaps, suitable for production use |
| 3 | Adequate — usable with occasional issues |
| 2 | Below average — frequent errors or omissions |
| 1 | Poor — unreliable for the task |

## Scoring Dimensions

| Dimension | Description | Weight |
|-----------|-------------|-------:|
| Factual grounding | Answers cite real content from the meeting | 0.20 |
| Summary completeness | Key topics, decisions, and outcomes captured | 0.15 |
| Action item correctness | Tasks are accurate, attributed, and actionable | 0.15 |
| Decision capture | Decisions and their rationale are preserved | 0.10 |
| Answer helpfulness | Q&A responses are useful and on-topic | 0.10 |
| Citation quality | Sources are traceable and verifiable | 0.10 |
| Low hallucination risk | Output does not fabricate content | 0.10 |
| Latency score | Time to first result | 0.05 |
| Offline availability | Features work without internet | 0.05 |

## Weighted Quality Score Formula

```
quality_score =
    0.20 × factual_grounding
  + 0.15 × summary_completeness
  + 0.15 × action_item_correctness
  + 0.10 × decision_capture
  + 0.10 × answer_helpfulness
  + 0.10 × citation_quality
  + 0.10 × low_hallucination_risk
  + 0.05 × latency_score
  + 0.05 × offline_availability_score
```

## Default Modeled Scores

| Dimension | Cloud-First | Offline-First | Hybrid Router |
|-----------|:-----------:|:-------------:|:-------------:|
| Factual grounding | 4.5 | 4.0 | 4.5 |
| Summary completeness | 4.5 | 4.0 | 4.4 |
| Action item correctness | 4.3 | 4.0 | 4.4 |
| Decision capture | 4.4 | 3.9 | 4.4 |
| Answer helpfulness | 4.5 | 4.0 | 4.6 |
| Citation quality | 4.0 | 4.2 | 4.4 |
| Low hallucination risk | 4.0 | 4.0 | 4.3 |
| Latency score | 3.5 | 4.2 | 4.0 |
| Offline availability | 1.0 | 5.0 | 4.5 |
| **Weighted quality score** | **4.215** | **4.045** | **4.420** |
| Privacy score (separate) | 2.0 | 5.0 | 4.3 |

These scores reflect modeled expectations, not measured evaluation data.

## Example Evaluation Questions

To validate quality scores with real data, evaluate outputs against questions such as:

1. Does the summary capture all key decisions made in the meeting?
2. Are action items correctly attributed to the right person?
3. Does the Q&A answer cite specific meeting content?
4. Is any content hallucinated or fabricated?
5. Are timestamps and speaker labels correct?
6. Can the user trace an answer back to the source transcript?
7. How long does the user wait for results?
8. Does the system work when the user is on a plane?

## How to Compare Cloud/Offline/Hybrid

1. **Same meeting, three architectures**: Process identical transcripts through each architecture and score outputs.
2. **Blind evaluation**: Present outputs without architecture labels to human raters.
3. **Task-specific scoring**: Some tasks favor cloud (complex reasoning), others favor local (privacy, latency, availability).
4. **Aggregate and weight**: Use the weighted formula to produce a single comparable score.

## Human Review Option

For enterprise evaluations:
1. Select 20–50 representative meetings.
2. Process through each architecture.
3. Have 2–3 raters score each output on all dimensions.
4. Calculate inter-rater agreement.
5. Report mean scores with confidence intervals.

## LLM-as-Judge Option

For automated evaluation at scale:
1. Use a separate evaluation LLM to score outputs against reference answers.
2. Calibrate against human ratings on a subset.
3. Report correlation between human and LLM-judge scores.
4. Disclose the evaluation model and prompt.

## Limitations

- Default scores are modeled assumptions, not empirical measurements.
- Quality varies by meeting type, language, domain, and speaker count.
- Local model quality improves as models are updated (Gemma versions, quantization advances).
- Cloud model quality varies by provider, model version, and prompt engineering.
- The rubric weights are configurable and should be adjusted for each organization's priorities.
- A single weighted score may obscure important dimension-level differences.
- Privacy and offline availability are included as quality dimensions because they represent value to the user, but they are not traditional NLP quality metrics.
