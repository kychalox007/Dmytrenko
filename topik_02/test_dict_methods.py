import unittest


class DictionaryMethodTests(unittest.TestCase):
    def test_update(self):
        values = {"a": 1}
        values.update({"b": 2})
        self.assertEqual(values, {"a": 1, "b": 2})

    def test_del(self):
        values = {"a": 1, "b": 2}
        del values["a"]
        self.assertEqual(values, {"b": 2})

    def test_clear(self):
        values = {"a": 1}
        values.clear()
        self.assertEqual(values, {})

    def test_keys(self):
        values = {"a": 1, "b": 2}
        self.assertEqual(set(values.keys()), {"a", "b"})

    def test_values(self):
        values = {"a": 1, "b": 2}
        self.assertEqual(list(values.values()), [1, 2])

    def test_items(self):
        values = {"a": 1, "b": 2}
        self.assertEqual(set(values.items()), {("a", 1), ("b", 2)})


if __name__ == "__main__":
    unittest.main()
