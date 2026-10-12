"""No source identifiers or provider URLs are needed to test public science routing."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_public_science_writeback import validate_new_research

BASE = """---
artifact_id: TEST-SCIENCE-001
exposure: PUBLIC
bw_ingestion_event_id: ING-20261012-0001
archive_mode: PUBLIC_ARTIFACT
scientific_claim_ceiling: CONDITIONAL
---
# Test source
""" + ("Assumptions, calculations, limitations and an explicit falsifier. " * 12)


class PublicScienceWritebackTests(unittest.TestCase):
    def test_completed_public_result(self):
        self.assertEqual([], validate_new_research("research/example/2026-10-12/a.md", BASE))

    def test_pending_bw_is_legal_and_explicit(self):
        src = BASE.replace(
            "bw_ingestion_event_id: ING-20261012-0001",
            "sync_state: GITHUB_PENDING_BW_INGEST",
        )
        self.assertEqual([], validate_new_research("research/example/2026-10-12/a.md", src))

    def test_no_bw_link_is_a_failure(self):
        src = BASE.replace("bw_ingestion_event_id: ING-20261012-0001", "")
        self.assertIn("BW_EVENT_OR_EXPLICIT_PENDING_REQUIRED",
                      validate_new_research("research/example/2026-10-12/a.md", src))

    def test_private_exposure_fails_public_write(self):
        src = BASE.replace("exposure: PUBLIC", "exposure: PRIVATE")
        self.assertIn("PUBLIC_EXPOSURE_REQUIRED",
                      validate_new_research("research/example/2026-10-12/a.md", src))

    def test_pointer_is_not_a_scientific_body(self):
        src = BASE.replace("archive_mode: PUBLIC_ARTIFACT", "archive_mode: POINTER_ONLY")
        self.assertIn("PUBLIC_SCIENCE_BODY_NOT_POINTER",
                      validate_new_research("research/example/2026-10-12/a.md", src))

    def test_short_stub_not_completed_body(self):
        self.assertIn("SOURCE_BODY_TOO_SHORT_FOR_DEFAULT_PUBLIC_RESEARCH_ARTIFACT",
                      validate_new_research("research/example/2026-10-12/a.md", BASE[:150]))

    def test_existing_non_research_outside_scope(self):
        self.assertEqual([], validate_new_research("docs/operator.md", "PRIVATE"))


if __name__ == "__main__":
    unittest.main()
