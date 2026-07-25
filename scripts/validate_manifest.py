from __future__ import annotations

import argparse
import json
from pathlib import Path
from nash_iw.manifest import ManifestError, validate_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate NASH/IW manifest hashes")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        errors = validate_manifest(args.manifest, args.root)
    except ManifestError as exc:
        errors = [str(exc)]
    result = {"status": "PASS" if not errors else "FAIL", "errors": errors, "exec_sign": False, "canon_merge": False}
    if args.as_json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result["status"])
        for error in errors: print(f"- {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
