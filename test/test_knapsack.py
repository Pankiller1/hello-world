import unittest
from src import DP

class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = DP.knapsack(values, weights, capacity)
        self.assertEqual(result, 220)

if __name__ == '__main__':
    unittest.main()
