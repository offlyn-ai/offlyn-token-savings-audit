# Sample Meeting: 30-Minute Meeting

This example shows the token and cost comparison for a standard 30-minute meeting using default assumptions.

## Meeting Parameters

| Parameter | Value |
|-----------|------:|
| Duration | 30 minutes |
| Speaking rate | 150 words/minute |
| Tokens per word | 1.3 |
| Transcript tokens | 5,850 |
| Q&A queries | 5 |
| Follow-up drafts | 1 |

## Cloud-First Token Breakdown

| Component | Input Tokens | Output Tokens |
|-----------|------------:|-------------:|
| Summarization | 5,850 | 800 |
| Action items | 5,850 | 500 |
| Q&A (5 queries) | 10,000 | 2,500 |
| Memory consolidation | 5,850 | 500 |
| Follow-up (1 draft) | 2,000 | 400 |
| Embedding | 5,850 | — |
| **LLM input total** | **29,550** | — |
| **LLM output total** | — | **4,700** |
| **Embedding tokens** | **5,850** | — |
| **Cloud billable tokens** | **40,100** | — |

## Cost Comparison

| Architecture | Cloud API Cost | Local Compute Cost | Total Cost |
|--------------|---------------:|-------------------:|-----------:|
| Cloud-first | ~$0.35 | $0.00 | ~$0.35 |
| Offline-first | $0.00 | ~$0.004 | ~$0.004 |
| Hybrid router | ~$0.005 | ~$0.004 | ~$0.009 |

## Savings Summary

| Metric | Offline-First | Hybrid Router |
|--------|-------------:|-------------:|
| Tokens avoided | 40,100 | ~39,400 |
| Token reduction | 100% | ~98% |
| Cost avoided | ~$0.35 | ~$0.34 |

## Notes

- A 30-minute meeting is the shortest standard benchmark duration.
- Even short meetings accumulate significant tokens due to repeated context passes and Q&A expansion.
- All values are computed from configurable defaults in `assumptions/`.
