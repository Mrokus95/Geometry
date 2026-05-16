import functools
from utils.helpers import cross_product, squared_distance

def graham_scan(points, debug=False):
    def dprint(text):
        if debug: print(text)

    dprint("\n" + "=" * 50 + "\nROZPOCZYNAM ALGORYTM GRAHAMA\n" + "=" * 50)

    points = list(set(points))
    if len(points) <= 2:
        dprint("Mniej niż 3 unikalne punkty. Zwracam je jako otoczkę.")
        return points

    # Step 1: Find the lowest point (lowest Y, then lowest X)
    pivot = min(points, key=lambda p: (p[1], p[0]))
    dprint(f"\n[KROK 1] Znaleziono punkt startowy: {pivot}")

    dprint("\n[KROK 2] Sortowanie punktów po kącie względem punktu startowego (bez trygonometrii)...")

    def compare_angles(p1, p2):
        angle_direction = cross_product(pivot, p1, p2, debug=False)
        if angle_direction > 0:
            return -1
        elif angle_direction < 0:
            return 1
        else:
            d1 = squared_distance(pivot, p1)
            d2 = squared_distance(pivot, p2)
            if d1 < d2:
                return -1
            elif d1 > d2:
                return 1
            else:
                return 0

    remaining = [p for p in points if p != pivot]
    sorted_points = sorted(remaining, key=functools.cmp_to_key(compare_angles))
    dprint(f"Posortowane punkty: {sorted_points}")

    # Step 3: Build the convex hull stack
    stack = [pivot, sorted_points[0]]
    dprint(f"\n[KROK 3] Inicjalny stos: {stack}")

    for p in sorted_points[1:]:
        dprint(f"\n--- Przetwarzanie punktu: {p} ---")
        while len(stack) > 1:
            dprint(f"  Sprawdzanie zwrotu: {stack[-2]} -> {stack[-1]} -> {p}")
            direction = cross_product(stack[-2], stack[-1], p, debug)
            if direction <= 0:
                dprint(f"  [!] Zwrot w prawo lub punkty współliniowe. Usuwam {stack[-1]} ze stosu.")
                stack.pop()
            else:
                dprint("  [OK] Zwrot w lewo. Zachowuję punkt.")
                break
        stack.append(p)
        dprint(f"  Bieżący stos: {stack}")

    dprint("\nALGORYTM GRAHAMA ZAKOŃCZONY")
    return stack
