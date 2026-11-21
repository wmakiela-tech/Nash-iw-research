---
artifact_id: IW_BADACZ_B1_RATE_TRANSFER_PREREG_079_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, właściciel T2
created_at: 2026-11-21
document_type: PREREGISTRATION (zamrożona przed jakimkolwiek przebiegiem pomiarowym)
authorization: Moderator 21 XI 12:41 „prowadź swoje badania naukowe i pilnuj funkcji” — kierunek. Przebiegi Julii wymagają osobnej zgody Moderatora (protokół 30-dniowy §E); do tego czasu nic nie jest uruchamiane.
follows: REVIEW_078 (`GAIN_T_DEPENDENT`, Nash-iw-research@2544401) §6
claim_ceiling: NUMERYCZNY w modelach (przeniesienie natywnych szybkości do pełnej sieci) / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_079: czy przesunięcie T2 przeżywa pełną sieć BBN? Transfer natywnych szybkości konwersji Wu–Xu do PRyMordial

## 0. Pytanie i znaczenie

- **Skąd pytanie.** REVIEW_078 pokazał, że między Y_C kodu a helem z pełnej sieci nie ma jednego czynnika przeniesienia: R zależy od T. Fizyczne odczytanie T2 wymaga więc znajomości historii źródła.
- **Zmiana metody względem propozycji z REVIEW_078.** Zamiast liniowego splotu z G biorę bezpośrednio z kodu autorów **natywne szybkości konwersji hadronowej na nukleon** r_{p→n}(T) i r_{n→p}(T). Liczę je własnymi funkcjami ⟨σv⟩ autorów z ich własnych gęstości hadronów. Następnie dodaję je do szybkości słabych w pełnej sieci.
  - Zaleta 1: metoda jest nieliniowa i nie zależy od rozdzielczości G. Ma to znaczenie, bo dla j22 G jest słabo wyznaczone powyżej 1.2 MeV.
  - Zaleta 2: oba obiekty dostają tę samą historię konwersji, różnią się tylko resztą fizyki (szybkości słabe, sieć jądrowa, odczyt helu).
- **Pytanie decyzyjne.** Czy przesunięcie D = log β(E5) − log β(orig) przy równym efekcie helowym jest takie samo w kodzie i w pełnej sieci? To przesunięcie wynosi w kodzie +0.272 (j22) i +0.298 (j62), REVIEW_071; w ramieniu orig potwierdził je natywnie Mech-S10 (T2R).
  - Jeśli tak, korekta normalizacji ładunkowej nie zależy od odwzorowania Y_C → Y_p.
  - Jeśli nie, T2 nie przenosi się na fizykę bez dalszych zmian.

## 1. Definicje

- **Ramiona natywne (CODE).** Kod autorów (d395183, `main-scan.jl` blob b368ba55), `magic(m, β; hadrons_output_flag=true)`.
  - Domyślny solver, bez zmian.
  - E5: łatka Mech-S6 (`apply_wuxu_charge_pair_source_map.py`, SHA-256 7fd531f2…), dokładnie jak w T2.
  - Na 10000 punktach wyjściowych autorów:
    - r_{p→n} = n_{π⁻}σv_{π⁻,p→n} + n_{K⁻}σv_{K⁻,p→n} + n_{K⁰L}σv_{K⁰L,p→n} + n_{n̄}σv_{nn̄,p→n} [1/s na proton];
    - r_{n→p} = n_{π⁺}σv_{π⁺,n→p} + n_{K⁻}σv_{K⁻,n→p} + n_{K⁰L}σv_{K⁰L,n→p} + n_{p̄}σv_{pp̄,n→p} [1/s na neutron];
    - to dokładnie człony hadronowe dX_n/dt z `evolution_system!`.
- **Ramię sieci (NET).** PRyMordial @725d8a8 z łatką 077 (tutaj neutralną) i hakiem 079: do szybkości słabych w erach HT, MT i LT dodaję r_{n→p}(T) do frwrd i r_{p→n}(T) do bkwrd.
  - Dopasowanie po temperaturze: T_γ sieci ↔ T_SM kodu, interpolacja liniowa r w log T; poza zakresem r = 0.
  - Ustawienia: η₀ = 6.1e-10, mała sieć. Y := YP_BBN.
