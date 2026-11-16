#!/usr/bin/env python3
"""ROT027 read-only original v2.3 BBN PYTHIA tables current/old numerical comparison.
Required input exact Wu-Xu pinned SHA and 161495983-byte official tar.bz2.
No BlackHawk/JULIA execution. No redistribution of original source or tables.
"""
import sys, tarfile, hashlib, json, tempfile, pathlib, shutil, itertools
from decimal import Decimal, InvalidOperation

V23_SHA="dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7"
V23_SIZE=161495983
FIVE=("pipm","Kpm","K0L","proton","neutron")
M={
"pipm": ("603f8b1a53efe316b4378da9a6242c1a1b3be026c17fbdaa917cb07f13850ac4","39306be56e4feeeb361c23983e64b7c4f193c60be4ffa7211b745275cad679fa"),
"Kpm": ("2ac524d17a4d7314fd994f612d482f0f8dfc247fa71fad9b39f776671a23060d","e19d5fe9e15ab378ac81ab2da8c5581ac089f1b09ddd17b5bc209d1867a309b2"),
"K0L": ("05f011a903c7f531e5414d47e515a2e616a619c71772b43c2fb4865ccc63e8cc","7fa26124a55aa3829733fdfb450ac70bbe0a1a292494db41912b29de5674972e"),
"proton": ("c684958259aaaf834d5f7caec91ae8bb3a3e73d8bab049efb3cc7dbb852aa8d9","320b06bdd60123e593e0739984cbae363e2c892453bbf11e6baf9c3e3beab584"),
"neutron": ("f20ba13c0db4b4b59159ad427062a695665a85ee2b0cf63a9c38ba35b56d1945","c47ea846f13a625ac285b968c89ec3b732f07c8029c0a9eceea134639e9cf210")}
PATH_PREFIX="blackhawk_v2.3/src/tables/hadronization_tables/pythia_tables/"
GIT_SOURCE="Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d"
def sha(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for block in iter(lambda:f.read(1<<20),b""):h.update(block)
 return h.hexdigest()

def numeric_equal(s,t):
 if s==t:return True
 try:
  x,y=Decimal(s.decode("ascii")),Decimal(t.decode("ascii"))
  return x.is_finite() and y.is_finite() and x==y
 except (InvalidOperation,UnicodeError):return False

def compare_file(a,b):
 n=0; byteeq=0; token_eq=0; numeq=0; num_mismatch=0
 first=None; examples=[];lines_old=0
 sizes=[]; types={}
 with open(a,"rb") as f,open(b,"rb") as g:
  for pos,(u,v) in enumerate(itertools.zip_longest(f,g),1):
   if u is None or v is None:
    raise AssertionError(f"Different physical row counts at {pos}")
   n+=1
   if pos in (1,2,3,4,5,100,1000,100000,125001):
    examples.append({"line":pos,"current_bytes":len(u),"old_bytes":len(v),
                    "current_token_count":len(u.split()),"old_token_count":len(v.split()),
                    "current_line_sha256":hashlib.sha256(u).hexdigest(),
                    "old_line_sha256":hashlib.sha256(v).hexdigest()})
   if u==v:byteeq+=1
   U,V=u.split(),v.split()
   if U==V:token_eq+=1;numeq+=1;continue
   if len(U)!=len(V):
    if first is None:first={"line":pos,"case":"token_count_mismatch",
      "current_token_count":len(U),"old_token_count":len(V)}
    num_mismatch+=1
    continue
   changes=[k for k,(x,y) in enumerate(zip(U,V)) if not numeric_equal(x,y)]
   if changes:
    num_mismatch+=1
    if first is None:
     first={"line":pos,"case":"numeric_or_literal_mismatch",
       "different_col_indices_zero_based":changes[:15],
       "current_tokens":[U[k].decode("ascii","replace")[:64] for k in changes[:8]],
       "old_tokens":[V[k].decode("ascii","replace")[:64] for k in changes[:8]]}
   else:numeq+=1
  assert n>=100000,("unexpected source grid",n)
 return {"rows_compared":n,"raw_byte_equal_rows":byteeq,
         "whitespace_token_equal_rows":token_eq,
         "numeric_equivalent_rows":numeq,
         "numeric_different_rows":num_mismatch,
         "first_numeric_difference":first,"sample_line_shapes_and_hashes":examples}

def run(path):
 p=pathlib.Path(path)
 assert p.stat().st_size==V23_SIZE,"original source archive size mismatch"
 assert sha(p)==V23_SHA,"original archive SHA mismatch"
 data={};interesting=[];source_lines={};table_meta={}
 with tempfile.TemporaryDirectory() as td:
  d=pathlib.Path(td)
  with tarfile.open(p,"r|bz2") as f:
   for m in f:
    if not m.isfile():continue
    k=None
    if m.name.startswith(PATH_PREFIX):
     if m.name.endswith(".txt"):
      q=m.name[len(PATH_PREFIX):]
      if q in (x+".txt" for x in FIVE):k=("current",q[:-4])
      elif q.startswith("old/") and q[4:] in (x+".txt" for x in FIVE):k=("old",q[4:-4])
    if k:
     stream=f.extractfile(m);assert stream
     dest=d/("_".join(k)+".txt")
     hh=hashlib.sha256()
     with dest.open("wb") as out:
      while True:
       c=stream.read(1<<20)
       if not c:break
       out.write(c);hh.update(c)
     digest=hh.hexdigest()
     assert digest==M[k[1]][0 if k[0]=="current" else 1],(m.name,digest,"PINNED_V23_TABLE_MISMATCH")
     data[k]={"path":m.name,"sha256":digest,"bytes":m.size,"temporary_file":str(dest)}
    elif m.name.endswith("src/hadro_pythia.c") or m.name.endswith("src/hadro_herwig.c") or m.name.endswith("src/tables/hadronization_tables/infos.txt") or m.name.endswith("/Makefile"):
     if m.size<100000:
      stream=f.extractfile(m);assert stream
      txt=stream.read().decode("utf-8","replace")
      if m.name.endswith("infos.txt"):
       table_meta["selected_lines"]=[x.strip()[:180] for x in txt.splitlines() if "BBN" in x or "nb_init_en" in x or "Emin_" in x or "Emax_" in x][:65]
      if m.name.endswith("hadro_pythia.c"):
       ll=txt.splitlines()
       source_lines["hadro_pythia_relevant"]=[{"line":i+1,"text":x.strip()[:170]} for i,x in enumerate(ll) if "HARDTABLES" in x or "header" in x or "fopen" in x or ".txt" in x or "read" in x][:35]
      if m.name.endswith("Makefile"):
       relevant=[{"line":i+1,"text":x.strip()[:150]} for i,x in enumerate(txt.splitlines()) if "HARDTABLES" in x or "hadro_pythia" in x or "pythia_tables" in x]
       if relevant: source_lines[m.name]=relevant[:25]
  assert len(data)==10,("expected ten current/old original source BBN tables",list(data))
  result={"original_archive_sha256":V23_SHA,"archive_bytes":V23_SIZE,
  "author_source_ref":GIT_SOURCE,
  "source_direct_tar_verified":True,"source_code_notes":source_lines,"table_meta":table_meta,
  "channels":{},"generator_executed":False,"native_julia_executed":False}
  for species in FIVE:
   current=data[("current",species)];old=data[("old",species)]
   cmp=compare_file(current["temporary_file"],old["temporary_file"])
   result["channels"][species]={
    "current_SHA256":current["sha256"],"old_SHA256":old["sha256"],
    "current_bytes":current["bytes"],"old_bytes":old["bytes"],"bytes_difference_old_minus_current":old["bytes"]-current["bytes"],
    **cmp}
 return result

def synthetic():
 with tempfile.TemporaryDirectory() as td:
  p=pathlib.Path(td)
  x,y=p/"a",p/"b"
  content=(b" 1.0000e+0   2.5e-2 \n"*100001)
  x.write_bytes(content);y.write_bytes(content.replace(b"  2.5",b" 2.50"))
  z=compare_file(x,y)
  assert z["numeric_different_rows"]==0
  y.write_bytes(content.replace(b"2.5e-2",b"2.6e-2"))
  z=compare_file(x,y)
  assert z["numeric_different_rows"]==100001
  return True

if __name__=="__main__":
 assert len(sys.argv)==3
 assert synthetic()
 output=run(sys.argv[1])
 path=pathlib.Path(sys.argv[2])
 path.write_text(json.dumps(output,indent=2,sort_keys=True,ensure_ascii=False)+"\n")
 print(json.dumps({"result":"ORIGINAL_V23_SOURCE_TABLE_COMPARE_PASS",
    "per_channel":{k:{x:v[x] for x in ("rows_compared","numeric_equivalent_rows","numeric_different_rows","first_numeric_difference")} for k,v in output["channels"].items()}},indent=2))
