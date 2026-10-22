"""Bounded checksum gate; synthetic content only, no project-private data."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_drive_migration_batch import verify, _safe_relative_path


class MigrationIntegrityTests(unittest.TestCase):
    def _run(self, cases, existing=b"known export bytes"):
        with tempfile.TemporaryDirectory() as td:
            top = Path(td)
            checkout = top / "repo"
            checkout.mkdir()
            result = checkout / "science-private" / "a.md"
            result.parent.mkdir()
            result.write_bytes(existing)
            manifest = top / "inventory.jsonl"
            manifest.write_text("".join(json.dumps(item) + "\n" for item in cases))
            return verify(manifest, checkout)

    def test_export_hash_verified(self):
        data = b"known export bytes"
        x = {"source_id": "synthetic-1",
             "target_path": "science-private/a.md",
             "sha256": hashlib.sha256(data).hexdigest(),
             "status": "MIGRATED_VERIFIED"}
        y = self._run([x])
        self.assertEqual((y["verified"], y["failed"]), (1, 0))

    def test_pending_kept_distinct_from_verified(self):
        x = {"source_id": "synthetic-2", "status": "NOT_YET_EXPORTED"}
        y = self._run([x])
        self.assertEqual((y["pending"], y["verified"]), (1, 0))

    def test_mismatched_hash_blocks_completion(self):
        x = {"source_id": "synthetic-3",
             "target_path": "science-private/a.md",
             "sha256": "0" * 64,
             "status": "MIGRATED_VERIFIED"}
        y = self._run([x])
        self.assertEqual((y["failed"], y["verified"]), (1, 0))

    def test_duplicate_source_detected(self):
        items = [{"source_id": "synthetic-4", "status": "HOLD"},
                 {"source_id": "synthetic-4", "status": "HOLD"}]
        self.assertEqual(self._run(items)["duplicate_source"], 1)

    def test_unsafe_path_rejected(self):
        self.assertFalse(_safe_relative_path("../secret.txt"))
        self.assertFalse(_safe_relative_path("/etc/passwd"))
        self.assertTrue(_safe_relative_path("registry/bw/snapshots/2026-10-22/a.csv"))


if __name__ == "__main__":
    unittest.main()
