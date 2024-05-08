import unittest
from dp.count_construct import count_construct


class TestCountConstruct(unittest.TestCase):
    def test_count_construct(self):
        self.assertEqual(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 1)
        self.assertEqual(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]), 0)
        self.assertEqual(count_construct("", ["cat", "dog", "mouse"]), 1)
        # self.assertEqual(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]), 4)
        # self.assertEqual(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        #                                  ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]), 0)
        self.assertEqual(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]), 2)


if __name__ == '__main__':
    unittest.main()
