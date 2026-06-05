# SCI-AI Methodology

This audit uses an SCI-AI-aligned reporting structure inspired by the Green Software Foundation SCI-AI specification and ISO/IEC 21031:2024.

The audit separates:

1. **Consumer SCI** -- carbon intensity of AI service consumption during operation and monitoring.
2. **Provider SCI** -- carbon intensity of model development, training, deployment, and retirement.

For Offlyn Clipper-style enterprise audits, Consumer SCI is the default because the audit compares cloud-first, local-first, and hybrid runtime workflows.

---

## Consumer SCI Formula

Consumer SCI is reported as:

```
Consumer SCI = total_consumer_carbon_gCO2e / functional_unit_count
```

Where total consumer carbon may include:

```
total_consumer_carbon_gCO2e =
  cloud_inference_carbon_gCO2e
  + local_incremental_inference_carbon_gCO2e
  + orchestration_carbon_gCO2e
  + retrieval_and_embedding_carbon_gCO2e
  + storage_carbon_gCO2e
  + network_carbon_gCO2e
  + observability_carbon_gCO2e
  + client_side_carbon_gCO2e
  + allocated_embodied_carbon_gCO2e_when_available
```

**Important:**
- By default, this repo reports an operational SCI-AI proxy because embodied hardware data is often unavailable.
- Full SCI-AI reporting should include embodied carbon when reliable allocation data is available.
- Reports must clearly label whether results are:
  - `operational_proxy`
  - `operational_plus_embodied_estimate`
  - `third_party_verified`

---

## Consumer SCI Boundary Components

When material, the Consumer SCI boundary includes:

| Component | Description |
|-----------|-------------|
| API and inference | Cloud LLM, ASR, and embedding API calls |
| Local inference | On-device model execution (incremental energy only) |
| Orchestration | Agentic workflow routing, model-to-model exchanges |
| Scaling | Load balancers, API gateways, auto-scaling infrastructure |
| Observability and monitoring | Logging, metrics, tracing infrastructure |
| Data and feature management | Feature stores, caching layers |
| Storage and artifacts | Model artifacts, vector stores, search indexes |
| UX and client-side | Application energy on user device |
| Model/tool/service connectors | Tool calls, MCP servers, external API adapters |
| Retrieval | RAG pipelines, vector search, hybrid search |
| Embeddings | Embedding generation for semantic search |
| Network transfer | Data movement between client, edge, and cloud |

---

## AI-Specific Functional Units

Support multiple functional units because AI workflows are multi-modal and multi-step.

| AI Workload | Functional Unit |
|-------------|----------------|
| LLM summarization | gCO2e per 1,000 tokens or per million tokens |
| Speech recognition | gCO2e per second of audio processed |
| Meeting intelligence | gCO2e per meeting hour |
| Agentic workflow | gCO2e per workflow execution |
| Document analysis | gCO2e per page processed |
| Retrieval / RAG | gCO2e per retrieval operation |
| Embeddings | gCO2e per embedding generated |
| Accepted output | gCO2e per accepted summary or action item |

The repo reports at least:
- gCO2e per meeting hour
- gCO2e per transcript
- gCO2e per second of audio processed
- gCO2e per 1,000 cloud tokens
- gCO2e per accepted summary
- gCO2e per workflow execution

---

## Multi-Operation Accounting

For hybrid AI workflows, account for all triggered operations when material:

```
workflow_carbon_gCO2e =
  audio_capture_or_import_carbon
  + speech_to_text_carbon
  + local_llm_carbon
  + cloud_llm_carbon
  + embedding_carbon
  + retrieval_carbon
  + tool_call_carbon
  + orchestration_carbon
  + storage_carbon
  + network_transfer_carbon
  + observability_carbon
```

This is important because a cloud-first meeting intelligence system is not just "one LLM call." It may include ASR, transcript cleanup, embeddings, summary generation, action-item extraction, document retrieval, retries, storage, monitoring, and API infrastructure.

---

## Provider SCI (Optional / Future-Facing)

Provider SCI is not used by default in this audit. It applies only when measuring model development, training, fine-tuning, optimization, deployment, or retirement work.

Provider SCI boundary may include:
- Data collection
- Data preprocessing and cleaning
- Synthetic data generation
- Model training or fine-tuning
- Distributed training infrastructure
- Model evaluation and benchmarking
- Model optimization
- Deployment infrastructure
- Retirement / decommissioning
- Embodied carbon of training hardware when available

---

## Reporting Modes

| Mode | Includes | Use Case |
|------|----------|----------|
| `operational_proxy` | Cloud inference + local incremental energy | Default for architecture comparison |
| `operational_plus_embodied_estimate` | Operational + allocated hardware embodied carbon | When hardware lifecycle data available |
| `third_party_verified` | Full lifecycle with external verification | Formal ESG reporting |

This repo defaults to `operational_proxy`.

---

## Relationship to ISO/IEC 21031:2024

This audit is ISO/IEC 21031:2024-informed but not ISO-certified. The SCI formula structure (E * I + M per R) informs the reporting approach, but this implementation:
- Uses modeled token-proxy estimates rather than measured energy data
- Does not include embodied carbon by default
- Has not undergone third-party verification
- Is designed for internal architecture decision support

---

## Limitations

- All values are modeled estimates based on configurable assumptions.
- Real cloud inference energy varies by model, hardware, utilization, and provider.
- Local incremental energy varies by chip generation, thermal state, and workload.
- Embodied carbon allocation is excluded unless explicitly enabled.
- This is not a certified carbon footprint, offset, or credit.
- The audit does not constitute compliance with any environmental regulation.
