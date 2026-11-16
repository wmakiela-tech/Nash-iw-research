#!/usr/bin/env python3
"""Approved T1 five-mass exact source replay; original Wu-Xu/BlackHawk v2.3."""
import os,sys,pathlib,hashlib,subprocess,tarfile,tempfile,urllib.request,time,math,json,statistics
assert len(sys.argv)==4
arc=pathlib.Path(sys.argv[1]).resolve();out=pathlib.Path(sys.argv[2]).resolve();ref=pathlib.Path(sys.argv[3]).resolve();out.mkdir(exist_ok=True,parents=True)
V23="dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7"
WU="d395183674cace6c9906a8911bdeb7234ba4040d"
REFBLOB="06d0883a27b108692720422294ba2baacd381a64"
PATCH={"BlackHawk_inst.c":"f517b0a71a3c994e396600ce73cb9658e440d646","BlackHawk_tot.c":"76758e05a71688b94979b326723d02dbdf630dc5","src/include.h":"3a1eaefd6d884c864056ea45233513493794ee7e"}
CH=("pipm","Kpm","K0L","proton","neutron")
IX=(0,22,49,74,99)
HBAR=6.582119569e-25
def sha(b):return hashlib.sha256(b).hexdigest()
def fh(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return h.hexdigest()
def git(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def write(p,b):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def cmd(args,cwd,log,timeout=400):
 t=time.time()
 with log.open("wb") as f:
  f.write((repr(args)+"\n").encode());f.flush()
  try:p=subprocess.run(args,cwd=cwd,stdout=f,stderr=subprocess.STDOUT,timeout=timeout)
  except subprocess.TimeoutExpired:raise RuntimeError("Timed out, see "+str(log))
  f.write(("\nEXIT="+str(p.returncode)+" seconds="+str(time.time()-t)+"\n").encode())
 if p.returncode:raise RuntimeError("Original C tool error; see "+str(log))
 return time.time()-t
def fetch(path,expect):
 url=f"https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/{WU}/arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/{path}"
 with urllib.request.urlopen(url,timeout=70) as f:b=f.read()
 assert git(b)==expect,("original overlay Git blob mismatch",path)
 return b
assert arc.stat().st_size==161495983 and fh(arc)==V23,"FAIL_ORIGINAL_ARCHIVE_SHA"
rb=ref.read_bytes()
assert git(rb)==REFBLOB,"FAIL_AUTHOR_REFERENCE_BLOB"
lines=rb.decode().strip().splitlines()
assert len(lines)==101
table=[list(map(float,z.split())) for z in lines[1:]]
assert all(len(x)==6 and all(v>0 for v in x) for x in table)
print("T1_ORIGINAL_V23_AND_REFERENCE_AUTHENTICATED",flush=True)
with tempfile.TemporaryDirectory(prefix="t1_wuxu_") as td:
 tmp=pathlib.Path(td)
 with tarfile.open(arc,"r:bz2") as f:
  members=f.getmembers()
  assert len(members)>300
  for x in members:
   assert not x.name.startswith("/") and ".." not in pathlib.PurePosixPath(x.name).parts
  f.extractall(tmp)
 root=tmp/"blackhawk_v2.3"
 assert root.is_dir()
 build={"original_tar_SHA256":V23,"reference_gitblob":REFBLOB,"author_git_ref":WU,"patches":{},"compile":[]}
 for path,blob in PATCH.items():
  data=fetch(path,blob);write(root/pathlib.Path(path),data)
  build["patches"][path]={"gitblob":blob,"sha256":sha(data)}
 header=(root/"src/include.h").read_text()
 assert "//#define HARDTABLES" in header
 make=(root/"Makefile").read_text()
 build["author_header_hardtables_commented"]=True
 build["makefile_SHA256"]=sha(make.encode())
 build["make_HARDTABLES_flag_found"]=("-DHARDTABLES" in make)
 src=(root/"src/hadro_pythia.c").read_text()
 build["original_hadro_pythia_C_SHA256"]=fh(root/"src/hadro_pythia.c")
 build["original_current_pipm_SHA256"]=fh(root/"src/tables/hadronization_tables/pythia_tables/pipm.txt")
 build["original_old_pipm_SHA256"]=fh(root/"src/tables/hadronization_tables/pythia_tables/old/pipm.txt")
 assert build["original_current_pipm_SHA256"]=="603f8b1a53efe316b4378da9a6242c1a1b3be026c17fbdaa917cb07f13850ac4"
 assert build["original_old_pipm_SHA256"]=="39306be56e4feeeb361c23983e64b7c4f193c60be4ffa7211b745275cad679fa"
 build["compile"].append({"cmd":"make BlackHawk_inst.c BlackHawk_tot.c","elapsed":cmd(["make","BlackHawk_inst.c","BlackHawk_tot.c"],root,out/"SOURCE_PATCH_PREPARE.log",timeout=120)})
 build["compile"].append({"cmd":"make -j2 BlackHawk_inst.x","elapsed":cmd(["make","-j2","BlackHawk_inst.x"],root,out/"SOURCE_BUILD.log",timeout=480)})
 exe=root/"BlackHawk_inst.x"
 assert exe.is_file(),"missing original BlackHawk_inst.x"
 build["binary_sha256"]=fh(exe)
 write(out/"T1_ORIGINAL_BUILD_IDENTITY.json",(json.dumps(build,indent=2,sort_keys=True)+"\n").encode())
 default={
 "full_output":1,"interpolation_method":0,"metric":0,"BH_number":1,"param_number":1,
 "amin":0.0,"amax":.5,"Qmin":0.0,"Qmax":.7,"epsilon_LQG":1.5,
 "a0_LQG":0.0,"n":0,"spectrum_choice":0,"spectrum_choice_param":0,
 "amplitude_lognormal":1.0,"amplitude_lognormal2":1.0,"stand_dev_lognormal":1.0,
 "crit_mass_lognormal":1.0,"amplitude_powerlaw":1.0,"eqstate_powerlaw":1/3,
 "amplitude_critical_collapse":1.0,"crit_mass_critical_collapse":1.0,
 "amplitude_uniform":1.0,"stand_dev_param_Gaussian":1.0,
 "mean_param_Gaussian":1.0,"table":"spin_distribution_BH.txt",
 "tmin_manual":0,"tmin":1e-30,"limit":5000,"BH_remnant":0,"M_remnant":1e-4,
 "E_number":100,"Emin":5.0,"Emax":1e5,"grav":1,"add_DM":0,
 "m_DM":1.0,"spin_DM":0.0,"dof_DM":1.0,
 "primary_only":0,"hadronization_choice":0}
 observed=[]
 for j in IX:
  mass=(table[j][0]/table[0][0])*1e9
  assert abs(mass/(1e9*4000**(j/99))-1)<1e-12
  name="t1_j%02d"%j
  params={"destination_folder":name,**default,"Mmin":mass,"Mmax":10*mass}
  body="\n".join(k+" = "+(format(v,".17g") if isinstance(v,float) else str(v)) for k,v in params.items())+"\n"
  write(root/(name+".in"),body.encode());write(out/(name+".in"),body.encode())
  print("T1_AUTHORIZED_FIVE_POINT_RUN j=",j,"M_g=",mass,flush=True)
  duration=cmd(["./BlackHawk_inst.x",name+".in"],root,out/(name+".log"),timeout=600)
  secondary=root/"results"/name/"instantaneous_secondary_spectra.txt"
  assert secondary.is_file(),"source secondary file missing: "+str(secondary)
  b=secondary.read_bytes();write(out/(name+"_instantaneous_secondary_spectra.txt"),b)
  ls=b.decode(errors="replace").splitlines()
  headidx=next((i for i,x in enumerate(ls[:10]) if "energy/particle" in x),None)
  assert headidx is not None,ls[:3]
  headers=ls[headidx].split()
  assert headers[0]=="energy/particle" and all(x in headers for x in CH),headers
  records=[l.split() for l in ls[headidx+1:] if l.strip()]
  assert len(records)==500,("secondary provider energy grid mismatch",j,len(records))
  assert all(len(l)==len(headers) for l in records)
  vals=[[float(x) for x in l] for l in records]
  E=[x[0] for x in vals]
  assert all(math.isfinite(x) and x>0 for x in E)
  assert all(a<b for a,b in zip(E,E[1:]))
  h=statistics.fmean(math.log(b)-math.log(a) for a,b in zip(E,E[1:]))
  rates={}
  for k in CH:
   F=[e*row[headers.index(k)] for e,row in zip(E,vals)]
   assert all(math.isfinite(x) and x>=0 for x in F)
   calc=h*(math.fsum(F)-.5*(F[0]+F[-1]))*HBAR
   expected=table[j][CH.index(k)+1]
   assert calc>0 and expected>0
   ratio=calc/expected
   rates[k]={"source_rate_GeV":calc,"original_author_GeV":expected,"ratio_calc_over_author":ratio,
             "relative_group":abs(ratio-1),
             "relative_perstate":abs((.5 if k!="K0L" else 1)*ratio-1)}
  observed.append({"j_0based":j,"mass_g":mass,"original_m_GeV":table[j][0],
                   "secondary_output_SHA256":sha(b),"secondary_grid_points":len(E),
                   "runtime_seconds":duration,"rates":rates})
  print("T1_POINT_DONE",j,{"ratios":{k:round(v["ratio_calc_over_author"],8) for k,v in rates.items()}},flush=True)
 gm=max(v["rates"][k]["relative_group"] for v in observed for k in CH)
 pm=max(v["rates"][k]["relative_perstate"] for v in observed for k in CH)
 verdict="T1-GROUPED" if gm<=1e-5 and pm>1e-5 else ("T1-PERSTATE" if pm<=1e-5 and gm>1e-5 else "T1-NOREPRO")
 result={
 "author_source_commit":WU,"author_original_v23_SHA256":V23,
 "reference_original_gitblob":REFBLOB,"prereg_commit":"c896351e537d79c401eee9a36a80cfac3a47f19d",
 "prereg_pre_exec_erratum_commit":"9feb28e014f0256490cfd72ee10ac009580ab782",
 "five_indices_0based":IX,"number_of_cells":25,"relative_tolerance":1e-5,
 "producer":"Original Wu-Xu 3 patches on exact Arbey-Auffinger BlackHawk v2.3",
 "source_BBN_PYTHIA_choice":0,"source_primary_E_number":100,"source_secondary_grid_n":500,
 "hbar_GeV_s":HBAR,"points":observed,
 "max_group_relative_mismatch":gm,"max_perstate_relative_mismatch":pm,
 "verdict":verdict,"build_identity":build,
 "no_new_Julia":True,"no_physical_PBH_bound":True,"NO_CANON":True,"NO_EXEC_SIGN":True}
 write(out/"T1_FIVE_MASS_25CELL_VERDICT.json",(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n").encode())
 print("T1_VERDICT",verdict,"max_group",gm,"max_perstate",pm,flush=True)
