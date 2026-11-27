---
artifact_id: IW_BADACZ_G3_SOURCE_ADMISSION_147_20261127
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-27
document_type: SOURCE_ADMISSION_RETURN (G3/H6, poza B1, FLW i ekranem entropii)
assignment: LT11 ROT022 (zaproszenie do jednego ograniczonego zadania przyjęcia źródła; cytowane po ID)
controls: PRF14 ROT022 (publiczny; kontrola negatywna p_plus/p_minus, kontrola pozytywna Bell-BREAK we własnym kontrakcie)
claim_ceiling: SOURCE_ADMISSION_VERDICT / LITERATURE_ONLY / NO_RUN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
verdict: NO_ADMISSIBLE_SOURCE (najbliższe źródło i bloker poniżej); most z dokładną etykietą = STOP-2 (dojrzałe zastosowanie) jako [▷]
revision: r2 (2026-11-27) — naprawy zakresu według Mech-S11 ROT034, PRF15 ROT026 i INT11 ROT028 (§0, §2, B3, B4, §4, §6, §8); werdykt bez zmian; erratum w §9
sync_state: GITHUB_PENDING_BW_INGEST
---

# G3/H6: przyjęcie źródła dla monitora etykiet Pauliego w kontekście UNIT

## 0. Werdykt

**NO_ADMISSIBLE_SOURCE.**

Najbliższe źródło pierwotne to Singh, Bradley, Anand, Ramesh, White, Bernien, *Mid-circuit correction of correlated phase errors using an array of spectator qubits*, arXiv:2208.11716v2 (29 VIII 2022), opublikowane w Science 380, 1265 (2023). Czytałem wersję arXiv v2, w tym suplement §9.

Odczyt jest lokalny dla źródła, wykonywany w trakcie nieprzerwanej sekwencji kubitów danych i nie zastępuje ich trajektorii; brak zaburzenia trajektorii danych jest udokumentowany. To nie jest jednak certyfikat braku wpływu na prawo źródła ani ograniczenie transportu w TV (r2). Źródło nie spełnia warunku klasy. Monitorowana zmienna to ciągła faza z jednego okna pomiarowego, a nie dwie etykiety Pauliego. Mapa monitor→dane jest modelowa i zależy od widma szumu. Źródło jest wstrzykiwanym polem makroskopowym, którego prawo z konstrukcji nie zależy od sterowania danymi. To przesłanka o źródle (μ_A = μ_B), a nie ustalone τ = 0: w kontrakcie jednej ciągłej fazy τ dla dwóch etykiet Pauliego nie jest zdefiniowane bez legalnej mapy (r2).

G3 pozostaje HOLD. Karta EKS1 nie jest wyzwalana, a slot jest wolny.

## 1. Kontrakt (z LT11 ROT022) i kontrole

- **Klasa.** Dwuczasowy klasyczny szum etykiet Pauliego (v, w) ∈ F2²×F2² na kubicie, albo dokładny równoważnik z jawną mapą.
- **Sterowania.** Dwa ustalone nieprzerwane sterowania unitarne q_A i q_B między czasami 1 i 2.
- **Cel.** τ = TV(p_A^UNIT, p_B^UNIT).
- **Monitor.** Lokalny dla źródła zapis lub pomiar obu etykiet w kontekście UNIT. Bez niszczącego zastąpienia trajektorii. Z udokumentowanym wpływem na źródło albo z niezależnie ograniczonym transportem.
- **Kontrola negatywna** (PRF14 ROT022 §4). Prawa p_plus i p_minus = [1 ± 0,99 χ_X(v)]/16 dają identyczne kanały końcowe i identyczne dane Bell-BREAK, a mimo to TV w kontekście UNIT wynosi 0 albo 0,99.
- **Kontrola pozytywna** (PRF14 ROT022 §3). Dwa pomiary Bella odtwarzają p^(q,BREAK), ale nie p^(q,UNIT).
- **STOP-1.** Szum programowany lub logowany z trywialnym, dokładnym zapisem.
- **STOP-2.** Całość sprowadza się do dojrzałej tomografii, Neymana–Pearsona lub Blackwella bez residuum.

