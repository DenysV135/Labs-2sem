import unittest
from lab1 import identlims
class Test(unittest.TestCase):
    def test_basic_case(self):
        test_mas = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        expected = [7, 10, 11, 7, 12, 6, 7]
        identlims(test_mas)
        self.assertEqual(test_mas, expected)

    def test_already_sorted(self):
        test_mas = [1, 2, 3]
        result = identlims(test_mas)
        self.assertEqual(result, (-1, -1))

    def test_full_sort_needed(self):
        test_mas = [30, 17, 22, 1]
        expected = [30, 17, 22, 1]
        result = identlims(test_mas)
        self.assertEqual(result, expected)

    def test_one_elem_massive(self):
        test_mas = [5]
        result = identlims(test_mas)
        self.assertEqual(result, (-1, -1))

    def test_empty_array(self):
        arr = []
        self.assertEqual(identlims(arr), (-1, -1))

if __name__ == "__main__":
    unittest.main()
