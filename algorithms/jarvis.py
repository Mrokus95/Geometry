from utils.helpers import cross_product, squared_distance

def jarvis_march(points, debug=False):
    def dprint(text):
        if debug: print(text)

    dprint("\n" + "=" * 50 + "\nROZPOCZYNAM MARSZ JARVISA\n" + "=" * 50)

    points = list(set(points))
    if len(points) <= 2:
        return points

    # Step 1: Start from the leftmost point
    start = min(points, key=lambda point: (point[0], point[1]))
    dprint(f"\n[KROK 1] Punkt startowy (najbardziej lewy): {start}")

    hull = []
    current = start
    step = 1

    while True:
        dprint(f"\n--- KROK {step} ---")
        dprint(f"Dodaję {current} do otoczki.")
        hull.append(current)

        next_point = points[0]
        for p in points:
            if p == current:
                continue

            direction = cross_product(current, next_point, p, debug=False)
            if (next_point == current or
                    direction > 0 or
                    (direction == 0 and squared_distance(current, p) > squared_distance(current, next_point))):
                if debug: dprint(f"  [!] Lepszy kandydat: {p} (zastępuje {next_point})")
                next_point = p

        current = next_point
        dprint(f"Zatwierdzony następny punkt: {current}")

        if current == start:
            dprint("Osiągnięto punkt startowy. Otoczka zamknięta!")
            break
        step += 1

    return hull
