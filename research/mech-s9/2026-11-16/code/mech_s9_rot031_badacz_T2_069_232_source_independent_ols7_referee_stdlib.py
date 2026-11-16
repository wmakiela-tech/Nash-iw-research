#!/usr/bin/env python3
"""IW/Mech-S9 ROT031 -- bounded, cross-implementation original Badacz T2 PREREG_069
source referee. No native Julia, no BlackHawk, no physical PBH bound.
Usage: python3 -I referee.py <Badacz_owner_dir> <WuXu_scan_jld2> <output.json>
Original owner (Badacz) native run FIRST. Independent centered least-squares
poly2, linear, and OLS7 implemented using Python stdlib only.
"""
import sys,pathlib,hashlib,json,csv,math,statistics,struct,zlib,re,collections
BASE=pathlib.Path(sys.argv[1]); JLD=pathlib.Path(sys.argv[2]); OUT=pathlib.Path(sys.argv[3])
assert len(sys.argv)==4
REF="2390d0d568a5501b34b44463c82f4bc996665af0"
ORIG_JLD_SHA="51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786"
MAT={"data/analysis069.json":"25fc97abeda1d314cd4f695074ccc77e14bb3879",
"data/t2_orig_default.csv":"84945f4b387a59b4f97aa16017a016941c63e83a",
"data/t2_e5_default.csv":"7e61b28a85f26f5dfd28a56ec887d9ebbba73e5c",
"data/t2_orig_1e-4.csv":"f818894764cc5650dfc9cb16fd643a7bbdeeddd5",
"data/t2_e5_1e-4.csv":"68755d3335a058b81008ef3324859a9cd3bc3dc2",
"data/t2_run_record.json":"a6df162615169ea486efe27249b6d0d79fbfde04",
"code/b1_t2_069_analysis.py":"4902fa31cb14d5bcc873861c7e26b109fe387197"}
def gitblob(v):return hashlib.sha1(b"blob "+str(len(v)).encode()+b"\0"+v).hexdigest()
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name,blob in MAT.items():
 path=BASE/name
 assert gitblob(path.read_bytes())==blob,(name,"owner Git blob changed")
assert digest(JLD)==ORIG_JLD_SHA,"AUTHOR_ORIGINAL_SCAN_SHA_MISMATCH"
owner=json.loads((BASE/"data/analysis069.json").read_text())
run=json.loads((BASE/"data/t2_run_record.json").read_text())
manifest=(BASE/"data/MANIFEST_SHA256.md").read_text()
for name in MAT:
 if name.startswith("data/") and name!="data/t2_run_record.json":
  actual=digest(BASE/name)
  assert re.search(r"(?m)^"+actual+r"\s+"+re.escape(name)+r"$",manifest),(name,"manifest source SHA mismatch",actual)
assert set(owner)=={"roots","shift","verdicts","tol_check"}
SCHEMES=("orig_default","e5_default","orig_1e-4","e5_1e-4")
RECORD_COUNTS={"orig_default":102,"e5_default":102,"orig_1e-4":14,"e5_1e-4":14}
MASSES=(22,28,38,51,62,90)
DATA={}
SOURCE_META={}
for key in SCHEMES:
 p=BASE/("data/t2_"+key+".csv")
 raw=p.read_text()
 metadata=raw.splitlines()[0]
 assert "BITS=100" in metadata and "DiffEq=7.17.0" in metadata,(key,"source env header mismatch")
 rows=list(csv.DictReader(line for line in raw.splitlines() if not line.startswith("#")))
 assert len(rows)==RECORD_COUNTS[key]
 log=run["series"][key]
 assert log["status"]==0 and log["csv_sha256"]==digest(p)
 by_j=collections.defaultdict(list)
 for v in rows:
  assert v["arm"]==key.split("_")[0] and v["tol"]==("default" if key.endswith("default") else "1e-4")
  j=int(v["j"]);b=float(v["log10beta"]);y=float(v["Y"])
  assert math.isfinite(y) and y>0 and math.isfinite(b) and y<1
  assert j in MASSES
  by_j[j].append((b,y,float(v["m_g"])))
 expected=MASSES if key.endswith("default") else (22,62)
 assert set(by_j)==set(expected)
 for j in expected:
  z=sorted(by_j[j])
  assert len(z)==(17 if key.endswith("default") else 7)
  assert len(set(v[0] for v in z))==len(z)
  assert all(abs(z[i+1][0]-z[i][0]-(.02 if key.endswith("default") else .04))<1e-7 for i in range(len(z)-1))
  assert max(x[2] for x in z)-min(x[2] for x in z)==0
  by_j[j]=[(x,y) for x,y,_ in z]
 DATA[key]=by_j
 SOURCE_META[key]={"n_records":len(rows),"csv_sha256":digest(p),"native_exit":log["status"],
  "grids":{str(j):{"count":len(by_j[j]),"range":[by_j[j][0][0],by_j[j][-1][0]]} for j in expected}}

