# Carbon and Energy Methodology

This document explains how the repository estimates directional cloud-side carbon avoided and local compute energy consumed.

## Purpose

The carbon estimates in this repository help enterprises understand the environmental dimension of their AI architecture choice. They are not certified carbon footprint measurements.

## Token Proxy Method

The primary estimation method uses a per-token carbon proxy:

```
estimated_co2e_grams = (cloud_tokens / 1000) × grams_co2e_per_1000_tokens
```

Default: 0.10 grams CO2e per 1,000 cloud tokens.

This proxy accounts for:
- GPU compute energy during inference
- Datacenter overhead (cooling, networking, storage)
- Amortized embodied carbon of hardware

### Cloud-First Example (60-min meeting)

```
64,450 tokens × (0.10 g / 1000 tokens) = 6.445 g CO2e
```

### Tokens Avoided Under Offline-First

```
64,450 tokens avoided × (0.10 g / 1000 tokens) = 6.445 g CO2e avoided
```

### Scaling to Enterprise (1,000 meetings/month)

```
64,450,000 monthly tokens avoided × (0.10 g / 1000 tokens) = 6,445 g = 6.4 kg CO2e/month
Annual: ~77 kg CO2e avoided
```

## Energy Proxy Method

An alternative approach estimates cloud energy directly:

```
cloud_energy_kwh = cloud_tokens × energy_per_token_kwh
cloud_co2e = cloud_energy_kwh × grid_intensity × PUE
```

Where:
- `energy_per_token_kwh`: varies by model size and hardware (typically 0.001–0.01 Wh per token for large models)
- `grid_intensity`: grams CO2e per kWh (varies by region, default 350 g/kWh)
- `PUE`: Power Usage Effectiveness of the datacenter (default 1.2)

This method is more precise but requires assumptions about the specific inference hardware and datacenter.

## Local Electricity Method

For the offline-first and hybrid architectures, local compute has its own energy cost:

```
local_kwh = (local_inference_watts / 1000) × processing_hours
local_co2e = local_kwh × local_grid_intensity
local_cost = local_kwh × electricity_price_per_kwh
```

### Default Parameters

| Parameter | Value |
|-----------|------:|
| Local inference watts (midpoint) | 25 W |
| Local inference watts (low) | 15 W |
| Local inference watts (high) | 30 W |
| Grid intensity | 350 g CO2e/kWh |
| Electricity price | $0.30/kWh |

### Local Example (60-min meeting)

```
Energy: 25W × 1 hour = 0.025 kWh
CO2e: 0.025 kWh × 350 g/kWh = 8.75 g CO2e
Cost: 0.025 kWh × $0.30 = $0.0075
```

## Net Carbon Comparison

| Architecture | Cloud CO2e | Local CO2e | Net CO2e |
|--------------|:----------:|:----------:|:--------:|
| Cloud-first | 6.4 g | ~0 g | 6.4 g |
| Offline-first | 0 g | 8.75 g | 8.75 g |
| Hybrid | ~0.14 g | 8.75 g | ~8.9 g |

Note: local CO2e depends heavily on the user's electricity grid mix. In regions with renewable energy, local CO2e approaches zero.

## Carbon Disclaimer

Carbon estimates in this repository are **directional and assumption-based**. Real emissions vary by:

- Model size and architecture
- Inference hardware (GPU type, chip generation)
- Datacenter utilization and batching
- Batch size and request concurrency
- Datacenter PUE (Power Usage Effectiveness)
- Electricity grid mix at the datacenter location
- Electricity grid mix at the user's location (for local compute)
- Cooling requirements and ambient temperature
- Networking energy
- Whether inference is served from shared or dedicated infrastructure

Treat these numbers as a sensitivity model, not a certified carbon footprint.

## Sensitivity Analysis

### Cloud Token Carbon Proxy Sensitivity