## 2. Źródło pierwotne: co jest udokumentowane

Lokatory podaję według arXiv:2208.11716v2.

- **Preparacje.**
  - Kubity danych to atomy Rb, kodowane w stanach |F=1, m_F=0⟩ i |F=2, m_F=0⟩.
  - Spektatory to atomy Cs, kodowane w |F=3, m_F=0⟩ i |F=4, m_F=0⟩.
  - Tablice mają 10×10 i 11×11 pinset; obsadzenie wynosi ok. 55%. Średnia liczba spektatorów na strzał to N = 61 (suplement §9.3).
  - Przed obwodem wykonuje się obraz fluorescencyjny, który identyfikuje faktyczną liczbę spektatorów.
- **Czas źródła.**
  - Dane przechodzą sekwencję 16τ ([τ−π−τ]^8); spektatory sekwencję 12τ, czyli 3/4 czasu ewolucji danych. τ = 6,906 ms, f_AC = 1/(4τ) = 36,2 Hz.
  - Pozostałe 4τ przypada na odczyt w połowie obwodu (MCR) i sprzężenie w przód.
- **Dozwolony odczyt i interwencja.**
  - MCR spektatorów w osi ortogonalnej do preparacji: selektywne usunięcie |1⟩_Cs, potem obrazowanie przez 15 ms.
  - Sprzężenie w przód zmienia fazę końcowego impulsu π/2 danych, co jest obrotem Z.
  - Spektatory można uzupełniać w czasie koherencji danych.
- **Surowa obserwabla.** N_bright/N_initial. Z niej ⟨σ_y⟩ = 2(N_bright/N_initial) − 2a, przy a = 0,62(1). Estymator fazy: Φ'_S = arcsin(⟨σ_y⟩/C), z C = 0,46(1) skalibrowanym bez wstrzykiwanego szumu; obcięcie do ±π/2 (suplement §9.1).
- **Mapa docelowa.** Φ'_D = (4β/3)Φ'_S, gdzie β = 1,35 to stosunek współczynników kwadratowego efektu Zeemana, a 4/3 to stosunek czasów pomiaru.
  - Relacja jest wyprowadzona dla f_AC i jej nieparzystych harmonicznych.
  - Dla innych częstotliwości źródło dokumentuje jej załamanie (suplement, rys. 8).
- **Powtarzalność.**
  - Każdy punkt danych to 10 faz analizy φ_k × 80 powtórzeń.
  - Wierność rozróżnienia stanów spektatora: 0,989(5).
  - Koherencja spektatorów: T2^XY4 = 136(7) ms.
- **Zaburzenie trajektorii danych przez monitor.** Udokumentowane jako pomijalne (dotyczy trajektorii danych; nie jest certyfikatem dla prawa źródła ani transportu w TV, r2):
  - T2^XY8 danych wynosi 0,68(1) s z MCR i 0,65(2) s bez MCR.
  - Rozpraszanie spontaniczne ok. 10⁻⁷ Hz.
  - Prawdopodobieństwo przerzutu bitu danych w czasie 15-ms MCR ok. 10⁻¹¹.
- **Źródło i transport.**
  - Szum pola magnetycznego jest wstrzykiwany cewką Z z wolnobieżnego generatora (Rigol DG812). Faza szumu jest nieznana i losowa w każdym strzale.
  - Amplituda i częstotliwość są zadane: np. 10,7 mG RMS przy f_AC; obszar korekcji sięga do ok. 11 mG.
  - Wynik przy f_AC i 10,7 mG: ⟨σ_x⟩ danych = 0,53(1) ze sprzężeniem w przód i 0,02(2) bez niego.

**Wielkość wyprowadzona** (rachunek arytmetyczny z wartości źródłowych, nie pochodzi ze źródła): przy Φ = 0 i statystyce dwumianowej z N = 61, a = 0,62 i C = 0,46 odchylenie standardowe ⟨σ_y⟩ w jednym strzale wynosi 0,124. Daje to ok. 0,27 rad dla Φ'_S i ok. 0,49 rad dla Φ'_D. Monitor jest więc zaszumionym estymatorem ciągłej zmiennej, a nie rejestratorem etykiety.

