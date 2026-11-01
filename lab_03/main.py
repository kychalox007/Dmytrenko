import csv
import sys

from .student import Student
from .student_list import StudentList
from .utils import Utils


def read_student():
    values = [
        input("Ім'я та прізвище: ").strip(),
        input("Телефон: ").strip(),
        input("Електронна пошта: ").strip(),
        input("Група: ").strip(),
    ]

    if not all(values):
        print("Усі поля мають бути заповнені")
        return None

    return Student(*values)


def print_students(students):
    if not len(students):
        print("Довідник порожній")
        return

    for student in students:
        print(
            f"{student.name} | {student.phone} | "
            f"{student.email} | {student.group}"
        )


def main(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]

    if len(arguments) != 1:
        print("Вкажіть ім'я CSV-файлу")
        return 1

    storage = Utils(arguments[0])

    try:
        students = StudentList(storage.load_students())
    except (OSError, csv.Error, ValueError) as error:
        print(f"Не вдалося завантажити довідник: {error}")
        return 1

    while True:
        action = input(
            "Дія [C — додати, U — змінити, D — видалити, P — показати, X — вихід]: "
        ).strip().casefold()

        match action:
            case "c":
                student = read_student()
                if student is not None:
                    if students.add(student):
                        print("Запис додано")
                    else:
                        print("Студент із таким ім'ям уже є")
            case "u":
                name = input("Ім'я студента для зміни: ").strip()
                if students.find(name) is None:
                    print("Студента не знайдено")
                    continue

                student = read_student()
                if student is not None:
                    if students.update(name, student):
                        print("Запис змінено")
                    else:
                        print("Запис не змінено")
            case "d":
                name = input("Ім'я студента для видалення: ").strip()
                if students.delete(name):
                    print("Запис видалено")
                else:
                    print("Студента не знайдено")
            case "p":
                print_students(students)
            case "x":
                try:
                    storage.save_students(students)
                except (OSError, csv.Error, ValueError) as error:
                    print(f"Не вдалося зберегти довідник: {error}")
                    return 1

                print("Довідник збережено")
                return 0
            case _:
                print("Невідома дія")


if __name__ == "__main__":
    raise SystemExit(main())
