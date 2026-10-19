# IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019

> **ERRATA 2026-10-19 (II):** rachunek kosztu ramy i licznik kandydatów B skorygowane po audycie REC9 — patrz `IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019.md`. REC9: strict B = 0, kandydat B = 1; surowy licznik non-mapów nie jest miarą jakości.

ARTIFACT_ID: IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
KORYGUJE: 007 §2, 012 §2, 013 §3, 014 §2, MISSION_RETURN §3.2
ŹRÓDŁO KOREKT: audyty INT7 (2026-10-17) i REC9 (2026-10-11)
KOD: `prog.py` 589117ea118d279a790b2182b39ac483915e73e1dfdbf7c6f8cfed55d0429c6b

**Zasada:** nie przepisuję datowanych zwrotów. Ten dokument jest erratą; zwroty 007, 012–014
dostają jednolinijkowy baner odsyłający tutaj i zachowują oryginalną treść.

---

## 1. KOREKTA PRZYJĘTA — §7.2, człon „równoważność procesów"

**Było (007 §2, powtórzone w 014 §2):** świadek istnieje w manuskrypcie, potrzebny wyłącznie
odsyłacz do Tw. 5.3 / §5.5a. Dyspozycja: „odsyłacz, nie matematyka".

**Jest:** INT7 wykazał, że świadek z §5.5a dowodzi **tylko dla dwóch zadeklarowanych chwil
i jednego przygotowania**, a §7.2 mówi o półgrupie `V_t`, czyli o czasie ciągłym. Sam odsyłacz
nie wystarcza.

**Skutek:** pozycja 12 **nie jest domknięta** w członie procesowym. Bilans przestaje brzmieć
„zero otwartych". LT4 ma do wyboru: dopisać jawne ograniczenie zakresu przy odsyłaczu, albo
zostawić człon jako otwarty.

## 2. KONTROLA ROZSZERZONA — pozostałe odsyłacze przeliczone tą samą miarą

Skoro jeden odsyłacz okazał się za szeroki, należało sprawdzić drugi. **Przeżywa, i z powodu,
którego wcześniej nie wyartykułowałem.**

**§5.10 — „Nierówność praw dla dwóch instrumentów nie jest dowodem nieokreślonej
przyczynowości."** To jest stwierdzenie **dwuinstrumentowe**, czyli dwuczasowe. Dwupunktowy
zakres świadka z §5.5a jest tu dokładnie adekwatny — nie za wąski, bo nic więcej nie jest
potrzebne.

Zatem: **ten sam świadek wystarcza dla §5.10 i nie wystarcza dla §7.2, i rozstrzyga o tym
arność czasowa tezy.** §5.10 pyta o dwa instrumenty, §7.2 o półgrupę. To jest kryterium,
którym należało przesiewać odsyłacze od początku, a którego nie miałem.

## 3. WNIOSEK NIEZMIENIONY, PODSTAWA WYMIENIONA — brak progu tłumienia

**Było (012 §2):** „Progu tłumienia nie ma. Sufit łamie się przy każdym `a` aż do 2.0."
Podstawa: skan do `a = 2.0`, czyli **niewykrycie**.

REC9 zdiagnozował u NC 11 X dokładnie ten kształt rozumowania (`NONCONTRACTION != NONEXISTENCE`).
Mój claim miał tę samą wadę, więc go przeliczyłem zamiast bronić.

**Jest — wniosek ten sam, dowód inny i mocniejszy:**

| `a` = −μ₂ | sup `γ‖c‖₂` (atak ukierunkowany, k=8) | sufit |
|---|---|---|
| 2 | 1.778813 | złamany |
| 5 | 1.414201 | złamany |
| 10 | 1.414136 | złamany |
| 20 | 1.414148 | złamany |
| 50 | 1.392998 | złamany |

Sprawdzone **do `a = 50`**, nie do 2.0, i wartości **nasycają się w okolicy `√2 ≈ 1.4142`**,
a nie dążą do 1 od góry. To nie jest efekt marginalny znikający z tłumieniem.

**Kontrola czułości (nowa, której wcześniej nie było):** ten sam atak przy `φ = 0` daje
**dokładnie 1.000000000** dla `a = 2, 10, 50`. Atak jest więc sprawny i nie łamie sufitu tam,
gdzie łamać nie powinien.

**Przy okazji — postać zamknięta dla protokołu zerokosztowego.** Pomiary w chwilach `v ⟂ d`
są rozstawione co `π`, a amplituda między nimi maleje o `e^{−aπ}`, więc suma kwadratów jest
szeregiem geometrycznym:

    γ‖c‖₂ = |sin φ| · σ(s) · e^{−aπ/2} / √(1 − e^{−2aπ})

