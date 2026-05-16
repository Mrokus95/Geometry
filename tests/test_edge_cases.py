from algorithms.graham import graham_scan
from algorithms.jarvis import jarvis_march
from algorithms.quickhull import quickhull


class TestEdgeCases:
    def test_single_point_graham(self):
        assert len(graham_scan([(1, 1)])) == 1

    def test_two_points_graham(self):
        assert len(graham_scan([(0, 0), (1, 1)])) == 2

    def test_single_point_jarvis(self):
        assert len(jarvis_march([(1, 1)])) == 1

    def test_two_points_jarvis(self):
        assert len(jarvis_march([(0, 0), (1, 1)])) == 2

    def test_single_point_quickhull(self):
        assert len(quickhull([(1, 1)])) == 1

    def test_two_points_quickhull(self):
        assert len(quickhull([(0, 0), (1, 1)])) == 2

    def test_duplicates_graham(self):
        assert len(graham_scan([(1, 1), (1, 1), (1, 1), (1, 1)])) == 1

    def test_duplicates_jarvis(self):
        assert len(jarvis_march([(0, 0), (0, 0), (1, 1), (1, 1)])) == 2

    def test_collinear_graham(self):
        assert len(graham_scan([(0, 0), (1, 0), (2, 0), (3, 0)])) == 2

    def test_collinear_jarvis(self):
        assert len(jarvis_march([(0, 0), (1, 0), (2, 0), (3, 0)])) == 2

    def test_collinear_quickhull(self):
        assert len(quickhull([(0, 0), (1, 0), (2, 0), (3, 0)])) == 2

    def test_all_same_points_jarvis(self):
        assert len(jarvis_march([(5, 5), (5, 5), (5, 5)])) == 1

    def test_all_same_points_quickhull(self):
        assert len(quickhull([(3, 3), (3, 3), (3, 3)])) == 1

    def test_large_coordinates(self):
        pts = [(1e9, 1e9), (-1e9, 1e9), (-1e9, -1e9), (1e9, -1e9)]
        g = set(graham_scan(pts))
        j = set(jarvis_march(pts))
        q = set(quickhull(pts))
        assert g == j == q
        assert len(g) == 4

    def test_negative_coordinates_only(self):
        pts = [(-1, -1), (-4, -1), (-4, -4), (-1, -4)]
        g = set(graham_scan(pts))
        j = set(jarvis_march(pts))
        q = set(quickhull(pts))
        assert g == j == q
        assert len(g) == 4

    def test_zero_coordinates(self):
        assert len(graham_scan([(0, 0), (0, 0), (0, 0), (1, 1)])) == 2

    def test_very_close_points(self):
        pts = [(0.0, 0.0), (0.001, 0.0), (0.001, 0.001), (0.0, 0.001)]
        g = set(graham_scan(pts))
        j = set(jarvis_march(pts))
        q = set(quickhull(pts))
        assert g == j == q
        assert len(g) == 4

    def test_vertical_line(self):
        assert len(graham_scan([(0, 0), (0, 1), (0, 2), (0, 3)])) == 2

    def test_single_unique_point_after_dedup(self):
        assert len(quickhull([(2, 2), (2, 2), (2, 2), (2, 2)])) == 1

    def test_float_coordinates(self):
        pts = [(0.5, 1.5), (2.5, 0.5), (3.5, 2.5), (1.5, 3.5)]
        g = set(graham_scan(pts))
        j = set(jarvis_march(pts))
        q = set(quickhull(pts))
        assert g == j == q

    def test_mixed_positive_negative(self):
        pts = [(-2, -3), (4, -1), (3, 5), (-1, 4)]
        g = set(graham_scan(pts))
        j = set(jarvis_march(pts))
        q = set(quickhull(pts))
        assert g == j == q
        assert len(g) == 4

