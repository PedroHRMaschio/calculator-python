import pytest
from calculator import Calculator

class TestCalculator:
    
    # Test for addition
    def test_add(self):
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0

    # Test for subtraction
    def test_subtract(self):
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(3, 5) == -2
        assert Calculator.subtract(0, 0) == 0

    # Test for multiplication
    def test_multiply(self):
        assert Calculator.multiply(2, 3) == 6
        assert Calculator.multiply(-1, 1) == -1
        assert Calculator.multiply(0, 5) == 0

    # Test for division
    def test_divide(self):
        assert Calculator.divide(6, 3) == 2
        assert Calculator.divide(5, 2) == 2.5
        assert Calculator.divide(-4, 2) == -2

    # Test for division by zero (should raise exception)
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(5, 0)
