"""Tests for the claims policy enforcement."""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_POLICY = REPO_ROOT / "analysis" / "claims_policy.md"
ASSUMPTIONS_REGISTER = REPO_ROOT / "certification" / "assumptions_register.yml"


class TestClaimsPolicy:
    def setup_method(self):
        self.policy_content = CLAIMS_POLICY.read_text(encoding="utf-8")

    def test_disallows_iso_certified(self):
        assert "ISO certified" in self.policy_content
        # Verify it's in the disallowed section
        disallowed_idx = self.policy_content.find("Disallowed")
        iso_idx = self.policy_content.find("ISO certified")
        assert iso_idx > disallowed_idx

    def test_disallows_carbon_neutral(self):
        assert "Carbon neutral" in self.policy_content
        disallowed_idx = self.policy_content.find("Disallowed")
        cn_idx = self.policy_content.find("Carbon neutral")
        assert cn_idx > disallowed_idx

    def test_disallows_sci_for_ai_certified(self):
        assert "SCI for AI certified" in self.policy_content
        disallowed_idx = self.policy_content.find("Disallowed")
        sci_idx = self.policy_content.find("SCI for AI certified")
        assert sci_idx > disallowed_idx

    def test_allows_sci_for_ai_aligned(self):
        assert "SCI for AI-aligned" in self.policy_content
        allowed_idx = self.policy_content.find("Allowed")
        aligned_idx = self.policy_content.find("SCI for AI-aligned")
        assert aligned_idx > allowed_idx

    def test_allows_certification_readiness(self):
        assert "Certification-readiness package" in self.policy_content

    def test_disallows_guaranteed_scope_3(self):
        assert "Guaranteed Scope 3 reduction" in self.policy_content


class TestAssumptionsRegisterClaims:
    def setup_method(self):
        import yaml
        with open(ASSUMPTIONS_REGISTER, "r") as f:
            self.register = yaml.safe_load(f)

    def test_certification_status_not_certified(self):
        assert self.register["claims"]["certification_status"] == "not_certified"

    def test_allowed_terms_present(self):
        allowed = self.register["claims"]["allowed_terms"]
        assert "SCI for AI-aligned" in allowed
        assert "modeled estimate" in allowed
        assert "self-attested disclosure" in allowed

    def test_disallowed_terms_present(self):
        disallowed = self.register["claims"]["disallowed_terms"]
        assert "ISO certified" in disallowed
        assert "carbon neutral" in disallowed
        assert "SCI for AI certified" in disallowed
        assert "Green Software Foundation certified" in disallowed
