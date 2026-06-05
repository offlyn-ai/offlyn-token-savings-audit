"""Tests for the cost model calculations."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from calculate_savings import (
    calculate_cost,
    calculate_cloud_first_meeting,
    calculate_offline_first_meeting,
    calculate_hybrid_meeting,
    calculate_quality_score,
    load_all_assumptions,
)


def get_assumptions():
    return load_all_assumptions()


def test_calculate_cost_basic():
    assumptions = get_assumptions()
    pricing = assumptions["pricing"]
    result = calculate_cost(1_000_000, 1_000_000, 1_000_000, 60, pricing)
    expected_transcription = 60 * 0.006
    expected_llm = 2.50 + 10.00
    expected_embedding = 0.02
    assert abs(result["transcription_cost_usd"] - expected_transcription) < 0.001
    assert abs(result["llm_cost_usd"] - expected_llm) < 0.001
    assert abs(result["embedding_cost_usd"] - expected_embedding) < 0.001


def test_calculate_cost_zero_tokens():
    assumptions = get_assumptions()
    pricing = assumptions["pricing"]
    result = calculate_cost(0, 0, 0, 0, pricing)
    assert result["transcription_cost_usd"] == 0.0
    assert result["llm_cost_usd"] == 0.0
    assert result["embedding_cost_usd"] == 0.0
    assert result["total_cost_usd"] == 0.0


def test_cloud_first_transcription_cost_60min():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    expected = 60 * 0.006
    assert abs(cf["transcription_cost_usd"] - expected) < 0.0001


def test_offline_local_compute_cost():
    assumptions = get_assumptions()
    of = calculate_offline_first_meeting(60, assumptions)
    expected_kwh = (25 / 1000) * 1.0
    expected_cost = expected_kwh * 0.30
    assert abs(of["local_compute_cost_usd"] - expected_cost) < 0.0001


def test_cost_ordering():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    of = calculate_offline_first_meeting(60, assumptions)
    hr = calculate_hybrid_meeting(60, assumptions)
    assert cf["total_estimated_cost_usd"] > hr["total_estimated_cost_usd"]
    assert cf["total_estimated_cost_usd"] > of["total_estimated_cost_usd"]


def test_quality_score_weighted_calculation():
    weights = {
        "factual_grounding": 0.20,
        "summary_completeness": 0.15,
        "action_item_correctness": 0.15,
        "decision_capture": 0.10,
        "answer_helpfulness": 0.10,
        "citation_quality": 0.10,
        "low_hallucination_risk": 0.10,
        "latency_score": 0.05,
        "offline_availability_score": 0.05,
    }
    scores = {k: 4.0 for k in weights}
    result = calculate_quality_score(scores, weights)
    assert abs(result - 4.0) < 0.001


def test_quality_score_weights_sum_to_one():
    assumptions = get_assumptions()
    weights = assumptions["quality"]["quality_weights"]
    total = sum(weights.values())
    assert abs(total - 1.0) < 0.001


def test_cloud_first_total_cost_components():
    assumptions = get_assumptions()
    cf = calculate_cloud_first_meeting(60, assumptions)
    computed_total = cf["transcription_cost_usd"] + cf["llm_cost_usd"] + cf["embedding_cost_usd"]
    assert abs(cf["cloud_total_cost_usd"] - computed_total) < 0.0001
