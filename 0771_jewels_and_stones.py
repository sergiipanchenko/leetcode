import unittest

# Accepted	28 ms	12.8 MB
def numJewelsInStones(J, S):
    counter = 0
    jewelry_dict = {each:True for each in J}

    for stone in S:
        if stone in jewelry_dict:
            counter += 1

    return counter

# Accepted	32 ms	12.8 MB
# def numJewelsInStones(J, S):
#     jewels_count = 0
#     for char in J:
#         jewels_count += S.count(char)
#     return jewels_count


class RobTests(unittest.TestCase):
    def test_numJewelsInStones(self):
        self.assertEqual(numJewelsInStones('aA', 'aAAbbbb'), 3)
        self.assertEqual(numJewelsInStones('z', 'ZZ'), 0)
        self.assertEqual(numJewelsInStones('ABCDEF', 'aAbBBcCdDeFFgGh'), 7)


if __name__ == '__main__':
    unittest.main()
