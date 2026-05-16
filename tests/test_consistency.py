import pytest

from algorithms.graham import graham_scan
from algorithms.jarvis import jarvis_march
from algorithms.quickhull import quickhull


class TestAlgorithmConsistency:
    @pytest.mark.parametrize("points,expected_size", [
        ([(0.0, 0.0), (3.0, 0.0), (3.0, 3.0), (0.0, 3.0)], 4),
        ([(0.0, 0.0), (4.0, 0.0), (2.0, 3.0), (2.0, 1.0)], 3),
        ([(0.0, 0.0), (1.0, 0.0), (2.0, 0.0), (3.0, 0.0)], 2),
        ([(0.0, 0.0), (5.0, 1.0), (2.0, 4.0), (1.5, 2.0)], 3),
        ([(-3.0, -2.0), (4.0, -1.0), (2.0, 5.0), (-1.0, 3.0)], 4),
        ([(-5.0, 0.0), (0.0, 5.0), (5.0, 0.0), (0.0, -5.0)], 4),
        ([(-1.0, -1.0), (1.0, -1.0), (0.0, 1.0), (0.0, 0.0)], 3),
        ([(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (0.5, 0.5)], 3),
        ([(0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (-0.5, -0.5)], 3),
        ([(1e6, 0.0), (-1e6, 0.0), (0.0, 1e6), (0.0, -1e6)], 4),
        ([(0.0, 0.0), (100.0, 0.01), (200.0, 0.0), (100.0, -0.01)], 4),
        ([(1, 2), (3, 4), (5, 2), (3, 0)], 4),
        ([(0, 0), (10, 0), (5, 1), (5, 8)], 3),
        ([(0, 0), (6, 0), (3, 4), (3, 1)], 3),
        ([(0, 0), (4, 0), (2, 3), (1, 0)], 3),
    ])
    def test_same_hull_points(self, points, expected_size):
        g = set(graham_scan(points))
        j = set(jarvis_march(points))
        q = set(quickhull(points))

        assert g == j == q, (
            f"Algorytmy zwrocily rozne wyniki!\n"
            f"Graham:    {g}\n"
            f"Jarvis:    {j}\n"
            f"Quickhull: {q}"
        )
        assert len(g) == expected_size, (
            f"Oczekiwano {expected_size} wierzcholkow, otrzymano {len(g)}"
        )

