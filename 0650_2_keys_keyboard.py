import unittest


# accepted	28ms 12.6MB
def min_steps(n):
    if n == 1:
        return 0

    for i in range(2, int(n+1)):
        if n % i == 0:
            return min_steps(n/i)+i


class Tests(unittest.TestCase):
    def test_min_steps(self):
        self.assertEqual(min_steps(3), 3)


if __name__ == '__main__':
    unittest.main()
