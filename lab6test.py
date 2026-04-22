import unittest
from lab6 import min_beers

class TestBeerOptimizer(unittest.TestCase):

    def test_example_1(self):
        n, b = 2, 2
        preferences = "YN NY"
        self.assertEqual(min_beers(n, b, preferences), 2)

    def test_example_2(self):
        n, b = 6, 3
        preferences = "YNN YNY YNY NYY NYY NYN"
        self.assertEqual(min_beers(n, b, preferences), 2)

    def test_all_like_one(self):
        n, b = 3, 3
        preferences = "YNN YNY YNN"
        self.assertEqual(min_beers(n, b, preferences), 1)

if __name__ == '__main__':
    unittest.main()