from algorithms.graham import graham_scan
from algorithms.jarvis import jarvis_march
from algorithms.quickhull import quickhull
from utils.helpers import parse_point
from utils.visualization import draw_hull

def main():
    print("--- PROGRAM DO WYZNACZANIA OTOCZKI WYPUKŁEJ (4 PUNKTY) ---")

    while True:
        points = []
        n = 4

        print(f"\nPodaj współrzędne {n} punktów (x y):")
        for i in range(n):
            while True:
                try:
                    x, y = parse_point(input(f"Punkt {i + 1}: "))
                    points.append((x, y))
                    break
                except ValueError:
                    print("Błąd. Podaj dwie liczby oddzielone spacją (np. '2.5 3').")

        print("\nWybierz algorytm:")
        print("1 - Algorytm Grahama")
        print("2 - Marsz Jarvisa")
        print("3 - Quickhull")
        choice = input("Twój wybór (domyślnie 1): ")

        debug_input = input("Czy włączyć tryb krok po kroku (wypisywanie logów)? (t/n): ").strip().lower()
        debug_mode = (debug_input == 't')

        if choice == "2":
            hull = jarvis_march(points, debug=debug_mode)
        elif choice == "3":
            hull = quickhull(points, debug=debug_mode)
        else:
            hull = graham_scan(points, debug=debug_mode)

        print("\n" + "=" * 50)

        vertex_count = len(hull)
        if vertex_count == 1:
            shape = "PUNKT"
        elif vertex_count == 2:
            shape = "ODCINEK"
        elif vertex_count == 3:
            shape = "TRÓJKĄT"
        elif vertex_count == 4:
            shape = "CZWOROKĄT"
        else:
            shape = "WIELOKĄT"

        print(f"INFORMACJA: Otoczka wypukła jest zbiorem typu: **{shape}**")
        print("-" * 50)
        print("Współrzędne kolejnych wierzchołków otoczki wypukłej:")
        for vertex in hull:
            print(f" -> {vertex}")
        print("=" * 50)

        draw_hull(points, hull)

        again = input("\nCzy chcesz wyznaczyć nową otoczkę dla innych punktów? (t/n): ").strip().lower()
        if again != 't':
            print("Zamykanie programu. Do widzenia!")
            break


if __name__ == "__main__":
    main()
