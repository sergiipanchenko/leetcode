import unittest


# accepted 68ms 13.9MB faster than 31.68% of Python3
def maxProfit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for current_price in prices:
        guess_profit = current_price - min_price
        max_profit = max(max_profit, guess_profit)
        min_price = min(min_price, current_price)

    return max_profit


class Tests(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(maxProfit([6, 1, 3, 2, 4, 7]), 6)
        self.assertEqual(maxProfit([7, 6, 4, 3, 1]), 0)

        self.assertEqual(maxProfit([6, 13]), 7)
        self.assertEqual(maxProfit([7, 6]), 0)

        self.assertEqual(maxProfit([]), 0)



if __name__ == '__main__':
    unittest.main()
