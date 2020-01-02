import unittest


# Accepted	48 ms	12.7 MB
def find_numbers(nums):
    counter = 0

    for num in nums:
        if not len(str(num)) % 2:
            counter += 1

    return counter


class Tests(unittest.TestCase):
    def test_find_numbers(self):
        self.assertEqual(find_numbers([12, 345, 2, 6, 7896]), 2)
        self.assertEqual(find_numbers([555, 901, 482, 1771]), 1)
        self.assertEqual(find_numbers([0, 1, 2, 3, 4]), 0)


if __name__ == '__main__':
    unittest.main()
