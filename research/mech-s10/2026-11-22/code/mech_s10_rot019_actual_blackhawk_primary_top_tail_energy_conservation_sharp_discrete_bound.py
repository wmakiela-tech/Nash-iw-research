#!/usr/bin/env python3
"""Mech-S10 ROT019: ORIGINAL source-gzip primary top tail × energy-conservation
worst-case bound on missing Herwig7.1.5 E>70710.678 GeV top contribution.

Exact owner original Git blob inputs from a public repo:
  primary_spectra_090.tsv.gz: original 100 masses ×100 E points BlackHawk
  hadrons_099_Sa.dat: original frozen Sa 100 masses ×five hadrons
  fold_090.py: original meaning Phi[c] and trapezoid(E), HBAR
  build_tables_109.py: original 109 Sc uses 1/BIN_HW and high top clip
  analysis_109.py: exact top 100000 exclusion from pre-native G_MC
  run109_dev2.sh, PREREG109: original owner pre-native controls
NO Herwig/BlackHawk/Julia/PRyMordial PHYSICS simulated.

Bound on five species has assumption per PRIMARY n_h(E) ≤ E/m_h,
from per e+e- event energy sqrt(s)=2E and pair-to-primary 0.5;
same assumption for last-good clipped n(E_last) at E≥E_last.
Use deliberately CONSERVATIVE common m_h >= .1 GeV to avoid claiming
exact PDG hadron masses; all five hadrons (charged pion, K+, K0L,
proton, neutron) satisfy this. For any two permitted 0≤n_true,n_clip≤E/m0,
|n_true - n_clip|≤E/m0 (not twice the upper bound).
Thus discrete original fold source, species h at each owner mass j:
|Delta S_h| <= (1/BIN_HW) trapezoid(E, Phi_top(E;Mj) E/m0 1_{E>E_last})
and relative to positive exact ORIGINAL Sa_h = Sa.dat[j,h]/HBAR.

This is an upper bound on DISCRETIZED HADRON SOURCE under energy
conservation, **not** PBH beta root / helium Yp bound and NOT continuum
extrapolation bound. Requires original primary top flux nonnegative.
Only 4 grid nodes above last HERWIG7.1.5 top good E=70710.678.
It remains valid irrespective of unknown actual high-energy top
multiplicity shape, if the source model's energy bookkeeping is correct.
Record 0/underflow where present, not P-values.

Run from public repo root:
python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot019_actual_blackhawk_primary_top_tail_energy_conservation_sharp_discrete_bound.py OUT.json
"""
import csv
import gzip
import json
import math
from pathlib import Path
import subprocess
import sys

B=Path("research/badacz/2026-11-22")
D=Path("research/badacz/2026-11-21")
SOURCES={
    D/"data/primary_spectra_090.tsv.gz":"e2079be0b6dfab12a743c09e6937f1d2383d3a57",
    B/"data/hadrons_099_Sa.dat":"3aac28554204e6b6951a7472773535ad3c8613ea",
    D/"code/fold_090.py":"3392d1d088a4bdae869ecdc70bcd2081861ecf37",
    B/"code/build_tables_109.py":"fd231901b01602909974f77cdffd2af5053f8de6",
    B/"code/analysis_109.py":"c84d3a32603d96f08c4be4c3e8198772c9bf2e92",
    B/"code/run109_dev2.sh":"38c2b8ba2d21826893eff5198adb6353a6eb5a57",
    B/"IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_PREREG_109_20261122.md":"4cb85ea4b112780d588884361c4d076952d58dfa",
}
H=6.582119569e-25
BIN_HW=math.expm1(math.log(1e11)/99)/(math.log(1e11)/99)
E_LAST=70710.67811865475
M0=0.1
FIELDS=("pipm","Kpm","K0L","proton","neutron")
CHANNELS=("photon","gluons","higgs","Wpm","Z0","electron","muon","tau",
          "up","down","charm","strange","top","bottom")
