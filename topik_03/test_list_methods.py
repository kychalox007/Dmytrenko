import unittest


class ListMethodTests(unittest.TestCase):
    def test_extend(self):
        values = [1, 2]
        values.extend([3, 4])
        self.assertEqual(values, [1, 2, 3, 4])

    def test_append(self):
        values = [1]
        values.append(2)
        self.assertEqual(values, [1, 2])

    def test_insert(self):
        values = [1, 3]
        values.insert(1, 2)
        self.assertEqual(values, [1, 2, 3])

    def test_remove(self):
        values = [1, 2, 3]
        values.remove(2)
        self.assertEqual(values, [1, 3])

    def test_clear(self):
        values = [1, 2, 3]
        values.clear()
        self.assertEqual(values, [])

    def test_sort(self):
        values = [3, 1, 2]
        values.sort()
        self.assertEqual(values, [1, 2, 3])

    def test_reverse(self):
        values = [1, 2, 3]
        values.reverse()
        self.assertEqual(values, [3, 2, 1])

    def test_copy(self):
        values = [1, 2]
        copied = values.copy()
        copied.append(3)
        self.assertEqual(values, [1, 2])
        self.assertEqual(copied, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
