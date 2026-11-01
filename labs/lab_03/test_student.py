import pytest

from labs.lab_03.student import Student


def test_student_stores_all_fields():
    student = Student(" Anna ", " 111 ", "anna@example.com", "Group 1")

    assert student.name == "Anna"
    assert student.phone == "111"
    assert student.email == "anna@example.com"
    assert student.group == "Group 1"


def test_student_requires_name():
    with pytest.raises(ValueError):
        Student("", "111")


def test_student_requires_phone():
    with pytest.raises(ValueError):
        Student("Anna", "")
