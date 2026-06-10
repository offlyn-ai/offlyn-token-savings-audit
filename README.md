# Offlyn Token Savings Audit

**Token, cost, carbon, water, privacy, and SCI-AI reporting for cloud-first, local-first, and hybrid AI workflows.**

> Useful intelligence. Fewer tokens. Lower watts. Less cloud water.

---

Offlyn Token Savings Audit is a transparent benchmark framework for estimating how many cloud AI tokens, API dollars, cloud-side emissions, and datacenter cooling water can be avoided when meeting intelligence runs locally or through a local-first hybrid router instead of a cloud-first AI pipeline. It includes SCI-AI-aligned reporting with AI-native functional units for enterprise GreenOps and FinOps decision support.

This repository compares three architectures:

1. **Cloud-first meeting AI notepad** — all intelligence via cloud APIs
2. **Offlyn Clipper offline-first local AI** — all intelligence on Apple Silicon
3. **Hybrid local-first router with selective cloud fallback** — local by default, cloud when needed

> **Disclaimer**: This repository does not make proprietary claims about any specific third-party meeting app. The "cloud-first meeting AI notepad" baseline is a configurable architecture model used to estimate the cost of workflows where transcription, summarization, embeddings, Q&A, and memory consolidation are handled by cloud APIs. Update the assumptions to match your actual provider, model, retention policy, routing policy, and workload.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Why Token Savings Matter](#why-token-savings-matter)
3. [The Three Architectures Compared](#the-three-architectures-compared)
4. [What Offlyn Clipper Runs Locally](#what-offlyn-clipper-runs-locally)
5. [What the Cloud-First Baseline Models](#what-the-cloud-first-baseline-models)
6. [What the Hybrid Router Models](#what-the-hybrid-router-models)
7. [Methodology](#methodology)
8. [Per-Meeting Token Model](#per-meeting-token-model)
9. [Cost Model](#cost-model)
10. [Quality Model](#quality-model)
11. [Privacy Model](#privacy-model)
12. [Carbon and Energy Model](#carbon-and-energy-model)
13. [SCI-AI-Aligned Reporting](#sci-ai-aligned-reporting)
14. [Water Use Reporting](#water-use-reporting)
15. [Example Results](#example-results)
16. [Team-Scale Savings](#team-scale-savings)
17. [Best-Fit Use Cases by Architecture](#best-fit-use-cases-by-architecture)
18. [How to Update Assumptions](#how-to-update-assumptions)
19. [How to Run the Calculator](#how-to-run-the-calculator)
20. [Enterprise Audit Tiers](#enterprise-audit-tiers)
21. [Claims Policy](#claims-policy)
22. [Limitations](#limitations)
23. [License](#license)

---

## Executive Summary

Using default assumptions, a 60-minute meeting with 5 Q&A queries generates approximately **64,450 cloud billable tokens** under a cloud-first architecture. The offline-first architecture avoids **100%** of these tokens. Under the default modeled 60-minute meeting-intelligence scenario, the hybrid local-first router reduces cloud billable tokens by **97.9%** versus the configurable cloud-first baseline, escalating only compact context for selected fallback tasks.

| Metric | Cloud-First Baseline | Offlyn Clipper Offline-First | Hybrid Local-First Router |
|--------|---------------------:|----------------------------:|-------------------------:|
| Cloud transcription | yes | no | no by default |
| Cloud summarization | yes | no | only on fallback (~5%) |
| Cloud embeddings | yes | no | no by default |
| Cloud Q&A | yes | no | selected questions (~20%) |
| Cloud memory | yes | no | no by default |
| Raw transcript leaves device | yes | no | no by default |
| Cloud tokens (60-min meeting) | 64,450 | 0 | ~1,354 |
| API cost (60-min meeting) | ~$0.53 | $0.00 | ~$0.008 |
| Local compute cost | ~$0.00 | ~$0.0075 | ~$0.0075 |
| Offline functionality | limited | full | core features full |
| Answer quality | high for complex tasks | strong for routine/private tasks | best cost-quality balance |
| Privacy exposure | highest | lowest | low |
| Best for | cloud-native teams | regulated/offline/private teams | enterprises balancing quality and savings |

---

## SCI for AI-aligned Disclosure

This repository includes a public Green Software Foundation SCI for AI-aligned disclosure package for a modeled 60-minute meeting intelligence workflow.

The disclosure compares cloud-first, local-first, and hybrid local-first AI routing across:

- Cloud tokens
- API cost
- Incremental local energy
- Operational carbon intensity
- Answer-quality preservation
- Privacy exposure
- Network transfer
- Supplemental datacenter cooling-water impact

The default calculation is a Consumer SCI operational proxy. It is ISO/IEC 21031:2024-informed and designed for architecture comparison, FinOps, GreenOps, and enterprise sustainability readiness.

This disclosure is self-attested and modeled. It is not a carbon credit, offset, certified emissions reduction, carbon-neutrality claim, or formal ISO/SCI certification unless and until a public Green Software Foundation SCI self-certification certificate is issued.

### Disclosure status

| Item | Status |
|------|--------|
| Disclosure type | SCI for AI-aligned Consumer SCI operational proxy |
| Boundary | 60-minute meeting intelligence workflow |
| Functional unit | One meeting workflow |
| Water | Supplemental metric, not included in SCI score |
| Verification | Self-attested modeled disclosure |
| Certification status | Certification-readiness package, not yet certified |

The current disclosure package is prepared for Green Software Foundation SCI self-certification submission review and should not be described as certified unless and until an official public certificate is issued.

**Key documents:**
- [`certification/sci_ai_disclosure.md`](certification/sci_ai_disclosure.md) — Main disclosure
- [`certification/assumptions_register.yml`](certification/assumptions_register.yml) — Consolidated assumptions
- [`certification/sci_ai_calculation.csv`](certification/sci_ai_calculation.csv) — Machine-readable results
- [`certification/data_sources.md`](certification/data_sources.md) — Assumption data sources
- [`certification/gsf_submission_checklist.md`](certification/gsf_submission_checklist.md) — Submission checklist

See [`certification/`](certification/) for the full disclosure package.

---

## Why Token Savings Matter

Most enterprise AI cost and privacy exposure come from repeatedly sending large meeting transcripts, audio-derived text, embeddings, retrieved context, summaries, and Q&A prompts to cloud APIs. Each meeting processed cloud-first passes the transcript through multiple pipeline stages, multiplying the token cost.

Token savings matter because:
- **Cost scales linearly**: more meetings and more Q&A = more tokens = more spend.
- **Privacy exposure scales with tokens**: every token sent represents meeting content on third-party infrastructure.
- **Many tasks are routine**: summarization, action items, and note search do not require frontier cloud models.
- **Offline work is common**: field operations, travel, and intentional disconnection need local intelligence.

---

## The Three Architectures Compared

### Architecture A: Cloud-First Meeting AI Notepad

A pipeline where transcription, summarization, embedding, Q&A, memory consolidation, and follow-up drafting are processed by cloud APIs. Produces high-quality outputs using frontier models but incurs recurring per-token cost and requires connectivity.

### Architecture B: Offlyn Clipper Offline-First Local AI

A native macOS application that runs all intelligence locally on Apple Silicon using MLX models (Whisper, Gemma 4, BGE-Base). Zero cloud tokens by default. Full functionality offline. Trades cloud cost for local compute energy.

### Architecture C: Hybrid Local-First Router

Runs all tasks locally by default using Offlyn Clipper. Selectively escalates only low-confidence, complex, or explicitly requested tasks to cloud with compact context (~20% of full transcript). Logs every escalation for audit.

---

## What Offlyn Clipper Runs Locally

| Model | Purpose | Size | Runtime |
|-------|---------|-----:|---------|
| Whisper Large V3 Turbo 8-bit | Speech-to-text transcription | ~809 MB | MLX Whisper |
| Gemma 4 E4B 4-bit | Summary, tasks, key moments, Q&A | ~2.9 GB | MLX Swift LM |
| Gemma 4 E2B 4-bit | Lighter LLM for 8 GB Macs | ~2.1 GB | MLX Swift LM |
| BGE-Base-EN v1.5 | 768-dim embeddings, semantic search | ~270 MB | MLX Embedders |

Total one-time model download: approximately 3.2–4.0 GB. No per-query cloud API cost after download.

**Local processing pipeline**: audio capture, transcription, speaker diarization, summarization, task extraction, key moment extraction, embedding generation, hybrid search (FTS5 + HNSW), Q&A answer composition, memory consolidation, document intelligence.

All features work on Apple Silicon Macs including 8 GB MacBook Air.

---

## What the Cloud-First Baseline Models

The cloud-first baseline counts token usage for:
1. Cloud transcription (per audio minute)
2. Cloud LLM summarization (full transcript input)
3. Cloud LLM action item extraction (full transcript input)
4. Cloud embedding (full transcript)
5. Cloud Q&A (retrieved context per query)
6. Cloud memory consolidation (full transcript input)
7. Cloud follow-up drafting

Each step that takes the transcript as input re-incurs the full token cost. See [benchmarks/cloud_baseline.md](benchmarks/cloud_baseline.md) for details.

---

## What the Hybrid Router Models

The hybrid router models selective cloud escalation:
- **Default**: all tasks run locally.
- **Fallback trigger**: low confidence, complex reasoning, external knowledge, or user request.
- **What is sent**: compact context (local summary + top snippets + question), not the full transcript.
- **What is never sent**: raw audio, full transcript, embeddings, memory consolidation.

Default fallback rates: summary 5%, action items 5%, Q&A 20%, follow-up 15%, memory 0%.

See [benchmarks/hybrid_router.md](benchmarks/hybrid_router.md) for full routing policy.

---

## Methodology

All calculations derive from configurable assumptions in the `assumptions/` directory:
- [`pricing.yml`](assumptions/pricing.yml) — API rates, electricity cost
- [`workload.yml`](assumptions/workload.yml) — speaking rate, token ratios, meeting profiles
- [`routing.yml`](assumptions/routing.yml) — hybrid fallback rates, compact context ratio
- [`quality.yml`](assumptions/quality.yml) — quality dimension scores and weights
- [`carbon.yml`](assumptions/carbon.yml) — carbon proxy parameters

Formulas are documented in [analysis/token_savings_calculator.md](analysis/token_savings_calculator.md) and implemented in [scripts/calculate_savings.py](scripts/calculate_savings.py).

---

## Per-Meeting Token Model

```
transcript_tokens = meeting_minutes × words_per_minute × tokens_per_word
```

| Duration | Transcript Tokens | Cloud-First Total Billable | Hybrid Total Billable |
|---------:|------------------:|---------------------------:|----------------------:|
| 30 min | 5,850 | 40,100 | ~844 |
| 60 min | 11,700 | 64,450 | ~1,354 |
| 90 min | 17,550 | 89,100 | ~1,904 |

The offline-first architecture has 0 cloud billable tokens for all durations.

---

## Cost Model

Default pricing (configurable):
- Cloud transcription: $0.006/audio minute
- Cloud LLM input: $2.50 per 1M tokens
- Cloud LLM output: $10.00 per 1M tokens
- Cloud embedding: $0.02 per 1M tokens
- Local electricity: $0.30/kWh

| Duration | Cloud-First Cost | Offline-First Cost | Hybrid Cost |
|---------:|-----------------:|-------------------:|------------:|
| 30 min | ~$0.35 | ~$0.004 | ~$0.009 |
| 60 min | ~$0.53 | ~$0.008 | ~$0.016 |
| 90 min | ~$0.73 | ~$0.011 | ~$0.023 |

---

## Quality Model

Quality is assessed using a weighted rubric across 9 dimensions. Scores are modeled defaults (1–5 scale), not measured benchmarks.

| Architecture | Weighted Quality Score | Privacy Score | Offline Resilience |
|--------------|:----------------------:|:-------------:|:------------------:|
| Cloud-first | 4.22 | 2.0 | 0.20 |
| Offline-first | 4.05 | 5.0 | 1.00 |
| Hybrid router | 4.42 | 4.3 | 0.90 |

See [benchmarks/quality_methodology.md](benchmarks/quality_methodology.md) for the full rubric.

---

## Privacy Model

| Data Type | Cloud-First | Offline-First | Hybrid |
|-----------|:-----------:|:-------------:|:------:|
| Raw audio | potentially sent | stays local | stays local |
| Full transcript | sent to cloud | stays local | stays local |
| Embeddings | sent to cloud | stays local | stays local |
| Q&A context | sent per query | stays local | compact context on fallback |
| Memory | sent to cloud | stays local | stays local |

See [analysis/privacy_value.md](analysis/privacy_value.md) for enterprise privacy analysis.

---

## Carbon and Energy Model

Carbon estimates are **directional and assumption-based**. The SCI-AI calculator uses 0.50 gCO2e per 1,000 cloud tokens (midpoint) and an incremental local energy model (5W above device baseline).

| Architecture | Cloud CO2e (60-min) | Local Incremental CO2e (60-min) | Total Consumer CO2e |
|--------------|:-------------------:|:-------------------------------:|:-------------------:|
| Cloud-first | 32.2 g | 0 g | 32.2 g |
| Offline-first | 0 g | 1.75 g | 1.75 g |
| Hybrid | 0.68 g | 1.75 g | 2.43 g |

Local CO2e uses the **incremental** energy model: only the additional power drawn for AI inference above the device's idle baseline (5W midpoint vs 25W total device). See [analysis/energy_methodology.md](analysis/energy_methodology.md).

See [analysis/carbon_methodology.md](analysis/carbon_methodology.md) for full methodology and sensitivity analysis.

---

## SCI-AI-Aligned Reporting

This repository includes an SCI-AI-aligned reporting model for comparing AI workflow carbon intensity across cloud-first, local-first, and hybrid architectures.

The default reporting boundary is **Consumer SCI**, covering operational AI consumption: inference, orchestration, retrieval, storage, observability, network transfer, client-side energy, and model/tool connectors.

For meeting intelligence workflows, the audit reports carbon intensity using AI-native functional units:

- gCO2e per meeting hour
- gCO2e per second of audio processed
- gCO2e per transcript
- gCO2e per 1,000 cloud tokens
- gCO2e per accepted summary
- gCO2e per workflow execution

| Functional Unit | Cloud-First | Offline-First | Hybrid |
|-----------------|------------:|-------------:|-------:|
| gCO2e / meeting hour | 32.2 | 1.75 | 2.43 |
| gCO2e / second audio | 0.0090 | 0.0005 | 0.0007 |
| gCO2e / workflow execution | 32.2 | 1.75 | 2.43 |

These are modeled estimates for architecture comparison and decision support. They are not carbon credits, offsets, certified emissions reductions, or ISO/SCI certifications.

See [analysis/sci_ai_methodology.md](analysis/sci_ai_methodology.md) for the full SCI-AI framework.

---

## Water Use Reporting

Datacenter cooling water is reported as a **supplemental** AI resource efficiency metric (not part of the SCI carbon formula).

| Architecture | Direct Datacenter Water (60-min) | Avoided vs Cloud-First |
|--------------|:--------------------------------:|:----------------------:|
| Cloud-first | 0.147 L | -- |
| Offline-first | 0 L | 0.147 L |
| Hybrid | 0.003 L | 0.144 L |

Local devices do not use datacenter-style evaporative cooling. This metric estimates only direct datacenter cooling water demand avoided.

See [analysis/water_methodology.md](analysis/water_methodology.md) for methodology and caveats.

---

## Example Results

### 60-Minute Meeting (Default Assumptions)

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Cloud billable tokens | 64,450 | 0 | 1,354 |
| Transcription cost | $0.3600 | $0.0000 | $0.0000 |
| LLM cost | $0.1743 | $0.0000 | $0.0083 |
| Embedding cost | $0.0002 | $0.0000 | $0.0000 |
| Total cloud cost | $0.5345 | $0.0000 | $0.0083 |
| Local compute cost | $0.0000 | $0.0075 | $0.0075 |
| **Total cost** | **$0.5345** | **$0.0075** | **$0.0158** |
| Token reduction vs cloud-first | — | 100% | 97.9% |

See [analysis/generated_results.md](analysis/generated_results.md) for full 30/60/90-minute tables.

---

## Team-Scale Savings

### Enterprise Team: 1,000 meetings/month, 60-min average

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Monthly cloud tokens | 64,450,000 | 0 | 1,354,000 |
| Monthly cost | ~$534 | ~$7.50 | ~$15.80 |
| Annual cost | ~$6,414 | ~$90 | ~$190 |
| **Annual savings vs cloud-first** | — | **~$6,324** | **~$6,224** |

### Solo User: 20 meetings/month

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Monthly cost | ~$10.69 | ~$0.15 | ~$0.32 |
| Annual cost | ~$128 | ~$1.80 | ~$3.79 |
| Annual savings | — | ~$126 | ~$124 |

---

## Best-Fit Use Cases by Architecture

### Offline-First (Offlyn Clipper)
- Regulated industries: healthcare, legal, finance, defense
- Offline field operations
- Maximum privacy requirements
- Cost elimination (zero cloud API)
- Predictable, routine meeting workflows

### Hybrid Local-First Router
- Enterprises balancing quality and cost
- Teams needing occasional complex reasoning or external knowledge
- Organizations building toward local-first with cloud safety net
- Mixed connectivity environments

### Cloud-First
- Teams without Apple Silicon devices
- Workflows requiring constant frontier model access
- Cross-platform requirements
- Organizations with established cloud data policies

---

## How to Update Assumptions

All configurable parameters live in YAML files:

```
assumptions/
├── pricing.yml      # API rates, electricity cost
├── workload.yml     # Speaking rate, meeting profiles, scenarios
├── routing.yml      # Hybrid fallback rates, compact context ratio
├── quality.yml      # Quality scores and weights
└── carbon.yml       # Carbon proxy parameters
```

Edit any file to match your organization's actual values, then re-run the calculator.

---

## How to Run the Calculator

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Generate Token/Cost Results

```bash
python scripts/calculate_savings.py
```

This writes comparison tables to `analysis/generated_results.md`.

### Generate SCI-AI Results

```bash
python scripts/calculate_sci_ai.py
```

This writes SCI-AI functional unit tables to `analysis/generated_sci_ai_results.md`.

### Render Tables to Stdout

```bash
python scripts/render_tables.py
```

### Run Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## Enterprise Audit Tiers

### Tier 1: Self-Serve AI Resource Audit

- Token, cost, carbon, water, privacy, and Consumer SCI-AI operational proxy estimates.
- Update assumptions with your pricing and workload.
- Run the calculator on default or exported meeting data.
- Get architecture comparison tables with SCI-AI functional units.
- Zero cost to evaluate.

### Tier 2: Forward-Deployed GreenOps Audit

- Offlyn engineers instrument real workflows.
- Measure actual routing, fallback rate, transcript length, cloud calls, and local runtime metrics.
- Produce workflow-level Consumer SCI, token savings, quality, privacy, water, and carbon report.
- Custom recommendations for your workload with ESG/FinOps/GreenOps exports.

### Tier 3: Offline AI Roadmap + Assurance Packet

- Architecture design across meetings, documents, field workflows, and edge devices.
- Hybrid routing implementation with measurement instrumentation.
- ESG / FinOps / GreenOps reporting exports.
- Third-party verification readiness.
- Optional Provider SCI modeling for custom model training or fine-tuning.
- Full deployment plan with audit traces and privacy policy.

---

## Supported Workflows

This framework is designed to extend beyond meeting intelligence to any AI workflow where local-first processing can avoid cloud resources.

| Workflow | Status | Description |
|----------|--------|-------------|
| Meeting Intelligence | **Active** | Transcription, summarization, action items, Q&A, memory |
| Document Q&A | Planned | PDF/document processing, local RAG, on-device Q&A |
| Field Operations | Planned | Offline pack processing, edge inference, selective sync |
| Code Review | Planned | Local code analysis, diff summarization, PR assistance |
| Customer Support | Planned | Ticket classification, response drafting, knowledge base |

See [`assumptions/workflows.yml`](assumptions/workflows.yml) for the extensibility schema.

---

## Machine-Readable Exports

For FinOps/GreenOps dashboard integration, export audit results in JSON or CSV:

```bash
python scripts/export_audit.py --format json -o output/audit_run.json
python scripts/export_audit.py --format csv -o output/audit_run.csv
```

Output conforms to [`schemas/audit_run.schema.json`](schemas/audit_run.schema.json) and includes all 10 dimensions across all architectures, plus SCI-AI functional units.

---

## Claims Policy

This repository uses SCI-AI-aligned, ISO/IEC 21031:2024-informed methodology. All outputs are modeled estimates for architecture decision support.

**Allowed**: "SCI-AI-aligned," "modeled estimate," "operational SCI-AI proxy," "estimated avoided cloud inference emissions," "assurance-ready methodology."

**Disallowed**: "ISO certified," "SCI certified," "carbon neutral," "zero carbon AI," "water-free AI," "verified emissions reduction," "carbon credit," "offset."

See [analysis/claims_policy.md](analysis/claims_policy.md) for the full claims framework.

---

## Limitations

- Token estimates use approximations (1 word ≈ 1.3 tokens, 150 words/minute). Actual values vary.
- Quality scores are modeled rubric defaults, not measured benchmarks, unless stated otherwise.
- Carbon estimates are directional. Real emissions depend on datacenter location, hardware, and grid mix.
- The cloud-first baseline is a configurable architecture model, not a description of any specific product.
- Local compute estimates assume midpoint power draw (25W for cost, 5W incremental for carbon). Actual varies by chip, workload, and thermal state.
- Pricing changes frequently. Update `assumptions/pricing.yml` with current rates.
- This framework does not measure actual inference quality; use human evaluation for production decisions.
- Offline-first requires Apple Silicon Mac. Not applicable to other platforms without adaptation.

---

## Enterprise Engagement

Interested in an AI Resource Avoidance audit for your organization?

| | Self-Serve | Forward-Deployed | Full Roadmap |
|---|---|---|---|
| **What** | Run calculator with your assumptions | Offlyn engineers measure real workloads | Architecture design + deployment plan |
| **Output** | JSON/CSV + markdown tables | Custom SCI-AI report | Audit traces + assurance packet |
| **Timeline** | Immediate | 2-4 weeks | 4-8 weeks |
| **Cost** | Free (open source) | Contact us | Contact us |

**Get started:**
- Self-serve: Clone this repo and run `python scripts/export_audit.py`
- Enterprise: [hello@offlyn.ai](mailto:hello@offlyn.ai) | [offlyn.ai](https://offlyn.ai)
- Contributing: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

Apache License 2.0. See [LICENSE](LICENSE).

---

*All values in this document use configurable defaults. Run `python scripts/calculate_savings.py` to regenerate with your assumptions.*
