# Scenarios

This document describes the standard scenarios used for team-scale savings calculations.

## Scenario A: Solo User

A single professional using meeting intelligence for their own meetings.

| Parameter | Value |
|-----------|------:|
| Team size | 1 |
| Meetings per month | 20 |
| Average meeting duration | 60 min |
| Q&A queries per meeting | 5 |
| Follow-up drafts per meeting | 1 |

**Typical profile**: IC engineer, product manager, consultant, or researcher who records their own meetings and searches/queries their notes daily.

## Scenario B: Small Team

A team of 5 people sharing meeting intelligence infrastructure.

| Parameter | Value |
|-----------|------:|
| Team size | 5 |
| Meetings per month (total) | 100 |
| Average meeting duration | 60 min |
| Q&A queries per meeting | 5 |
| Follow-up drafts per meeting | 1 |

**Typical profile**: startup team, small department, or project group where all members record meetings and use search/Q&A regularly.

## Scenario C: Enterprise Team

A department or business unit with 50 people.

| Parameter | Value |
|-----------|------:|
| Team size | 50 |
| Meetings per month (total) | 1,000 |
| Average meeting duration | 60 min |
| Q&A queries per meeting | 5 |
| Follow-up drafts per meeting | 1 |

**Typical profile**: enterprise department, consulting practice, or sales organization where meeting intelligence is deployed across the group.

## How to Customize Scenarios

Edit `assumptions/workload.yml` to define your own scenarios:

```yaml
scenarios:
  my_org:
    meetings_per_month: 500
    average_minutes: 45
    team_size: 25
```

Then run:
```bash
python scripts/calculate_savings.py
```

## Scaling Notes

- Token usage and cost scale linearly with meeting count.
- Q&A-heavy teams will have higher cloud-first costs due to per-query token expansion.
- Organizations with longer meetings (90+ min) will see larger absolute savings.
- Teams with high-sensitivity meetings benefit most from offline-first or local-only hybrid policies.
