#!/usr/bin/env python3
"""Mech-S7 rotation 002: conditional Wu-Xu post-source background diagnostic.
Requirements: numpy, pandas, scipy. Input: PUBLIC_ACTIONS.zip PAPER_ACTIONS.zip.
Writes nothing; JSON to stdout. NO full Julia solver/physical endpoint.
"""
import io,sys,json,hashlib
from zipfile import ZipFile
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator
from scipy.integrate import solve_ivp

PUB="75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5"
PAPER="3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e"
FIRST_OFF=1470; TEST_INDEX=1502
Q=939.5654205-938.27208816 # MeV
TAU=878.4                 # seconds
T_NUC=0.078185270688319950 # MeV

def load(path,sha,mapping):
    b=open(path,"rb").read()
    assert hashlib.sha256(b).hexdigest()==sha,"ZIP SHA256 mismatch"
    with ZipFile(io.BytesIO(b)) as z:
        return {key:pd.read_csv(io.BytesIO(z.read("trajectory_"+value+".csv")))
                for key,value in mapping.items()}

def rates(T_GeV):
    x=Q/(1000*T_GeV)
    gamma=(255/TAU)*(12+6*x+x*x)/x**5
    return gamma*np.exp(-x),gamma*(1+np.exp(-x))+1/TAU

def propagate(background,X0):
    b=background
    eta=np.log(b.a.to_numpy()[FIRST_OFF:])
    t=PchipInterpolator(eta,b.t_sec.to_numpy()[FIRST_OFF:])
    T=PchipInterpolator(eta,b.T_GeV.to_numpy()[FIRST_OFF:])
    def rhs(e,y):
        source,sink=rates(T(e))
        return [float(t.derivative()(e))*(source-sink*y[0])]
    s=solve_ivp(rhs,[eta[0],eta[-1]],[X0],t_eval=eta,method="DOP853",
                rtol=2e-11,atol=2e-13,max_step=.01)
    assert s.success
    return s.y[0]

def at_fixed_T(b,ys):
    x=Q/(1000*b.T_GeV.to_numpy()[FIRST_OFF:])
    assert np.all(np.diff(x)>0)
    return float(np.interp(Q/T_NUC,x,ys))

def contrasts(obj):
    return {"exec":obj["paper_exec"]-obj["public_exec"],
            "sym":obj["paper_sym"]-obj["public_sym"]}

def main():
    assert len(sys.argv)==3,"usage: script public.zip paper.zip"
    data={}
    data.update(load(sys.argv[1],PUB,{"public_exec":"current","public_sym":"repaired"}))
    data.update(load(sys.argv[2],PAPER,{"paper_exec":"paper_exec","paper_sym":"paper_sym"}))
    names=list(data)
    for b in data.values():
        assert len(b)==1600 and b.source_active.iloc[FIRST_OFF]==0
        assert np.array_equal(b.a.to_numpy(),data["public_exec"].a.to_numpy())
    x0={k:float(v.Xn.iloc[FIRST_OFF]) for k,v in data.items()}
    frozen={bg:{k:propagate(b,x0[k]) for k in names} for bg,b in data.items()}
    ref="public_exec"
    raw_fixed_a={k:float(v.Xn.iloc[TEST_INDEX]) for k,v in data.items()}
    raw_fixed_T={k:at_fixed_T(v,v.Xn.to_numpy()[FIRST_OFF:]) for k,v in data.items()}
    rep_fixed_a={k:float(frozen[k][k][TEST_INDEX-FIRST_OFF]) for k in names}
    rep_fixed_T={k:at_fixed_T(data[k],frozen[k][k]) for k in names}
    common_a={k:float(frozen[ref][k][TEST_INDEX-FIRST_OFF]) for k in names}
    common_T={k:at_fixed_T(data[ref],frozen[ref][k]) for k in names}
    def decomposition(raw,own,shared):
        actual,owncontrast,sharedcontrast=contrasts(raw),contrasts(own),contrasts(shared)
        return {m:{"raw":actual[m],"common_background":sharedcontrast[m],
                   "saved_background_drift":owncontrast[m]-sharedcontrast[m],
                   "replay_residual":actual[m]-owncontrast[m]} for m in ("exec","sym")}
    result={"archive_SHA256":dict(public=PUB,paper=PAPER),
      "source_commit":"d395183674cace6c9906a8911bdeb7234ba4040d",
      "readout_same_a_idx1502":decomposition(raw_fixed_a,rep_fixed_a,common_a),
      "readout_fixed_T_nuc":decomposition(raw_fixed_T,rep_fixed_T,common_T),
      "common_background_reference_controls":{
        bg:contrasts({k:float(frozen[bg][k][TEST_INDEX-FIRST_OFF]) for k in names})
        for bg in names},
      "ceiling":"SAVED_SOURCEOFF_CONDITIONAL_REPLAY_ONLY; NO_VALID_E2B; NO_PBH_BOUND; NO_CANON; NO_EXEC_SIGN"}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
