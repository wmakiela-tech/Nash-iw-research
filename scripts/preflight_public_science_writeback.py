#!/usr/bin/env python3
"""Explicit preflight of public research metadata (including modified files).

Shares validate_new_research with the existing added-only CI guard. No BW write,
no scientific adjudication and no direct private provider-coordinate output.
"""
from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

from check_public_science_writeback import validate_new_research

SHA = re.compile(r"[0-9a-fA-F]{7,40}\Z")
TEXT = {".md", ".rst", ".txt"}


def eligible_path(path: str) -> bool:
    p = PurePosixPath(path)
    return (
        path.startswith("research/")
        and not p.is_absolute()
        and ".." not in p.parts
        and p.suffix.lower() in TEXT
    )


def changed_paths(base: str, head: str) -> list[str]:
    if not SHA.fullmatch(base) or not SHA.fullmatch(head) or set(base) == {"0"}:
        raise ValueError("BAD_GIT_REVISION")
    result = subprocess.run(
        ["git", "diff", "--no-ext-diff", "--name-only", "-z",
         "--diff-filter=AM", base, head, "--", "research/"],
        check=True, capture_output=True,
    )
    paths = [part.decode("utf-8", "replace") for part
             in result.stdout.split(b"\0") if part]
    # Diff also contains scripts/data in research/. The science metadata guard
    # applies only to text research bodies, never code/data artifacts.
    return [path for path in paths if eligible_path(path)]


def preflight_path(path: str, body: str) -> list[str]:
    if not eligible_path(path):
        return ["NOT_RESEARCH_TEXT_PATH"]
    return validate_new_research(path, body)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Preflight PUBLIC research body metadata")
    parser.add_argument("paths", nargs="*", help="current working-tree research text files")
    parser.add_argument("--base", help="Git base SHA for explicit added+modified check")
    parser.add_argument("--head", help="Git head SHA, required with --base")
    args = parser.parse_args(argv)
    if bool(args.base) != bool(args.head) or (args.base and args.paths):
        parser.error("Use PATHS or --base SHA --head SHA, not both")
    if not args.paths and not args.base:
        parser.error("Supply research file paths or --base/--head")

    try:
        candidates = changed_paths(args.base, args.head) if args.base else args.paths
        if not candidates:
            if args.base:
                # A routine docs/code-only commit must not fail a metadata gate
                # intended for added or modified public research text bodies.
                print("PASS: 0 added/modified public research text bodies selected")
                return 0
            print("FAIL: NO_ELIGIBLE_RESEARCH_PATHS_SELECTED")
            return 2
        failures = []
        for path in dict.fromkeys(candidates):
            if not eligible_path(path):
                failures.append((path, "NOT_RESEARCH_TEXT_PATH"))
                continue
            if args.base:
                content = subprocess.run(
                    ["git", "show", f"{args.head}:{path}"],
                    check=True, capture_output=True,
                ).stdout.decode("utf-8", "replace")
            else:
                content = Path(path).read_text(encoding="utf-8")
            failures.extend((path, reason) for reason in preflight_path(path, content))
    except (OSError, ValueError, UnicodeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: PREFLIGHT_INPUT_UNREADABLE ({type(exc).__name__})", file=sys.stderr)
        return 2
    for path, reason in failures:
        print(f"{path}: {reason}")
    if failures:
        print(f"FAIL: {len(failures)} metadata or selection issue(s)")
        return 1
    print(f"PASS: {len(dict.fromkeys(candidates))} explicit public research body/bodies checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
