from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        This function removes all occurrences of a specified value from a list
        of integers in-place and
        returns the new length of the list.
        
        :param nums: The `nums` parameter is a list of integers that may
        contain the value `val` that
        needs to be removed. The function `removeElement` takes in this list
        `nums` and the value `val`
        that needs to be removed from the list. The function then modifies the
        list in-place
        :type nums: List[int]
        :param val: The `val` parameter in the `removeElement` function
        represents the value that you
        want to remove from the list `nums`. The function will remove
        all occurrences of this value from
        the list and return the new length of the list after removal
        :type val: int
        :return: the new length of the array `nums` after removing all
        occurrences of the value `val`.
        """
        k = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
        return k+1
