from algorithms.graham import graham_scan
from algorithms.jarvis import jarvis_march
from algorithms.quickhull import quickhull


class TestQuadrilateralGraham:
    def setup_method(self):
        self.points = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]

    def test_vertex_count(self):
        assert len(graham_scan(self.points)) == 4

    def test_all_points_on_hull(self):
        assert set(graham_scan(self.points)) == set(self.points)


class TestQuadrilateralJarvis:
    def setup_method(self):
        self.points = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]

    def test_vertex_count(self):
        assert len(jarvis_march(self.points)) == 4

    def test_all_points_on_hull(self):
        assert set(jarvis_march(self.points)) == set(self.points)


class TestQuadrilateralQuickhull:
    def setup_method(self):
        self.points = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]

    def test_vertex_count(self):
        assert len(quickhull(self.points)) == 4

    def test_all_points_on_hull(self):
        assert set(quickhull(self.points)) == set(self.points)


class TestTriangle:
    def setup_method(self):
        self.points = [(0.0, 0.0), (4.0, 0.0), (2.0, 4.0), (1.0, 1.0)]
        self.expected_hull = {(0.0, 0.0), (4.0, 0.0), (2.0, 4.0)}

    def test_graham_triangle(self):
        result = graham_scan(self.points)
        assert len(result) == 3
        assert set(result) == self.expected_hull

    def test_jarvis_triangle(self):
        result = jarvis_march(self.points)
        assert len(result) == 3
        assert set(result) == self.expected_hull

    def test_quickhull_triangle(self):
        result = quickhull(self.points)
        assert len(result) == 3
        assert set(result) == self.expected_hull

