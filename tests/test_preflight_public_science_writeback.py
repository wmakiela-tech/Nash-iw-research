"""Synthetic coverage of author-side preflight and the added-only blind spot."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))
from preflight_public_science_writeback import preflight_path, changed_paths
from check_public_science_writeback import added_research_paths

FILE = "research/test/2026-10-25/source.md"
GOOD = (
    "artifact_id: SYN_TEST_ARTIFACT\n"
    "exposure: PUBLIC\n"
    "claim_ceiling: SOURCE_ONLY_NO_EXEC\n"
    "sync_state: GITHUB_PENDING_BW_INGEST\n"
    "# Full synthetic source\n"
    + "a source with reproducible details and scope guards.\n" * 18
)


class TestPreflight(unittest.TestCase):
    def test_valid_pending(self):
        self.assertEqual(preflight_path(FILE, GOOD), [])

    def test_valid_actual_ing(self):
        self.assertEqual(preflight_path(FILE, GOOD.replace(
            "sync_state: GITHUB_PENDING_BW_INGEST",
            "bw_ingestion_event_id: ING-20261025-0042")), [])

    def test_exposure(self):
        bad = preflight_path(FILE, GOOD.replace("exposure: PUBLIC", "exposure: PUBLIC_SAFE"))
        self.assertIn("PUBLIC_EXPOSURE_REQUIRED", bad)

    def test_legacy_bw_field(self):
        bad = preflight_path(FILE, GOOD.replace("sync_state:", "bw_event_or_pending:"))
        self.assertIn("BW_EVENT_OR_EXPLICIT_PENDING_REQUIRED", bad)

    def test_legacy_headers(self):
        bad = GOOD.replace("artifact_id: SYN_TEST_ARTIFACT", "RETURN_ID: SYN_TEST_ARTIFACT")
        bad = bad.replace("claim_ceiling: SOURCE_ONLY_NO_EXEC", "CEILING SOURCE_ONLY_NO_EXEC")
        violations = preflight_path(FILE, bad)
        self.assertIn("ARTIFACT_ID_REQUIRED", violations)
        self.assertIn("CLAIM_CEILING_REQUIRED", violations)

    def test_pointer(self):
        self.assertIn("PUBLIC_SCIENCE_BODY_NOT_POINTER", preflight_path(
            FILE, GOOD + "archive_mode: POINTER_ONLY\n"))

    def test_short(self):
        self.assertIn("SOURCE_BODY_TOO_SHORT_FOR_DEFAULT_PUBLIC_RESEARCH_ARTIFACT",
                      preflight_path(FILE, GOOD[:120]))

    def test_malformed_path(self):
        self.assertEqual(preflight_path("research/../secrets.txt", GOOD),
                         ["NOT_RESEARCH_TEXT_PATH"])

    def test_modified_diff_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "research/test/2026-10-25").mkdir(parents=True)
            filename = root / FILE
            filename.write_text(GOOD, encoding="utf-8")

            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=tmp,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    text=True, check=True).stdout.strip()

            git("init", "-q")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            git("add", ".")
            git("commit", "-q", "-m", "good")
            base = git("rev-parse", "HEAD")
            filename.write_text(GOOD.replace("sync_state:", "bw_event_or_pending:"),
                                encoding="utf-8")
            git("add", ".")
            git("commit", "-q", "-m", "broken modified document")
            head = git("rev-parse", "HEAD")
            previous_cwd = Path.cwd()
            os.chdir(tmp)
            try:
                self.assertEqual(added_research_paths(base, head), [])
                self.assertEqual(changed_paths(base, head), [FILE])
                result = subprocess.run(
                    [sys.executable,
                     str(BASE / "scripts/preflight_public_science_writeback.py"),
                     "--base", base, "--head", head],
                    capture_output=True, text=True)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("BW_EVENT_OR_EXPLICIT_PENDING_REQUIRED", result.stdout)
            finally:
                os.chdir(previous_cwd)

    def test_direct_path_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "research/test/2026-10-25"
            root.mkdir(parents=True)
            (root / "source.md").write_text(GOOD, encoding="utf-8")
            result = subprocess.run(
                [sys.executable,
                 str(BASE / "scripts/preflight_public_science_writeback.py"), FILE],
                cwd=tmp, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_no_input(self):
        result = subprocess.run(
            [sys.executable, str(BASE / "scripts/preflight_public_science_writeback.py")],
            capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
