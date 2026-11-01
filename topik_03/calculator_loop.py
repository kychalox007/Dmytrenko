from topik_02.calculator_match import calculate


def main():
    while True:
        first = input().strip()
        if first.lower() == "exit":
            break

        operation = input().strip()
        if operation.lower() == "exit":
            break

        second = input().strip()
        if second.lower() == "exit":
            break

        try:
            print(calculate(float(first), operation, float(second)))
        except (ValueError, ZeroDivisionError) as error:
            print(error)


if __name__ == "__main__":
    main()
