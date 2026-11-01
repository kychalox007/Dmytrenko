import csv

from .student import Student


class Utils:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_students(self):
        with open(self.file_name, "r", newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            headers = {
                header.strip().casefold()
                for header in reader.fieldnames or []
                if header is not None
            }

            if "name" not in headers or "phone" not in headers:
                raise ValueError("CSV-файл має містити поля name і phone")

            students = []
            for row in reader:
                values = {
                    key.strip().casefold(): (value or "").strip()
                    for key, value in row.items()
                    if key is not None
                }
                students.append(
                    Student(
                        name=values.get("name", ""),
                        phone=values.get("phone", ""),
                        email=values.get("email", ""),
                        group=values.get("group", ""),
                    )
                )

        return students

    def save_students(self, students):
        with open(self.file_name, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=("name", "phone", "email", "group"),
            )
            writer.writeheader()

            for student in sorted(students, key=lambda item: item.name.casefold()):
                writer.writerow(student.to_csv_row())
