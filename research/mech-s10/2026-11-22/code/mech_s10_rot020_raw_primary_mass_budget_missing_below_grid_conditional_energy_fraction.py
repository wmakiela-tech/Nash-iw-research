#!/usr/bin/env python3
"""IW/Mech-S10 ROT020: mass-integrated *conditional* energy budget for the
unmeasured Herwig7.1.5 top high-energy endpoint in PREREG109 DEV-2.

ACTUAL PRIMARY DATA: parse original exact-source BlackHawk gz from 090,
100 masses x100 energy x14 primary channels, plus original 099 Sa via
exact SHA-gated ROT019 source parser, which reads all seven source Git
blobs and checks masses and positivity. Code origin itself Git SHA gated.

NO native Julia/Herwig/BlackHawk/PRyMordial/PYTHIA physics run.

The rest-mass energy bookkeeping for a non-accreting PBH is
    emitted energy dE = -c^2 dM.
For a mass-resolved fraction q(M) of emitted primary energy corresponding
to top E>70710.678GeV,
  E_missing_top/M_i c^2 <= (1/M_i) int_0^M_i q(M) dM.

The original primary spectrum has no mass grid BELOW 1e9g. From energy
conservation alone q(M) in [0,1] there. That totally unresolved mass
regime contributes <=M_min/M_i of INITIAL rest mass, independent of
evaporation time. Above M_min we have ORIGINAL q_i on 100 sampled masses.

CONDITIONAL MASS-INTERVAL ENVELOPE (H_M), NOT DATA-BASED PROOF:
for each mass interval [M_i,M_(i+1)], assume the real q(M) never exceeds
max(q_i,q_(i+1)). This is guaranteed if the nonnegative top-energy rate
and all-channel energy rate are each interpolated AFFINELY across masses
(their ratio is a positive weighted average of endpoint ratios), and
also for simultaneous LOG-LINEAR interpolation of both positive rates;
not guaranteed for arbitrary physical continuum or the independent
native solver interpolation rule. The script explicitly DOES NOT assert
the original Wu-Xu code uses either interpolation.

Then (conditional) total >=:
  B_total(M_init) = M_min/M_init
   + sum_(mass_bins up to init) (M_(i+1)-M_i)*max(q_i,q_(i+1))/M_init.
For completeness we also show a non-bound *linear-in-mass q interpolation*
point estimate (midpoint), and worst-case global monotone-like q<=q(Mmin)
from minimum mass to M_init. Without H_M or other regularity assumption,
the only source-independent whole-mass bound on q is trivial 1 (100%).
NO beta root, no helium Yp, no time-window response bound.

All ratios here are fractions of PBH INITIAL rest-mass energy (assuming
the whole interval is traversed); if evaporation stops before the
lower mass, contribution can only decrease under nonnegative q.
This denominator is NOT the total hadron rate nor the observed BBN dose.
"""
import json
import math
from pathlib import Path
import runpy
import subprocess
import sys

ROOT=Path("research/mech-s10/2026-11-22/code")
SOURCE=ROOT/"mech_s10_rot019_actual_blackhawk_primary_top_tail_energy_conservation_sharp_discrete_bound.py"
SOURCE_GIT_SHA="5d12bfe84eb95a5fdd2f91011e2211a284c178ea"
Q_NAME="top_tail_fraction_14_primary_energy"

