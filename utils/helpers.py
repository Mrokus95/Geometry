from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


def cross_product(p1, p2, p3, debug=False):
    """Returns cross product of vectors (p1->p2) and (p1->p3).
    > 0: left turn | < 0: right turn | = 0: collinear
    """
    result = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if debug:
        print(f"      [Pomocnicza] Iloczyn wektorowy: ({p1}->{p2}) i ({p1}->{p3}) | Wynik: {result:.2f}")
    return result


def squared_distance(p1, p2, debug=False):
    """Returns squared Euclidean distance between two points."""
    d = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
    if debug:
        print(f"      [Pomocnicza] Kwadrat odległości między {p1} a {p2} | Wynik: {d:.2f}")
    return d


def parse_point(raw: str) -> tuple:
    """Parses a raw input string into a (x, y) float tuple.

    Accepts any whitespace as separator (spaces, double spaces, tabs).
    Raises ValueError if input is not exactly two numeric values.
    Uses half-up rounding to 2 decimal places.
    """
    parts = raw.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Expected exactly 2 values, got {len(parts)}: '{raw}'")

    def round_half_up_to_2(value: str) -> float:
        try:
            return float(Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
        except (InvalidOperation, ValueError) as exc:
            raise ValueError(f"Invalid numeric value: '{value}'") from exc

    x = round_half_up_to_2(parts[0])
    y = round_half_up_to_2(parts[1])
    return x, y