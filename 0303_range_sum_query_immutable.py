# import unittest


# Time Limit Exceeded
# class NumArray:
#     def __init__(self, nums):
#         self.nums = nums
#
#     def sumRange(self, i: int, j: int) -> int:
#         sum = 0
#         for each in range(i, j+1):
#             sum += self.nums[each]
#         return sum

# Accepted	76 ms	16.3 MB
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sum = [0]
        for i in range(len(nums)):
            self.sum.append(self.sum[i]+nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1] - self.sum[i]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print('(0, 2)', obj.sumRange(0, 2))
print('(2, 5)', obj.sumRange(2, 5))
print('(0, 5)', obj.sumRange(0, 5))

# class NumArrayTests(unittest.TestCase):
#     def test_firstUniqChar(self):
#         self.assertEqual(obj.sumRange(0, 2), 1)
#         self.assertEqual(obj.sumRange(0, 2), 1)
#         self.assertEqual(obj.sumRange(0, 2), 1)
#
# if __name__ == '__main__':
#     unittest.main()