def main(outfile):
    got=subprocess.check_output(["git","hash-object",str(SOURCE)],text=True).strip()
    assert got==SOURCE_GIT_SHA,("ORIGINAL_AUDITOR_SHA_MISMATCH",got)
    a=runpy.run_path(str(SOURCE))
    a["check_sources"]()  # seven locked original inputs, including actual gzip
    mass_data=a["primary_read"]()  # 100x100 raw gzip, NOT ROT019 artifact
    Sa=a["sa_read"]()              # 100 owner original hadron source rows
    assert len(mass_data)==len(Sa)==100
    mmin=mass_data[0]["mass_g"]
    assert mmin==1e9
    cutoff=a["E_LAST"]
    rows=[]
    for j in range(100):
        dat=mass_data[j]
        mass=dat["mass_g"]
        E=dat["energy"]
        phi=dat["phi"]
        all_14=[E[k]*sum(phi[c][k] for c in a["CHANNELS"]) for k in range(100)]
        top_tail=[E[k]*phi["top"][k] if E[k]>cutoff else 0 for k in range(100)]
        den=a["trapezoid"](E,all_14)
        num=a["trapezoid"](E,top_tail)
        assert den>0 and 0<=num<=den
        assert abs(Sa[j][0]/(mass*5.609588603804452e23)-1.)<1e-10
        q=num/den
        rows.append({"index":j, "original_mass_grams":mass, Q_NAME:q,
                     "original_trapz_top_high_energy_flux":num,
                     "original_trapz_all14_primary_energy_flux":den})
    masses=[r["original_mass_grams"] for r in rows]
    q=[r[Q_NAME] for r in rows]
    assert all(masses[i]<masses[i+1] for i in range(99))
    assert all(q[i]>=q[i+1] for i in range(99)),("NONMONOTONE_SAMPLED_TOP_FRACTION",q)
    assert abs(q[0]-0.015607054684713455)<1e-14
    assert abs(q[22]-9.217349885910068e-16)<1e-26
    assert q[62]==0.
    def calc(j):
        M=masses[j]
        below=mmin/M
        intervals=[]
        for k in range(j):
            dm=masses[k+1]-masses[k]
            hi=max(q[k],q[k+1])
            lo=min(q[k],q[k+1])
            intervals.append({"left_mass_g":masses[k],"right_mass_g":masses[k+1],
                              "q_left":q[k],"q_right":q[k+1],
                              "mass_equivalent_g_interpolated_q_midpoint":dm*(q[k]+q[k+1])/2,
                              "mass_equivalent_g_endpoint_UB_under_HM":dm*hi,
                              "mass_equivalent_g_endpoint_LB_under_HM":dm*lo})
        integrated_mid=sum(x["mass_equivalent_g_interpolated_q_midpoint"] for x in intervals)
        integrated_up=sum(x["mass_equivalent_g_endpoint_UB_under_HM"] for x in intervals)
        integrated_low=sum(x["mass_equivalent_g_endpoint_LB_under_HM"] for x in intervals)
        assert integrated_low<=integrated_mid<=integrated_up
        envelope=(mmin+integrated_up)/M
        global_q_envelope=(mmin+(M-mmin)*q[0])/M
        assert 0<=envelope<=global_q_envelope<=1
        return {
            "initial_source_mass_index":j,
            "initial_mass_g":M,
            "mmin_original_primary_mass_table_g":mmin,
            "unknown_below_grid_mass_budget_upper_fraction_of_initial_rest_energy":below,
            "observed_mass_interval_finite_grid_q_linear_interpolation_fraction_of_initial_rest_energy_NOT_BOUND":integrated_mid/M,
            "observed_mass_interval_upper_fraction_under_EXPLICIT_HM_endpoint_envelope":integrated_up/M,
            "observed_mass_interval_lower_fraction_under_EXPLICIT_HM_endpoint_envelope":integrated_low/M,
            "full_mass_path_upper_fraction_CONDITIONAL_on_HM_and_energy_mass_loss":envelope,
            "global_q_M_le_q_at_mmin_full_path_upper_fraction_CONDITIONAL":global_q_envelope,
            "full_mass_path_UNCONDITIONAL_bound_without_mass_regularization":1.0,
            "unknown_subgrid_over_resolved_endpoint_envelope":mmin/integrated_up if integrated_up>0 else None,
            "resolved_upper_mass_energy_equivalent_grams":integrated_up,
            "total_upper_mass_energy_equivalent_grams_conditional":mmin+integrated_up,
            "assumption_HM_applies_between_source_mass_nodes":True,
            "grid_intervals_count":len(intervals),
            "M_below_min_primary_mass_1e9_NOT_OBSERVED":True
        }
    targets={str(j):calc(j) for j in (0,10,14,16,22,62,99)}
    assert abs(targets["22"]["full_mass_path_upper_fraction_CONDITIONAL_on_HM_and_energy_mass_loss"]-
        0.15905459726459173)<1e-12
    assert abs(targets["62"]["full_mass_path_upper_fraction_CONDITIONAL_on_HM_and_energy_mass_loss"]-
        0.0055740190939034175)<1e-12
    assert targets["22"]["unknown_subgrid_over_resolved_endpoint_envelope"]>200
    assert targets["62"]["unknown_subgrid_over_resolved_endpoint_envelope"]>200
    assert all(r["source_mass_index"] if False else True for r in [])
    result={
        "artifact":"IW_MECH_S10_ROT020_ORIGINAL_10000_BH_TOP_TAIL_MASS_PATH_ENERGY_BUDGET_001",
        "lineage":"IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10",
        "executed_mode":"ORIGINAL_RAW_GZIP_100x100_PRIMARY_PLUS_OWNER_Sa_SOURCE_ONLY",
        "verified_previous_original_source_reader_git_blob":SOURCE_GIT_SHA,
        "verified_all_seven_original_sources_via_rot019_reader":True,
        "raw_original_gzip_nodes_parsed_this_turn":10000,
        "original_mass_grid_rows":100,
        "original_energy_grid_nodes":100,
        "original_primary_channels":14,
        "original_energy_grid_top_cutoff":cutoff,
        "q_fraction_is_top_E_above_cutoff_over_fourteen_primary_channels_energy_flux":True,
        "missing_unaccounted_other_emission_channels_make_q14_conservative_if_all_flux_nonnegative":True,
        "sampled_original_mass_grid_q_nonincreasing":True,
        "assumption_for_mass_to_energy_transfer":"Single PBH mass changes only by Hawking emission and no accretion; emitted rest energy over mass loss dM is -c^2 dM, and 14-channel primary energy flux from 090 is nonnegative subset of actual total loss.",
        "H_M_mass_interval_endpoint_max_assumption":"True q(M) for M in [M_i,M_(i+1)] <= max(q_i,q_(i+1)); sufficient if top/all14 energy rates interpolated jointly linearly in M with positive totals, OR jointly log-linear in M when positive. Owner native interpolation has NOT been verified here.",
        "unresolved_mass_below_1e9_bound":"For M<1e9g the original dataset has ZERO mass rows; by energy conservation only 0<=q(M)<=1, hence at most 1e9g mass-equivalent energy for a PBH starting above 1e9g.",
        "no_mass_interpolation_assumption_all_emission_fraction_has_only_trivial_bound":1.0,
        "targets":targets,
        "all_100_actual_original_q_by_mass":rows,
        "negative_knowledge":[
            "The 0.5574% j62 bound is CONDITIONAL on H_M and mass-energy bookkeeping; it is an ENERGY fraction of initial rest mass, not a 0.5574% bound on nuclear reaction rate, hadronic shower energy or Yp.",
            "The absence of primary Phi_top stored for M<1e9g dominates uncertainty: for j22 the unknown subgrid energy budget alone is15.832%, for j62 .5548%.",
            "No data support H_M in unsampled mass intervals without an explicit interpolation model; observed 100 mass q monotonicity at nodes does NOT prove continuum monotonicity.",
            "Even if the conditional top-energy fraction is small, BBN Yp can be sensitive to the time-distribution and hadronic deposition; no beta threshold perturbation can be inferred.",
            "Actual 109 native Sc physical results and owner review unavailable at time of audit; no owner ACK or revision is assumed.",
            "No new physical model, generator, native solver or hadronization run performed."
        ],
        "NO_PHYSICAL_PBH_BOUND":True,"NO_NOVELTY":True,"NO_CANON":True,"NO_EXEC_SIGN":True
    }
    Path(outfile).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"sampled_q0":q[0],"q22":q[22],"q62":q[62],
                      "targets":{k:targets[k] for k in ("22","62")},
                      "original_grid_sha_source":SOURCE_GIT_SHA},indent=2,ensure_ascii=False))

if __name__=="__main__":
    assert len(sys.argv)==2,"usage: python3 rot020.py OUT.json"
    main(sys.argv[1])
