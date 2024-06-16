import pytest


def division(dividend, divisor):
    return dividend / divisor


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        result = division(1, 0)
