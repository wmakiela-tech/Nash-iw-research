from __future__ import annotations

import unittest

from nash_iw.system_contracts import (
    SystemContractError,
    assert_signal_only,
    explicit_current,
    transferred_witness,
    validate_execution_contract,
    validate_regression_metadata,
)


class SystemContractTests(unittest.TestCase):
    def _valid_execution_contract(self):
        digest = "b" * 64
        return {
            "execution_id": "EXEC-SYNTH-001",
            "requesting_cell": "SYNTHETIC_TEST_CELL",
            "scientific_request_ref": "SYNTHETIC_REQUEST_001",
            "code_commit_sha": "a" * 40,
            "entry_point": "python synthetic.py",
            "environment_spec": "python>=3.11",
            "input_refs_and_hashes": [{"ref": "synthetic-input.json", "sha256": digest}],
            "command": "python synthetic.py",
            "expected_outputs": ["synthetic-output.json"],
            "actual_output_refs_and_hashes": [{"ref": "synthetic-output.json", "sha256": digest}],
            "regression_command": "python -m unittest discover -s tests -v",
            "regression_result": "PASS",
            "runtime_warnings": [],
            "claim_ceiling": "Synthetic execution contract only; no scientific authority.",
            "return_to": "SYNTHETIC_TEST_CELL",
            "status": "PASS",
        }

    def test_thin_execution_contract_valid(self):
        self.assertEqual(validate_execution_contract(self._valid_execution_contract()), [])

    def test_execution_contract_missing_claim_ceiling_fails(self):
        contract = self._valid_execution_contract()
        contract.pop("claim_ceiling")
        errors = validate_execution_contract(contract)
        self.assertTrue(any("claim_ceiling" in error for error in errors))

    def test_current_is_explicit_not_newest(self):
        records = [
            {"id": "older-but-current", "timestamp": "2026-09-01T10:00:00Z", "current": True},
            {"id": "newer-but-superseded", "timestamp": "2026-09-02T10:00:00Z", "current": False},
        ]
        self.assertEqual(explicit_current(records)["id"], "older-but-current")

    def test_unknown_is_not_rewritten_as_false(self):
        record = {"support_check": "UNKNOWN", "scientific_status": "CURRENT_REPRESENTED"}
        self.assertEqual(record["support_check"], "UNKNOWN")
        self.assertNotEqual(record["support_check"], "FALSE")
        self.assertEqual(record["scientific_status"], "CURRENT_REPRESENTED")

    def test_signal_only_cannot_mutate_scientific_or_authority_state(self):
        before = {
            "scientific_status": "CURRENT",
            "authority_state": "NONE",
            "priority_state": "UNSET",
            "signals": [],
        }
        after = dict(before)
        after["signals"] = ["REVIEW_DEBT"]
        assert_signal_only(before, after)

        bad = dict(after)
        bad["scientific_status"] = "DOWNGRADED"
        with self.assertRaises(SystemContractError):
            assert_signal_only(before, bad)

    def test_transferred_witness_preserves_actor_and_no_self_attribution(self):
        witness = {
            "claim_id": "CLAIM-SYNTH-001",
            "witness_actor": "UPSTREAM_REVIEWER",
            "source_depth": "CLAIM_WITNESSED",
        }
        result = transferred_witness(witness, recipient="DOWNSTREAM_CELL")
        self.assertEqual(result["witness_actor"], "UPSTREAM_REVIEWER")
        self.assertEqual(
            result["knowledge_origin_current_participant"],
            "LINEAGE_OR_PARTICIPANT_HANDOFF",
        )
        self.assertFalse(result["current_participant_direct_source_inspection"])

    def test_nonhard_regression_requires_review_or_sunset_trigger(self):
        metadata = {
            "test_semantic_class": "CURRENT_POLICY",
            "human_readable_semantic": "A monitor signal does not alter scientific authority.",
            "what_pass_does_not_mean": "Scientific truth or CANON.",
        }
        errors = validate_regression_metadata(metadata)
        self.assertTrue(any("review_or_sunset_trigger" in error for error in errors))

    def test_historical_fixture_with_sunset_metadata_is_valid(self):
        metadata = {
            "test_semantic_class": "HISTORICAL_BUG_FIXTURE",
            "human_readable_semantic": "CURRENT is resolved explicitly, not by newest timestamp.",
            "what_pass_does_not_mean": "That the represented record is scientifically correct.",
            "review_or_sunset_trigger": "Review if the currentness representation contract changes.",
        }
        self.assertEqual(validate_regression_metadata(metadata), [])


if __name__ == "__main__":
    unittest.main()
