#!/usr/bin/env python3
"""
Offlyn Token Savings Calculator

Calculates cloud token usage, API cost, quality scores, and savings
for cloud-first, offline-first, and hybrid meeting intelligence architectures.
"""

import os
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
ASSUMPTIONS_DIR = REPO_ROOT / "assumptions"
OUTPUT_FILE = REPO_ROOT / "analysis" / "generated_results.md"


def load_yaml(filename):
    with open(ASSUMPTIONS_DIR / filename, "r") as f:
        return yaml.safe_load(f)


def load_all_assumptions():
    return {
        "pricing": load_yaml("pricing.yml"),
        "workload": load_yaml("workload.yml"),
        "routing": load_yaml("routing.yml"),
        "quality": load_yaml("quality.yml"),
        "carbon": load_yaml("carbon.yml"),
    }


def calculate_transcript_tokens(minutes, words_per_minute, tokens_per_word):
    return int(minutes * words_per_minute * tokens_per_word)


def get_meeting_profile(minutes, workload):
    meetings = workload["meetings"]
    if minutes <= 30:
        return meetings["short"]
    elif minutes <= 60:
        return meetings["standard"]
    else:
        return meetings["long"]


def calculate_cloud_first_meeting(minutes, assumptions):
    workload = assumptions["workload"]
    pricing = assumptions["pricing"]
    carbon = assumptions["carbon"]
    quality = assumptions["quality"]

    defaults = workload["defaults"]
    profile = get_meeting_profile(minutes, workload)

    wpm = defaults["words_per_minute"]
    tpw = defaults["tokens_per_word"]
    transcript_tokens = calculate_transcript_tokens(minutes, wpm, tpw)

    summary_input = transcript_tokens
    summary_output = profile["summary_output_tokens"]

    action_input = transcript_tokens
    action_output = profile["action_output_tokens"]

    embedding_tokens = transcript_tokens

    qa_queries = defaults["qa_queries_per_meeting"]
    qa_input = qa_queries * defaults["qa_input_tokens_per_query"]
    qa_output = qa_queries * defaults["qa_output_tokens_per_query"]

    memory_input = transcript_tokens
    memory_output = profile["memory_output_tokens"]

    followup_drafts = defaults["followup_drafts_per_meeting"]
    followup_input = followup_drafts * defaults["followup_input_tokens_per_draft"]
    followup_output = followup_drafts * defaults["followup_output_tokens_per_draft"]

    llm_input_total = (
        summary_input + action_input + qa_input + memory_input + followup_input
    )
    llm_output_total = (
        summary_output + action_output + qa_output + memory_output + followup_output
    )
    cloud_billable_tokens = llm_input_total + llm_output_total + embedding_tokens

    transcription_cost = minutes * pricing["transcription"]["cloud_whisper_per_minute_usd"]
    llm_cost = (
        (llm_input_total / 1_000_000) * pricing["llm"]["input_per_1m_tokens_usd"]
        + (llm_output_total / 1_000_000) * pricing["llm"]["output_per_1m_tokens_usd"]
    )
    embedding_cost = (
        (embedding_tokens / 1_000_000) * pricing["embedding"]["input_per_1m_tokens_usd"]
    )
    cloud_total_cost = transcription_cost + llm_cost + embedding_cost
    local_compute_cost = 0.0
    total_cost = cloud_total_cost + local_compute_cost

    scores = quality["modeled_scores"]["cloud_first"]
    weights = quality["quality_weights"]
    quality_score = calculate_quality_score(scores, weights)
    privacy_score = scores["privacy_score"]
    offline_resilience = scores["offline_availability_score"] / 5.0

    co2e_g = (cloud_billable_tokens / 1000) * carbon["carbon"]["grams_co2e_per_1000_cloud_tokens"]

    return {
        "architecture": "cloud_first",
        "meeting_minutes": minutes,
        "transcript_tokens": transcript_tokens,
        "cloud_llm_input_tokens": llm_input_total,
        "cloud_llm_output_tokens": llm_output_total,
        "cloud_embedding_tokens": embedding_tokens,
        "cloud_billable_tokens": cloud_billable_tokens,
        "transcription_cost_usd": round(transcription_cost, 6),
        "llm_cost_usd": round(llm_cost, 6),
        "embedding_cost_usd": round(embedding_cost, 6),
        "cloud_total_cost_usd": round(cloud_total_cost, 6),
        "local_compute_cost_usd": round(local_compute_cost, 6),
        "total_estimated_cost_usd": round(total_cost, 6),
        "tokens_saved_vs_cloud_first": 0,
        "token_reduction_pct_vs_cloud_first": 0.0,
        "quality_score": round(quality_score, 3),
        "privacy_score": privacy_score,
        "offline_resilience_score": round(offline_resilience, 3),
        "estimated_co2e_g": round(co2e_g, 4),
    }


