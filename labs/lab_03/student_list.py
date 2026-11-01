from .student import Student


class StudentList:
    def __init__(self, students=None):
        self.students = sorted(list(students or []), key=self._sort_key)

    @staticmethod
    def _sort_key(student):
        return student.name.casefold()

    def _find_index(self, name):
        name = name.strip().casefold()

        for position, student in enumerate(self.students):
            if student.name.casefold() == name:
                return position

        return -1

    def find(self, name):
        position = self._find_index(name)
        if position == -1:
            return None
        return self.students[position]

    def add(self, student):
        if self._find_index(student.name) != -1:
            return False

        position = 0
        while position < len(self.students) and self._sort_key(self.students[position]) < self._sort_key(student):
            position += 1

        self.students.insert(position, student)
        return True

    def update(self, name, updated_student):
        position = self._find_index(name)
        if position == -1:
            return False

        duplicate_position = self._find_index(updated_student.name)
        if duplicate_position != -1 and duplicate_position != position:
            return False

        del self.students[position]
        self.add(updated_student)
        return True

    def delete(self, name):
        position = self._find_index(name)
        if position == -1:
            return False

        del self.students[position]
        return True

    def __iter__(self):
        return iter(self.students)

    def __len__(self):
        return len(self.students)
