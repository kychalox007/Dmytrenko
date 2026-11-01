STUDENT_FIELDS = ("name", "phone", "email", "group")
students = []


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


def find_student(name):
    name = name.casefold()

    for position, student in enumerate(students):
        if student["name"].casefold() == name:
            return position

    return -1


def insert_student(student):
    position = 0
    name = student["name"].casefold()

    while position < len(students) and students[position]["name"].casefold() < name:
        position += 1

    students.insert(position, student)


def print_all_students():
    if not students:
        print("Довідник порожній")
        return

    for student in students:
        print(
            f"{student['name']} | {student['phone']} | "
            f"{student['email']} | {student['group']}"
        )


def add_student():
    student = read_student()
    if student is None:
        return

    if find_student(student["name"]) != -1:
        print("Студент із таким ім'ям уже є")
        return

    insert_student(student)
    print("Запис додано")


def update_student():
    name = input("Ім'я студента для зміни: ").strip()
    position = find_student(name)

    if position == -1:
        print("Студента не знайдено")
        return

    student = read_student()
    if student is None:
        return

    duplicate_position = find_student(student["name"])
    if duplicate_position != -1 and duplicate_position != position:
        print("Студент із таким ім'ям уже є")
        return

    del students[position]
    insert_student(student)
    print("Запис змінено")


def delete_student():
    name = input("Ім'я студента для видалення: ").strip()
    position = find_student(name)

    if position == -1:
        print("Студента не знайдено")
        return

    del students[position]
    print("Запис видалено")


def main():
    while True:
        action = input("Дія [C — додати, U — змінити, D — видалити, P — показати, X — вихід]: ").strip().casefold()

        match action:
            case "c":
                add_student()
            case "u":
                update_student()
            case "d":
                delete_student()
            case "p":
                print_all_students()
            case "x":
                break
            case _:
                print("Невідома дія")


if __name__ == "__main__":
    main()
