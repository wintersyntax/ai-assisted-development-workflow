#!/usr/bin/env python3
"""Standard-library validation for the public workflow repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "docs/ARCHITECTURE.md",
    "docs/WORKFLOW.md",
    "docs/AGENT_ROLES.md",
    "docs/DOCUMENTATION_AUTHORITY.md",
    "docs/MODEL_AND_COST_STRATEGY.md",
    "docs/HANDOFF_CONTRACT.md",
    "docs/LEDGER_SYSTEM.md",
    "docs/CHECKPOINTS_AND_REPAIR.md",
    "docs/CI_CD.md",
    "docs/CASE_STUDY.md",
    "schemas/handoff.schema.json",
    "examples/architect-handoff.example.json",
    "examples/do-not-forget-ledger.example.md",
    "examples/repair-loop.example.md",
    "demo/index.html",
    "demo/style.css",
    "demo/app.js",
    "scripts/serve_demo.py",
]

PRIVATE_PATTERNS = [
    re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
TASK_RE = re.compile(r"^TASK-[A-Z0-9-]+$")
LEDGER_TASK_RE = re.compile(r"^### (TASK-\d{3})\s+—\s+(.+)$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    raise ValueError(message)


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require_nonempty_list(obj: dict, field: str) -> None:
    value = obj.get(field)
    if not isinstance(value, list) or not value:
        fail(f"{field} must be a non-empty list")


def validate_handoff() -> None:
    data = load_json("examples/architect-handoff.example.json")
    if set(data) != {"_comment", "contract", "blueprint"}:
        fail("handoff must contain _comment, contract and blueprint")

    contract = data["contract"]
    blueprint = data["blueprint"]

    required_contract = {
        "contract_version", "task_id", "base_main_sha", "objective",
        "non_goals", "relevant_paths", "invariants", "acceptance",
        "verification", "stop_conditions", "risks",
    }
    if set(contract) != required_contract:
        fail("contract field set does not match public schema")

    if contract["contract_version"] != 1:
        fail("contract_version must be 1")
    if not TASK_RE.fullmatch(contract["task_id"]):
        fail("contract task_id is invalid")
    if not SHA_RE.fullmatch(contract["base_main_sha"]):
        fail("contract base_main_sha must be a 40-character lowercase SHA")
    if not isinstance(contract["objective"], str) or not contract["objective"].strip():
        fail("contract objective must be non-empty")

    for field in (
        "relevant_paths", "invariants", "acceptance",
        "verification", "stop_conditions", "risks",
    ):
        require_nonempty_list(contract, field)
    if not isinstance(contract["non_goals"], list):
        fail("contract non_goals must be a list")

    if blueprint.get("task_id") != contract["task_id"]:
        fail("blueprint task_id must match contract task_id")
    if not isinstance(blueprint.get("blueprint_version"), int):
        fail("blueprint_version must be an integer")
    if not isinstance(blueprint.get("solved_solution"), str) or not blueprint["solved_solution"].strip():
        fail("blueprint solved_solution must be non-empty")
    slices = blueprint.get("slices")
    if not isinstance(slices, list) or not slices:
        fail("blueprint slices must be non-empty")
    if not isinstance(blueprint.get("final_verify"), dict):
        fail("blueprint final_verify must be an object")

    seen = set()
    for index, slice_ in enumerate(slices):
        slice_id = slice_.get("slice_id")
        if not isinstance(slice_id, str) or not slice_id:
            fail(f"slice {index + 1} lacks slice_id")
        if slice_id in seen:
            fail(f"duplicate slice_id: {slice_id}")
        depends_on = slice_.get("depends_on")
        if not isinstance(depends_on, list):
            fail(f"{slice_id} depends_on must be a list")
        unknown = [dep for dep in depends_on if dep not in seen]
        if unknown:
            fail(f"{slice_id} depends on later/unknown slices: {unknown}")
        seen.add(slice_id)

        require_nonempty_list(slice_, "paths")
        require_nonempty_list(slice_, "exact_changes")
        require_nonempty_list(slice_, "mutation_targets")
        require_nonempty_list(slice_, "preserve")
        require_nonempty_list(slice_, "stop_conditions")
        if not isinstance(slice_.get("regression_tests"), list):
            fail(f"{slice_id} regression_tests must be a list")
        verify = slice_.get("verify")
        if not isinstance(verify, dict) or not verify.get("commands"):
            fail(f"{slice_id} requires verification commands")

    first = slices[0]
    edits = first["exact_changes"][0].get("edits")
    if not isinstance(edits, list) or not edits:
        fail("first example slice must demonstrate exact edits")
    if not first["regression_tests"]:
        fail("first example slice must demonstrate Architect-authored regression tests")


def validate_ledger() -> None:
    path = ROOT / "examples/do-not-forget-ledger.example.md"
    text = path.read_text(encoding="utf-8")
    required_sections = [
        "## Current / Next Work",
        "## Blocked / Waiting / Evidence Pending",
        "## Deferred / Triggered Later",
    ]
    for heading in required_sections:
        if heading not in text:
            fail(f"ledger example missing section: {heading}")

    matches = list(LEDGER_TASK_RE.finditer(text))
    if not matches:
        fail("ledger example contains no TASK-### records")

    ids = [m.group(1) for m in matches]
    if len(ids) != len(set(ids)):
        fail("ledger example contains duplicate task IDs")

    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end]
        for field in ("**Status:**", "**Priority:**", "**Goal:**", "**Done when:**"):
            if field not in block:
                fail(f"{match.group(1)} missing {field}")


def validate_required_paths() -> None:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def validate_markdown_links() -> None:
    markdown_files = [
        ROOT / "README.md",
        *sorted((ROOT / "docs").glob("*.md")),
        *sorted((ROOT / "examples").glob("*.md")),
    ]
    errors = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            if raw.startswith("#"):
                continue
            parsed = urlparse(raw)
            if parsed.scheme in {"http", "https", "mailto"}:
                continue
            target = raw.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} -> escapes repo: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} -> missing: {raw}")
    if errors:
        fail("broken Markdown links:\n" + "\n".join(errors))


def validate_public_safety() -> None:
    text_files = [
        *[ROOT / p for p in REQUIRED_PATHS],
        *sorted((ROOT / "examples").glob("*")),
        *sorted((ROOT / "scripts").glob("*.py")),
    ]
    hits = []
    for path in text_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                hits.append(f"{path.relative_to(ROOT)}: {pattern.pattern}")
    if hits:
        fail("possible private/secret material detected:\n" + "\n".join(hits))


def main() -> int:
    checks = [
        validate_required_paths,
        validate_handoff,
        validate_ledger,
        validate_markdown_links,
        validate_public_safety,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("Workflow repository validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
