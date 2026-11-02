#!/usr/bin/env python3
"""Wu-Xu Fig5 public CODE PATH audit, not a reproduction of the published beta bound.
Python >=3.9 stdlib, requires internet to read pinned upstream GitHub commit.
"""
import hashlib, json
from urllib.request import urlopen
COMMIT="d395183674cace6c9906a8911bdeb7234ba4040d"
BASE="https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/"+COMMIT+"/arXiv-2509.05618/"
P={
 "v3_nb":("main.ipynb","171c4a29e414860d724c817641896628f35982b0"),
 "v1_nb":("arXiv-2509.05618v1/main.ipynb","89a69d1ac23f3024893db51da29c9f573ecf0c5f"),
 "v3_scan":("main-scan.jl","b368ba55d5a493f7bc185909730f7fe5691f10d6"),
 "v3_source":("tool_script-hadrons_from_PBH.jl","cc73432910f872d526113ce59b6204f38d0766a9"),
 "v1_source":("arXiv-2509.05618v1/tool_script-mesons_from_PBH.jl","d9b9b15adaf8e500c67f1d1f1f531ccf26002b35"),
 "v3_jld2":("data/out/scanning.jld2","10cc9b3f078fcadb91b5e520e75845859ca00b74"),
 "v1_jld2":("arXiv-2509.05618v1/data/out/scanning.jld2","ff08072449c4ef46144cb800778224acd9669a8f"),
 "oldlink":("data/out/scanning_old.jld2","5dd0a2032c4612a25c0e1a72ab58d0ad8f8ab084")
}
def read(name):
  path,expected=P[name]
  with urlopen(BASE+path,timeout=45) as stream: data=stream.read()
  gitblob=hashlib.sha1(("blob "+str(len(data))+"\0").encode()+data).hexdigest()
  assert gitblob==expected,(name,gitblob,expected)
  return data
def code(nb,i):return "".join(nb["cells"][i]["source"])
def main():
  d={name:read(name) for name in P}
  n=json.loads(d["v3_nb"]);old=json.loads(d["v1_nb"])
  sr=d["v3_source"].decode();scan=d["v3_scan"].decode()
  assert 'include("tool_script-hadrons_from_PBH.jl")' in code(n,4) and 'include("tool_script-hadrons_from_PBH.jl")' in scan
  assert sr.count("ExtrapolationType.Linear")==5
  assert "dN_over_dt_π(m_PBH) * n_PBH" in code(n,9) and "dN_over_dt_π(m_PBH) * n_PBH" in scan
  assert 'io["Y_P_mat"]' in scan and 'io["chi2_mat"]' in scan
  plot=code(n,14)
  assert 'scanning.jld2' in plot and 'scanning_old.jld2' in plot
  assert 'plot_basename = "Y_P"' in plot and 'plot_basename = "Y_P_with_v1"' in plot
  assert plot.index('plot_basename = "Y_P"') < plot.index('χ²_old_mat;')
  assert "linestyle=:dash" in plot and 'save_plot_flag = false' in code(n,3)
  assert 'include("tool_script-mesons_from_PBH.jl")' in code(old,4)
  assert d["v1_source"].count(b"ExtrapolationType.Linear")==3
  assert len([x for x in code(n,9).splitlines() if x.strip().startswith("du[")])==10
  assert len([x for x in code(old,9).splitlines() if x.strip().startswith("du[")])==8
  assert d["oldlink"].decode()=="../../arXiv-2509.05618v1/data/out/scanning.jld2"
  assert b"Julia 1.12.3" in d["v3_jld2"][:120]
  assert b"Julia 1.11.6" in d["v1_jld2"][:120]
  print(json.dumps({"code_path":"PASS", "old_overlay":"SEPARATE_8D_MODEL",
   "historical_exact_fig5_provenance":"OPEN","E4":"HOLD/SOURCE_BLOCK",
   "no_claim":"NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN"},indent=2))
if __name__=="__main__":main()
