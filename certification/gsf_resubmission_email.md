# GSF SCI Self-Certification Resubmission

**To:** sci-certification@greensoftware.foundation

**Subject:** SCI Self-Certification Resubmission — Offlyn.ai — Offlyn Clipper

---

Hi Kirsty,

Thank you for the detailed feedback. We have revised the disclosure to address all four items you identified.

---

## Revision Summary

### Item 1 — Software System Name and Shared Infrastructure

**Your feedback:** The submission listed "Offlyn Token Savings Audit" but the disclosure title referred to "Offlyn Meeting Intelligence Hybrid Routing Benchmark." You requested clarification on which name is the system of record and an explicit shared infrastructure statement.

**Resolution:**

- **Software system:** The system of record is now clearly identified as **Offlyn Clipper** — our native macOS application for on-device meeting intelligence (https://clipper.offlyn.ai/)
- **Shared infrastructure statement:** Added explicitly in Section 3:

> "No included component runs on shared multi-tenant infrastructure. Offlyn Clipper runs entirely on end-user Apple Silicon devices. Audio capture, transcription, embedding generation, and AI inference all execute locally on the user's Mac. There is no cloud component in the default configuration."

---

### Item 2 — SCI Score and Measurement Period

**Your feedback:** No single numeric SCI score with units tied to a defined measurement period. The original package modeled a comparison across routing architectures rather than reporting a completed SCI calculation for one system.

**Resolution:**

We conducted direct power measurements on an Apple M4 Mac using macOS `powermetrics` and now report a completed SCI calculation:

| Field | Value |
|-------|-------|
| **SCI score** | 0.35 gCO2eq per meeting workflow |
| **Measurement period** | 2026-07-22 to 2026-07-22 |
| **Device** | Apple M4 Mac |
| **Method** | Direct power measurement |

**Measured power values:**
- Baseline (idle): 198 mW
- Transcription (Whisper): 1,056 mW (0.86 W incremental)
- Summarization (Gemma 4): 12,313 mW (12.11 W incremental)

**Calculation shown in Section 7:**
```
E × I = 0.00101 kWh × 350 gCO2eq/kWh = 0.35 gCO2eq
M = 0 gCO2eq
R = 1 meeting workflow

SCI = (E × I + M) / R = (0.35 + 0) / 1 = 0.35 gCO2eq per meeting workflow
```

---

### Item 3 — Carbon Intensity Data Source

**Your feedback:** Carbon-intensity data source should be named with a specific year directly in the main disclosure document.

**Resolution:**

Section 5 now explicitly states:

> **Data source:** IEA World Energy Outlook 2023, global average electricity emission factor

This citation appears in the main disclosure, the calculation section, and the data sources document.

---

### Item 4 — Attestation

**Your feedback:** The attached attestation was a custom-written statement rather than the programme's required 10-point attestation.

**Resolution:**

We have replaced the custom attestation with the verbatim 10-point attestation from the GSF submission template (`docs/submission-email-template.md`), including:

1. DECLARE conformity with ISO/IEC 21031:2024
2. ATTEST good faith methodology
3. ACKNOWLEDGE ISO/IEC 17050 self-certification framework
4. MAINTAIN documentation for 3 years
5. ACCEPT RESPONSIBILITY for accuracy
6. AGREE to correct errors
7. UNDERSTAND GSF's limited review role
8. AGREE to badge usage guidelines
9. ACKNOWLEDGE consequences of false certification
10. CONSENT to public disclosure

Signed and dated: Joel Nishant Reddy, July 22, 2026

---

## Revised Package

**Repository:** https://github.com/offlyn-ai/offlyn-token-savings-audit

**Release:** https://github.com/offlyn-ai/offlyn-token-savings-audit/releases/tag/v1.0.0-sci-measured

**Key documents:**
| Document | Description |
|----------|-------------|
| `certification/sci_ai_disclosure.md` | Main disclosure (revised) |
| `certification/sci_ai_attestation.md` | 10-point attestation (replaced) |
| `certification/sci_ai_boundary.md` | Boundary with shared infrastructure statement |
| `certification/sci_ai_calculation.md` | Calculation with measured values |
| `measurements/` | Raw powermetrics logs |

---

## Checklist Confirmation

- [x] Section 1 — Organization and software details (Offlyn Clipper)
- [x] Section 2 — SCI score with units and measurement period (0.35 gCO2eq, 2026-07-22)
- [x] Section 3 — Included and excluded components with rationales
- [x] Section 4 — Functional unit with rationale and measurement method
- [x] Section 5 — Energy with per-component breakdown; carbon intensity with source and year (IEA 2023)
- [x] Section 6 — Embodied emissions justification (M = 0, consumer device)
- [x] Section 7 — Methodology, assumptions, limitations, and calculation shown
- [x] Attestation — Verbatim 10-point template, signed and dated

---

Please let us know if any additional information is needed.

Best regards,

Joel Nishant Reddy  
Co-founder, Offlyn.ai
