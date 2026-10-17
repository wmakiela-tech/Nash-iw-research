from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
PATCHER = (
    REPO_ROOT
    / "research"
    / "mech-s6"
    / "2026-10-17"
    / "apply_wuxu_charge_pair_source_map.py"
)

spec = importlib.util.spec_from_file_location("wuxu_charge_pair_patch", PATCHER)
patch = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(patch)


FIXTURE = """\
header
    d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH
    d_n_K_dt_from_PBH = dN_over_dt_K(m_PBH) * n_PBH
    d_n_K⁰ᴸ_dt_from_PBH = dN_over_dt_K⁰ᴸ(m_PBH) * n_PBH
    d_n_proton_dt_from_PBH = dN_over_dt_proton(m_PBH) * n_PBH
    d_n_neutron_dt_from_PBH = dN_over_dt_neutron(m_PBH) * n_PBH
footer
"""


class WuXuChargePairPatchTests(unittest.TestCase):
    def test_expected_contract_is_patched_and_k0l_is_unchanged(self) -> None:
        out = patch.patch_text(FIXTURE)

        self.assertIn(
            "d_n_π_dt_from_PBH = 0.5 * dN_over_dt_π(m_PBH) * n_PBH", out
        )
        self.assertIn(
            "d_n_K_dt_from_PBH = 0.5 * dN_over_dt_K(m_PBH) * n_PBH", out
        )
        self.assertIn(
            "d_n_proton_dt_from_PBH = 0.5 * dN_over_dt_proton(m_PBH) * n_PBH",
            out,
        )
        self.assertIn(
            "d_n_neutron_dt_from_PBH = 0.5 * dN_over_dt_neutron(m_PBH) * n_PBH",
            out,
        )
        self.assertEqual(
            out.count(
                "d_n_K⁰ᴸ_dt_from_PBH = dN_over_dt_K⁰ᴸ(m_PBH) * n_PBH"
            ),
            1,
        )

    def test_upstream_contract_drift_fails_closed(self) -> None:
        drifted = FIXTURE.replace(
            "d_n_proton_dt_from_PBH = dN_over_dt_proton(m_PBH) * n_PBH",
            "d_n_proton_dt_from_PBH = other_source(m_PBH) * n_PBH",
        )
        with self.assertRaises(RuntimeError):
            patch.patch_text(drifted)


if __name__ == "__main__":
    unittest.main()