def check_sources():
    for p,sha in SOURCES.items():
        assert p.is_file(),("ABSENT",str(p))
        got=subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
        assert sha==got,("SOURCE_SHA_CHANGED",str(p),got,sha)
    f=(D/"code/fold_090.py").read_text(encoding="utf-8")
    b=(B/"code/build_tables_109.py").read_text(encoding="utf-8")
    a=(B/"code/analysis_109.py").read_text(encoding="utf-8")
    assert 'HBAR = 6.582119569e-25' in f
    assert 'E = np.clip(E, Ei[0], Ei[-1])' in f
    assert 'Y[:, si] += np.trapezoid' in b
    assert '"/BIN_HW"' not in b # no source alteration
    assert '"Sc": fold_parts(n_py, n_hc, 12.5, BIN_PY, BIN_HW)' in b
    assert 'EXCL = {("top", 100000.0)}' in a

def trapezoid(xx,yy):
    assert len(xx)==len(yy)
    return sum((xx[i+1]-xx[i])*(yy[i]+yy[i+1])*.5 for i in range(len(xx)-1))

def primary_read():
    arr={}
    with gzip.open(D/"data/primary_spectra_090.tsv.gz",mode="rt",encoding="utf-8") as h:
        rd=csv.DictReader(h,delimiter="\t")
        pcol={c:("W+-" if c=="Wpm" else c) for c in CHANNELS}
        assert set(["k","m_g","energy",*pcol.values()]).issubset(rd.fieldnames),("HEAD",rd.fieldnames)
        for row in rd:
            k=int(row["k"])
            mm=float(row["m_g"])
            en=float(row["energy"])
            phi={c:float(row[pcol[c]]) for c in CHANNELS}
            assert 0<=k<100
            assert mm>0 and en>0 and all(math.isfinite(v) and v>=0 for v in phi.values())
            if k not in arr:arr[k]={"mass_g":mm,"energy":[],"phi":{c:[] for c in CHANNELS}}
            assert arr[k]["mass_g"]==mm
            arr[k]["energy"].append(en)
            for c in CHANNELS:arr[k]["phi"][c].append(phi[c])
    assert len(arr)==100 and all(len(q["energy"])==100 for q in arr.values())
    for k,a in arr.items():
        E=a["energy"]
        assert all(E[i]<E[i+1] for i in range(len(E)-1))
        assert abs(E[0]/5.-1)<1e-9 and abs(E[-1]/1e5-1)<1e-9
    return arr

def sa_read():
    d=[]
    with open(B/"data/hadrons_099_Sa.dat",encoding="utf-8") as f:
        header=f.readline()
        assert header.startswith("m_PBH")
        for line in f:
            if line.strip():
                t=[float(x) for x in line.split()]
                assert len(t)==6 and all(v>0 and math.isfinite(v) for v in t)
                d.append(t)
    assert len(d)==100
    return d

