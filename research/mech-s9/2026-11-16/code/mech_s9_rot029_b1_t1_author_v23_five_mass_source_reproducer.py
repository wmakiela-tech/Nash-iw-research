#!/usr/bin/env python3
"""ROT029, prereg c896351e: one and only authorized T1 original BlackHawk v2.3 experiment.
Source input: exact official archive, original Wu/Xu 3-file overlay, original reference table.
No Julia, no changed BlackHawk physical equations, no added masses or scanning.
Usage: python3 -I <script> <BH_directory> <reference.dat> <evidence_directory>
"""
from __future__ import annotations
import hashlib, json, math, pathlib, subprocess, sys, datetime, traceback, os

INDICES=(0,22,49,74,99)
CHANNELS=("pipm","Kpm","K0L","proton","neutron")
GROUP_CHANNELS=frozenset(("pipm","Kpm","proton","neutron"))
EPS=1e-5
ENERGY_MIN=5.0
ENERGY_MAX=1e5
ENERGY_COUNT=100
AUTHOR_REF_BLOB="06d0883a27b108692720422294ba2baacd381a64"
HBAR_IN_GEV_SECONDS=6.582119569e-25
TITLE="IW_MECH_S9_ROT029_T1_WUXU_SOURCE_BLACKHAWK_V23_FIVE_MASS_QB"

def git_sha(data:bytes)->str:
    h=hashlib.sha1()
    h.update(b"blob "+str(len(data)).encode("ascii")+b"\0"+data)
    return h.hexdigest()

def digest(path:pathlib.Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""):
            h.update(block)
    return h.hexdigest()

def original_table(path):
    data=path.read_bytes()
    assert git_sha(data)==AUTHOR_REF_BLOB,("original Wu-Xu source reference GIT blob mismatch",git_sha(data))
    lines=data.decode("utf-8").splitlines()
    assert lines[0].split("\t")==[
      "m_PBH [GeV]","charged_pion_dN_over_dt [GeV]",
      "charged_kaon_dN_over_dt [GeV]","kaon_zero_long_dN_over_dt [GeV]",
      "proton_dN_over_dt [GeV]","neutron_dN_over_dt [GeV]"],"author reference header mismatch"
    rows=[tuple(map(float,x.split())) for x in lines[1:] if x.strip()]
    assert len(rows)==100
    assert all(len(row)==6 and all(math.isfinite(x) and x>0 for x in row) for row in rows), "reference nonpositive/NaN"
    gram_to_gev=rows[0][0]/1e9
    assert 5.60958e23 < gram_to_gev <5.60960e23
    masses=[]
    for j in INDICES:
        mtab=rows[j][0]/gram_to_gev
        geom=1e9*math.exp(j*math.log(4000)/99)
        assert abs(mtab/geom-1) <= 1e-12,("source mass row not expected log-grid",j,mtab,geom)
        masses.append((j,mtab,rows[j]))
    return masses,gram_to_gev,digest(path)

def write_original_julia_params(name,mass,path):
    """Direct translation of original wrapper BlackHawkParameters(), 4 fixed changes."""
    v=[
     ("destination_folder",name),("full_output",1),
     ("interpolation_method",0),("metric",0),
     ("BH_number",1),("Mmin",format(mass,".17g")),
     ("Mmax",format(10*mass,".17g")),("param_number",1),
     ("amin",0.0),("amax",0.5),("Qmin",0.0),("Qmax",0.7),
     ("epsilon_LQG",1.5),("a0_LQG",0.0),("n",0),
     ("spectrum_choice",0),("spectrum_choice_param",0),
     ("amplitude_lognormal",1.0),("amplitude_lognormal2",1.0),
     ("stand_dev_lognormal",1.0),("crit_mass_lognormal",1.0),
     ("amplitude_powerlaw",1.0),("eqstate_powerlaw",1/3),
     ("amplitude_critical_collapse",1.0),("crit_mass_critical_collapse",1.0),
     ("amplitude_uniform",1.0),("stand_dev_param_Gaussian",1.0),
     ("mean_param_Gaussian",1.0),("table","spin_distribution_BH.txt"),
     ("tmin_manual",0),("tmin",1e-30),("limit",5000),
     ("BH_remnant",0),("M_remnant",1e-4),
     ("E_number",ENERGY_COUNT),("Emin",ENERGY_MIN),("Emax",ENERGY_MAX),
     ("grav",1),("add_DM",0),("m_DM",1.0),("spin_DM",0.0),("dof_DM",1.0),
     ("primary_only",0),("hadronization_choice",0)]
    assert len(v)==44 and len({k for k,_ in v})==len(v)
    path.write_text("".join(f"{k} = {value}\n" for k,value in v),encoding="ascii")
    return {k:value for k,value in v}

