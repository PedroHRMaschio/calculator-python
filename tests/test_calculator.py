import pytest
from calculator import Calculator

calculator = Calculator()
class Testcalculator:
    
    # Test for addition
    def test_add(self):
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    # Test for subtraction
    def test_subtract(self):
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(3, 5) == -2
        assert calculator.subtract(0, 0) == 0

    # Test for multiplication
    def test_multiply(self):
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(-1, 1) == -1
        assert calculator.multiply(0, 5) == 0

    # Test for division
    def test_divide(self):
        assert calculator.divide(6, 3) == 2
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(-4, 2) == -2

    # Test for division by zero (should raise exception)
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(5, 0)

    # Test for power
    def test_power(self):
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1

    # Test for sqrt
    def test_sqrt(self):
        assert calculator.sqrt(16) == 4
        assert calculator.sqrt(64) == 8

    # Test for sqrt of a negative number (should raise exception)
    def test_sqrt_negative_number(self):
        with pytest.raises(ValueError):
            calculator.sqrt(-4)