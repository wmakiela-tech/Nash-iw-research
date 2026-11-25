import csv, json, math, statistics, sys, time, importlib.metadata
from pathlib import Path
import pythia8mc as p8
IDS=(211,-211,321,-321,130,2212,-2212,2112,-2112)
ENERGIES=(10000,30000,100000,300000,1000000,2000000)
PROC={
    "up": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on","23:onMode = off","23:onIfAny = 2"],
    "gluon": ["HiggsSM:ffbar2H = on","25:onMode = off","25:onIfAny = 21"],
}
def main():
    prim,w,index,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),Path(sys.argv[4])
    assert prim in PROC and w in (0,1) and 0<=index<6
    assert importlib.metadata.version("pythia8mc")=="8.318.3"
    out.mkdir(parents=True,exist_ok=True)
    E=ENERGIES[index]
    seed=110000+10000*(prim=="gluon")+1000*w+index
    py=p8.Pythia("",False)
    settings=["Beams:idA = 11","Beams:idB = -11","PhaseSpace:pTHatMin = 0.","PartonLevel:ISR = off","PDF:lepton = off",f"Beams:eCM = {2*E}","Random:setSeed = on",f"Random:seed = {seed}",f"TimeShower:weakShower = {'on' if w else 'off'}","Next:numberCount = 0","Next:numberShowEvent = 0","Next:numberShowProcess = 0","Next:numberShowInfo = 0"]+PROC[prim]
    for s in settings:
        assert py.readString(s), s
    pd=py.particleData
    assert not any(pd.mayDecay(i) for i in (211,321,130,13,2112))
    assert all(pd.mayDecay(i) for i in (310,3122,3222,3112,3312,3322,3334))
    assert py.init()
    tag=f"{prim}_w{w}_e{index}"
    accepted=failed=rejected=charge_bad=energy_bad=0
    samples=[]; start=time.time()
    max_res=0.
    with (out/f"{tag}.csv").open("x",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["attempt","accepted","hard_size","charge3","Efinal_over_2E"]+[f"n_{i}" for i in IDS]+[f"E_{i}" for i in IDS]+[f"E2_{i}" for i in IDS])
        for attempt in range(1,20001):
            if not py.next():
                failed+=1; continue
            ev=py.event
            hard=[ev[k].id() for k in range(ev.size()) if ev[k].status()==-23]
            if not hard or not all((abs(i)==2 if prim=="up" else i==21) for i in hard):
                rejected+=1; continue
            c=dict.fromkeys(IDS,0); en=dict.fromkeys(IDS,0.); en2=dict.fromkeys(IDS,0.)
            q3=0; energy=0.
            for k in range(ev.size()):
                p=ev[k]
                if not p.isFinal(): continue
                q3+=int(p.chargeType())
                e=p.e(); energy+=e
                i=p.id()
                if i in c: c[i]+=1; en[i]+=e; en2[i]+=e*e
            assert math.isfinite(energy) and all(math.isfinite(x) for x in en.values()) and all(math.isfinite(x) for x in en2.values())
            ratio=energy/(2*E)
            accepted+=1
            charge_bad+=q3!=0
            energy_bad+=abs(ratio-1)>1e-6
            max_res=max(max_res,abs(ratio-1))
            vals=[c[i] for i in IDS]
            samples.append(vals)
            writer.writerow([attempt,accepted,len(hard),q3,ratio]+vals+[en[i] for i in IDS]+[en2[i] for i in IDS])
            if accepted==2000: break
    def stats(v):
        return {"mean":statistics.mean(v),"sd":statistics.stdev(v),"se":statistics.stdev(v)/math.sqrt(len(v))} if len(v)>1 else {"mean":v[0] if v else None,"sd":None,"se":None}
    species={str(i):stats([v[k] for v in samples]) for k,i in enumerate(IDS)}
    groups={str(IDS[a]):stats([v[a]+v[b] for v in samples]) for a,b in ((0,1),(2,3),(5,6),(7,8))}
    groups["130"]=species["130"]
    pairs={str(IDS[a]):stats([v[a]-v[b] for v in samples]) for a,b in ((0,1),(2,3),(5,6),(7,8))}
    for d in pairs.values():
        d["G_QS"]=None if d["se"] is None else abs(d["mean"])<=3*d["se"]
    for d in groups.values():
        d["per_primary_mean"]=None if d["mean"] is None else d["mean"]/2
        d["per_primary_se"]=None if d["se"] is None else d["se"]/2
    result=dict(primary=prim,weakShower=w,E=E,seed=seed,settings=settings,version=importlib.metadata.version("pythia8mc"),accepted=accepted,failed=failed,rejected=rejected,attempts=accepted+failed+rejected,charge_bad=charge_bad,energy_bad=energy_bad,max_energy_residual=max_res,seconds=time.time()-start,species=species,groups=groups,charge_pairs=pairs,gates={"G_MC":accepted==2000,"G_Q":charge_bad==0,"G_E":energy_bad==0})
    (out/f"{tag}.json").write_text(json.dumps(result,indent=2,allow_nan=False))
    print(json.dumps(result,allow_nan=False),flush=True)
    if not all(result["gates"].values()): sys.exit(2)
if __name__=="__main__": main()
