# Offlyn Clipper Offline-First Processing

This document describes the Offlyn Clipper architecture and explains why its default cloud token usage is zero.

## Local-First Invariant

Every intelligence feature in Offlyn Clipper runs locally on Apple Silicon. By default:

- Zero cloud API calls for intelligence features.
- No meeting transcript, audio, embeddings, summaries, Q&A, or memory leaves the device.
- All AI inference uses local MLX models.
- Functionality is identical regardless of connectivity state.

## Native macOS Architecture

- Built in Swift/SwiftUI.
- Apple Silicon only: M1–M4.
- macOS 14+.
- 100% offline-capable.
- All AI inference runs via MLX Swift.

## Local Model Table

| Model | Purpose | Size | Runtime |
|-------|---------|-----:|---------|
| Whisper Large V3 Turbo 8-bit | Speech-to-text | ~809 MB | MLX Whisper |
| Gemma 4 E4B 4-bit | Summary, tasks, key moments, Q&A | ~2.9 GB | MLX Swift LM |
| Gemma 4 E2B 4-bit | Lighter LLM for 8GB Macs | ~2.1 GB | MLX Swift LM |
| BGE-Base-EN v1.5 | 768-dim embeddings | ~270 MB | MLX Embedders |

Total one-time model download: approximately 3.2–4.0 GB.

No per-query cloud API cost after download.

## Processing Pipeline

1. **Audio capture**: AVAudioEngine captures microphone and system audio. Output: M4A file.
2. **Transcription**: Whisper Large V3 Turbo transcribes full audio locally. Target: less than 2x real time.
3. **Speaker diarization**: Local speaker embedding model labels who spoke when.
4. **Summarization**: Gemma 4 processes transcript locally.
   - Transcripts ≤ 2,400 words: single "stuff" pass.
   - Transcripts > 2,400 words: map-reduce-segmented pipeline.
5. **Task/action item extraction**: Gemma 4 extracts structured tasks from transcript.
6. **Key moment extraction**: Gemma 4 identifies important moments with timestamps.
7. **Embedding generation**: BGE-Base encodes chunks into 768-dimensional vectors.
8. **Memory consolidation**: Gemma 4 compresses daily notes into daily digest and weekly digest.

## Local Search and Retrieval

- **Full-text search**: SQLite FTS5. Target latency: under 200 ms.
- **Semantic search**: Local HNSW vector index with cosine similarity.
- **Hybrid search**: Reciprocal rank fusion merges lexical and semantic results. Target latency: under 500 ms.
- **Answer composition**: Gemma 4 generates answers from top retrieved results with citations. Target latency: under 2 seconds.

## Live Meeting Intelligence

- Live context engine suggests relevant questions and intent chips during meetings.
- LocalToolRouter chooses retrieval tools before Gemma invocation.
- "Ask what you missed" supports real-time Q&A against live transcript using local LLM.

## Document Intelligence

- PDF text extraction via PDFKit.
- OCR via Apple Vision.
- Topic extraction via NLTagger plus Gemma 4.
- Document Q&A via retrieval plus Gemma 4 generation.
- All local.

## Offline Packs

Pre-processes documents, notes, and search indexes for field use.

Tracks readiness:
- Files local
- Search indexes built
- OCR complete
- Topics extracted
- Shows explicit "Ready for offline work" status

## Hardware Profiles

| Profile | RAM | Description |
|---------|----:|-------------|
| Constrained | 8 GB | MacBook Air. Uses Gemma 4 E2B. |
| Standard | 16 GB | Most MacBook Pros. Uses Gemma 4 E4B. |
| Performance | 32 GB+ | Pro/Max chips. Full pipeline headroom. |

- Sequential model loading: only one large model in memory at a time.
- Thermal management pauses inference at serious or critical thermal states.
- Core guarantee: all features work on supported Apple Silicon Macs, including 8 GB MacBook Air.

## Connectivity Awareness

Connectivity states:
- `online`
- `limitedConnection`
- `offline`
- `fieldMode`

Field Mode toggle enables intentional offline operation. App functionality is identical regardless of connectivity state.

## Local Compute and Electricity Estimate

Apple Silicon active AI inference power: 15–30W (midpoint: 25W).

**Formula:**
```
kWh = watts / 1000 × hours
electricity_cost = kWh × electricity_price_per_kWh
```

**Example (60-minute meeting):**
- Local processing at 25W for 1 hour = 0.025 kWh
- At $0.30/kWh, local energy cost = $0.0075

Compare to cloud-first cost of ~$0.53 for the same meeting.

## What Still Costs Money

- One-time model download bandwidth (~3.2–4.0 GB).
- Local electricity during inference.
- Hardware purchase (Mac with Apple Silicon).
- Developer time to build and maintain local AI pipeline.

## Limitations

- Local model quality depends on model size and quantization level.
- Complex reasoning tasks may benefit from larger cloud models.
- First-run model download requires internet.
- Processing speed depends on available thermal headroom and chip generation.
- Gemma 4 E2B (for 8 GB Macs) has lower capacity than E4B.
