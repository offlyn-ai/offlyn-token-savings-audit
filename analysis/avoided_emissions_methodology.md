# Avoided Emissions Methodology

This document defines how the audit calculates and reports avoided carbon emissions when workloads move from cloud-first to local-first or hybrid architectures.

---

## Key Definitions

### Avoided Cloud Carbon

```
avoided_cloud_carbon_g =
  baseline_cloud_carbon_g - solution_cloud_carbon_g
```

This measures the cloud inference emissions that are no longer incurred because the workload runs locally. It does not account for any incremental local energy.

### Net Avoided Total Carbon

```
net_avoided_total_carbon_g =
  baseline_total_carbon_g - solution_total_carbon_g
```

Where:
```
baseline_total_carbon_g = cloud_carbon + local_incremental_carbon (if any)
solution_total_carbon_g = cloud_carbon + local_incremental_carbon
```

This is the true net difference: cloud savings minus any additional local energy consumed.

---

## Example: 60-Minute Meeting (Midpoint Assumptions)

| Metric | Cloud-First | Offline-First | Hybrid |
|--------|------------|---------------|--------|
| Cloud carbon (gCO2e) | 32.2 | 0 | 0.7 |
| Local incremental carbon (gCO2e) | 0 | 1.75 | 1.75 |
| Total consumer carbon (gCO2e) | 32.2 | 1.75 | 2.4 |
| Avoided cloud carbon (gCO2e) | -- | 32.2 | 31.5 |
| Net avoided total carbon (gCO2e) | -- | 30.5 | 29.8 |

---

## Why This Is Not an Offset or Credit

Avoided emissions represent a comparison between two architecture choices. They do not:

- Generate carbon credits or tradeable instruments
- Constitute verified emissions reductions under any carbon market standard
- Offset emissions from other activities
- Guarantee absolute emissions reduction at the organizational level

They are useful for:
- Architecture decision support
- FinOps and GreenOps cost-benefit analysis
- Directional sustainability reporting
- Identifying workloads suitable for local-first migration

---

## Reporting Requirements

When reporting avoided emissions, always include:

1. **Baseline architecture**: what the comparison is against (cloud-first)
2. **Functional unit**: per meeting, per month, per team, etc.
3. **Assumptions**: token proxy rate, grid intensity, incremental watts
4. **Claim level**: "modeled estimate" or "measured" or "verified"
5. **Caveat**: not an offset, credit, or certified reduction

---

## Consumer SCI Operational Proxy

The `consumer_sci_operational_proxy` metric reports operational carbon only:

```
consumer_sci_operational_proxy =
  (cloud_inference_carbon + local_incremental_carbon) / functional_unit_count
```

The `consumer_sci_full_estimate` adds allocated embodied carbon when available:

```
consumer_sci_full_estimate =
  consumer_sci_operational_proxy + (embodied_carbon_allocated / functional_unit_count)
```

This repo defaults to `operational_proxy` because embodied carbon allocation data is typically unavailable for cloud inference providers.

---

## Limitations

- Avoided emissions are counterfactual: they depend on what would have happened otherwise.
- The baseline (cloud-first) is a modeled architecture, not necessarily the user's current state.
- Cloud carbon per token varies significantly by model, hardware, and provider.
- Local incremental energy varies by device and workload.
- These figures should not be used for Scope 3 reporting without additional verification.
