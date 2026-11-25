---
artifact_id: IW_BADACZ_PEV_GENERATOR_DIAGNOSTIC_SIGN_SPLIT_PREREG_134_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); misja poza B1
created_at: 2026-11-25
document_type: MISSION_MANIFEST + PREREG (zamrożony przed obliczeniem jakiejkolwiek statystyki z podziałem na znak)
authorization: Moderator 25 XI 22:50 (dosłownie): „Możesz podjąć diagnostykę poza b1”
claim_ceiling: DIAGNOSTIC / GENERATOR_MODEL / NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_134: czy błąd energii PYTHIA przy PeV psuje liczebności hadronów?

## 0. Manifest misji
- **Cel.** Rozstrzygnąć, czy porażki bramki G_E z PREREG_129 (|ΣE/2E′ − 1| do 1.7e−5) wynikają z topologii zdarzenia, czy z błędu bilansu, który zmienia liczebności hadronów. Od tego zależy, czy przy PeV liczebności z tego generatora nadają się w ogóle do testu źródła.
- **Prowadzący:** Badacz.
- **Zasoby:** wyłącznie istniejące dane. 8 artefaktów Actions z przebiegów 45702555163 i 45703311781, 24 pliki CSV, 48 000 zaakceptowanych zdarzeń. Zgodność SHA artefaktów z raportami Mech-S11 sprawdziłem po prefiksach. Nie ma nowej generacji.
- **Wynik oczekiwany:** werdykt H_T / H_C / UNDETERMINED według §3.
- **Pierwszeństwo:**
  - Mech-S11 ROT017/018: porażki mają niższą liczbę pionów, korelacja ujemna z |reszta|, opis post hoc.
  - Mech-S11 ROT021/022: rozjazd już przed rozpadami, a w większości przypadków już na wejściu fragmentacji.
  - Nowością tego testu jest tylko podział porażek według znaku.
- **Stan wiedzy przy zamrożeniu.** Obejrzałem jedynie nagłówki CSV. Żadnej statystyki z podziałem na znak nie obliczyłem ani nie widziałem.

## 1. Dane i definicje
- Zdarzenia: `accepted == 1`.
- Komórki główne: ramiona off (w0) dla u i g, przy E′ = 1e6 (e4) i 2e6 GeV (e5). Razem 4 komórki.
- Podział zdarzeń: `r = Efinal_over_2E − 1`.
  - PASS: |r| ≤ 1e−6.
  - DEF: r < −1e−6 (niedobór energii).
  - SUR: r > +1e−6 (nadmiar energii).
- N = `n_211 + n_-211`, czyli liczba pionów naładowanych.
- ⟨E_π⟩ = (`E_211 + E_-211`)/N.

## 2. Statystyki
- W każdej komórce: różnice średnich N z błędem standardowym Welcha dla par DEF−PASS, SUR−PASS i SUR−DEF, każda jako z.
- Łączenie komórek metodą Stouffera: z_tot = Σz/√k, po komórkach, w których obie grupy mają co najmniej 10 zdarzeń.
- To samo dla ⟨E_π⟩ w porównaniu FAIL (DEF ∪ SUR) − PASS.

## 3. Reguła decyzji (komórki główne)
- **H_T** (topologia; liczebności nie zależą od znaku błędu): z_tot(DEF−PASS) ≤ −3, z_tot(SUR−PASS) ≤ −3 oraz |z_tot(SUR−DEF)| < 3.
- **H_C** (błąd bilansu zmienia liczebności zgodnie ze znakiem): z_tot(SUR−DEF) ≥ +3.
- W każdym innym przypadku: UNDETERMINED.
- Predykcja pomocnicza H_T (opisowa, nie decyduje): z_tot(⟨E_π⟩: FAIL−PASS) ≥ +3, czyli porażki to zdarzenia z twardszą fragmentacją.

## 4. Raport opisowy
Te same statystyki podaję dla ramion on (w1) i dla komórek e3 (3e5 GeV). Nie są one częścią decyzji, bo ramię on jest obciążone filtrem −23 (REVIEW_132 §2).

## 5. Konsekwencje (nie automatyczne)
- **H_T.** Porażki G_E są objawem topologii i precyzji rekordu, a nie utraty energii zmieniającej liczebności. Estymatorem liczebności inkluzywnych jest wtedy zbiór wszystkich zaakceptowanych zdarzeń; selekcja według G_E byłaby obciążeniem. Otwiera to propozycję (do decyzji Moderatora) testu źródła z bramką powiązaną z wielkością decyzyjną. Nie dowodzi to fizycznej poprawności liczebności.
- **H_C.** Liczebności przy PeV są obciążone błędem bilansu, więc trasa „generator przy PeV” dla STOP A zostaje zamknięta jako wiedza negatywna.
- **UNDETERMINED.** Raportuję wynik bez dalszych wariantów.

Kod: `code/pev_sign_split_134.py`. Wynik: `data/pev_sign_split_134.json`. Oba powstaną po zamrożeniu tego dokumentu.

NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
