
class Calculator:

    def __init__(self):
        self.history = []

    def _add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def get_history(self):
        return self.history

    def add(self, a, b):
        result = a + b
        self._add_to_history(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._add_to_history(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._add_to_history(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self._add_to_history(f"{a} / {b}", result)
        return result

    def power(self, base, exponent):
        result = base ** exponent
        self._add_to_history(f"{base} ^ {exponent}", result)
        return result

    def sqrt(self, number):
        if number < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        result = number ** 0.5
        self._add_to_history(f"√{number}", result)
        return result
