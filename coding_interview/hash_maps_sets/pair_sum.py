from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    digits: dict[int, int] = {}
    result: List[int] = []
    
    for i in range(len(nums)):
        # ni + nj = target -> nj = target - ni
        nj = target - nums[i]
        if nj in digits:
            result += [digits[nj], i]
            # remove key stored in result from digits
            digits.pop(nj)
        else:
            digits[nums[i]] = i
    return result
    