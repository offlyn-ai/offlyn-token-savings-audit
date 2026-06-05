# Sample Meeting: 90-Minute Meeting

This example shows the token and cost comparison for a 90-minute meeting using default assumptions. Longer meetings amplify the token savings because the transcript is larger and passed to more pipeline stages.

## Meeting Parameters

| Parameter | Value |
|-----------|------:|
| Duration | 90 minutes |
| Speaking rate | 150 words/minute |
| Tokens per word | 1.3 |
| Transcript tokens | 17,550 |
| Q&A queries | 5 |
| Follow-up drafts | 1 |

## Cloud-First Token Breakdown

| Component | Input Tokens | Output Tokens |
|-----------|------------:|-------------:|
| Summarization | 17,550 | 1,800 |
| Action items | 17,550 | 1,200 |
| Q&A (5 queries) | 10,000 | 2,500 |
| Memory consolidation | 17,550 | 1,000 |
| Follow-up (1 draft) | 2,000 | 400 |
| Embedding | 17,550 | — |
| **LLM input total** | **64,650** | — |
| **LLM output total** | — | **6,900** |
| **Embedding tokens** | **17,550** | — |
| **Cloud billable tokens** | **89,100** | — |

## Cost Comparison

| Architecture | Cloud API Cost | Local Compute Cost | Total Cost |
|--------------|---------------:|-------------------:|-----------:|
| Cloud-first | ~$0.73 | $0.00 | ~$0.73 |
| Offline-first | $0.00 | ~$0.011 | ~$0.011 |
| Hybrid router | ~$0.012 | ~$0.011 | ~$0.023 |

## Savings Summary

| Metric | Offline-First | Hybrid Router |
|--------|-------------:|-------------:|
| Tokens avoided | 89,100 | ~87,200 |
| Token reduction | 100% | ~97.9% |
| Cost avoided | ~$0.73 | ~$0.71 |

## Why Longer Meetings Amplify Savings

1. **Transcript size scales linearly**: 17,550 tokens vs. 11,700 for 60 min.
2. **Each pipeline pass re-sends the full transcript**: 3 LLM passes × 17,550 = 52,650 tokens just for transcript input.
3. **Embedding cost increases**: the full transcript is embedded.
4. **Memory consolidation sends the full transcript again**.
5. **Q&A cost is fixed** (query-count dependent, not duration-dependent), so longer meetings make the transcript-pass costs proportionally larger.

## Monthly Scaling (20 meetings/month at 90 min)

| Architecture | Monthly Cost | Annual Cost |
|--------------|------------:|------------:|
| Cloud-first | ~$14.53 | ~$174.36 |
| Offline-first | ~$0.23 | ~$2.70 |
| Hybrid router | ~$0.47 | ~$5.59 |

## Notes

- Teams with frequent long meetings (board meetings, all-hands, strategy sessions) see the largest absolute savings.
- At 90 minutes, cloud-first transcription alone costs $0.54 (90 × $0.006).
- All values are computed from configurable defaults in `assumptions/`.
