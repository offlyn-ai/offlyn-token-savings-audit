# GSF SCI Self-Certification Resubmission

**To:** sci-certification@greensoftware.foundation

**Subject:** SCI Self-Certification Resubmission — Offlyn.ai — Offlyn Clipper

---

Hi Kirsty,

Thank you for the detailed feedback on our original submission. We have revised the disclosure to address all four items:

## 1. Software System Name (Item 1)

The software system is now clearly identified as **Offlyn Clipper** — our native macOS application for on-device meeting intelligence. We have added an explicit shared infrastructure statement confirming that no components run on shared multi-tenant infrastructure; all processing occurs locally on Apple Silicon.

## 2. SCI Score and Measurement Period (Item 2)

The revised disclosure reports a **completed SCI calculation based on measured power data**:

| Metric | Value |
|--------|-------|
| SCI score | **0.35 gCO2eq per meeting workflow** |
| Measurement date | July 22, 2026 |
| Device | Apple M4 Mac |
| Method | Direct power measurement (macOS `powermetrics`) |

Power measurements:
- Baseline (idle): 198 mW
- Transcription (Whisper): 1,056 mW (0.86 W incremental)
- Summarization (Gemma 4): 12,313 mW (12.11 W incremental)

## 3. Carbon Intensity Source (Item 3)

The main disclosure now explicitly names **"IEA World Energy Outlook 2023, global average electricity emission factor"** as the carbon intensity data source (350 gCO2eq/kWh).

## 4. Attestation (Item 4)

We have replaced the custom attestation with the verbatim 10-point attestation from the GSF submission template, signed and dated.

---

## Revised Package

The complete revised disclosure is available at:

**Repository:** https://github.com/offlyn-ai/offlyn-token-savings-audit

**Key documents:**
- Main disclosure: `certification/sci_ai_disclosure.md`
- Attestation: `certification/sci_ai_attestation.md`
- Boundary: `certification/sci_ai_boundary.md`
- Calculation: `certification/sci_ai_calculation.md`
- Raw measurements: `measurements/` directory

**Public release:**
https://github.com/offlyn-ai/offlyn-token-savings-audit/releases/tag/v1.0.0-sci-measured

---

Please let us know if any additional information is needed.

Best regards,

Joel Nishant Reddy  
Co-founder, Offlyn.ai
