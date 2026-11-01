def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ділення на нуль"


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


def request_data():
    try:
        first = input().strip()
        if first.lower() == "exit":
            return "exit"
        a = float(first)

        operation = input().strip()
        if operation.lower() == "exit":
            return "exit"
        if operation not in ("+", "-", "*", "/"):
            raise ValueError

        second = input().strip()
        if second.lower() == "exit":
            return "exit"
        b = float(second)

        return a, operation, b
    except ValueError:
        print("Помилка введення")
        return None


def main():
    while True:
        data = request_data()
        if data == "exit":
            break
        if data is None:
            continue

        a, operation, b = data
        print(calculate(a, operation, b))


if __name__ == "__main__":
    main()
