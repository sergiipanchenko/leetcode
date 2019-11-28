import unittest


def word_break(s, word_dict):
    word = ''

    while s:
        word += s[0]
        if word in word_dict:
            # print(word)
            word = ''
        s = s[1:]

    return False if word else True


class WordBreakTests(unittest.TestCase):
    def test_word_break(self):
        # tests pass OK
        self.assertTrue(word_break('leetcode', ['leet', 'code']))
        self.assertTrue(word_break('applepenapple', ['apple', 'pen']))
        self.assertFalse(word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
        self.assertTrue(word_break('cars', ['car', 'ca', 'rs']))
        # TODO failures
        self.assertTrue(word_break('aaaaaaa', ['aaaa', 'aaa']))


if __name__ == '__main__':
    unittest.main()
