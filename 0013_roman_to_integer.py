import unittest


# Accepted 44ms 12.7MB
def roman_to_integer(s):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = romans[s[0]]

    for i in range(1, len(s)):
        result += romans[s[i]]
        if romans[s[i]] > romans[s[i-1]]:
            result -= 2 * romans[s[i-1]]

    return result


class Tests(unittest.TestCase):
    def test_roman_to_integer(self):
        self.assertEqual(roman_to_integer('III'), 3)
        self.assertEqual(roman_to_integer('LVIII'), 58)
        self.assertEqual(roman_to_integer('MMXX'), 2020)

        self.assertEqual(roman_to_integer('IV'), 4)
        self.assertEqual(roman_to_integer('IX'), 9)
        self.assertEqual(roman_to_integer('XLIX'), 49)

        self.assertEqual(roman_to_integer('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
