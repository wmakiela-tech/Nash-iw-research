---
artifact_id: IW_BADACZ_B1_DIR010_BACKGROUND_ONLY_SWITCH_REVIEW_104_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel natywny B1
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_103)
follows: PREREG_103 (Nash-iw-research@b5cd208)
claim_ceiling: NUMERYCZNY w modelu Wu–Xu [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_104: przełączenie „tło bez hadronów” daje GATE_FAIL_NO_LABEL (G_BASE). Opisowo, post hoc: tło nie wnosi nic mierzalnego na progach hadronowych, a samo przecina progi dopiero ~4.7 dex wyżej (j62)

## 1. Przebieg i bramki

- **Julia:** 61 przebiegów, 17:13:23–17:28:22, wszystkie rc = 0. Analizę powtórzyłem i wynik jest bitowo identyczny (SHA 99e22dd0…).
- **Bramki:**

| bramka | wynik |
|---|---|
| G_COMPLETE | PASS |
| G_RUN | PASS |
| G_DRIVER | PASS (k22_1720 bitowo równe 083 o22_1720) |
| G_BASE | **FAIL** |

- **Co nie przeszło:** baza ramienia z (β = 1e−30) różni się od bazy 083 o 1.9e−4 (j22) i 1.0e−3 (j62), przy progu 5e−4.
- **Skąd to wiadomo:** baza z przy j62 (0.24371) odstaje od wszystkich węzłów ramienia z przy lb ≤ −17, które leżą w 0.24474 ± 0.00002. Odstaje więc baza, a nie krzywa. Przy tablicy × 1e−12 solwer zachowuje się w punkcie bazowym inaczej niż przy tablicach fizycznych; v2 = 1.0 (źle uwarunkowane, jak zapowiedziałem).
- **Wynik według preregistracji: `GATE_FAIL_NO_LABEL`.** Predykcji Pr1 i Pr2 nie oceniam. Bramka zadziałała zgodnie z przeznaczeniem: f w analizie (0.16 i 0.28 przy j62) liczone względem odstającej bazy byłoby artefaktem.

## 2. Opisowo i post hoc (`posthoc_103.py`, nierejestrowane)

Odniesieniem jest średnia węzłów z przy lb ≤ −18.5 zamiast odstającej bazy. Przecięcia nie zależą od bazy.

**Ułamek tła na progach hadronowych** (próg Wu–Xu z tablicą autorów, model kodu):

| masa | f przy Y* = 0.251 | f przy Y* = 0.2484 | odpowiednik szumu 1σ |
|---|---|---|---|
| j22 | +0.003 | +0.004 | 0.005–0.009 |
| j62 | −0.001 | +0.000 | 0.002–0.004 |

Tło nie wnosi mierzalnego udziału w progach Wu–Xu przy tych masach.

**Przecięcia samego tła:**

| masa | zachowanie Y(lb) | przecięcie 0.2484 | przecięcie 0.251 | odstęp od progów hadronowych |
|---|---|---|---|---|
| j62 | płasko do ~−16.75, potem silny wzrost: 0.2451 przy −16, 0.2480 przy −15, 0.338 przy −13 | −14.96 | −14.70 | +4.67 i +4.69 dex |
| j22 | płasko do ~−16.25, potem lekki spadek o ~3e−4 do lb = −13 | brak | brak | — |

**Odczyt dla DIR-010 [▷]:**

- W modelu Wu–Xu, przy M ≈ 1.1–3.5e9 g, progi Y_p są czysto hadronowe.
- Tło i parowanie PBH działają dopiero przy β o ~4.7 dex większym (j62) albo wcale do lb = −13 (j22).
- Różnice 0.5–2.2 dex między Wu–Xu a Kohri i Keith nie mogą więc pochodzić z tła w sensie tego modelu. Muszą pochodzić z sektora hadronowego (wydajności, przekroje n↔p, profil czasowy) albo z progów obserwacyjnych i konwencji β.
- To zawęża DIR-010, ale go nie rozstrzyga: przeniesienie na modele Kohri i Keith pozostaje TYPE_TRANSFER_HOLD (XH-S8).
- Mechanizm (dominacja PBH przed odparowaniem przy dużym β) jest znany. Nowości nie ma.

**Wobec REVIEW_093:** lekki spadek krzywych hadronowych między −16 a −15 przy j19–j24 nie wynika z addytywnego tła przy j22. Tło zmienia tam Y o mniej niż 1e−4 (poziom szumu).

## 3. Granice

- Wynik według preregistracji to GATE_FAIL. Wszystko z §2 jest post hoc, z odniesieniem innym niż zamrożone.
- Tablica × 1e−12 zmienia zachowanie solwera w punkcie bazowym. Nie da się wykluczyć podobnego wpływu w węzłach, choć te są spójne (σ ~ 1.5–3.4e−5).
- Tylko model kodu Wu–Xu, dwie masy, siatka co 0.25 dex.

## 4. Trzy warstwy

- **Wynik:**
  - GATE_FAIL_NO_LABEL;
  - opisowo: progi Wu–Xu przy 1.1–3.5e9 g są hadronowe (f ≈ 0);
  - tło samo przecina progi dopiero przy lb ≈ −14.7…−15.0 (j62).
- **Konfiguracja:** XH-S8 słusznie odrzucił budowę własnych adapterów Kohri i Keith. Jedno przełączenie natywne zawęziło przestrzeń przyczyn w 15 minut.
- **Uczenie systemu:**
  - Bramkę G_BASE (5e−4) skalibrowałem na tablicach fizycznych. Przy skrajnych wejściach (× 1e−12) baza solwera może odstawać o 1e−3, więc bramka oparta na pojedynczym punkcie bazowym jest krucha.
  - Łatka: przy skrajnych przełączeniach zamrażać z góry odniesienie wielopunktowe (np. średnią węzłów daleko poniżej efektu) obok bazy β = 1e−30. Bramkę bazy traktować jako diagnostykę, a nie jedyną podstawę f.
  - origin_failure_mode: SINGLE_POINT_REFERENCE_UNDER_EXTREME_INPUT.

## 5. Dane

- `data/analysis103.json`, `posthoc103.json`, `summary_{k,z22,z62}_103.csv`.
- Logi: `timeline_103.log`, `inputs_sha_103.log`, `tables_sha256_103.log`, `aux_logs_103.log`, `jl_logs_103.log`, `rate_dumps_103_sha256.log`.
- Surowe zrzuty usunąłem po zapisaniu SHA.
- SHA w `MANIFEST_SHA256_092.md` (sekcja 103).
