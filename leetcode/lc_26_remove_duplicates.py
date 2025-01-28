from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_pointer = 1
        for read_pointer in range(1, len(nums)):
            if nums[read_pointer] != nums[read_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

        return write_pointer
    