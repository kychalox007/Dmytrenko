from dataclasses import dataclass


@dataclass
class Student:
    name: str
    phone: str
    email: str = ""
    group: str = ""

    def __post_init__(self):
        self.name = self.name.strip()
        self.phone = self.phone.strip()
        self.email = self.email.strip()
        self.group = self.group.strip()

        if not self.name:
            raise ValueError("Ім'я не може бути порожнім")
        if not self.phone:
            raise ValueError("Телефон не може бути порожнім")

    def to_csv_row(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group,
        }
