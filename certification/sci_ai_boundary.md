# SCI Boundary Definition — Offlyn Clipper

## Disclosure Boundary

Consumer SCI operational boundary for on-device meeting intelligence.

## Software System

**Offlyn Clipper** — A native macOS application that provides AI-powered meeting intelligence running entirely on Apple Silicon devices.

## Component Inclusion Table

| Component | Included? | Method | Notes |
|-----------|-----------|--------|-------|
| On-device ASR (Whisper) | Yes | Measured | Real-time transcription, 0.86W incremental |
| On-device LLM (Gemma 4) | Yes | Measured | Summarization, action items, 12.11W incremental |
| On-device embeddings (BGE-Base) | Yes | Included in LLM | Semantic indexing |
| Audio capture | Yes | Negligible | System audio capture overhead |
| Local storage I/O | Yes | Negligible | SQLite writes, file storage |
| Network transfer | No | N/A | No network activity in default config |
| Cloud API calls | No | N/A | No cloud in default config |
| Model training | No | Out of scope | Pre-operational; Provider SCI |
| Model download | No | Amortized | One-time ~4GB; negligible per-meeting |
| Baseline device power | No | Excluded | Common to all architectures |
| Embodied hardware | No | Unavailable | No reliable allocation method |

## Shared Infrastructure

No included component runs on shared multi-tenant infrastructure. Offlyn Clipper runs entirely on end-user Apple Silicon devices. Audio capture, transcription, embedding generation, and AI inference all execute locally on the user's Mac.

There is no cloud component in the default configuration. If a future hybrid fallback mode is enabled, cloud API calls would be consumed via standard API endpoints with per-request carbon attribution using published token-based proxy factors, and would be measured and reported separately.

## Boundary Rationale

### Why Consumer SCI

This disclosure uses the Consumer SCI boundary because:
- Offlyn Clipper is end-user software running on consumer devices
- The SCI measures operational carbon during actual use
- Provider SCI (model training, deployment) is excluded as it occurred before operational use

### Why Baseline Device Power is Excluded

All Clipper users have an active Mac running. The baseline device power consumption (198 mW measured) is identical regardless of whether Clipper is processing a meeting or idle. Only the incremental inference power above this baseline is included because it represents the additional energy consumed specifically for the meeting intelligence workload.

### Why Embodied Carbon is Excluded

Embodied carbon allocation requires lifecycle assessment data for:
- End-user MacBooks (various models and generations)
- Apple Silicon chips

Reliable, publicly available allocation methodologies for consumer devices do not exist at the precision level required for meaningful disclosure. M = 0 is used with this limitation explicitly documented.

### Why Network is Excluded

Offlyn Clipper in its default configuration performs all processing locally with zero network activity. There are no API calls, no cloud uploads, and no data leaving the device. Network carbon is therefore zero.
