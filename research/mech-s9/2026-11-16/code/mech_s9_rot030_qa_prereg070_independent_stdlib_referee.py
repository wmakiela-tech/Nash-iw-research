#!/usr/bin/env python3
"""Mech-S9 ROT030: DIFFERENT-IMPLEMENTATION stdlib referee of Badacz PREREG070.
No Julia/BlackHawk calls; owner original raw CSV and analysis frozen Git source.
Usage python -I .../mech_s9_rot030_qa_regime_referee.py <owner_b1_dir> <out.json>
"""
from pathlib import Path
import hashlib,csv,sys,json,math,statistics,collections
D=Path(sys.argv[1]);dest=Path(sys.argv[2])
expected={
"code/b1_qa_070_analysis.py":"1a9d5aafeca14a4c2729572157b6463dc4926c5c526f999116dcbb223487f1f7",
"data/qa_A.csv":"0d7922b78ffe07dd85bbc462324dbf1d9ae6a4fdcc3040d0cf643a08af3f9d56",
"data/qa_B.csv":"7b25eb8728d0f4c449631ca0035d96ef6ed820d5b4a3b8f2014497a8e6d083cd",
"data/analysis070.json":"72c0925bbf0f9ba3f39b09edab4a63003db0fac9492ccb22575325a95d3f5db4",
"data/qa_run_record.json":"1ed1a26abb8874784fcc5c04297a03cf151ba3f4e1f8ca9714ddd50e2317cade"
}
for name,sha in expected.items():
 got=hashlib.sha256((D/name).read_bytes()).hexdigest()
 assert got==sha,(name,"actual original source SHA disagreement",got,sha)
owner=json.loads((D/"data/analysis070.json").read_text())
manifest=(D/"data/MANIFEST_SHA256.md").read_text()
for name,sha in expected.items():
 assert sha+"  "+name in manifest,(name,"owner source SHA entry missing")
run=json.loads((D/"data/qa_run_record.json").read_text())
assert run["grids"]["A"]["status"]==run["grids"]["B"]["status"]==0
assert all(run["grids"][n]["csv_sha256"]==expected["data/qa_"+n+".csv"] for n in ("A","B"))

def load(tag,js,k_start,k_end):
 raw=(D/("data/qa_"+tag+".csv")).read_text()
 rows=list(csv.DictReader(ln for ln in raw.splitlines() if not ln.startswith("#")))
 assert len(rows)==(192 if tag=="A" else 63),(tag,len(rows))
 data=collections.defaultdict(dict)
 for r in rows:
  assert r["arm"]=="orig" and r["tol"]=="default"
  j=int(r["j"])
  assert j in js and math.isfinite(float(r["Y"])) and float(r["Y"])>0
  beta=round(float(r["log10beta"]),6)
  assert beta not in data[j]
  data[j][beta]=float(r["Y"])
 assert set(data)==set(js)
 expectedkeys={-30.0}|{round((k_start+t)/10,6) for t in range(k_end-k_start+1)}
 for j in js:
  assert set(data[j])==expectedkeys,(tag,j,sorted(set(data[j])^expectedkeys))
 return data,len(rows)

# 0.1-dex 5-neighbour OLS implemented independently (no NumPy, polyfit, imports of owner code)
def local_slope(x,y):
 mx=math.fsum(x)/len(x);my=math.fsum(y)/len(y)
 z=math.fsum((v-mx)**2 for v in x)
 return math.fsum((a-mx)*(b-my) for a,b in zip(x,y))/z
def slope_sigma(x,w,sigma):
 mean=math.fsum(x)/len(x)
 denom=math.fsum((a-mean)**2 for a in x)
 return math.sqrt(math.fsum(((sigma/w_i)*(x_i-mean)/denom)**2 for x_i,w_i in zip(x,w)))
