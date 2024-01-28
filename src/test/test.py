import unittest

from src.main.main import *


class TestCalculatorFunctions(unittest.TestCase):
    def test_calculate_lcm(self):
        self.assertEqual(calculate_lcm([3, 5, 7]), 105)
        self.assertEqual(calculate_lcm([2, 4, 8]), 8)
        self.assertEqual(calculate_lcm([15, 25, 35]), 525)

    def test_calculate_hcf(self):
        self.assertEqual(calculate_hcf([12, 18, 24]), 6)
        self.assertEqual(calculate_hcf([16, 24, 32]), 8)
        self.assertEqual(calculate_hcf([20, 30, 40]), 10)

    def test_calculate_add(self):
        self.assertEqual(calculate_add([1, 2, 3]), 6)
        self.assertEqual(calculate_add([5, 10, 15]), 30)
        self.assertEqual(calculate_add([2, 4, 6, 8]), 20)

    def test_calculate_multiply(self):
        self.assertEqual(calculate_multiply([2, 3, 4]), 24)
        self.assertEqual(calculate_multiply([1, 5, 10]), 50)
        self.assertEqual(calculate_multiply([2, 2, 2, 2]), 16)

    def test_calculate_divide(self):
        self.assertEqual(calculate_divide([10, 2, 2]), 2.5)
        self.assertEqual(calculate_divide([25, 5, 1]), 5)
        self.assertIsNone(calculate_divide([10, 0, 2]))

    def test_calculate_subtract(self):
        self.assertEqual(calculate_subtract([10, 2, 3]), 5)
        self.assertEqual(calculate_subtract([20, 5, 3, 1]), 11)
        self.assertEqual(calculate_subtract([15, 3, 2]), 10)

    def test_calculate_mean(self):
        self.assertEqual(calculate_mean([2, 4, 6]), 4)
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_mean([10, 20, 30]), 20)

    def test_calculate_median(self):
        self.assertEqual(calculate_median([2, 4, 6]), 4)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_median([10, 20, 30]), 20)

    def test_calculate_quantile(self):
        self.assertEqual(calculate_quantile([1, 2, 3, 4], 0), 1)
        self.assertEqual(calculate_quantile([1, 2, 3, 4], 2), 3)
        self.assertEqual(calculate_quantile([10, 20, 30, 40], 1), 20)

    def test_calculate_max(self):
        self.assertEqual(calculate_max([5, 10, 3, 8]), 10)
        self.assertEqual(calculate_max([15, 20, 30]), 30)
        self.assertEqual(calculate_max([1, 2, 3, 4, 5]), 5)

    def test_calculate_upper_q_range(self):
        self.assertEqual(calculate_upper_q_range([1, 2, 3, 4, 5]), 2)
        self.assertEqual(calculate_upper_q_range([10, 15, 20, 30, 40]), 20)
        self.assertEqual(calculate_upper_q_range([2, 4, 6, 8]), 4)

    def test_calculate_lower_q_range(self):
        self.assertEqual(calculate_lower_q_range([1, 2, 3, 4, 5]), 1)
        self.assertEqual(calculate_lower_q_range([10, 15, 20, 30, 40]), 10)
        self.assertEqual(calculate_lower_q_range([2, 4, 6, 8]), 2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
    unittest.TextTestRunner().run(suite)
