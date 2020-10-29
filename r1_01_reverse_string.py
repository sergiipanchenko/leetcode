import unittest


def reverse_string(s):
    lo = 0
    hi = len(s) - 1

    while lo < hi:
        s[lo], s[hi] = s[hi], s[lo]
        lo += 1
        hi -= 1

    return s


def reverse_string_r(s):
    def reverse(lo, hi):
        if lo < hi:
            s[hi], s[lo] = s[lo], s[hi]
            reverse(lo+1, hi-1)
    reverse(0, len(s)-1)


class Tests(unittest.TestCase):
    def test_restore_string(self):
        self.assertEqual(reverse_string_r(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(reverse_string_r(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])


if __name__ == '__main__':
    unittest.main()
