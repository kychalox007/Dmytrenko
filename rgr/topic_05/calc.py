"""Запуск із кореня проєкту: python -m rgr.topic_05.calc."""
import math
from . import functions, operations


def run(input_fn=input, output=print, log=lambda text: None):
    actions = {"+": functions.add, "-": functions.subtract,
               "*": functions.multiply, "/": functions.divide}
    log("START")
    while True:
        try:
            operation = operations.read_operation(input_fn, log)
            if operation.upper() == "X":
                log("EXIT command")
                return
            if operation not in actions:
                log(f"ERROR unknown_operation={operation!r}")
                output("Невідома операція")
                continue
            a = operations.read_number("Перше число: ", input_fn, output, log)
            b = operations.read_number("Друге число: ", input_fn, output, log)
            try:
                result = actions[operation](a, b)
                if not math.isfinite(result):
                    raise ValueError("Результат виходить за допустимий діапазон")
                log(f"RESULT {a} {operation} {b} = {result}")
                output(f"Результат: {result:g}")
            except (ZeroDivisionError, ValueError, OverflowError) as error:
                log(f"ERROR {a} {operation} {b}: {error}")
                output(f"Помилка: {error}")
        except (EOFError, KeyboardInterrupt):
            log("EXIT interrupted")
            return


if __name__ == "__main__":
    run()
