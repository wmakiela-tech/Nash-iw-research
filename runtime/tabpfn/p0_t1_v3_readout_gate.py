#!/usr/bin/env python3
"""
IW / NASH — TabPFN P0-T1 V3 readout compatibility gate 003
Exact-source pin:
  TabPFN core commit: fa9b33344bc37b8a896f40efaf9ec5f331057615 (v8.3.0)
  tabpfn-extensions commit: 572858f20a925b27f26236b000da33b3c9b89d11
Fail closed. Compatibility only.
"""

from __future__ import annotations
import hashlib, importlib.metadata as im, json, os, platform, sys, traceback
from pathlib import Path
from typing import Any
import numpy as np

OUT=Path(os.environ.get("IW_TABPFN_P0_T1_OUT","./IW_TABPFN_P0_T1_V3_OUTPUT"))
OUT.mkdir(parents=True,exist_ok=True)

CORE_COMMIT="fa9b33344bc37b8a896f40efaf9ec5f331057615"
EXT_COMMIT="572858f20a925b27f26236b000da33b3c9b89d11"
SEED=20260816
N_TRAIN=128
N_QUERY=12
ROW_SUM_TOL=5e-6
NEG_TOL=1e-8
PRED_PERM_TOL=5e-5
WEIGHT_PERM_TOL=5e-5

