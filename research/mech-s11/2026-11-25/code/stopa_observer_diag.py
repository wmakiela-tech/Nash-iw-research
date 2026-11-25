import hashlib, gzip, csv, json, math, statistics, sys, time, importlib.metadata
from pathlib import Path
import pythia8mc as p8
IDS=(211,-211,321,-321,130,2212,-2212,2112,-2112)
ENERGIES=(10000,30000,100000,300000,1000000,2000000)
PROC={
    "up": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on","23:onMode = off","23:onIfAny = 2"],
    "gluon": ["HiggsSM:ffbar2H = on","25:onMode = off","25:onIfAny = 21"],
}
CELLS=(("up",0,100000,250001),("up",0,2000000,250002),("up",1,2000000,250003),("gluon",0,2000000,250004))
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
def digest(rows):
    return hashlib.sha256(json.dumps(rows,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def snapshot(rows):
    final=[p for p in rows if p["final"]]
    valid=len(rows)>2 and sorted([rows[1]["id"],rows[2]["id"]])==[-11,11] and rows[1]["status"]==rows[2]["status"]==-12
    return dict(n=len(rows),nfinal=len(final),beam_valid=valid,beam=summ(rows[1:3]) if valid else None,system=rows[0]["v"],final=summ(final),charge3=sum(p["charge3"] for p in final),hard_ids=[p["id"] for p in rows if p["status"]==-23],sha256=digest(rows))
class Observer(p8.UserHooksVector):
    def __init__(self):
        super().__init__()
        self.trace=[]
    def canVetoPartonLevel(self): return True
    def canVetoAfterHadronization(self): return True
    def doVetoPartonLevel(self,event):
        self.trace.append(dict(stage="A",**snapshot(record(event))))
        return False
    def doVetoAfterHadronization(self,event):
        self.trace.append(dict(stage="B",**snapshot(record(event))))
        return False
def main():
    cell=int(sys.argv[1]); mode=sys.argv[2]; prim,w,E,seed=CELLS[cell];out=Path(sys.argv[3]);out.mkdir(parents=True,exist_ok=True)
    assert mode in ("baseline","observer")
    assert importlib.metadata.version("pythia8mc")=="8.318.3"
    py=p8.Pythia("",False)
    settings=["Beams:idA = 11","Beams:idB = -11","PhaseSpace:pTHatMin = 0.","PartonLevel:ISR = off","PDF:lepton = off",f"Beams:eCM = {2*E}","Random:setSeed = on",f"Random:seed = {seed}",f"TimeShower:weakShower = {'on' if w else 'off'}","Next:numberCount = 0","Next:numberShowEvent = 0","Next:numberShowProcess = 0","Next:numberShowInfo = 0"]+PROC[prim]
    for s in settings: assert py.readString(s),s
    pd=py.particleData
    assert not any(pd.mayDecay(i) for i in (211,321,130,13,2112))
    assert all(pd.mayDecay(i) for i in (310,3122,3222,3112,3312,3322,3334))
    obs=Observer() if mode=="observer" else None
    if obs is not None: assert py.setUserHooksPtr(obs)
    assert py.init()
    effective={k:getattr(py.settings,f)(k) for k,f in (("Check:event","flag"),("Check:epTolWarn","parm"),("Check:epTolErr","parm"),("TimeShower:weakShower","flag"),("PartonLevel:ISR","flag"),("PDF:lepton","flag"),("Beams:eCM","parm"),("Random:seed","mode"))}
    n=0
    with (out/f"{mode}.jsonl").open("x") as f:
        for call in range(1,501):
            if obs is not None: obs.trace=[]
            ok=bool(py.next())
            row=dict(call=call,success=ok,trace=obs.trace if obs is not None else [])
            if ok:
                ev=record(py.event);proc=record(py.process); snap=snapshot(ev); hard=snap["hard_ids"]
                row.update(event=snap,process_sha256=digest(proc),qualified=bool(hard) and all(abs(i)==2 if prim=="up" else i==21 for i in hard))
                n+=1
            f.write(json.dumps(row,allow_nan=False,separators=(",",":"))+"\n")
            if n==50:break
    py.stat()
    (out/f"{mode}.json").write_text(json.dumps(dict(cell=cell,mode=mode,E=E,seed=seed,settings=settings,effective=effective,successful=n,calls=call),indent=2,allow_nan=False))
    if n!=50:sys.exit(2)
if __name__=="__main__": main()
