"""Flag newly added direct Drive/Slack provider coordinates in public Git sources.

Deliberately bounded: only added text lines of a selected Git diff. Historic
commits, binaries, obfuscated or split links, and actual sharing permissions are
outside this check. Never print a matched provider coordinate.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import PurePosixPath
from typing import Iterator

_RULES = (
    ("google-drive-document-url", re.compile(
        r"https?://(?:docs\.google\.com/(?:document|spreadsheets|presentation|forms)/d/"
        r"|drive\.google\.com/(?:file/d/|drive/(?:u/\d+/)?folders/|open\?id=))"
        r"[A-Za-z0-9_-]{20,}", re.IGNORECASE)),
    ("bare-drive-reference", re.compile(
        r"\bDrive(?:[ _-]*(?:ID|file|document))?\s*[:=# -]+\s*"
        r"[A-Za-z0-9_-]{27,}\b", re.IGNORECASE)),
    ("slack-workspace-source-url", re.compile(
        r"https?://[A-Za-z0-9.-]*slack\.com/(?:archives/[A-Za-z0-9]+/p\d{13,}"
        r"|files/[^\s<>\])]+)", re.IGNORECASE)),
)
TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".rst", ".toml",
    ".csv", ".html", ".js", ".jsx", ".ts", ".tsx", ".ipynb", ".sh",
    ".xml", ".ini", ".cfg", ".sql",
}
SHA_RE = re.compile(r"[0-9a-fA-F]{7,40}\Z")
HUNK_RE = re.compile(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")


def find_risks(line: str) -> list[str]:
    """Return rule categories only, never coordinates."""
    return [name for name, pattern in _RULES if pattern.search(line)]


def iter_added_lines(patch: str) -> Iterator[tuple[str, int, str]]:
    """Yield path, new line number, and text for additions in a -U0 Git patch."""
    path: str | None = None
    line_no: int | None = None
    for line in patch.splitlines():
        if line.startswith("+++ b/"):
            path = line[6:]
            line_no = None
        elif line.startswith("+++ /dev/null"):
            path = None
            line_no = None
        elif line.startswith("@@"):
            match = HUNK_RE.match(line)
            line_no = int(match.group(1)) if match else None
        elif line.startswith("+") and not line.startswith("+++"):
            if path is not None and line_no is not None:
                yield path, line_no, line[1:]
                line_no += 1
        elif line.startswith(" ") and line_no is not None:
            line_no += 1


def inspect_patch(patch: str) -> list[tuple[str, int, str]]:
    issues = []
    for path, number, line in iter_added_lines(patch):
        if PurePosixPath(path).suffix.lower() not in TEXT_EXTENSIONS:
            continue
        for rule in find_risks(line):
            issues.append((path, number, rule))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check added public Git source lines for Drive/Slack coordinates"
    )
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args(argv)
    if (not SHA_RE.fullmatch(args.base) or not SHA_RE.fullmatch(args.head)
            or set(args.base) == {"0"}):
        parser.error("Expected valid nonzero Git base/head commit hashes")
    try:
        patch = subprocess.run(
            ["git", "diff", "--no-ext-diff", "--unified=0", "--diff-filter=ACMR",
             args.base, args.head, "--"],
            check=True, text=True, capture_output=True, encoding="utf-8",
            errors="replace",
        ).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        print(
            f"FAIL: unable to inspect Git changes ({type(exc).__name__})",
            file=sys.stderr,
        )
        return 2
    issues = inspect_patch(patch)
    for path, number, rule in issues:
        print(
            f"{path}:{number}: {rule}: new provider coordinate; "
            "cite source name and keep private locator in BW"
        )
    if issues:
        print(f"FAIL: {len(issues)} new coordinate match(es); source review required")
        return 1
    print("PASS: no added direct provider coordinates (bounded check)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
