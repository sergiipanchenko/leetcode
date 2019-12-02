import unittest


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = seen = 0

    while seen < len(nums):
        num = nums[i]

        if num == 0:
            nums.pop(i)
            nums.insert(0, 0)
            i += 1
        elif num == 2:
            nums.pop(i)
            nums.append(2)
        else:
            i += 1

        seen += 1

    return nums


class MaxSubArrayTests(unittest.TestCase):
    def test_max_subArray(self):
        self.assertEqual(sortColors([1, 2, 0]), [0, 1, 2])
        self.assertEqual(sortColors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])


if __name__ == '__main__':
    unittest.main()
