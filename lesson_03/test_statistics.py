import unittest
from app.services.statistics import average, count_values, median, spread


class TestStatistics(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_median_odd(self):
        self.assertEqual(median([9, 1, 5]), 5)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            median([])

    def test_spread(self):
        self.assertEqual(spread([2, 9, 4]), 7)

    def test_count_values(self):
        self.assertEqual(count_values(["a", "b", "a"]), {"a": 2, "b": 1})


if __name__ == "__main__":
    unittest.main()
