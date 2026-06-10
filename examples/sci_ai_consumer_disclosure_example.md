# SCI for AI Consumer Disclosure Example

## Customer-Facing Summary

Offlyn estimated the operational carbon intensity and token cost of a 60-minute meeting intelligence workflow across cloud-first, local-first, and hybrid local-first architectures. The audit reports cloud tokens, API cost, incremental local energy, modeled operational CO2e, quality-risk notes, privacy exposure, and supplemental direct datacenter cooling-water impact. Results are modeled estimates for decision support and are not carbon credits, offsets, certified emissions reductions, or carbon-neutrality claims.

## Disclosure Type

SCI for AI-aligned Consumer SCI operational proxy.

## Results Summary (60-Minute Meeting)

| Metric | Cloud-first | Local-first | Hybrid |
|--------|------------:|------------:|-------:|
| Cloud tokens | 64,450 | 0 | ~1,354 |
| API cost | $0.534 | $0.00 | $0.008 |
| Total operational carbon | 32.2 gCO2e | 1.75 gCO2e | 2.43 gCO2e |
| SCI per workflow | 32.2 gCO2e | 1.75 gCO2e | 2.43 gCO2e |
| Direct datacenter water | 0.147 L | 0 L | 0.003 L |
| Water in SCI score | No | No | No |

## Key Findings

1. **Local-first reduces operational carbon by ~95%** compared to cloud-first for routine meeting intelligence.
2. **Hybrid achieves ~92% carbon reduction** while maintaining cloud access for complex queries.
3. **Water is supplemental** — reported for transparency but not included in SCI carbon intensity.
4. **Quality remains strong** — local models handle routine tasks at production quality (modeled 3.9/5.0 vs cloud 4.1/5.0).

## Methodology Notes

- Consumer SCI boundary (inference-time operational only)
- Embodied carbon excluded (M = 0; reliable allocation data unavailable)
- Water is supplemental and not part of SCI score
- Quality scores are modeled defaults, not measured evaluations
- ISO/IEC 21031:2024-informed methodology
- Self-attested, not third-party verified

## What This Is Not

This disclosure is not:
- A carbon credit or offset
- A certified emissions reduction
- An ISO certification
- A Green Software Foundation certification
- A carbon-neutrality claim
- A guaranteed Scope 3 reduction

## Next Steps

For a measured (not modeled) disclosure:
1. Run actual workloads through each architecture
2. Measure real token counts and response times
3. Conduct human quality evaluation
4. Measure device-level power consumption
5. Obtain facility-specific WUE data

## References

- Full disclosure: `certification/sci_ai_disclosure.md`
- Methodology: `analysis/sci_ai_methodology.md`
- Assumptions: `certification/assumptions_register.yml`
- Calculation: `certification/sci_ai_calculation.csv`