## 3. Dopasowanie do klasy G3: blokery

**B1 — brak dokładnej etykiety Pauliego.**
- Na danych działa obrót Z o kąt Φ_D, który jest ciągły. To etykieta Pauliego tylko dla Φ_D ∈ {0, π} mod 2π.
- Twirling Pauliego dałby etykietę Z z prawdopodobieństwem sin²(Φ_D/2). Etykieta byłaby jednak losowaniem, którego żaden monitor nie zapisuje. Sam twirling jest przy tym innym kontekstem, więc wymagałby nowej przesłanki transportu.
- Dokładny równoważnik z jawną mapą nie istnieje.

**B2 — jedno okno pomiarowe.**
- Spektatory mierzą jedną fazę na strzał (okno 12τ). Nie ma drugiej etykiety ani sterowania q umieszczonego między dwoma monitorowanymi oknami.
- Obiekt (v, w) z kontraktu nie jest więc mierzony nawet w wersji ciągłej.

**B3 — transport monitor→dane zależy od modelu i od widma.**
- Relacja Φ'_D = (4β/3)Φ'_S obowiązuje przy f_AC i nieparzystych harmonicznych.
- Poza nimi źródło dokumentuje jej załamanie (rys. 8). Ograniczenie transportu wymaga więc znajomości widma, czyli właśnie tego, co monitor ma mierzyć.
- Załamanie mapy fazowej poza f_AC to błąd transportu spektator→dane zależny od widma. Samo w sobie nie dowodzi, że istnieje jądro zależne od q (r2, Mech-S11 ROT034).

**B4 — źródło z konstrukcji nie zależy od kontekstu.**
- Prąd cewki z wolnobieżnego generatora nie może zależeć od sterowania mikrofalowego kubitów Rb. To daje przesłankę o prawie pola: μ_A = μ_B.
- Z μ_A = μ_B nie wynika p_A = p_B dla efektywnych etykiet bez niezależnie ustalonego wspólnego jądra (albo równych obrazów K_q μ_q). W kontrakcie jednej ciągłej fazy τ dla dwóch etykiet nie jest zdefiniowane bez legalnej mapy, więc nie piszę „τ = 0” (r2, Mech-S11 ROT034, INT11 ROT028).
- Różnica zarejestrowana przez monitor między kontekstami świadczyłaby o przesłuchu sterowania danych do spektatorów (transport monitora), a nie o reakcji źródła.
- Wymuszenie zależności przez zaprogramowanie generatora zależnie od q to STOP-1.

## 4. Najmniejsza decydująca kontrola wyprowadzona ze źródła

Na tej platformie i bez przebiegów jedyną rozstrzygającą kontrolą jest walidacja monitora, a nie pomiar τ.

- Przy tym samym wstrzykiwanym szumie zapisuje się Φ'_S w kontekście q_A i w kontekście q_B (dwa ustalone sterowania danymi).
- Na rozkładach Φ'_S wykonuje się test dwóch prób.
- **H0:** prawo zapisu monitora nie zależy od kontekstu danych. Odrzucenie H0 obala przesłankę „monitor nie widzi sterowania danych”.
- Test dotyczy obserwowanego prawa zapisu, a nie ukrytych etykiet. Nieodrzucenie H0 nie jest równoważnością. Deklaracja równoważności wymaga zdefiniowanej odległości, marginesu i skalibrowanej procedury ufności; samo hasło TOST nie jest certyfikatem (r2, PRF15 ROT026).
- Budżet liczy się w strzałach. Każdy strzał to jedna preparacja i jeden MCR z ok. 61 spektatorami. Osobno dochodzi kalibracja C bez szumu, z błędem C = 0,46(1).

Jest to dojrzały test dwóch prób. Nie dotyczy τ w kontekście UNIT, tylko transportu monitora.

## 5. Most z dokładną etykietą (spin jądrowy) — tylko jako [▷]

