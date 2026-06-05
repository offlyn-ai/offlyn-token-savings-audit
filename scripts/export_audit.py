#!/usr/bin/env python3
"""
Export Audit Results

Generates machine-readable audit output in JSON or CSV format,
conforming to schemas/audit_run.schema.json.

Usage:
    python scripts/export_audit.py                    # JSON to stdout
    python scripts/export_audit.py --format json -o output/audit_run.json
    python scripts/export_audit.py --format csv -o output/audit_run.csv
"""

import argparse
import csv
import io
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculate_savings import (
    load_all_assumptions,
    calculate_cloud_first_meeting,
    calculate_offline_first_meeting,
    calculate_hybrid_meeting,
    calculate_quality_score,
)
from calculate_sci_ai import (
    load_sci_ai_assumptions,
    calculate_sci_ai_meeting,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def get_git_hash():
    try:
        import subprocess
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return result.stdout.strip()[:12] if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def build_audit_run(minutes: int = 60) -> dict:
    assumptions = load_sci_ai_assumptions()
    sci_ai_results = calculate_sci_ai_meeting(minutes, assumptions)

    savings_assumptions = load_all_assumptions()
    cf = calculate_cloud_first_meeting(minutes, savings_assumptions)
    of = calculate_offline_first_meeting(minutes, savings_assumptions)
    hr = calculate_hybrid_meeting(minutes, savings_assumptions)

    architectures = {}
    for arch_key, savings, sci in [
        ("cloud_first", cf, sci_ai_results["cloud_first"]),
        ("offline_first", of, sci_ai_results["offline_first"]),
        ("hybrid_router", hr, sci_ai_results["hybrid_router"]),
    ]:
        architectures[arch_key] = {
            "cloud_billable_tokens": savings["cloud_billable_tokens"],
            "cloud_llm_input_tokens": savings["cloud_llm_input_tokens"],
            "cloud_llm_output_tokens": savings["cloud_llm_output_tokens"],
            "cloud_embedding_tokens": savings["cloud_embedding_tokens"],
            "transcription_cost_usd": savings["transcription_cost_usd"],
            "llm_cost_usd": savings["llm_cost_usd"],
            "embedding_cost_usd": savings["embedding_cost_usd"],
            "cloud_total_cost_usd": savings["cloud_total_cost_usd"],
            "local_compute_cost_usd": savings["local_compute_cost_usd"],
            "total_estimated_cost_usd": savings["total_estimated_cost_usd"],
            "cloud_carbon_gco2e": sci["cloud_carbon_gco2e"],
            "local_incremental_carbon_gco2e": sci["local_incremental_carbon_gco2e"],
            "total_consumer_carbon_gco2e": sci["total_consumer_carbon_gco2e"],
            "avoided_cloud_carbon_gco2e": sci["avoided_cloud_carbon_gco2e"],
            "net_avoided_total_carbon_gco2e": sci["net_avoided_total_carbon_gco2e"],
            "direct_datacenter_water_liters": sci["direct_datacenter_water_liters"],
            "avoided_direct_water_liters": sci["avoided_direct_water_liters"],
            "cloud_transfer_mb": sci["cloud_transfer_mb"],
            "avoided_transfer_mb": sci["avoided_transfer_mb"],
            "quality_score": savings["quality_score"],
            "privacy_score": savings["privacy_score"],
            "offline_resilience_score": savings["offline_resilience_score"],
        }

    functional_units = {}
    for fu_key in ["gco2e_per_meeting_hour", "gco2e_per_second_audio",
                   "gco2e_per_transcript", "gco2e_per_workflow_execution",
                   "gco2e_per_accepted_summary"]:
        functional_units[fu_key] = {}
        for arch_key in ["cloud_first", "offline_first", "hybrid_router"]:
            val = sci_ai_results[arch_key].get(fu_key)
            if val is not None and val == val:
                functional_units[fu_key][arch_key] = val

    audit_run = {
        "run_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "assumptions_version": get_git_hash(),
        "claim_level": "modeled_not_verified",
        "reporting_mode": "operational_proxy",
        "sci_ai_boundary": "consumer",
        "meeting_minutes": minutes,
        "architectures": architectures,
        "functional_units": functional_units,
    }

    return audit_run


def export_json(audit_run: dict) -> str:
    return json.dumps(audit_run, indent=2)


def export_csv(audit_run: dict) -> str:
    output = io.StringIO()
    writer = csv.writer(output)

    header = ["metric", "cloud_first", "offline_first", "hybrid_router"]
    writer.writerow(header)

    archs = audit_run["architectures"]
    metrics = list(archs["cloud_first"].keys())

    for metric in metrics:
        row = [metric]
        for arch in ["cloud_first", "offline_first", "hybrid_router"]:
            row.append(archs[arch].get(metric, ""))
        writer.writerow(row)

    writer.writerow([])
    writer.writerow(["functional_unit", "cloud_first", "offline_first", "hybrid_router"])
    for fu_key, fu_vals in audit_run.get("functional_units", {}).items():
        row = [fu_key]
        for arch in ["cloud_first", "offline_first", "hybrid_router"]:
            row.append(fu_vals.get(arch, "N/A"))
        writer.writerow(row)

    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description="Export audit results in JSON or CSV")
    parser.add_argument("--format", choices=["json", "csv"], default="json",
                        help="Output format (default: json)")
    parser.add_argument("-o", "--output", type=str,
                        help="Output file path (default: stdout)")
    parser.add_argument("--minutes", type=int, default=60,
                        help="Meeting duration in minutes (default: 60)")
    args = parser.parse_args()

    audit_run = build_audit_run(args.minutes)

    if args.format == "csv":
        content = export_csv(audit_run)
    else:
        content = export_json(audit_run)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            f.write(content)
        print(f"Audit exported to: {out_path}")
    else:
        print(content)


if __name__ == "__main__":
    main()
