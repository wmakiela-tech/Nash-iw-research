---
artifact_id: IW_BADACZ_B1_HERWIG_TABLE_LABEL_THRESHOLD_DECOMPOSITION_REVIEW_100_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 085/090/098
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_099)
follows: PREREG_099 (Nash-iw-research@0bbaa7a)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_100: na progu β kontrast „tablica HERWIG z BlackHawk względem H73” to w ~85% (j62) dwa artefakty tablic (etykieta √s i binowanie); przy j22 udział zależy od ekstrapolacji ponad 5e4 GeV. Pr3 PASS; Pr1, Pr2 i Pr4 FAIL

## 1. Przebieg

- **Julia:** 209 przebiegów, 12:39:20–13:28:23, wszystkie rc = 0.
- **PRyMordial:** 210 przebiegów, 13:29:29–13:47:20, 0 błędów; ALL_DONE.
- **Bramki 5/5 PASS:**
  - G_TABLES: L/R2 = 1 ± 1.4e−4;
  - G_DRIVER: k22_1720 i net_base bitowo równe 085/090;
  - G_COMPLETE, G_V2, G_BASE.
- Analizę powtórzyłem i wynik jest bitowo identyczny (SHA 4d992ff2…).

## 2. Wynik według preregistracji

Wartości w dex. Ujemne znaczy: niższy próg, czyli więcej hadronów.

| komórka | d_ctrl | d_label (Sa) | d_label (Sb) | d_bin | d_resid | total |
|---|---|---|---|---|---|---|
| j22 code 0.251 | −0.031 | +0.008 | −0.046 | −0.058 | −0.127 | −0.177 |
| j22 code 0.2484 | +0.012 | −0.035 | −0.081 | −0.061 | −0.121 | −0.217 |
| j22 net 0.251 | −0.002 | −0.024 | −0.070 | −0.046 | −0.128 | −0.197 |
| j22 net 0.2484 | +0.001 | −0.027 | −0.076 | −0.053 | −0.112 | −0.192 |
| j62 code 0.251 | +0.002 | −0.074 | −0.081 | −0.047 | −0.022 | −0.143 |
| j62 code 0.2484 | −0.008 | −0.068 | −0.069 | −0.048 | −0.014 | −0.130 |
| j62 net 0.251 | −0.000 | −0.070 | −0.080 | −0.048 | −0.023 | −0.141 |
| j62 net 0.2484 | −0.000 | −0.076 | −0.081 | −0.045 | −0.026 | −0.147 |

Kolumna d_resid jest liczona względem Ua, czyli wariantu Sa.

**Predykcje:**

| predykcja | wynik | szczegół |
|---|---|---|
| Pr1 (d_label < 0 w 8/8) | **FAIL** | 7/8; wyjątek j22 code 0.251 (+0.008) to ta sama komórka, w której d_ctrl = −0.031. Wariant Sb daje 8/8 ujemnych. |
| Pr2 (udział etykiety ≥ 0.3 w ≥ 6/8) | **FAIL** | 4/8 (komórki j62, ~0.5); przy j22 0.12–0.16 dla Sa, 0.26–0.41 dla Sb |
| Pr3 (d_resid < 0 w ≥ 6/8) | **PASS** | 8/8 |
| Pr4 (G_LINK) | **FAIL** | max |d_ctrl| = 0.0312 > 0.03 |

Zgodnie z PREREG_099 §4, wobec niespełnionego G_LINK rozkład odnoszę do tablicy L, a nie do historycznego dhold z 085/090. L odtwarza tablicę R2 do 1.4e−4, a pierwiastki różnią się o ≤ 0.012 w 7/8 komórek.

## 3. Odczyt [▷]

**j62** (pierwotne głównie poniżej 5e4 GeV, Sa ≈ Sb):

| składnik | wartość | udział w total |
|---|---|---|
| etykieta √s | −0.07 | ~50% |
| binowanie | −0.047 | ~33% |
| reszta (kaony, rocznik, strojenie) | −0.02 | ~16% |

Dawny kontrast tablicy HERWIG z BlackHawk względem współczesnego Herwig to tu w ~85% dwa artefakty techniczne tablic.

**j22** (pierwotne blisko i powyżej 5e4 GeV, gdzie poprawiona tablica nie ma danych):

