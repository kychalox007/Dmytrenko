"""Сортування словників за ім'ям та оцінкою за допомогою lambda."""


def demo():
    students = [{"name": "Zak", "grade": 75}, {"name": "Bob", "grade": 90},
                {"name": "Emma", "grade": 82}]
    print("За ім'ям:", sorted(students, key=lambda student: student["name"]))
    print("За оцінкою:", sorted(students, key=lambda student: student["grade"]))
    print("Початковий список:", students)


if __name__ == "__main__":
    demo()
