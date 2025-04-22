import math_functions

def test_exponent():
    assert math_functions.exponent(2, 3) == 8
    assert math_functions.exponent(5, 0) == 1

def test_logarithm():
    from math_functions import logarithm
    # 基本测试
    assert abs(logarithm(8, 2) - 3) < 1e-6
    # 异常测试
    import pytest
    with pytest.raises(ValueError):
        logarithm(-5, 2)
