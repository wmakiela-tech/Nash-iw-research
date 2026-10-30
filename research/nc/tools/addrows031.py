import csv

P = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv"
with open(P, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
hdr, body = rows[0], rows[1:]

NEW = [
    ["NC-FAL-023", "NC", "2026-10-24",
     "ART029 przedstawil jako ustalenie trzy rzeczy zapisane przez MOJA WLASNA komorke 18 X 2026: skalowanie sqrt(m) w konfiguracji bez back-action (NC-NUM-004), prawo kata |sin phi| (NC-ALG-005) i empiryczny prog mu_2>0 (NC-NUM-003). Weryfikacja chk18.py sha256 5c34a959f4842fb9e2dc9b4e2edff18e56ebe4a8a17dc66c47d39abf900c3c96",
     "NC (autokorekta z wlasnej inicjatywy, PRZED jakimkolwiek audytem zewnetrznym)",
     "[\U0001f534] FALSIFIED", "ART031 par.1, par.2, par.4",
     "WERYFIKACJA, ze to te same prawa: NC-NUM-004 raportuje 40.46 przy k=4096; sqrt(4096)*(1-e^-1) = 40.455716, odtworzone do 2.7e-14. Dzisiejsze T1 daje kres sqrt(4096)=64, a wartosc z 18 X to dokladnie (1-u)=0.632125 tego kresu. Kontrole: NC-ALG-003 sqrt(tanh(gamma s/2))=0.679791995584 odtworzone do 12 cyfr jako granica m->inf przy e=d; NC-ALG-004 1/sqrt(1-e^{-2 gamma s})=1.075415102530 odtworzone do 12 cyfr jako zmierzony iloraz m=inf/m=1. Wszystkie trzy wiersze z 18 X sa POPRAWNE i spojne z dzisiejsza praca. DEFEKT REGULY, NIE POTKNIECIE: ART018 par.8.1 zarejestrowal te sama rodzine bledu z przyczyna 'nie wykonalem KROK 0'; przyjeta poprawka byla KROK 0. DZIS KROK 0 WYKONALEM I WROCIL CZYSTY, bo sprawdza istnienie IDENTYFIKATORA ZWROTU, a nie istnienie WYNIKU — to kontrola duplikatu skladania, nie odejmowanie stanu wiedzy. Poprawka z ART018 chybila mechanizmu, wiec blad wrocil po szesciu dniach. ZMIERZONE: zero z dwunastu moich preregestracji (ALIGN, DELAY, GEN, L2, MT13_EVENT, MT13_NONLIN, COLL, DUH, IDE, KREISS, SAT, SCHUR) wymagalo przejscia po CLAIM_ROWS_NC — ani jedna, przez trzydziesci zwrotow. ASYMETRIA: na zewnatrz szukalem starannie (Briat & Seuret, BAE/QND, Dahlquist, dwie prace odrzucone jako host po przeczytaniu), a wlasny rejestr — jeden grep w sekunde — pominalem trzydziesci razy. Odejmowanie wobec obcych jest widoczne i chroni przed zarzutem; odejmowanie wobec siebie nie przynosi nic poza mniejszym claimem. origin_failure_mode: PERFORMED_EXTERNAL_PRIOR_ART_SUBTRACTION_WHILE_NEVER_GREPPING_MY_OWN_CLAIM_REGISTRY.",
     "[OBSERVED]", "P_SIMULATED", "NONE"],

    ["NC-OPN-027", "NC", "2026-10-24",
     "Proponowana regula: preregestracja nie jest kompletna, dopoki nie zawiera WYNIKU przejscia po CLAIM_ROWS_NC po mierzonej wielkosci — lista trafien albo jawne 'brak trafien', wpisane PRZED uruchomieniem kodu",
     "Moderator (decyzja o regule); egzekwowalne z zewnatrz z publicznego pliku preregestracji",
     "[OPEN]", "ART031 par.5",
     "DRUGA, OSOBNA kontrola obok KROK 0 — nie zmiana KROK 0, ktory pozostaje kontrola duplikatu skladania, czym jest. Egzekwowalnosc: plik preregestracji jest publiczny, a brak tej sekcji widac bez pytania mnie o cokolwiek, czyli regula spelnia projektowy wymog odpowiednika egzekwowalnego z zewnatrz. origin_failure_mode: NC-FAL-023. WYMAGA DECYZJI MODERATORA — zmiana regul pracy, nie moj nawyk; nie przyjmuje jej sam, mimo delegacji priorytetow z 2026-10-24, bo delegacja dotyczy kolejnosci zadan, nie tworzenia regul projektu.",
     "[OBSERVED]", "P_SIMULATED", "NONE"],
]

for r in NEW:
    assert len(r) == len(hdr), (r[0], len(r), len(hdr))
ids = {r[0] for r in body if r}
for r in NEW:
    assert r[0] not in ids, "duplikat " + r[0]

# atrybucja: dopisac do wierszy z ART029, ktore powtarzaja wlasny dorobek
AT = {
 "NC-ALG-021": ("ATRYBUCJA SKORYGOWANA 2026-10-24 (ART031): to NIE jest ustalenie z ART029. "
   "Moja wlasna komorka zapisala to 18 X 2026 jako NC-NUM-004 ('protokol zerokosztowy przy "
   "phi=pi/2 daje gamma||c||_2 = 40.46 przy k=4096, ubytek amplitudy ~1e-13'). Odtworzone: "
   "sqrt(4096)*(1-e^-1) = 40.455716 do 2.7e-14. Nie jest nowe ani wobec literatury (BAE/QND), "
   "ani wobec mnie samego. | "),
 "NC-ALG-020": ("ATRYBUCJA SKORYGOWANA 2026-10-24 (ART031): prawo kata zapisala moja wlasna "
   "komorka 18 X 2026 jako NC-ALG-005 ('nadmiar na pomiar przy niewspolosiowosci phi wynosi "
   "dokladnie |sin phi|', status [PROVEN]). Nowy wobec wlasnego rejestru jest tylko pomiar "
   "wygasania zaleznosci od kata przy silnym wzroscie transientowym. | "),
 "NC-ALG-018": ("ATRYBUCJA UZUPELNIONA 2026-10-24 (ART031): empiryczna tresc progu mu_2>0 "
   "zaobserwowala moja wlasna komorka 18 X 2026 jako NC-NUM-003 ('atak ukierunkowany lamie "
   "sufit w 12/12 generatorow z mu_2>0; najmniejsze mu_2=0.0099'). Nowe tutaj sa DOWOD progu, "
   "redukcja rangi 1 i tempo — nie sam fakt lamania. Awans NC-NUM-003 z [OBSERVED] jest awansem "
   "MOJEJ WLASNEJ obserwacji, nie odkryciem. | "),
 "NC-ALG-017": ("ZAKRES WOBEC WLASNEGO REJESTRU 2026-10-24 (ART031): wiersze z 18 X obejmuja "
   "przypadek BEZ PRZEPLYWU (G=0). T1 rozszerza na dowolny przeplyw kontraktujacy i to jest "
   "czesc, do ktorej potrzebny byl host zewnetrzny (Dahlquist/Lozinskii). T1a (warunek osiagania) "
   "nie ma odpowiednika w rejestrze. Te dwie czesci ZOSTAJA jako nowe wobec mnie samego. | "),
}
upd = 0
for r in body:
    if r and r[0] in AT:
        r[7] = AT[r[0]] + r[7]
        upd += 1
assert upd == len(AT), upd

body += NEW
with open(P, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(hdr); w.writerows([r for r in body if r])

st = {}
for r in body:
    if r:
        st[r[5]] = st.get(r[5], 0) + 1
print("wierszy:", len([r for r in body if r]), "| skorygowano atrybucje:", upd)
for k in sorted(st):
    print(f"  {k:<22} {st[k]}")
