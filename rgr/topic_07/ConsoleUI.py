from rgr.topic_05.operations import read_number


class ConsoleUI:
    def __init__(self, calculator):
        self.calculator = calculator

    def run(self):
        while True:
            try:
                operation = input("Операція + - * / або X: ").strip()
                if operation.upper() == "X":
                    print(self.calculator)
                    return
                if operation not in self.calculator.operations:
                    print("Невідома операція")
                    continue
                a = read_number("Перше число: ")
                b = read_number("Друге число: ")
                try:
                    print("Результат:", self.calculator.calculate(a, operation, b))
                except (ValueError, ZeroDivisionError, OverflowError) as error:
                    print("Помилка:", error)
            except (EOFError, KeyboardInterrupt):
                return
