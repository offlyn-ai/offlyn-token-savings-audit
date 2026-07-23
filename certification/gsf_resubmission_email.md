# GSF SCI Self-Certification Resubmission

**To:** sci-certification@greensoftware.foundation

**Subject:** SCI Self-Certification Resubmission — Offlyn.ai — Offlyn Clipper

---

Hi Kirsty,

Thank you for the detailed feedback. We have revised the disclosure to address all four items.

---

## Summary

| Field | Value |
|-------|-------|
| **Organization** | Offlyn.ai |
| **Software system** | Offlyn Clipper |
| **Software version** | 1.0 (beta-2026-07) |
| **Software URL** | https://clipper.offlyn.ai/ |
| **SCI score** | **0.35 gCO2eq per meeting workflow** |
| **Measurement period** | 2026-07-22 to 2026-07-22 (benchmark) |
| **Method** | Direct power measurement (macOS powermetrics, Apple M4) |

---

## Revision Details

### Item 1 — Software System Name and Shared Infrastructure

**Your feedback:** Clarify the system of record and add shared infrastructure statement.

**Resolution:**
- **Software system:** Offlyn Clipper — native macOS app for on-device meeting intelligence
- **Shared infrastructure:** "No included component runs on shared multi-tenant infrastructure. Offlyn Clipper runs entirely on end-user Apple Silicon devices."

---

### Item 2 — SCI Score and Measurement Period

**Your feedback:** Provide a completed SCI calculation for one system over one period.

**Resolution:** We conducted direct power measurements and report:

| Component | Duration | Incremental Power | Energy |
|-----------|----------|-------------------|--------|
| Transcription (Whisper) | 60 min | 0.86 W | 0.00086 kWh |
| Summarization (Gemma 4) | 45 sec | 12.11 W | 0.00015 kWh |
| **Total E** | — | — | **0.00101 kWh** |

**Calculation:**
```
E × I = 0.00101 kWh × 350 gCO2eq/kWh = 0.35 gCO2eq
M = 0 gCO2eq (consumer device — no reliable allocation methodology)
R = 1 meeting workflow

SCI = (E × I + M) / R = 0.35 gCO2eq per meeting workflow
```

This is a representative benchmark measurement appropriate for consumer software where each user runs the software independently.

---

### Item 3 — Carbon Intensity Data Source

**Your feedback:** Name the data source with a specific year in the main disclosure.

**Resolution:** Section 5 now states: "**Data source:** IEA World Energy Outlook 2023, global average electricity emission factor"

---

### Item 4 — Attestation

**Your feedback:** Use the verbatim 10-point attestation.

**Resolution:** Replaced with the GSF template attestation including all 10 points (DECLARE conformity, ATTEST methodology, ACKNOWLEDGE framework, MAINTAIN documentation, ACCEPT responsibility, AGREE to corrections, UNDERSTAND GSF role, AGREE to badge guidelines, ACKNOWLEDGE consequences, CONSENT to disclosure). Signed: Joel Nishant Reddy, July 22, 2026.

---

## Package Links

**Repository:** https://github.com/offlyn-ai/offlyn-token-savings-audit

**Release:** https://github.com/offlyn-ai/offlyn-token-savings-audit/releases/tag/v1.0.0-sci-measured

| Document | Path |
|----------|------|
| Main disclosure | `certification/sci_ai_disclosure.md` |
| Attestation | `certification/sci_ai_attestation.md` |
| Boundary | `certification/sci_ai_boundary.md` |
| Calculation | `certification/sci_ai_calculation.md` |
| Raw measurements | `measurements/` |

---

## Checklist

- [x] Section 1 — Organization and software details
- [x] Section 2 — SCI score with units and measurement period
- [x] Section 3 — Included/excluded components with rationales
- [x] Section 4 — Functional unit with rationale and method
- [x] Section 5 — Energy breakdown; carbon intensity with source + year
- [x] Section 6 — Embodied emissions with justification (M = 0)
- [x] Section 7 — Methodology, assumptions, limitations, calculation
- [x] Attestation — 10-point template, signed and dated

---

Please let us know if anything else is needed.

Best regards,

Joel Nishant Reddy  
Co-founder, Offlyn.ai
