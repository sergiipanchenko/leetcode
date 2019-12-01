import unittest

# Accepted      28ms   12.8MB
def word_break(s, wordDict):
    way_list = [0]*(len(s))

    for each in wordDict:
        if s.startswith(each):
            way_list[len(each) - 1] += 1

    for i in range(1, len(s)):
        reminder = s[i:]
        for each in wordDict:
            if way_list[i-1] and reminder.startswith(each):
                way_list[i+len(each)-1] += 1

    if way_list[-1]:
        return True

    return False


# Accepted      32ms    12.7MB
# def word_break_02(s, wordDict):
#     check_list = [s]
#     seen_list = set()
#
#     while check_list:
#         for word in wordDict:
#             check_word = check_list[0]
#
#             if check_word.startswith(word):
#                 remainder = check_word[len(word):]
#                 if remainder == '':
#                     return True
#                 if remainder not in seen_list:
#                     check_list.append(remainder)
#                     seen_list.add(remainder)
#         check_list.pop(0)
#
#     return False


# Wrong Answers:
# def word_break_01(s, wordDict):
#     word = ''
#     while s:
#         word += s[0]
#         if word in wordDict:
#             word = ''
#         s = s[1:]
#     return False if word else True


class WordBreakTests(unittest.TestCase):
    def test_word_break(self):
        # tests pass OK
        self.assertTrue(word_break('leetcode', ['leet', 'code']))
        self.assertTrue(word_break('applepenapple', ['apple', 'pen']))
        self.assertFalse(word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
        self.assertTrue(word_break('cars', ['car', 'ca', 'rs']))
        self.assertTrue(word_break('aaaaaaa', ['aaaa', 'aaa']))

        self.assertFalse(word_break('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
                                   ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))


if __name__ == '__main__':
    unittest.main()
