# SCI Self-Certification Disclosure — Offlyn Clipper

## Reviewer Quick Summary

| Item | Value |
|------|-------|
| Organization | Offlyn.ai |
| Software system | Offlyn Clipper |
| Software version | 1.0 (beta-2026-07) |
| Software URL | https://clipper.offlyn.ai/ |
| SCI score | **0.35 gCO2eq per meeting workflow** |
| Measurement period | 2026-07-22 to 2026-07-22 (benchmark) |
| Boundary | Consumer SCI operational boundary |
| Functional unit | One 60-minute meeting intelligence workflow |
| Formula | SCI = (E × I + M) / R |
| Embodied emissions | Excluded; M = 0 (reliable allocation data unavailable) |
| Verification status | Self-certified, measured |
| Signatory | Joel Nishant Reddy, Co-founder, Offlyn.ai |

---

## Section 1 — About You and Your Software

**Organization name:** Offlyn.ai

**Contact name:** Joel Nishant Reddy

**Contact email:** [REDACTED - provided in original submission]

**Software name:** Offlyn Clipper

**Software version:** 1.0 (beta-2026-07)

**Software URL:** https://clipper.offlyn.ai/

**What does it do?**

Offlyn Clipper is a native macOS application that provides AI-powered meeting intelligence running entirely on-device. It captures audio from Mac system audio, transcribes speech to text using on-device Whisper (MLX), and generates meeting summaries, action items, and searchable notes using on-device LLM inference (Gemma 4 via MLX). All AI processing runs locally on Apple Silicon with zero cloud API calls in the default configuration.

---

## Section 2 — Your SCI Score

**SCI score:** 0.35 gCO2eq per meeting workflow

**Measurement period:** 2026-07-22 to 2026-07-22 (single-day benchmark)

**Measurement method:** Direct power measurement using macOS `powermetrics` on Apple M4

**Note:** This is a representative benchmark measurement. The SCI score represents the carbon intensity of a single 60-minute meeting workflow based on measured power consumption during controlled testing.

---

## Section 3 — Software Boundary

### What's Included?

| Component | Description |
|-----------|-------------|
| On-device ASR (Whisper Large V3 Turbo) | Speech-to-text transcription, ~809 MB model, MLX runtime |
| On-device LLM (Gemma 4 E4B 4-bit) | Summary, action items, key moments, Q&A, ~2.9 GB model, MLX runtime |
| On-device embeddings (BGE-Base-EN) | Semantic search indexing, ~270 MB model, MLX runtime |
| Audio capture | System audio capture from Mac |
| Local storage | SQLite database and file storage on user device |

### What's Excluded, and Why?

| Component | Reason for exclusion |
|-----------|----------------------|
| Model training | Training occurred before operational use; outside consumer SCI boundary |
| Model download | One-time download (~4 GB); amortized over device lifetime, negligible per-meeting |
| Baseline device power | All users have an active Mac; baseline is common across all architectures |
| Cloud fallback (if enabled) | Not used in default configuration; would be measured separately if enabled |
| Embodied hardware carbon | Reliable allocation methodology unavailable for consumer devices |

### Shared Infrastructure

No included component runs on shared multi-tenant infrastructure. Offlyn Clipper runs entirely on end-user Apple Silicon devices. Audio capture, transcription, embedding generation, and AI inference all execute locally on the user's Mac.

There is no cloud component in the default configuration.

---

## Section 4 — Functional Unit (R)

**Functional unit:** One 60-minute meeting intelligence workflow

**Why this unit:** A meeting workflow is the primary unit of value delivered by Clipper. It encompasses the complete pipeline: audio capture, transcription, summarization, action item extraction, and searchable indexing.

**How counted:** Each meeting processed through Clipper from start (begin recording) to finish (summary generated) counts as one functional unit.

**Total in measurement period:** 1 meeting workflow

**Benchmark methodology:** Power consumption was measured during a controlled 60-minute meeting workflow using macOS `powermetrics`. The measurement captures one complete functional unit to establish the per-workflow SCI score. This benchmark approach is appropriate for consumer software where each user runs the software independently on their own device.

---

## Section 5 — Energy (E) and Carbon Intensity (I)

### Energy

**Total energy:** 0.00101 kWh per meeting workflow

**PUE applied:** N/A — local consumer device (no datacenter infrastructure)

**Method:** Direct power measurement using macOS `powermetrics` with incremental power calculation (active inference power minus baseline idle power)

