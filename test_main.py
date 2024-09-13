import main
import pytest

@pytest.mark.parametrize("a, b, expresult", [(10, 2, 5),
                                             (20, 10, 2),
                                             (30, -3, -10),
                                             (5, 2, 2.5)])
def test_divison_good(a, b, expresult):
    assert main.divison(a, b) == expresult

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert main.divison(10, 0)

def test_zero_division():
    with pytest.raises(TypeError):
        assert main.divison("Kholin", 0)