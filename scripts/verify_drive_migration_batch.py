"""Verify a *private* Drive-to-GitHub migration export against a local checkout.

Run only against private manifests, stored outside public repositories.
Input is newline-delimited JSON with: source_id, target_path, sha256, status.
sha256 refers to the bytes of the *exported migration file*, not the original
Google-native document and not a semantic-fidelity assurance.

Example:
  python scripts/verify_drive_migration_batch.py \
     --manifest /secure/path/migration/file-mapping.jsonl \
     --checkout /secure/path/Nash-iw-private

Do not publish the manifest or print its original source IDs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_VALID_STATUS = {"MIGRATED_VERIFIED", "MIGRATION_PARTIAL", "NOT_YET_EXPORTED",
                 "ACCESS_BLOCKED", "FORMAT_LOSS", "LFS_OBJECT_MISSING",
                 "BW_RECONCILIATION_REQUIRED", "SOURCE_ONLY_SLACK", "HOLD"}


def _safe_relative_path(value: str) -> bool:
    if not value or "\\" in value or value.startswith("/"):
        return False
    path = PurePosixPath(value)
    return all(component not in {".", "..", ""} for component in path.parts)


def verify(manifest: Path, checkout: Path) -> dict[str, int]:
    counts = {"records": 0, "verified": 0, "pending": 0, "failed": 0,
              "duplicate_source": 0, "duplicate_target": 0}
    seen_sources, seen_paths = set(), set()
    checkout = checkout.resolve(strict=True)
    with manifest.open(encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            counts["records"] += 1
            try:
                record = json.loads(line)
                if not isinstance(record, dict):
                    raise ValueError("not an object")
                source = record.get("source_id", "")
                target = record.get("target_path", "")
                digest = record.get("sha256", "")
                status = record.get("status", "")
                if not isinstance(source, str) or not source:
                    raise ValueError("missing source identity")
                if source in seen_sources:
                    counts["duplicate_source"] += 1
                seen_sources.add(source)
                if status not in _VALID_STATUS:
                    raise ValueError("unrecognized migration state")
                if status != "MIGRATED_VERIFIED":
                    counts["pending"] += 1
                    continue
                if not isinstance(target, str) or not _safe_relative_path(target):
                    raise ValueError("invalid target path")
                if target in seen_paths:
                    counts["duplicate_target"] += 1
                seen_paths.add(target)
                if not isinstance(digest, str) or not _SHA256.fullmatch(digest):
                    raise ValueError("invalid export sha256")
                full = (checkout / target).resolve()
                if not full.is_relative_to(checkout) or not full.is_file():
                    raise ValueError("target file absent or escapes checkout")
                hasher = hashlib.sha256()
                with full.open("rb") as f:
                    for block in iter(lambda: f.read(1024 * 1024), b""):
                        hasher.update(block)
                if hasher.hexdigest() != digest:
                    raise ValueError("target byte hash mismatch")
                counts["verified"] += 1
            except (ValueError, TypeError, OSError, json.JSONDecodeError):
                counts["failed"] += 1
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify private migration copies")
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--checkout", type=Path, required=True)
    args = ap.parse_args()
    try:
        counts = verify(args.manifest, args.checkout)
    except (OSError, ValueError) as exc:
        print(f"ERROR: cannot verify manifest ({type(exc).__name__})", file=sys.stderr)
        return 2
    # Print aggregate only: never echo private IDs, titles or source URLs.
    print(json.dumps(counts, sort_keys=True))
    return 0 if (counts["failed"] == 0 and counts["duplicate_source"] == 0
                 and counts["duplicate_target"] == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
