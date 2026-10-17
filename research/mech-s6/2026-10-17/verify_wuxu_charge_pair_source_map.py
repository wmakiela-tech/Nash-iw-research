#!/usr/bin/env python3
"""Static verifier for the Mech-S6 Wu-Xu charge-pair comparator patch."""

from pathlib import Path
import importlib.util
import sys
import tempfile

THIS = Path(__file__).resolve()
PATCHER = THIS.with_name("apply_wuxu_charge_pair_source_map.py")

spec = importlib.util.spec_from_file_location("charge_patch", PATCHER)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

FIXTURE = """
header
    d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH
    d_n_K_dt_from_PBH = dN_over_dt_K(m_PBH) * n_PBH
    d_n_K⁰ᴸ_dt_from_PBH = dN_over_dt_K⁰ᴸ(m_PBH) * n_PBH
    d_n_proton_dt_from_PBH = dN_over_dt_proton(m_PBH) * n_PBH
    d_n_neutron_dt_from_PBH = dN_over_dt_neutron(m_PBH) * n_PBH
footer
""".lstrip()

out = mod.patch_text(FIXTURE)

assert "0.5 * dN_over_dt_π(m_PBH) * n_PBH" in out
assert "0.5 * dN_over_dt_K(m_PBH) * n_PBH" in out
assert "0.5 * dN_over_dt_proton(m_PBH) * n_PBH" in out
assert "0.5 * dN_over_dt_neutron(m_PBH) * n_PBH" in out
assert out.count("d_n_K⁰ᴸ_dt_from_PBH = dN_over_dt_K⁰ᴸ(m_PBH) * n_PBH") == 1

# Contract drift must fail closed.
try:
    mod.patch_text(FIXTURE.replace(
        "d_n_proton_dt_from_PBH = dN_over_dt_proton(m_PBH) * n_PBH",
        "d_n_proton_dt_from_PBH = some_other_source(m_PBH) * n_PBH",
    ))
except RuntimeError:
    pass
else:
    raise AssertionError("contract-drift test did not fail closed")

print("PASS: static comparator-patch verifier")
