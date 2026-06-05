# Hybrid Local-First Router

This document describes the architecture that gives enterprises a practical balance between local-first privacy/cost savings and cloud-quality fallback for tasks that benefit from it.

## Hybrid Routing Thesis

Most meeting intelligence tasks are routine: summarization, action item extraction, keyword search, Q&A over personal notes. These can run locally with high quality. A small percentage of tasks genuinely benefit from frontier cloud models: complex reasoning, external knowledge, low-confidence answers, or tasks where the user explicitly requests cloud quality.

The hybrid router:
1. Runs all tasks locally by default.
2. Scores confidence and task complexity.
3. Escalates only selected tasks to cloud with compact context.
4. Logs every escalation for audit and cost tracking.

## Routing Policy

| Task | Default Route | Cloud Fallback Allowed? | Context Sent if Fallback |
|------|---------------|:-----------------------:|--------------------------|
| Transcription | local | no | none |
| Summary | local | optional (5%) | compact summary only |
| Action items | local | optional (5%) | relevant snippets |
| Key moments | local | optional (5%) | timestamps + snippets |
| Q&A | local | yes (20%) | top chunks + question |
| Memory | local | no by default | none |
| Follow-up email | local | yes (15%) | summary + selected decisions |
| External/latest knowledge | cloud | yes | question only or approved context |

Default fallback rates are configurable in `assumptions/routing.yml`.

## Confidence Thresholds

The router decides based on:
- **Answer confidence**: local LLM self-assessed confidence score.
- **Task complexity**: multi-hop reasoning, external facts, legal/regulatory language.
- **User preference**: explicit "use cloud" toggle.
- **Enterprise policy**: compliance rules that block or allow cloud for certain meeting types.
- **Connectivity**: if offline or in field mode, all tasks remain local regardless of confidence.

## Compact Context Strategy

When a task is escalated to cloud, the hybrid router does **not** send the full transcript. Instead it sends:
- Local summary (compressed representation)
- Top retrieved snippets (relevant chunks only)
- Citations and source references
- Uncertainty explanation (why local was insufficient)
- User question or task instruction

This compact context is approximately 20% of the full transcript token count, configured via `compact_context_ratio` in `assumptions/routing.yml`.

## Cloud Escalation Reasons

Tasks may be escalated when:
- Local answer confidence is below threshold
- Task requires complex multi-step reasoning
- User requests external or latest knowledge
- User explicitly requests cloud-quality response
- Enterprise policy approves escalation for the task type

Tasks that are **never** escalated by default:
- Transcription
- Raw audio upload
- Full transcript upload
- Memory consolidation
- Sensitive meeting summaries (executive, legal, HR)

## Token Savings vs Cloud-First

Using default assumptions for a 60-minute meeting:
- Cloud-first billable tokens: 64,450
- Hybrid billable tokens: ~1,354
- Token reduction: ~97.9%

The hybrid router avoids most cloud tokens because:
1. Transcription stays local (saves audio-minute charges + transcript tokens)
2. Embeddings stay local (saves embedding tokens)
3. Memory stays local (saves a full transcript pass)
4. Only a fraction of summary/action/Q&A/followup tasks fall back
5. Fallback tasks send compact context (20% of full), not the raw transcript

## Quality Tradeoff vs Offline-Only

The hybrid router can achieve higher quality than pure offline on difficult tasks:
- Complex reasoning benefits from frontier cloud models
- External knowledge queries can access current information
- Low-confidence local answers get a "second opinion"

For routine tasks, quality is equivalent to offline-first since the same local models handle them.

## Privacy Safeguards

- Raw transcript never leaves the device by default
- Full audio never uploaded
- Compact context sent on fallback contains only derived summaries and snippets
- Each escalation is logged with reason, timestamp, and tokens sent
- Enterprise can configure which meeting types allow cloud fallback
- Sensitive meetings (executive, legal, HR) default to local-only

## Audit Logging

Every cloud escalation records:
- Task type
- Escalation reason
- Compact context token count
- Cloud response token count
- Timestamp
- Meeting sensitivity classification
- User who triggered escalation

This enables cost attribution, compliance review, and fallback rate optimization over time.

## Example Routing Outcomes

| Scenario | Route | Reason |
|----------|-------|--------|
| Routine summary of team standup | Local | High confidence, standard task |
| Action items from project meeting | Local | Structured extraction, local quality sufficient |
| "What did I miss?" | Local | Retrieval + local LLM, fast and private |
| Search my notes for decision on pricing | Local | Hybrid search, local answer composition |
| Sensitive executive meeting summary | Local only | Policy: no cloud for exec meetings |
| Complex legal contract question | Cloud fallback | Multi-hop reasoning, low local confidence |
| "What's the latest public earnings?" | Cloud allowed | External knowledge required |
| Low-confidence answer about budget | Cloud fallback | Local flagged uncertainty, compact context sent |
| Field mode / offline | Local only | No connectivity, full functionality maintained |
