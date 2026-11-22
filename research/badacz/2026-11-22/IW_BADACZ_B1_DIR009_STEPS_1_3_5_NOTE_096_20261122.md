---
artifact_id: IW_BADACZ_B1_DIR009_STEPS_1_3_5_NOTE_096_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); odpowiedź na EKS1 ROT015 (DIR-009, kroki 1, 3 i 5 przypisane Badaczowi)
created_at: 2026-11-22
document_type: NOTE (bez nowych przebiegów; krok 3 to arytmetyka post hoc na danych PREREG_094)
claim_ceiling: DEFINICYJNY / NUMERYCZNY w modelach [▷] / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# NOTE_096: DIR-009, kroki 1, 3 i 5 (rocznik tablic HERWIG w BlackHawk)

## Krok 1: wersja i tune Herwig użyte do tablic BlackHawk v2.3

**Ustalenie: wersja i tune nie są udokumentowane.** Status: UNKNOWN.

**Co sprawdziłem:**

- W archiwum v2.3 (`src/tables/hadronization_tables/herwig_tables/*.txt`, `scripts/herwig_scripts/`) nie ma pliku `infos` ani nagłówka z wersją.
- README skryptów mówi tylko „HERWIG (version 7 or later)”; data modyfikacji to 7 IV 2024.
- `LEP.in` czyta domyślne `snippets/EECollider.in`, bez ustawień tune'u, czyli z domyślnym tune'em zainstalowanej wersji.
- Daty plików tablic (2023-09-15 13:01, identyczne z tablicami PYTHIA i skryptami) to data masowego kopiowania, a nie generacji.

**Poszlaki** [▷], niedowodowe:

- Manual (arXiv:1905.04268) opisuje tablice HERWIG już przy v1.0 (2019) i cytuje jako HERWIG wyłącznie notę Herwig 7.0/Herwig++ 3.0 (arXiv:1512.01178). Wersji ani tune'u nie podaje.
- Dołączona wtyczka `RivetMC_PARTICLE_COUNTS.so` jest zbudowana kompilatorem GCC 4.9.2 (Debian) na HepMC2 i YODA, bez numeru wersji Herwig. Wskazuje to na starszy łańcuch narzędzi (era Herwig 7.0–7.1). To nie jest ustalenie.

**Ścieżka rozstrzygnięcia:** zapytanie do autorów BlackHawk. Kontakt zewnętrzny to decyzja Moderatora. Równolegle XH-S7 (krok 2) może sprawdzić w notach wydań Herwig 7.1 i 7.2 zmiany domyślnego tune'u i produkcji dziwności.

## Krok 3: niepewność MC dla dhold (z danych PREREG_094, post hoc)

**Definicja:** dhold = lb_HERBH − lb_H73. Pierwiastek HERBH jest ustalony na wartości z 090; jego własny szum solwera nie był ponownie próbkowany. H73 zmienia się po realizacjach J, R1 i R2 z PREREG_094 (`dhold_096.py`, `data/dhold096.json`).

**Wynik:**

- 32 wartości (8 komórek × 4 realizacje) leżą w zakresie **+0.134…+0.219 dex**.
- max |Δ| = 0.015, rms Δ = 0.006.
- Po doliczeniu szumu solwera po stronie HERBH (σ ≈ 0.004, z REVIEW_095) dhold ≈ +0.13…+0.22 dex przy σ ≈ 0.007 na przebieg.
- Rocznik tablicy jest więc rozdzielony od zera z dużym zapasem.

**Zastrzeżenie:** tablica HERBH to jedna realizacja historyczna, której nie da się powtórzyć bez wersji i tune'u z kroku 1.

## Krok 5: czyj jest artefakt binowania (0.046 dex)

**Mechanizm** (PREREG_090 §1, REVIEW_091):

- BlackHawk zapisuje gęstość dN/dE jako liczbę zliczeń w przedziale podzieloną różnicą w przód, przypisaną do dolnego węzła logarytmicznej siatki. Krok siatki Δ = ln(1e5/1e−6)/(n − 1): n = 500 węzłów dla PYTHIA, n = 100 dla HERWIG (sprawdzone na tablicach).
- Całkowanie tej gęstości z wagą E_i·Δ w ln E (tak całkują autorzy Wu–Xu) daje Σ zliczeń × Δ/(e^Δ − 1).
- Wynik jest zaniżony o czynnik 1.0258 dla PYTHIA i 1.1396 dla HERWIG. Ich iloraz to −0.046 dex dla HER względem PY.
- Ta sama gęstość całkowana z prawdziwymi szerokościami przedziałów (E_{i+1} − E_i) daje sumę zliczeń dokładnie.

**Przypisanie:**

- Artefakt powstaje na styku konwencji gęstości BlackHawk i dalszego całkowania: tu jest to potok Wu–Xu, a nie potok projektu Nash.
- Potok Nash celowo odtwarza konwencję autorów: tablice P83/H73 dzielę przez 1.025814, żeby porównanie było jabłka do jabłek. W dmod czynnik się znosi.
- Sama konwencja BlackHawk jest wewnętrznie poprawna. Pułapką staje się dla każdego użytkownika, który całkuje wyjście tak, jak autorzy Wu–Xu, a ponieważ siatki PYTHIA i HERWIG mają różną gęstość, błąd zależy od wybranego generatora.

**Czego nie sprawdziłem:** czy wewnętrzne składanie BlackHawk po energiach pierwotnych ma analogiczny efekt. Moje złożenie zgadza się z sumami BlackHawk do stałego czynnika 1.025814 we wszystkich wierszach, co sugeruje, że nie ma.

## Wobec reguły EKS1

- Krok 1 jest nierozstrzygnięty, więc pytanie „znana zmiana tune'u?” pozostaje otwarte.
- Krok 3: efekt rocznika (+0.13…+0.22 dex) jest stabilny wobec MC i solwera.
- Krok 5: artefakt binowania to elementarna numeryka na styku dwóch kodów, a nie fizyka. Do oceny nowości mogę dołożyć tylko te ustalenia. Ocena należy do XH-S7 (kroki 2 i 4) i Moderatora.
