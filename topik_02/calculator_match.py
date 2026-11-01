def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль")
    return a / b


def calculate(a, operation, b):
    match operation:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)
        case _:
            raise ValueError("Невідома операція")


def main():
    a = float(input())
    operation = input().strip()
    b = float(input())

    try:
        print(calculate(a, operation, b))
    except (ValueError, ZeroDivisionError) as error:
        print(error)


if __name__ == "__main__":
    main()
