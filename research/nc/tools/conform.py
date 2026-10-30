import os, re, glob

# Doprowadzenie naglowkow zwrotow NC do zgodnosci z docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md
# par.2 pkt 7: artifact_id | exposure | canonical_body_path | source_revision/commit |
#             bw_event_or_pending | claim_ceiling | HOLD
# Commit nie moze byc w ciele pliku (plik nie zna wlasnego hasha) — rozwiazuje go git log
# dla danej sciezki; manifest i linia zwrotna podaja commit po zapisie.

BASE = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18"
os.chdir(BASE)

CEIL = ("NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / "
        "MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY")

def block(fn):
    return (
        "<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->\n"
        "```text\n"
        f"artifact_id          : {fn[:-3]}\n"
        "exposure             : PUBLIC_SAFE\n"
        f"canonical_body_path  : research/nc/2026-10-18/{fn}\n"
        "source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`\n"
        "bw_event_or_pending  : GITHUB_PENDING_BW_INGEST\n"
        f"claim_ceiling        : {CEIL}\n"
        "hold                 : BRAK\n"
        "```\n"
    )

files = sorted([f for f in glob.glob("*.md") if f != "README.md" and not f.startswith("MANIFEST_NC")])
dodane, pominiete = [], []
for f in files:
    s = open(f, encoding="utf-8").read()
    if "IW_CONFORMANCE_BLOCK" in s:
        pominiete.append(f); continue
    L = s.split("\n")
    # wstaw po pierwszym naglowku H1 oraz po ewentualnych banerach erraty
    idx = None
    for i, x in enumerate(L):
        if x.startswith("# "): idx = i + 1; break
    if idx is None:
        pominiete.append(f); continue
    # przeskocz baner(y) erraty bezposrednio po H1
    while idx < len(L) and (L[idx].strip() == "" or L[idx].lstrip().startswith(">")):
        idx += 1
    L.insert(idx, "\n" + block(f))
    open(f, "w", encoding="utf-8").write("\n".join(L))
    dodane.append(f)

print("blok dodany     :", len(dodane))
print("pominiete       :", len(pominiete), pominiete if pominiete else "")

# manifest
lines = ["# MANIFEST NC — linie zwrotne wg routing §2.7", "",
         "Wiersze w formacie wymaganym przez `docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md` §2 pkt 7.",
         "`source_revision` rozwiazuje `git log -- <canonical_body_path>`; `bw_event_or_pending` wynosi",
         "`GITHUB_PENDING_BW_INGEST` dla wszystkich pozycji, bo zaden zwrot NC nie ma jeszcze zdarzenia BW.",
         "", "```text"]
for f in files:
    lines.append(f"{f[:-3]} | PUBLIC_SAFE | research/nc/2026-10-18/{f} | git-log | GITHUB_PENDING_BW_INGEST | {CEIL} | BRAK")
for f in sorted(glob.glob("*.csv")):
    lines.append(f"{f[:-4]} | PUBLIC_SAFE | research/nc/2026-10-18/{f} | git-log | GITHUB_PENDING_BW_INGEST | {CEIL} | BRAK")
lines += ["```", "",
          "## Czego ten manifest NIE robi", "",
          "Nie rejestruje zdarzenia BW i nie twierdzi `SYNCED`. Rejestracja w `REGISTRY`",
          "i `CROSS_SURFACE_CUSTODY` nalezy do uprawnionego wlasciciela procesu BW, nie do NC —",
          "zgodnie z routing §2 pkt 5. Do tego czasu kazda pozycja stoi na `GITHUB_PENDING_BW_INGEST`."]
open("MANIFEST_NC_20261018.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("manifest        : MANIFEST_NC_20261018.md,", len(files), "zwrotow +", len(glob.glob("*.csv")), "csv")
