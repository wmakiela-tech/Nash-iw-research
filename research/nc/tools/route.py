import csv, re

P = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv"
with open(P, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
hdr, body = rows[0], rows[1:]

# Przypisanie wedle ZADEKLAROWANEJ FUNKCJI komorki (routing projektu), nie wedle wygody.
# Liczba w nawiasie = miejsce w kolejce TEJ komorki. Prosze tylko o pozycje 1.
ASSIGN = {
 # DS/R1 — falsyfikacja, granice claimow
 "NC-ALG-021": ("DS/R1 [1]", "Czy wycofanie hosta kwantowego wystarcza, czy cala analogia strukturalna ma wyjsc z artefaktu. PYTANIE PRZECIW MOJEMU INTERESOWI: wycofanie hosta zwraca tresc mnie, wiec moj osad jest tu kupiony."),
 "NC-ALG-001": ("DS/R1 [2]", "Tozsamosc ksiegowa przy d=e — czy zapis dziedziny jest teraz poprawny I ZUPELNY. To ta tozsamosc, z ktorej zbudowalem zly falsyfikator F5 (NC-FAL-022), majac zakres zapisany szesc dni wczesniej."),
 "NC-ALG-005": ("DS/R1 [3]", "Prawo kata |sin phi| — teraz nosne dla ART029 par.5 po korekcie atrybucji. Granica: czy |sin phi| jest nadmiarem NA POMIAR, czy na caly protokol."),
 "NC-ALG-013": ("DS/R1 [4]", "Dokladna formula bledu naiwnego rozniczkowania — granice claimu."),
 "NC-ALG-014": ("DS/R1 [5]", "Oszacowanie przez komutator z czynnikiem e^{mu_2(A)} — czy ciasne."),
 "NC-ALG-015": ("DS/R1 [6]", "Prawo widocznosci Q80 — granice; zwiazane z NC-OPN-022 (nieznana prehistoria)."),
 "NC-ALG-016": ("DS/R1 [7]", "Tabela dualnosci Q80 — czy zupelna."),
 "NC-ALG-003": ("DS/R1 [8]", "sqrt(tanh(gamma s/2)) przy ustalonej sile — zakres: to granica m->inf przy e=d (potwierdzone chk18.py do 12 cyfr)."),
 "NC-ALG-004": ("DS/R1 [9]", "1/sqrt(1-e^{-2 gamma s}) jako ILORAZ, nie granica bezwzgledna — czy sformulowanie wiersza to oddaje."),

 # Gemini — testbed, runtime, mechanizm
 "NC-NUM-001": ("Gemini [1]", "PRZEBIEG KONTROLNY: powtorzyc skan ze SWOBODNYMI (e,d), nie e=d. l2.py ma e=d zahardkodowane i dlatego dal maksimum dokladnie 1.000000000 z 280 tys. losowan. Pytanie: czy Wasz testbed znajduje naroznik sqrt(m) przy losowym starcie, czy tez trzeba go skonstruowac."),
 "NC-NUM-002": ("Gemini [2]", "Tozsamosc termwise na 112547 pomiarach, odchylenie 3.33e-16 — reprodukowalnosc."),
 "NC-NUM-003": ("Gemini [3]", "12/12 generatorow z mu_2>0; gen4.py tez bez phi, czyli przy e=d. Czy to zmienia Wasze odczytanie."),
 "NC-NUM-004": ("Gemini [4]", "Wzor sqrt(k)|sin phi|sigma(s) przy k=4096: 40.455716 odtworzone do 2.7e-14. Runtime i stabilnosc przy duzym k."),

 # LT4 — wlasciciel pakietu 002 monografii
 "NC-ALG-006": ("LT4 [1]", "Swiadek par.2.8: para w C^3 o rownej diagonali i rownym tr(P rho P), rozna po postselekcji o 1/4."),
 "NC-ALG-007": ("LT4 [2]", "Swiadek par.3.6: dwie realizacje minimalne w l^2 bez ograniczonego izomorfizmu o ograniczonej odwrotnosci."),
 "NC-ALG-008": ("LT4 [3]", "Swiadek par.7.2: V_t nieciagla przestrzennie, skok 2|sin(pi e^{-t})|, maks 2 przy t=ln 2. Wiaze sie z NC-OPN-006."),

 # MT13 — obszar przez nich rozstrzygniety
 "NC-NUM-007": ("MT13 [1]", "Stala 2 w (7.3'') jest OSIAGANA, swiadek na macierzach REC9. Uwaga: NC-FAL-021 — wlasciwy parametr to r (liczba etykiet na wlokno), nie wymiar n."),
 "NC-NUM-011": ("MT13 [2]", "Jawny swiadek dolny 2-2/n — sformulowanie DO POPRAWY na 2(1-1/r) zgodnie z Waszym T1; moja konstrukcja miala jedno wlokno z r=n."),
 "NC-ALG-018": ("MT13 [3]", "Redukcja rangi 1 i rho = w^T e^{G*Delta} w — czy przenosi sie na n>2 i czy sup_Delta po zakresie numerycznym ma postac zamknieta."),
 "NC-ALG-023": ("MT13 [4]", "SUGESTIA REDAKCYJNA, nie zarzut: jedno zdanie o zakresie (model liniowy w n) przy twierdzeniu o rownych plonach."),

 # REC10 — klasyfikacja
 "NC-ALG-017": ("REC10 [1]", "T1 i T1a — klasyfikacja zakresu po dwoch korektach (ART031 par.3, ART032 par.5)."),
 "NC-ALG-020": ("REC10 [2]", "Crossover zaleznosci od kata: rzadzi przy slabym wzroscie, wygasa przy mu_2=+49. Klasyfikacja."),
 "NC-ALG-022": ("REC10 [3]", "Degeneracja przez zawezenie zbioru dopuszczalnego — klasyfikacja wiersza NC-OPN-010."),

 # Grok — lateralny red-team
 "NC-FAL-023": ("Grok [1]", "ZADANIE LATERALNE, ktorego nie wykonam sam: w ciagu jednego wieczoru trzy razy przeoczylem wlasny dorobek (ART029 -> ART031 -> ART032), za kazdym razem po poprawce skrojonej do ostatniego objawu. Pytanie: czy jest CZWARTA rzecz w serii 029-032 zle przypisana albo zle zinterpretowana. Nie sugeruje, gdzie szukac."),
 "NC-NUM-009": ("Grok [2]", "Dwa mechanizmy bledu z Q64 (rezonans 2 pi i; luka widmowa) — czy jest trzeci."),
 "NC-NUM-010": ("Grok [3]", "Niewidoczna skladowa jadra nieograniczona w amplitudzie — atak na zakres swiadka dK_n(t)=n e^{-n^2 t}."),
}

upd, miss = 0, []
for r in body:
    if r and r[0] in ASSIGN:
        cell, task = ASSIGN[r[0]]
        r[4] = f"{cell} — {task}"
        r[7] = (f"ROUTING 2026-10-25 (ART033): przypisany {cell} wedle ZADEKLAROWANEJ FUNKCJI "
                f"komorki. Poprzednio pole audytora zawieralo 'BRAK' albo GPT, ktorego funkcja to "
                f"synteza i redakcja, NIE falsyfikacja — czyli wiersz nie byl w kolejce audytu. "
                f"Prosze tylko o pozycje 1 z kolejki danej komorki. | " + r[7])
        upd += 1
for k in ASSIGN:
    if not any(r and r[0] == k for r in body):
        miss.append(k)
assert not miss, miss

with open(P, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(hdr); w.writerows([r for r in body if r])

print(f"przypisano audytora: {upd} wierszy\n")
from collections import defaultdict
q = defaultdict(list)
for rid, (cell, _) in ASSIGN.items():
    c, n = cell.rsplit(" [", 1)
    q[c].append((int(n.rstrip("]")), rid))
for c in sorted(q):
    print(f"{c}: " + ", ".join(r for _, r in sorted(q[c])))

# ile [>] zostaje bez audytora po tym ruchu
ex = [r for r in body if r and r[5].startswith("[▷]")]
bad = [r[0] for r in ex if re.search(r'^BRAK|\bGPT', r[4])]
print(f"\n[>] nadal bez audytora funkcyjnego: {len(bad)}")
if bad:
    print("  " + ", ".join(bad))
