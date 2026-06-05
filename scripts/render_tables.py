#!/usr/bin/env python3
"""
Render Tables

Standalone entry point that imports the calculator and renders
comparison tables to stdout or a specified output file.

Usage:
    python scripts/render_tables.py              # prints to stdout
    python scripts/render_tables.py -o FILE      # writes to file
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculate_savings import (
    load_all_assumptions,
    calculate_cloud_first_meeting,
    calculate_offline_first_meeting,
    calculate_hybrid_meeting,
    calculate_scenario,
    render_markdown_tables,
)


def build_results(assumptions):
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

    return all_results


def main():
    parser = argparse.ArgumentParser(description="Render token savings comparison tables")
    parser.add_argument("-o", "--output", type=str, help="Output file path (default: stdout)")
    args = parser.parse_args()

    assumptions = load_all_assumptions()
    results = build_results(assumptions)
    markdown = render_markdown_tables(results)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(markdown)
        print(f"Tables written to: {args.output}")
    else:
        print(markdown)


if __name__ == "__main__":
    main()
