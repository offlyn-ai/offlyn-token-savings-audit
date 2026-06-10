#!/usr/bin/env python3
"""
SCI for AI Disclosure Certification Readiness Validator

Inspects the repository for completeness against a 25-item checklist.
Each item is worth 4 points, for a maximum score of 100.

Usage:
    python scripts/validate_sci_ai_disclosure.py
    python scripts/validate_sci_ai_disclosure.py --strict
"""

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CERT_DIR = REPO_ROOT / "certification"
ANALYSIS_DIR = REPO_ROOT / "analysis"
ASSUMPTIONS_DIR = REPO_ROOT / "assumptions"
SCRIPTS_DIR = REPO_ROOT / "scripts"
TESTS_DIR = REPO_ROOT / "tests"


def file_contains(path: Path, keyword: str) -> bool:
    if not path.exists():
        return False
    content = path.read_text(encoding="utf-8").lower()
    return keyword.lower() in content


def file_exists(path: Path) -> bool:
    return path.exists() and path.stat().st_size > 0


def run_checklist() -> list:
    items = []

    # 1. Software system described
    items.append({
        "id": "software_system_described",
        "description": "Software system described",
        "passed": file_contains(CERT_DIR / "sci_ai_disclosure.md", "software system"),
        "remediation": "Add a 'Software System' section to certification/sci_ai_disclosure.md"
    })

    # 2. Disclosure version present
    items.append({
        "id": "disclosure_version_present",
        "description": "Disclosure version present",
        "passed": file_contains(CERT_DIR / "assumptions_register.yml", "version"),
        "remediation": "Add 'version' field to certification/assumptions_register.yml"
    })

    # 3. Boundary clearly defined
    items.append({
        "id": "boundary_defined",
        "description": "Boundary clearly defined",
        "passed": file_exists(CERT_DIR / "sci_ai_boundary.md") and
                  file_contains(CERT_DIR / "sci_ai_boundary.md", "consumer sci"),
        "remediation": "Create certification/sci_ai_boundary.md with Consumer SCI boundary definition"
    })

    # 4. Functional unit clearly defined
    items.append({
        "id": "functional_unit_defined",
        "description": "Functional unit clearly defined",
        "passed": file_exists(CERT_DIR / "sci_ai_functional_unit.md") and
                  file_contains(CERT_DIR / "sci_ai_functional_unit.md", "60-minute"),
        "remediation": "Create certification/sci_ai_functional_unit.md with primary functional unit"
    })

    # 5. SCI formula included
    items.append({
        "id": "sci_formula_included",
        "description": "SCI formula included",
        "passed": file_contains(CERT_DIR / "sci_ai_calculation.md", "sci") and
                  file_contains(CERT_DIR / "sci_ai_calculation.md", "o + m"),
        "remediation": "Add SCI = (O + M) / R formula to certification/sci_ai_calculation.md"
    })

    # 6. Operational emissions included
    items.append({
        "id": "operational_emissions_included",
        "description": "Operational emissions included",
        "passed": file_contains(CERT_DIR / "sci_ai_calculation.md", "operational"),
        "remediation": "Document operational emissions in certification/sci_ai_calculation.md"
    })

    # 7. Embodied emissions explicitly excluded with rationale
    items.append({
        "id": "embodied_emissions_addressed",
        "description": "Embodied emissions included or explicitly excluded with rationale",
        "passed": file_contains(CERT_DIR / "sci_ai_calculation.md", "embodied") and
                  file_contains(CERT_DIR / "sci_ai_calculation.md", "excluded"),
        "remediation": "Add embodied emissions exclusion rationale to certification/sci_ai_calculation.md"
    })

    # 8. Energy assumptions documented
    items.append({
        "id": "energy_assumptions_documented",
        "description": "Energy assumptions documented",
        "passed": file_contains(CERT_DIR / "assumptions_register.yml", "local_incremental_power_watts"),
        "remediation": "Add local_energy section to certification/assumptions_register.yml"
    })

    # 9. Carbon intensity assumptions documented
    items.append({
        "id": "carbon_intensity_documented",
        "description": "Carbon intensity assumptions documented",
        "passed": file_contains(CERT_DIR / "assumptions_register.yml", "cloud_token_co2e_g_per_1k"),
        "remediation": "Add carbon section to certification/assumptions_register.yml"
    })

    # 10. Water disclosed as supplemental
    items.append({
        "id": "water_supplemental",
        "description": "Water disclosed as supplemental and excluded from SCI score",
        "passed": file_contains(CERT_DIR / "assumptions_register.yml", "supplemental") and
                  file_contains(CERT_DIR / "sci_ai_disclosure.md", "supplemental"),
        "remediation": "Ensure water is marked supplemental in assumptions_register.yml and disclosure"
    })

    # 11. Avoided emissions separated from SCI score
    items.append({
        "id": "avoided_emissions_separated",
        "description": "Avoided emissions separated from SCI score",
        "passed": file_contains(CERT_DIR / "sci_ai_calculation.md", "avoided") and
                  file_contains(CERT_DIR / "sci_ai_calculation.md", "not part of the sci"),
        "remediation": "Document that avoided emissions are separate from SCI score in calculation.md"
    })

    # 12. Scenarios documented
    items.append({
        "id": "scenarios_documented",
        "description": "Cloud-first/local-first/hybrid scenarios documented",
        "passed": file_contains(CERT_DIR / "sci_ai_disclosure.md", "cloud-first") and
                  file_contains(CERT_DIR / "sci_ai_disclosure.md", "local-first") and
                  file_contains(CERT_DIR / "sci_ai_disclosure.md", "hybrid"),
        "remediation": "Document all three scenarios in certification/sci_ai_disclosure.md"
    })

    # 13. Token calculations reproducible
    items.append({
        "id": "token_calculations_reproducible",
        "description": "Token calculations reproducible",
        "passed": file_exists(SCRIPTS_DIR / "calculate_savings.py") and
                  file_exists(SCRIPTS_DIR / "calculate_sci_ai.py"),
        "remediation": "Ensure scripts/calculate_savings.py and scripts/calculate_sci_ai.py exist"
    })

    # 14. Carbon calculations reproducible
    items.append({
        "id": "carbon_calculations_reproducible",
        "description": "Carbon calculations reproducible",
        "passed": file_contains(SCRIPTS_DIR / "calculate_sci_ai.py", "calculate_cloud_token_carbon") or
                  file_contains(SCRIPTS_DIR / "calculate_sci_ai.py", "cloud_carbon"),
        "remediation": "Ensure carbon calculation functions exist in scripts/calculate_sci_ai.py"
    })

    # 15. Water calculations reproducible
    items.append({
        "id": "water_calculations_reproducible",
        "description": "Water calculations reproducible",
        "passed": file_contains(SCRIPTS_DIR / "calculate_sci_ai.py", "calculate_cloud_direct_water"),
        "remediation": "Ensure water calculation function exists in scripts/calculate_sci_ai.py"
    })

    # 16. Quality methodology disclosed
    items.append({
        "id": "quality_methodology_disclosed",
        "description": "Quality methodology disclosed",
        "passed": file_exists(ANALYSIS_DIR / "quality_methodology.md") or
                  file_exists(REPO_ROOT / "benchmarks" / "quality_methodology.md"),
        "remediation": "Create analysis/quality_methodology.md with quality dimensions"
    })

    # 17. Quality scores marked modeled or measured
    items.append({
        "id": "quality_scores_labeled",
        "description": "Quality scores marked modeled or measured",
        "passed": file_contains(CERT_DIR / "assumptions_register.yml", "quality_scores_are_modeled_defaults"),
        "remediation": "Add quality_scores_are_modeled_defaults to assumptions_register.yml"
    })

    # 18. Claims policy exists
    items.append({
        "id": "claims_policy_exists",
        "description": "Claims policy exists",
        "passed": file_exists(ANALYSIS_DIR / "claims_policy.md"),
        "remediation": "Create analysis/claims_policy.md"
    })

    # 19. Disallowed claims absent from public claims
    # Terms appearing in "Disallowed" or "Do not use" sections are acceptable (they document what NOT to say)
    disallowed_in_readme = False
    if file_exists(REPO_ROOT / "README.md"):
        readme_content = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        readme_lower = readme_content.lower()
        disallowed_terms = ["iso certified", "sci certified", "carbon neutral", "zero carbon ai", "water-free ai"]
        for term in disallowed_terms:
            positions = []
            start = 0
            while True:
                idx = readme_lower.find(term, start)
                if idx == -1:
                    break
                positions.append(idx)
                start = idx + 1
            for pos in positions:
                context_start = max(0, pos - 200)
                context = readme_lower[context_start:pos]
                if "disallowed" not in context and "do not use" not in context and "not a" not in context:
                    disallowed_in_readme = True
                    break
            if disallowed_in_readme:
                break
    items.append({
        "id": "disallowed_claims_absent",
        "description": "Disallowed claims absent from public claims",
        "passed": not disallowed_in_readme,
        "remediation": "Remove disallowed claims from README.md"
    })

    # 20. Attestation file exists with signatory + submission email draft
    attestation_ok = (
        file_exists(CERT_DIR / "sci_ai_attestation.md") and
        file_contains(CERT_DIR / "sci_ai_attestation.md", "joel nishant reddy") and
        file_contains(CERT_DIR / "sci_ai_attestation.md", "co-founder, offlyn.ai") and
        file_exists(CERT_DIR / "gsf_submission_email_draft.md")
    )
    items.append({
        "id": "attestation_exists",
        "description": "Attestation file exists with signatory",
        "passed": attestation_ok,
        "remediation": "Create certification/sci_ai_attestation.md with Joel Nishant Reddy and gsf_submission_email_draft.md"
    })

    # 21. Evidence log exists
    items.append({
        "id": "evidence_log_exists",
        "description": "Evidence log exists",
        "passed": file_exists(CERT_DIR / "evidence_log.md"),
        "remediation": "Create certification/evidence_log.md"
    })

    # 22. Limitations file exists with data sources reference
    items.append({
        "id": "limitations_exists",
        "description": "Limitations file exists",
        "passed": file_exists(CERT_DIR / "limitations.md") and
                  file_exists(CERT_DIR / "data_sources.md"),
        "remediation": "Create certification/limitations.md and certification/data_sources.md"
    })

    # 23. Calculation CSV and submission metadata exist
    items.append({
        "id": "calculation_csv_exists",
        "description": "Calculation CSV exists",
        "passed": file_exists(CERT_DIR / "sci_ai_calculation.csv") and
                  file_exists(CERT_DIR / "submission_metadata.yml"),
        "remediation": "Run scripts/export_sci_ai_disclosure.py and create certification/submission_metadata.yml"
    })

    # 24. Tests pass or test command documented; submission files present; reproduce instructions
    items.append({
        "id": "tests_documented",
        "description": "Tests pass or test command documented",
        "passed": file_exists(TESTS_DIR / "test_sci_ai.py") and
                  file_exists(CERT_DIR / "reviewer_notes.md") and
                  file_contains(CERT_DIR / "reviewer_notes.md", "pytest") and
                  file_exists(CERT_DIR / "gsf_submission_checklist.md") and
                  file_exists(CERT_DIR / "release_notes_v0.1.md") and
                  file_contains(CERT_DIR / "README.md", "reproduce"),
        "remediation": "Ensure tests, reviewer_notes, gsf_submission_checklist, release_notes, and reproduce instructions exist"
    })

    # 25. README disclosure status present with not-yet-certified language + reviewer aids
    items.append({
        "id": "readme_disclosure_status",
        "description": "README disclosure status present",
        "passed": (file_contains(REPO_ROOT / "README.md", "sci for ai-aligned disclosure") or
                   file_contains(REPO_ROOT / "README.md", "sci for ai-aligned")) and
                  file_contains(REPO_ROOT / "README.md", "not yet certified") and
                  file_contains(CERT_DIR / "README.md", "reviewer navigation") and
                  file_contains(CERT_DIR / "sci_ai_disclosure.md", "reviewer quick summary"),
        "remediation": "Add SCI for AI-aligned Disclosure section, reviewer navigation, and reviewer quick summary"
    })

    return items