# Stable independent 3x3 pivoted Gaussian elimination for centered quadratic
def solve3(matrix,vec):
 A=[list(map(float,m))+[float(v)] for m,v in zip(matrix,vec)]
 for i in range(3):
  best=max(range(i,3),key=lambda k:abs(A[k][i]))
  assert abs(A[best][i])>1e-24
  A[i],A[best]=A[best],A[i]
  p=A[i][i]
  for j in range(i,4):A[i][j]/=p
  for k in range(3):
   if k==i:continue
   f=A[k][i]
   for j in range(i,4):A[k][j]-=f*A[i][j]
 return [A[i][3] for i in range(3)]

def change(y):
 for i in range(len(y)-1):
  if y[i]<0<=y[i+1]:return i
 return None
def lin(lb,y):
 k=change(y)
 if k is None:return None
 return lb[k]-y[k]*(lb[k+1]-lb[k])/(y[k+1]-y[k])
def quad(lb,y):
 k=change(y)
 if k is None:return None
 lo=max(0,k-1);hi=min(len(lb),k+3)
 x0=lb[k]
 w=[v-x0 for v in lb[lo:hi]]
 v=y[lo:hi];a=[math.fsum(x**n for x in w) for n in range(5)]
 b=[math.fsum(x**n*f for x,f in zip(w,v)) for n in range(3)]
 c0,c1,c2=solve3([[a[0],a[1],a[2]],[a[1],a[2],a[3]],[a[2],a[3],a[4]]],b)
 disc=c1*c1-4*c2*c0
 if disc<0:return None
 if abs(c2)<1e-20:roots=[-c0/c1]
 else:roots=[(-c1+sign*math.sqrt(disc))/(2*c2) for sign in (1,-1)]
 roots=[z+x0 for z in roots if lb[lo]-1e-9<=z+x0<=lb[hi-1]+1e-9]
 return min(roots,key=lambda z:abs(z-lb[k])) if roots else None
def ols(lb,y):
 first=lin(lb,y)
 if first is None:return None,None
 keys=sorted(range(len(lb)),key=lambda k:abs(lb[k]-first))[:7]
 xx=[lb[k] for k in keys];yy=[y[k] for k in keys]
 mx=math.fsum(xx)/7;my=math.fsum(yy)/7
 sxx=math.fsum((x-mx)**2 for x in xx)
 beta=math.fsum((x-mx)*(v-my) for x,v in zip(xx,yy))/sxx
 assert beta>0
 root=mx-my/beta
 resid=[v-(my+beta*(x-mx)) for x,v in zip(xx,yy)]
 variance=math.fsum(u*u for u in resid)/5
 se=math.sqrt(variance)/abs(beta)*math.sqrt(1/7+(root-mx)**2/sxx)
 return root,se
def numclose(x,y,tol=1e-8):
 if x is None or y is None:assert x is y
 else:assert math.isclose(x,y,abs_tol=tol,rel_tol=0),(x,y,"ROOT_RECOMPUTATION_DIFF")

ROOTS={};DIFFS=[]
for scheme,grids in DATA.items():
 ROOTS[scheme]={}
 for j,obs in grids.items():
  lb=[x for x,y in obs];y=[y-.251 for x,y in obs]
  r0=lin(lb,y);rB=quad(lb,y);rD,se=ols(lb,y)
  sign_changes=sum(((a>0)-(a<0))!=((b>0)-(b<0)) for a,b in zip(y,y[1:]))
  found={"M_B":rB,"M_C":r0,"M_D":rD,"se_M_D":se,
    "n_sign_changes":sign_changes,"n":len(lb)}
  expected=owner["roots"][scheme][str(j)]
  for k in found:
   if k in ("n_sign_changes","n"):assert found[k]==expected[k],(scheme,j,k)
   else:numclose(found[k],expected[k],tol=2e-8)
  ROOTS[scheme][str(j)]=found
  DIFFS.append(max(abs(found[k]-expected[k]) for k in ("M_B","M_C","M_D","se_M_D")))
