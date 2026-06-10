# Certification Readiness Checklist

25 items, 4 points each, 100 maximum score.

Target: 100/100 internal completeness before GSF SCI self-certification submission.

## Checklist

| # | Item | Points | Status |
|---|------|--------|--------|
| 1 | Software system described | 4 | |
| 2 | Disclosure version present | 4 | |
| 3 | Boundary clearly defined | 4 | |
| 4 | Functional unit clearly defined | 4 | |
| 5 | SCI formula included | 4 | |
| 6 | Operational emissions included | 4 | |
| 7 | Embodied emissions included or explicitly excluded with rationale | 4 | |
| 8 | Energy assumptions documented | 4 | |
| 9 | Carbon intensity assumptions documented | 4 | |
| 10 | Water disclosed as supplemental and excluded from SCI score | 4 | |
| 11 | Avoided emissions separated from SCI score | 4 | |
| 12 | Cloud-first/local-first/hybrid scenarios documented | 4 | |
| 13 | Token calculations reproducible | 4 | |
| 14 | Carbon calculations reproducible | 4 | |
| 15 | Water calculations reproducible | 4 | |
| 16 | Quality methodology disclosed | 4 | |
| 17 | Quality scores marked modeled or measured | 4 | |
| 18 | Claims policy exists | 4 | |
| 19 | Disallowed claims absent from public claims | 4 | |
| 20 | Attestation file exists | 4 | |
| 21 | Evidence log exists | 4 | |
| 22 | Limitations file exists | 4 | |
| 23 | Calculation CSV exists | 4 | |
| 24 | Tests pass or test command documented | 4 | |
| 25 | README disclosure status present | 4 | |

## Scoring

- **100/100**: All items pass. Certification-ready for GSF SCI self-certification submission.
- **96-99/100**: Minor gaps. Review remediation items before submission.
- **< 96/100**: Significant gaps. Address missing items before proceeding.

## How to Run

```bash
python scripts/validate_sci_ai_disclosure.py --strict
```

This produces `certification/certification_readiness_score.json` with pass/fail status and remediation guidance for each item.

## Important Note

A perfect score (100/100) indicates internal completeness. It does not guarantee GSF approval. The Green Software Foundation's SCI self-certification program checks that required disclosure information is present; responsibility remains with the applicant through self-attestation.
