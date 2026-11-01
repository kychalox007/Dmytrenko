import csv

import pytest

from lab_02.phonebook import (
    add_student,
    delete_student,
    load_students,
    main,
    save_students,
    update_student,
)


def test_load_students_sorts_csv(tmp_path):
    csv_path = tmp_path / "students.csv"
    csv_path.write_text(
        "name,phone,email,group\nZak,333,zak@example.com,Group 1\n"
        "Bob,111,bob@example.com,Group 1\n",
        encoding="utf-8",
    )

    students = load_students(csv_path)

    assert [student["name"] for student in students] == ["Bob", "Zak"]


def test_load_students_accepts_two_column_csv(tmp_path):
    csv_path = tmp_path / "students.csv"
    csv_path.write_text("Name,Phone\nBob,111\n", encoding="utf-8")

    assert load_students(csv_path) == [
        {"name": "Bob", "phone": "111", "email": "", "group": ""}
    ]


def test_load_students_requires_name_and_phone(tmp_path):
    csv_path = tmp_path / "students.csv"
    csv_path.write_text("email,group\na@example.com,Group 1\n", encoding="utf-8")

    with pytest.raises(ValueError):
        load_students(csv_path)


def test_save_students_writes_csv(tmp_path):
    csv_path = tmp_path / "students.csv"
    students = [
        {"name": "Zak", "phone": "333", "email": "zak@example.com", "group": "Group 1"},
        {"name": "Bob", "phone": "111", "email": "bob@example.com", "group": "Group 1"},
    ]

    save_students(csv_path, students)

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert [row["name"] for row in rows] == ["Bob", "Zak"]


def test_add_student_keeps_list_sorted():
    students = [
        {"name": "Bob", "phone": "111", "email": "bob@example.com", "group": "Group 1"}
    ]
    new_student = {
        "name": "Anna",
        "phone": "222",
        "email": "anna@example.com",
        "group": "Group 1",
    }

    assert add_student(students, new_student)
    assert [student["name"] for student in students] == ["Anna", "Bob"]
    assert not add_student(students, new_student)


def test_update_student_keeps_list_sorted():
    students = [
        {"name": "Bob", "phone": "111", "email": "bob@example.com", "group": "Group 1"},
        {"name": "Zak", "phone": "333", "email": "zak@example.com", "group": "Group 1"},
    ]
    updated_student = {
        "name": "Anna",
        "phone": "222",
        "email": "anna@example.com",
        "group": "Group 1",
    }

    assert update_student(students, "Bob", updated_student)
    assert [student["name"] for student in students] == ["Anna", "Zak"]


def test_update_student_rejects_duplicate_name():
    students = [
        {"name": "Bob", "phone": "111", "email": "bob@example.com", "group": "Group 1"},
        {"name": "Zak", "phone": "333", "email": "zak@example.com", "group": "Group 1"},
    ]
    updated_student = {
        "name": "Zak",
        "phone": "222",
        "email": "new@example.com",
        "group": "Group 1",
    }

    assert not update_student(students, "Bob", updated_student)
    assert [student["name"] for student in students] == ["Bob", "Zak"]


def test_delete_student_removes_record():
    students = [
        {"name": "Bob", "phone": "111", "email": "bob@example.com", "group": "Group 1"}
    ]

    assert delete_student(students, "bob")
    assert students == []
    assert not delete_student(students, "Bob")


def test_main_saves_changes_before_exit(tmp_path, monkeypatch):
    csv_path = tmp_path / "students.csv"
    save_students(csv_path, [])
    values = iter(["c", "Anna", "111", "anna@example.com", "Group 1", "x"])
    monkeypatch.setattr("builtins.input", lambda _: next(values))

    assert main([str(csv_path)]) == 0
    assert [student["name"] for student in load_students(csv_path)] == ["Anna"]
