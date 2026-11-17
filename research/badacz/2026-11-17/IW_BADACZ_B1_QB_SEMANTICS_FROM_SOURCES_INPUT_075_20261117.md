---
artifact_id: IW_BADACZ_B1_QB_SEMANTICS_FROM_SOURCES_INPUT_075_20261117
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, autor hipotezy Q-B
created_at: 2026-11-17
document_type: SOURCE_INPUT (materiał do zewnętrznej weryfikacji; nie jest werdyktem)
responds_to: Moderator 17 XI 01:53 („…może są inne możliwości dokonania ustaleń”); T3 LT9 (AUTHOR_INTENT_UNRESOLVED)
claim_type: DEFINICYJNY (konwencja normalizacji ustalona ze źródeł) + jedna kontrola arytmetyczna [▷]
claim_ceiling: SOURCE_INPUT / NO_PAPER_ERROR_CLAIM / NO_LITERATURE_ERROR_CLAIM / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# INPUT_075: konwencja normalizacji Wu–Xu da się ustalić ze źródeł — i nie jest specyficzna dla Wu–Xu

**Rola:** Badacz, autor hipotezy Q-B. To materiał do weryfikacji przez komórkę spoza mojej hipotezy. Nie jest werdyktem.

## Wynik w skrócie [▷]

Pytanie „co autorzy mieli na myśli” da się zastąpić pytaniem źródłowym, rozstrzygalnym bez kontaktu z autorami: jaka konwencja obowiązuje w literaturze, którą autorzy cytują.

Odpowiedź ze źródeł:
- Wu–Xu wstrzykują do każdego stanu ładunkowego wydajność **na poziomie sumy grupy**.
- Tę samą skalę widać w cytowanym rodowodzie: Kohri 2001 (źródło przekrojów w kodzie) oraz Kohri–Yokoyama 1999.
- Względem fizycznej wydajności pojedynczego stanu (przy symetrii ładunkowej N_{π⁺} ≈ N_{π⁻} ≈ ½·N_{π±}) to wciąż czynnik 2. Jest to jednak **własność konwencji rodowodu**, a nie odstępstwo Wu–Xu od cytowanego formalizmu.

**Korekta mojej wcześniejszej roboczej tezy.** W wersji roboczej tego dokumentu (niezacommitowanej, nierozesłanej) napisałem, że „względem cytowanego formalizmu kod wstrzykuje 2× wydajność stanu”. Ta teza była błędna. Wynikała z dwóch błędów:
- porównałem kod z niewłaściwym źródłem (KY 1999 zamiast Kohri 2001, który kod cytuje przy przekrojach);
- przyjąłem etykiety „per stan” w KY 1999 bez sprawdzenia, czy ich wartości są fizycznie możliwe jako wydajności pojedynczych stanów (patrz C2).

## A. Przekroje dotyczą pojedynczych stanów

- Kod (`d395183`, `tool_script-parameters.jl`):
  - linia 81 to komentarz `# from [Kohri:2001jx-arXiv:astro-ph/0103411v2]`;
  - linie 82–94 definiują σv(π⁺ n→p) = 1.7 mb, σv(π⁻ p→n) = 1.5 mb·F_c, K⁻: 26 / 34 / 31·F_c / 14.5·F_c mb, nn̄: 37 / 28 mb, pp̄: 28 / 37 mb;
  - linia 96 to komentarz `# from [Kohri:1999ex-arXiv:astro-ph/9908160]` (dotyczy tylko K⁰_L, linie 97–100).
- Kohri 2001, równ. (22)–(23) i (25)–(32) oraz Kohri–Yokoyama 1999, równ. (16)–(22) i (27)–(30): te same wartości, dla reakcji konkretnych stanów (π⁺n, π⁻p, K⁻N).
- **Wniosek:** gałąź „σ uśrednione po grupie” (np. ½·σ) odpada. Ten punkt się nie zmienia.

## B. Wydajności Wu–Xu są sumami grup (konstrukcja autorów)

1. Licznik PYTHIA w v1 (`3613b54`, `PYTHIA8_table_scripts/table_up.jl`, linie 107–116) wrzuca `±211` do jednej tablicy `pipm`; analogicznie `±321` → `Kpm`, `±2212` → `proton`, `±2112` → `neutron`.
2. Kolumna stawek nosi nazwę `charged_pion_dN_over_dt`. Kolumny mezonowe są identyczne w v1 i v2.
3. Tablica odtwarza się jako sumy grup BlackHawk: T1-GROUPED 25/25 (przyjęte przez Moderatora), AUD3 I1.
4. Tekst od wersji JCAP/v2: „Note that these numbers include contributions of both particles and antiparticles.”
5. Wstrzykiwanie:
   - v1: `main-scan.jl`, linie 162 i 166–169 (ta sama `d_n_pion_d_t_from_PBH` w π⁻ i w π⁺);
   - v2: linie 103–127 (stawka grupy π do π⁻ i do π⁺, K± do K⁻, grupa p+p̄ do „pp̄”, grupa n+n̄ do „nn̄”).
   - Nigdzie nie ma ½.

## C. Ta sama skala występuje w cytowanym rodowodzie

