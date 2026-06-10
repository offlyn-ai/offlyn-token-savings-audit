# SCI for AI Functional Unit Definitions

## Primary Functional Unit

**One 60-minute meeting intelligence workflow.**

### Workflow Definition

A single 60-minute meeting processed through the following pipeline:

1. Audio capture and transcription (ASR)
2. Speaker diarization
3. Summary generation
4. Action item extraction
5. Key moment identification
6. Q&A-ready memory indexing (embedding + retrieval)
7. Follow-up draft generation

This represents a complete end-to-end meeting intelligence workflow from audio input to actionable outputs.

## Secondary Functional Units

| Functional Unit | Definition | Use Case |
|----------------|------------|----------|
| gCO2e per meeting hour | Total operational carbon / meeting hours | Normalizes across meeting durations |
| gCO2e per second of audio processed | Total operational carbon / (minutes × 60) | Granular time-based comparison |
| gCO2e per transcript generated | Total operational carbon / 1 transcript | Per-document intensity |
| gCO2e per 1,000 cloud tokens | Cloud carbon / (cloud tokens / 1000) | Cloud-specific cost intensity |
| gCO2e per accepted summary | Total operational carbon / 1 summary | Output-quality-weighted intensity |
| gCO2e per workflow execution | Total operational carbon / 1 workflow | Equivalent to primary unit for single-meeting |

## Rationale

### Why Workflow-Level Metrics

Token-only metrics (gCO2e per 1,000 tokens) are useful for cloud API cost analysis but insufficient for full architecture comparison because:

1. **Local-first architectures use zero cloud tokens** — a token-only metric produces division-by-zero or N/A for offline scenarios.
2. **Local energy is not measured in tokens** — local inference consumes watts, not billable tokens.
3. **Workflow captures the full pipeline** — transcription, embedding, retrieval, summarization, and generation are all part of the carbon footprint.
4. **Enterprise decisions are per-workflow** — "How much does it cost to process one meeting?" is the natural unit for budgeting.

### Why Multiple Units

Different stakeholders need different views:
- **FinOps teams** prefer per-token or per-dollar metrics
- **GreenOps teams** prefer per-workflow or per-hour metrics
- **Engineering teams** prefer per-second metrics for performance optimization
- **Executive reporting** prefers per-workflow for simplicity

Providing multiple functional units allows the same underlying data to serve all audiences without recalculation.

## Functional Unit Count

For the default 60-minute disclosure:
- Meeting hours: 1.0
- Seconds of audio: 3,600
- Transcripts generated: 1
- Workflow executions: 1
- Accepted summaries: 1
- Cloud tokens: varies by architecture (0 for local-first, ~64,450 for cloud-first)
