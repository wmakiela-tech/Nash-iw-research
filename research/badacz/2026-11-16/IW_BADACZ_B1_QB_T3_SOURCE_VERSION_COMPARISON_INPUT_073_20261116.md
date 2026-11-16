---
artifact_id: IW_BADACZ_B1_QB_T3_SOURCE_VERSION_COMPARISON_INPUT_073_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, autor hipotezy Q-B
created_at: 2026-11-16
document_type: SOURCE_INPUT (materiał wejściowy dla T3; nie jest werdyktem T3)
responds_to: prośba o T3 do LT8 (#iw-dispatch, 16 XI 21:35); REVIEW_071 r2 (2fd6ee4)
claim_type: REDAKCYJNY / DEFINICYJNY (porównanie wersji tekstu); bez claimu numerycznego ani fizycznego
claim_ceiling: SOURCE_INPUT / NO_T3_VERDICT / NO_PAPER_ERROR_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# INPUT_073: wersje artykułu Wu–Xu a konwencja normalizacji ładunkowej — materiał dla T3

**Rola:** Badacz. Jestem autorem hipotezy Q-B, więc **nie wydaję werdyktu T3**. Zebrałem fakty o wersjach z lokatorami, żeby wykonawca T3 (LT8 albo XH) mógł je sprawdzić i ocenić.

**Zastrzeżenie metodyczne:** cytaty pochodzą z odczytu wspomaganego (narzędzie streszczające PDF) z 16 XI ok. 22:50, a nie z ręcznej lektury pełnego tekstu. T3 musi je zweryfikować bezpośrednio w PDF-ach.

## Oś czasu źródeł

| źródło | data | lokator |
|---|---|---|
| arXiv v1 | 6 IX 2025 | arxiv.org/abs/2509.05618v1, arxiv.org/pdf/2509.05618v1 |
| JCAP 02(2026) 063 | wpłynął 15 IX 2025, poprawiony 25 XII 2025, przyjęty 29 XII 2025, opublikowany 17 II 2026 | DOI 10.1088/1475-7516/2026/02/063; kopia: inspirehep.net/files/9adbfbb35c345cc510bed18e66a36b55 |
| kod autorów `d395183` („2509.05618: update to v2”) | 30 XII 2025 | github.com/Fenyutanchan/primordial-black-hole; `origin/master` = `d395183`, po pobraniu 16 XI brak nowszych commitów |
| arXiv v3 | 6 V 2026 | arxiv.org/pdf/2509.05618 (stempel „arXiv:2509.05618v3 [astro-ph.CO] 6 May 2026”) |

Wersji v2 arXiv nie dało się pobrać z tego kontenera. Wersja JCAP jest najbliższym odpowiednikiem kodu v2; to założenie do sprawdzenia.

## Porównanie (odczyt wspomagany)

| element | v1 | JCAP | v3 |
|---|---|---|---|
| multiplicities zawierają cząstki i antycząstki | NIE MA takiego zdania | „Note that these numbers include contributions of both particles and antiparticles.” | to samo zdanie (po równ. 4.4) |
| równanie równowagi mezonów | n_j Γ_j ≈ n_BH dN_j/dt, j ∈ {π±, K±, K⁰_L} | n_j(Γ_dec + Γ_scat) ≈ n_BH dN_j/dt (4.6), ten sam zbiór j | jak JCAP |
| antynukleony w (4.6) | NIE MA | „For anti-protons and anti-neutrons (j = p, n), eq. (4.6) also applies” | jak JCAP |
| konwersja n↔p od mezonów (4.7–4.8) | Γ^j = n_j⟨σ^j v⟩, suma po j; π⁺ ↔ n→p (1.7 mb), π⁻ ↔ p→n (1.5 mb·C_π), K⁻ w obu kierunkach | jak v1 | jak v1 |
| czynnik ½ dla stanów ładunkowych | brak | brak (jedyne „2” dotyczy produkcji par i spinu) | brak |
| zakres ograniczenia w abstrakcie | β od 1e−17 do 1e−19 dla [1e9, 1e10] g | to samo | to samo |
| podziękowania | Bhupal Dev + finansowanie | to samo | dodane: Boting Zhou „for his help in correcting a minor mistake in the calculation of neutron-proton conversion rates” |
| notka o zmianach względem JCAP | — | — | brak |

## Co z tego wynika dla T3 (fakty, nie ocena)

1. **Kod jest zgodny z tekstem.** W tekście grupa (π±, K±, p/p̄, n/n̄) ma jedną gęstość n_j z równania (4.6), a multiplicities (od JCAP) obejmują oba stany. W konwersji n↔p ta sama n_j jest mnożona przez przekrój jednego stanu: π⁺ dla n→p, π⁻ dla p→n, K⁻ w obu kierunkach. `main-scan.jl` robi to samo: całą stawkę grupy dostaje każdy stan (T1-GROUPED, Mech-S9 ROT029).
2. **Pytanie definicyjne dla T3:**
   - Czy n_j w (4.7–4.8) ma znaczyć gęstość *jednego* stanu ładunkowego?
   - Jeśli tak, to przy multiplicities obejmujących oba stany formalizm liczy podwójnie, i to już w tekście, nie tylko w kodzie.
   - Czy przekroje ⟨σ^j v⟩ są zdefiniowane per grupa, czyli uśrednione po stanach? To zmieniałoby wniosek.

   To claim definicyjny. Rozstrzyga go lektura definicji i źródeł przekrojów, nie liczba.
3. **Poprawka w v3:** „minor mistake in the calculation of neutron-proton conversion rates” pojawia się dopiero w v3 (V 2026), czyli po kodzie `d395183`.
   - Nie wiem, czy dotyczy stawek słabych SM (Dodatek B), czy konwersji od mezonów (4.7–4.8).
   - Nie wiem też, czy zmieniła Rys. 5. Zakres w abstrakcie się nie zmienił.
   - **To pierwszy punkt T3:** różnica JCAP → v3 w Dodatku B, w równaniach (4.7–4.8) i na Rys. 5.
4. **Konwencja ładunkowa jest w v3 bez zmian:** to samo zdanie o antycząstkach i brak czynnika ½. Jeśli T3 uzna podwójne liczenie za rzeczywiste, nie zostało ono poprawione w żadnej wersji, o ile poprawka z punktu 3 go nie dotyczy.

## Granice

- To nie jest werdykt T3 ani twierdzenie o błędzie w artykule. Wykonawca T3 ocenia samodzielnie i może odrzucić mój odczyt.
- Cytaty pochodzą z narzędzia streszczającego, a nie z pełnej lektury.
- Wersji v2 arXiv nie dało się pobrać.
