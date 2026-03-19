from lab2 import calcut
import unittest

class test(unittest.TestCase):
    def test_alg(self):
        calcut(2,3,4)
        
    def test_alll(self):
        calcut(10,2,3)

    def test_sss(self):
        calcut(2, 1000000000, 999999999)

    def test_ggg(self):
        calcut(4, 1, 1)

if __name__ == "__main__":
    unittest.main()