def calculate_score(items: list) -> dict:
    points_per_item = 4
    passed_count = sum(1 for item in items if item["passed"])
    score = passed_count * points_per_item
    max_score = len(items) * points_per_item

    result = {
        "score": score,
        "max": max_score,
        "passed_count": passed_count,
        "total_count": len(items),
        "items": []
    }

    for item in items:
        result["items"].append({
            "id": item["id"],
            "description": item["description"],
            "passed": item["passed"],
            "remediation": None if item["passed"] else item["remediation"]
        })

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Validate SCI for AI disclosure certification readiness"
    )
    parser.add_argument("--strict", action="store_true",
                        help="Exit nonzero if score < 99")
    parser.add_argument("--output", type=str,
                        help="Output JSON file path (default: certification/certification_readiness_score.json)")
    args = parser.parse_args()

    items = run_checklist()
    result = calculate_score(items)

    output_path = Path(args.output) if args.output else CERT_DIR / "certification_readiness_score.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Certification Readiness Score: {result['score']}/{result['max']}")
    print(f"Items passed: {result['passed_count']}/{result['total_count']}")

    failed = [item for item in result["items"] if not item["passed"]]
    if failed:
        print(f"\nFailed items ({len(failed)}):")
        for item in failed:
            print(f"  - [{item['id']}] {item['description']}")
            if item["remediation"]:
                print(f"    Remediation: {item['remediation']}")

    if args.strict and result["score"] < 99:
        print(f"\n[STRICT] Score {result['score']} < 99. Exiting with error.")
        sys.exit(1)

    return result


if __name__ == "__main__":
    main()
