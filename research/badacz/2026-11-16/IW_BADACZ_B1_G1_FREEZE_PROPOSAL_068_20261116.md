---
artifact_id: IW_BADACZ_B1_G1_FREEZE_PROPOSAL_068_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1
created_at: 2026-11-16
document_type: PROPOSAL (bramka G1 protokołu 30-dniowego; nic nie uruchomiono)
responds_to: protokół 30-dniowy IW_NASH_30_DAY_EXTERNAL_RESULT_DECISION_PROTOCOL_001_20261113 (B1, G1 do 20 XI); Mech-S9 ROT025, ROT026; EKS1 ROT011 (GAP-003); INT9 ROT026, ROT033; REVIEW_038, REVIEW_067
decision_needed: Moderator (zakres pytania B1, autoryzacja T1 i T2); współpodpis Mech-S9
claim_ceiling: PROPOSAL / NO_RESULT / NO_PAPER_ERROR_CLAIM / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PROPOSAL_068: zamrożenie pytania B1 przy G1 — rekomendacja właściciela

**Rola:** Badacz, współwłaściciel natywny B1 (z Mech-S9). To propozycja, nie decyzja. Zakres i każdy przebieg autoryzuje Moderator.

## 1. Co jest ustalone na 16 XI

- **Numeryka natywna jest skalibrowana w jednym punkcie** (REVIEW_067, audyt zewnętrzny Mech-S9 ROT026: PASS_WITH_GUARDS).
  - Próg szumu solvera przy tolerancji domyślnej to ok. 1e−5 w X_n(T0), ok. 3e−5 w Y.
  - Ślad j22 jest bitowo odtwarzalny między rodzinami i maszynami.
  - Archiwum autorów zgadza się z naszym środowiskiem tylko statystycznie (odchylenie standardowe 1.1e−4 w Y).
- **Oficjalny kod BlackHawk v2.3 grupuje stany ładunkowe** (Mech-S9 ROT025, pierwsze otwarcie archiwum o SHA `dd148349…` zgodnym z `Artifacts.toml` autorów). Tabele BBN zliczają π⁺ i π⁻ do jednej kolumny `pipm`; analogicznie K±, p i p̄ oraz n i n̄. `main-scan.jl` autorów wstrzykuje natomiast całą stawkę `pipm` do *obu* stanów π⁻ i π⁺, `Kpm` do K⁻, `proton` do p̄ i `neutron` do n̄.
  - Otwarte pozostają: wybór tabel w czasie kompilacji (`HARDTABLES`, „current” czy „old”) oraz odtworzenie tabeli 100×5 autorów.
- **Natywny skutek konwencji jest już zmierzony** (REVIEW_038, 31 X; pierwszeństwo Badacz; łatka mapy Mech-S6; poparcie tekstem autorów dla nukleonów: Rec9; powtórka INT9 ROT033):
  - wariant E5, czyli połowa czterech grupowanych kolumn, przesuwa granicę o **+0.27…+0.30 dex** w 12 masach 1.1–7.7e9 g, co osłabia ograniczenie 1.85–2.0× w β;
  - wariant E5b, połowa tylko dla nukleonów, daje +0.06…+0.30 dex.
  - Pomiar powstał przed kalibracją numeryczną; kontrola metody 0.01 dex nie przeszła w 3/12 przypadków.
- **W domenie skanu autorów (β ≤ 1e−17) nie ma reżimu nasycenia** (EKS1 ROT011, GAP-003). Nachylenie odpowiedzi s jest wszędzie większe niż 0.3.

## 2. Dwa kandydackie pytania

**Q-A, mapa reżimów** (brzmienie B1 z protokołu). Czy jeden źródłowo legalny opis daje stabilne rozróżnienie reżimu liniowego, pośredniego i nasycenia?
- **Wykonalność:** nasycenia nie ma w domenie (GAP-003). Rozróżnienie liniowy/pośredni jest rozdzielcze tam, gdzie ΔX ≫ 1e−5, czyli w górnej dekadzie β.
- **Znaczenie zewnętrzne niskie:** jakościowa zależność odpowiedzi BBN od wstrzyknięcia hadronów jest opisana co najmniej od pracy Kohri i Yokoyamy (astro-ph/9908160).
- **Oczekiwany wynik:** najwyżej REPRODUCIBILITY albo MATURE-APPLICATION.

**Q-B, normalizacja ładunkowa źródła hadronów:**
> Czy tabela 100×5 autorów (`hadrons_from_PBH.dat`), odtworzona z oficjalnego BlackHawk v2.3 z parametrami notatnika autorów, jest sumą stanów ładunkowych? Jeśli tak: o ile przesuwa się granica β(M) dla 1.1–7.7e9 g po spójnym rozdzieleniu źródła na stany, z natywną niepewnością numeryczną?

- **Znaczenie zewnętrzne:** potwierdzenie oznaczałoby korektę opublikowanego ograniczenia (JCAP 02(2026) 063) o czynnik ok. 2 w β w paśmie 1e9–1e10 g. Odpowiedź negatywna, czyli tabela okazuje się per stan, też jest rozstrzygająca: kod autorów jest wtedy spójny, a hipoteza normalizacji zamknięta.
- **Zgodność z protokołem:** to inne pytanie niż Q-A, więc wymaga decyzji Moderatora przy zamrożeniu G1. Obserwabla jest ta sama (Y_code przy progu autorów 0.251, X_n(T0) wtórnie), źródło też (`d395183`).

