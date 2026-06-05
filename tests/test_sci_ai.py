"""Tests for SCI-AI calculator: incremental energy, Consumer SCI, water, claims policy."""

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from calculate_sci_ai import (
    calculate_incremental_local_energy,
    calculate_cloud_token_carbon,
    calculate_net_avoided_cloud_carbon,
    calculate_net_avoided_total_carbon,
    calculate_cloud_direct_water,
    calculate_consumer_sci,
    calculate_sci_ai_meeting,
    load_sci_ai_assumptions,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def get_assumptions():
    return load_sci_ai_assumptions()


def test_incremental_local_energy_uses_incremental_watts():
    """Local carbon must use incremental watts (5W), not total device watts (25W)."""
    kwh = calculate_incremental_local_energy(5.0, 1.0)
    assert abs(kwh - 0.005) < 0.0001
    kwh_total = calculate_incremental_local_energy(25.0, 1.0)
    assert kwh_total == 0.025
    assert kwh < kwh_total


def test_consumer_sci_zero_denominator_raises():
    """Consumer SCI with zero functional units must raise ValueError."""
    with pytest.raises(ValueError, match="positive"):
        calculate_consumer_sci(10.0, 0)
    with pytest.raises(ValueError, match="positive"):
        calculate_consumer_sci(10.0, -1)


def test_consumer_sci_per_meeting_hour():
    assumptions = get_assumptions()
    results = calculate_sci_ai_meeting(60, assumptions)
    for arch in ["cloud_first", "offline_first", "hybrid_router"]:
        assert "gco2e_per_meeting_hour" in results[arch]
        val = results[arch]["gco2e_per_meeting_hour"]
        assert isinstance(val, float)
        assert val >= 0


def test_consumer_sci_per_second_audio():
    assumptions = get_assumptions()
    results = calculate_sci_ai_meeting(60, assumptions)
    for arch in ["cloud_first", "offline_first", "hybrid_router"]:
        assert "gco2e_per_second_audio" in results[arch]
        val = results[arch]["gco2e_per_second_audio"]
        assert isinstance(val, float)
        assert val >= 0


def test_consumer_sci_per_workflow_execution():
    assumptions = get_assumptions()
    results = calculate_sci_ai_meeting(60, assumptions)
    for arch in ["cloud_first", "offline_first", "hybrid_router"]:
        assert "gco2e_per_workflow_execution" in results[arch]
        val = results[arch]["gco2e_per_workflow_execution"]
        assert isinstance(val, float)
        assert val >= 0


def test_local_direct_cooling_water_zero():
    """Offline-first has zero direct datacenter cooling water."""
    assumptions = get_assumptions()
    results = calculate_sci_ai_meeting(60, assumptions)
    assert results["offline_first"]["direct_datacenter_water_liters"] == 0.0


def test_hybrid_water_less_than_cloud_first():
    assumptions = get_assumptions()
    results = calculate_sci_ai_meeting(60, assumptions)
    assert results["hybrid_router"]["direct_datacenter_water_liters"] < results["cloud_first"]["direct_datacenter_water_liters"]


def test_water_is_supplemental_not_sci_carbon():
    """Water assumptions must be labeled as supplemental, not part of SCI carbon."""
    assumptions = get_assumptions()
    assert assumptions["water"]["water_metric_type"] == "supplemental_not_sci_carbon"


def test_provider_sci_not_used_by_default():
    """Provider SCI should not be the default boundary."""
    assumptions = get_assumptions()
    assert assumptions["sci_ai"]["default_boundary"] == "consumer"
    assert assumptions["sci_ai"]["claim_level"] == "aligned_not_certified"


def test_claims_policy_file_contains_disallowed():
    """Claims policy must exist and contain key disallowed claims."""
    claims_file = REPO_ROOT / "analysis" / "claims_policy.md"
    assert claims_file.exists(), "claims_policy.md must exist"
    content = claims_file.read_text()
    disallowed = [
        "ISO certified",
        "SCI certified",
        "SCI-AI certified",
        "Carbon neutral",
        "Zero carbon AI",
        "Water-free AI",
        "Verified emissions reduction",
        "Carbon credit",
        "Offset",
    ]
    for claim in disallowed:
        assert claim.lower() in content.lower(), f"Missing disallowed claim: {claim}"


def test_negative_tokens_rejected():
    """Negative token counts must raise ValueError."""
    with pytest.raises(ValueError):
        calculate_cloud_token_carbon(-1000, 0.5)


def test_negative_energy_rejected():
    """Negative energy values must raise ValueError."""
    with pytest.raises(ValueError):
        calculate_incremental_local_energy(-5, 1.0)
    with pytest.raises(ValueError):
        calculate_incremental_local_energy(5, -1.0)


def test_existing_tests_still_pass():
    """Meta-check: original calculator functions are still importable and functional."""
    from calculate_savings import (
        calculate_transcript_tokens,
        calculate_cloud_first_meeting,
        calculate_offline_first_meeting,
        calculate_hybrid_meeting,
        load_all_assumptions,
    )
    assumptions = load_all_assumptions()
    tokens = calculate_transcript_tokens(60, 150, 1.3)
    assert tokens == 11700
    cf = calculate_cloud_first_meeting(60, assumptions)
    assert cf["cloud_billable_tokens"] == 64450
