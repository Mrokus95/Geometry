import math
import matplotlib.pyplot as plt

# ==========================================
# FUNKCJE POMOCNICZE
# ==========================================

def iloczyn_wektorowy(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def odleglosc_kwadrat(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

# ==========================================
# ALGORYTM GRAHAMA
# ==========================================

def algorytm_grahama(punkty):
    punkty = list(set(punkty))
    if len(punkty) <= 2:
        return punkty

    p0 = min(punkty, key=lambda p: (p[1], p[0]))

    def klucz(p):
        return (
            math.atan2(p[1] - p0[1], p[0] - p0[0]),
            odleglosc_kwadrat(p0, p)
        )

    posortowane = sorted([p for p in punkty if p != p0], key=klucz)

    stos = [p0, posortowane[0]]

    for p in posortowane[1:]:
        while len(stos) > 1 and iloczyn_wektorowy(stos[-2], stos[-1], p) <= 0:
            stos.pop()
        stos.append(p)

    return stos

# ==========================================
# ALGORYTM JARVISA
# ==========================================

def algorytm_jarvisa(punkty):
    punkty = list(set(punkty))
    if len(punkty) <= 2:
        return punkty

    start = min(punkty, key=lambda p: p[0])
    otoczka = []
    obecny = start

    while True:
        otoczka.append(obecny)
        nastepny = punkty[0]

        for p in punkty:
            if p == obecny:
                continue

            kierunek = iloczyn_wektorowy(obecny, nastepny, p)

            if (nastepny == obecny or
                kierunek > 0 or
                (kierunek == 0 and odleglosc_kwadrat(obecny, p) > odleglosc_kwadrat(obecny, nastepny))):
                nastepny = p

        obecny = nastepny
        if obecny == start:
            break

    return otoczka

# ==========================================
# ALGORYTM QUICKHULL
# ==========================================

def algorytm_quickhull(punkty):
    punkty = list(set(punkty))
    if len(punkty) <= 2:
        return punkty

    def odleglosc_od_linii(p1, p2, p):
        return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
                   (p2[1] - p1[1]) * (p[0] - p1[0]))

    def rekurencja(zbior, p1, p2):
        if not zbior:
            return []

        najdalszy = max(zbior, key=lambda p: odleglosc_od_linii(p1, p2, p))

        lewy1 = [p for p in zbior if iloczyn_wektorowy(p1, najdalszy, p) > 0]
        lewy2 = [p for p in zbior if iloczyn_wektorowy(najdalszy, p2, p) > 0]

        return (rekurencja(lewy1, p1, najdalszy) +
                [najdalszy] +
                rekurencja(lewy2, najdalszy, p2))

    min_x = min(punkty, key=lambda p: p[0])
    max_x = max(punkty, key=lambda p: p[0])

    lewy = [p for p in punkty if iloczyn_wektorowy(min_x, max_x, p) > 0]
    prawy = [p for p in punkty if iloczyn_wektorowy(max_x, min_x, p) > 0]

    return ([min_x] +
            rekurencja(lewy, min_x, max_x) +
            [max_x] +
            rekurencja(prawy, max_x, min_x))

# ==========================================
# WIZUALIZACJA
# ==========================================

def rysuj_otoczke(punkty, otoczka):
    xs = [p[0] for p in punkty]
    ys = [p[1] for p in punkty]

    zamknieta = otoczka + [otoczka[0]]
    ox = [p[0] for p in zamknieta]
    oy = [p[1] for p in zamknieta]

    plt.figure(figsize=(6, 6))
    plt.plot(ox, oy)
    plt.scatter(xs, ys)

    for i, p in enumerate(punkty):
        plt.annotate(f"P{i+1}", (p[0], p[1]))

    plt.grid()
    plt.axis('equal')
    plt.show()

def main():
    punkty = []

    # Pobieranie liczby punktów od użytkownika
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

    print("\nOtoczka:", otoczka)
    rysuj_otoczke(punkty, otoczka)

if __name__ == "__main__":
    main()