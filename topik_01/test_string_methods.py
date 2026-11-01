"""Топік 2: тести методів рядків Python."""

import unittest


class StringMethodTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
