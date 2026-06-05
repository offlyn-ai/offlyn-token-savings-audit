# Sample Meeting: 60-Minute Meeting

This example shows the token and cost comparison for a standard 60-minute meeting using default assumptions. This is the primary reference meeting duration used throughout the audit.

## Meeting Parameters

| Parameter | Value |
|-----------|------:|
| Duration | 60 minutes |
| Speaking rate | 150 words/minute |
| Tokens per word | 1.3 |
| Transcript tokens | 11,700 |
| Q&A queries | 5 |
| Follow-up drafts | 1 |

## Cloud-First Token Breakdown

| Component | Input Tokens | Output Tokens |
|-----------|------------:|-------------:|
| Summarization | 11,700 | 1,200 |
| Action items | 11,700 | 800 |
| Q&A (5 queries) | 10,000 | 2,500 |
| Memory consolidation | 11,700 | 750 |
| Follow-up (1 draft) | 2,000 | 400 |
| Embedding | 11,700 | — |
| **LLM input total** | **47,100** | — |
| **LLM output total** | — | **5,650** |
| **Embedding tokens** | **11,700** | — |
| **Cloud billable tokens** | **64,450** | — |

## Cost Comparison

| Architecture | Cloud API Cost | Local Compute Cost | Total Cost |
|--------------|---------------:|-------------------:|-----------:|
| Cloud-first | ~$0.53 | $0.00 | ~$0.53 |
| Offline-first | $0.00 | ~$0.0075 | ~$0.0075 |
| Hybrid router | ~$0.008 | ~$0.0075 | ~$0.016 |

## Savings Summary

| Metric | Offline-First | Hybrid Router |
|--------|-------------:|-------------:|
| Tokens avoided | 64,450 | ~63,096 |
| Token reduction | 100% | ~97.9% |
| Cost avoided | ~$0.53 | ~$0.52 |

## Monthly Scaling (20 meetings/month, solo user)

| Architecture | Monthly Cost | Annual Cost |
|--------------|------------:|------------:|
| Cloud-first | ~$10.69 | ~$128.28 |
| Offline-first | ~$0.15 | ~$1.80 |
| Hybrid router | ~$0.32 | ~$3.79 |

## Enterprise Scaling (1,000 meetings/month)

| Architecture | Monthly Cost | Annual Cost |
|--------------|------------:|------------:|
| Cloud-first | ~$534.50 | ~$6,414 |
| Offline-first | ~$7.50 | ~$90 |
| Hybrid router | ~$15.80 | ~$189.60 |
| **Annual savings (offline)** | — | **~$6,324** |
| **Annual savings (hybrid)** | — | **~$6,224** |

## Notes

- The 60-minute meeting is the standard benchmark reference.
- Cloud-first cost is dominated by transcription ($0.36) and LLM input ($0.12).
- Hybrid achieves near-offline savings because most tasks stay local and fallback sends compact context.
- All values are computed from configurable defaults in `assumptions/`.
