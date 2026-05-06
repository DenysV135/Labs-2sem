import unittest
import os
from lab7 import get_minimum_cable_length


class TestMSTSolver(unittest.TestCase):
    def setUp(self):
        self.valid_csv = "test_valid.csv"
        self.disconnected_csv = "test_disconnected.csv"

        with open(self.valid_csv, "w", encoding="utf-8") as f:
            f.write("K1, K2, 100\n")
            f.write("K2, K3, 200\n")
            f.write("K1, K3, 400\n")
            f.write("K3, K4, 50\n")

        with open(self.disconnected_csv, "w", encoding="utf-8") as f:
            f.write("K1, K2, 100\n")
            f.write("K3, K4, 200\n")

    def tearDown(self):
        if os.path.exists(self.valid_csv):
            os.remove(self.valid_csv)
        if os.path.exists(self.disconnected_csv):
            os.remove(self.disconnected_csv)

    def test_valid_network(self):
        result = get_minimum_cable_length(self.valid_csv)
        self.assertEqual(result, 350)

    def test_disconnected_network(self):
        result = get_minimum_cable_length(self.disconnected_csv)
        self.assertEqual(result, -1)

    def test_missing_file(self):
        result = get_minimum_cable_length("non_existent_file.csv")
        self.assertEqual(result, -1)

    def test_empty_graph(self):
        empty_csv = "empty.csv"
        with open(empty_csv, "w", encoding="utf-8") as f:
            pass
        result = get_minimum_cable_length(empty_csv)
        self.assertEqual(result, 0)
        os.remove(empty_csv)


if __name__ == "__main__":
    unittest.main()
