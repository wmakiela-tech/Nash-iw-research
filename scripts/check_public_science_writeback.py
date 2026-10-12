"""Forward-only lint for new public research bodies and their BW linkage.

Checks newly added research/ files only. It does not read private BW or certify
BW ingestion, source truth, publication rights, or scientific validation.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import PurePosixPath

SHA = re.compile(r"[0-9a-fA-F]{7,40}\Z")
TEXT = {".md", ".rst", ".txt"}


def validate_new_research(path: str, body: str) -> list[str]:
    """Metadata/body completeness checks; only return generic rule categories."""
    if not path.startswith("research/") or PurePosixPath(path).suffix.lower() not in TEXT:
        return []
    bad = []
    header = body[:3500]
    required = {
        "ARTIFACT_ID_REQUIRED": r"(?m)^artifact_id:\s*\S+",
        "PUBLIC_EXPOSURE_REQUIRED": r"(?m)^exposure:\s*PUBLIC\s*$",
        "CLAIM_CEILING_REQUIRED": r"(?m)^(?:scientific_claim_ceiling|claim_ceiling|result_class|status):\s*\S+",
    }
    for reason, pattern in required.items():
        if not re.search(pattern, header):
            bad.append(reason)
    bw_event = re.search(r"(?m)^bw_ingestion_event_id:\s*ING-\d{8}-\d+\s*$", header)
    pending = re.search(r"(?m)^sync_state:\s*GITHUB_PENDING_BW_INGEST\s*$", header)
    if not (bw_event or pending):
        bad.append("BW_EVENT_OR_EXPLICIT_PENDING_REQUIRED")
    if re.search(r"(?m)^archive_mode:\s*(?:POINTER_ONLY|HASH_ONLY)\s*$", header):
        bad.append("PUBLIC_SCIENCE_BODY_NOT_POINTER")
    if len(body.strip()) < 600:
        bad.append("SOURCE_BODY_TOO_SHORT_FOR_DEFAULT_PUBLIC_RESEARCH_ARTIFACT")
    return bad


def added_research_paths(base: str, head: str) -> list[str]:
    data = subprocess.run(
        ["git", "diff", "--no-ext-diff", "--name-only", "-z",
         "--diff-filter=A", base, head, "--", "research/"],
        check=True, capture_output=True,
    ).stdout
    return [
        path.decode("utf-8", "replace")
        for path in data.split(b"\x00") if path
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate new GitHub public science routing")
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args(argv)
    if (not SHA.fullmatch(args.base) or not SHA.fullmatch(args.head)
            or set(args.base) == {"0"}):
        parser.error("Expected nonzero base/head Git commit hashes")
    try:
        names = added_research_paths(args.base, args.head)
        failures = []
        for name in names:
            if PurePosixPath(name).suffix.lower() not in TEXT:
                continue
            result = subprocess.run(
                ["git", "show", f"{args.head}:{name}"],
                check=True, capture_output=True,
            )
            body = result.stdout.decode("utf-8", errors="replace")
            failures.extend((name, error) for error in validate_new_research(name, body))
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: unable to inspect new research ({type(exc).__name__})", file=sys.stderr)
        return 2
    for path, error in failures:
        print(f"{path}: {error}")
    if failures:
        print(f"FAIL: {len(failures)} new public-science routing issue(s)")
        return 1
    print(f"PASS: {len(names)} new research path(s) scanned for public science/BW metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
