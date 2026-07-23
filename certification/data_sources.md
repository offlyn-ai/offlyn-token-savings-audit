# Data Sources and Assumption Status

This disclosure uses modeled defaults for architecture comparison. Where provider-specific or hardware-specific values are unavailable, assumptions are labeled as modeled defaults pending future validation.

## Key Assumptions Requiring Review

| Assumption | Current Value | Status | Notes |
|------------|-------------:|--------|-------|
| Cloud token carbon intensity | 0.50 gCO2e / 1,000 cloud tokens | Modeled default pending provider-specific validation | Used as mid-case operational proxy. Low/high sensitivity values are disclosed in the assumptions register. |
| Incremental local inference power | 5W | Modeled default pending Apple Silicon measurement | Counts incremental inference energy above baseline user-device power, not full device power. |
| Local grid intensity | 350 gCO2e/kWh | Modeled default pending region-specific update | Customers should replace with region-specific electricity carbon intensity where available. |
| Efficient cloud WUE | 0.27 L/kWh | Modeled default pending provider-specific update | Used only for supplemental direct datacenter cooling-water estimates, not the SCI carbon score. |
| Datacenter PUE | 1.2 | Modeled default | Represents efficient hyperscaler operations. |
| Words per minute | 150 | Modeled default | Standard conversational speech rate assumption. |
| Tokens per word | 1.3 | Modeled default | Standard tokenizer ratio for English text. |

## Source References

| Parameter | Source Type | Reference |
|-----------|-----------|-----------|
| Cloud token carbon | Literature estimate | Published AI carbon footprint research (range: 0.10 - 3.00 gCO2e/1k tokens) |
| Local incremental power | Engineering estimate | Apple Silicon power measurement literature (3-8W range for inference workloads) |
| Grid intensity | Published data | IEA World Energy Outlook 2023, global average electricity emission factor |
| PUE | Industry report | Uptime Institute Global Data Center Survey |
| WUE | Provider reports | Published hyperscaler sustainability reports |

## Future Validation Upgrades

- Measure Offlyn Clipper local inference energy on Apple Silicon.
- Replace generic cloud-token carbon assumptions with provider-specific or workload-specific estimates.
- Add region-specific grid carbon intensity.
- Add customer-specific WUE assumptions where cloud provider data is available.
- Add measured quality evaluation using human review or LLM-as-judge scoring.
- Add embodied carbon allocation when reliable cloud and local hardware allocation data is available.

## Relationship to Disclosure

All assumptions in this document are reflected in:
- `certification/assumptions_register.yml` (consolidated values)
- `assumptions/carbon.yml` (carbon parameters)
- `assumptions/water.yml` (water parameters)
- `certification/limitations.md` (exclusions and caveats)

Changes to any assumption require re-running the calculation and validation scripts to update generated outputs.