**C1. Kohri 2001 (astro-ph/0103411v2), źródło przekrojów w kodzie.**
- Równ. (34): K_{N→N'} = Σ_{H_i} (N_jet/2)·N_{H_i}·R^{H_i}_{N→N'}, gdzie N_{H_i} „is presented in Fig. 5”.
- Rys. 5 pokazuje wyłącznie krzywe zsumowane: „π⁺ + π⁻”, „K⁺ + K⁻”, K⁰_L, „p + p̄”, „n + n̄”.
- Nukleony są traktowane jako „mezon NN̄” (za Reno–Seckel).
- Tekst nie mówi, czy dla H_i = π⁺ bierze się całą krzywą „π⁺ + π⁻”, czy jej połowę. Jedyne wydajności, jakie formalizm dostarcza, są jednak sumami grup. Odczyt Wu–Xu jest z tym zgodny.

**C2. Kohri–Yokoyama 1999 (astro-ph/9908160) — kontrola arytmetyczna [▷].**
- Równ. (13) podaje wydajności z etykietami pojedynczych stanów (na dwa dżety, √s = 91.2 GeV): n_{π⁺} = n_{π⁻} = 14.1, n_{K⁺} = n_{K⁻} = 1.67, n_p = n_{p̄} = 0.772.
- Własne równ. (11) tej pracy daje ⟨N_ch⟩(91.2 GeV) = **20.82**.
- Suma naładowanych wydajności „per stan”: 33.08 = **1.59 × ⟨N_ch⟩**. Samo π⁺ + π⁻ = 28.2 = 1.35 × ⟨N_ch⟩. Jako wydajności pojedynczych stanów te liczby są niemożliwe: naładowanych hadronów nie może być więcej niż naładowanych cząstek.
- Odczytane jako sumy grup, przypisane każdemu stanowi: 16.54 = 0.79 × ⟨N_ch⟩, co jest wartością wiarygodną.
- Kod i wynik:
  - `code/ky1999_yield_consistency_075.py` (SHA-256 `a7e82c19…24f953c1`);
  - `data/ky1999_yield_consistency_075.json` (SHA-256 `06dda818…2397b68`).
- Etykiety w KY 1999 są więc „per stan”, ale wartości mają skalę grupy. To ten sam wzór co u Wu–Xu.

## Co z tego wynika [▷]

1. **Semantyka Wu–Xu jest ustalona ze źródeł w stopniu, w jakim to możliwe.** Autorzy stosują konwencję widoczną w cytowanym rodowodzie: przekroje dla pojedynczych stanów, wydajności na poziomie grupy. Kontakt z autorami mógłby najwyżej potwierdzić, że świadomie poszli za Kohri 2001. Nie rozstrzygnąłby fizyki.
2. **Merytoryczne pytanie przesuwa się z „zamiaru Wu–Xu” na fizykę konwencji.** Symetria ładunkowa dżetów i tablice krotności (PDG) pozwalają ustalić fizyczną wydajność stanu bez pytania kogokolwiek. Jeśli konwencja rodowodu daje 2× względem fizyki, dotyczy to rodowodu (co najmniej KY 1999 i Kohri 2001; Reno–Seckel 1988 niesprawdzone), nie tylko Wu–Xu.
3. **T2 (REVIEW_071) się nie zmienia.** Nadal mierzy różnicę między konwencją rodowodu a normalizacją fizyczną per stan (mapa E5): +0.27…+0.30 dex. Zmienia się tylko jej opis: z „różnicy względem formalizmu” na „różnicę konwencja vs fizyka”.
4. **Granica G-GOV / ostrożności.** Pozycja C2 to wskazanie wewnętrznej niespójności w opublikowanej pracy z 1999 r. Do zewnętrznej weryfikacji pozostaje sufit NO_LITERATURE_ERROR_CLAIM. Nie wiadomo, skąd pochodzi 14.1: tablica 38.1 PDG z tamtego okresu nie została sprawdzona.

## Granice

- Cytaty z obu prac Kohriego pochodzą z ekstrakcji tekstu PDF (alphaXiv). Weryfikator musi je sprawdzić w oryginale. Linie kodu są przeczytane bezpośrednio z historii git repozytorium autorów.
- Nie sprawdzono: Reno–Seckel 1988; tablicy PDG użytej przez KY 1999; tego, czy w kodzie Kohri 2001 była połowa.
- To nie jest twierdzenie o błędzie w artykule Wu–Xu ani w literaturze. Nie jest to też fizyczna granica PBH. E4 pozostaje HOLD.
- **origin_failure_mode** (moja robocza teza):
  - `CITED_SOURCE_NOT_MATCHED_TO_CODE_COMMENT`: porównanie z pracą, której kod nie cytuje przy danym elemencie;
  - `LABEL_TRUSTED_OVER_MAGNITUDE`: etykieta „per stan” przyjęta bez kontroli wielkości.
  - Reguła na przyszłość: przy pytaniu o semantykę normalizacji najpierw dopasuj źródło do komentarza w kodzie, potem sprawdź wielkości względem niezależnego ograniczenia (tu ⟨N_ch⟩).

## Prośba o weryfikację (jedna pozycja na komórkę)

**LT9 (właściciel T3), poza rodziną Claude.** Sprawdzić C1 i C2 w oryginałach. Odpowiedzieć, czy konkluzja „konwencja rodowodu, nie odstępstwo Wu–Xu” wytrzymuje. Zwrot: `SEMANTICS_ESTABLISHED_AS_LINEAGE_CONVENTION` / `SEMANTICS_OPEN`, z uzasadnieniem.

**XH-S7, opcjonalnie, literatura.**
- Ustalić, skąd pochodzi 14.1 w KY 1999 (wydanie tablicy krotności PDG około 1998).
- Ustalić, jak Reno–Seckel 1988 normalizują wydajności π±.
