# Cloud-First Meeting AI Notepad Baseline

This document models what a cloud-first meeting intelligence workflow may consume when transcription, summarization, embeddings, Q&A, and memory consolidation are handled by cloud APIs.

## Pipeline Diagram

```
Audio Input
    │
    ▼
[Cloud Transcription API] ──► transcript tokens
    │
    ▼
[Cloud LLM: Summarization] ──► transcript in, summary out
    │
    ▼
[Cloud LLM: Action Items] ──► transcript in, actions out
    │
    ▼
[Cloud LLM: Key Moments] ──► transcript in, moments out
    │
    ▼
[Cloud Embedding API] ──► transcript tokens embedded
    │
    ▼
[Cloud LLM: Q&A × N queries] ──► retrieved context + question in, answer out
    │
    ▼
[Cloud LLM: Memory Consolidation] ──► transcript in, memory digest out
    │
    ▼
[Cloud LLM: Follow-up Drafting] ──► context in, draft out
```

Each downstream step re-sends the transcript or derived context to cloud APIs, creating a repeated context penalty.

## What Is Counted

- Cloud transcription (per audio minute)
- Cloud LLM input tokens for summarization, action items, key moments, Q&A, memory, and follow-ups
- Cloud LLM output tokens for each task
- Cloud embedding input tokens
- Cumulative cost across all pipeline stages

## What Is Not Counted

- Local audio capture cost (negligible)
- Network bandwidth for uploading audio/text
- Cloud storage or retention charges
- UI rendering or client-side processing
- Any vendor-specific discounts, caching, or batching optimizations

## Per-Meeting Token Estimates

All values use configurable defaults from `assumptions/workload.yml` and `assumptions/pricing.yml`.

### 30-Minute Meeting

| Component | Input Tokens | Output Tokens |
|-----------|------------:|-------------:|
| Transcript | 5,850 | — |
| Summarization | 5,850 | 800 |
| Action items | 5,850 | 500 |
| Embedding | 5,850 | — |
| Q&A (5 queries) | 10,000 | 2,500 |
| Memory consolidation | 5,850 | 500 |
| Follow-up (1 draft) | 2,000 | 400 |
| **LLM input total** | **29,550** | — |
| **LLM output total** | — | **4,700** |
| **Embedding tokens** | **5,850** | — |
| **Cloud billable tokens** | **40,100** | — |

### 60-Minute Meeting

| Component | Input Tokens | Output Tokens |
|-----------|------------:|-------------:|
| Transcript | 11,700 | — |
| Summarization | 11,700 | 1,200 |
| Action items | 11,700 | 800 |
| Embedding | 11,700 | — |
| Q&A (5 queries) | 10,000 | 2,500 |
| Memory consolidation | 11,700 | 750 |
| Follow-up (1 draft) | 2,000 | 400 |
| **LLM input total** | **47,100** | — |
| **LLM output total** | — | **5,650** |
| **Embedding tokens** | **11,700** | — |
| **Cloud billable tokens** | **64,450** | — |

### 90-Minute Meeting

| Component | Input Tokens | Output Tokens |
|-----------|------------:|-------------:|
| Transcript | 17,550 | — |
| Summarization | 17,550 | 1,800 |
| Action items | 17,550 | 1,200 |
| Embedding | 17,550 | — |
| Q&A (5 queries) | 10,000 | 2,500 |
| Memory consolidation | 17,550 | 1,000 |
| Follow-up (1 draft) | 2,000 | 400 |
| **LLM input total** | **64,650** | — |
| **LLM output total** | — | **6,900** |
| **Embedding tokens** | **17,550** | — |
| **Cloud billable tokens** | **89,100** | — |

## Repeated Context Penalty

In a cloud-first architecture, the full transcript is sent as input to multiple LLM tasks (summarization, action items, key moments, memory). Each pass re-incurs input token cost. With 5 Q&A queries, additional retrieved context is sent each time.

For a 60-minute meeting, the transcript alone (11,700 tokens) appears in at least 3 separate LLM passes plus the embedding pass, totaling 46,800 tokens just from transcript re-sends before Q&A expansion.

## Q&A Token Expansion

Each Q&A query sends approximately 2,000 input tokens (retrieved context + question) and receives approximately 500 output tokens. With 5 queries per meeting, this adds 10,000 input tokens and 2,500 output tokens per meeting.

Q&A cost grows linearly with query count. Teams that use meeting search heavily may generate significantly more.

## Cost Breakdown (60-Minute Meeting, Default Pricing)

| Cost Component | Amount |
|----------------|-------:|
| Transcription (60 min × $0.006/min) | $0.3600 |
| LLM input (47,100 tokens) | $0.1178 |
| LLM output (5,650 tokens) | $0.0565 |
| Embedding (11,700 tokens) | $0.0002 |
| **Total per meeting** | **$0.5345** |

## Limitations

- This model does not account for caching, prompt optimization, or batch processing that may reduce actual token usage.
- Real-world pricing varies by provider, model version, commitment tier, and volume discounts.
- Some providers may charge differently for audio transcription (per-second vs. per-minute vs. per-token).
- Actual transcript length varies by speaker density, silence, and conversation pace.

## What This Baseline Does Not Claim

This baseline does not describe or accuse any specific product. Some meeting tools may capture audio locally, avoid storing raw audio, use hybrid transcription, or use local preprocessing. This document models a cloud-dependent architecture so enterprises can estimate the potential savings from moving eligible steps to local inference.
