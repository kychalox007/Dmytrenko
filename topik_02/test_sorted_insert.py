import unittest

from topik_02.sorted_insert import find_insertion_position


class InsertionPositionTests(unittest.TestCase):
    def test_insert_between_values(self):
        values = [1, 3, 5]
        index = find_insertion_position(values, 4)
        values.insert(index, 4)
        self.assertEqual(values, [1, 3, 4, 5])

    def test_insert_at_start(self):
        self.assertEqual(find_insertion_position([2, 3], 1), 0)

    def test_insert_at_end(self):
        self.assertEqual(find_insertion_position([1, 2], 3), 2)

    def test_empty_list(self):
        self.assertEqual(find_insertion_position([], 5), 0)

    def test_existing_value(self):
        self.assertEqual(find_insertion_position([1, 2, 2, 3], 2), 1)


if __name__ == "__main__":
    unittest.main()
