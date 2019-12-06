import unittest


# Accepted	116 ms	12.8 MB
def firstUniqChar(s):
    chars_dict = {}

    for char in s:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    for char in s:
        if chars_dict[char] == 1:
            return s.index(char)

    return -1


# Accepted	84 ms	12.7 MB
# def firstUniqChar(s):
#     seen = set()
#     for char in s:
#         if char not in seen and s.count(char) == 1:
#             return s.index(char)
#         else:
#             seen.add(char)
#
#     return -1


class FirstUniqCharTests(unittest.TestCase):
    def test_firstUniqChar(self):
        self.assertEqual(firstUniqChar('leetcode'), 0)
        self.assertEqual(firstUniqChar('loveleetcode'), 2)


if __name__ == '__main__':
    unittest.main()
