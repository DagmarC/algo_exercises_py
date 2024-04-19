import unittest
from leetcode.lc_27_remove_element import Solution


class TestRemoveElement(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [3, 2, 2, 3]
        val = 3
        expected_output = 2
        self.assertEqual(solution.removeElement(nums, val), expected_output)

    def test_example_2(self):
        solution = Solution()
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_output = 5
        self.assertEqual(solution.removeElement(nums, val), expected_output)

    def test_example_3(self):
        solution = Solution()
        nums = [1]
        val = 1
        expected_output = 0
        self.assertEqual(solution.removeElement(nums, val), expected_output)