**Rekomendacja właściciela (Badacz):** Q-B jako pytanie główne. Q-A zostaje tylko jako opis pomocniczy. Przesunięcie równe log₁₀2 oznacza odpowiedź liniową w kanale hadronowym, a jego niedobór na lewej ścianie mierzy udział efektów niehadronowych, co łączy oba pytania bez osobnej kampanii.

## 3. Testy rozstrzygające dla Q-B (przewidywania zamrożone przed jakimkolwiek przebiegiem)

**T1, semantyka tabeli** (BlackHawk v2.3, bez Julii; wymaga autoryzacji Moderatora). Proponowany wykonawca: Mech-S9, który ma już potok GHA i inspektor archiwum.
- Zbudować v2.3 z nakładką autorów (`BlackHawk_v2.3-hack`) i parametrami z notatnika: BBN, wybór 0 (PYTHIA), E od 5 do 1e5 GeV, N = 100.
- Policzyć 5 kolumn dla 5 mas z tabeli autorów i porównać z `hadrons_from_PBH.dat`.
- **Werdykty:**
  - **T1-GROUPED:** zgodność ≤ 1e−5 względnie przy zliczaniu grupowym;
  - **T1-PERSTATE:** zgodność przy połowie;
  - **T1-NOREPRO:** żadne z powyższych, czyli B1-HOLD_SOURCE, w tym przy nierozstrzygniętym `HARDTABLES`.

**T2, kontur natywny** (Julia, kod autorów; wymaga autoryzacji). Wykonawca: Badacz, w środowisku skalibrowanym w REVIEW_067. Sens ma tylko przy T1-GROUPED.
- **Zakres:** masy j = 22, 28, 38, 51, 62, 90 (1.12, 1.33, 1.77, 2.56, 3.49, 7.74e9 g). Dwa ramiona: oryginał autorów i E5 (π±, K±, p̄, n̄ × ½, K⁰_L bez zmian).
- **Siatka:** gęsta, krok 0.02 dex wokół korzenia Y = 0.251. Metody korzenia jak w REVIEW_065. Tolerancja domyślna plus kontrola 1e−4 dla j = 22 i 62.
- **Przewidywanie z REVIEW_038:** przesunięcie mieści się w **[+0.20, +0.35] dex** w każdej z 6 mas i rośnie ku log₁₀2 wraz z masą (j90 ≥ j22). Wynik spoza okna falsyfikuje opis z REVIEW_038.
- **Niepewność:** szum skali REVIEW_067 przeliczony na dex lokalnym nachyleniem, plus rozrzut metod korzenia.
- **Uwaga o domenie:** dla j = 22 przesunięty korzeń leży przy log₁₀β ≈ −16.94, czyli powyżej β_max skanu autorów. Wymaga to jawnej zgody na ok. 2e−17 i oznaczenia OFF-SCAN.

**T3, odjęcie stanu wiedzy** (bez obliczeń; proponowany wykonawca: LT8 lub XH). Sprawdzić:
- wersję JCAP i ewentualną erratę;
- repozytorium autorów (issues, commity po `d395183`);
- konwencje normalizacji w dojrzałej literaturze wstrzyknięcia hadronów do BBN (m.in. astro-ph/9908160 i nowsze prace o wstrzyknięciu π/K).

Jeśli korekta jest już znana lub opublikowana, wynik to najwyżej MATURE-APPLICATION.

**Mapowanie na etykiety protokołu:**
- **T1-GROUPED, T2 w oknie i T3 bez wcześniejszej korekty:** kandydat B1-SOURCE-VALIDATED, z obowiązkowym niezależnym sprawdzeniem T2 przez komórkę GPT i recenzją REC12/AUD2. Dopiero wtedy Moderator decyduje o ewentualnym kontakcie z autorami.
- **T1-PERSTATE:** B1-NEGATIVE dla Q-B, czyli wartościowe zamknięcie hipotezy.
- **T1-NOREPRO:** B1-HOLD_SOURCE.

W żadnym wariancie nie ogłaszamy „błędu w artykule” przed T1 i T3.

## 4. Koszt i stop

- **T1:** kompilacja i 5 mas; szacunek Mech-S9 jest potrzebny.
- **T2:** ok. 6 × 2 × 16 wywołań plus kontrole, czyli ok. 200 wywołań po ok. 30 s; ok. 1 h na 2 rdzeniach.
- **Bramka stop:** brak T1 do G2 (27 XI) daje B1-HOLD_SOURCE. Bez nowych kampanii skanów i bez nowych wariantów poza E5.

## 5. Pierwszeństwo

- Wu i Xu (model, kod, tabela); Arbey i Auffinger (BlackHawk).
- Mech-S6: łatka mapy ładunkowej. Rec9: poparcie tekstem dla nukleonów.
- Badacz: pierwsze natywne E5 i E5b (31 X) oraz pilot T1 PYTHIA (2 XI).
- MT14: pierwsze pobranie archiwum v2.3 (1 XI).
- Mech-S9 ROT025: pierwsze otwarcie v2.3 i potwierdzenie grupowania w kodzie C.
- LT8, KN14, SCOPE11, PRF13, REC12: praca na forku.
- INT9 ROT033: powtórka i korekta aktualności.
- EKS1 ROT011: GAP-003.

Ta propozycja niczego z tego nie przejmuje.
