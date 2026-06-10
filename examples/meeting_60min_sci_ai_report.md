# 60-Minute Meeting — SCI for AI Report

## Meeting Profile

| Parameter | Value |
|-----------|-------|
| Duration | 60 minutes |
| Words per minute | 150 |
| Tokens per word | 1.3 |
| Transcript tokens | ~11,700 |
| Q&A queries | 5 |
| Architecture comparison | Cloud-first vs Local-first vs Hybrid |

## SCI for AI-aligned Results

### Operational Carbon Intensity

| Architecture | Cloud Tokens | Total Carbon (gCO2e) | SCI per Workflow | SCI per Second |
|-------------|-------------:|--------------------:|----------------:|---------------:|
| Cloud-first | 64,450 | 32.23 | 32.23 | 0.00895 |
| Local-first | 0 | 1.75 | 1.75 | 0.00049 |
| Hybrid | 1,354 | 2.43 | 2.43 | 0.00067 |

### Cost Comparison

| Architecture | Cloud API Cost | Local Compute Cost | Total Cost |
|-------------|---------------:|-------------------:|-----------:|
| Cloud-first | $0.534 | $0.00 | $0.534 |
| Local-first | $0.00 | $0.0075 | $0.0075 |
| Hybrid | $0.008 | $0.0075 | $0.016 |

### Supplemental Water Impact

| Architecture | Direct Datacenter Water (L) | Notes |
|-------------|----------------------------:|-------|
| Cloud-first | 0.147 | Cloud inference cooling |
| Local-first | 0.000 | No datacenter cooling |
| Hybrid | 0.003 | Minimal cloud fallback |

Water is supplemental and is not included in the SCI carbon score.

### Token Reduction

| Architecture | Tokens | Reduction vs Cloud-first |
|-------------|-------:|-------------------------:|
| Cloud-first | 64,450 | — |
| Local-first | 0 | 100% |
| Hybrid | 1,354 | 97.9% |

## Formula Applied

```
SCI operational proxy = O / R

Where:
  O = total_consumer_operational_carbon_gCO2e
  R = 1 (one 60-minute meeting workflow)
  M = 0 (embodied carbon excluded)
```

## Assumptions Used

| Parameter | Value | Source |
|-----------|-------|--------|
| Cloud token carbon | 0.50 gCO2e / 1k tokens | Configurable mid estimate |
| Local incremental power | 5W above baseline | Configurable mid estimate |
| Grid intensity | 350 gCO2e/kWh | Global average proxy |
| Datacenter PUE | 1.2 | Efficient hyperscaler |
| WUE | 0.27 L/kWh | Efficient cloud |

## Disclosure Status

- Type: SCI for AI-aligned Consumer SCI operational proxy
- Verification: Self-attested modeled disclosure
- Embodied carbon: Excluded (M = 0)
- Water: Supplemental only, not in SCI score
- Quality: Modeled defaults, not measured

This report is a modeled estimate for architecture comparison. It is not a carbon credit, offset, certified emissions reduction, or carbon-neutrality claim.
