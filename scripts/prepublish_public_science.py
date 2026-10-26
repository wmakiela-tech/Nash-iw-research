#!/usr/bin/env python3
"""Author-side, fail-closed public publication check (no BW writes).

Run after committing locally and BEFORE pushing public research:
  python scripts/prepublish_public_science.py --base origin/main --head HEAD

CI runs the same check on PRs and main pushes. It checks NEW diff lines for
direct Drive/Slack coordinates, and new OR modified research text bodies for
required publication/BW metadata. It does not certify sharing rights or BW sync.
Never echo a matched provider URL or identifier.
"""
from __future__ import annotations

import argparse
import subprocess
import sys

from check_public_locators import inspect_patch
from preflight_public_science_writeback import changed_paths, preflight_path


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, text=True, capture_output=True,
        encoding="utf-8", errors="replace",
    ).stdout


def audit(base_ref: str, head_ref: str):
    base = git("rev-parse", "--verify", base_ref + "^{commit}").strip()
    head = git("rev-parse", "--verify", head_ref + "^{commit}").strip()
    # PR branches may diverge from the latest main; only audit the authored
    # changes, not unrelated commits that reached main in the meantime.
    common = git("merge-base", base, head).strip()
    if not common or not head:
        raise ValueError("UNRESOLVED_HISTORY")
    patch = git(
        "diff", "--no-ext-diff", "--unified=0", "--diff-filter=ACMR",
        common, head, "--",
    )
    locator_issues = inspect_patch(patch)
    metadata_issues = []
    paths = changed_paths(common, head)
    for path in paths:
        content = git("show", head + ":" + path)
        metadata_issues.extend(
            (path, reason) for reason in preflight_path(path, content)
        )
    return locator_issues, metadata_issues, paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check a committed change before public GitHub publication"
    )
    parser.add_argument("--base", required=True, help="baseline ref, e.g. origin/main")
    parser.add_argument("--head", default="HEAD", help="new commit/ref (default HEAD)")
    args = parser.parse_args(argv)
    try:
        locators, metadata, paths = audit(args.base, args.head)
    except (OSError, ValueError, subprocess.CalledProcessError):
        print("FAIL: PUBLICATION_PREFLIGHT_INPUT_OR_HISTORY_UNREADABLE",
              file=sys.stderr)
        return 2
    for path, line, category in locators:
        print(f"{path}:{line}: {category}: PRIVATE_PROVIDER_COORDINATE")
    for path, reason in metadata:
        print(f"{path}: {reason}")
    if locators or metadata:
        print(f"FAIL: {len(locators)} provider coordinate(s), "
              f"{len(metadata)} public research metadata issue(s)")
        return 1
    print(f"PASS: PUBLICATION_PREFLIGHT (research texts checked: {len(paths)}; "
          "added private provider coordinates: 0)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
