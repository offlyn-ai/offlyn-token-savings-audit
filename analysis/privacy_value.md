# Privacy and Compliance Value

This document describes the privacy implications of each architecture for enterprise meeting intelligence.

## Why Local-First Meeting Intelligence Changes the Privacy Model

In a cloud-first architecture, meeting transcripts — containing sensitive conversations, strategic decisions, personnel discussions, and proprietary information — are sent to third-party APIs for processing. Each intelligence step (summarization, Q&A, embeddings, memory) creates an additional data exposure event.

A local-first architecture eliminates these exposure events by processing all intelligence on-device. The hybrid router minimizes them by sending only compact derived context when escalation is needed.

## Data That Stays on Device in Offlyn Clipper

| Data Type | Stays Local? |
|-----------|:------------:|
| Raw audio recording | Yes |
| Full transcript | Yes |
| Speaker identity labels | Yes |
| Meeting summary | Yes |
| Action items | Yes |
| Key moments | Yes |
| Embeddings/vectors | Yes |
| Search indexes | Yes |
| Q&A answers | Yes |
| Memory digests | Yes |
| Document content | Yes |
| OCR results | Yes |

No data leaves the device unless the user explicitly enables cloud features.

## Cloud Exposure in a Cloud-First Baseline

| Data Type | Sent to Cloud? |
|-----------|:--------------:|
| Audio (for transcription) | Potentially |
| Full transcript (for LLM tasks) | Yes |
| Meeting context (for Q&A) | Yes |
| Embeddings | Yes |
| Summary and action items (generated cloud-side) | Processed remotely |
| Memory consolidation input | Yes |

Each cloud API call represents a data exposure event subject to the provider's data handling, retention, and training policies.

## Hybrid Routing Privacy Controls

The hybrid router adds privacy safeguards when cloud fallback is used:

1. **No raw transcript sent**: only compact derived context (summaries, snippets).
2. **No audio uploaded**: transcription is always local.
3. **No embeddings sent**: vector generation is local.
4. **No memory consolidation sent**: daily/weekly digests stay local.
5. **Compact context ratio**: fallback tasks receive ~20% of the token volume that cloud-first would send.
6. **Per-meeting policy**: sensitive meetings can be marked "local-only" regardless of confidence.
7. **Audit trail**: every cloud escalation is logged with reason and token count.

## Compliance-Sensitive Scenarios

| Scenario | Recommended Architecture |
|----------|--------------------------|
| Executive strategy session | Offline-first (no cloud exposure) |
| Legal privileged conversation | Offline-first |
| HR personnel discussion | Offline-first |
| Healthcare patient discussion | Offline-first |
| Financial earnings pre-release | Offline-first |
| Cross-border regulated data | Offline-first or hybrid with jurisdiction controls |
| Standard team standup | Any (low sensitivity) |
| Client meeting with NDA | Offline-first or hybrid local-only |
| Field operation without connectivity | Offline-first |

## Sensitive Industries

Industries where local-first meeting intelligence provides particular value:

- **Healthcare**: patient information must not leave controlled environments.
- **Legal**: attorney-client privilege requires strict data handling.
- **Financial services**: material non-public information regulations.
- **Defense and government**: classified or controlled unclassified information.
- **Pharmaceutical**: R&D discussions with IP sensitivity.
- **Human resources**: personnel discussions with privacy requirements.

## Vendor Lock-In Reduction

Local-first architecture reduces dependency on cloud AI providers:

- No ongoing API subscription required for core functionality.
- Switching providers (or eliminating them) does not disrupt existing meeting intelligence.
- Historical data remains accessible without cloud API access.
- No risk of provider deprecating models or changing pricing.
- No data portability concerns — all data is already local.

## Offline Resilience

| Capability | Cloud-First | Offline-First | Hybrid |
|------------|:-----------:|:-------------:|:------:|
| Transcription | Requires internet | Works offline | Works offline |
| Summarization | Requires internet | Works offline | Works offline (local) |
| Search | May require internet | Works offline | Works offline |
| Q&A | Requires internet | Works offline | Works offline (local, cloud optional) |
| Document processing | May require internet | Works offline | Works offline |

Offline-first provides full functionality during:
- Air travel
- Remote field work
- Network outages
- Intentional disconnection (field mode)
- Bandwidth-constrained environments

## Risk and Governance Checklist

For enterprises evaluating meeting intelligence architectures:

- [ ] Where is meeting audio processed? (local vs. cloud)
- [ ] Where are transcripts stored? (on-device vs. provider infrastructure)
- [ ] What data is sent to third-party APIs?
- [ ] What is the provider's data retention policy?
- [ ] Is meeting data used for model training?
- [ ] Can specific meetings be excluded from cloud processing?
- [ ] Is there an audit trail for cloud data transmissions?
- [ ] Does the system work offline for sensitive contexts?
- [ ] What happens to data if the vendor relationship ends?
- [ ] Are there jurisdictional data residency controls?

## Important Disclaimer

Local-first architecture may support compliance programs by reducing third-party data exposure, but compliance depends on deployment, controls, policies, auditing, encryption, retention, access control, vendor agreements, and organizational governance. This document does not constitute legal advice or claim automatic compliance with any regulation including HIPAA, SOC 2, GDPR, or ISO standards.
