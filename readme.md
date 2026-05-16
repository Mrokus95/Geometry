# Projekt: Otoczka wypukła (Zespół nr 9)

## Opis projektu
Program służy do wyznaczania otoczki wypukłej dla podanych czterech punktów na płaszczyźnie. Aplikacja informuje, jakim zbiorem jest wynikowa otoczka wypukła (czworokąt, trójkąt, odcinek, punkt) oraz wypisuje współrzędne jej kolejnych wierzchołków.

Projekt posiada prosty interfejs tekstowy, w którym użytkownik ręcznie wprowadza dane oraz wybiera operacje do wykonania.

## Skład zespołu
* **Tomasz Czech** (Nr indeksu: 189803)
  * *Zadania:* Uzupełnienie dokumentacji projektu, przygotowanie instrukcji uruchomienia programu.
* **Mateusz Loska** (Nr indeksu: 189804)
  * *Zadania:* Analiza i wybór możliwych algorytmów, wstępne przygotowanie koncepcji skryptu, przygotowanie funkcji iloczynu wektorowego/testu orientacji.
* **Franciszek Spyra** (Nr indeksu: 189809)
  * *Zadania:* Implementacja algorytmów Grahama i Quickhull.

## Struktura plików z kodem źródłowym
* `projekt_geometria_otoczka_wypukla.py` – główny plik programu zawierający implementację algorytmów wyznaczania otoczki wypukłej (Graham, Jarvis, Quickhull), funkcje pomocnicze (iloczyn wektorowy, odległość) oraz funkcję wizualizacji wyników przy użyciu biblioteki `matplotlib`.
* `otoczka_debugowa.py` – rozszerzona wersja programu służąca do analizowania działania algorytmów w trybie debugowania. Zawiera komunikaty diagnostyczne (`print`) pokazujące przebieg obliczeń, wybór punktów, kierunki skrętów oraz działanie rekurencji.
* `otoczka_wypukla.ipynb` – notebook Jupyter służący wyłącznie do testów i wizualizacji działania algorytmów za pomocą `matplotlib`.

## Wymagania i instalacja
Do prawidłowego działania programu wymagane są:
* Zainstalowany Python 3.x
* Biblioteka zewnętrzna: `matplotlib`

W przypadku braku biblioteki `matplotlib`, można ją zainstalować za pomocą menedżera pakietów `pip`:
```bash
pip install matplotlib
```

## Instrukcja uruchomienia

### 1. Uruchomienie pliku `.py` (Terminal / CMD)
Program można uruchomić z poziomu wiersza poleceń:
* **Krok 1 (Przejście do katalogu z plikiem):**
  ```bash
  cd ścieżka_do_folderu_z_programem
  ```
* **Krok 2 (Uruchomienie programu):**
  ```bash
  python otoczka_wypukla.py
  ```
  lub (w zależności od konfiguracji systemu):
  ```bash
  py otoczka_wypukla.py
  ```

### 2. Uruchomienie pliku `.ipynb` (Jupyter Notebook)
Notebook służy do testowania i prezentacji działania programu. Plik można otworzyć w jednym z poniższych środowisk:
* Visual Studio Code (z rozszerzeniem Jupyter)
* Google Colab (środowisko online)
* Jupyter Notebook / Jupyter Lab

## Opcje programu i specyfikacja danych

### Wprowadzenie współrzędnych punktów
Użytkownik wprowadza cztery punkty na płaszczyźnie w postaci par liczb rzeczywistych `(x, y)`.
* **Dozwolone wartości:** liczby rzeczywiste (typ `float`), dowolny zakres liczbowy.
* **Wymagany format:** dwie liczby oddzielone spacją (np. `0 1`).
* W przypadku błędnego formatu danych program zgłasza błąd i prosi o ponowne wprowadzenie wartości.

### Wybór algorytmu
Użytkownik wybiera jeden z trzech dostępnych algorytmów wyznaczania otoczki wypukłej:
* `1` → Algorytm Grahama
* `2` → Algorytm Jarvisa
* `3` → Algorytm Quickhull

### Wyświetlenie wyników
Program analizuje zbiór punktów, usuwa punkty wewnętrzne, porządkuje wierzchołki otoczki i wypisuje:
* Typ figury (punkt / odcinek / trójkąt / czworokąt)
* Współrzędne wierzchołków otoczki

#### Przykładowe wywołanie (konsola):
```text
Podaj 4 punkty (x y):
Punkt 1: 0 1
Punkt 2: 1 0
Punkt 3: 2 0
Punkt 4: 0 4
Wybierz algorytm:
1 - Graham
2 - Jarvis
3 - Quickhull
Twój wybór: 1
Otoczka: [(1.0, 0.0), (2.0, 0.0), (0.0, 4.0), (0.0, 1.0)]
```

## Schemat algorytmu / Pseudokod

```text
1. Wczytaj współrzędne czterech punktów: A, B, C, D
2. Umieść punkty w zbiorze P
3. Wybierz algorytm wyznaczania otoczki (Graham / Jarvis / Quickhull)
4. W zależności od wybranego algorytmu:
   - wykonaj odpowiednią metodę wyznaczania otoczki
5. Sprawdź współliniowość punktów:
   - oblicz orientację dla odpowiednich trójek punktów
   - jeśli wszystkie wartości orientacji są równe:
     - jeśli wszystkie punkty są identyczne:
       wynik = punkt
     - w przeciwnym razie:
       wynik = odcinek (skrajne punkty)
     - zakończ program
6. Wyznacz otoczkę wypukłą:
   - dodaj pierwszy punkt do otoczki
   - przejdź przez kolejne punkty:
     - dopóki ostatnie trzy punkty nie tworzą skrętu w lewo:
       usuń środkowy punkt z otoczki
     - dodaj punkt do otoczki
7. Określ typ otoczki:
   - jeśli liczba punktów = 1 → punkt
   - jeśli liczba punktów = 2 → odcinek
   - jeśli liczba punktów = 3 → trójkąt
   - jeśli liczba punktów = 4 → czworokąt
8. Wypisz:
   - typ otoczki
   - współrzędne punktów otoczki w odpowiedniej kolejności
```

### Główne funkcje programu
* `main()` → wczytanie danych i sterowanie programem
* `orientacja()` → sprawdzanie skrętu punktów (test orientacji / iloczyn wektorowy)
* `otoczka()` → wyznaczanie otoczki wypukłej

## Niezgodności z założeniami
Nie stwierdzono niezgodności. Projekt został zrealizowany zgodnie z założeniami zawartymi w treści zadania.
