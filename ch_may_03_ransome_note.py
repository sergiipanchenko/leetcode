import unittest


def ransom_note(ransomNote, magazine):
    for l in ransomNote:
        if l not in magazine:
            return False
        else:
            magazine = magazine.replace(l, '', 1)
    return True


class Tests(unittest.TestCase):
    def test_ransom_note(self):
        self.assertEqual(ransom_note('a', 'b'), False)
        self.assertEqual(ransom_note('aa', 'ab'), False)
        self.assertEqual(ransom_note('aa', 'aab'), True)


if __name__ == '__main__':
    unittest.main()