def main(out):
    check_sources()
    A=primary_read()
    Sa=sa_read()
    entries=[]
    for j in range(100):
        E=A[j]["energy"]
        flux=A[j]["phi"]
        assert abs(Sa[j][0]/(A[j]["mass_g"]*5.609588603804452e23)-1)<1e-10
        mask=[e>E_LAST for e in E]
        above=[i for i,q in enumerate(mask) if q]
        assert len(above)==4 and above==[96,97,98,99]
        ph=flux["top"]
        # Original discrete quadrature with mask applied to top source
        I_tail_E=trapezoid(E,[ph[i]*E[i] if mask[i] else 0 for i in range(100)])
        I_top_E=trapezoid(E,[ph[i]*E[i] for i in range(100)])
        I_total_E=trapezoid(E,[E[i]*sum(flux[c][i] for c in CHANNELS) for i in range(100)])
        I_top_num=trapezoid(E,ph)
        I_tail_num=trapezoid(E,[ph[i] if mask[i] else 0 for i in range(100)])
        assert I_total_E>0 and I_top_E>=I_tail_E>=0
        frac_energy_top=I_tail_E/I_top_E if I_top_E>0 else 0
        frac_energy_all=I_tail_E/I_total_E
        max_possible_delta_source=I_tail_E/(M0*BIN_HW)
        relative_bounds={FIELDS[h]:max_possible_delta_source/(Sa[j][h+1]/H)
                         for h in range(5)}
        assert all(math.isfinite(v) and v>=0 for v in relative_bounds.values())
        entries.append({
          "mass_grid_index":j,
          "physical_original_mass_grams":A[j]["mass_g"],
          "top_tail_energy_flux_integral_Egt70710":I_tail_E,
          "top_full_energy_flux_integral":I_top_E,
          "all_primary_full_energy_flux_integral":I_total_E,
          "top_tail_number_fraction_in_all_top_flux":I_tail_num/I_top_num if I_top_num>0 else 0,
          "top_tail_energy_fraction_in_all_top_energy_flux":frac_energy_top,
          "top_tail_energy_fraction_all_primary_energy":frac_energy_all,
          "source_energy_conservation_0p1GeV_common_hadron_floor_abs_bound":max_possible_delta_source,
          "relative_max_possible_source_change_per_hadron_against_original_Sa":relative_bounds,
          "no_claim_beta_root":True
        })
    # j22, j62 are ORIGINAL owner mass index IDs, not labels inferred
    key={j:entries[j] for j in (0,22,62,99)}
    global_max={s:max(entries,key=lambda e:e["relative_max_possible_source_change_per_hadron_against_original_Sa"][s]) for s in FIELDS}
    compact={s:{"index":v["mass_grid_index"],
                "value":v["relative_max_possible_source_change_per_hadron_against_original_Sa"][s]} for s,v in global_max.items()}
    # Conservative bound mathematically rooted in event energy;
    # no guarantee if MC multiplicities violate energy conservation
    result={
      "id":"IW_MECH_S10_ROT019_ORIGINAL_100x100_GZIP_TOP_TAIL_CONSERVATION_FOLD_BOUND",
      "owner_firstness":"Badacz original PRIMARY spectra 090 and 109 DEV2 source/table",
      "scientific_type":"ACTUAL_ORIGINAL_RAW_PRIMARY_GZIP_PARSED + EXACT_DISCRETE_CONSERVATIVE_ENERGY_CONSERVATION_BOUND, NOT NATIVE BBN",
      "sha_verified_original_source_git_blobs":{str(p):h for p,h in SOURCES.items()},
      "independent_original_gzip_source_nodes":10000,
      "source_mass_grid_points":100,
      "source_energy_grid_points":100,
      "top_tail_node_ids_zero_indexed":[96,97,98,99],
      "top_tail_cutoff_Eprim_GeV":E_LAST,
      "energy_event_conservation_mean_per_primary_assumption":
         "At sqrt(s)=2E the sum of energies of all produced hadrons is ≤2E. Per-primary pairing divide by 2, so any one hadron species multiplicity n_h(E)≤E/m_h. All five target hadrons have mass >=0.1GeV; use intentionally looser common m0=0.1GeV.",
      "unknown_top_endpoint_n_true_and_clipped_are_each_nonnegative_and_below_E_over_m0":True,
      "therefore_sharp_shared_event_budget_pointwise_difference_cap":
         "For 0<=n_true,n_clip<=E/m0, absolute difference<=E/m0; not 2E/m0",
      "BIN_HER":BIN_HW,
      "HBAR":H,
      "hadron_floor_GeV":M0,
      "j0_j22_j62_j99":{str(k):v for k,v in key.items()},
      "global_mass_max_source_relative_bounds":compact,
      "all_100_mass_source_derived_diagnostics":entries,
      "scope_limitations":[
        "The bound covers the exact 100-node trapezoidal discretized original source and one missing top channel, not the unknown physical continuum.",
        "The baseline Sa_h is an actual owner original 099 native table in units GeV; dividing by original HBAR converts to rate.",
        "No missing Herwig7.1.5 event generated; this bound does not assume any n_top(E) shape beyond nonnegativity and event energy conservation.",
        "Even a tiny source-relative bound cannot be promoted without a sensitivity/conditioning theorem into a bound on inverse beta root or helium Yp.",
        "This test does not settle the native 109 source if other channels failed, or owner 1 percent claim 106.",
        "Both true and clipped per-primary top hadron multiplicity must respect energy conservation; this is a model assumption, not a verified original 109 event-by-event check.",
        "The original source is a precomputed BlackHawk primary_spectra_090.tsv.gz; independent raw gzip directly ingested and original Git SHA gated, unlike prior ROT018."
      ],
      "no_native_physics_executed":True,
      "no_new_MC_generated":True,
      "NO_PBH_BOUND":True,"NO_NOVELTY":True,"NO_CANON":True,"NO_EXEC_SIGN":True
    }
    Path(out).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"sha_pins":len(SOURCES),"raw_gzip_nodes":10000,"j22":key[22],
                      "j62":key[62],"global_max":compact},indent=2,ensure_ascii=False))

if __name__=="__main__":
    assert len(sys.argv)==2,"Usage: python3 script.py output.json"
    main(sys.argv[1])
