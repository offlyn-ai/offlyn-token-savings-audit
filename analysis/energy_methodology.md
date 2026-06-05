# Energy Methodology

This document explains the incremental energy accounting model used for SCI-AI-aligned carbon reporting.

---

## Key Distinction: Incremental vs Total Device Power

The previous version of this audit used total device inference power (15-30W midpoint 25W) for local compute cost estimation. The SCI-AI carbon model uses **incremental inference power above baseline device usage** (3-8W midpoint 5W).

| Model | Watts | Purpose |
|-------|------:|---------|
| Total device power (legacy) | 25W | Electricity cost estimation |
| Incremental inference power | 5W | Carbon attribution for SCI-AI reporting |

### Why Incremental?

A MacBook draws power whether or not AI inference is running. The baseline includes display, OS, background processes, and idle silicon power. Only the additional power drawn specifically for AI inference should be attributed to the AI workload for carbon accounting purposes.

```
incremental_kwh = (incremental_watts / 1000) * active_processing_hours
```

### Why Total Power for Cost?

The electricity cost model uses total inference power because the user's electricity bill reflects the full draw during processing, not just the increment. This is a different question (cost allocation vs. carbon attribution).

---

## Cloud-First Client-Side Energy

Cloud-first architectures also have client-side device energy: the app is running, displaying UI, streaming audio, sending network requests. This common baseline energy is excluded from both cloud-first and local-first accounting because it cancels out in comparison.

The only energy difference attributed:
- **Cloud-first**: cloud inference energy (via token proxy)
- **Local-first**: incremental local inference energy (above device baseline)
- **Hybrid**: both, proportionally

---

## Default Parameters

| Parameter | Value | Source |
|-----------|------:|--------|
| Incremental inference watts (low) | 3W | Efficient M-series chips, light workloads |
| Incremental inference watts (mid) | 5W | Standard inference on M1-M4 |
| Incremental inference watts (high) | 8W | Heavy inference, multiple models |
| Grid intensity | 350 gCO2e/kWh | US average grid |

Configurable in `assumptions/carbon.yml` under `energy.local_incremental_power_watts_*`.

---

## Example: 60-Minute Meeting

**Incremental model (SCI-AI):**
```
5W * 1 hour = 0.005 kWh
0.005 kWh * 350 gCO2e/kWh = 1.75 gCO2e
```

**Total device model (cost):**
```
25W * 1 hour = 0.025 kWh
0.025 kWh * $0.30/kWh = $0.0075
```

Both are reported but serve different purposes:
- 1.75 gCO2e is the carbon attribution for SCI-AI reporting
- $0.0075 is the electricity cost for FinOps reporting

---

## Backward Compatibility

The existing `scripts/calculate_savings.py` continues to use `local_inference_watts_midpoint: 25` for cost calculations. The SCI-AI script `scripts/calculate_sci_ai.py` uses `local_incremental_power_watts_mid: 5` for carbon attribution. Both coexist in `assumptions/carbon.yml`.

---

## Limitations

- Incremental power draw varies by chip generation (M1 vs M4), model size, quantization, and thermal state.
- The 5W midpoint is a modeled estimate for Apple Silicon running 4-bit quantized models.
- Real measurement requires per-process power monitoring (e.g., `powermetrics` on macOS).
- Grid intensity varies by location and time of day; 350 gCO2e/kWh is a US average.