def each_regime(data,tag):
 evidence={};diffs=[];counts={}
 for j,points in sorted(data.items()):
  baseline=points[-30.]
  xs=baseline/(2+baseline)
  grid=sorted(b for b in points if b>-29)
  ys=[points[b] for b in grid]
  dY=[v-baseline for v in ys]
  dX=[v/(2+v)-xs for v in ys]
  ownerj=owner[tag][str(j)]
  assert math.isclose(ownerj["X_SBBN"],xs,abs_tol=5e-16)
  assert math.isclose(ownerj["Y_SBBN"],baseline,abs_tol=5e-16)
  ob=ownerj["nodes"];assert len(ob)==len(grid)-4
  nodes=[]
  for k in range(2,len(grid)-2):
   xw=[grid[t]*math.log(10) for t in range(k-2,k+3)]
   n={"log10beta":grid[k]}
   reported=ob[k-2]
   assert abs(reported["log10beta"]-grid[k])<1e-10
   for key,values,noise in (("X",dX,1.4e-5),("Y",dY,3.6e-5)):
    w=values[k-2:k+3]
    if min(w)>0:
     slope=local_slope(xw,[math.log(v) for v in w])
     sigma=slope_sigma(xw,w,noise)
     resolved=all(v>=0.001 for v in w)
     label=(("LINEAR" if slope>=.9 else "SATURATION" if slope<=.3 else "INTERMEDIATE") if resolved else None)
    else:slope=None;sigma=None;resolved=False;label=None
    ov=reported[key]
    assert (ov["label"],ov["resolvable"])==(label,resolved),(tag,j,k,key,"LABEL_SOURCE_MISMATCH",ov,label)
    assert math.isclose(values[k],ov["dQ"],abs_tol=5e-15)
    if slope is not None:
     assert math.isclose(ov["s"],slope,rel_tol=1e-10,abs_tol=1e-10),(tag,j,k,key,"SLOPE",ov["s"],slope)
     assert math.isclose(ov["sigma_s"],sigma,rel_tol=2e-10,abs_tol=2e-10),(tag,j,k,key,"SIGMA",ov["sigma_s"],sigma)
    else:assert ov["s"] is None
    n[key]={"dQ":values[k],"slope":slope,"sigma_s_assuming_independent_noise":sigma,"resolvable":resolved,"label":label}
   nodes.append(n)
  counts[j]={q:dict(collections.Counter(n[q]["label"] or "UNRESOLVED" for n in nodes)) for q in ("X","Y")}
  evidence[str(j)]={"baseline_Y":baseline,"baseline_X":xs,"nodes":nodes}
 return evidence,counts

A,rowsA=load("A",(22,28,38,51,62,90),-200,-170)
B,rowsB=load("B",(19,22,24),-169,-150)
resA,countsA=each_regime(A,"A")
resB,countsB=each_regime(B,"B")
verdicts=owner["verdicts"]
assert verdicts["P-A1"]["verdict"]=="PASS"
def lookup(tree,j,beta):
 return next((r for r in tree[str(j)]["nodes"] if abs(r["log10beta"]-beta)<1e-9),None)
sat=[(int(j),x["log10beta"]) for j,e in resA.items() for x in e["nodes"] if x["X"]["label"]=="SATURATION"]
assert not sat
reg={q:{} for q in ("P-A2","P-A3")}
for key,beta,lo,hi in (("P-A2",-17.2,.35,.7),("P-A3",-18.2,.75,1.05)):
 for j in (22,28,38):
  node=lookup(resA,j,beta);assert node is not None
  y=node["Y"]
  label=("UNRESOLVED" if not y["resolvable"] else "PASS" if lo<=y["slope"]<=hi else "FAIL")
  assert label==verdicts[key][str(j)],(key,j,label,verdicts[key][str(j)])
  reg[key][j]={"slope":y["slope"],"dY":y["dQ"],"sigma_s_assumed":y["sigma_s_assuming_independent_noise"],"gate":label}
first={}
for j in (19,22,24):
 first[j]=next((n["log10beta"] for n in resB[str(j)]["nodes"] if n["X"]["label"]=="SATURATION"),None)
 assert first[j]==verdicts["B_first_saturation"][str(j)],(j,first[j],verdicts["B_first_saturation"])
