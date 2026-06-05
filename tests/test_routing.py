"""Tests for hybrid routing logic."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from calculate_savings import (
    calculate_cloud_first_meeting,
    calculate_hybrid_meeting,
    load_all_assumptions,
)


def get_assumptions():
    return load_all_assumptions()


def test_hybrid_no_transcription_cost():
    assumptions = get_assumptions()
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["transcription_cost_usd"] == 0.0


def test_hybrid_no_embedding_tokens():
    assumptions = get_assumptions()
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["cloud_embedding_tokens"] == 0


def test_hybrid_token_reduction_positive():
    assumptions = get_assumptions()
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["token_reduction_pct_vs_cloud_first"] > 0


def test_hybrid_token_reduction_less_than_100():
    assumptions = get_assumptions()
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["token_reduction_pct_vs_cloud_first"] < 100


def test_hybrid_compact_context_reduces_input():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["cloud_llm_input_tokens"] < cf["cloud_llm_input_tokens"]


def test_hybrid_all_durations():
    assumptions = get_assumptions()
    for minutes in [30, 60, 90]:
        cf = calculate_cloud_first_meeting(minutes, assumptions)
        hr = calculate_hybrid_meeting(minutes, assumptions)
        assert hr["cloud_billable_tokens"] < cf["cloud_billable_tokens"]
        assert hr["cloud_total_cost_usd"] < cf["cloud_total_cost_usd"]


def test_zero_fallback_means_zero_cloud():
    """If all fallback rates are 0, hybrid should have zero cloud tokens."""
    assumptions = get_assumptions()
    routing = assumptions["routing"]["hybrid_router"]
    for key in routing["fallback_rates"]:
        routing["fallback_rates"][key] = 0.0

    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["cloud_llm_input_tokens"] == 0
    assert hr["cloud_llm_output_tokens"] == 0


def test_full_fallback_approaches_cloud_first():
    """If all fallback rates are 1.0 with compact ratio, hybrid input < cloud-first."""
    assumptions = get_assumptions()
    routing = assumptions["routing"]["hybrid_router"]
    for key in routing["fallback_rates"]:
        routing["fallback_rates"][key] = 1.0
    routing["compact_context_ratio"] = 0.20

    cf = calculate_cloud_first_meeting(60, assumptions)
    hr = calculate_hybrid_meeting(60, assumptions)
    assert hr["cloud_llm_input_tokens"] < cf["cloud_llm_input_tokens"]
    assert hr["cloud_llm_output_tokens"] == cf["cloud_llm_output_tokens"]
