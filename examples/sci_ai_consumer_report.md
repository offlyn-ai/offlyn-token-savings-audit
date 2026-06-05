# SCI-AI Consumer Report

> Consumer SCI functional unit table for a sample audit period.

---

## Report Metadata

| Field | Value |
|-------|-------|
| Standard | Green Software Foundation SCI-AI |
| ISO reference | ISO/IEC 21031:2024-informed |
| Boundary | Consumer SCI |
| Reporting mode | Operational proxy |
| Claim level | Modeled, not verified |
| Embodied carbon | Excluded (data unavailable) |
| Provider SCI | Not in scope |

---

## Audit Parameters

| Parameter | Value |
|-----------|-------|
| Meeting duration | 60 minutes |
| Audio processed | 3,600 seconds |
| Transcript tokens | 11,700 |
| Cloud token carbon proxy | 0.50 gCO2e per 1,000 tokens |
| Local incremental power | 5W (above device baseline) |
| Grid intensity | 350 gCO2e/kWh |
| Datacenter PUE | 1.2 |
| Water Usage Effectiveness | 1.90 L/kWh |

---

## Consumer SCI by Architecture

### Cloud-First

| Functional Unit | Value | Unit |
|-----------------|------:|------|
| Per meeting hour | 32.225 | gCO2e/hr |
| Per second of audio | 0.008951 | gCO2e/s |
| Per transcript | 32.225 | gCO2e |
| Per 1,000 cloud tokens | 0.500 | gCO2e/1k tokens |
| Per workflow execution | 32.225 | gCO2e |
| Per accepted summary | 32.225 | gCO2e |

### Offline-First (Offlyn Clipper)

| Functional Unit | Value | Unit |
|-----------------|------:|------|
| Per meeting hour | 1.750 | gCO2e/hr |
| Per second of audio | 0.000486 | gCO2e/s |
| Per transcript | 1.750 | gCO2e |
| Per 1,000 cloud tokens | N/A | (no cloud tokens) |
| Per workflow execution | 1.750 | gCO2e |
| Per accepted summary | 1.750 | gCO2e |

### Hybrid Local-First Router

| Functional Unit | Value | Unit |
|-----------------|------:|------|
| Per meeting hour | 2.427 | gCO2e/hr |
| Per second of audio | 0.000674 | gCO2e/s |
| Per transcript | 2.427 | gCO2e |
| Per 1,000 cloud tokens | 0.500 | gCO2e/1k tokens |
| Per workflow execution | 2.427 | gCO2e |
| Per accepted summary | 2.427 | gCO2e |

---

## Carbon Breakdown

| Component | Cloud-First | Offline-First | Hybrid |
|-----------|------------:|-------------:|-------:|
| Cloud inference carbon (gCO2e) | 32.225 | 0.000 | 0.677 |
| Local incremental carbon (gCO2e) | 0.000 | 1.750 | 1.750 |
| Total consumer carbon (gCO2e) | 32.225 | 1.750 | 2.427 |

---

## Water (Supplemental, Not SCI Carbon)

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------:|-------------:|-------:|
| Direct datacenter water (L) | 0.147 | 0.000 | 0.003 |
| Avoided water vs baseline (L) | -- | 0.147 | 0.144 |

---

## Boundary Components Included

Consumer SCI for this audit includes:
- API and inference (cloud LLM, ASR, embedding calls)
- Local inference (incremental energy above device baseline)
- Retrieval (RAG pipeline, vector search)
- Embeddings (embedding generation)

Components excluded (not material or data unavailable):
- Orchestration (negligible for single-device workflows)
- Network transfer (excluded as common across architectures)
- Storage (excluded as common across architectures)
- Observability (excluded, not instrumented)
- Embodied carbon (data unavailable from cloud providers)

---

## Interpretation Guide

- **Lower Consumer SCI = more carbon-efficient per unit of work.**
- Offline-first has the lowest SCI per meeting hour because it avoids cloud inference entirely.
- Hybrid is close to offline-first because only ~2% of workload routes to cloud.
- Cloud-first has highest SCI because all inference is cloud-based.

---

## Limitations and Caveats

- These are modeled estimates using the token-proxy method.
- Real cloud inference energy varies by GPU type, model size, and utilization.
- Local incremental energy is estimated at 5W midpoint for Apple Silicon.
- Embodied carbon is excluded; full SCI-AI would include it when data is available.
- This report does not constitute a verified carbon footprint.
- See [Claims Policy](../analysis/claims_policy.md) for allowed and disallowed language.
