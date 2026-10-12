"""Tests for the non-destructive public source-coordinate diff gate."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_public_locators import find_risks, inspect_patch


class PublicLocatorGuardTests(unittest.TestCase):
    def test_google_document_link(self):
        fake = "https://docs.google.com/" + "document/d/" + ("A" * 34) + "/edit"
        self.assertIn("google-drive-document-url", find_risks(fake))

    def test_google_drive_file_link(self):
        fake = "https://drive.google.com/" + "file/d/" + ("B" * 34) + "/view"
        self.assertIn("google-drive-document-url", find_risks(fake))

    def test_bare_drive_identifier(self):
        self.assertIn("bare-drive-reference", find_risks("Drive " + ("C" * 34)))

    def test_slack_thread_link(self):
        fake = "https://example.slack.com/" + "archives/C0ABCDEF/p1234567890123456"
        self.assertIn("slack-workspace-source-url", find_risks(fake))

    def test_safe_source_title(self):
        self.assertEqual([], find_risks("Source: MECH-S6 gate (private provenance in BW)"))

    def test_deleted_link_does_not_fail_new_diff(self):
        fake = "https://docs.google.com/" + "document/d/" + ("D" * 34) + "/edit"
        patch = "\n".join([
            "diff --git a/a.md b/a.md", "--- a/a.md", "+++ b/a.md",
            "@@ -1 +1 @@",
            "-Private old link " + fake, "+Source title only",
        ])
        self.assertEqual([], inspect_patch(patch))

    def test_added_link_fails_without_printing_identifier(self):
        fake = "https://drive.google.com/" + "file/d/" + ("E" * 34) + "/view"
        patch = "\n".join([
            "diff --git a/note.md b/note.md", "--- /dev/null",
            "+++ b/note.md", "@@ -0,0 +1 @@", "+" + fake,
        ])
        issues = inspect_patch(patch)
        self.assertEqual([("note.md", 1, "google-drive-document-url")], issues)
        self.assertNotIn("E" * 34, str(issues))

    def test_binary_extension_outside_scope(self):
        fake = "https://docs.google.com/" + "document/d/" + ("F" * 34)
        patch = "\n".join([
            "--- /dev/null", "+++ b/image.png", "@@ -0,0 +1 @@", "+" + fake,
        ])
        self.assertEqual([], inspect_patch(patch))


if __name__ == "__main__":
    unittest.main()
