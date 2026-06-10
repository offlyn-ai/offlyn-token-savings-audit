#!/usr/bin/env python3
"""
Offlyn SCI-AI Calculator

Extends the token savings calculator with SCI-AI-aligned reporting:
- Incremental local energy (above baseline device usage)
- Cloud token carbon intensity
- Datacenter cooling water avoidance
- Consumer SCI per multiple AI-native functional units
- Net avoided emissions accounting

Reference: Green Software Foundation SCI-AI / ISO/IEC 21031:2024-informed.
All outputs are modeled estimates, not certified environmental claims.
"""

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculate_savings import (
    REPO_ROOT,
    ASSUMPTIONS_DIR,
    load_all_assumptions,
    calculate_cloud_first_meeting,
    calculate_offline_first_meeting,
    calculate_hybrid_meeting,
    calculate_transcript_tokens,
)

SCI_AI_OUTPUT_FILE = REPO_ROOT / "analysis" / "generated_sci_ai_results.md"


def load_sci_ai_assumptions():
    base = load_all_assumptions()
    with open(ASSUMPTIONS_DIR / "sci_ai.yml", "r") as f:
        base["sci_ai"] = yaml.safe_load(f)
    with open(ASSUMPTIONS_DIR / "water.yml", "r") as f:
        base["water"] = yaml.safe_load(f)
    with open(ASSUMPTIONS_DIR / "network.yml", "r") as f:
        base["network"] = yaml.safe_load(f)
    return base


# --- Dataclass for structured disclosure output ---


@dataclass
class SciAiScenarioResult:
    scenario_name: str
    cloud_tokens: int
    token_reduction_pct: Optional[float]
    api_cost_usd: float
    cloud_carbon_g: float
    local_incremental_energy_kwh: float
    local_carbon_g: float
    total_operational_carbon_g: float
    sci_g_per_workflow: float
    sci_g_per_meeting_hour: float
    sci_g_per_second_audio: float
    sci_g_per_1k_cloud_tokens: Optional[float]
    direct_datacenter_water_liters: float
    water_included_in_sci: bool
    embodied_carbon_included: bool
    verification_status: str


# --- Validation helpers ---


def validate_non_negative(value: float, name: str) -> None:
    """Raise ValueError for negative values."""
    if value < 0:
        raise ValueError(f"{name} cannot be negative, got {value}")


def validate_positive_denominator(value: float, name: str) -> None:
    """Raise ValueError for zero or negative functional-unit denominators."""
    if value <= 0:
        raise ValueError(f"{name} must be positive (non-zero denominator), got {value}")


# --- Pure calculation functions ---


def calculate_local_carbon_g(local_kwh: float, grid_intensity_g_per_kwh: float) -> float:
    """Return local operational carbon in gCO2e."""
    validate_non_negative(local_kwh, "local_kwh")
    validate_non_negative(grid_intensity_g_per_kwh, "grid_intensity_g_per_kwh")
    return local_kwh * grid_intensity_g_per_kwh


def calculate_operational_sci_g_per_unit(
    total_operational_carbon_g: float, functional_unit_count: float
) -> float:
    """Return operational SCI proxy in gCO2e per functional unit."""
    validate_non_negative(total_operational_carbon_g, "total_operational_carbon_g")
    validate_positive_denominator(functional_unit_count, "functional_unit_count")
    return total_operational_carbon_g / functional_unit_count


def calculate_token_reduction_pct(baseline_tokens: int, solution_tokens: int) -> float:
    """Return token reduction percentage."""
    validate_non_negative(baseline_tokens, "baseline_tokens")
    validate_non_negative(solution_tokens, "solution_tokens")
    if baseline_tokens == 0:
        return 0.0
    return ((baseline_tokens - solution_tokens) / baseline_tokens) * 100


def calculate_incremental_local_energy(
    incremental_power_watts: float,
    active_processing_hours: float,
) -> float:
    """Return incremental local kWh above baseline device usage."""
    if incremental_power_watts < 0:
        raise ValueError("Incremental power watts cannot be negative")
    if active_processing_hours < 0:
        raise ValueError("Active processing hours cannot be negative")
    return (incremental_power_watts / 1000) * active_processing_hours


