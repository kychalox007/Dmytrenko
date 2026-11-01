import csv

import pytest

from lab_03.student import Student
from lab_03.student_list import StudentList
from lab_03.utils import Utils


def test_load_students_creates_sorted_student_objects(tmp_path):
    file_name = tmp_path / "students.csv"
    file_name.write_text(
        "name,phone,email,group\nZak,333,zak@example.com,Group 1\n"
        "Bob,111,bob@example.com,Group 1\n",
        encoding="utf-8",
    )

    students = StudentList(Utils(file_name).load_students())

    assert [student.name for student in students] == ["Bob", "Zak"]
    assert all(isinstance(student, Student) for student in students)


def test_load_students_accepts_two_column_csv(tmp_path):
    file_name = tmp_path / "students.csv"
    file_name.write_text("Name,Phone\nBob,111\n", encoding="utf-8")

    students = Utils(file_name).load_students()

    assert students == [Student("Bob", "111")]


def test_load_students_rejects_missing_required_fields(tmp_path):
    file_name = tmp_path / "students.csv"
    file_name.write_text("email,group\na@example.com,Group 1\n", encoding="utf-8")

    with pytest.raises(ValueError):
        Utils(file_name).load_students()


def test_save_students_writes_sorted_csv(tmp_path):
    file_name = tmp_path / "students.csv"
    students = StudentList([Student("Zak", "333"), Student("Bob", "111")])

    Utils(file_name).save_students(students)

    with file_name.open(newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert [row["name"] for row in rows] == ["Bob", "Zak"]
