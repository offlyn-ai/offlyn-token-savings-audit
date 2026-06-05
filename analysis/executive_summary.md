# Executive Summary: AI Resource Avoidance Audit

> Reduce AI operating cost and sustainability impact — fewer cloud tokens, less water, lower carbon.

## Overview

This audit benchmarks three AI architectures across 10 enterprise dimensions: cloud tokens, API cost, energy, carbon intensity (SCI-AI), water, privacy, network transfer, quality, resilience, and local compute. The goal is to help enterprises identify which AI workflows can move to local inference, which should remain in the cloud, and which benefit from a hybrid router — and to quantify the resource, cost, and environmental impact of each choice.

## The Three Architectures

| | Cloud-First Baseline | Offlyn Clipper Offline-First | Hybrid Local-First Router |
|---|---|---|---|
| **How it works** | All intelligence via cloud APIs | All intelligence on Apple Silicon | Local by default, selective cloud fallback |
| **Cloud tokens** | Highest | Zero | Low (~2% of cloud-first) |
| **API cost** | Highest | Zero cloud API | Minimal cloud + local electricity |
| **Carbon** | Highest (cloud compute + cooling) | Local incremental only | Minimal cloud + local incremental |
| **Water** | Datacenter cooling water | None | Near-zero |
| **Network** | Full audio + payload upload | Zero transfer | Compact context only |
| **Privacy** | Transcripts sent to cloud | Nothing leaves device | Compact context only on fallback |
| **Offline** | Limited | Full | Core features full |
| **Best for** | Cloud-native teams | Regulated/offline/private | Enterprises balancing quality + savings |

## 10-Dimension Comparison (60-Minute Meeting)

| Dimension | Cloud-First | Offline-First | Hybrid Router | Unit |
|-----------|------------:|-------------:|-------------:|------|
| Cloud tokens | 64,450 | 0 | ~1,354 | tokens |
| API cost | $0.534 | $0.00 | $0.008 | USD |
| Local compute cost | $0.00 | $0.0075 | $0.0075 | USD |
| Cloud carbon | 32.2 | 0.0 | 0.68 | gCO2e |
| Local incremental carbon | 0.0 | 1.75 | 1.75 | gCO2e |
| Total consumer carbon | 32.2 | 1.75 | 2.43 | gCO2e |
| Datacenter water | 0.147 | 0.0 | 0.003 | liters |
| Network transfer | ~60 | 0.0 | ~0.1 | MB |
| Quality score | 4.1 | 3.9 | 4.1 | /5.0 |
| Privacy score | 2.0 | 5.0 | 4.5 | /5.0 |
| Offline resilience | 0.2 | 1.0 | 0.85 | 0-1 |

## Enterprise Team Example (1,000 meetings/month, 60-min average)

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Monthly cloud tokens | 64,450,000 | 0 | ~1,354,000 |
| Monthly API cost | ~$534 | $0 | ~$8.30 |
| Monthly cloud carbon | 32.2 kg CO2e | 0 | ~0.68 kg CO2e |
| Monthly datacenter water | 147 liters | 0 | ~3 liters |
| Monthly network transfer | ~60 GB | 0 | ~0.1 GB |
| Annual API savings vs cloud | — | ~$6,414 | ~$6,314 |
| Annual carbon avoided | — | ~386 kg CO2e | ~378 kg CO2e |

## Key Findings

**1. Most meeting AI resources are avoidable.**
A standard 60-minute meeting consumes ~64,450 cloud tokens, ~32 gCO2e, ~0.15 liters of datacenter cooling water, and ~60 MB of network transfer under a cloud-first pipeline. The offline-first architecture avoids all of them. The hybrid router avoids >97%.

**2. The cost and environmental impact compounds at scale.**
For a 50-person team with 1,000 meetings/month, annual cloud savings reach thousands of dollars. Carbon avoidance reaches hundreds of kg CO2e — equivalent to multiple transatlantic flights.

**3. Privacy and network exposure scale with cloud token usage.**
Every cloud token represents meeting content processed by third-party infrastructure. Reducing tokens directly reduces data exposure events and network egress.

**4. Water avoidance is a concrete, measurable benefit.**
Datacenter cooling water is consumed proportionally to cloud compute. Moving inference local eliminates this direct water footprint entirely.

**5. Quality remains strong for routine tasks.**
Local models (Gemma 4, Whisper Large V3 Turbo) handle summarization, action items, search, and Q&A at production quality for routine meeting intelligence. Cloud models add value primarily for complex reasoning and external knowledge.

**6. Hybrid is the practical enterprise default.**
Most enterprises benefit from running routine tasks locally and reserving cloud for genuinely difficult queries. This captures >95% of resource savings while maintaining access to frontier model quality when needed.

## SCI-AI Reporting

All carbon and energy metrics follow the Green Software Foundation SCI-AI framework (ISO/IEC 21031:2024-informed):

- **Consumer SCI boundary**: Operational carbon only (scope 2 equivalent)
- **Functional units**: gCO2e per meeting hour, per second of audio, per transcript, per workflow execution
- **Claim level**: Modeled, not verified — all outputs are estimates based on published assumptions
- **Incremental energy model**: Only the additional energy above baseline device usage is attributed to AI

## Why Each Architecture Fits

### Offline-First is Best For:
- Regulated industries (healthcare, legal, finance, defense)
- Offline field work
- Maximum privacy requirements
- Cost and resource elimination (not just reduction)
- Teams with predictable, routine meeting patterns

### Hybrid is Best For:
- Enterprises balancing quality and cost
- Teams that occasionally need complex reasoning or external knowledge
- Organizations building toward local-first with cloud safety net
- Environments with mixed connectivity

### Cloud-First Remains Useful For:
- Teams without Apple Silicon devices
- Workflows requiring latest frontier model capabilities
- Cross-platform requirements
- Organizations where cloud data policies are already established

## Enterprise Engagement

Offlyn helps enterprises reduce AI operating cost and sustainability impact by optimizing where intelligence runs: cloud, local, or hybrid. This audit identifies which workflows can move local, quantifies resource avoidance, and provides SCI-AI-aligned reporting.

### Tier 1: Self-Serve Audit
Update assumptions, run the calculator, get architecture comparison tables with JSON/CSV export for FinOps/GreenOps dashboard integration.

### Tier 2: Forward-Deployed Offlyn Audit
Offlyn engineers measure real meeting workloads and produce a custom resource avoidance, quality, privacy, SCI-AI carbon, and water report.

### Tier 3: Full Offline AI Roadmap
Architecture design across meetings, documents, field workflows, and edge devices with deployment plan and ongoing SCI-AI monitoring.

---

*All values use configurable defaults from `assumptions/`. Update with your organization's actual pricing, meeting patterns, and routing preferences. Machine-readable exports available via `scripts/export_audit.py --format json`.*
