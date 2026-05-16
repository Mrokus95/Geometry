from algorithms.graham import graham_scan
from utils.helpers import cross_product


class TestCounterClockwiseOrder:
    def test_graham_ccw(self):
        points = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]
        hull = graham_scan(points)
        n = len(hull)
        for i in range(n):
            assert cross_product(hull[i], hull[(i + 1) % n], hull[(i + 2) % n]) >= 0