def calculate_cloud_token_carbon(
    cloud_tokens: int,
    co2e_g_per_1k_tokens: float,
) -> float:
    """Return cloud token carbon in gCO2e."""
    if cloud_tokens < 0:
        raise ValueError("Cloud tokens cannot be negative")
    if co2e_g_per_1k_tokens < 0:
        raise ValueError("CO2e per 1k tokens cannot be negative")
    return (cloud_tokens / 1000) * co2e_g_per_1k_tokens


def calculate_net_avoided_cloud_carbon(
    baseline_cloud_carbon_g: float,
    solution_cloud_carbon_g: float,
) -> float:
    """Return avoided cloud carbon, not including local increment."""
    return baseline_cloud_carbon_g - solution_cloud_carbon_g


def calculate_net_avoided_total_carbon(
    baseline_total_carbon_g: float,
    solution_total_carbon_g: float,
) -> float:
    """Return total net avoided carbon (cloud savings minus local increment)."""
    return baseline_total_carbon_g - solution_total_carbon_g


def calculate_network_transfer_avoided(
    meeting_minutes: float,
    architecture: str,
    assumptions: dict,
) -> dict:
    """Return network transfer metrics in MB for a given architecture.

    Returns dict with cloud_transfer_mb, avoided_transfer_mb.
    """
    net = assumptions.get("network", {})
    if not net.get("enabled", False):
        return {"cloud_transfer_mb": 0.0, "avoided_transfer_mb": 0.0}

    workload = assumptions.get("workload", {})
    cloud_cfg = net.get("cloud_first_transfers", {})

    audio_mb = cloud_cfg.get("audio_upload_mb_per_minute", 1.0) * meeting_minutes
    wl = assumptions.get("workload", {})
    wpm = wl.get("words_per_minute", 150)
    tpw = wl.get("tokens_per_word", 1.3)
    transcript_tokens = calculate_transcript_tokens(meeting_minutes, wpm, tpw)
    transcript_mb = (transcript_tokens * cloud_cfg.get("transcript_bytes_per_token", 4)) / (1024 * 1024)

    num_chunks = max(1, transcript_tokens // cloud_cfg.get("embedding_chunk_size_tokens", 512))
    embedding_mb = (num_chunks * cloud_cfg.get("embedding_dims", 768) * 4) / (1024 * 1024)

    queries = workload.get("queries_per_meeting", 5)
    qa_mb = (queries * cloud_cfg.get("qa_payload_bytes_per_query", 8000)) / (1024 * 1024)
    summary_mb = cloud_cfg.get("summary_response_bytes", 4800) / (1024 * 1024)
    action_mb = cloud_cfg.get("action_response_bytes", 3200) / (1024 * 1024)
    memory_mb = cloud_cfg.get("memory_response_bytes", 3000) / (1024 * 1024)
    followup_mb = cloud_cfg.get("followup_response_bytes", 1600) / (1024 * 1024)

    cloud_total_mb = audio_mb + transcript_mb + embedding_mb + qa_mb + summary_mb + action_mb + memory_mb + followup_mb

    if architecture == "offline_first":
        avoided_mb = cloud_total_mb
    elif architecture == "hybrid_router":
        avoided_mb = audio_mb + transcript_mb
    else:
        avoided_mb = 0.0

    return {
        "cloud_transfer_mb": cloud_total_mb,
        "avoided_transfer_mb": avoided_mb,
    }


def calculate_cloud_direct_water(
    cloud_it_energy_kwh: float,
    wue_l_per_kwh: float,
) -> float:
    """Return direct datacenter cooling water in liters."""
    if cloud_it_energy_kwh < 0:
        raise ValueError("Cloud IT energy cannot be negative")
    if wue_l_per_kwh < 0:
        raise ValueError("WUE cannot be negative")
    return cloud_it_energy_kwh * wue_l_per_kwh


def calculate_consumer_sci(
    total_consumer_carbon_g: float,
    functional_unit_count: float,
) -> float:
    """Return Consumer SCI in gCO2e per functional unit."""
    if functional_unit_count <= 0:
        raise ValueError(
            "Functional unit count must be positive (cannot divide by zero)"
        )
    return total_consumer_carbon_g / functional_unit_count


def estimate_cloud_it_energy_kwh(cloud_tokens: int, energy_per_1k_tokens_kwh: float = 0.001) -> float:
    """Estimate cloud IT energy from token count."""
    return (cloud_tokens / 1000) * energy_per_1k_tokens_kwh


# --- Multi-functional-unit reporting ---


def calculate_all_functional_units(meeting_carbon_g: float, meeting_minutes: int, assumptions: dict) -> dict:
    """
    Calculate Consumer SCI across all supported functional units for a single meeting.
    Returns dict of {functional_unit_name: gCO2e_per_unit}.
    """
    results = {}
    workload = assumptions["workload"]["defaults"]

    meeting_hours = meeting_minutes / 60.0
    if meeting_hours > 0:
        results["gco2e_per_meeting_hour"] = calculate_consumer_sci(meeting_carbon_g, meeting_hours)

    audio_seconds = meeting_minutes * 60.0
    if audio_seconds > 0:
        results["gco2e_per_second_audio"] = calculate_consumer_sci(meeting_carbon_g, audio_seconds)

    results["gco2e_per_transcript"] = meeting_carbon_g

    results["gco2e_per_workflow_execution"] = meeting_carbon_g

    summary_count = 1.0
    results["gco2e_per_accepted_summary"] = calculate_consumer_sci(meeting_carbon_g, summary_count)

    return results


def calculate_cloud_token_sci(cloud_tokens: int, cloud_carbon_g: float) -> float:
    """Return gCO2e per 1,000 cloud tokens. Returns N/A sentinel if no cloud tokens."""
    if cloud_tokens <= 0:
        return float("nan")
    return (cloud_carbon_g / cloud_tokens) * 1000


# --- Architecture-level SCI-AI calculations ---


def calculate_sci_ai_meeting(minutes: int, assumptions: dict) -> dict:
    """Calculate full SCI-AI metrics for all three architectures."""
    carbon = assumptions["carbon"]
    water = assumptions["water"]

    co2e_mid = carbon["carbon"]["cloud_token_co2e_g_per_1k_mid"]
    incremental_watts = carbon["energy"]["local_incremental_power_watts_mid"]
    grid_intensity = carbon["energy"]["grid_intensity_gco2e_per_kwh"]
    pue = carbon["energy"]["datacenter_pue"]
    wue = water["generic_cloud_wue_l_per_kwh"]

    cf = calculate_cloud_first_meeting(minutes, assumptions)
    of = calculate_offline_first_meeting(minutes, assumptions)
    hr = calculate_hybrid_meeting(minutes, assumptions)

    active_hours = minutes / 60.0

    results = {}
    for arch_key, meeting in [("cloud_first", cf), ("offline_first", of), ("hybrid_router", hr)]:
        cloud_tokens = meeting["cloud_billable_tokens"]

        cloud_carbon_g = calculate_cloud_token_carbon(cloud_tokens, co2e_mid)

        local_incremental_kwh = calculate_incremental_local_energy(incremental_watts, active_hours)
        local_incremental_carbon_g = local_incremental_kwh * grid_intensity

        if arch_key == "cloud_first":
            local_incremental_kwh = 0.0
            local_incremental_carbon_g = 0.0

        total_carbon_g = cloud_carbon_g + local_incremental_carbon_g

        cloud_it_energy_kwh = estimate_cloud_it_energy_kwh(cloud_tokens)
        direct_water_l = calculate_cloud_direct_water(cloud_it_energy_kwh * pue, wue)

        functional_units = calculate_all_functional_units(total_carbon_g, minutes, assumptions)

        token_sci = calculate_cloud_token_sci(cloud_tokens, cloud_carbon_g)

        network = calculate_network_transfer_avoided(minutes, arch_key, assumptions)

        results[arch_key] = {
            "architecture": arch_key,
            "meeting_minutes": minutes,
            "cloud_billable_tokens": cloud_tokens,
            "cloud_carbon_gco2e": round(cloud_carbon_g, 4),
            "local_incremental_kwh": round(local_incremental_kwh, 6),
            "local_incremental_carbon_gco2e": round(local_incremental_carbon_g, 4),
            "total_consumer_carbon_gco2e": round(total_carbon_g, 4),
            "direct_datacenter_water_liters": round(direct_water_l, 6),
            "cloud_transfer_mb": round(network["cloud_transfer_mb"], 3),
            "avoided_transfer_mb": round(network["avoided_transfer_mb"], 3),
            "gco2e_per_1k_cloud_tokens": round(token_sci, 4) if token_sci == token_sci else "N/A",
            **{k: round(v, 6) for k, v in functional_units.items()},
        }

    baseline_cloud_carbon = results["cloud_first"]["cloud_carbon_gco2e"]
    baseline_total_carbon = results["cloud_first"]["total_consumer_carbon_gco2e"]
    baseline_water = results["cloud_first"]["direct_datacenter_water_liters"]

    for arch_key in ["offline_first", "hybrid_router"]:
        r = results[arch_key]
        r["avoided_cloud_carbon_gco2e"] = round(
            calculate_net_avoided_cloud_carbon(baseline_cloud_carbon, r["cloud_carbon_gco2e"]), 4
        )
        r["net_avoided_total_carbon_gco2e"] = round(
            calculate_net_avoided_total_carbon(baseline_total_carbon, r["total_consumer_carbon_gco2e"]), 4
        )
        r["avoided_direct_water_liters"] = round(baseline_water - r["direct_datacenter_water_liters"], 6)

    results["cloud_first"]["avoided_cloud_carbon_gco2e"] = 0.0
    results["cloud_first"]["net_avoided_total_carbon_gco2e"] = 0.0
    results["cloud_first"]["avoided_direct_water_liters"] = 0.0

    return results


# --- Rendering ---


def render_sci_ai_table(results: dict, title: str) -> str:
    lines = []
    lines.append(f"### {title}\n")
    lines.append("| Metric | Cloud-First | Offline-First | Hybrid Router |")
    lines.append("|--------|------------:|-------------:|-------------:|")

    cf = results["cloud_first"]
    of = results["offline_first"]
    hr = results["hybrid_router"]

    rows = [
        ("Cloud billable tokens", "cloud_billable_tokens", ",d"),
        ("Cloud carbon (gCO2e)", "cloud_carbon_gco2e", ".4f"),
        ("Local incremental kWh", "local_incremental_kwh", ".6f"),
        ("Local incremental carbon (gCO2e)", "local_incremental_carbon_gco2e", ".4f"),
        ("Total consumer carbon (gCO2e)", "total_consumer_carbon_gco2e", ".4f"),
        ("Avoided cloud carbon (gCO2e)", "avoided_cloud_carbon_gco2e", ".4f"),
        ("Net avoided total carbon (gCO2e)", "net_avoided_total_carbon_gco2e", ".4f"),
        ("Direct datacenter water (L)", "direct_datacenter_water_liters", ".6f"),
        ("Avoided direct water (L)", "avoided_direct_water_liters", ".6f"),
        ("Consumer SCI: gCO2e/meeting hour", "gco2e_per_meeting_hour", ".4f"),
        ("Consumer SCI: gCO2e/second audio", "gco2e_per_second_audio", ".6f"),
        ("Consumer SCI: gCO2e/transcript", "gco2e_per_transcript", ".4f"),
        ("Consumer SCI: gCO2e/1k cloud tokens", "gco2e_per_1k_cloud_tokens", "s"),
        ("Consumer SCI: gCO2e/workflow exec", "gco2e_per_workflow_execution", ".4f"),
        ("Consumer SCI: gCO2e/accepted summary", "gco2e_per_accepted_summary", ".4f"),
    ]

    for label, key, fmt in rows:
        vals = []
        for arch in [cf, of, hr]:
            v = arch.get(key, "N/A")
            if v == "N/A" or (isinstance(v, float) and v != v):
                vals.append("N/A")
            elif fmt == ",d":
                vals.append(f"{int(v):,}")
            elif fmt == "s":
                vals.append(f"{v}")
            else:
                vals.append(f"{v:{fmt}}")
        lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} |")

    lines.append("")
    return "\n".join(lines)


