---
artifact_id: IW_BADACZ_B1_SUBGRID_EXTRAPOLATION_NATIVE_CHECK_REVIEW_117_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099–116
created_at: 2026-11-23
document_type: REVIEW (wynik zamrożonej PREREG_116)
follows: PREREG_116 (Nash-iw-research@44bd016)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_117: ekstrapolacja poniżej 1e9 g istotnie steruje progiem przy j22. Recepta z artykułu (M^−1.3) zamiast ekstrapolacji kodu przesuwa próg o −0.061 dex; skrajne warianty topu dają −0.059…+0.021 dex; przybliżenie D nie przewiduje progu (3/6 predykcji FAIL)

## 1. Przebieg

- Tablice: G_REBUILD_SC (bitowo), G_FINITE; D identyczne z PREREG_116.
- Julia: 7 procesów, 07:25:51–08:13:43, rc = 0; surowe zrzuty haszowane, deduplikowane i usuwane po kolei.
- PRyMordial: 187/187, 0 błędów; ALL_DONE 08:32:04.
- Bramki 5/5 PASS: G_TABLES, G_COMPLETE, G_V2, G_DRIVER (k22_1720 w kodzie i w sieci oraz net_base bitowo równe 099), G_BASE (max |ΔY_base| = 7.2e−5).
- Analiza z przebiegu i powtórka ręczna są bitowo identyczne (SHA fe27677a…).

## 2. Wynik według preregistracji

dr = r_ramię − r_c (dex), średnia z 4 komórek (code/net × Y* 0.251/0.2484).

| para | D (przybliżenie) | zamrożony przedział | średnie dr | zakres 4 komórek | c_hat = −dr/D | wynik |
|---|---|---|---|---|---|---|
| x0\|22 (top ×0) | −0.0093 | [−0.023, +0.044] | **+0.021** | +0.008…+0.032 | 2.26 | PASS |
| x3\|22 (top ×3) | +0.0219 | [−0.063, +0.012] | **−0.059** | −0.077…−0.045 | 2.71 | PASS (na brzegu) |
| p13\|22 (recepta z artykułu) | +0.0177 | [−0.057, +0.016] | **−0.061** | −0.071…−0.052 | 3.48 | **FAIL** |
| p13\|62 | +0.0074 | [−0.041, +0.024] | −0.005 | −0.008…−0.002 | 0.62 | PASS |
| s15\|22 (kalibracja, M^−1.5) | +0.3070 | [−0.491, −0.216] | **−0.165** | −0.195…−0.149 | 0.54 | **FAIL** |
| s15\|62 | +0.2096 | [−0.344, −0.138] | −0.011 | −0.013…−0.008 | 0.05 | **FAIL** |

Predykcje: 3/6 PASS. Oba testy silne (s15) FAIL. Przybliżenie D nie jest wiarygodnym predyktorem przesunięcia progu.

## 3. Odczyt [▷]

**(a) Kod a artykuł.** Przy j22 zastąpienie ekstrapolacji kodu (nachylenie wierszy 0–1 tablicy, dla Sc −1.16…−1.19) receptą opisaną w artykule Wu–Xu (szybkość ∝ T^1.3 ∝ M^−1.3, kalibrowana przy 1e9 g) obniża próg β o 0.052–0.071 dex w 4/4 komórkach. Przy j62 zmiana wynosi 0.002–0.008 dex.
- Opublikowany kod i opis w artykule różnią się więc w sposobie, który przy j22 zmienia próg o ~0.06 dex. To ten sam rząd co efekt etykiety √s (−0.08) i rocznika (−0.07).
- Pomiar dotyczy tablicy Sc. Własna tablica autorów ma nachylenie wierszy 0–1 równe −1.20, czyli bliżej −1.3, więc dla niej różnica byłaby mniejsza. Nie mierzyłem tego.
- Nie twierdzę, że autorzy popełnili błąd. Opisuję rozbieżność między tekstem a kodem i jej skalę w tym modelu.

**(b) Przycięty top (odpowiedź na Mech-S10 ROT022).** Skrajne nawiasy przesuwają próg przy j22 o +0.021 (×0) i −0.059 (×3) dex. Ograniczenie 0.011 dex z REVIEW_110 §4 obowiązywało więc tylko w wierszach tablicy, a w natywnym progu skrajne warianty dają do ~0.06 dex. Mech-S10 miał rację co do kierunku.
- Realistyczna kontynuacja nachylenia MC ma D = 0.0003. Nawet przy największym zaobserwowanym c (3.5) to ≤ 0.001 dex, czyli pomijalnie.
- Wynik Sc pozostaje warunkowy, teraz ze zmierzonymi nawiasami.

