"""Тести для функцій з main.py та методів рядків Python."""

import unittest

from main import discriminant, reverse_string


class StringTests(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_strip(self):
        self.assertEqual("  Hello, World! \n".strip(), "Hello, World!")

    def test_capitalize(self):
        self.assertEqual("pYTHON ROCKS".capitalize(), "Python rocks")

    def test_title(self):
        self.assertEqual("hello world from python".title(), "Hello World From Python")

    def test_upper(self):
        self.assertEqual("Hello, world!".upper(), "HELLO, WORLD!")

    def test_lower(self):
        self.assertEqual("PyThOn 3.12".lower(), "python 3.12")


class DiscriminantTests(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(discriminant(1, -3, 2), 1)

    def test_zero_discriminant(self):
        self.assertEqual(discriminant(1, 2, 1), 0)

    def test_negative_discriminant(self):
        self.assertEqual(discriminant(1, 0, 1), -4)


if __name__ == "__main__":
    unittest.main()
