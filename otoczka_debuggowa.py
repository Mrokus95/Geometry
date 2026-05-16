import math
import matplotlib.pyplot as plt

# ==========================================
# FUNKCJE POMOCNICZE (DEBUG)
# ==========================================

def iloczyn_wektorowy(p1, p2, p3):
    wynik = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    # Zwraca > 0 dla skrętu w lewo, < 0 dla skrętu w prawo, 0 dla współliniowych
    print(f"      [Pomocnicza] Iloczyn wektorowy: wektory ({p1}->{p2}) i ({p1}->{p3}) | Wynik: {wynik:.2f}")
    return wynik

def odleglosc_kwadrat(p1, p2):
    d = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
    print(f"      [Pomocnicza] Kwadrat odległości między {p1} a {p2} | Wynik: {d:.2f}")
    return d

# ==========================================
# ALGORYTM GRAHAMA (DEBUG)
# ==========================================

def algorytm_grahama(punkty):
    print("\n" + "="*50)
    print("ROZPOCZYNAM ALGORYTM GRAHAMA")
    print("="*50)
    
    punkty = list(set(punkty))
    if len(punkty) <= 2:
        print("Mniej niż 3 unikalne punkty. Zwracam je jako otoczkę.")
        return punkty

    # Krok 1: Znalezienie punktu startowego
    p0 = min(punkty, key=lambda p: (p[1], p[0]))
    print(f"\n[KROK 1] Znaleziono punkt startowy p0 (najniższy Y, potem X): {p0}")

    # Krok 2: Sortowanie kątowe
    print("\n[KROK 2] Sortowanie pozostałych punktów po kącie względem p0...")
    def klucz(p):
        print("\nKąt między tymi punktami wyliczony z atan:", math.atan2(p[1] - p0[1], p[0] - p0[0]))
        return (
            math.atan2(p[1] - p0[1], p[0] - p0[0]),
            odleglosc_kwadrat(p0, p)
        )

    posortowane = sorted([p for p in punkty if p != p0], key=klucz)
    print(f"Posortowane punkty: {posortowane}")

    # Krok 3: Budowa stosu
    stos = [p0, posortowane[0]]
    print(f"\n[KROK 3] Inicjalizacja stosu z 2 pierwszymi punktami: {stos}")

    for p in posortowane[1:]:
        print(f"\n--- Rozpatruję nowy punkt z posortowanej listy: {p} ---")
        while len(stos) > 1:
            print(f"  Sprawdzam skręt dla: {stos[-2]} -> {stos[-1]} -> {p}")
            kierunek = iloczyn_wektorowy(stos[-2], stos[-1], p)
            if kierunek <= 0:
                print(f"  [! UWAGA] Skręt w prawo lub linia prosta (wynik <= 0). Odrzucam punkt {stos[-1]} ze stosu.")
                stos.pop()
            else:
                print("  [OK] Skręt w lewo (wynik > 0). Zatrzymuję pętlę sprawdzania.")
                break
        stos.append(p)
        print(f"  Dodaję punkt {p} do stosu. Aktualny stos: {stos}")

    print("\nZAKOŃCZONO ALGORYTM GRAHAMA")
    return stos

# ==========================================
# ALGORYTM JARVISA (DEBUG)
# ==========================================

def algorytm_jarvisa(punkty):
    print("\n" + "="*50)
    print("ROZPOCZYNAM ALGORYTM JARVISA (MARSZ JARVISA)")
    print("="*50)
    
    punkty = list(set(punkty))
    if len(punkty) <= 2:
        return punkty

    start = min(punkty, key=lambda p: p[0])
    print(f"\n[KROK 1] Punkt startowy (najbardziej po lewej, min X): {start}")
    
    otoczka = []
    obecny = start

    krok = 1
    while True:
        print(f"\n--- KROK MARSZU {krok} ---")
        print(f"Dodaję {obecny} do otoczki.")
        otoczka.append(obecny)
        
        nastepny = punkty[0]
        print(f"Wstępnie zakładam, że następnym punktem będzie {nastepny}")

        for p in punkty:
            if p == obecny:
                continue

            print(f"  Porównuję z potencjalnym kandydatem: {p}")
            kierunek = iloczyn_wektorowy(obecny, nastepny, p)

            if (nastepny == obecny or
                kierunek > 0 or
                (kierunek == 0 and odleglosc_kwadrat(obecny, p) > odleglosc_kwadrat(obecny, nastepny))):
                print(f"  [!] Znaleziono lepszego kandydata, który jest bardziej 'na prawo'. Zmieniam na: {p}")
                nastepny = p

        obecny = nastepny
        print(f"Zatwierdzono następny punkt: {obecny}")
        
        if obecny == start:
            print("Osiągnięto punkt startowy. Zamykam otoczkę!")
            break
        krok += 1

    print("\nZAKOŃCZONO ALGORYTM JARVISA")
    return otoczka

# ==========================================
# ALGORYTM QUICKHULL (DEBUG)
# ==========================================

