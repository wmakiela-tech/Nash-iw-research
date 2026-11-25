import gzip, csv, json, math, statistics, sys, time, importlib.metadata
from pathlib import Path
import pythia8mc as p8
IDS=(211,-211,321,-321,130,2212,-2212,2112,-2112)
ENERGIES=(10000,30000,100000,300000,1000000,2000000)
PROC={
    "up": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on","23:onMode = off","23:onIfAny = 2"],
    "gluon": ["HiggsSM:ffbar2H = on","25:onMode = off","25:onIfAny = 21"],
}
CELLS=(("up",0,100000,220001),("up",0,2000000,220002),("up",1,2000000,220003),("gluon",0,2000000,220004))
def record(ev):
    rows=[]
    for k in range(ev.size()):
        p=ev[k]
        row=dict(k=k,id=p.id(),status=p.status(),final=bool(p.isFinal()),mother=[p.mother1(),p.mother2()],daughter=[p.daughter1(),p.daughter2()],color=[p.col(),p.acol()],charge3=int(p.chargeType()),v=[p.px(),p.py(),p.pz(),p.e()],mass=p.m())
        assert all(math.isfinite(x) for x in row["v"]+[row["mass"]])
        rows.append(row)
    return rows
def summ(rows,accurate=True):
    return [(math.fsum if accurate else sum)(p["v"][j] for p in rows) for j in range(4)]
def main():
    cell=int(sys.argv[1]); prim,w,E,seed=CELLS[cell]; out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    assert importlib.metadata.version("pythia8mc")=="8.318.3"
    py=p8.Pythia("",False)
    settings=["Beams:idA = 11","Beams:idB = -11","PhaseSpace:pTHatMin = 0.","PartonLevel:ISR = off","PDF:lepton = off",f"Beams:eCM = {2*E}","Random:setSeed = on",f"Random:seed = {seed}",f"TimeShower:weakShower = {'on' if w else 'off'}","Next:numberCount = 0","Next:numberShowEvent = 0","Next:numberShowProcess = 0","Next:numberShowInfo = 0"]+PROC[prim]
    for s in settings: assert py.readString(s),s
    pd=py.particleData
    assert not any(pd.mayDecay(i) for i in (211,321,130,13,2112))
    assert all(pd.mayDecay(i) for i in (310,3122,3222,3112,3312,3322,3334))
    assert py.init()
    effective={}
    for key,fn in (("Check:event","flag"),("Check:epTolWarn","parm"),("Check:epTolErr","parm")):
        try: effective[key]=getattr(py.settings,fn)(key)
        except Exception as exc: effective[key]={"api_error":str(exc)}
    n=failed=0; classes={}; qual=0; maxdiff=0.
    with gzip.open(out/f"cell{cell}.jsonl.gz","xt") as f:
        for attempt in range(1,2001):
            if not py.next(): failed+=1;continue
            ev=record(py.event); process=record(py.process)
            final=[p for p in ev if p["final"]]; hard=[p["id"] for p in ev if p["status"]==-23]
            ok=bool(hard) and all(abs(i)==2 if prim=="up" else i==21 for i in hard)
            qual+=ok; n+=1
            counts={str(i):0 for i in IDS}
            for p in final:
                if str(p["id"]) in counts: counts[str(p["id"])]+=1
            naive=summ(final,False); exact=summ(final); nominal=[0.,0.,0.,2.*E]
            valid=len(ev)>2 and sorted([ev[1]["id"],ev[2]["id"]])==[-11,11] and ev[1]["status"]==ev[2]["status"]==-12
            beam=summ(ev[1:3]) if valid else None
            def res(v,ref): return [(a-b)/(2*E) for a,b in zip(v,ref)]
            rn=res(naive,nominal); re=res(exact,nominal); rb=res(exact,beam) if valid else None; rs=res(exact,ev[0]["v"])
            diff=max(map(abs,res(naive,exact)));maxdiff=max(maxdiff,diff)
            if abs(rn[3])<=1e-6: cls="old_gate_pass"
            elif abs(re[3])<=1e-6: cls="summation_sensitive"
            elif valid and max(map(abs,rb))<=1e-6: cls="nominal_reference_sensitive"
            elif valid: cls="persistent_recorded_mismatch"
            else: cls="unresolved"
            classes[cls]=classes.get(cls,0)+1
            f.write(json.dumps(dict(attempt=attempt,success=n,qualified=ok,hard_ids=hard,counts=counts,charge3=sum(p["charge3"] for p in final),naive=naive,fsum=exact,nominal=nominal,beam=beam,beam_valid=valid,system=ev[0]["v"],res_naive=rn,res_exact=re,res_beam=rb,res_system=rs,classification=cls,event=ev,process=process),allow_nan=False,separators=(",",":"))+"\n")
            if n==200:break
    py.stat()
    result=dict(cell=cell,primary=prim,weak=w,E=E,seed=seed,successful=n,failed=failed,qualified=qual,rejected=n-qual,classes=classes,max_naive_fsum_normalized=maxdiff,effective_settings=effective,settings=settings)
    (out/f"cell{cell}.json").write_text(json.dumps(result,indent=2,allow_nan=False))
    print(json.dumps(result),flush=True)
    if n!=200:sys.exit(2)
if __name__=="__main__":main()