def calculate_offline_first_meeting(minutes, assumptions):
    workload = assumptions["workload"]
    pricing = assumptions["pricing"]
    carbon = assumptions["carbon"]
    quality = assumptions["quality"]

    defaults = workload["defaults"]
    wpm = defaults["words_per_minute"]
    tpw = defaults["tokens_per_word"]
    transcript_tokens = calculate_transcript_tokens(minutes, wpm, tpw)

    local_watts = carbon["energy"]["local_inference_watts_midpoint"]
    local_hours = minutes / 60.0
    local_kwh = (local_watts / 1000) * local_hours
    local_compute_cost = local_kwh * pricing["electricity"]["local_price_per_kwh_usd"]

    scores = quality["modeled_scores"]["offline_first"]
    weights = quality["quality_weights"]
    quality_score = calculate_quality_score(scores, weights)
    privacy_score = scores["privacy_score"]
    offline_resilience = scores["offline_availability_score"] / 5.0

    cloud_first = calculate_cloud_first_meeting(minutes, assumptions)
    tokens_saved = cloud_first["cloud_billable_tokens"]

    return {
        "architecture": "offline_first",
        "meeting_minutes": minutes,
        "transcript_tokens": transcript_tokens,
        "cloud_llm_input_tokens": 0,
        "cloud_llm_output_tokens": 0,
        "cloud_embedding_tokens": 0,
        "cloud_billable_tokens": 0,
        "transcription_cost_usd": 0.0,
        "llm_cost_usd": 0.0,
        "embedding_cost_usd": 0.0,
        "cloud_total_cost_usd": 0.0,
        "local_compute_cost_usd": round(local_compute_cost, 6),
        "total_estimated_cost_usd": round(local_compute_cost, 6),
        "tokens_saved_vs_cloud_first": tokens_saved,
        "token_reduction_pct_vs_cloud_first": 100.0,
        "quality_score": round(quality_score, 3),
        "privacy_score": privacy_score,
        "offline_resilience_score": round(offline_resilience, 3),
        "estimated_co2e_g": 0.0,
    }


