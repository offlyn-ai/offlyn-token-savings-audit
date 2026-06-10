# Limitations

This document discloses known limitations of the SCI for AI-aligned disclosure.

## Modeled vs Measured

| Aspect | Status | Notes |
|--------|--------|-------|
| Cloud token carbon | Modeled | Based on configurable gCO2e/1k tokens assumption |
| Local energy | Modeled | Incremental watts above baseline; not measured per-device |
| Quality scores | Modeled defaults | Not from measured human or LLM evaluation |
| Network transfer | Modeled | Estimated MB per meeting; not measured traffic |
| Water | Modeled | Based on published WUE values, not measured facility data |
| Token counts | Modeled | Based on words-per-minute and tokens-per-word assumptions |

## Excluded Components

| Component | Reason for Exclusion |
|-----------|---------------------|
| Embodied hardware carbon | Reliable allocation data unavailable for local devices, cloud servers, networking, and storage |
| Provider SCI (training) | Outside Consumer SCI boundary; common across compared architectures |
| Baseline device power | All architectures require a user device; not a differentiator |
| Indirect electricity water | Grid-level water impacts of electricity generation are not modeled |
| Storage carbon | Per-meeting allocation for cloud storage is not reliably attributable |
| Observability carbon | Monitoring overhead is negligible at per-meeting granularity |
| Network transfer carbon | Transfer volume is modeled in MB but energy-per-byte attribution is TBD |
| Orchestration carbon | API routing overhead is negligible compared to inference |

## Key Assumptions

- Cloud carbon uses mid estimate (0.50 gCO2e per 1,000 tokens) unless overridden
- Local incremental power is 5W above baseline (mid estimate)
- Grid intensity is 350 gCO2e/kWh (global average proxy)
- Datacenter PUE is 1.2 (efficient hyperscaler)
- WUE is 0.27 L/kWh (efficient cloud; generic is 1.90 L/kWh)
- Meeting generates ~11,700 transcript tokens at 150 words/minute × 1.3 tokens/word

## Non-Certification Disclaimer

This disclosure is:
- A modeled estimate for architecture comparison
- Self-attested, not third-party verified
- Not a carbon credit, offset, or certified emissions reduction
- Not a formal ISO certification or Green Software Foundation certification
- Not a carbon-neutrality claim

This is a certification-readiness package designed for GSF SCI self-certification submission preparation. It does not constitute certification unless and until an official public certificate is issued.

## Future Improvements

| Improvement | Impact |
|-------------|--------|
| Measured quality evaluation | Upgrade quality scores from modeled to measured |
| Per-device energy measurement | Replace incremental power estimate with measured data |
| Embodied carbon inclusion | Add M > 0 when allocation data is available |
| Provider SCI extension | Optional training/deployment carbon for full lifecycle |
| Facility-specific WUE | Replace generic with actual datacenter WUE |
| Network energy attribution | Convert MB avoided to gCO2e with per-byte energy data |

See [data_sources.md](data_sources.md) for detailed assumption validation status and planned upgrades.