- **Wielkości:**
  - ΔY_code = Y_native − Y0_code(j), gdzie Y0_code to wiersz bazowy β = 1e-30;
  - ΔY_net = Y_net(szybkości tego przebiegu) − Y0_net;
  - ρ = ΔY_net / ΔY_code.
- **Przesunięcia** (oba liczone na tych samych 9-węzłowych siatkach, ta sama metoda, interpolacja liniowa w log β między węzłami obejmującymi poziom; wymagany dokładnie jeden przedział):
  - D_code(j) = lb_E5(ΔY_code = d0) − lb_orig(ΔY_code = d0), gdzie d0 = 0.251 − Y0_code(j);
  - D_net(j) = lb_E5(ΔY_net = d*) − lb_orig_root_code(j), gdzie d* = ΔY_net(orig) interpolowane w pierwiastku kodu orig.
  - Interpretacja D_net: o ile trzeba podnieść β w E5, żeby **w pełnej sieci** dostać ten sam nadmiar helu, jaki orig daje przy swoim progu kodowym.

## 2. Plan przebiegów (zamrożony)

- **Węzły β:** co drugi węzeł zamrożonych siatek T2 (cfg069_{orig,e5}_default, indeksy 0, 2, …, 16), czyli 9 węzłów co 0.04 dex na każdy z czterech przypadków (j22 i j62, orig i E5). Dodatkowo bazy j22 i j62 przy log β = −30.
- **CODE:** 38 wywołań Julii (orig 20, E5 18), dwie kolejki równolegle, około 30 s na wywołanie.
- **NET:**
  - baza;
  - 38 przebiegów z szybkościami;
  - V4 (tol_scale 1e-2) i V5 (co drugi punkt szybkości) dla o22_n08 i o62_n08.
  - Razem 43 przebiegi, około 10–16 s każdy.
- **Czas łącznie:** około 30 min CPU w kontenerze, bez innych kosztów.

## 3. Zamrożony kod (`research/badacz/2026-11-21/code/`)

| plik | SHA-256 |
|---|---|
| `rate_dump_079.jl` | 1cf59db6c8434c17afa48ea9f02ce1f968aa6db0f641e00050974ea54b6cd01e |
| `prym_rate_patch_079.py` | 93989e68411ff7d641bd780e6d902fa495eaef892bfe954cef13a9c744b7fac1 |
| `net_rate_079.py` | 866f90fc75d453751b9d7a1906a3718c44a9337c32f18574a5a1767319fef763 |
| `run_net_079.py` | eb76ab846dbe8ee9b3b748f979fa37882f697a27c433fa813269e110d76d806b |
| `analysis_079.py` | 95f43381d388e772872c4e9fceb3137ef4f2b21e807b683a80d444440d17c9ab |
| `run079.sh` | b9332a7e0dfb49d9c5825d6d9bd0e1fdf7bf938357ea331d8643f031528dbc2d |
| `cfg079_orig.dat` | 50478cee99699f41449c16fdf0f2d151bfafcd2a27b223a6a56d07ecd469d1f2 |
| `cfg079_e5.dat` | d0fe761f4851fdecb780320f74a432c6dc3546d5af40253157151f00678f871e |

Łatka 079 nakłada się na łatkę 077. Weryfikuje SHA wyniku 077 (cd607965eb711efc…6fd0) i daje wynik o SHA b6bb5636…29ce0.

## 4. Bramki (zamrożone)

- **V1_NATIVE_REPRO:** każdy natywny Y odtwarza wartość T2 (t2_{arm}_default.csv) dla tego samego węzła z |Δ| ≤ 1e-12. Bazy odtwarzają qa_A (j22 i j62, log β = −30). Oczekuję zgodności bitowej, bo flaga hadronów zmienia tylko wyjście, a nie solve.
- **V2_RATE_CONSISTENCY:** na odcinkach z żywą PBH i T ≤ 20 MeV, gdzie człon hadronowy przeważa nad SM+rozpadem, mediana |dX/dt_różnicowe / RHS − 1| ≤ 2%.
  - RHS = SM (formuła autorów 255/τ_n·(12 + 6x + x²)/x⁵) + rozpad + (1−X)r_{p→n} − X·r_{n→p}.
  - Sprawdzam to, że moje r to dokładnie te szybkości, których używa kod.
  - Przy mniej niż 20 takich punktach przypadek dostaje status NOT_APPLICABLE i nie blokuje.
