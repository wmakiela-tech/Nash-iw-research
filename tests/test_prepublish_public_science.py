"""End-to-end synthetic tests for the author-side pre-push gate."""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "scripts/prepublish_public_science.py"
GOOD = (
    "artifact_id: SYN_PUBLICATION_TEST\n"
    "exposure: PUBLIC\n"
    "claim_ceiling: TEST_ONLY_NO_EXEC\n"
    "sync_state: GITHUB_PENDING_BW_INGEST\n"
    "# Synthetic test source\n"
    + ("Assumptions, evidence, negative controls, and scope. " * 20)
)


class TestPublicPublicationGate(unittest.TestCase):
    def scenario(self, file_path: str, body: str):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=tmp, capture_output=True,
                    text=True, check=True,
                ).stdout.strip()

            git("init", "-q")
            git("config", "user.name", "Synthetic")
            git("config", "user.email", "test@example.invalid")
            (root / "README.md").write_text("baseline\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "baseline")
            base = git("rev-parse", "HEAD")
            full = root / file_path
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text(body, encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "candidate")
            head = git("rev-parse", "HEAD")
            return subprocess.run(
                [sys.executable, str(SOURCE), "--base", base, "--head", head],
                cwd=tmp, capture_output=True, text=True,
            )

    def test_valid_full_public_science_passes(self):
        result = self.scenario("research/test/2026-10-26/ok.md", GOOD)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS: PUBLICATION_PREFLIGHT", result.stdout)

    def test_missing_metadata_blocks_before_push(self):
        result = self.scenario(
            "research/test/2026-10-26/bad.md",
            GOOD.replace("sync_state:", "bw_event_or_pending:"),
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("BW_EVENT_OR_EXPLICIT_PENDING_REQUIRED", result.stdout)

    def test_provider_link_blocks_without_echoing_identifier(self):
        identifier = "Z" * 34
        link = "https://docs.google.com/document/d/" + identifier + "/edit"
        result = self.scenario(
            "research/test/2026-10-26/private_link.md", GOOD + "\n" + link,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("PRIVATE_PROVIDER_COORDINATE", result.stdout)
        self.assertNotIn(identifier, result.stdout + result.stderr)

    def test_unrelated_document_is_allowed(self):
        result = self.scenario("README_EXTRA.md", "Safe maintenance note\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
