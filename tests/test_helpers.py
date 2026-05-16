from utils.helpers import cross_product, squared_distance


class TestCrossProduct:
    def test_left_turn(self):
        assert cross_product((0, 0), (1, 0), (1, 1)) > 0

    def test_right_turn(self):
        assert cross_product((0, 0), (1, 0), (1, -1)) < 0

    def test_collinear(self):
        assert cross_product((0, 0), (1, 0), (2, 0)) == 0

    def test_identical_points(self):
        assert cross_product((1, 1), (1, 1), (1, 1)) == 0


class TestSquaredDistance:
    def test_standard(self):
        assert squared_distance((0, 0), (3, 4)) == 25

    def test_same_point(self):
        assert squared_distance((2, 3), (2, 3)) == 0

    def test_negative_coordinates(self):
        assert squared_distance((-1, -1), (2, 3)) == 25

