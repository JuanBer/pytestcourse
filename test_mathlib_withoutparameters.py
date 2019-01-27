import mathlib


def test_calc_square_1():
    result = mathlib.calc_square(5)
    assert result == 25


def test_calc_square_2():
    result = mathlib.calc_square(9)
    assert result == 81


def test_calc_square_3():
    result = mathlib.calc_square(6)
    assert result == 36
