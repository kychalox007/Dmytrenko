import argparse
from .Student import Student
from .Calculator import Calculator
from .ConsoleUI import ConsoleUI


def demo():
    students = [Student("Zak", 20), Student("Bob", 19), Student("Emma", 18)]
    print("За ім'ям:")
    for student in sorted(students, key=lambda item: item.name):
        print(student)
    print("За віком:")
    for student in sorted(students, key=lambda item: item.age):
        print(student)
    print("__repr__:", repr(students[0]))
    calculator = Calculator()
    print("8 + 2 =", calculator.calculate(8, "+", 2))
    print("8 / 2 =", calculator.calculate(8, "/", 2))
    print(calculator)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    if parser.parse_args().demo:
        demo()
    else:
        ConsoleUI(Calculator()).run()
