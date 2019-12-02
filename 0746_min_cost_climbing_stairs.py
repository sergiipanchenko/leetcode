import unittest


def minCostClimbingStairs(cost):
    steps = [cost[0], cost[1]]
    for i in range(2, len(cost)):
        steps.append(cost[i]+min(steps[i-1], steps[i-2]))
    # print(steps)
    return min(steps[-2], steps[-1])


class MaxSubArrayTests(unittest.TestCase):
    def test_minCostClimbingStairs(self):
        self.assertEqual(minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)


if __name__ == '__main__':
    unittest.main()