def parse_secondary(path):
    assert path.is_file(),("original secondary not produced",str(path))
    lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
    assert len(lines)>2, "empty secondary output"
    header=lines[1].split()
    assert header[0]=="energy/particle",("original header changed",header)
    assert len(header)==len(set(header))
    assert all(k in header for k in CHANNELS)
    data=[]
    for line in lines[2:]:
        if not line.strip():continue
        t=line.split()
        assert len(t)==len(header),("native output row width",len(t),header)
        a=list(map(float,t))
        assert all(math.isfinite(x) for x in a),"nonfinite native output"
        data.append(a)
    assert len(data)==ENERGY_COUNT,("unexpected source E_number",len(data))
    E=[x[0] for x in data]
    assert E[0]>0 and all(E[i]<E[i+1] for i in range(99))
    assert abs(E[0]/ENERGY_MIN-1) <= 1e-5
    assert abs(E[-1]/ENERGY_MAX-1) <= 1e-5
    # Source Julia notebook mean(diff(log(E))) with 100 printed BlackHawk values.
    delta=[math.log(E[i+1])-math.log(E[i]) for i in range(len(E)-1)]
    h=sum(delta)/len(delta)
    assert h>0
    out={}
    for k in CHANNELS:
        col=header.index(k)
        integrand=[E[i]*data[i][col] for i in range(ENERGY_COUNT)]
        assert all(x>=0 for x in integrand),(k,"negative source hadron spectrum")
        R_per_s=(h/2)*(2*sum(integrand)-integrand[0]-integrand[-1])
        R_in_GeV=R_per_s*HBAR_IN_GEV_SECONDS
        assert R_in_GeV>0 and math.isfinite(R_in_GeV),(k,R_in_GeV)
        out[k]={"integral_s_inverse":R_per_s,"rate_GeV":R_in_GeV}
    return out,{"header":header,"n_energies":len(E),"E_first_GeV":E[0],
                "E_last_GeV":E[-1],"mean_delta_logE":h,
                "original_output_SHA256":digest(path)}

