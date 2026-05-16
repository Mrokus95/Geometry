import pytest

from main import parse_point


class TestParsePoint:
    # --- Valid inputs ---
    def test_integers(self):
        assert parse_point("1 2") == (1.0, 2.0)

    def test_floats(self):
        assert parse_point("1.5 2.75") == (1.5, 2.75)

    def test_negative_numbers(self):
        assert parse_point("-3 -4.5") == (-3.0, -4.5)

    def test_negative_x_positive_y(self):
        assert parse_point("-1 5") == (-1.0, 5.0)

    def test_positive_x_negative_y(self):
        assert parse_point("7 -2.5") == (7.0, -2.5)

    def test_double_space_separator(self):
        assert parse_point("3  4") == (3.0, 4.0)

    def test_tab_separator(self):
        assert parse_point("3\t4") == (3.0, 4.0)

    def test_leading_trailing_spaces(self):
        assert parse_point("  2 3  ") == (2.0, 3.0)

    def test_zero_values(self):
        assert parse_point("0 0") == (0.0, 0.0)

    def test_rounding_to_two_decimals(self):
        assert parse_point("1.555 2.999") == (1.56, 3.0)

    def test_large_numbers(self):
        assert parse_point("1000000 -999999") == (1000000.0, -999999.0)

    def test_scientific_notation(self):
        assert parse_point("1e2 2e1") == (100.0, 20.0)

    # --- Invalid inputs ---
    def test_letters_only(self):
        with pytest.raises(ValueError):
            parse_point("abc def")

    def test_one_letter_one_number(self):
        with pytest.raises(ValueError):
            parse_point("a 3")

    def test_number_and_letter(self):
        with pytest.raises(ValueError):
            parse_point("3 b")

    def test_single_number(self):
        with pytest.raises(ValueError):
            parse_point("5")

    def test_three_numbers(self):
        with pytest.raises(ValueError):
            parse_point("1 2 3")

    def test_empty_string(self):
        with pytest.raises(ValueError):
            parse_point("")

    def test_only_spaces(self):
        with pytest.raises(ValueError):
            parse_point("   ")

    def test_comma_separator(self):
        with pytest.raises(ValueError):
            parse_point("1,2")

    def test_comma_with_space(self):
        with pytest.raises(ValueError):
            parse_point("1, 2")

    def test_semicolon_separator(self):
        with pytest.raises(ValueError):
            parse_point("1;2")

    def test_word_mixed_with_number(self):
        with pytest.raises(ValueError):
            parse_point("1abc 2")

    def test_special_characters(self):
        with pytest.raises(ValueError):
            parse_point("@ #")

    def test_minus_alone(self):
        with pytest.raises(ValueError):
            parse_point("- 3")

