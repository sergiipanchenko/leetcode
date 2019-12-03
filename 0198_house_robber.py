import unittest


def rob(nums):
    odd_max = even_max = 0

    for i in range(len(nums)):
        if i % 2:
            odd_max = max(even_max, odd_max + nums[i])
        else:
            even_max = max(odd_max, even_max + nums[i])

    return max(odd_max, even_max)


class RobTests(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(rob([3, 10, 3, 1, 2]), 12)
        self.assertEqual(rob([100, 0, 100, 100, 100, 0, 0, 100]), 400)


if __name__ == '__main__':
    unittest.main()
