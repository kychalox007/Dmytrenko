from lab_03.main import main
from lab_03.utils import Utils


def test_main_saves_changes_before_exit(tmp_path, monkeypatch):
    file_name = tmp_path / "students.csv"
    Utils(file_name).save_students([])
    values = iter(["c", "Anna", "111", "anna@example.com", "Group 1", "x"])
    monkeypatch.setattr("builtins.input", lambda _: next(values))

    assert main([str(file_name)]) == 0
    assert [student.name for student in Utils(file_name).load_students()] == ["Anna"]
