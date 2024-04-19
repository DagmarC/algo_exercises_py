from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of a specified value from a list of integers.

        Args:
            nums (List[int]): The list of integers.
            val (int): The value to be removed.

        Returns:
            int: The number of elements in the modified list after removing the specified value.

        Examples:
            >>> s = Solution()
            >>> s.removeElement([3, 2, 2, 3], 3)
            2
            >>> s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
            5
        """
        k = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
        return k+1