def algorytm_quickhull(punkty):
    print("\n" + "="*50)
    print("ROZPOCZYNAM ALGORYTM QUICKHULL")
    print("="*50)
    
    punkty = list(set(punkty))
    if len(punkty) <= 2:
        return punkty

    def odleglosc_od_linii(p1, p2, p):
        return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
                   (p2[1] - p1[1]) * (p[0] - p1[0]))

    def rekurencja(zbior, p1, p2, glebokosc=1):
        wciecie = "  " * glebokosc
        print(f"\n{wciecie}[REKURENCJA L{glebokosc}] Szukam w zbiorze: {zbior} dla linii {p1} -> {p2}")
        
        if not zbior:
            print(f"{wciecie}Zbiór pusty, wracam.")
            return []

        najdalszy = max(zbior, key=lambda p: odleglosc_od_linii(p1, p2, p))
        print(f"{wciecie}Najdalszy punkt od linii to: {najdalszy}")

        lewy1 = [p for p in zbior if iloczyn_wektorowy(p1, najdalszy, p) > 0]
        lewy2 = [p for p in zbior if iloczyn_wektorowy(najdalszy, p2, p) > 0]
        
        print(f"{wciecie}Podział: nowe punkty na zewnątrz ({p1}->{najdalszy}): {lewy1}")
        print(f"{wciecie}Podział: nowe punkty na zewnątrz ({najdalszy}->{p2}): {lewy2}")

        return (rekurencja(lewy1, p1, najdalszy, glebokosc+1) +
                [najdalszy] +
                rekurencja(lewy2, najdalszy, p2, glebokosc+1))

    # Krok 1: Ekstrema
    min_x = min(punkty, key=lambda p: p[0])
    max_x = max(punkty, key=lambda p: p[0])
    print(f"\n[KROK 1] Znaleziono ekstrema na osi X. Min: {min_x}, Max: {max_x}")

    # Krok 2: Podział początkowy na dwa podzbiory
    print("\n[KROK 2] Dzielę zbiór na lewy i prawy względem prostej tworzonej przez ekstrema.")
    lewy = [p for p in punkty if iloczyn_wektorowy(min_x, max_x, p) > 0]
    prawy = [p for p in punkty if iloczyn_wektorowy(max_x, min_x, p) > 0]
    print(f"Zbiór 'lewy' (górny): {lewy}")
    print(f"Zbiór 'prawy' (dolny): {prawy}")

    # Krok 3: Start rekurencji
    print("\n[KROK 3] Uruchamiam rekurencję dla obu połówek...")
    wynik = ([min_x] +
             rekurencja(lewy, min_x, max_x) +
             [max_x] +
             rekurencja(prawy, max_x, min_x))

    print("\nZAKOŃCZONO ALGORYTM QUICKHULL")
    return wynik

# ==========================================
# WIZUALIZACJA I GŁÓWNA PĘTLA
# ==========================================

def rysuj_otoczke(punkty, otoczka):
    xs = [p[0] for p in punkty]
    ys = [p[1] for p in punkty]

    zamknieta = otoczka + [otoczka[0]]
    ox = [p[0] for p in zamknieta]
    oy = [p[1] for p in zamknieta]

    plt.figure(figsize=(6, 6))
    plt.plot(ox, oy, 'r-', linewidth=2, label="Otoczka")
    plt.scatter(xs, ys, c='blue', label="Punkty")

    for i, p in enumerate(punkty):
        plt.annotate(f"P{i+1}\n{p}", (p[0], p[1]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.title("Wizualizacja Otoczki Wypukłej")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

def main():
    punkty = []

    print("--- PROGRAM DO WYZNACZANIA OTOCZKI WYPUKŁEJ (TRYB DEBUG) ---")
    while True:
        try:
            n = int(input("Podaj liczbę punktów: "))
            if n > 0:
                break
            else:
                print("Liczba punktów musi być większa od zera.")
        except ValueError:
            print("To nie jest poprawna liczba całkowita. Spróbuj ponownie.")

    print(f"Podaj {n} punktów (x y):")
    for i in range(n):
        while True:
            try:
                x, y = map(float, input(f"Punkt {i+1}: ").split())
                punkty.append((x, y))
                break
            except ValueError:
                print("Błąd. Podaj dwie liczby oddzielone spacją (np. '2.5 3').")

    print("\nWybierz algorytm:")
    print("1 - Graham")
    print("2 - Jarvis")
    print("3 - Quickhull")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        otoczka = algorytm_grahama(punkty)
    elif wybor == "2":
        otoczka = algorytm_jarvisa(punkty)
    elif wybor == "3":
        otoczka = algorytm_quickhull(punkty)
    else:
        print("Nieznany wybór, domyślnie uruchamiam algorytm Grahama.")
        otoczka = algorytm_grahama(punkty)

    print("\n" + "="*50)
    print("KOŃCOWY WYNIK - OTOCZKA:", otoczka)
    print("="*50)
    rysuj_otoczke(punkty, otoczka)

if __name__ == "__main__":
    main()