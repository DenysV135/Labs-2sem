import unittest
from lab9 import kmp_search


class TestKMPSearch(unittest.TestCase):
    def test_single_match(self):
        haystack = "hello world"
        needle = "world"
        self.assertEqual(kmp_search(haystack, needle), [6])

    def test_multiple_matches(self):
        haystack = "abafuncaba"
        needle = "aba"
        self.assertEqual(kmp_search(haystack, needle), [0, 7])

    def test_no_match(self):
        haystack = "hello world"
        needle = "goodbye"
        self.assertEqual(kmp_search(haystack, needle), [])

    def test_overlapping_matches(self):
        haystack = "aaaaa"
        needle = "aa"
        self.assertEqual(kmp_search(haystack, needle), [0, 1, 2, 3])

    def test_empty_needle(self):
        haystack = "hello"
        needle = ""
        self.assertEqual(kmp_search(haystack, needle), [])

    def test_empty_haystack(self):
        haystack = ""
        needle = "hello"
        self.assertEqual(kmp_search(haystack, needle), [])


if __name__ == "__main__":
    unittest.main()