#!/usr/bin/env python3
"""
Apply the Mech-S6 charge-pair source-map repair to Wu-Xu v2 main-scan.jl.

This script is intentionally narrow:
- it expects the exact four aggregate-source assignment lines used by the audited
  Wu-Xu v2 source;
- it multiplies those four aggregate columns by 1/2 before they enter tracked
  single-charge / single-antiparticle populations;
- it verifies that the K0L source assignment is present and leaves it unchanged;
- it refuses to run if the expected upstream contract is not found exactly once.

Scientific status:
implementation-ready comparator patch only; no BBN endpoint is computed here.
"""

from __future__ import annotations

import argparse
from pathlib import Path

EXPECTED = {
    "pi": "    d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH",
    "kpm": "    d_n_K_dt_from_PBH = dN_over_dt_K(m_PBH) * n_PBH",
    "k0l": "    d_n_K⁰ᴸ_dt_from_PBH = dN_over_dt_K⁰ᴸ(m_PBH) * n_PBH",
    "proton": "    d_n_proton_dt_from_PBH = dN_over_dt_proton(m_PBH) * n_PBH",
    "neutron": "    d_n_neutron_dt_from_PBH = dN_over_dt_neutron(m_PBH) * n_PBH",
}

REPAIRED = {
    "pi": "    d_n_π_dt_from_PBH = 0.5 * dN_over_dt_π(m_PBH) * n_PBH",
    "kpm": "    d_n_K_dt_from_PBH = 0.5 * dN_over_dt_K(m_PBH) * n_PBH",
    "proton": "    d_n_proton_dt_from_PBH = 0.5 * dN_over_dt_proton(m_PBH) * n_PBH",
    "neutron": "    d_n_neutron_dt_from_PBH = 0.5 * dN_over_dt_neutron(m_PBH) * n_PBH",
}


def require_exactly_once(text: str, needle: str, label: str) -> None:
    n = text.count(needle)
    if n != 1:
        raise RuntimeError(
            f"{label}: expected audited upstream line exactly once, found {n}. "
            "Refusing to patch a different/modified source contract."
        )


def patch_text(text: str) -> str:
    for key, line in EXPECTED.items():
        require_exactly_once(text, line, key)

    out = text
    for key in ("pi", "kpm", "proton", "neutron"):
        out = out.replace(EXPECTED[key], REPAIRED[key], 1)

    # K0L is intentionally unchanged.
    if out.count(EXPECTED["k0l"]) != 1:
        raise RuntimeError("K0L invariant failed: source assignment changed unexpectedly.")

    # Old affected assignments must be gone; repaired assignments must appear once.
    for key in ("pi", "kpm", "proton", "neutron"):
        if out.count(EXPECTED[key]) != 0:
            raise RuntimeError(f"{key}: old aggregate-to-single assignment survived patch.")
        if out.count(REPAIRED[key]) != 1:
            raise RuntimeError(f"{key}: repaired assignment missing or duplicated.")

    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path, help="audited Wu-Xu arXiv-2509.05618/main-scan.jl")
    ap.add_argument("output", type=Path, help="destination for comparator variant")
    args = ap.parse_args()

    src = args.input.read_text(encoding="utf-8")
    dst = patch_text(src)
    args.output.write_text(dst, encoding="utf-8")

    print("PASS: charge-pair source-map comparator patch applied.")
    print("Changed: pi± aggregate -> each pi charge: x0.5")
    print("Changed: K± aggregate -> K-: x0.5")
    print("Changed: p+pbar aggregate -> pbar: x0.5")
    print("Changed: n+nbar aggregate -> nbar: x0.5")
    print("Unchanged: K0L source")


if __name__ == "__main__":
    main()
