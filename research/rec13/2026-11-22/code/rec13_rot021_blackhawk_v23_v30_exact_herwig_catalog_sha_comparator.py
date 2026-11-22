#!/usr/bin/env python3
"""REC13 ROT021 BlackHawk v2.3 vs v3.0 HERWIG catalog SHA256 audit.
Reads authentic local .tar.bz2 originals; does NOT download or claim real comparison.
Usage: python rec13_rot021_blackhawk_v23_v30_exact_herwig_catalog_sha_comparator.py original23.tar.bz2 original30.tar.bz2
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tarfile

PATTERN = re.compile(r"(?:^|/)src/tables/herwig_tables/(.+)$")

def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for block in iter(lambda: fp.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def catalog(path: Path) -> dict:
    if not path.is_file():
        return {"status": "FILE_NOT_AVAILABLE", "path": str(path)}
    if not path.name.endswith(".tar.bz2"):
        return {"status": "UNSUPPORTED_ARCHIVE_NAME", "path": str(path)}
    found = {}
    try:
        with tarfile.open(path, "r:bz2") as archive:
            for item in archive:
                match = PATTERN.search(item.name.replace("\\", "/"))
                if not match or item.isdir():
                    continue
                rel = str(PurePosixPath(match.group(1)))
                if rel in (".", "..") or rel.startswith("../") or rel.startswith("/"):
                    raise ValueError("UNSAFE_PATH")
                if not item.isfile():
                    raise ValueError("NONREGULAR_MEMBER:" + rel)
                if rel in found:
                    raise ValueError("DUPLICATE_RELATIVE_PATH:" + rel)
                h = hashlib.sha256()
                with archive.extractfile(item) as fp:
                    for block in iter(lambda: fp.read(1024 * 1024), b""):
                        h.update(block)
                found[rel] = {"bytes": item.size, "sha256": h.hexdigest()}
    except (tarfile.TarError, OSError, ValueError, EOFError) as exc:
        return {"status": "ARCHIVE_READ_FAIL_CLOSED", "error": str(exc)}
    if not found:
        return {"status": "NO_HERWIG_CATALOG", "archive_sha256": digest_file(path)}
    return {"status": "MANIFEST_PASS", "archive_sha256": digest_file(path),
            "archive_bytes": path.stat().st_size, "file_count": len(found),
            "files": dict(sorted(found.items()))}

def compare(v23: Path, v30: Path) -> dict:
    a, b = catalog(v23), catalog(v30)
    if a["status"] != "MANIFEST_PASS" or b["status"] != "MANIFEST_PASS":
        return {"verdict": "ACCESS_OR_CATALOG_HOLD", "v23": a, "v30": b}
    x, y = a["files"], b["files"]
    old, new = sorted(set(x)-set(y)), sorted(set(y)-set(x))
    changed = sorted(k for k in x.keys() & y.keys() if x[k] != y[k])
    return {"verdict": ("DIFFERENT_CATALOG_BYTES" if old or new or changed
                        else "SAME_CATALOG_BYTES"),
            "v23_archive_sha256": a["archive_sha256"], "v30_archive_sha256": b["archive_sha256"],
            "v23_count": a["file_count"], "v30_count": b["file_count"],
            "only_v23": old, "only_v30": new, "changed": changed,
            "v23_files": x, "v30_files": y,
            "ceiling": "Byte-level tabular catalog only, not runtime or physical bounds."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("v23_archive", type=Path)
    parser.add_argument("v30_archive", type=Path)
    args = parser.parse_args()
    print(json.dumps(compare(args.v23_archive, args.v30_archive), ensure_ascii=False, indent=2))
