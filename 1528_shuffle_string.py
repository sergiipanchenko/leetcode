import unittest


def restore_string(s, indices):
    s_list_result = ['']*len(s)

    for i, each in enumerate(s):
        s_list_result[indices[i]] = each
    # print(s_list_result)

    return ''.join(s_list_result)


class Tests(unittest.TestCase):
    def test_restore_string(self):
        self.assertEqual(restore_string('abc', [0, 1, 2]), 'abc')
        self.assertEqual(restore_string('art', [1, 0, 2]), 'rat')
        self.assertEqual(restore_string('aiohn', [3, 1, 4, 2, 0]), 'nihao')
        self.assertEqual(restore_string('aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5]), 'arigatou')
        self.assertEqual(restore_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]), 'leetcode')


if __name__ == '__main__':
    unittest.main()
