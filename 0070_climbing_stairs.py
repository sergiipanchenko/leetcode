import unittest


def climbStairs(n):
    stairs = []
    stairs.append(1)
    stairs.append(1)

    for i in range(2, n+1):
        stairs.append(stairs[i-1]+stairs[i-2])

    return stairs[n]


class ClimbStairsTests(unittest.TestCase):
    def test_climb_stairs(self):
        # tests pass OK
        self.assertEqual(climbStairs(3), 3)
        self.assertEqual(climbStairs(9), 55)
        self.assertEqual(climbStairs(19), 6765)


if __name__ == '__main__':
    unittest.main()
