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
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
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