def render_sci_ai_markdown(all_results: dict) -> str:
    lines = []
    lines.append("# Generated SCI-AI Results: Offlyn AI Resource Avoidance Audit\n")
    lines.append("> Auto-generated by `scripts/calculate_sci_ai.py`.")
    lines.append("> SCI-AI-aligned reporting. All values are modeled estimates, not certified claims.")
    lines.append("> Reference: Green Software Foundation SCI-AI / ISO/IEC 21031:2024-informed.\n")
    lines.append("---\n")
    lines.append("## Consumer SCI Comparison by Meeting Duration\n")

    for duration_label, duration_min in [("30-Minute Meeting", 30), ("60-Minute Meeting", 60), ("90-Minute Meeting", 90)]:
        results = all_results[duration_min]
        lines.append(render_sci_ai_table(results, duration_label))

    lines.append("---\n")
    lines.append("## Methodology Notes\n")
    lines.append("- **Boundary**: Consumer SCI (operational AI consumption only).")
    lines.append("- **Reporting mode**: Operational proxy (embodied carbon excluded by default).")
    lines.append("- **Local energy model**: Incremental inference above baseline device usage (5W midpoint).")
    lines.append("- **Cloud carbon**: Token proxy method (0.50 gCO2e per 1,000 tokens midpoint).")
    lines.append("- **Water**: Direct datacenter cooling water only. Not part of SCI carbon formula.")
    lines.append("- **Provider SCI**: Not included (no model training or fine-tuning in scope).")
    lines.append("- **Functional units**: Meeting hour, second of audio, transcript, workflow execution, accepted summary.")
    lines.append("")
    lines.append("## Claim Status\n")
    lines.append("These are modeled estimates for architecture comparison and decision support.")
    lines.append("They are not carbon credits, offsets, certified emissions reductions, or ISO/SCI certifications.")
    lines.append("See `analysis/claims_policy.md` for allowed and disallowed claims.")
    lines.append("")

    return "\n".join(lines)


