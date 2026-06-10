#!/usr/bin/env python3
"""
Export SCI for AI-aligned Disclosure

Generates:
- certification/sci_ai_calculation.csv (3 scenarios x 16 columns)
- certification/certification_readiness_score.json (via validator)

Usage:
    python scripts/export_sci_ai_disclosure.py
"""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculate_savings import (
    load_all_assumptions,
    calculate_cloud_first_meeting,
    calculate_offline_first_meeting,
    calculate_hybrid_meeting,
)
from calculate_sci_ai import (
    load_sci_ai_assumptions,
    calculate_sci_ai_meeting,
    calculate_token_reduction_pct,
    calculate_local_carbon_g,
    calculate_operational_sci_g_per_unit,
    SciAiScenarioResult,
)
from validate_sci_ai_disclosure import run_checklist, calculate_score

REPO_ROOT = Path(__file__).resolve().parent.parent
CERT_DIR = REPO_ROOT / "certification"


def build_scenario_results(minutes: int = 60) -> list:
    assumptions = load_sci_ai_assumptions()
    sci_results = calculate_sci_ai_meeting(minutes, assumptions)

    savings_assumptions = load_all_assumptions()
    cf = calculate_cloud_first_meeting(minutes, savings_assumptions)
    of = calculate_offline_first_meeting(minutes, savings_assumptions)
    hr = calculate_hybrid_meeting(minutes, savings_assumptions)

    baseline_tokens = cf["cloud_billable_tokens"]

    scenarios = []
    for arch_key, arch_name, savings in [
        ("cloud_first", "Cloud-first", cf),
        ("offline_first", "Local-first", of),
        ("hybrid_router", "Hybrid local-first router", hr),
    ]:
        sci = sci_results[arch_key]
        cloud_tokens = savings["cloud_billable_tokens"]

        token_reduction = calculate_token_reduction_pct(baseline_tokens, cloud_tokens) if arch_key != "cloud_first" else None

        sci_per_1k = None
        if cloud_tokens > 0:
            sci_per_1k = sci["cloud_carbon_gco2e"] / (cloud_tokens / 1000)

        result = SciAiScenarioResult(
            scenario_name=arch_name,
            cloud_tokens=cloud_tokens,
            token_reduction_pct=round(token_reduction, 2) if token_reduction is not None else None,
            api_cost_usd=savings["cloud_total_cost_usd"],
            cloud_carbon_g=sci["cloud_carbon_gco2e"],
            local_incremental_energy_kwh=sci["local_incremental_kwh"],
            local_carbon_g=sci["local_incremental_carbon_gco2e"],
            total_operational_carbon_g=sci["total_consumer_carbon_gco2e"],
            sci_g_per_workflow=sci["total_consumer_carbon_gco2e"],
            sci_g_per_meeting_hour=sci.get("gco2e_per_meeting_hour", sci["total_consumer_carbon_gco2e"]),
            sci_g_per_second_audio=sci.get("gco2e_per_second_audio", sci["total_consumer_carbon_gco2e"] / 3600),
            sci_g_per_1k_cloud_tokens=round(sci_per_1k, 4) if sci_per_1k is not None else None,
            direct_datacenter_water_liters=sci["direct_datacenter_water_liters"],
            water_included_in_sci=False,
            embodied_carbon_included=False,
            verification_status="self_attested_modeled_not_certified",
        )
        scenarios.append(result)

    return scenarios


def export_csv(scenarios: list, output_path: Path):
    columns = [
        "scenario", "cloud_tokens", "token_reduction_pct", "api_cost_usd",
        "cloud_carbon_g", "local_incremental_energy_kwh", "local_carbon_g",
        "total_operational_carbon_g", "sci_g_per_workflow", "sci_g_per_meeting_hour",
        "sci_g_per_second_audio", "sci_g_per_1k_cloud_tokens",
        "direct_datacenter_water_liters", "water_included_in_sci",
        "embodied_carbon_included", "verification_status",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for s in scenarios:
            writer.writerow([
                s.scenario_name,
                s.cloud_tokens,
                s.token_reduction_pct if s.token_reduction_pct is not None else "N/A",
                round(s.api_cost_usd, 6),
                round(s.cloud_carbon_g, 4),
                round(s.local_incremental_energy_kwh, 6),
                round(s.local_carbon_g, 4),
                round(s.total_operational_carbon_g, 4),
                round(s.sci_g_per_workflow, 4),
                round(s.sci_g_per_meeting_hour, 4),
                round(s.sci_g_per_second_audio, 6),
                round(s.sci_g_per_1k_cloud_tokens, 4) if s.sci_g_per_1k_cloud_tokens is not None else "N/A",
                round(s.direct_datacenter_water_liters, 6),
                s.water_included_in_sci,
                s.embodied_carbon_included,
                s.verification_status,
            ])


def export_readiness_score(output_path: Path) -> dict:
    import json
    items = run_checklist()
    result = calculate_score(items)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    return result


def main():
    csv_path = CERT_DIR / "sci_ai_calculation.csv"
    score_path = CERT_DIR / "certification_readiness_score.json"

    print("SCI for AI-aligned Disclosure Export")
    print("=" * 50)

    scenarios = build_scenario_results(60)
    export_csv(scenarios, csv_path)
    print(f"\nGenerated: {csv_path}")

    print("\nDisclosure Summary (60-minute meeting workflow):")
    print("-" * 50)
    print(f"{'Metric':<35} {'Cloud-first':>12} {'Local-first':>12} {'Hybrid':>12}")
    print("-" * 50)
    for attr, label in [
        ("cloud_tokens", "Cloud tokens"),
        ("api_cost_usd", "API cost (USD)"),
        ("total_operational_carbon_g", "Total carbon (gCO2e)"),
        ("sci_g_per_workflow", "SCI per workflow (gCO2e)"),
        ("direct_datacenter_water_liters", "Water (liters, supplemental)"),
    ]:
        vals = []
        for s in scenarios:
            v = getattr(s, attr)
            if isinstance(v, float):
                vals.append(f"{v:.4f}")
            else:
                vals.append(str(v))
        print(f"{label:<35} {vals[0]:>12} {vals[1]:>12} {vals[2]:>12}")

    print(f"\nWater included in SCI: No (supplemental only)")
    print(f"Embodied carbon included: No (M = 0, excluded by default)")
    print(f"Verification: Self-attested, modeled, not certified")

    # Generate readiness score (CSV must exist first for item 23)
    score_result = export_readiness_score(score_path)
    print(f"\nCertification readiness: {score_result['score']}/{score_result['max']}")
    print(f"Generated: {score_path}")

    if score_result["score"] < 100:
        failed = [i for i in score_result["items"] if not i["passed"]]
        if failed:
            print(f"\nRemaining gaps ({len(failed)}):")
            for item in failed:
                print(f"  - {item['description']}")


if __name__ == "__main__":
    main()
