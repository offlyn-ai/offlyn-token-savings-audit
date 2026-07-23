# SCI Calculation — Offlyn Clipper

## Canonical SCI Formula

```
SCI = (E × I + M) / R
```

Where:
- **E** = Energy consumed (kWh)
- **I** = Carbon intensity of electricity (gCO2eq/kWh)
- **M** = Embodied emissions allocated to the functional unit (gCO2eq)
- **R** = Functional unit count

## This Disclosure

**SCI = 0.35 gCO2eq per meeting workflow**

Based on measured power consumption on Apple M4 Mac, July 22, 2026.

---

## Measured Power Values

| Phase | Baseline | Active | Incremental |
|-------|----------|--------|-------------|
| Idle | 198 mW | — | — |
| Transcription (Whisper) | 198 mW | 1,056 mW | 858 mW (0.86 W) |
| Summarization (Gemma 4) | 198 mW | 12,313 mW | 12,115 mW (12.11 W) |

**Measurement method:** macOS `powermetrics` with `cpu_power` sampler at 1-second intervals

**Device:** Apple M4 Mac

---

## Energy Calculation

### Transcription Phase (Whisper ASR)

```
Duration: 60 minutes = 1.0 hour (real-time transcription)
Incremental power: 0.86 W
Energy: 0.86 W × 1.0 h = 0.00086 kWh
```

### Summarization Phase (Gemma 4 LLM)

```
Duration: 45 seconds = 0.0125 hour (post-meeting inference)
Incremental power: 12.11 W
Energy: 12.11 W × 0.0125 h = 0.00015 kWh
```

### Total Energy (E)

```
E = 0.00086 + 0.00015 = 0.00101 kWh
```

---

## Carbon Intensity (I)

```
I = 350 gCO2eq/kWh
```

**Source:** IEA World Energy Outlook 2023, global average electricity emission factor

**Approach:** Location-based (global average; users should substitute region-specific values)

---

## Embodied Emissions (M)

```
M = 0 gCO2eq
```

Embodied emissions are excluded because reliable allocation methodology for consumer device hardware is unavailable. This is a documented limitation.

---

## Functional Unit (R)

```
R = 1 meeting workflow
```

One 60-minute meeting intelligence workflow, encompassing audio capture, transcription, summarization, action item extraction, and searchable indexing.

---

## Final Calculation

```
E × I = 0.00101 kWh × 350 gCO2eq/kWh = 0.35 gCO2eq
M = 0 gCO2eq
R = 1 meeting workflow

SCI = (E × I + M) / R = (0.35 + 0) / 1 = 0.35 gCO2eq per meeting workflow
```

---

## Comparison to Original Modeled Estimate

| Metric | Original (modeled) | Revised (measured) | Change |
|--------|-------------------|-------------------|--------|
| Incremental power | 5 W (estimate) | 0.86–12.11 W (measured) | Varies by phase |
| Energy per meeting | 0.005 kWh | 0.00101 kWh | 80% lower |
| SCI score | 1.75 gCO2eq | 0.35 gCO2eq | **80% lower** |

The measured SCI is significantly lower than the original modeled estimate because:
1. Transcription (Whisper) draws only 0.86 W, much lower than the 5W estimate
2. Summarization (Gemma 4) draws 12 W but only runs for ~45 seconds
3. The original model assumed 5W continuous for the full meeting duration

---

## Secondary Functional Units

| Functional Unit | Value |
|-----------------|-------|
| gCO2eq per meeting workflow | 0.35 |
| gCO2eq per meeting hour | 0.35 |
| gCO2eq per second of audio | 0.000097 |
| gCO2eq per transcript generated | 0.35 |