def main():
    assumptions = load_sci_ai_assumptions()

    all_results = {}
    for minutes in [30, 60, 90]:
        all_results[minutes] = calculate_sci_ai_meeting(minutes, assumptions)

    markdown = render_sci_ai_markdown(all_results)

    SCI_AI_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SCI_AI_OUTPUT_FILE, "w") as f:
        f.write(markdown)

    print(f"SCI-AI results written to: {SCI_AI_OUTPUT_FILE}")
    print(f"\n--- 60-Minute Meeting SCI-AI Summary ---")
    m60 = all_results[60]
    for arch in ["cloud_first", "offline_first", "hybrid_router"]:
        r = m60[arch]
        print(f"\n{arch}:")
        print(f"  Cloud carbon: {r['cloud_carbon_gco2e']} gCO2e")
        print(f"  Local incremental carbon: {r['local_incremental_carbon_gco2e']} gCO2e")
        print(f"  Total consumer carbon: {r['total_consumer_carbon_gco2e']} gCO2e")
        print(f"  Direct datacenter water: {r['direct_datacenter_water_liters']} L")
        print(f"  Consumer SCI (per meeting hour): {r['gco2e_per_meeting_hour']} gCO2e/hr")
        print(f"  Net avoided total carbon: {r['net_avoided_total_carbon_gco2e']} gCO2e")

    return all_results


if __name__ == "__main__":
    main()
