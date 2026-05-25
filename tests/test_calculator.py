import pytest
from calculator import add, subtract, multiply, divide, calculate


def test_addition():
    assert add(1, 2) == 3
    assert add("1.5", "2.5") == 4.0


def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract("5", "3") == 2.0


def test_multiplication():
    assert multiply(2, 4) == 8
    assert multiply("2", 4.5) == 9.0


def test_division():
    assert divide(10, 5) == 2
    assert divide("9", "3") == 3.0


def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(1, 0)


def test_invalid_input():
    with pytest.raises(ValueError, match="a must be a number"):
        add("x", 2)

    with pytest.raises(ValueError, match="b must be a number"):
        multiply(1, None)


def test_unsupported_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculate("power", 2, 3)