# Original scanned Wu-Xu archive 100x100 JLD2 source, native independently decoded.
binary=JLD.read_bytes()
streams=[];i=0
while i<len(binary)-2:
 if binary[i]==120 and binary[i+1] in (1,94,156,218):
  try:
   d=zlib.decompressobj();value=d.decompress(binary[i:])
   used=len(binary[i:])-len(d.unused_data)
   if len(value)>=64 and len(value)%8==0:
    streams.append(struct.unpack("<"+"d"*(len(value)//8),value))
    i+=used;continue
  except (zlib.error,struct.error,ValueError):pass
 i+=1
assert len(streams)>=3
lb_arch=[math.log10(v) for v in streams[1]]
Ymat=next((s for s in streams[2:] if len(s)==10000 and 0<max(s)<2),None)
assert len(lb_arch)==100 and Ymat is not None

T2={};CANON={22:.279,28:.268,38:.281,51:.287,62:.295,90:.301}
for j in MASSES:
 ro=ROOTS["orig_default"][str(j)]
 re=ROOTS["e5_default"][str(j)]
 md={m:re[m]-ro[m] for m in ("M_B","M_C","M_D")}
 Y=[Ymat[100*k+j] for k in range(100)]
 k=next(k for k in range(99) if Y[k]<.251<=Y[k+1])
 arch=lb_arch[k]+(.251-Y[k])*(lb_arch[k+1]-lb_arch[k])/(Y[k+1]-Y[k])
 shift=owner["shift"][str(j)]
 numclose(arch,shift["archive_root"])
 for m in ("M_B","M_C","M_D"):numclose(md[m],shift["D_by_method"][m])
 numclose(md["M_D"],shift["D_M_D"])
 se=math.hypot(ro["se_M_D"],re["se_M_D"])
 numclose(se,shift["se_D_M_D"])
 spread=max(md.values())-min(md.values())
 numclose(spread,shift["method_spread"])
 root_offset=ro["M_D"]-arch
 numclose(root_offset,shift["orig_root_minus_archive_root"])
 numclose(md["M_D"]-math.log10(2),shift["D_minus_log10_2"])
 assert 0.20<=md["M_D"]<=.35
 T2[str(j)]={"orig_M_D":ro["M_D"],"e5_M_D":re["M_D"],"D_M_D":md["M_D"],
            "D_methods":md,"method_spread":spread,
            "conditional_LSQ_SE_D":se,
            "D_minus_log10_2":md["M_D"]-math.log10(2),
            "orig_archive_beta_root":arch,"orig_minus_archive_root":root_offset,
            "number_sign_changes_orig":ro["n_sign_changes"],
            "number_sign_changes_e5":re["n_sign_changes"]}
assert T2["90"]["D_M_D"]>=T2["22"]["D_M_D"]
assert owner["verdicts"]["W"]=="W-PASS"
assert owner["verdicts"]["ORD"]=="ORD-PASS"
tol={}
for j in (22,62):
 base=ROOTS["orig_1e-4"][str(j)]
 alt=ROOTS["e5_1e-4"][str(j)]
 dd=alt["M_D"]-base["M_D"]
 default=T2[str(j)]["D_M_D"]
 delta=dd-default
 assert abs(delta)<=.03
 a=base["M_D"]-ROOTS["orig_default"][str(j)]["M_D"]
 c=alt["M_D"]-ROOTS["e5_default"][str(j)]["M_D"]
 source=owner["tol_check"][str(j)]
 for k,x in (("D_1e-4",dd),("diff_vs_default",delta),("orig_root_1e-4_minus_default",a)):
  numclose(x,source[k])
 tol[str(j)]={"D_default":default,"D_1e4":dd,"D_change":delta,
             "orig_root_change":a,"e5_root_change":c,
             "abs_root_change_max":max(abs(a),abs(c)),
             "abs_root_change_max_over_shift_change":max(abs(a),abs(c))/max(abs(delta),1e-50),
             "cancellation_warning": "STABLE_SHIFT_NOT_ABSOLUTE_ROOT_ACCURACY"}
assert owner["verdicts"]["TOL"]=="TOL-STABLE"
assert sum(v["n_records"] for v in SOURCE_META.values())==232
out={"artifact_id":"IW_MECH_S9_ROT031_T2_PREREG069_INDEPENDENT_SOURCE_REFEREE",
"owner_firstness":"Badacz PREREG069 REVIEW071 232 native Wu-Xu Julia calls executed FIRST",
"owner_commit":REF,"original_author_scanning_sha256":ORIG_JLD_SHA,
"original_owner_git_blobs":MAT,"raw_CSV_native_run_evidence":SOURCE_META,
"analyzed_roots":ROOTS,"root_max_abs_independent_vs_owner_float":max(DIFFS),
"per_mass_T2_source_results":T2,
"preregistered_gates_independently_verified":{"W":"W-PASS","ORD":"ORD-PASS","TOL":"TOL-STABLE"},
"tol_control_abs_root_vs_shift_difference":tol,
"original_author_scan_100x100_reconstruction":True,
"nonewJulia":True,"nonewBlackHawk":True,
"limitations":["Independent source CSV and code analysis, NOT independently executed native 10D solver",
"Owner M_D SE from OLS local residuals conditional, NOT certified stochastic error bars or full solver uncertainty",
"Tolerance stability of SHIFT can arise from cancellation of larger, correlated absolute-root changes",
"Root M_B,C,D method spread is sensitivity, not statistical confidence interval",
"6x contour-root shifts refer to deterministic code Y=2X/(1-X) only, not physical helium Yp",
"j22 source beta off original author maximum allowed only by original Badacz prereg",
"No automatic physical PBH bound, physics novelty, paper-error assertion or CANON promotion",
"Badacz owns native results, firstness preserved"]}
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
print(json.dumps({"numCSV":sum(v["n_records"] for v in SOURCE_META.values()),
"gates":out["preregistered_gates_independently_verified"],
"max_abs_float_root_difference":max(DIFFS),
"shifts":{j:{k:v[k] for k in ("D_M_D","method_spread","D_minus_log10_2")} for j,v in T2.items()},
"tolerance_cancellation":tol},indent=2))
