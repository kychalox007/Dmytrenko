from labs.lab_03.student import Student
from labs.lab_03.student_list import StudentList


def test_add_keeps_students_sorted_and_rejects_duplicate():
    students = StudentList([Student("Bob", "111")])

    assert students.add(Student("Anna", "222"))
    assert [student.name for student in students] == ["Anna", "Bob"]
    assert not students.add(Student("bob", "333"))


def test_update_keeps_students_sorted():
    students = StudentList([Student("Bob", "111"), Student("Zak", "333")])

    assert students.update("Bob", Student("Anna", "222"))
    assert [student.name for student in students] == ["Anna", "Zak"]


def test_update_rejects_duplicate_name():
    students = StudentList([Student("Bob", "111"), Student("Zak", "333")])

    assert not students.update("Bob", Student("Zak", "222"))
    assert [student.name for student in students] == ["Bob", "Zak"]


def test_find_and_delete_are_case_insensitive():
    students = StudentList([Student("Bob", "111")])

    assert students.find("bob").phone == "111"
    assert students.delete("BOB")
    assert len(students) == 0
    assert not students.delete("Bob")
