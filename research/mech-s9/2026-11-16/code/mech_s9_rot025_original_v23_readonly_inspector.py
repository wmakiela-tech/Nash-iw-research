#!/usr/bin/env python3
"""Read-only exact BlackHawk v2.3 source archive inspector. No code execution."""
import sys, pathlib, hashlib, tarfile, json, re

SHA="dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7"
SIZE=161495983
NAMES=("pipm","K0L","Kpm","proton","neutron")
PDGS={"pipm":211,"K0L":130,"Kpm":321,"proton":2212,"neutron":2112}

def check_sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b)
    return h.hexdigest()

def wanted_source(path):
    q=path.lower()
    return any(q.endswith(s) for s in (
       "/scripts/pythia_scripts/table_up.cc",
       "/scripts/pythia_scripts/table_gluon.cc",
       "/scripts/pythia_scripts/formatting.c",
       "/scripts/herwig_scripts/mc_particle_counts.cc",
       "/scripts/herwig_scripts/formatting.c",
       "/src/secondary.c","/src/hadro_pythia.c","/src/hadro_herwig.c",
       "/src/tables/hadronization_tables/infos.txt",
       "/src/tables/write_secondary_bbn.txt"))

def wanted_table(path):
    q=path.lower()
    if not ("/hadronization_tables/pythia_tables/" in q
            or "/hadronization_tables/herwig_tables/" in q):
        return False
    return q.split("/")[-1] in tuple(n.lower()+".txt" for n in NAMES)

def inspect(path):
    assert path.stat().st_size==SIZE,"source archive SIZE mismatch"
    assert check_sha(path)==SHA,"source archive SHA mismatch"
    src, data, files={}, {}, 0
    with tarfile.open(path,"r:bz2") as tar:
        for m in tar:
            if not m.isfile(): continue
            files+=1
            name=m.name
            if not wanted_source(name) and not wanted_table(name): continue
            stream=tar.extractfile(m)
            assert stream is not None
            raw=stream.read()
            assert len(raw)==m.size
            item={"path":name,"bytes":m.size,"sha256":hashlib.sha256(raw).hexdigest()}
            if wanted_table(name):
                data[name]=item
                continue
            txt=raw.decode("utf-8","replace")
            item["pdg_sign_presence"]={k:{"positive":bool(re.search(r"(?<!\d)"+str(v)+r"(?!\d)",txt)),
                        "negative":bool(re.search(r"(?<!\d)-"+str(v)+r"(?!\d)",txt))}
                        for k,v in PDGS.items()}
            item["has_abs_pdgId"]=bool(re.search(r"abs\s*\([^)]*pdgId",txt))
            if name.lower().endswith("/infos.txt"):
                item["energy_metadata"]=[x.strip() for x in txt.splitlines()
                    if any(y in x for y in ("Emin_hadro_pythia","Emax_hadro_pythia",
                       "Emin_hadro_herwig","Emax_hadro_herwig",
                       "nb_init_en_pythia","nb_init_en_herwig"))][:16]
            if "/pythia_scripts/" in name.lower() and name.lower().endswith(".cc"):
                item["signed_pdg_conditions"]=[x.strip()[:180] for x in txt.splitlines()
                    if "id()" in x and any(str(v) in x for v in (211,321,2212,2112))][:12]
            if "/herwig_scripts/" in name.lower() and name.lower().endswith(".cc"):
                item["pdg_source_lines"]=[x.strip()[:180] for x in txt.splitlines()
                    if "pdgId" in x or "_ids={" in x][:8]
            # Detailed original-source seam: context is restricted to short
            # relevant source spans, never full redistribution of C files.
            ll=txt.splitlines()
            lname=name.lower()
            if lname.endswith("/scripts/pythia_scripts/formatting.c"):
                item["primary_parton_normalization_lines_65_77"]=[
                  f"{i+1}: {ll[i].strip()[:180]}"
                  for i in range(64,min(77,len(ll)))]
                item["primary_loop_and_divisor2"]=(
                   any("nb_initial_particles" in x for x in ll[63:77])
                   and any("/2." in x or "/ 2." in x for x in ll[63:77]))
            if lname.endswith("/src/hadro_pythia.c"):
                item["hadro_pythia_header_loader_lines_8_25"]=[
                  f"{i+1}: {ll[i].strip()[:160]}"
                  for i in range(7,min(25,len(ll)))]
                item["uses_precomputed_pythia_header"]="hadronization_tables_pythia.h" in txt
            if lname.endswith("/src/hadro_herwig.c"):
                item["uses_precomputed_herwig_header"]="hadronization_tables_herwig.h" in txt
            if lname.endswith("/src/secondary.c"):
                item["secondary_convolution_core_lines"]=[
                  f"{i+1}: {ll[i].strip()[:170]}"
                  for i in range(len(ll))
                  if 758<=i<=784 and (
                  "for(int i" in ll[i] or "temp +=" in ll[i]
                  or "contribution_instantaneous" in ll[i]
                  or "hadronization_choice" in ll[i])]
            src[name]=item
    assert len(src)>=3,"too few source files found, not a source admission"
    return {"source":"Arbey-Auffinger official BlackHawk v2.3 archive",
      "verified_against":"Wu-Xu Artifacts.toml@d395183",
      "exact_archive_sha256":SHA,"exact_archive_bytes":SIZE,
      "archive_regular_files":files,"source_files":list(src.values()),
      "selected_raw_BBN_tables":list(data.values()),"count_raw_tables":len(data),
      "archive_identity_verified":True,"generator_executed":False,"julia_executed":False,
      "limitations":["original Wu-Xu runtime table instance not independently proven",
        "source code counters do not establish per-charge normalisation by themselves",
        "no physical beta, Xn, Yp or PBH bound","NO_CANON","NO_EXEC_SIGN"]}

def main():
    assert len(sys.argv)==3
    path=pathlib.Path(sys.argv[1])
    out=pathlib.Path(sys.argv[2])
    out.mkdir(parents=True,exist_ok=True)
    res=inspect(path)
    (out/"ORIGINAL_V23_SOURCE_ONLY_RESULT.json").write_text(
      json.dumps(res,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
    print("SOURCE_ADMISSION_PASS",len(res["source_files"]),res["count_raw_tables"])

if __name__=="__main__":
    main()
