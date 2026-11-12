class Student:
    def __init__(self, name, age):
        if not str(name).strip() or not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Потрібні непорожнє ім'я та невід'ємний цілий вік")
        self.name = str(name).strip()
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age!r})"
