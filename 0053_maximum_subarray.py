import unittest


def maxSubArray(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    max_sum = local_sum = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        if local_sum >= 0:
            local_sum += num
        else:
            local_sum = num

        if local_sum > max_sum:
            max_sum = local_sum

    return max_sum


class MaxSubArrayTests(unittest.TestCase):
    def test_max_subArray(self):
        self.assertEqual(maxSubArray([]), 0)
        self.assertEqual(maxSubArray([-1]), -1)
        self.assertEqual(maxSubArray([1, 2]), 3)
        self.assertEqual(maxSubArray([-2, -1]), -1)
        self.assertEqual(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()
    # print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
