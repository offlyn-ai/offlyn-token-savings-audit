"""Tests for the SCI-AI disclosure certification readiness validator."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from validate_sci_ai_disclosure import run_checklist, calculate_score

REPO_ROOT = Path(__file__).resolve().parent.parent


class TestValidatorChecklist:
    def test_checklist_has_25_items(self):
        items = run_checklist()
        assert len(items) == 25

    def test_all_items_have_required_fields(self):
        items = run_checklist()
        for item in items:
            assert "id" in item
            assert "description" in item
            assert "passed" in item
            assert "remediation" in item

    def test_score_reaches_at_least_99(self):
        items = run_checklist()
        result = calculate_score(items)
        assert result["score"] >= 99, (
            f"Score {result['score']}/100. Failed: "
            + ", ".join(i["id"] for i in result["items"] if not i["passed"])
        )

    def test_max_score_is_100(self):
        items = run_checklist()
        result = calculate_score(items)
        assert result["max"] == 100

    def test_points_per_item_is_4(self):
        items = run_checklist()
        result = calculate_score(items)
        assert result["max"] == len(items) * 4


class TestStrictMode:
    def test_strict_exits_nonzero_below_threshold(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_sci_ai_disclosure.py", "--strict",
             "--output", "/tmp/test_validator_output.json"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        score_file = Path("/tmp/test_validator_output.json")
        if score_file.exists():
            data = json.loads(score_file.read_text())
            if data["score"] >= 99:
                assert result.returncode == 0
            else:
                assert result.returncode == 1


class TestAttestationSignatory:
    def test_attestation_contains_joel_nishant_reddy(self):
        attestation = (REPO_ROOT / "certification" / "sci_ai_attestation.md").read_text()
        assert "Joel Nishant Reddy" in attestation

    def test_attestation_contains_cofounder_title(self):
        attestation = (REPO_ROOT / "certification" / "sci_ai_attestation.md").read_text()
        assert "Co-founder, Offlyn.ai" in attestation


class TestSubmissionFiles:
    def test_data_sources_exists(self):
        assert (REPO_ROOT / "certification" / "data_sources.md").exists()

    def test_submission_metadata_exists(self):
        assert (REPO_ROOT / "certification" / "submission_metadata.yml").exists()

    def test_gsf_submission_checklist_exists(self):
        assert (REPO_ROOT / "certification" / "gsf_submission_checklist.md").exists()

    def test_release_notes_exist(self):
        assert (REPO_ROOT / "certification" / "release_notes_v0.1.md").exists()

    def test_submission_metadata_has_signatory(self):
        import yaml
        with open(REPO_ROOT / "certification" / "submission_metadata.yml") as f:
            meta = yaml.safe_load(f)
        assert meta["submission"]["signatory_name"] == "Joel Nishant Reddy"
        assert meta["submission"]["certification_claim_status"] == "not_certified"


class TestGsfSubmissionEmail:
    def test_gsf_submission_email_exists(self):
        assert (REPO_ROOT / "certification" / "gsf_submission_email_draft.md").exists()

    def test_submission_email_contains_gsf_address(self):
        content = (REPO_ROOT / "certification" / "gsf_submission_email_draft.md").read_text()
        assert "sci-certification@greensoftware.foundation" in content

    def test_submission_email_water_excluded(self):
        content = (REPO_ROOT / "certification" / "gsf_submission_email_draft.md").read_text()
        assert "excluded from the SCI score" in content


class TestReviewerAids:
    def test_disclosure_has_reviewer_quick_summary(self):
        content = (REPO_ROOT / "certification" / "sci_ai_disclosure.md").read_text()
        assert "Reviewer quick summary" in content

    def test_certification_readme_has_reviewer_navigation(self):
        content = (REPO_ROOT / "certification" / "README.md").read_text()
        assert "Reviewer Navigation" in content

    def test_certification_readme_has_reproduce_commands(self):
        content = (REPO_ROOT / "certification" / "README.md").read_text()
        assert "pytest tests/" in content