**(c) Dlaczego D zawodzi.** c_hat leży między 0.05 a 3.5 i zależy od tego, gdzie w masie działa zmiana:
- zmiany w górnej części reżimu ekstrapolowanego (1e9 → 5e8 g; x0, x3, p13) działają ze wzmocnieniem 2.3–3.5;
- zmiany skupione przy małych masach (s15) są tłumione: 0.54 przy j22 i 0.05 przy j62.

Dwie hipotezy, nietestowane:
- **wymywanie:** konwersje przy T ≳ 2 MeV są zacierane przez szybkie procesy słabe SM, a D normuje przez całą konwersję, łącznie z tą nieefektywną. Zaniża to względną zmianę w efektywnym oknie;
- **nasycenie i moment wstrzyknięcia przy końcowym rozbłysku:** s15 dokłada konwersje w ostatnich chwilach, przy M ≪ 1e8 g.

Do rozdzielenia potrzebne byłoby natywne jądro odpowiedzi: zlokalizowane zaburzenia szybkości w kolejnych przedziałach masy.

**(d) Skutek dla 100/110/113.** Przy j22 natywny próg zależy w istotnym stopniu od ekstrapolacji poniżej 1e9 g. Wszystkie wyniki przy j22 dotyczą więc modelu z ekstrapolacją kodu w postaci wykonanej.
- Rozkłady 110/113 pozostają pomiarami w tym modelu.
- Ich część przenoszona przez nachylenie wierszy 0–1 była w stawkach ≤ 0.012 dex przy 5e8 g. Przy wzmocnieniu do ~3.5 może jednak sięgać ~0.04 dex na progu.
- Przypisanie składników do „fizyki tablicy” obowiązuje z tym zastrzeżeniem. Przy j62 wpływ ekstrapolacji jest mały (p13 −0.005, s15 −0.011).

## 4. Granice

- Ramiona p13 i s15 nie są fizyczną hadronizacją przy M < 1e9 g. Porównują dwie recepty ekstrapolacji i jedną skrajną.
- Recepta z artykułu jest moją implementacją opisu z równań 4.4–4.5 (jeden wykładnik −1.3 dla wszystkich gatunków, od wiersza 0). Autorzy mogli ją realizować inaczej.
- Pojedyncze przebiegi; szum pojedynczego pierwiastka do ~0.03. Wnioski (a) i (b) opieram na zgodności znaku i rzędu w 4/4 komórkach.
- Wynik dotyczy progów w natywnym modelu Wu–Xu, nie fizycznej granicy PBH.

## 5. Trzy warstwy

- **Wynik:** ekstrapolacja poniżej 1e9 g jest przy j22 dźwignią rzędu 0.06 dex (kod a artykuł; skrajne warianty topu), a przy j62 jest mała. Przybliżenie D nie przewiduje progu.
- **Konfiguracja:** zewnętrzny audyt źródeł Mech-S10 (ROT021/022) wskazał lukę w zakresie mojego wniosku. Jego przypisanie mas było błędne (j22 = 1.121e9 g, nie 6.316e9), ale główna teza się potwierdziła i została zmierzona natywnie. Cykl audyt → pomiar zajął jeden obrót.
- **Uczenie systemu:**
  - origin_failure_mode: EXPOSURE_PROXY_WITHOUT_RESPONSE_KERNEL. Proxy ważone równomiernie w czasie dało błędne przedziały, choć ryzyko nazwałem w preregistracji i nie poszerzyłem przedziałów. Łatka: do predykcji progu nie używam całkowanych szybkości; tylko przebieg natywny albo zmierzone jądro odpowiedzi.
  - origin_failure_mode: UNIFORM_SHIFT_HEURISTIC_APPLIED_TO_NONUNIFORM_CHANGE (REVIEW_110 r3) potwierdzony natywnie; skala błędu ×5.
  - CLOCK_TIME_WRITTEN_FROM_ESTIMATE, piąte wystąpienie (RUNLOG_20261123): znacznik Slack przeliczony w pamięci. Łatka: `date -d @<ts>` w poleceniu zapisu.

## 6. Dane

- `data/analysis116.json`, `tables116.json`, `hadrons_116_{x0,x3,p13,s15}.dat`, `summary_{k,x0,x3,p13,s15}_116.csv`, `net116_raw.jsonl`.
- Logi: `timeline_116.log`, `inputs_sha_116.log`, `tables_sha256_116.log`, `jl_logs_116.log`, `aux_logs_116.log`, `rate_dumps_116_sha256.log` (193 surowe pliki, usunięte po zapisaniu SHA).
- Kod: `code/build_tables_116.py`, `analysis_116.py`, `run116.sh`, `run_net_116.py`, `cfg116_*.dat`. SHA w `MANIFEST_SHA256_116.md`.
