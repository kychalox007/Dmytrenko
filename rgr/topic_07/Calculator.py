import math
from rgr.topic_05 import functions


class Calculator:
    def __init__(self):
        self.history = []
        self.operations = {"+": functions.add, "-": functions.subtract,
                           "*": functions.multiply, "/": functions.divide}

    def calculate(self, a, operation, b):
        if operation not in self.operations:
            raise ValueError("Невідома операція")
        if not math.isfinite(a) or not math.isfinite(b):
            raise ValueError("Потрібні скінченні числа")
        result = self.operations[operation](a, b)
        if not math.isfinite(result):
            raise ValueError("Результат виходить за допустимий діапазон")
        self.history.append((a, operation, b, result))
        return result

    def __str__(self):
        return f"Калькулятор: успішних операцій {len(self.history)}"
