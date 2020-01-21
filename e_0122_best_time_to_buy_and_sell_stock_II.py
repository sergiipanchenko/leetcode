import unittest


# accepted 68ms 13.7MB faster than 18.97% of Python3
def maxProfit(prices):
    if len(prices) < 2:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit


class Tests(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(maxProfit([7, 6, 4, 3, 1]), 0)

        self.assertEqual(maxProfit([6, 13]), 7)
        self.assertEqual(maxProfit([7, 6]), 0)

        self.assertEqual(maxProfit([]), 0)



if __name__ == '__main__':
    unittest.main()