def sha256_file(p:Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def pkg(name:str)->str:
    return im.version(name)

def direct_url(name:str):
    try:
        raw=im.distribution(name).read_text("direct_url.json")
        return json.loads(raw) if raw else None
    except Exception:
        return None

def vcs_commit(d):
    if not isinstance(d,dict): return None
    return ((d.get("vcs_info") or {}).get("commit_id"))

def j(x:Any)->Any:
    if isinstance(x,Path): return str(x)
    if isinstance(x,np.ndarray): return x.tolist()
    if isinstance(x,(str,int,float,bool)) or x is None:return x
    if isinstance(x,dict):return {str(k):j(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [j(v) for v in x]
    if hasattr(x,"__dict__"):
        try:return {str(k):j(v) for k,v in vars(x).items() if not str(k).startswith("_")}
        except Exception:pass
    return str(x)

result={
 "artifact_id":"IW_MGPT_BUD_01_TABPFN_P0_T1_V3_READOUT_COMPATIBILITY_003_20260816",
 "mission":"IW_TABPFN_DEPLOYMENT_SHIFT_RESEARCH_MISSION_001_20260816",
 "scope":"compatibility only; no RET scientific result",
 "status":"RUNNING",
 "expected":{"tabpfn_version":"8.3.0","core_commit":CORE_COMMIT,"extensions_commit":EXT_COMMIT,"model":"V3"}
}

try:
    if not os.environ.get("TABPFN_TOKEN"):
        raise RuntimeError(
          "TABPFN_TOKEN missing. Accept Prior Labs model license and provide token "
          "via runtime secret/environment; never paste it into project artifacts."
        )

    import torch
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from tabpfn import TabPFNClassifier
    from tabpfn.constants import ModelVersion
    from tabpfn_extensions.interpretability import get_decoder_readout,class_vote

    du_core=direct_url("tabpfn")
    du_ext=direct_url("tabpfn-extensions")
    result["environment"]={
      "python":sys.version,
      "platform":platform.platform(),
      "numpy":np.__version__,
      "torch":torch.__version__,
      "tabpfn":pkg("tabpfn"),
      "tabpfn_extensions":pkg("tabpfn-extensions"),
      "tabpfn_direct_url":du_core,
      "extensions_direct_url":du_ext,
      "cuda_available":bool(torch.cuda.is_available()),
      "cuda_device":torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
    }
    if pkg("tabpfn")!="8.3.0":
        raise AssertionError(f"core version mismatch: {pkg('tabpfn')}")
    if vcs_commit(du_core)!=CORE_COMMIT:
        raise AssertionError(f"core VCS commit mismatch: {vcs_commit(du_core)}")
    if vcs_commit(du_ext)!=EXT_COMMIT:
        raise AssertionError(f"extensions VCS commit mismatch: {vcs_commit(du_ext)}")

    np.random.seed(SEED); torch.manual_seed(SEED)
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(SEED)

    X,y=load_breast_cancer(return_X_y=True)
    X=X.astype(np.float32); y=y.astype(int)
    Xtr,Xq,ytr,yq=train_test_split(
      X,y,train_size=N_TRAIN,test_size=N_QUERY,random_state=SEED,stratify=y
    )
    device="cuda" if torch.cuda.is_available() else "cpu"

    def make_clf():
        return TabPFNClassifier.create_default_for_version(
          ModelVersion.V3,
          device=device,
          random_state=SEED,
          n_estimators=8,
          softmax_temperature=1.0,
          balance_probabilities=False,
          fit_mode="fit_preprocessors",
          inference_precision=torch.float32,
          show_progress_bar=False,
        )

    clf=make_clf()
    clf.fit(Xtr,ytr)
    proba=np.asarray(clf.predict_proba(Xq),float)

    mp=Path(str(clf.model_path))
    result["checkpoint"]={
      "path":str(mp),"exists":mp.exists(),
      "sha256":sha256_file(mp) if mp.exists() else None,
      "size_bytes":mp.stat().st_size if mp.exists() else None,
    }
    if not mp.exists(): raise AssertionError("checkpoint path does not exist after fit")

    result["inference_config"]=j(clf.get_inference_config())

    dec=[m for m in clf.model_.modules() if type(m).__name__=="ManyClassDecoder"]
    result["decoder"]={"ManyClassDecoder_count":len(dec)}
    if len(dec)!=1: raise AssertionError(f"expected 1 ManyClassDecoder, found {len(dec)}")

    w,idx=get_decoder_readout(clf,Xq,average_over_estimators=True)
    w=np.asarray(w,float); idx=np.asarray(idx,int)
    result["readout"]={
      "shape":list(w.shape),
      "indices_shape":list(idx.shape),
      "unique_indices":int(len(np.unique(idx))),
      "min_weight":float(w.min()),
      "max_row_sum_error":float(np.max(np.abs(w.sum(axis=1)-1.0))),
    }
    if w.shape!=(N_QUERY,N_TRAIN):raise AssertionError(f"bad shape {w.shape}")
    if not np.array_equal(np.sort(idx),np.arange(N_TRAIN)):
        raise AssertionError("train_indices not bijection over fitted rows")
    if w.min() < -NEG_TOL:raise AssertionError("negative decoder weights")
    if np.max(np.abs(w.sum(axis=1)-1.0))>ROW_SUM_TOL:
        raise AssertionError("decoder rows do not sum to one")

    y_aligned=ytr[idx]
    votes,classes=class_vote(w,y_aligned,classes=np.asarray(clf.classes_))
    votes=np.asarray(votes,float)
    vote_diff=float(np.max(np.abs(votes-proba)))
    result["class_vote"]={"max_abs_diff_predict_proba":vote_diff}
    if vote_diff>1e-3:
        raise AssertionError(f"class_vote mismatch {vote_diff} > 1e-3")

    perm=np.random.default_rng(SEED+1).permutation(N_TRAIN)
    clf2=make_clf(); clf2.fit(Xtr[perm],ytr[perm])
    proba2=np.asarray(clf2.predict_proba(Xq),float)
    w2,idx2=get_decoder_readout(clf2,Xq,average_over_estimators=True)
    w2=np.asarray(w2,float); idx2=np.asarray(idx2,int)

    orig1=idx
    orig2=perm[idx2]
    ord1=np.argsort(orig1); ord2=np.argsort(orig2)
    if not np.array_equal(orig1[ord1],np.arange(N_TRAIN)):
        raise AssertionError("fit1 original-ID map failed")
    if not np.array_equal(orig2[ord2],np.arange(N_TRAIN)):
        raise AssertionError("fit2 original-ID map failed")
    wdiff=float(np.max(np.abs(w[:,ord1]-w2[:,ord2])))
    pdiff=float(np.max(np.abs(proba-proba2)))
    result["row_permutation_guard"]={
      "prediction_max_abs_diff":pdiff,
      "readout_after_unpermute_max_abs_diff":wdiff,
      "prediction_tol":PRED_PERM_TOL,
      "readout_tol":WEIGHT_PERM_TOL,
    }
    if pdiff>PRED_PERM_TOL or wdiff>WEIGHT_PERM_TOL:
        raise AssertionError(f"row permutation guard failed pred={pdiff} readout={wdiff}")

    result["status"]="P0_T1_V3_PASS"
    result["gate"]={"verdict":"PASS","authorize":["P0_A_RET_V3","P0_B_CONTEXT_VOLATILITY_V3"]}

except Exception as e:
    result["status"]="P0_T1_V3_ERROR"
    result["error"]={"type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()}
    result["gate"]={"verdict":"ERROR","authorize":[]}

(OUT/"P0_T1_V3_result.json").write_text(json.dumps(j(result),indent=2,ensure_ascii=False),encoding="utf-8")
manifest={
 "source_file":Path(__file__).name if "__file__" in globals() else "notebook",
 "source_sha256":sha256_file(Path(__file__)) if "__file__" in globals() and Path(__file__).exists() else None,
 "core_commit":CORE_COMMIT,"extensions_commit":EXT_COMMIT,
 "status":result["status"],"gate":result["gate"]
}
(OUT/"P0_T1_V3_manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
print(json.dumps(j(result),indent=2,ensure_ascii=False))
if result["gate"]["verdict"]!="PASS": raise SystemExit(2)
