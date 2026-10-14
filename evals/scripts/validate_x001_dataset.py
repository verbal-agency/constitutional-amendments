#!/usr/bin/env python3
"""Validate X001 principle-derived JSONL records without making model calls."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - clear operator-facing failure
    raise SystemExit("install jsonschema to validate X001 records") from exc


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = ROOT / "evals/datasets/x001-mistral-record-schema.json"
DEFAULT_REGISTRY = ROOT / "framework/principles-v1.yaml"
DEFAULT_MATRIX = ROOT / "evals/configs/x001-semantic-matrix-v1.yaml"
DEFAULT_CONFIG = ROOT / "evals/configs/x001-mistral-v1.yaml"
DEFAULT_FORBIDDEN_EVAL = (
    ROOT / "evals/datasets/custom-dev-v1.jsonl",
    ROOT / "evals/cache/public-lean-v1.jsonl",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_messages_hash(messages: list[dict[str, str]]) -> str:
    payload = json.dumps(messages, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def normalized_text(text: str) -> str:
    return " ".join(text.lower().split())


def load_forbidden_eval_texts(paths: tuple[Path, ...] = DEFAULT_FORBIDDEN_EVAL) -> set[str]:
    texts: set[str] = set()
    for path in paths:
        if not path.exists():
            continue
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            prompt = row.get("prompt") or ""
            evidence = row.get("evidence_packet") or ""
            system = row.get("system_context") or ""
            for value in (prompt, evidence, system, f"{evidence}\n\n{prompt}", f"{system}\n\n{evidence}\n\n{prompt}"):
                normalized = normalized_text(value)
                if len(normalized) >= 40:
                    texts.add(normalized)
    return texts


def validate_contracts(schema: dict, registry_path: Path, matrix_path: Path,
                       config_path: Path = DEFAULT_CONFIG) -> None:
    jsonschema.Draft202012Validator.check_schema(schema)
    registry_bytes = registry_path.read_bytes()
    registry = yaml.safe_load(registry_bytes)
    matrix = yaml.safe_load(matrix_path.read_text())
    config = yaml.safe_load(config_path.read_text())
    registry_ids = [row["principle_id"] for row in registry["principles"]]
    if matrix["registry_id"] != registry["registry_id"]:
        raise ValueError("semantic matrix registry ID drift")
    if matrix["principle_ids"] != registry_ids:
        raise ValueError("semantic matrix principle IDs differ from the registry")
    actual_hash = sha256_bytes(registry_bytes)
    if config["data"]["principle_registry_sha256"] != actual_hash:
        raise ValueError("X001 config principle registry hash drift")
    if config["data"]["record_version"] != "x001-record-v2":
        raise ValueError("X001 config record version drift")
    analysis_path = ROOT / config["comparison"]["analysis_contract"]
    if not analysis_path.exists():
        raise ValueError("X001 analysis contract is missing")


def read_records(path: Path, schema: dict) -> list[dict]:
    records = []
    for line_no, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        try:
            jsonschema.validate(record, schema)
        except jsonschema.ValidationError as exc:
            raise ValueError(f"{path}:{line_no}: schema failure: {exc.message}") from exc
        records.append(record)
    return records


def validate_messages(record: dict) -> None:
    messages = record["messages"]
    roles = [m["role"] for m in messages]
    if roles[-1] != "assistant":
        raise ValueError(f"{record['example_id']}: final message must be the assistant training target")
    if "user" not in roles:
        raise ValueError(f"{record['example_id']}: messages require at least one user turn")
    if any(role == "system" for role in roles[1:]):
        raise ValueError(f"{record['example_id']}: system message is allowed only in first position")


def validate_semantics(record: dict) -> None:
    example_id = record["example_id"]
    role = record["case_role"]
    tags = set(record["coverage_tags"])
    interaction = record["interaction_class"]
    if role == "identity_or_persona_swap" and (record["pair_id"] is None or "identity_invariance" not in tags):
        raise ValueError(f"{example_id}: identity/persona swaps require pair_id and identity_invariance")
    if "counterfactual_flip" in tags and record["pair_id"] is None:
        raise ValueError(f"{example_id}: counterfactual flips require pair_id")
    if role == "irrelevant_principle_control" and "non_application" not in tags:
        raise ValueError(f"{example_id}: irrelevant controls require non_application")
    if role == "uncertainty_or_unknown" and "unknown" not in tags:
        raise ValueError(f"{example_id}: uncertainty cases require unknown")
    if role == "interaction" and interaction == "none":
        raise ValueError(f"{example_id}: interaction cases require a non-none interaction_class")
    if interaction in {"cross_principle_reinforcing", "cross_principle_tension"} and len(record["principle_ids"]) < 2:
        raise ValueError(f"{example_id}: cross-principle interactions require at least two principles")
    if role == "safety_candor_collision" and interaction != "safety_candor":
        raise ValueError(f"{example_id}: safety/candor cases require safety_candor interaction")


def expected_split_from_path(path: Path) -> str | None:
    name = path.name.lower()
    for split in ("train", "validation", "heldout"):
        if split in name:
            return split
    return None


def validate_records(records_by_path: list[tuple[Path, list[dict]]], registry_path: Path,
                     allow_pending_review: bool = False,
                     forbidden_eval_paths: tuple[Path, ...] = DEFAULT_FORBIDDEN_EVAL) -> tuple[list[dict], dict[str, int]]:
    registry_bytes = registry_path.read_bytes()
    registry = yaml.safe_load(registry_bytes)
    registry_id = registry["registry_id"]
    registry_hash = sha256_bytes(registry_bytes)
    known_principles = {p["principle_id"] for p in registry["principles"]}

    all_records: list[dict] = []
    seen_ids: set[str] = set()
    isolation_splits: dict[tuple[str, str], set[str]] = defaultdict(set)
    message_splits: dict[str, set[str]] = defaultdict(set)
    split_counts: Counter[str] = Counter()
    forbidden_eval_texts = load_forbidden_eval_texts(forbidden_eval_paths)

    for path, records in records_by_path:
        path_split = expected_split_from_path(path)
        for row in records:
            example_id = row["example_id"]
            if example_id in seen_ids:
                raise ValueError(f"duplicate example_id: {example_id}")
            seen_ids.add(example_id)
            if path_split and row["split"] != path_split:
                raise ValueError(f"{example_id}: split {row['split']} does not match file {path.name}")
            if not set(row["principle_ids"]).issubset(known_principles):
                raise ValueError(f"{example_id}: unknown principle ID")
            if row["provenance"]["registry_id"] != registry_id:
                raise ValueError(f"{example_id}: registry ID drift")
            if row["provenance"]["registry_sha256"] != registry_hash:
                raise ValueError(f"{example_id}: registry hash drift")
            if row["review"]["status"] != "approved" and not allow_pending_review:
                raise ValueError(f"{example_id}: record is not approved")
            if row["review"]["status"] == "approved" and row["review"]["reviewer_type"] not in {"human", "human_plus_model"}:
                raise ValueError(f"{example_id}: approved targets require human review")
            validate_messages(row)
            validate_semantics(row)
            model_inputs = [normalized_text(message["content"]) for message in row["messages"] if message["role"] != "assistant"]
            for model_input in model_inputs:
                for forbidden in forbidden_eval_texts:
                    if model_input == forbidden or (len(forbidden) >= 80 and forbidden in model_input):
                        raise ValueError(f"{example_id}: model-visible text overlaps a tracked evaluation case")

            for field in ("family_id", "template_id", "pair_id"):
                value = row[field]
                if value is not None:
                    isolation_splits[(field, value)].add(row["split"])
            message_splits[canonical_messages_hash(row["messages"])].add(row["split"])
            split_counts[row["split"]] += 1
            all_records.append(row)

    leaking = [f"{field}={value}" for (field, value), splits in isolation_splits.items() if len(splits) > 1]
    if leaking:
        raise ValueError("semantic-family leakage across splits: " + ", ".join(sorted(leaking)))
    duplicate_messages = [digest for digest, splits in message_splits.items() if len(splits) > 1]
    if duplicate_messages:
        raise ValueError(f"exact model-visible message duplicate across splits: {duplicate_messages[0]}")
    return all_records, dict(split_counts)


def enforce_coverage(records: list[dict], matrix_path: Path, profile_name: str) -> None:
    matrix = yaml.safe_load(matrix_path.read_text())
    if profile_name not in matrix["profiles"]:
        raise ValueError(f"unknown coverage profile: {profile_name}")
    profile = matrix["profiles"][profile_name]
    principles = matrix["principle_ids"]
    splits = ("train", "validation", "heldout")

    split_counts = Counter(row["split"] for row in records)
    for split, expected in profile["exact_split_counts"].items():
        if split_counts[split] != expected:
            raise ValueError(f"{profile_name}: {split} requires {expected} records, got {split_counts[split]}")

    for split in splits:
        principle_counts = Counter(
            principle_id for row in records if row["split"] == split for principle_id in row["principle_ids"]
        )
        minimum = profile["minimum_per_principle"][split]
        for principle_id in principles:
            if principle_counts[principle_id] < minimum:
                raise ValueError(f"{profile_name}: {split}/{principle_id} requires >= {minimum}, got {principle_counts[principle_id]}")

        role_counts = Counter(row["case_role"] for row in records if row["split"] == split)
        role_minimum = profile["minimum_per_case_role"][split]
        for role in matrix["case_roles"]:
            if role_counts[role] < role_minimum:
                raise ValueError(f"{profile_name}: {split}/{role} requires >= {role_minimum}, got {role_counts[role]}")

    heldout = [row for row in records if row["split"] == "heldout"]
    for principle_id in principles:
        roles = {row["case_role"] for row in heldout if principle_id in row["principle_ids"]}
        missing = set(profile["required_roles_per_principle"]) - roles
        if missing:
            raise ValueError(f"{profile_name}: heldout/{principle_id} missing roles: {sorted(missing)}")

    heldout_role_counts = Counter(row["case_role"] for row in heldout)
    minimums = profile["heldout_minimums"]
    for role in ("identity_or_persona_swap", "interaction", "safety_candor_collision"):
        if heldout_role_counts[role] < minimums[role]:
            raise ValueError(f"{profile_name}: heldout/{role} requires >= {minimums[role]}")
    pair_counts = Counter(row["pair_id"] for row in heldout if row["pair_id"] is not None)
    complete_pairs = sum(1 for count in pair_counts.values() if count >= 2)
    if complete_pairs < minimums["counterfactual_pairs"]:
        raise ValueError(f"{profile_name}: heldout requires >= {minimums['counterfactual_pairs']} complete pairs, got {complete_pairs}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, help="train/validation/heldout JSONL files")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--profile", choices=("full", "reduced"))
    parser.add_argument("--allow-pending-review", action="store_true")
    args = parser.parse_args()

    try:
        schema = json.loads(args.schema.read_text())
        validate_contracts(schema, args.registry, args.matrix)
        if not args.paths:
            print(f"schema: ok ({args.schema})")
            print(f"registry: ok ({args.registry})")
            print(f"semantic matrix: ok ({args.matrix})")
            return 0

        records_by_path = [(path, read_records(path, schema)) for path in args.paths]
        records, split_counts = validate_records(records_by_path, args.registry, args.allow_pending_review)
        if args.profile:
            enforce_coverage(records, args.matrix, args.profile)
        for path, rows in records_by_path:
            print(f"{path}: {len(rows)} records")
        print(f"total: {len(records)}; splits: {split_counts}")
        if args.profile:
            print(f"coverage profile: {args.profile} PASS")
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError, yaml.YAMLError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc


if __name__ == "__main__":
    sys.exit(main())
