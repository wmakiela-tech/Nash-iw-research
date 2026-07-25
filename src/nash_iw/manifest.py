from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class ManifestError(ValueError):
    """Raised when a manifest is structurally invalid."""


REQUIRED_TOP_LEVEL = {"manifest_id", "status", "files", "boundaries"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ManifestError(f"Manifest not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ManifestError("Manifest root must be an object")
    return value


def validate_manifest(manifest_path: Path, repository_root: Path) -> list[str]:
    manifest = _load(manifest_path)
    errors: list[str] = []
    missing = sorted(REQUIRED_TOP_LEVEL - manifest.keys())
    if missing:
        errors.append("Missing top-level fields: " + ", ".join(missing))

    entries = manifest.get("files")
    if not isinstance(entries, list):
        errors.append("'files' must be a list")
        return errors

    root = repository_root.resolve()
    seen: set[str] = set()
    for index, entry in enumerate(entries):
        prefix = f"files[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} must be an object")
            continue
        rel = entry.get("path")
        expected = entry.get("sha256")
        role = entry.get("role")
        if not isinstance(rel, str) or not rel:
            errors.append(f"{prefix}.path must be a non-empty string")
            continue
        if rel in seen:
            errors.append(f"Duplicate file path: {rel}")
        seen.add(rel)
        if not isinstance(expected, str) or len(expected) != 64:
            errors.append(f"{prefix}.sha256 must be a 64-character hex digest")
            continue
        try:
            int(expected, 16)
        except ValueError:
            errors.append(f"{prefix}.sha256 is not hexadecimal")
            continue
        if not isinstance(role, str) or not role:
            errors.append(f"{prefix}.role must be a non-empty string")

        candidate = (root / rel).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            errors.append(f"{prefix}.path escapes repository root: {rel}")
            continue
        if not candidate.is_file():
            errors.append(f"Missing file: {rel}")
            continue
        actual = sha256_file(candidate)
        if actual != expected.lower():
            errors.append(f"Hash mismatch for {rel}: expected {expected.lower()}, got {actual}")

    boundaries = manifest.get("boundaries")
    if not isinstance(boundaries, list) or not all(isinstance(x, str) and x for x in boundaries):
        errors.append("'boundaries' must be a list of non-empty strings")
    return errors
