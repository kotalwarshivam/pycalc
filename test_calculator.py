import pytest

from calculator import add, subtract, multiply, divide, is_prime, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(2) is True


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-3)
