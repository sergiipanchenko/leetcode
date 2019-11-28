def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]


def twoSum2(nums, target):
    nums_dict = {}

    for index, num in enumerate(nums):
        remaining = target - num

        if remaining in nums_dict:
            return [nums_dict[remaining], index]

        nums_dict[num] = index

    return []


def twoSum3(nums, target):
    check = {}

    for i, num in enumerate(nums):
        remainder = target - num

        if remainder in check:
            return [check[remainder], i]

        check[num] = i


print('result: ', twoSum2([3, 3], 6)) 	# [0,1]

# and nums_dict.get(delta) != index