| gCO2e per 1000 tokens | 60-min Cloud-First CO2e | Enterprise Annual CO2e Avoided |
|-----------------------:|------------------------:|-------------------------------:|
| 0.05 | 3.2 g | ~39 kg |
| 0.10 (default) | 6.4 g | ~77 kg |
| 0.20 | 12.9 g | ~155 kg |
| 0.50 | 32.2 g | ~387 kg |

### Local Grid Intensity Sensitivity

| Grid Intensity (g/kWh) | Local 60-min CO2e | Context |
|------------------------:|------------------:|---------|
| 50 | 1.25 g | Low-carbon grid (nuclear/hydro/renewable) |
| 200 | 5.0 g | Mixed grid |
| 350 (default) | 8.75 g | Average US grid |
| 600 | 15.0 g | Coal-heavy grid |

## Why Carbon Estimates Vary

1. **No standardized reporting**: cloud providers have different approaches to carbon accounting.
2. **Shared infrastructure**: inference requests share GPUs, making per-request attribution complex.
3. **Dynamic grid mix**: the same datacenter has different carbon intensity at different times of day.
4. **Model efficiency improves**: newer models and hardware reduce per-token energy over time.
5. **Quantization reduces local energy**: 4-bit models use less memory bandwidth and compute per token.

## Incremental Energy Model (SCI-AI)

For SCI-AI-aligned carbon attribution, this audit uses an **incremental energy model** that attributes only the additional power drawn by AI inference above the device's baseline idle consumption.

| Model | Watts | Purpose |
|-------|------:|---------|
| Total device power (cost model) | 25W | Electricity cost in FinOps reporting |
| Incremental inference power (carbon model) | 5W | Carbon attribution for SCI-AI |

The incremental model (3-8W, midpoint 5W) is used for Consumer SCI reporting because the device draws baseline power regardless of whether AI inference is running. Only the marginal energy should be attributed to the AI workload.

See [analysis/energy_methodology.md](energy_methodology.md) for the full rationale.

---

## SCI-AI-Aligned Reporting

This carbon methodology feeds into the broader SCI-AI reporting framework:

- **Consumer SCI**: `total_consumer_carbon_gCO2e / functional_unit_count`
- **Functional units**: gCO2e per meeting hour, per second of audio, per transcript, per workflow execution
- **Boundary**: Operational AI consumption (inference, retrieval, orchestration)
- **Reporting mode**: `operational_proxy` by default

See [analysis/sci_ai_methodology.md](sci_ai_methodology.md) for the full SCI-AI framework.

---

## Net Avoided vs Gross Avoided

- **Avoided cloud carbon**: cloud inference emissions not incurred because workload is local.
- **Net avoided total carbon**: avoided cloud emissions minus incremental local energy.

This distinction prevents overclaiming. See [analysis/avoided_emissions_methodology.md](avoided_emissions_methodology.md).

---

## Updated Cloud Token Carbon Range

The audit supports three cloud token carbon intensity levels:

| Level | gCO2e per 1,000 tokens | Context |
|-------|------------------------:|---------|
| Low | 0.10 | Efficient models on renewable-powered infrastructure |
| Mid (default for SCI-AI) | 0.50 | Standard cloud inference |
| High | 3.00 | Large models on carbon-intensive grids |

The legacy token proxy (0.10 g/1k tokens) remains in the basic calculator for backward compatibility. The SCI-AI calculator uses the mid value (0.50 g/1k tokens) by default.

---

## Recommendations for Accurate Carbon Assessment

For organizations that need precise carbon accounting:

1. Use provider-specific carbon reporting APIs where available.
2. Measure actual GPU utilization for inference workloads.
3. Use location-specific and time-specific grid intensity data.
4. Account for the amortized embodied carbon of hardware.
5. Consider the full lifecycle: training, inference, networking, storage.
6. Update assumptions annually as hardware and grid mix evolve.
7. Use incremental local energy measurements (e.g., macOS `powermetrics`) rather than estimates.
8. Engage third-party verification for formal sustainability reporting.
