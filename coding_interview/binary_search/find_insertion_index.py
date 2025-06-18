from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return 0
    
    left = 0
    right = len(nums) - 1
    
    # left <= right ensures all elements are considered.
    # When the target is not found, left ends up pointing to the index where 
    # the target should be inserted to keep the array sorted.
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # insertion point