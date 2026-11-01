import csv
import sys

STUDENT_FIELDS = ("name", "phone", "email", "group")


def load_students(file_name):
    with open(file_name, "r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        headers = {
            header.strip().casefold(): header
            for header in reader.fieldnames or []
            if header is not None
        }

        if "name" not in headers or "phone" not in headers:
            raise ValueError("CSV-файл має містити поля name і phone")

        students = []
        for row in reader:
            values = {
                key.strip().casefold(): value
                for key, value in row.items()
                if key is not None
            }
            student = {
                field: (values.get(field) or "").strip()
                for field in STUDENT_FIELDS
            }

            if not student["name"] or not student["phone"]:
                raise ValueError("У записі мають бути вказані ім'я та телефон")

            students.append(student)

    return sorted(students, key=lambda student: student["name"].casefold())


def save_students(file_name, students):
    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=STUDENT_FIELDS)
        writer.writeheader()

        for student in sorted(students, key=lambda item: item["name"].casefold()):
            writer.writerow({field: student.get(field, "") for field in STUDENT_FIELDS})


def find_student(students, name):
    name = name.strip().casefold()

    for position, student in enumerate(students):
        if student["name"].casefold() == name:
            return position

    return -1


def insert_student(students, student):
    position = 0
    name = student["name"].casefold()

    while position < len(students) and students[position]["name"].casefold() < name:
        position += 1

    students.insert(position, student)


def add_student(students, student):
    if find_student(students, student["name"]) != -1:
        return False

    insert_student(students, student)
    return True


def update_student(students, old_name, new_student):
    position = find_student(students, old_name)
    if position == -1:
        return False

    duplicate_position = find_student(students, new_student["name"])
    if duplicate_position != -1 and duplicate_position != position:
        return False

    del students[position]
    insert_student(students, new_student)
    return True


def delete_student(students, name):
    position = find_student(students, name)
    if position == -1:
        return False

    del students[position]
    return True


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

    return dict(zip(STUDENT_FIELDS, values))


def print_students(students):
    if not students:
        print("Довідник порожній")
        return

    for student in students:
        print(
            f"{student['name']} | {student['phone']} | "
            f"{student['email']} | {student['group']}"
        )


def main(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]

    if len(arguments) != 1:
        print("Вкажіть ім'я CSV-файлу")
        return 1

    file_name = arguments[0]

    try:
        students = load_students(file_name)
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
                    if add_student(students, student):
                        print("Запис додано")
                    else:
                        print("Студент із таким ім'ям уже є")
            case "u":
                old_name = input("Ім'я студента для зміни: ").strip()
                if find_student(students, old_name) == -1:
                    print("Студента не знайдено")
                    continue

                student = read_student()
                if student is not None:
                    if update_student(students, old_name, student):
                        print("Запис змінено")
                    else:
                        print("Запис не змінено")
            case "d":
                name = input("Ім'я студента для видалення: ").strip()
                if delete_student(students, name):
                    print("Запис видалено")
                else:
                    print("Студента не знайдено")
            case "p":
                print_students(students)
            case "x":
                try:
                    save_students(file_name, students)
                except (OSError, csv.Error, ValueError) as error:
                    print(f"Не вдалося зберегти довідник: {error}")
                    return 1

                print("Довідник збережено")
                return 0
            case _:
                print("Невідома дія")


if __name__ == "__main__":
    raise SystemExit(main())
