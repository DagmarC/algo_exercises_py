import unittest
from leetcode.lc_80_remove_duplicates import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates2(self):
        solution = Solution()
        # Test case 1: Array with duplicates
        nums = [1, 1, 1, 2, 2, 3]
        expected_result = 5
        got = solution.remove_duplicates2(nums)
        self.assertEqual(got, expected_result)

    def test_example_2(self):
        solution = Solution()
        # Test case 2: Array without duplicates
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_result = 7
        got = solution.remove_duplicates2(nums)
        print(nums)
        self.assertEqual(got, expected_result)
  
    def test_example_3(self):
        solution = Solution()
        # Test case 2: Array without duplicates
        nums = [1, 2, 3]
        expected_result = [1, 2, 3]
        solution.remove_duplicates2(nums)
        self.assertEqual(nums, expected_result)


