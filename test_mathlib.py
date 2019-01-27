import mathlib
import pytest

@pytest.mark.windows
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9

def test_calc_multiply():
    result = mathlib.calc_multipy(4,5)
    assert result == 20
@pytest.mark.linux
def test_dummy():
    assert True