nonvac={int(j):sum(v!="UNRESOLVED" for v in [x["X"]["label"] or "UNRESOLVED" for x in resA[j]["nodes"]]) for j in resA}
contours={22:-17.22,28:-18.36,38:-19.01,51:-19.30,62:-19.39,90:-19.37}
near={}
for j,beta in contours.items():
 n=min(resA[str(j)]["nodes"],key=lambda x:abs(x["log10beta"]-beta))
 near[j]={"log10beta_nearest_node":n["log10beta"],"contour_log10beta_owner_rounded":beta,
   "slope_X_at_nearest_node":n["X"]["slope"],"slope_Y_at_nearest_node":n["Y"]["slope"],
   "resolvable_X":n["X"]["resolvable"],"resolvable_Y":n["Y"]["resolvable"]}
# Mechanistic self-audit: Y=2X/(1-X), so for constant X0, Y0:
# DeltaY/DeltaX = 2/[(1-X)(1-X0)] at every source observation, not an independent observable.
identity_max=0
for source in (A,B):
 for j,pts in source.items():
  Y0=pts[-30.];X0=Y0/(Y0+2)
  for beta,Y in pts.items():
   X=Y/(Y+2)
   if beta==-30 or abs(X-X0)<1e-8:continue
   deltaY=Y-Y0;deltaX=X-X0
   rhs=2/((1-X)*(1-X0))
   identity_max=max(identity_max,abs(deltaY/deltaX/rhs-1))
assert identity_max<1e-8
out={"identity":"IW_MECH_S9_ROT030_INDEPENDENT_STDLIB_REFEREE_QA070",
 "author_Badacz_firstness":True,"owner_commit":"f42da5ca89227ce2a1b72664a747a4d593e18853",
 "owner_source_sha256":expected,"native_Julia_called":False,"number_of_owner_source_records":rowsA+rowsB,
 "owner_source_run_statuses":{"A":run["grids"]["A"]["status"],"B":run["grids"]["B"]["status"]},
 "full_source_node_audit":{"grid_A_nodes":sum(len(e["nodes"]) for e in resA.values()),
    "grid_B_nodes":sum(len(e["nodes"]) for e in resB.values()),"all_X_Y_slopes_sigma_s_labels_matched_original_owner":True},
 "predictions_independently_regenerated":{"P-A1":"PASS","P-A2":reg["P-A2"],"P-A3":reg["P-A3"],
                                      "B_first_resolvable_saturation":first},
 "A_nonlinear_label_nonvacuity_resolvable_X_nodes":nonvac,
 "A_regime_node_counts":countsA,"B_regime_node_counts":countsB,
 "nearest_QB_T2_contour_source_slopes":near,
 "Y_code_exact_algebra_identity_deltaY_over_deltaX_max_relative_error":identity_max,
 "source_evidence_limitations":[
 "One-point default-versus-explicit-tolerance variation 1.4e-5 X IS NOT statistical standard deviation for all mass/beta nodes",
 "Owner uncertainty sigma_s is conditional on assumed independent point-noise with constant sigma_X; non-probabilistic conditional proxy",
 "Original Q-A B grid beyond author beta scan; numerical source only",
 "Ycode=2X/(1-X) is deterministic transform; slopes X and Y are not independent physics",
 "Near contour slopes are node-level finite-window estimates; beta roots come from distinct Badacz T2 result",
 "J28 and J38 linear near T2 roots with D below log10(2) disfavours NONLINEARITY AS SOLE cause but does NOT uniquely identify K0L versus other unhalved/nonhadronic terms",
 "No original Wu-Xu physical BBN or PBH bound; T1 source gate separately admitted by Moderator",
 "No novelty; no canon; no exec sign"] }
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
print(json.dumps({"QA_OWNER_SOURCE_COLD_INDEPENDENT_PASS":True,
 "rows":rowsA+rowsB,
 "node_counts":out["full_source_node_audit"],
 "gates":{k:v for k,v in out["predictions_independently_regenerated"].items()},
 "nonvacuous_nodes":nonvac,"near_contour":near,"identity_max":identity_max},indent=2))
