import unittest

from topik_00.main import discriminant, reverse_string


class TopicOneTests(unittest.TestCase):
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

    def test_discriminant(self):
        self.assertEqual(discriminant(1, -3, 2), 1)


if __name__ == "__main__":
    unittest.main()
