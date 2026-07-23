# GSF SCI Self-Certification Resubmission

**To:** sci-certification@greensoftware.foundation

**Subject:** RE: Revision Request for SCI Self-Certification Submission — Offlyn.ai

---

Hi Kirsty,

Thank you for the detailed feedback. We have revised the disclosure to address all four items.

## Clarification on Naming

To address the naming confusion you identified:

- **Offlyn Clipper** is the **software system being certified** — a native macOS application for on-device meeting intelligence (https://clipper.offlyn.ai/)
- **Offlyn Token Savings Audit** is the **audit framework** we used to measure and document Clipper's carbon intensity

The SCI certification applies to **Offlyn Clipper**. The repository contains the disclosure package, measurement methodology, and raw data.

---

## Certification Summary

| Field | Value |
|-------|-------|
| **Organization** | Offlyn.ai |
| **Software system** | Offlyn Clipper |
| **Software version** | 1.0 (beta-2026-07) |
| **Software URL** | https://clipper.offlyn.ai/ |
| **SCI score** | **0.35 gCO2eq per meeting workflow** |
| **Measurement period** | 2026-07-22 to 2026-07-22 |
| **Functional unit (R)** | 1 meeting workflow (60 minutes) |
| **Approach** | Measurement (not modeled) |

---

## Revision Details

### 1. Software/System Name (Item 1 — Identity and Scope)

**Your feedback:** Confirm which name is the system of record; add shared infrastructure statement.

**Resolution:**

- **Software system:** Offlyn Clipper
- **Shared infrastructure:** Added to Section 3:

> "No included component runs on shared multi-tenant infrastructure. Offlyn Clipper runs entirely on end-user Apple Silicon devices. Audio capture, transcription, embedding generation, and AI inference all execute locally on the user's Mac. There is no cloud component in the default configuration."

---

### 2. SCI Score and Measurement Period (Item 2 — Score and Period)

**Your feedback:** Clarify whether this is measured or modeled; provide a single SCI score with dates.

**Resolution:** This is now based on **direct power measurement**, not a model/simulation.

**Measured values (Apple M4 Mac, July 22, 2026):**

| Component | Duration | Incremental Power | Energy (kWh) |
|-----------|----------|-------------------|--------------|
| Transcription (Whisper) | 60 min | 0.86 W | 0.00086 |
| Summarization (Gemma 4) | 45 sec | 12.11 W | 0.00015 |
| **Total Energy (E)** | — | — | **0.00101** |

**SCI Calculation per ISO/IEC 21031:2024:**

```
E × I = 0.00101 kWh × 350 gCO2eq/kWh = 0.35 gCO2eq
M = 0 gCO2eq (embodied excluded — no reliable allocation for consumer devices)
R = 1 meeting workflow

SCI = (E × I + M) / R = (0.35 + 0) / 1 = 0.35 gCO2eq per meeting workflow
```

---

### 3. Carbon-Intensity Data Source (Item 4 — Energy and Carbon Intensity)

**Your feedback:** Name the carbon-intensity source with year in the main disclosure.

**Resolution:** Section 5 now states:

> **Carbon intensity:** 350 gCO2eq/kWh  
> **Data source:** IEA World Energy Outlook 2023, global average electricity emission factor  
> **Approach:** Location-based

---

### 4. Attestation (Item 7 — Attestation)

**Your feedback:** Replace custom attestation with verbatim 10-point GSF template.

**Resolution:** Replaced with the exact attestation from `docs/submission-email-template.md`, including:

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

**Signed:** Joel Nishant Reddy, Co-founder, Offlyn.ai  
**Date:** July 22, 2026

---

## Package Links

**Release:** https://github.com/offlyn-ai/offlyn-token-savings-audit/releases/tag/v1.0.0-sci-measured

| Document | Path |
|----------|------|
| Main disclosure | `certification/sci_ai_disclosure.md` |
| Attestation | `certification/sci_ai_attestation.md` |
| Boundary definition | `certification/sci_ai_boundary.md` |
| Calculation details | `certification/sci_ai_calculation.md` |
| Raw measurement logs | `measurements/` |

---

## GSF 7-Item Checklist Confirmation

- [x] **Item 1 — Identity and scope:** Offlyn Clipper, with shared infrastructure statement
- [x] **Item 2 — Score and period:** 0.35 gCO2eq, 2026-07-22 to 2026-07-22, measured
- [x] **Item 3 — Software boundary:** Included/excluded components with rationales
- [x] **Item 4 — Energy and carbon intensity:** E = 0.00101 kWh, I = 350 gCO2eq/kWh (IEA 2023)
- [x] **Item 5 — Functional unit:** 1 meeting workflow, methodology explained
- [x] **Item 6 — Embodied emissions:** M = 0, justified (consumer device)
- [x] **Item 7 — Attestation:** Verbatim 10-point template, signed and dated

---

Please let me know if anything else is needed.

Best regards,

Joel Nishant Reddy  
Co-founder, Offlyn.ai
