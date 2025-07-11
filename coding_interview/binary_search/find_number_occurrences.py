# Given an array of integers sorted in non-decreasing order, return the first and last indexes of a target number. If the target is not found, return [-1, -1] .
from typing import List

# O(n) in the worst case, because I will linearly find right and left boundaries - nums = 4, 4, 4, 4, t=4 will go throughout the whoole array
def first_and_last_occurrences_of_a_number_lin(nums: List[int], target: int) -> List[int]:
    # Default values, if target number is not found
    left_boundary, right_boundary = -1, -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            left_boundary, right_boundary = mid, mid
           
            # Explore to the right
            for i in range(mid, len(nums)):
                if nums[i] != target:
                    break  # no more target values to the right of the mid
                right_boundary = i
            # Explore to the left
            for i in range(mid, -1, -1):
                if nums[i] != target:
                    break  # no more target values to the right of the mid
                left_boundary = i

        if target < nums[mid]:
            # Go to the mid left section
            right = mid - 1
        else:
            # Go the the mid right section
            left = mid + 1
        
    return [left_boundary, right_boundary]


def first_and_last_occurrences_of_a_number_rec(nums: List[int], target: int) -> List[int]:
    # Default values, if target number is not found
    left, right = 0, len(nums) - 1

    def number_occurrence_indices(left: int, right: int, left_target_index: int, right_target_index: int) -> (int, int):
        if left > right:
            return left_target_index, right_target_index
        
        mid = (left + right) // 2
        
        # Target found
        if nums[mid] == target:
            left_target_index = min(left_target_index, mid) if left_target_index != -1 else mid
            right_target_index = max(right_target_index, mid)
            
            # There is a possibility that target number can be located more on the left side
            if left_target_index > left:
                left_target_index, right_target_index = number_occurrence_indices(left, right=mid-1, 
                                                left_target_index=left_target_index, right_target_index=right_target_index)
            
            # There is a possibility that target number can be located more on the left side
            if right_target_index < right:
                left_target_index, right_target_index = number_occurrence_indices(left=mid+1, right=right, 
                                        left_target_index=left_target_index, right_target_index=right_target_index)
        
        # Target not found yet
        if target < nums[mid]:
            left_target_index, right_target_index = number_occurrence_indices(left, right=mid-1, 
                                                                            left_target_index=left_target_index, right_target_index=right_target_index)
        else:    
            left_target_index, right_target_index = number_occurrence_indices(left=mid+1, right=right, 
                                left_target_index=left_target_index, right_target_index=right_target_index)
        
        return left_target_index, right_target_index
        
            
    result = number_occurrence_indices(left, right, -1, -1)
    return list(result)


def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> List[int]:
   
   lower_bound = lower_bound_number(nums, target)
   upper_bound = upper_bound_number(nums, target)
   
   return [lower_bound, upper_bound]


def lower_bound_number(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid
        
    return left if nums and nums[left] == target else -1


def upper_bound_number(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2 + 1  # bias the midpoint to the right
        
        if nums[mid] < target:
            left = mid + 1
            
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid
        
    return right if nums and nums[right] == target else -1


if __name__ == "__main__":
    nums = [1,2,3,4,4,4,4,4,7,8,9,10,11]
    print(first_and_last_occurrences_of_a_number(nums=nums, target=4))