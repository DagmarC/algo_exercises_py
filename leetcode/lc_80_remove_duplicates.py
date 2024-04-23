from typing import List


class Solution:
    def remove_duplicates2(self, nums: List[int]) -> int:
        w = 0
        for num in nums:
            if w < 2 or num > nums[w-2]:
                nums[w] = num
                w += 1
        return w
