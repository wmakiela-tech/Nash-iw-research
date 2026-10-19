#!/usr/bin/env python3
"""
Patch Wu-Xu v2 hadron source helper to implement the paper-declared
sub-edge law Q_h(M)=Q_h(M0)*(M/M0)^(-1.3) below the first table mass M0.

Above/at M0 the original public helper is retained exactly.

Fail-closed: audited source lines must appear exactly once.
"""

from __future__ import annotations
import argparse
from pathlib import Path

LINES = {
    "pi": "dN_over_dt_π(m_PBH) = (GeV ∘ exp ∘ π_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)",
    "K": "dN_over_dt_K(m_PBH) = (GeV ∘ exp ∘ K_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)",
    "K0L": "dN_over_dt_K⁰ᴸ(m_PBH) = (GeV ∘ exp ∘ K⁰ᴸ_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)",
    "p": "dN_over_dt_proton(m_PBH) = (GeV ∘ exp ∘ proton_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)",
    "n": "dN_over_dt_neutron(m_PBH) = (GeV ∘ exp ∘ neutron_from_PBH_interpolation ∘ log ∘ EUval)(GeV, m_PBH)",
}

PUBLIC = {
    key: line.replace("dN_over_dt_", "_public_dN_over_dt_", 1)
    for key, line in LINES.items()
}

WRAPPERS = r'''
const _paper_source_edge_mass_GeV = hadrons_from_PBH[1, 1]
const _paper_source_exponent = -1.3

function _paper_subedge_rate(m_PBH, edge_rate, public_fun)
    m_GeV = EUval(GeV, m_PBH)
    if m_GeV < _paper_source_edge_mass_GeV
        return GeV(edge_rate * (m_GeV / _paper_source_edge_mass_GeV)^(_paper_source_exponent))
    end
    return public_fun(m_PBH)
end

dN_over_dt_π(m_PBH) = _paper_subedge_rate(m_PBH, hadrons_from_PBH[1, 2], _public_dN_over_dt_π)
dN_over_dt_K(m_PBH) = _paper_subedge_rate(m_PBH, hadrons_from_PBH[1, 3], _public_dN_over_dt_K)
dN_over_dt_K⁰ᴸ(m_PBH) = _paper_subedge_rate(m_PBH, hadrons_from_PBH[1, 4], _public_dN_over_dt_K⁰ᴸ)
dN_over_dt_proton(m_PBH) = _paper_subedge_rate(m_PBH, hadrons_from_PBH[1, 5], _public_dN_over_dt_proton)
dN_over_dt_neutron(m_PBH) = _paper_subedge_rate(m_PBH, hadrons_from_PBH[1, 6], _public_dN_over_dt_neutron)
'''.lstrip()


def patch_text(text: str) -> str:
    out = text
    for key, line in LINES.items():
        n = out.count(line)
        if n != 1:
            raise RuntimeError(f"{key}: expected audited helper definition once, found {n}")
        out = out.replace(line, PUBLIC[key], 1)

    if "_paper_subedge_rate(" in text:
        raise RuntimeError("paper subedge patch appears already present")

    out = out.rstrip() + "\n\n" + WRAPPERS
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()

    src = args.input.read_text(encoding="utf-8")
    dst = patch_text(src)
    args.output.write_text(dst, encoding="utf-8")

    print("PASS: paper M^-1.3 sub-edge helper patch applied.")
    print("Above/at first table mass: original helper retained.")
    print("Below first table mass: each species anchored to its edge value with exponent -1.3.")


if __name__ == "__main__":
    main()
