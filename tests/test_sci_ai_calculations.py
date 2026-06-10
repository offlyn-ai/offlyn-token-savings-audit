"""Tests for SCI-AI pure calculation functions."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from calculate_sci_ai import (
    calculate_cloud_token_carbon,
    calculate_incremental_local_energy,
    calculate_local_carbon_g,
    calculate_operational_sci_g_per_unit,
    calculate_token_reduction_pct,
    validate_non_negative,
    validate_positive_denominator,
)


class TestCloudTokenCarbon:
    def test_basic_calculation(self):
        result = calculate_cloud_token_carbon(10000, 0.5)
        assert result == pytest.approx(5.0)

    def test_zero_tokens(self):
        result = calculate_cloud_token_carbon(0, 0.5)
        assert result == 0.0

    def test_high_intensity(self):
        result = calculate_cloud_token_carbon(1000, 3.0)
        assert result == pytest.approx(3.0)


class TestIncrementalLocalEnergy:
    def test_basic_calculation(self):
        result = calculate_incremental_local_energy(5.0, 1.0)
        assert result == pytest.approx(0.005)

    def test_half_hour(self):
        result = calculate_incremental_local_energy(5.0, 0.5)
        assert result == pytest.approx(0.0025)

    def test_zero_watts(self):
        result = calculate_incremental_local_energy(0.0, 1.0)
        assert result == 0.0


class TestLocalCarbonG:
    def test_basic_calculation(self):
        result = calculate_local_carbon_g(0.005, 350.0)
        assert result == pytest.approx(1.75)

    def test_zero_energy(self):
        result = calculate_local_carbon_g(0.0, 350.0)
        assert result == 0.0

    def test_negative_kwh_raises(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_local_carbon_g(-1.0, 350.0)

    def test_negative_intensity_raises(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_local_carbon_g(0.005, -100.0)


class TestOperationalSci:
    def test_basic_calculation(self):
        result = calculate_operational_sci_g_per_unit(32.0, 1.0)
        assert result == pytest.approx(32.0)

    def test_multiple_units(self):
        result = calculate_operational_sci_g_per_unit(32.0, 3600.0)
        assert result == pytest.approx(32.0 / 3600.0)

    def test_zero_denominator_raises(self):
        with pytest.raises(ValueError, match="must be positive"):
            calculate_operational_sci_g_per_unit(32.0, 0.0)

    def test_negative_denominator_raises(self):
        with pytest.raises(ValueError, match="must be positive"):
            calculate_operational_sci_g_per_unit(32.0, -1.0)


class TestTokenReductionPct:
    def test_full_reduction(self):
        result = calculate_token_reduction_pct(64450, 0)
        assert result == pytest.approx(100.0)

    def test_partial_reduction(self):
        result = calculate_token_reduction_pct(64450, 1354)
        assert result == pytest.approx(97.9, abs=0.1)

    def test_no_reduction(self):
        result = calculate_token_reduction_pct(64450, 64450)
        assert result == pytest.approx(0.0)

    def test_zero_baseline(self):
        result = calculate_token_reduction_pct(0, 0)
        assert result == 0.0

    def test_negative_tokens_raises(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_token_reduction_pct(-100, 50)


class TestValidationHelpers:
    def test_validate_non_negative_passes(self):
        validate_non_negative(0.0, "test")
        validate_non_negative(100.0, "test")

    def test_validate_non_negative_raises(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            validate_non_negative(-0.001, "test_value")

    def test_validate_positive_denominator_passes(self):
        validate_positive_denominator(1.0, "test")
        validate_positive_denominator(0.001, "test")

    def test_validate_positive_denominator_raises_zero(self):
        with pytest.raises(ValueError, match="must be positive"):
            validate_positive_denominator(0.0, "test_value")

    def test_validate_positive_denominator_raises_negative(self):
        with pytest.raises(ValueError, match="must be positive"):
            validate_positive_denominator(-1.0, "test_value")
