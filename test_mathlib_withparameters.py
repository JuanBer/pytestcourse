import mathlib
import pytest


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (6, 36),
                             (2, 4),
                             (7, 49),
                             (8, 63)
                         ])
def test_calc_square_1(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output
