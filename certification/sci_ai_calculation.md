# SCI for AI Calculation Methodology

## Canonical SCI Formula

```
SCI = (O + M) / R
```

Where:
- **O** = Operational emissions (gCO2e) — included
- **M** = Embodied emissions allocated to the functional unit (gCO2e) — excluded (M = 0)
- **R** = Functional unit count — one 60-minute meeting workflow

## This Disclosure: Operational Proxy

```
SCI operational proxy = O / R
```

**M = 0** because:

Embodied emissions are excluded from the default operational proxy because reliable allocation data for local user devices, cloud provider hardware, networking, and storage infrastructure is not currently available. Future disclosures may include embodied emissions when reliable allocation data is available.

## Operational Emissions Component Breakdown

```
total_consumer_operational_carbon_gCO2e =
    cloud_inference_carbon_gCO2e
  + local_incremental_inference_carbon_gCO2e
  + asr_carbon_gCO2e
  + embedding_carbon_gCO2e
  + retrieval_carbon_gCO2e
  + orchestration_carbon_gCO2e
  + storage_carbon_gCO2e
  + network_transfer_carbon_gCO2e
  + observability_carbon_gCO2e
```

### Component Status

| Component | Status | Method |
|-----------|--------|--------|
| Cloud inference carbon | Included | Token count × gCO2e per 1k tokens (configurable) |
| Local incremental inference carbon | Included | Incremental watts × hours × grid intensity |
| ASR carbon | Included | Modeled within cloud or local inference |
| Embedding carbon | Included | Modeled within cloud or local inference |
| Retrieval carbon | Included | Modeled within cloud or local inference |
| Orchestration carbon | Modeled as zero | Negligible for inference-time orchestration |
| Storage carbon | Modeled as zero | Reliable allocation data unavailable |
| Network transfer carbon | Modeled as zero | Transfer modeled in MB; carbon attribution TBD |
| Observability carbon | Modeled as zero | Negligible for inference-time monitoring |

### Components Modeled as Zero

The following components are currently set to zero due to lack of reliable attribution data:
- **Orchestration**: Inference-time API routing overhead is negligible compared to model inference
- **Storage**: Cloud storage carbon allocation per meeting is not reliably attributable
- **Network transfer carbon**: Network energy per MB transferred varies by infrastructure; modeled in volume only
- **Observability**: Monitoring overhead is negligible at the per-meeting level

These are listed in [limitations.md](limitations.md) and may be included in future disclosures.

## Calculation Parameters

### Cloud Inference Carbon

```
cloud_inference_carbon_gCO2e = (cloud_tokens / 1000) × co2e_g_per_1k_tokens
```

Default: 0.50 gCO2e per 1,000 tokens (mid estimate)

### Local Incremental Inference Carbon

```
local_incremental_energy_kwh = (incremental_power_watts / 1000) × active_processing_hours
local_incremental_carbon_gCO2e = local_incremental_energy_kwh × grid_intensity_gCO2e_per_kwh
```

Defaults:
- Incremental power: 5W (mid estimate, above baseline device usage)
- Active processing: 1.0 hour (full meeting duration)
- Grid intensity: 350 gCO2e/kWh

### SCI Per Functional Unit

```
sci_g_per_workflow = total_consumer_operational_carbon_gCO2e / 1
sci_g_per_meeting_hour = total_consumer_operational_carbon_gCO2e / 1.0
sci_g_per_second_audio = total_consumer_operational_carbon_gCO2e / 3600
sci_g_per_1k_cloud_tokens = cloud_carbon_gCO2e / (cloud_tokens / 1000)  [N/A if tokens = 0]
```

## Water (Supplemental, Not in SCI Score)

```
direct_datacenter_water_liters = cloud_it_energy_kwh × PUE × WUE_l_per_kwh
```

Water is reported separately and is NOT included in the SCI carbon intensity calculation.

## Avoided Emissions (Separate from SCI Score)

Avoided emissions represent the difference between the cloud-first baseline and the solution architecture:

```
avoided_cloud_carbon = cloud_first_carbon - solution_cloud_carbon
net_avoided_total_carbon = cloud_first_total_carbon - solution_total_carbon
```

Avoided emissions are informational and are NOT part of the SCI score. They represent what would have been emitted under the baseline, not a reduction claim.

## Calculation Results

See [sci_ai_calculation.csv](sci_ai_calculation.csv) for the machine-readable results.