Kandydat strukturalny, którego źródła pierwotnego w tej rotacji nie przeczytałem w całości: spin elektronowy NV jako system, a spin jądrowy azotu jako źródło etykiety.

- Przy sekularnym sprzężeniu nadsubtelnym A·I_z·S_z i dobranym czasie ewolucji (A·t = π) warunkowa ewolucja elektronu to dokładnie Z^e, gdzie e jest klasową etykietą stanu jądra. Dla 14N trzy stany jądrowe trzeba zgrubnić do dwóch etykiet.
- Odczyt jądra jest QND, ale biegnie przez elektron, więc musi leżeć poza oknem UNIT („kanapka”: przed i po).
- W reżimie sekularnym etykieta jest zachowana, czyli e1 = e2 = e0 = e3, i nie zależy od sterowania elektronu. Odchyłki są ograniczone parametrami hamiltonianu, a nie danymi.
- τ sprowadza się wtedy do porównania dwóch praw etykiety odczytanej przed eksperymentem. To STOP-2: dojrzałe zastosowanie bez residuum.
- Brak modelu przerzutów oznacza, że kanapka nie wyklucza dwóch przerzutów wewnątrz okna wymuszonych przez q. To jest dokładnie przeciwnik z kontroli negatywnej.

Status: [▷]. Nie rozstrzygam tego bez lektury źródła pierwotnego.

## 6. Uwaga strukturalna [▷] i dojrzały element

**[▷] Napięcie monitorowalność–reaktywność.** Hipoteza oparta na dwóch obejrzanych przykładach; nie jest twierdzeniem:
- Monitory, które nie dotykają systemu, istnieją dla szumu makroskopowego. Jego prawo nie zależy od kontekstu z mocy fizyki (przesłanka μ_A = μ_B, nie ustalone τ = 0; r2).
- Źródła, które mogą reagować na sterowanie (mikroskopowe środowiska), są odczytywane przez sam system albo poza oknem UNIT.
- Kontrprzykład obaliłby hipotezę: mikroskopowe źródło sprzężone z kubitem przez kontrolowane Pauli, z osobnym detektorem działającym w trakcie UNIT. Nie szukałem go szeroko, zgodnie z zakazem przeglądu. Hipoteza nie jest dowodem globalnej niemożliwości monitora reaktywnego środowiska.

**Element dojrzały** (nierówność przetwarzania danych plus nierówność trójkąta; brak nowości). Wersja r2 według PRF15 ROT026 i Mech-S11 ROT034:
- Rozróżniam trzy obiekty: fizyczną zmienną monitora z prawem μ_q, faktycznie zapisane prawo m_q oraz docelowe prawo etykiet p_q.
- Jeśli jedno fizycznie uzasadnione jądro Markowa K z zapisanych wyników do 16 par etykiet obowiązuje w obu kontekstach i niezależnie certyfikowano TV(p_q, K m_q) ≤ η_q, to τ ≤ TV(m_A, m_B) + η_A + η_B.
- Przy jądrach zależnych od kontekstu dochodzi człon sup_z TV(K_A(·|z), K_B(·|z)) albo jego wersja ważona prawem źródła.
- Bez niezależnych η_q nie wynika żadne nietrywialne ograniczenie górne. Mały błąd standardowy fazy ani brak zaburzenia koherencji danych nie są takim certyfikatem; twirling nie tworzy zapisanej etykiety.
- Z certyfikatem ograniczenie górne można zestawić z dolnym L_unit z PRF14 ROT021/022 (|E_XY|/2): L_unit ≤ τ ≤ U_monitor.
- W źródle z §2 nie ma certyfikatu η_q. Załamanie mapy fazowej poza f_AC nie jest ani certyfikatem, ani kontrprzykładem dla wspólnego K.

## 7. Stan i dalsze kroki

- G3: HOLD. Nie dopuszczono żadnego źródła, które spełnia jednocześnie klasę, monitor i transport.
- EKS1: według LT11 ROT022 karta nie jest wyzwalana; slot jest wolny.
- Ewentualne wznowienie wymaga jednego z dwóch warunków. (a) Źródło pierwotne z mikroskopowym, kontrolowanym-Pauli środowiskiem i detektorem działającym w trakcie UNIT. (b) Decyzja koordynatora, że most z §5 ma zostać sprawdzony na źródle pierwotnym, z wiedzą, że prawdopodobnie kończy się na STOP-2.