def run():
    assert len(sys.argv)==4
    bh=pathlib.Path(sys.argv[1]).resolve()
    ref=pathlib.Path(sys.argv[2]).resolve()
    ev=pathlib.Path(sys.argv[3]).resolve()
    ev.mkdir(parents=True,exist_ok=True)
    status={"identity":TITLE,"prereg_commit":"c896351e537d79c401eee9a36a80cfac3a47f19d",
         "original_author_commit":"d395183674cace6c9906a8911bdeb7234ba4040d",
         "official_v23_SHA256":"dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7",
         "five_table_indices_0based":list(INDICES),
         "channels":list(CHANNELS),"epsilon":EPS,"results":[],
         "generator_original_author_BBN_PYTHIA_runs":0,
         "native_julia_runs":0,
         "verdict":"T1-NOREPRO","error":None}
    dest=ev/"T1_SOURCE_COMPARE_RESULT.json"
    try:
        masses,conversion,refsha=original_table(ref)
        status["reference_table_SHA256"]=refsha
        status["original_gram_to_GeV_from_first_reference_row"]=conversion
        csrc=bh/"src/include.h"
        source=csrc.read_text(errors="replace")
        assert "//#define HARDTABLES" in source and not any(
         x.strip()=="#define HARDTABLES" for x in source.splitlines()),"HARDTABLES selection changed"
        status["overlay_include_SHA256"]=digest(csrc)
        exe=bh/"BlackHawk_inst.x"
        assert exe.is_file() and os.access(exe,os.X_OK),"compiled exact original executable unavailable"
        status["compiled_original_executable_SHA256"]=digest(exe)
        for j,m,original in masses:
            name=f"t1_rot029_j{j:03d}"
            config_file=bh/(name+".in")
            assert not (bh/"results"/name).exists(),"source result collision; overwrite not allowed"
            write_original_julia_params(name,m,config_file)
            shutil_config=ev/(name+".in")
            shutil_config.write_bytes(config_file.read_bytes())
            outlog=ev/(name+"_BLACKHAWK_INST_STDOUT.txt")
            with outlog.open("wb") as log:
                p=subprocess.run(["./BlackHawk_inst.x",config_file.name],cwd=bh,
                 stdout=log,stderr=subprocess.STDOUT,timeout=900,check=False)
            status["generator_original_author_BBN_PYTHIA_runs"]+=1
            assert p.returncode==0,("BlackHawk native process failure",j,p.returncode)
            outfile=bh/"results"/name/"instantaneous_secondary_spectra.txt"
            model,meta=parse_secondary(outfile)
            (ev/(name+"_ORIGINAL_SECONDARY_SPECTRUM.txt")).write_bytes(outfile.read_bytes())
            original_rate=dict(zip(CHANNELS,original[1:]))
            ratios={k:model[k]["rate_GeV"]/original_rate[k] for k in CHANNELS}
            row={"j_0based":j,"mass_g":m,
                 "mass_source_geV":original[0],"params_SHA256":digest(config_file),
                 "native_log_SHA256":digest(outlog),"source_energy_meta":meta,
                 "channels":{k:{"R_author_GeV":original_rate[k],
                     "R_original_executable_GeV":model[k]["rate_GeV"],
                     "R_original_executable_per_second":model[k]["integral_s_inverse"],
                     "model_to_author_ratio":ratios[k],
                     "grouped_rel_mismatch":abs(ratios[k]-1),
                     "perstate_rel_mismatch":abs((ratios[k]/2 if k in GROUP_CHANNELS else ratios[k])-1)}
                     for k in CHANNELS}}
            status["results"].append(row)
        assert len(status["results"])==5
        group_errors=[v["grouped_rel_mismatch"] for row in status["results"]
            for v in row["channels"].values()]
        per_errors=[v["perstate_rel_mismatch"] for row in status["results"]
            for v in row["channels"].values()]
        status["max_grouped_rel_mismatch"]=max(group_errors)
        status["max_perstate_rel_mismatch"]=max(per_errors)
        status["all_25_strictly_positive"]=True
        grouped=max(group_errors)<=EPS
        perstate=max(per_errors)<=EPS
        assert not(grouped and perstate),"ambiguous multiple matching gates"
        status["verdict"]="T1-GROUPED" if grouped else ("T1-PERSTATE" if perstate else "T1-NOREPRO")
    except Exception as e:
        status["error"]={"type":type(e).__name__,"message":str(e),
                         "traceback":traceback.format_exc()[-2500:]}
        status["verdict"]="T1-NOREPRO"
    dest.write_text(json.dumps(status,indent=2,sort_keys=True,ensure_ascii=False)+"\n")
    print("T1_GENERATOR_RUNS",status["generator_original_author_BBN_PYTHIA_runs"],
          "T1_VERDICT",status["verdict"])
    if status["error"]:print("SOURCE_ERROR",status["error"]["message"])
    print("OUTPUT",str(dest))
    return 0

if __name__=="__main__":
    raise SystemExit(run())