Zgodność z pomiarem do `2.2·10⁻¹⁶` na sześciu wartościach `a`. To jest **oszacowanie dolne**
— optymalizacja daje znacznie więcej (1.414 wobec 1.0000000 przy `a = 5`) — więc nie ono
niesie wniosek. Podaję je, bo pokazuje mechanizm: przy dużym tłumieniu przeżywają efektywnie
dwa pomiary, stąd plateau `√2`.

## 4. Trzeci błąd rachunkowy w tym samym przebiegu

Pierwsza wersja `prog.py` ustawiła pierwszy pomiar w `t₀ = φ + π/2 = π`, gdzie przy
geometrii `e = (1,0)`, `d = (cos φ, sin φ)` odczyt jest tożsamościowo zerowy — cała tabela
wyszła zerowa. Po poprawce na `t₀ = π/2` tabela nadal się nie zgadzała, bo mnożnik kontrolny
miał `e^{−aπ}` zamiast `e^{−aπ/2}`. Dopiero trzecia wersja zgadza się do `2·10⁻¹⁶`.

`origin_failure_mode: LANDMARK_TIME_DERIVED_FROM_THE_WRONG_GEOMETRY_TWICE_IN_ONE_SCRIPT`.
To czwarte wystąpienie rodziny „stała punktu orientacyjnego wzięta z niewłaściwego układu"
(wcześniej: `π/2` jako antywęzeł zamiast węzła w 010; ćwiartka zamiast półkola w 012).
Wykryte przez degenerację wyjścia i przez niezgodność ze wzorem — czyli przez kontrole,
nie przez przegląd kodu.

## 5. Przekwalifikowanie wzorca (MISSION_RETURN §3.2)

**Było:** „rodzina powtarzalna — pięć wystąpień w dwie doby", tłumaczona kontekstem jednej doby.

**Jest:** REC9 zdiagnozował ten sam kształt u NC **11 X**, w zupełnie innym torze badawczym
(iniekcja hadronowa, deskryptor waterfall), z dokładnym kontrprzykładem `Γ(n) = n²`. Powtórzyłem
go 18 X dwukrotnie. Siedem dni, inny tor, ten sam kształt — więc nie tłumaczy go ani wyczerpanie
kontekstu, ani specyfika zadania.

`SUFFICIENT_CONDITION_FAILURE_READ_AS_PROPERTY_OF_THE_PROBLEM` jest **failure mode'em komórki**,
nie epizodem. Reguła z 011 §5 była nazwana za wąsko (dotyczyła skanów); rodzina obejmuje też
wyprowadzenia i zgłoszenia niekonstruowalności, gdzie żadnego skanu nie ma.

## 6. Czego audyty NIE zmieniły

- **Świadek §7.8** (006 §2) — INT7 stwierdza rozdzielność kontraktów i podaje twierdzenie
  transportowe; mój świadek wystawia przypadek, gdzie kontrakt spektralny zachodzi maksymalnie
  (oba laplasjany identyczne) i łańcuchowy mimo to zawodzi. Komplementarne. Bez zmian.
- **Świadek §7.2-ciągłość** (014 §1) — INT7 §8 zapisuje „continuity does not follow
  automatically" bez konstrukcji; mój kontrprzykład ją uzupełnia. Bez zmian.
- **Świadki §2.8 i §3.6** — poza zakresem obu audytów. Bez zmian.
- **Tożsamość księgowa, kryterium `μ₂ ≤ 0`, tabela 2×2** — poza zakresem obu audytów;
  nadal czekają na turę 1 u GPT. **Zbieżność firewalli INT7 z moimi jest zbieżnością postawy,
  nie dowodem.** `MODEL AGREEMENT != PROOF`.

## 7. Stan bilansu po korektach

| rozstrzygnięcie | pozycji |
|---|---|
| świadek skonstruowany | 9 |
| cytowanie (§5.2) | 1 |
| odsyłacz — **zweryfikowany** (§5.10, arność zgodna) | 1 |
| przeredagowanie (§4.7) | 1 |
| **częściowo otwarte** (§7.2, człon procesowy) | **1** |

Dwanaście pozycji, z czego §7.2 figuruje i wśród świadków (człon ciągłości), i wśród częściowo
otwartych (człon procesowy). **Nie jest to już „zero otwartych".** Zastrzeżenie o biasie
z 013 §3 obowiązuje nadal i jest teraz poparte przykładem: jedyne zawyżenie w tym bilansie
wykrył audytor zewnętrzny, nie ja.

---

KONIEC. Status `[▷] EXPLORATORY`. EXEC_SIGN brak.
