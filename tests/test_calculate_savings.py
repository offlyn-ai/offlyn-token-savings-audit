"""Tests for the token savings calculator."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from calculate_savings import (
    calculate_transcript_tokens,
    calculate_cloud_first_meeting,
    calculate_offline_first_meeting,
    calculate_hybrid_meeting,
    calculate_quality_score,
    calculate_scenario,
    load_all_assumptions,
    render_markdown_tables,
    OUTPUT_FILE,
)


def get_assumptions():
    return load_all_assumptions()


def test_transcript_tokens_60min():
    tokens = calculate_transcript_tokens(60, 150, 1.3)
    assert tokens == 11700


def test_transcript_tokens_30min():
    tokens = calculate_transcript_tokens(30, 150, 1.3)
    assert tokens == 5850


def test_transcript_tokens_90min():
    tokens = calculate_transcript_tokens(90, 150, 1.3)
    assert tokens == 17550


def test_offline_first_cloud_tokens_zero():
    assumptions = get_assumptions()
    result = calculate_offline_first_meeting(60, assumptions)
    assert result["cloud_llm_input_tokens"] == 0
    assert result["cloud_llm_output_tokens"] == 0
    assert result["cloud_embedding_tokens"] == 0
    assert result["cloud_billable_tokens"] == 0


def test_offline_first_cloud_cost_zero():
    assumptions = get_assumptions()
    result = calculate_offline_first_meeting(60, assumptions)
    assert result["cloud_total_cost_usd"] == 0.0
    assert result["transcription_cost_usd"] == 0.0


def test_hybrid_less_than_cloud_first():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["cloud_billable_tokens"] < cf["cloud_billable_tokens"]


def test_hybrid_gte_offline_first():
    assumptions = get_assumptions()
    of = calculate_offline_first_meeting(60, assumptions)
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["cloud_billable_tokens"] >= of["cloud_billable_tokens"]


def test_cloud_first_cost_greater_than_offline():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    of = calculate_offline_first_meeting(60, assumptions)
    assert cf["cloud_total_cost_usd"] > of["cloud_total_cost_usd"]


def test_quality_score_range():
    assumptions = get_assumptions()
    weights = assumptions["quality"]["quality_weights"]
    for arch_key in ["cloud_first", "offline_first", "hybrid_router"]:
        scores = assumptions["quality"]["modeled_scores"][arch_key]
        qs = calculate_quality_score(scores, weights)
        assert 1.0 <= qs <= 5.0, f"{arch_key} quality score {qs} out of range"


def test_generated_results_file_created():
    assumptions = get_assumptions()
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
    assert len(markdown) > 100
    assert "Cloud-First" in markdown
    assert "Offline-First" in markdown
    assert "Hybrid Router" in markdown


def test_cloud_first_60min_values():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    assert cf["transcript_tokens"] == 11700
    assert cf["cloud_llm_input_tokens"] == 47100
    assert cf["cloud_llm_output_tokens"] == 5650
    assert cf["cloud_embedding_tokens"] == 11700
    assert cf["cloud_billable_tokens"] == 64450