def calculate_hybrid_meeting(minutes, assumptions):
    workload = assumptions["workload"]
    pricing = assumptions["pricing"]
    routing = assumptions["routing"]
    carbon = assumptions["carbon"]
    quality = assumptions["quality"]

    defaults = workload["defaults"]
    profile = get_meeting_profile(minutes, workload)
    router = routing["hybrid_router"]

    wpm = defaults["words_per_minute"]
    tpw = defaults["tokens_per_word"]
    transcript_tokens = calculate_transcript_tokens(minutes, wpm, tpw)

    compact_ratio = router["compact_context_ratio"]
    rates = router["fallback_rates"]

    summary_input = transcript_tokens * compact_ratio * rates["summary"]
    summary_output = profile["summary_output_tokens"] * rates["summary"]

    action_input = transcript_tokens * compact_ratio * rates["action_items"]
    action_output = profile["action_output_tokens"] * rates["action_items"]

    qa_queries = defaults["qa_queries_per_meeting"]
    qa_input_full = qa_queries * defaults["qa_input_tokens_per_query"]
    qa_output_full = qa_queries * defaults["qa_output_tokens_per_query"]
    qa_input = qa_input_full * compact_ratio * rates["qa"]
    qa_output = qa_output_full * rates["qa"]

    memory_input = transcript_tokens * compact_ratio * rates["memory"]
    memory_output = profile["memory_output_tokens"] * rates["memory"]

    followup_drafts = defaults["followup_drafts_per_meeting"]
    followup_input_full = followup_drafts * defaults["followup_input_tokens_per_draft"]
    followup_output_full = followup_drafts * defaults["followup_output_tokens_per_draft"]
    followup_input = followup_input_full * compact_ratio * rates["followup"]
    followup_output = followup_output_full * rates["followup"]

    llm_input_total = int(summary_input + action_input + qa_input + memory_input + followup_input)
    llm_output_total = int(summary_output + action_output + qa_output + memory_output + followup_output)

    embedding_tokens = 0
    cloud_billable_tokens = llm_input_total + llm_output_total + embedding_tokens

    transcription_cost = 0.0
    llm_cost = (
        (llm_input_total / 1_000_000) * pricing["llm"]["input_per_1m_tokens_usd"]
        + (llm_output_total / 1_000_000) * pricing["llm"]["output_per_1m_tokens_usd"]
    )
    embedding_cost = 0.0
    cloud_total_cost = transcription_cost + llm_cost + embedding_cost

    local_watts = carbon["energy"]["local_inference_watts_midpoint"]
    local_hours = minutes / 60.0
    local_kwh = (local_watts / 1000) * local_hours
    local_compute_cost = local_kwh * pricing["electricity"]["local_price_per_kwh_usd"]
    total_cost = cloud_total_cost + local_compute_cost

    scores = quality["modeled_scores"]["hybrid_router"]
    weights = quality["quality_weights"]
    quality_score = calculate_quality_score(scores, weights)
    privacy_score = scores["privacy_score"]
    offline_resilience = scores["offline_availability_score"] / 5.0

    cloud_first = calculate_cloud_first_meeting(minutes, assumptions)
    tokens_saved = cloud_first["cloud_billable_tokens"] - cloud_billable_tokens
    token_reduction_pct = (tokens_saved / cloud_first["cloud_billable_tokens"] * 100) if cloud_first["cloud_billable_tokens"] > 0 else 0.0

    co2e_g = (cloud_billable_tokens / 1000) * carbon["carbon"]["grams_co2e_per_1000_cloud_tokens"]

    return {
        "architecture": "hybrid_router",
        "meeting_minutes": minutes,
        "transcript_tokens": transcript_tokens,
        "cloud_llm_input_tokens": llm_input_total,
        "cloud_llm_output_tokens": llm_output_total,
        "cloud_embedding_tokens": embedding_tokens,
        "cloud_billable_tokens": cloud_billable_tokens,
        "transcription_cost_usd": round(transcription_cost, 6),
        "llm_cost_usd": round(llm_cost, 6),
        "embedding_cost_usd": round(embedding_cost, 6),
        "cloud_total_cost_usd": round(cloud_total_cost, 6),
        "local_compute_cost_usd": round(local_compute_cost, 6),
        "total_estimated_cost_usd": round(total_cost, 6),
        "tokens_saved_vs_cloud_first": tokens_saved,
        "token_reduction_pct_vs_cloud_first": round(token_reduction_pct, 2),
        "quality_score": round(quality_score, 3),
        "privacy_score": privacy_score,
        "offline_resilience_score": round(offline_resilience, 3),
        "estimated_co2e_g": round(co2e_g, 4),
    }


def calculate_cost(input_tokens, output_tokens, embedding_tokens, minutes, pricing):
    transcription_cost = minutes * pricing["transcription"]["cloud_whisper_per_minute_usd"]
    llm_cost = (
        (input_tokens / 1_000_000) * pricing["llm"]["input_per_1m_tokens_usd"]
        + (output_tokens / 1_000_000) * pricing["llm"]["output_per_1m_tokens_usd"]
    )
    embedding_cost = (embedding_tokens / 1_000_000) * pricing["embedding"]["input_per_1m_tokens_usd"]
    return {
        "transcription_cost_usd": round(transcription_cost, 6),
        "llm_cost_usd": round(llm_cost, 6),
        "embedding_cost_usd": round(embedding_cost, 6),
        "total_cost_usd": round(transcription_cost + llm_cost + embedding_cost, 6),
    }


def calculate_quality_score(scores, weights):
    total = 0.0
    for dimension, weight in weights.items():
        total += scores.get(dimension, 0.0) * weight
    return total