| składnik | wartość |
|---|---|
| etykieta √s | −0.02…−0.035 (Sa, stała) lub −0.05…−0.08 (Sb, kształt H73) |
| binowanie | ~−0.055 |
| reszta | −0.07…−0.13, zależnie od wariantu |

Udział etykiety √s przy j22 jest więc nieoznaczony z dokładnością do ekstrapolacji. Reszta przy j22 zawiera tę niepewność i deficyt kaonów, który według REVIEW_098 rośnie z energią.

**Szum:**

- d_ctrl to zmiana tablicy o 1e−4 przy fizycznie identycznym wejściu. W 7/8 komórek jest ≤ 0.012, ale w j22 code 0.251 sięga 0.031.
- Pojedyncze pierwiastki w komórkach „code” j22 mogą więc skakać o ~0.03 (por. ε = 1.17 noise_dex w 094).
- Ta sama komórka daje jedyny dodatni d_label. Wynik FAIL Pr1 przypisuję temu szumowi [▷], ale nie zmieniam przez to wyniku.

**Skutek dla GAP-005** (dgenBH +0.33…+0.37 = drepro + dmod + dhold):

- Składowa dhold (+0.13…+0.22) to przy j62 głównie artefakty tablic HERWIG z BlackHawk (~+0.12 z +0.14).
- Przy j22 artefakty (etykieta + binowanie) dają +0.05…+0.10 w wariancie Sa i +0.10…+0.14 w wariancie Sb.
- Prawdziwa systematyka generatora to dmod (+0.13…+0.22, REVIEW_091/095) plus reszta kaonowa.

## 4. Granice

- Pojedyncze przebiegi; szum pierwiastków do ~0.03 w komórkach j22 code.
- Brak danych HERWIG ponad 5e4 GeV; Sa i Sb tylko pokazują wrażliwość.
- Reszta łączy rocznik generatora, strojenie, różnice przepisu i ekstrapolację.
- Wyniki dotyczą progów w modelach, nie fizycznej granicy PBH.
- Nowość etykiety √s nadal nie jest ustalona (REVIEW_098, XH-S7).

## 5. Trzy warstwy

- **Wynik:**
  - przy j62 dawny kontrast tablic to w ~85% etykieta √s (~−0.07) i binowanie (~−0.05);
  - przy j22 binowanie ~−0.055, a etykieta zależy od ekstrapolacji (−0.02…−0.08);
  - Pr3 PASS; Pr1, Pr2 i Pr4 FAIL, przy czym Pr1 i Pr4 o włos, w komórce o największym szumie.
- **Konfiguracja:** ramię Sb dodałem, żeby wykorzystać bezczynny rdzeń. Okazało się kluczowe, bo pokazało, że przy j22 etykieta zależy od ekstrapolacji.
- **Uczenie systemu:**
  - Próg G_LINK = 0.03 ustawiłem poniżej udokumentowanego maksimum szumu pojedynczego pierwiastka w komórkach j22 code: ε do 1.17·noise_dex, czyli ~0.009 w 094, oraz pojedyncze skoki ~0.03. To ten sam błąd, który dzień wcześniej przypisałem EKS1. origin_failure_mode: ACCEPTANCE_WINDOW_BELOW_DOCUMENTED_NOISE_OF_THE_COMPARAND (powtórzenie, tym razem u mnie).
  - Łatka mechaniczna: progi kontrolne ustalać z maksimum, a nie z typowego szumu z poprzednich przebiegów, i zapisywać to przy predykcji.
  - Przy tablicach z obciętym zakresem energii zawsze trzeba preregistrować dwa warianty ekstrapolacji, bo jeden wariant ukrywa niepewność.

## 6. Dane

- `data/analysis099.json`, `tables099.json`, `hadrons_099_{L,Sa,Sb,Ua}.dat`, `summary_{k,l,s,u,b}_099.csv`, `net099_raw.jsonl`.
- Logi: `timeline_099.log`, `inputs_sha_099.log`, `tables_sha256_099.log`, `aux_logs_099.log`, `jl_logs_099.log`, `rate_dumps_099_sha256.log`.
- Surowe zrzuty po zapisaniu SHA usunąłem (zgoda Moderatora 11:36). Zrzuty po deduplikacji zostają lokalnie na potrzeby I1.
- SHA w `MANIFEST_SHA256_092.md` (sekcja 099).
