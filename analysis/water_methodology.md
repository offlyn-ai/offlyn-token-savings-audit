# Water Use Methodology

This audit estimates avoided datacenter cooling-water demand for workloads moved from cloud-first to local-first or hybrid execution.

**Water is supplemental and is not included in the SCI carbon score.** It is reported as a separate infrastructure-efficiency metric to inform decision-making without conflating distinct environmental impacts.

---

## Why Water Matters for AI

Large-scale AI inference requires GPU clusters that generate significant heat. Datacenters use cooling systems that consume water directly (evaporative cooling towers) or indirectly (electricity generation). Moving workloads from cloud inference to local devices reduces demand on datacenter cooling infrastructure.

---

## Default Model

```
cloud_direct_water_liters =
  cloud_it_energy_kwh * cloud_wue_liters_per_kwh

hybrid_direct_water_liters =
  baseline_cloud_it_energy_kwh
  * cloud_routed_fraction
  * cloud_wue_liters_per_kwh

local_direct_cooling_water_liters = 0
```

Where:
- `cloud_it_energy_kwh` is estimated from cloud token count
- `cloud_wue_liters_per_kwh` is the Water Usage Effectiveness of the datacenter
- Local devices do not use datacenter-style evaporative cooling

---

## Water Usage Effectiveness (WUE) Assumptions

| Datacenter Type | WUE (L/kWh) | Source |
|----------------|------------:|--------|
| Efficient hyperscaler | 0.27 | Industry reports for modern facilities |
| Generic cloud datacenter | 1.90 | Industry average for older facilities |
| Local device | 0.0 | No datacenter cooling system |

Default: `generic_cloud_wue_l_per_kwh: 1.90`

These values are configurable in `assumptions/water.yml`.

---

## Example: 60-Minute Meeting

Using the generic WUE (1.90 L/kWh):

**Cloud-first:**
- Cloud IT energy: ~0.077 kWh (estimated from 64,450 tokens)
- Direct water: ~0.077 * 1.2 (PUE) * 1.90 = ~0.147 L

**Offline-first:**
- Cloud IT energy: 0 kWh
- Direct water: 0 L

**Hybrid:**
- Cloud IT energy: ~0.0016 kWh (estimated from 1,354 tokens)
- Direct water: ~0.003 L

---

## What This Model Does Not Include

- **Indirect electricity-generation water**: Water used to generate the electricity that powers both datacenters and local devices. Excluded by default because it applies to all architectures.
- **Embodied water**: Water used in semiconductor manufacturing and hardware production.
- **Office HVAC**: Building cooling where the local device operates.

---

## Caveats

- **Local-first AI is not water-free.** Local devices still use electricity, and electricity generation may have indirect water impacts. The default model only estimates reduction in direct cloud datacenter cooling-water demand.
- This default model only estimates direct datacenter cooling water.
- Do not claim local AI is "water-free."
- Claim only that local-first and hybrid routing can reduce datacenter cooling-water dependency.
- WUE varies significantly by geography, climate, and facility age.
- Some datacenters use closed-loop cooling with minimal water consumption.

---

## Claim Language

Allowed:
- "Estimated reduction in datacenter cooling-water demand"
- "Direct cooling water avoided"
- "Supplemental water efficiency metric"

Disallowed:
- "Water-free AI"
- "Zero water impact"
- "Water neutral"

See `analysis/claims_policy.md` for the full claims framework.
