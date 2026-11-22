---
artifact_id: IW_BADACZ_B1_DIR009_BLACKHAWK_V30_HERWIG_TABLES_NOTE_111_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel DIR-009 (097–106)
created_at: 2026-11-22
document_type: NOTE (porównanie plików; bez przebiegu fizycznego)
answers: EKS1 ROT023 §1 i REC13 ROT021 (bramka „te same / inne / brak dostępu” dla tablic HERWIG w BlackHawk v3.0)
claim_ceiling: PROWENIENCJA PLIKÓW / [▷] dla wniosku o v3.0 / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# NOTE_111: tablice HERWIG w BlackHawk v3.0 są bajtowo identyczne z v2.3 (11/11 plików); czytnik `hadro_herwig.c` różni się tylko komentarzem w nagłówku

## 1. Co sprawdziłem

- Oficjalne archiwa z blackhawk.hepforge.org: v2.3 (SHA-256 dd148349…, to samo archiwum co w 085) i v3.0 (c8bf4ccc…, pobrane dziś przez `downloader?f=blackhawk_v3.0.tar.bz2`).
- `code/compare_bh_tables_111.py` czyta oba archiwa strumieniowo (tarfile, nic nie jest rozpakowywane ani uruchamiane) i liczy SHA-256 każdego pliku w `src/tables/hadronization_tables/herwig_tables/`. Reguła decyzji pochodzi z REC13 ROT021 i była ustalona przed przebiegiem: SAME_CATALOG_BYTES / DIFFERENT_CATALOG_BYTES / ACCESS_OR_CATALOG_HOLD. Dwa przebiegi dały bitowo ten sam wynik.
- Opisowo: te same porównania dla tablic PYTHIA, nagłówków tablic i skryptów generatora HERWIG, a także `diff` źródeł C (`src/*.c`, `*.h`, bez tablic).

## 2. Wynik

| obiekt | werdykt |
|---|---|
| `herwig_tables/` | **SAME_CATALOG_BYTES**: 11/11 plików, te same nazwy i SHA-256 |
| `pythia_tables/` | 11/11 bieżących plików identycznych; v3.0 nie zawiera już podkatalogu `old/` (11 plików) |
| `hadronization_tables_herwig.h`, `infos.txt` | identyczne |
| `scripts/herwig_scripts/` (LEP.in, main.cpp, BH_TABLE_GENERATOR.cc) | identyczne; różnią się README (nagłówek autorów i data) oraz binaria `bottom/a.exe`, `main.o` |
| `src/hadro_herwig.c` | 6 linii różnicy, wszystkie w komentarzu nagłówka (data, autorzy); 0 linii kodu |
| `src/secondary.c` | nowe opcje `interpolation_method` (2, 3) i większe bufory nazw; żadna linia różnicy nie dotyczy HERWIG |
| `src/general.c`, `primary.c` | żadna linia różnicy nie dotyczy HERWIG; w `general.c` poprawiono nawiasy w sprawdzeniu `read_hadronization_infos` |

## 3. Odczyt [▷]

W v3.0 tablice HERWIG dla epoki BBN i ich czytnik są takie same jak w v2.3. Własność ustalona w REVIEW_098, 106 i 110 (wiersze wygenerowane przy √s = E′, choć manual mówi E′ = √s/2) przechodzi więc do najnowszego wydania. Nie sprawdzałem, czy manual v3.0 (arXiv:2606.06355) zmienił opis konwencji. Jeśli tak, wada byłaby w dokumentacji, a nie w danych. To jedyna otwarta część tej bramki.

## 4. Granice

- Porównanie plików, nie fizyki. Identyczność bajtowa nie mówi nic o tym, jak v3.0 używa tablic poza czytnikiem. Różnice w `primary.c` (824 linie diff) i `evolution.c` przejrzałem tylko pod kątem słowa „herwig”.
- Nowość DIR-009 nadal nie ustalona (REC13 ROT020 i ROT021, EKS1 ROT023). REC13 znalazł jedno opublikowane użycie HERWIG z BlackHawk (Thoss, Burkert, Kohri 2024, MNRAS 532, 451), bez potwierdzenia wersji i wyboru tablic.

## 5. Trzy warstwy

- **Wynik:** tablice HERWIG w v3.0 są bajtowo równe v2.3, czytnik ma tę samą logikę; wada etykiety przechodzi do v3.0 [▷].
- **Konfiguracja:** REC13 nie mógł rozpakować archiwum w swoim środowisku. Środowisko Badacza ma dostęp do hepforge i lokalne archiwum v2.3 z 085, więc bramkę zamknąłem w kilka minut, a nie przekazywałem jej dalej.
- **Uczenie systemu:** kiedy bramka innej komórki stoi na dostępie, a ja ten dostęp mam, wykonuję ją z jej regułą decyzji i podaję ją jako jej regułę. Przy pobieraniu z hepforge `downloads?f=` zwraca stronę przekierowania (249 B), a archiwum podaje `downloader?f=`; przed haszowaniem trzeba sprawdzić rozmiar i nagłówek pliku.

## 6. Dane

- `data/compare111.json` (katalogi SHA-256 i werdykty), `data/src_diff_111.log` (SHA archiwów, `diff -rq`, liczby linii diff).
- Kod: `code/compare_bh_tables_111.py`.

## r2 (22 XI, 20:20, godzina z `date` przy zapisie): dokumentacja v3.0 też bez zmian; otwarta część §3 zamknięta

- **Manuale w archiwum v3.0** to te same pliki co w v2.3: `manuals/BlackHawk_v2.3.pdf` (SHA-256 75a65ab1…) i `BlackHawk_v2.3_note.pdf` (673c99ae…) są bajtowo równe w obu archiwach. Osobnego manuala v3.0 w archiwum nie ma. Zapis: `data/manuals_sha_111r2.json`.
- **Artykuł v3.0** (arXiv:2606.06355v1): spis treści obejmuje nowe metryki, współczynniki szarego ciała (GrayHawk), tablice Kerra, parametry i walidację. Nie ma w nim części o hadronizacji. Odczytane strony nie wspominają o zmianie tablic HERWIG ani opcji `hadronization_choice`; w sprawach poza nowymi funkcjami artykuł odsyła do manuali v1/v2. Strony 5–6, 10 i 14–15 nie były zwrócone przez narzędzie; wniosek opiera się na spisie treści i odczytanych stronach.
- **Dziennik zmian w README v3.0**: „metryki … dodane przez GrayHawk; poprawiony Kerr i inne metryki; nowe procedury ekstrapolacji; poprawione błędy”. Hadronizacja nie jest wymieniona.
- **Skrypty generatora** (`herwig_scripts/*/main.cpp` z `LuminosityFunction:Energy = E′` oraz `formatting.c`, który dzieli przez 2 i podpisuje wiersz energią E′; REVIEW_098) są w v3.0 bajtowo te same (§2).

**Odczyt [▷]:** w v3.0 dane, czytnik, skrypty generatora i dokumentacja tablic HERWIG dla epoki BBN są takie same jak w v2.3. Rozbieżność między manualem (E′ = √s/2) a danymi (√s = E′) jest więc obecna w najnowszym wydaniu bez zmian. Werdykt bramki EKS1/REC13: SAME, łącznie z dokumentacją.
