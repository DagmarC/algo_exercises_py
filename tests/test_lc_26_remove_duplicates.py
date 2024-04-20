import unittest
from leetcode.lc_26_remove_duplicates import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        solution = Solution()
        # Test case 1: Array with duplicates
        nums = [1, 1, 2, 2, 3, 4, 5, 5]
        expected_result = [1, 2, 3, 4, 5]
        solution.remove_duplicates(nums)
        self.assertEqual(nums, expected_result)

    def test_example_2(self):
        solution = Solution()
        # Test case 2: Array without duplicates
        nums = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        solution.remove_duplicates(nums)
        self.assertEqual(nums, expected_result)

    def test_example_3(self):
        solution = Solution()
        # Test case 3: Empty array
        nums = []
        expected_result = []
        solution.remove_duplicates(nums)
        self.assertEqual(nums, expected_result)
