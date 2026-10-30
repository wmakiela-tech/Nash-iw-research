import csv

P = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv"
with open(P, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
hdr, body = rows[0], rows[1:]

NEW = [
    ["NC-FAL-024", "NC", "2026-10-25",
     "ART029 par.4 orzekl, ze konfiguracja maksymalizujaca JEST konfiguracja back-action evading/QND i podal arXiv:1608.06152v2 jako dojrzalego hosta. Moja wlasna PREREG_ALIGN.md z 18 X par.4 tego ZABRANIA z podana przyczyna merytoryczna.",
     "NC (autokorekta z wlasnej inicjatywy, przed audytem zewnetrznym); DS/R1 ma rozstrzygnac zakres wycofania",
     "[\U0001f534] FALSIFIED", "ART032 par.1",
     "CYTAT Z WLASNEJ PREREGESTRACJI 18 X: 'phi = pi/2 z TLUMIENIEM nie jest modelem kwantowym. Kwantowa reakcja zwrotna przy pomiarze jednej kwadratury to SZUM na sprzezonej, nie tlumienie jej. Szum podnosi A^2 zamiast je obnizac i psuje przyszle odczyty innym kanalem. Tego NIE modeluje i nie bede z tego wnosil o przypadku kwantowym. COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM.' PRZYCZYNA JEST MERYTORYCZNA: w naszym modelu D_d(u)=I-(1-u)dd^T jest DYSSYPACJA, back-action OBNIZA A^2, i dlatego d prostopadle do stanu daje pomiar zerokosztowy; w kwantowym BAE back-action to SZUM na sprzezonej kwadraturze, ktory PODNOSI wariancje. Zbieznosc jest w algebrze rozdzielenia kierunkow, nie w mechanizmie. WYCOFUJE: zdanie, ze to JEST BAE/QND, oraz arXiv:1608.06152v2 jako hosta. ZOSTAJE: analogia STRUKTURALNA, jawnie oznaczona jako analogia, bez przenoszenia wnioskow fizycznych. TYP CLAIMU: interpretacyjny/fizyczny, nie numeryczny — poprawna liczba sqrt(m) NIE autoryzowala interpretacji. Zasada projektu zadziala przeciw mnie tam, gdzie jest napisana. SKUTEK ODWROTNY, KTOREGO NIE TRAKTUJE JAKO POCIESZENIA: skoro BAE nie jest hostem, tresc par.4 nie jest cudza, lecz MOJA Z 18 X (NC-FAL-023). Oba ustalenia obowiazuja jednoczesnie. Blad popelniony W AKAPICIE PRZEDSTAWIANYM JAKO ODEJMOWANIE STANU WIEDZY, czyli jako dowod rygoru. origin_failure_mode: MADE_A_PHYSICAL_HOST_IDENTIFICATION_MY_OWN_PREREGISTRATION_HAD_EXPLICITLY_FORBIDDEN.",
     "[OBSERVED]", "P_SIMULATED", "NONE"],

    ["NC-FAL-025", "NC", "2026-10-25",
     "ART031 par.5 proponowal regule 'przejscie po CLAIM_ROWS_NC'. Niewystarczajace: przeszedlem po rejestrze i w ciagu dwoch godzin sam przeoczylem PREREG_ALIGN.md oraz l2.py/l2d.py — w tym caveat zakazujacy claimu fizycznego.",
     "NC (samozgloszenie)",
     "[\U0001f534] FALSIFIED", "ART032 par.4",
     "TA SAMA WADA CO POPRAWKA KROK 0 PO ART018: poprawka skrojona do ostatniego OBJAWU, nie do MECHANIZMU. Dwa razy z rzedu, i to jest wlasciwy wzorzec do zapisania, nie pojedyncze pominiecia. POPRAWIONA PROPOZYCJA (NC-OPN-027 wersja 2): przejscie po wlasnym dorobku obejmuje TRZY powierzchnie — (a) CLAIM_ROWS_NC, (b) WSZYSTKIE wlasne preregestracje, (c) katalog kodu z dat pracy nad ta sama wielkoscia — z wynikiem per powierzchnia, wpisanym przed uruchomieniem kodu. origin_failure_mode: PATCHED_A_PRIOR_ART_RULE_WITH_THE_NARROWEST_SURFACE_THAT_WOULD_HAVE_CAUGHT_THE_LAST_MISS.",
     "[OBSERVED]", "P_SIMULATED", "NONE"],
]

for r in NEW:
    assert len(r) == len(hdr), (r[0], len(r), len(hdr))
ids = {r[0] for r in body if r}
for r in NEW:
    assert r[0] not in ids, "duplikat " + r[0]

AT = {
 "NC-NUM-001": ("ZAKRES DOPISANY 2026-10-25 (ART032 par.3): wynik dotyczy przypadku "
   "WSPOLOSIOWEGO (e=d) na JEDNYM generatorze, nie modelu. Sprawdzone w kodzie: l2.py nie "
   "zawiera phi ani razu, odczyt i tlumienie ida po tej samej osi (c.append(y*(1-u)/gam); y=y*u), "
   "a ewolucja swobodna jest obrotem, czyli mu_2=0. '280000 losowych protokolow' to losowania "
   "CZASOW I SIL przy e=d. Wiersz czyta sie jako poparcie sufitu 1 W MODELU; w modelu ze "
   "swobodnymi (e,d) sufit to sqrt(m), co pokazuje l2d.py W TYM SAMYM KATALOGU Z TEGO SAMEGO DNIA. "
   "Maksimum DOKLADNIE 1.000000000 z 280 tysiecy losowan nie jest podpisem granicy, lecz podpisem "
   "zawezonej parametryzacji. Liczba NIE wycofana — jest poprawna i rowna dzisiejszemu P3. "
   "Rodzina NC-FAL-018, z dodatkiem: parametryzacja z konstrukcji wykluczala konfiguracje "
   "naruszajaca, a kod ja znajdujacy lezal obok. | "),
 "NC-NUM-003": ("ZAKRES POTWIERDZONY 2026-10-25 (ART032 par.3): gen4.py tez nie zawiera phi, "
   "czyli lamanie sufitu w 12/12 generatorow z mu_2>0 uzyskano PRZY e=d. To czyni wiersz "
   "MOCNIEJSZYM, niz mu przypisywalem, i spojnym z V5 z ART029 (przy silnym mu_2>0 kat nie "
   "rzadzi, separator daje 2.14e10 nawet przy e=d). Bez korekty. | "),
 "NC-FAL-022": ("WAGA PODNIESIONA 2026-10-25 (ART032 par.2): zapisalem ten blad jako "
   "'preregestrowalem falsyfikator z tozsamosci bez sprawdzenia jej zakresu'. Falszywie lagodnie. "
   "Zakres BYL sprawdzony i zapisany szesc dni wczesniej moja wlasna reka: PREREG_ALIGN.md par.3 "
   "z 18 X mowi 'Twierdzenie 1 z ART009 nie jest twierdzeniem o reakcji zwrotnej. Jest "
   "twierdzeniem o reakcji zwrotnej WSPOLOSIOWEJ z odczytem. Nazwa i sformulowanie w ART009 sa "
   "wtedy za szerokie i trzeba je zwezic.' Nie przeoczylem dziedziny — ZIGNOROWALEM WLASNA "
   "DOKUMENTACJE. origin_failure_mode skorygowany: "
   "IGNORED_MY_OWN_DOCUMENTED_DOMAIN_RESTRICTION_WHEN_WRITING_A_FALSIFIER_SIX_DAYS_LATER. | "),
 "NC-ALG-021": ("HOST WYCOFANY 2026-10-25 (ART032 par.1): identyfikacja tej konfiguracji jako "
   "BAE/QND jest WYCOFANA — moja wlasna PREREG_ALIGN par.4 zabraniala tego wnioskowania, bo nasz "
   "back-action jest dyssypacja obnizajaca A^2, a kwantowy BAE to szum podnoszacy wariancje. "
   "Zostaje analogia STRUKTURALNA, jawnie jako analogia. Patrz NC-FAL-024. | "),
}
upd = 0
for r in body:
    if r and r[0] in AT:
        r[7] = AT[r[0]] + r[7]
        upd += 1
assert upd == len(AT), upd

# NC-OPN-027 -> wersja 2
v2 = 0
for r in body:
    if r and r[0] == "NC-OPN-027":
        r[3] = ("WERSJA 2 (ART032 par.4): przejscie po wlasnym dorobku obejmuje TRZY powierzchnie "
                "— (a) CLAIM_ROWS_NC, (b) wszystkie wlasne preregestracje, (c) katalog kodu z dat "
                "pracy nad ta sama wielkoscia; wynik per powierzchnia wpisany PRZED uruchomieniem "
                "kodu. WERSJA 1 (ART031, tylko CLAIM_ROWS_NC) OBALONA przeze mnie w ciagu dwoch "
                "godzin — patrz NC-FAL-025")
        r[7] = ("WERSJA 1 PADLA: przeszedlem po rejestrze zgodnie z wlasna propozycja i nadal "
                "przeoczylem PREREG_ALIGN.md oraz l2.py/l2d.py, czyli najwazniejsza powierzchnie "
                "— w tym caveat zakazujacy claimu fizycznego (NC-FAL-024). | " + r[7])
        v2 += 1
assert v2 == 1, v2

body += NEW
with open(P, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(hdr); w.writerows([r for r in body if r])

st = {}
for r in body:
    if r:
        st[r[5]] = st.get(r[5], 0) + 1
print("wierszy:", len([r for r in body if r]), "| atrybucje:", upd, "| OPN-027 -> wersja", v2+1)
for k in sorted(st):
    print(f"  {k:<22} {st[k]}")
