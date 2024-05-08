import unittest
from dp.can_construct import can_construct_dp


class TestCanConstruct(unittest.TestCase):
    def test_can_construct(self):
        self.assertTrue(can_construct_dp("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
        self.assertFalse(can_construct_dp("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
        self.assertTrue(can_construct_dp("", ["cat", "dog", "mouse"]))
        self.assertTrue(can_construct_dp("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
        self.assertFalse(can_construct_dp("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                                          ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))


if __name__ == '__main__':
    unittest.main()
