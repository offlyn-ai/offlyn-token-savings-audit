# Executive Summary: Token Savings Audit

> Useful intelligence. Fewer tokens. Lower watts.

## Overview

This audit compares three meeting intelligence architectures on cloud token usage, API cost, answer quality, privacy exposure, and offline resilience. The goal is to help enterprises identify which AI workflows can move to local inference, which should remain in the cloud, and which benefit from a hybrid approach.

## The Three Architectures

| | Cloud-First Baseline | Offlyn Clipper Offline-First | Hybrid Local-First Router |
|---|---|---|---|
| **How it works** | All intelligence via cloud APIs | All intelligence on Apple Silicon | Local by default, selective cloud fallback |
| **Cloud tokens** | Highest | Zero | Low (~2% of cloud-first) |
| **API cost** | Highest | Zero cloud API | Minimal cloud + local electricity |
| **Privacy** | Transcripts sent to cloud | Nothing leaves device | Compact context only on fallback |
| **Offline** | Limited | Full | Core features full |
| **Best for** | Cloud-native teams | Regulated/offline/private | Enterprises balancing quality + savings |

## 60-Minute Meeting Example (Default Assumptions)

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Cloud billable tokens | 64,450 | 0 | ~1,354 |
| Cloud API cost | $0.53 | $0.00 | $0.008 |
| Local compute cost | $0.00 | $0.0075 | $0.0075 |
| Total cost | $0.53 | $0.0075 | $0.016 |
| Token reduction | — | 100% | 97.9% |

## Enterprise Team Example (1,000 meetings/month, 60-min average)

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Monthly cloud tokens | 64,450,000 | 0 | ~1,354,000 |
| Monthly API cost | ~$534 | $0 | ~$8.30 |
| Annual API cost | ~$6,414 | $0 | ~$100 |
| Annual savings vs cloud-first | — | ~$6,414 | ~$6,314 |

## Key Findings

**1. Most meeting intelligence tokens are avoidable.**
A standard 60-minute meeting generates ~64,450 cloud tokens under a cloud-first pipeline. The offline-first architecture avoids all of them. The hybrid router avoids ~97.9%.

**2. The cost difference compounds at scale.**
For a 50-person team with 1,000 meetings/month, the annual cloud API difference is measured in thousands of dollars — and grows linearly with meeting volume and Q&A usage.

**3. Privacy exposure scales with cloud token usage.**
Every cloud token represents meeting content processed by third-party infrastructure. Reducing tokens directly reduces data exposure events.

**4. Quality remains strong for routine tasks.**
Local models (Gemma 4, Whisper Large V3 Turbo) handle summarization, action items, search, and Q&A at production quality for routine meeting intelligence. Cloud models add value primarily for complex reasoning and external knowledge.

**5. Hybrid is the practical enterprise default.**
Most enterprises benefit from running routine tasks locally and reserving cloud for genuinely difficult queries. This captures >95% of token savings while maintaining access to frontier model quality when needed.

## Why Each Architecture Fits

### Offline-First is Best For:
- Regulated industries (healthcare, legal, finance, defense)
- Offline field work
- Maximum privacy requirements
- Cost elimination (not just reduction)
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

Offlyn helps enterprises reduce AI operating costs by optimizing where intelligence runs: cloud, local, or hybrid. The audit identifies which workflows can move local, which should remain cloud, and which should use selective fallback.

### Tier 1: Self-Serve Audit
Update assumptions, run the calculator, get architecture comparison tables.

### Tier 2: Forward-Deployed Offlyn Audit
Offlyn engineers measure real meeting workloads and produce a custom token savings, quality, privacy, and carbon report.

### Tier 3: Full Offline AI Roadmap
Architecture design across meetings, documents, field workflows, and edge devices with deployment plan.

---

*All values use configurable defaults from `assumptions/`. Update with your organization's actual pricing, meeting patterns, and routing preferences.*
