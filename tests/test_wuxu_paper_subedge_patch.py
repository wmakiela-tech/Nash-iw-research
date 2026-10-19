from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
PATCHER = (
    REPO_ROOT
    / "research"
    / "mech-s6"
    / "2026-10-19"
    / "apply_wuxu_paper_subedge_law.py"
)

spec = importlib.util.spec_from_file_location("paper_subedge_patch", PATCHER)
patch = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(patch)

FIXTURE = """\
hadrons_from_PBH = readdlm("x")
dN_over_dt_π(m_PBH) = (GeV ∘ exp ∘ π_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)
dN_over_dt_K(m_PBH) = (GeV ∘ exp ∘ K_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)
dN_over_dt_K⁰ᴸ(m_PBH) = (GeV ∘ exp ∘ K⁰ᴸ_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)
dN_over_dt_proton(m_PBH) = (GeV ∘ exp ∘ proton_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)
dN_over_dt_neutron(m_PBH) = (GeV ∘ exp ∘ neutron_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)
"""


class PaperSubedgePatchTests(unittest.TestCase):
    def test_patch_renames_public_helpers_and_adds_wrappers(self) -> None:
        out = patch.patch_text(FIXTURE)
        for key, line in patch.PUBLIC.items():
            self.assertIn(line, out)
        self.assertIn("const _paper_source_exponent = -1.3", out)
        self.assertIn(
            "dN_over_dt_π(m_PBH) = _paper_subedge_rate",
            out,
        )
        self.assertIn(
            "dN_over_dt_neutron(m_PBH) = _paper_subedge_rate",
            out,
        )

    def test_contract_drift_fails_closed(self) -> None:
        drifted = FIXTURE.replace(
            "dN_over_dt_neutron(m_PBH) =",
            "dN_over_dt_neutron_CHANGED(m_PBH) =",
        )
        with self.assertRaises(RuntimeError):
            patch.patch_text(drifted)

    def test_idempotence_fails_closed(self) -> None:
        once = patch.patch_text(FIXTURE)
        with self.assertRaises(RuntimeError):
            patch.patch_text(once)


if __name__ == "__main__":
    unittest.main()
