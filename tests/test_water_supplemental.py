"""Tests verifying water is supplemental and not included in SCI score."""

import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from calculate_sci_ai import (
    load_sci_ai_assumptions,
    calculate_sci_ai_meeting,
    calculate_cloud_direct_water,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


class TestWaterSupplemental:
    def setup_method(self):
        self.assumptions = load_sci_ai_assumptions()
        self.results = calculate_sci_ai_meeting(60, self.assumptions)

    def test_water_not_included_in_sci_score(self):
        """Water must be supplemental - verify assumptions explicitly state this."""
        water_config = self.assumptions["water"]
        assert water_config.get("water_metric_type") == "supplemental_not_sci_carbon"

    def test_assumptions_register_water_excluded(self):
        """The consolidated assumptions register must state water is not in SCI."""
        register_path = REPO_ROOT / "certification" / "assumptions_register.yml"
        with open(register_path, "r") as f:
            register = yaml.safe_load(f)
        assert register["water"]["included_in_sci_score"] is False

    def test_local_first_direct_water_equals_zero(self):
        """Local-first should have zero direct datacenter cooling water."""
        assert self.results["offline_first"]["direct_datacenter_water_liters"] == 0.0

    def test_hybrid_water_less_than_cloud_first(self):
        """Hybrid should use less datacenter water than cloud-first."""
        cloud_water = self.results["cloud_first"]["direct_datacenter_water_liters"]
        hybrid_water = self.results["hybrid_router"]["direct_datacenter_water_liters"]
        assert hybrid_water < cloud_water

    def test_cloud_first_water_positive(self):
        """Cloud-first should have positive water use."""
        assert self.results["cloud_first"]["direct_datacenter_water_liters"] > 0

    def test_water_calculation_pure_function(self):
        """Direct water calculation should work with known inputs."""
        water = calculate_cloud_direct_water(0.1, 1.90)
        assert water == pytest.approx(0.19)

    def test_zero_energy_zero_water(self):
        """Zero cloud energy should produce zero water."""
        water = calculate_cloud_direct_water(0.0, 1.90)
        assert water == 0.0
