import unittest
from leetcode.lc_26_remove_duplicates import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates2(self):
        solution = Solution()
        # Test case 1: Array with duplicates
        nums = [1, 1, 1, 2, 2, 3]
        expected_result = 3
        got = solution.remove_duplicates(nums)
        self.assertEqual(got, expected_result)

    def test_example_2(self):
        solution = Solution()
        # Test case 2: Array without duplicates
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_result = 4
        got = solution.remove_duplicates(nums)
        self.assertEqual(got, expected_result)