def calculate_scenario(meeting_result, meetings_per_month):
    monthly_tokens = meeting_result["cloud_billable_tokens"] * meetings_per_month
    annual_tokens = monthly_tokens * 12
    monthly_cost = meeting_result["total_estimated_cost_usd"] * meetings_per_month
    annual_cost = monthly_cost * 12
    monthly_tokens_saved = meeting_result["tokens_saved_vs_cloud_first"] * meetings_per_month
    annual_tokens_saved = monthly_tokens_saved * 12
    monthly_cost_saved = meeting_result.get("cloud_first_cost", 0.0) * meetings_per_month - monthly_cost
    annual_cost_saved = monthly_cost_saved * 12

    return {
        "architecture": meeting_result["architecture"],
        "meetings_per_month": meetings_per_month,
        "monthly_cloud_tokens": monthly_tokens,
        "annual_cloud_tokens": annual_tokens,
        "monthly_cost_usd": round(monthly_cost, 4),
        "annual_cost_usd": round(annual_cost, 4),
        "monthly_tokens_saved_vs_cloud_first": monthly_tokens_saved,
        "annual_tokens_saved_vs_cloud_first": annual_tokens_saved,
        "monthly_cost_saved_vs_cloud_first": round(monthly_cost_saved, 4),
        "annual_cost_saved_vs_cloud_first": round(annual_cost_saved, 4),
        "quality_score": meeting_result["quality_score"],
        "privacy_score": meeting_result["privacy_score"],
        "offline_resilience_score": meeting_result["offline_resilience_score"],
    }


def render_meeting_table(results_by_arch, title):
    lines = []
    lines.append(f"### {title}\n")
    lines.append("| Metric | Cloud-First | Offline-First | Hybrid Router |")
    lines.append("|--------|------------:|-------------:|-------------:|")

    cf = results_by_arch["cloud_first"]
    of = results_by_arch["offline_first"]
    hr = results_by_arch["hybrid_router"]

    rows = [
        ("Meeting minutes", "meeting_minutes", "d"),
        ("Transcript tokens", "transcript_tokens", ",d"),
        ("Cloud LLM input tokens", "cloud_llm_input_tokens", ",d"),
        ("Cloud LLM output tokens", "cloud_llm_output_tokens", ",d"),
        ("Cloud embedding tokens", "cloud_embedding_tokens", ",d"),
        ("Cloud billable tokens", "cloud_billable_tokens", ",d"),
        ("Transcription cost", "transcription_cost_usd", "$"),
        ("LLM cost", "llm_cost_usd", "$"),
        ("Embedding cost", "embedding_cost_usd", "$"),
        ("Cloud total cost", "cloud_total_cost_usd", "$"),
        ("Local compute cost", "local_compute_cost_usd", "$"),
        ("Total estimated cost", "total_estimated_cost_usd", "$"),
        ("Tokens saved vs cloud-first", "tokens_saved_vs_cloud_first", ",d"),
        ("Token reduction %", "token_reduction_pct_vs_cloud_first", "%"),
        ("Quality score (1-5)", "quality_score", ".3f"),
        ("Privacy score (1-5)", "privacy_score", ".1f"),
        ("Offline resilience (0-1)", "offline_resilience_score", ".3f"),
        ("Estimated CO2e (g)", "estimated_co2e_g", ".4f"),
    ]

    for label, key, fmt in rows:
        vals = []
        for arch in [cf, of, hr]:
            v = arch[key]
            if fmt == "$":
                vals.append(f"${v:.4f}")
            elif fmt == "%":
                vals.append(f"{v:.1f}%")
            elif fmt == ",d":
                vals.append(f"{int(v):,}")
            elif fmt == "d":
                vals.append(f"{int(v)}")
            else:
                vals.append(f"{v:{fmt}}")
        lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} |")

    lines.append("")
    return "\n".join(lines)


def render_scenario_table(scenarios_by_arch, title):
    lines = []
    lines.append(f"### {title}\n")
    lines.append("| Metric | Cloud-First | Offline-First | Hybrid Router |")
    lines.append("|--------|------------:|-------------:|-------------:|")

    cf = scenarios_by_arch["cloud_first"]
    of = scenarios_by_arch["offline_first"]
    hr = scenarios_by_arch["hybrid_router"]

    rows = [
        ("Meetings/month", "meetings_per_month", "d"),
        ("Monthly cloud tokens", "monthly_cloud_tokens", ",d"),
        ("Annual cloud tokens", "annual_cloud_tokens", ",d"),
        ("Monthly cost", "monthly_cost_usd", "$"),
        ("Annual cost", "annual_cost_usd", "$"),
        ("Monthly tokens saved", "monthly_tokens_saved_vs_cloud_first", ",d"),
        ("Annual tokens saved", "annual_tokens_saved_vs_cloud_first", ",d"),
        ("Monthly cost saved", "monthly_cost_saved_vs_cloud_first", "$"),
        ("Annual cost saved", "annual_cost_saved_vs_cloud_first", "$"),
        ("Quality score (1-5)", "quality_score", ".3f"),
        ("Privacy score (1-5)", "privacy_score", ".1f"),
        ("Offline resilience (0-1)", "offline_resilience_score", ".3f"),
    ]

    for label, key, fmt in rows:
        vals = []
        for arch in [cf, of, hr]:
            v = arch[key]
            if fmt == "$":
                vals.append(f"${v:.4f}")
            elif fmt == ",d":
                vals.append(f"{int(v):,}")
            elif fmt == "d":
                vals.append(f"{int(v)}")
            else:
                vals.append(f"{v:{fmt}}")
        lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} |")

    lines.append("")
    return "\n".join(lines)