- **V3_NET_ZERO:** szybkości z baz (β = 1e-30) dają Y0_net z dokładnością |Δ| ≤ 1e-10.
- **V4_NET_TOL:** |ΔY_net(tol × 1e-2) / ΔY_net − 1| ≤ 1% (o22_n08, o62_n08).
- **V5_INTERP:** co drugi punkt szybkości zmienia ΔY_net o ≤ 1%.

Niepowodzenie dowolnej bramki daje `GATE_FAIL_NO_LABEL`.

## 5. Etykiety i znaczenie decyzyjne (zamrożone)

| etykieta | warunek | znaczenie |
|---|---|---|
| `SHIFT_TRANSFERS` | \|D_net − D_code\| ≤ 0.02 dex dla j22 i j62 | korekta normalizacji ładunkowej z T2 jest odporna na przeniesienie do pełnej sieci (w tym modelu źródła); fizyczne odczytanie zależy już tylko od progu obserwacyjnego i linii bazowej, nie od wzmocnienia |
| `SHIFT_MODIFIED` | w przeciwnym razie | T2 nie przenosi się wprost; raportuję D_net jako wielkość „sieciową” |
| `OUT_OF_RANGE` | poziom poza 9 węzłami | brak wyniku; ewentualne rozszerzenie wymaga nowego preregu |

Raportuję też opisowo:
- ρ dla każdego węzła;
- T ostatniego punktu z żywą PBH;
- diagnostykę liniowego splotu z G z REVIEW_078: ∫G_code·s dt wobec natywnego ΔY_code oraz ∫G_net·s dt wobec ΔY_net z transferu. To test adekwatności przybliżenia liniowego, bez wpływu na etykietę.

## 6. Predykcje Badacza [▷] (zamrożone)

- **P1:** ρ(j62, orig, w pierwiastku kodu) ∈ [0.75, 0.95]. Uzasadnienie: dla emisji w 0.3–0.8 MeV REVIEW_078 dał R ≈ 1.06–1.15, a udział emisji przy T ≥ 1.2 MeV jest mały, bo G jest tam małe.
- **P2:** dla j22 nie podaję predykcji ρ, bo region ≥ 1.2 MeV nie jest wyznaczony.
- **P3:** `SHIFT_TRANSFERS`. Uzasadnienie: jeśli przeniesienie jest w przybliżeniu liniowe w amplitudzie źródła i podobne dla obu ramion (różnią się składem kanałów tylko przez nietknięte K⁰L), to D się zachowuje.

## 7. Ujawnienie przed zamrożeniem

- Jeden przebieg PRyMordial bez szybkości na kopii po łatce 079 dał 0.24687400446850843, czyli bitowo Y0_net z REVIEW_078. Potwierdza to neutralność haka.
- Żadnego przebiegu Julii nie wykonałem. Żaden przebieg z szybkościami się nie odbył.
- Driver `rate_dump_079.jl` jest nieprzetestowany w części eksportu szybkości: konwersja jednostek `r*NU.s` oraz `EUval(MeV, ·)`. Usterka techniczna przed uzyskaniem danych to odnotowane odchylenie, poprawiane bez oglądania wyników.

## 8. Granice

- Gęstości hadronów pochodzą z trajektorii kodu, a absorpcja zależy w nich od X_code. W sieci X jest inne, a sprzężenia zwrotnego nie modeluję. Pomijam też zmianę ekspansji i entropii od PBH.
- Dopasowanie po T (nie po t) jest wyborem jawnym. Emisja PBH w kodzie biegnie w czasie kodu.
- Działa tylko PRyMordial w małej sieci; duża sieć w REVIEW_078 różniła się o ≤ 0.09% w G.
- Nie są modelowane: fotodysocjacja, hadrodysocjacja ani E4 (hadronizacja < 1e9 g).
- Żadna etykieta nie jest granicą PBH. Próg obserwacyjny (0.251 vs LBT 0.2484) i linia bazowa (Y0_code vs Y0_net) zostają poza tym pomiarem.

## 9. Audyt

Wynik wymaga zewnętrznego I1, bo jestem autorem pomiaru: REC13 lub AUD3 do danych i analizy. Niezależną replikację haka szybkości (inny kod sieci) mile widzę w PRF14, równolegle z prośbą o G_net z REVIEW_078.
