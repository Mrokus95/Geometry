from utils.helpers import cross_product

def quickhull(points, debug=False):
    def dprint(text):
        if debug: print(text)

    dprint("\n" + "=" * 50 + "\nROZPOCZYNAM ALGORYTM QUICKHULL\n" + "=" * 50)

    points = list(set(points))
    if len(points) <= 2:
        return points

    def distance_from_line(p1, p2, p):
        """Returns unsigned distance from point p to line p1->p2."""
        return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

    def recurse(subset, p1, p2, depth=1):
        indent = "  " * depth
        dprint(f"\n{indent}[REKURENCJA L{depth}] Linia {p1} -> {p2}, Zbiór: {subset}")

        if not subset:
            dprint(f"{indent}Zbiór pusty, wracam.")
            return []

        farthest = max(subset, key=lambda p: distance_from_line(p1, p2, p))
        dprint(f"{indent}Najdalszy punkt: {farthest}")

        left1 = [p for p in subset if cross_product(p1, farthest, p) > 0]
        left2 = [p for p in subset if cross_product(farthest, p2, p) > 0]
        dprint(f"{indent}Podział: punkty na zewnątrz ({p1}->{farthest}): {left1}")
        dprint(f"{indent}Podział: punkty na zewnątrz ({farthest}->{p2}): {left2}")

        return (recurse(left1, p1, farthest, depth + 1) +
                [farthest] +
                recurse(left2, farthest, p2, depth + 1))

    # Step 1: Find horizontal extremes
    min_x = min(points, key=lambda p: (p[0], p[1]))
    max_x = max(points, key=lambda p: (p[0], p[1]))
    dprint(f"\n[KROK 1] Ekstrema - Min: {min_x}, Max: {max_x}")

    if min_x == max_x:
        return [min_x]

    # Step 2: Split into upper and lower subsets
    upper = [p for p in points if cross_product(min_x, max_x, p) > 0]
    lower = [p for p in points if cross_product(max_x, min_x, p) > 0]
    dprint(f"\n[KROK 2] Podział. Górny: {upper}, Dolny: {lower}")

    return [min_x] + recurse(upper, min_x, max_x) + [max_x] + recurse(lower, max_x, min_x)
