import unittest


# Accepted 24ms 12.7MB faster 82.88% less 100.00%
def sub_prod_sum(n):
    sum, prod = 0, 1

    for each in str(n):
        num = int(each)
        sum += num
        prod *= num

    return prod - sum


class Tests(unittest.TestCase):
    def test_sub_prod_sum(self):
        self.assertEqual(sub_prod_sum(234), 15)
        self.assertEqual(sub_prod_sum(4421), 21)


if __name__ == '__main__':
    unittest.main()
