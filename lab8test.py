import unittest
from src.electricians import calculate_max_wire_length

class TestElectricians(unittest.TestCase):
    def test_example_1(self):
        self.assertAlmostEqual(calculate_max_wire_length(2, [3, 3, 3]), 5.65, places=2)

    def test_example_2(self):
        self.assertAlmostEqual(calculate_max_wire_length(100, [1, 1, 1, 1]), 300.00, places=2)

    def test_example_3(self):
        self.assertAlmostEqual(calculate_max_wire_length(4, [100, 2, 100, 2, 100]), 396.32, places=2)

if __name__ == "__main__":
    unittest.main()