## 8. Trzy warstwy

1. **Wynik.** NO_ADMISSIBLE_SOURCE. Najbliższe źródło to Singh i in. 2022/2023. Blokery B1–B4. Najmniejsza kontrola waliduje tylko transport monitora. Most NV/jądro to [▷] i prawdopodobnie STOP-2.
2. **Konfiguracja.** Kontrakt LT11 zadziałał jak filtr: warunek klasy i STOP-y odrzuciły źródło bez szerokiego przeglądu. Koszt: kilka wyszukiwań i jedna pełna lektura. W r1 zaliczyłem Singh i in. część „monitor” za spełnioną; r2 zawęża to do braku zaburzenia trajektorii danych.
3. **Uczenie systemu.** origin_observation: `MODEL_LABEL_ASSUMED_PHYSICAL_VARIABLE`.
   - Etykiety (v, w) w klasie G3 są abstrakcją operacyjną; po twirlingu istnieją jako parametry modelu, ale nie muszą istnieć jako zmienna fizyczna środowiska.
   - Reguła na kolejne zadania typu „znajdź monitor”: najpierw sprawdzić, czy etykieta istnieje jako fizyczna zmienna środowiska z niezależnym od q sprzężeniem. Jeśli nie istnieje, szukamy pośrednika z jawną przesłanką jądra K. Wynik jest wtedy co najwyżej ograniczeniem górnym i tylko przy niezależnie certyfikowanym η_q.

## 9. Erratum r2 (2026-11-27)

Naprawy zakresu według Mech-S11 ROT034, PRF15 ROT026 i INT11 ROT028. Werdykt NO_ADMISSIBLE_SOURCE i blokery B1–B3 bez zmian.
- r1 pisało „τ = 0 jest przesłanką fizyczną”. W kontrakcie jednej ciągłej fazy τ dla dwóch etykiet nie jest zdefiniowane; przesłanką jest tylko μ_A = μ_B.
- r1 zaliczało „warunek monitora” za spełniony. Udokumentowany jest tylko brak zaburzenia trajektorii danych, a nie wpływ na prawo źródła ani transport w TV.
- r1 §6 traktowało załamanie mapy fazowej poza f_AC jako zawodzenie przesłanki wspólnego K. To nie wynika ze źródła.
- r1 §6 pomijało warunek certyfikowanego η_q; bez niego monitor nie daje nietrywialnego ograniczenia górnego.
- r1 §4 odwoływało się do „marginesu TOST” jako certyfikatu.

origin_failure_mode: `DATA_NONDISTURBANCE_READ_AS_SOURCE_TRANSPORT_CERTIFICATE` oraz `UNDEFINED_TARGET_REPORTED_AS_PREMISE_VALUE`. Reguła: przy przyjmowaniu monitora oddzielnie wpisuję (i) zaburzenie trajektorii systemu, (ii) wpływ na prawo źródła, (iii) certyfikat TV transportu zapis→etykieta. Wielkość docelowa przed liczbą: najpierw sprawdzam, czy τ jest zdefiniowane w danym kontrakcie.

## Źródła

- K. Singh, C. E. Bradley, S. Anand, V. Ramesh, R. White, H. Bernien, arXiv:2208.11716v2 (2022); Science 380, 1265–1269 (2023), doi:10.1126/science.ade5337. Czytane: tekst główny i suplement §9 (arXiv v2).
- PRF14 ROT022, research/prf14/2026-11-22/IW_PRF14_ROT022_TWO_BELL_TEMPORAL_PAULI_SOURCE_16_LABEL_FULL_RECOVERY_CAUSAL_BREAK_TRANSPORT_NO_GO_AND_HYBRID_95PC_TEST_001_20261122.md (§0–6).
- LT11 ROT022 (prywatny; cytowany po ID).
- Źródła pierwotne NV/jądro (§5) nie zostały przeczytane w tej rotacji.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
