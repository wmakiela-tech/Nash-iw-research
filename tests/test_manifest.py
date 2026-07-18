from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from nash_iw.manifest import ManifestError, validate_manifest


class ManifestTests(unittest.TestCase):
    def test_valid_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifact = root / "artifact.txt"
            artifact.write_text("verified\n", encoding="utf-8")
            manifest = {"manifest_id":"TEST_001","status":"TEST_ONLY","files":[{"path":"artifact.txt","sha256":hashlib.sha256(artifact.read_bytes()).hexdigest(),"role":"fixture"}],"boundaries":["NO_EXEC_SIGN"]}
            path = root / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertEqual(validate_manifest(path, root), [])

    def test_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "artifact.txt").write_text("changed", encoding="utf-8")
            manifest = {"manifest_id":"TEST_002","status":"TEST_ONLY","files":[{"path":"artifact.txt","sha256":"0"*64,"role":"fixture"}],"boundaries":["NO_EXEC_SIGN"]}
            path = root / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertTrue(any("Hash mismatch" in e for e in validate_manifest(path, root)))

    def test_escape_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = {"manifest_id":"TEST_003","status":"TEST_ONLY","files":[{"path":"../outside.txt","sha256":"0"*64,"role":"fixture"}],"boundaries":["NO_EXEC_SIGN"]}
            path = root / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertTrue(any("escapes repository root" in e for e in validate_manifest(path, root)))

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "manifest.json"
            path.write_text("{", encoding="utf-8")
            with self.assertRaises(ManifestError): validate_manifest(path, root)


if __name__ == "__main__": unittest.main()
