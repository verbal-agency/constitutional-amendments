#!/usr/bin/env python3
"""Run the predeclared three-replicate G006-S5R factorial probe."""
import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HISTORICAL_PRIMARY_COST = 2.149594
CEILING = 0.75
CELLS = (
    ("00", "evals/maps/g006-s5-factorial-00-base.json"),
    ("10", "evals/maps/g006-s5-factorial-10-map002-only.json"),
    ("01", "evals/maps/g006-s5-factorial-01-others-only.json"),
    ("11", "evals/maps/g006-replacement-v3.json"),
)


def manifest_cost(path):
    data = json.loads(path.read_text())
    generation = float(data["generation"]["cost_usd"])
    primary = float(data["primary"]["cumulative_cost_usd"]) - HISTORICAL_PRIMARY_COST
    secondary = float(data["secondary"]["cost_usd"])
    return generation + primary + secondary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-root", default="evals/runs/g006-s5r-d2-replication")
    ap.add_argument("--target-manifest", default="evals/manifests/g006-s5r-d2-replication.json")
    args = ap.parse_args()
    run_root = Path(args.run_root)
    if not run_root.is_absolute():
        run_root = ROOT / run_root
    target = Path(args.target_manifest)
    if not target.is_absolute():
        target = ROOT / target
    run_root.mkdir(parents=True, exist_ok=True)
    plan = {"replicates": 3, "cells": [cell for cell, _ in CELLS], "ceiling_usd": CEILING,
            "order": [], "completed": [], "cost_usd": 0.0}
    for replicate in range(1, 4):
        for cell, candidate_map in CELLS:
            run_dir = run_root / f"r{replicate}-{cell}"
            plan["order"].append(f"r{replicate}-{cell}")
            command = [sys.executable, str(ROOT / "evals/scripts/run_g006_failure_loop.py"),
                       "--target-manifest", str(target), "--run-dir", str(run_dir),
                       "--candidate-map", str(ROOT / candidate_map)]
            print(f"RUN r{replicate}-{cell}", flush=True)
            result = subprocess.run(command, cwd=ROOT)
            if result.returncode != 0:
                plan["stopped"] = f"r{replicate}-{cell} exited {result.returncode}"
                (run_root / "plan.json").write_text(json.dumps(plan, indent=2) + "\n")
                return result.returncode
            cost = manifest_cost(run_dir / "manifest.json")
            plan["cost_usd"] = round(plan["cost_usd"] + cost, 6)
            plan["completed"].append({"replicate": replicate, "cell": cell,
                                      "run_dir": str(run_dir.relative_to(ROOT)),
                                      "cost_usd": round(cost, 6)})
            (run_root / "plan.json").write_text(json.dumps(plan, indent=2) + "\n")
            print(f"COST r{replicate}-{cell} ${cost:.6f} cumulative=${plan['cost_usd']:.6f}", flush=True)
            if plan["cost_usd"] >= CEILING:
                plan["stopped"] = "approved cost ceiling reached"
                (run_root / "plan.json").write_text(json.dumps(plan, indent=2) + "\n")
                return 2
    plan["status"] = "complete"
    (run_root / "plan.json").write_text(json.dumps(plan, indent=2) + "\n")
    print(json.dumps(plan, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
