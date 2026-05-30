from lab2 import calcut
import unittest

class test(unittest.TestCase):
    def test_alg(self):
        self.assertEqual(calcut(2, 3, 4), 6)
        
    def test_alll(self):
        self.assertEqual(calcut(10, 2, 3), 9)

    def test_sss(self):
        self.assertEqual(calcut(2, 1000000000, 999999999), 1999999998)

    def test_ggg(self):
        self.assertEqual(calcut(4, 1, 1), 2)

if __name__ == "__main__":
    unittest.main()