| Component | Duration | Power (incremental) | Energy (kWh) | Data source |
|-----------|----------|---------------------|--------------|-------------|
| Transcription (Whisper) | 60 min | 0.86 W | 0.00086 | powermetrics measurement |
| Summarization (Gemma 4) | 45 sec | 12.11 W | 0.00015 | powermetrics measurement |
| **Total** | - | - | **0.00101** | - |

### Measured Power Values

| Phase | Baseline | Active | Incremental |
|-------|----------|--------|-------------|
| Idle | 198 mW | - | - |
| Transcription | 198 mW | 1,056 mW | 858 mW (0.86 W) |
| Summarization | 198 mW | 12,313 mW | 12,115 mW (12.11 W) |

### Carbon Intensity

**Carbon intensity:** 350 gCO2eq/kWh

**Location:** Global average (user location varies)

**Approach:** Location-based

**Data source:** IEA World Energy Outlook 2023, global average electricity emission factor

---

## Section 6 — Embodied Emissions (M)

**Total embodied (allocated):** 0 gCO2eq

**Justification:** Embodied carbon allocation requires lifecycle assessment data for end-user devices (MacBooks). Reliable, publicly available allocation methodologies for consumer device hardware do not exist at the precision level required for this disclosure. M = 0 is used with the understanding that this is a limitation, not an assertion that embodied emissions are zero.

---

## Section 7 — Methodology and Calculation

**Approach:** Measurement

**How you calculated your score:**

1. Power measurement was conducted on an Apple M4 Mac using macOS `powermetrics` with the `cpu_power` sampler at 1-second intervals
2. Baseline power was measured with Clipper open but idle (30 seconds)
3. Transcription power was measured during active real-time transcription (90 seconds)
4. Summarization power was measured during LLM inference for summary generation (60 seconds)
5. Incremental power was calculated as active power minus baseline power for each phase
6. Energy was calculated as incremental power × duration for each phase
7. Total operational carbon was calculated as total energy × grid carbon intensity

**Show your calculation:**

```
Energy breakdown:
  Transcription = 0.86 W × 1.0 h = 0.00086 kWh
  Summarization = 12.11 W × 0.0125 h = 0.00015 kWh
  Total E = 0.00101 kWh

E × I = 0.00101 kWh × 350 gCO2eq/kWh = 0.35 gCO2eq
M = 0 gCO2eq
R = 1 meeting workflow

SCI = (E × I + M) / R = (0.35 + 0) / 1 = 0.35 gCO2eq per meeting workflow
```

### Assumptions and Limitations

| Assumption or limitation | Justification or mitigation |
|--------------------------|----------------------------|
| Single device measurement (Apple M4) | Power varies by Apple Silicon generation; M4 represents current-generation efficiency |
| Global average grid intensity | Users should substitute region-specific values for more accurate local calculations |
| Summarization duration (45 sec) | Based on observed Gemma 4 inference time; varies with transcript length |
| Embodied emissions excluded | Reliable consumer device allocation methodology unavailable |
| Default configuration only | Cloud fallback mode, if enabled, would increase operational carbon |

---

## Attestation

See [sci_ai_attestation.md](sci_ai_attestation.md) for the signed attestation.

---

## Supporting Documents

| Document | Purpose |
|----------|---------|
| [sci_ai_boundary.md](sci_ai_boundary.md) | Complete boundary definition and component inclusion rationale |
| [sci_ai_calculation.md](sci_ai_calculation.md) | Detailed calculation methodology |
| [sci_ai_functional_unit.md](sci_ai_functional_unit.md) | Functional unit definition and rationale |
| [data_sources.md](data_sources.md) | Data sources and references |
| [limitations.md](limitations.md) | Complete limitations register |
| [measurements/](../measurements/) | Raw power measurement logs |

---

## Measurement Evidence

Power measurements were conducted on July 22, 2026, using macOS `powermetrics`. Raw log files are available in the `measurements/` directory:

- `baseline_v2_20260722_224445.log` — Baseline (idle) power measurements
- `active_v2_20260722_224445.log` — Transcription phase measurements
- `summarize_v2_20260722_224445.log` — Summarization phase measurements
- `summary_v2_20260722_224445.txt` — Measurement summary

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-06-10 | Initial modeled disclosure |
| 1.0.0 | 2026-07-22 | Revised with measured power data; single-system framing for Offlyn Clipper |
