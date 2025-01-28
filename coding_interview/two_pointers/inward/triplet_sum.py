from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    
    nums.sort()  # needs to be sorted before two pointers are used
    triplets: set[tuple[int, ...]] = set()
    
    for a in range(len(nums)-2):
        pairs = pair_sum_sorted(nums[a+1:], (-1)*nums[a])
        for p in pairs:
            triplet = tuple([nums[a]] + p)
            triplets.add(triplet)
            
    return [list(triplet) for triplet in triplets]


def pair_sum_sorted(nums: List[int], target: int) -> List[List[int]]:
    left, right = 0, len(nums) - 1
    results: List[List[int]] = []
    
    while left < right:
        tmp_sum = nums[left] + nums[right]
        if tmp_sum < target:
            left += 1
        elif tmp_sum > target:
            right -= 1
        else:
            results.append([nums[left], nums[right]])
            left += 1
            
    return results


if __name__ == "__main__":
    nums = [0, -1, 2, -3, -3, 1, 9, 0]
    result = triplet_sum(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    
    nums = [-4, -4, -2, 0, 0, 1, 2, 3]
    result = triplet_sum(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    
    nums = [9, 0, -9]
    result = triplet_sum(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")