"""Тести для функції обчислення дискримінанта."""

import unittest

from main import discriminant


class DiscriminantTests(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(discriminant(1, -3, 2), 1)

    def test_zero_discriminant(self):
        self.assertEqual(discriminant(1, 2, 1), 0)

    def test_negative_discriminant(self):
        self.assertEqual(discriminant(1, 0, 1), -4)


if __name__ == "__main__":
    unittest.main()