def render_markdown_tables(all_results):
    lines = []
    lines.append("# Generated Results: Offlyn Token Savings Audit\n")
    lines.append("> Auto-generated by `scripts/calculate_savings.py`.")
    lines.append("> All values derived from configurable assumptions in `assumptions/`.\n")
    lines.append("---\n")
    lines.append("## Per-Meeting Comparison\n")

    for duration_label, duration_min in [("30-Minute Meeting", 30), ("60-Minute Meeting", 60), ("90-Minute Meeting", 90)]:
        results = all_results["meetings"][duration_min]
        lines.append(render_meeting_table(results, duration_label))

    lines.append("---\n")
    lines.append("## Scenario Comparisons\n")

    for scenario_label, scenario_key in [
        ("Solo User (20 meetings/month)", "solo_user"),
        ("Small Team (100 meetings/month)", "small_team"),
        ("Enterprise Team (1,000 meetings/month)", "enterprise_team"),
    ]:
        scenarios = all_results["scenarios"][scenario_key]
        lines.append(render_scenario_table(scenarios, scenario_label))

    lines.append("---\n")
    lines.append("## Notes\n")
    lines.append("- All pricing assumptions are configurable in `assumptions/pricing.yml`.")
    lines.append("- Quality scores are modeled rubric defaults, not measured benchmarks.")
    lines.append("- Carbon estimates are directional. See `analysis/carbon_methodology.md`.")
    lines.append("- Hybrid router savings depend on fallback rates in `assumptions/routing.yml`.")
    lines.append("")

    return "\n".join(lines)


def main():
    assumptions = load_all_assumptions()

    all_results = {"meetings": {}, "scenarios": {}}

    for minutes in [30, 60, 90]:
        cf = calculate_cloud_first_meeting(minutes, assumptions)
        of = calculate_offline_first_meeting(minutes, assumptions)
        hr = calculate_hybrid_meeting(minutes, assumptions)

        of["cloud_first_cost"] = cf["total_estimated_cost_usd"]
        hr["cloud_first_cost"] = cf["total_estimated_cost_usd"]
        cf["cloud_first_cost"] = cf["total_estimated_cost_usd"]

        all_results["meetings"][minutes] = {
            "cloud_first": cf,
            "offline_first": of,
            "hybrid_router": hr,
        }

    scenarios_config = assumptions["workload"]["scenarios"]
    for scenario_key, scenario_cfg in scenarios_config.items():
        meetings_per_month = scenario_cfg["meetings_per_month"]
        avg_minutes = scenario_cfg["average_minutes"]

        meeting_results = all_results["meetings"][avg_minutes]

        scenario_results = {}
        for arch_key in ["cloud_first", "offline_first", "hybrid_router"]:
            meeting = meeting_results[arch_key]
            scenario_results[arch_key] = calculate_scenario(meeting, meetings_per_month)

        all_results["scenarios"][scenario_key] = scenario_results

    markdown = render_markdown_tables(all_results)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(markdown)

    print(f"Generated results written to: {OUTPUT_FILE}")
    print(f"\n--- 60-Minute Meeting Summary ---")
    m60 = all_results["meetings"][60]
    for arch in ["cloud_first", "offline_first", "hybrid_router"]:
        r = m60[arch]
        print(f"\n{arch}:")
        print(f"  Cloud billable tokens: {r['cloud_billable_tokens']:,}")
        print(f"  Cloud total cost: ${r['cloud_total_cost_usd']:.4f}")
        print(f"  Total cost: ${r['total_estimated_cost_usd']:.4f}")
        print(f"  Token reduction: {r['token_reduction_pct_vs_cloud_first']:.1f}%")

    return all_results


if __name__ == "__main__":
    main()
